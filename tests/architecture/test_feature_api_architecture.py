from __future__ import annotations

from dataclasses import fields
from dataclasses import is_dataclass
import importlib
import inspect
import pkgutil
from pathlib import Path
import sys
from typing import Any
from typing import get_args
from typing import get_origin
from typing import get_type_hints

import mfm.application.features as features_pkg


def _iter_feature_classes() -> list[type]:
    classes: list[type] = []
    package_root = Path(features_pkg.__path__[0])
    candidate_modules: set[str] = set()

    for module_path in package_root.rglob("*.py"):
        if not module_path.is_file():
            continue

        relative = module_path.relative_to(package_root)
        if relative.name == "__init__.py":
            relative = relative.parent
        else:
            relative = relative.with_suffix("")

        if str(relative) in {"", "."}:
            continue

        parts = [part for part in relative.parts if part]
        candidate_modules.add(".".join((features_pkg.__name__, *parts)))

    for module_info in pkgutil.iter_modules(
        features_pkg.__path__,
        f"{features_pkg.__name__}.",
    ):
        candidate_modules.add(module_info.name)

    for module_name in sorted(candidate_modules):
        module = importlib.import_module(module_name)
        for name, obj in vars(module).items():
            if (
                inspect.isclass(obj)
                and obj.__module__ == module.__name__
                and name.endswith("Feature")
            ):
                classes.append(obj)
    return sorted(classes, key=lambda cls: f"{cls.__module__}.{cls.__name__}")


def _is_frozen_dataclass(tp: Any) -> bool:
    return is_dataclass(tp) and bool(getattr(tp, "__dataclass_params__", None).frozen)


def _unwrap_response_types(tp: Any) -> list[type]:
    origin = get_origin(tp)
    if origin in {list, tuple, set}:
        args = [arg for arg in get_args(tp) if arg is not Ellipsis]
        return [arg for arg in args if inspect.isclass(arg)]
    return [tp] if inspect.isclass(tp) else []


def _contains_domain_type(tp: Any) -> bool:
    origin = get_origin(tp)
    if origin is not None:
        return any(_contains_domain_type(arg) for arg in get_args(tp))

    if inspect.isclass(tp):
        return tp.__module__.startswith("mfm.domain")

    return False


def _contains_forbidden_boundary_type(tp: Any) -> str | None:
    """Return a short reason string if ``tp`` leaks a domain or SQLAlchemy type.

    Implements the Public API Standard's "Domain Boundary Rules" and
    "SQLAlchemy Boundary Rules": DTOs must not expose domain objects,
    ORM models, or SQLAlchemy sessions/query types.
    """

    origin = get_origin(tp)
    if origin is not None:
        for arg in get_args(tp):
            reason = _contains_forbidden_boundary_type(arg)
            if reason:
                return reason
        return None

    if inspect.isclass(tp):
        import enum

        if issubclass(tp, enum.Enum):
            # Enums are explicitly allowed by the Public API Standard,
            # regardless of which module they're declared in.
            return None

        module = tp.__module__
        if module.startswith("mfm.domain"):
            return f"domain type '{tp.__qualname__}' ({module})"
        if module.startswith("sqlalchemy") or module.startswith("mfm.database.models"):
            return f"SQLAlchemy/ORM type '{tp.__qualname__}' ({module})"

    return None


def _request_response_pairs() -> list[tuple[type, type, Any]]:
    pairs: list[tuple[type, type, Any]] = []
    for feature_cls in _iter_feature_classes():
        assert hasattr(feature_cls, "execute"), (
            f"{feature_cls.__module__}.{feature_cls.__name__} must define execute(request)"
        )

        signature = inspect.signature(feature_cls.execute)
        params = list(signature.parameters.values())

        assert len(params) == 2, (
            f"{feature_cls.__module__}.{feature_cls.__name__}.execute must take exactly one argument"
        )
        assert params[0].name == "self", (
            f"{feature_cls.__module__}.{feature_cls.__name__}.execute first parameter must be self"
        )
        assert params[1].name == "request", (
            f"{feature_cls.__module__}.{feature_cls.__name__}.execute must use parameter name 'request'"
        )
        assert params[1].annotation is not inspect.Signature.empty, (
            f"{feature_cls.__module__}.{feature_cls.__name__}.execute request must be type-annotated"
        )
        assert signature.return_annotation is not inspect.Signature.empty, (
            f"{feature_cls.__module__}.{feature_cls.__name__}.execute must define return type"
        )

        module_globals = vars(sys.modules[feature_cls.__module__])
        execute_hints = get_type_hints(
            feature_cls.execute,
            globalns=module_globals,
            localns=module_globals,
        )

        request_type = execute_hints.get("request", params[1].annotation)
        response_type = execute_hints.get("return", signature.return_annotation)
        pairs.append((feature_cls, request_type, response_type))

    return pairs


def test_features_have_execute_request_signature_and_docstring() -> None:
    feature_classes = _iter_feature_classes()
    assert feature_classes, "No Feature classes found in mfm.application.features"

    _ = _request_response_pairs()

    for feature_cls in feature_classes:
        assert inspect.getdoc(feature_cls), (
            f"{feature_cls.__module__}.{feature_cls.__name__} must have class documentation"
        )


def test_all_feature_requests_are_immutable_request_dtos() -> None:
    seen: set[type] = set()
    for feature_cls, request_type, _ in _request_response_pairs():
        if request_type in seen:
            continue
        seen.add(request_type)

        assert _is_frozen_dataclass(request_type), (
            f"{feature_cls.__module__}.{feature_cls.__name__} request "
            f"{getattr(request_type, '__name__', request_type)} must be an immutable dataclass"
        )
        assert getattr(request_type, "__name__", "").endswith("Request"), (
            f"{feature_cls.__module__}.{feature_cls.__name__} request type name must end with 'Request'"
        )


def test_all_feature_responses_are_immutable_response_dtos() -> None:
    checked: set[type] = set()
    for feature_cls, _, response_annotation in _request_response_pairs():
        response_types = _unwrap_response_types(response_annotation)
        assert response_types, (
            f"{feature_cls.__module__}.{feature_cls.__name__} must return Response DTO type(s)"
        )

        for response_type in response_types:
            if response_type in checked:
                continue
            checked.add(response_type)

            assert _is_frozen_dataclass(response_type), (
                f"{feature_cls.__module__}.{feature_cls.__name__} response "
                f"{getattr(response_type, '__name__', response_type)} must be an immutable dataclass"
            )
            assert getattr(response_type, "__name__", "").endswith("Response"), (
                f"{feature_cls.__module__}.{feature_cls.__name__} response type name must end with 'Response'"
            )


def test_feature_responses_do_not_expose_domain_types() -> None:
    checked: set[type] = set()

    for feature_cls, _, response_annotation in _request_response_pairs():
        for response_type in _unwrap_response_types(response_annotation):
            if response_type in checked:
                continue
            checked.add(response_type)

            module_globals = vars(sys.modules[response_type.__module__])
            hints = get_type_hints(response_type, globalns=module_globals, localns=module_globals)

            for field in fields(response_type):
                field_type = hints.get(field.name, field.type)
                assert not _contains_domain_type(field_type), (
                    f"{feature_cls.__module__}.{feature_cls.__name__} response field "
                    f"{response_type.__name__}.{field.name} exposes domain type"
                )


def test_feature_requests_do_not_expose_domain_or_sqlalchemy_types() -> None:
    """Public API Standard, backlog item 5: requests were previously unchecked.

    Only response DTOs were guarded against leaking domain/ORM types;
    request DTOs had no equivalent check at all.
    """

    checked: set[type] = set()

    for feature_cls, request_type, _ in _request_response_pairs():
        if request_type in checked:
            continue
        checked.add(request_type)

        if not is_dataclass(request_type):
            continue

        module_globals = vars(sys.modules[request_type.__module__])
        hints = get_type_hints(request_type, globalns=module_globals, localns=module_globals)

        for field in fields(request_type):
            field_type = hints.get(field.name, field.type)
            reason = _contains_forbidden_boundary_type(field_type)
            assert reason is None, (
                f"{feature_cls.__module__}.{feature_cls.__name__} request field "
                f"{request_type.__name__}.{field.name} exposes {reason}"
            )


def test_feature_responses_do_not_expose_sqlalchemy_types() -> None:
    """Public API Standard "SQLAlchemy Boundary Rules": no ORM/Session leakage."""

    checked: set[type] = set()

    for feature_cls, _, response_annotation in _request_response_pairs():
        for response_type in _unwrap_response_types(response_annotation):
            if response_type in checked:
                continue
            checked.add(response_type)

            module_globals = vars(sys.modules[response_type.__module__])
            hints = get_type_hints(response_type, globalns=module_globals, localns=module_globals)

            for field in fields(response_type):
                field_type = hints.get(field.name, field.type)
                reason = _contains_forbidden_boundary_type(field_type)
                assert reason is None or "domain type" in reason, (
                    f"{feature_cls.__module__}.{feature_cls.__name__} response field "
                    f"{response_type.__name__}.{field.name} exposes {reason}"
                )


def test_request_and_response_dataclasses_use_slots() -> None:
    """Public API Standard requires ``@dataclass(frozen=True, slots=True)``."""

    checked: set[type] = set()
    for feature_cls, request_type, response_annotation in _request_response_pairs():
        candidates = [request_type, *_unwrap_response_types(response_annotation)]
        for dto_type in candidates:
            if dto_type in checked or not is_dataclass(dto_type):
                continue
            checked.add(dto_type)

            assert getattr(dto_type, "__dataclass_params__", None) is not None
            has_slots = "__slots__" in dto_type.__dict__
            assert has_slots, (
                f"{feature_cls.__module__}.{feature_cls.__name__} DTO "
                f"{dto_type.__name__} must use @dataclass(slots=True)"
            )




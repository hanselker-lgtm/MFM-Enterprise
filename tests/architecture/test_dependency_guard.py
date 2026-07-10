from __future__ import annotations

import ast
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = PROJECT_ROOT / "src" / "mfm"


def _python_files(package_path: Path) -> list[Path]:
    if not package_path.exists():
        return []
    return sorted(path for path in package_path.rglob("*.py") if path.is_file())


def _module_name(path: Path) -> str:
    relative = path.relative_to(PROJECT_ROOT / "src")
    parts = list(relative.parts)
    if parts[-1] == "__init__.py":
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1][:-3]
    return ".".join(parts)


def _resolve_from_import(module_name: str, level: int, imported_module: str | None) -> str:
    package_parts = module_name.split(".")[:-1]
    cut = max(level - 1, 0)
    anchor_parts = package_parts[: len(package_parts) - cut] if cut <= len(package_parts) else []
    if imported_module:
        return ".".join(anchor_parts + imported_module.split("."))
    return ".".join(anchor_parts)


def _imports_in_file(path: Path) -> set[str]:
    module_name = _module_name(path)
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imported: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imported.add(_resolve_from_import(module_name, node.level, node.module))

    return imported


def _matches_prefix(import_name: str, prefix: str) -> bool:
    return import_name == prefix or import_name.startswith(f"{prefix}.")


def _violations(package: str, forbidden_prefixes: tuple[str, ...]) -> list[str]:
    package_path = SRC_ROOT / package.replace(".", "/")
    violations: list[str] = []

    for file_path in _python_files(package_path):
        for imported in sorted(_imports_in_file(file_path)):
            if any(_matches_prefix(imported, prefix) for prefix in forbidden_prefixes):
                violations.append(
                    f"{file_path.relative_to(PROJECT_ROOT)} imports forbidden dependency '{imported}'"
                )

    return violations


def test_domain_must_not_depend_on_application_features_infrastructure_or_sqlalchemy() -> None:
    violations = _violations(
        "domain",
        (
            "mfm.application",
            "mfm.application.features",
            "mfm.database",
            "sqlalchemy",
        ),
    )
    assert not violations, "\n".join(violations)


def test_application_must_not_depend_on_gui() -> None:
    violations = _violations("application", ("mfm.gui",))
    assert not violations, "\n".join(violations)


def test_feature_layer_must_not_depend_on_sqlalchemy_models() -> None:
    violations = _violations(
        "application.features",
        (
            "mfm.database.models",
            "sqlalchemy",
        ),
    )
    assert not violations, "\n".join(violations)


def test_persistence_must_not_depend_on_gui() -> None:
    violations = _violations("database", ("mfm.gui",))
    assert not violations, "\n".join(violations)


def test_gui_may_only_depend_on_features() -> None:
    gui_path = SRC_ROOT / "gui"
    violations: list[str] = []

    for file_path in _python_files(gui_path):
        for imported in sorted(_imports_in_file(file_path)):
            if not _matches_prefix(imported, "mfm"):
                continue
            if _matches_prefix(imported, "mfm.gui"):
                continue
            if _matches_prefix(imported, "mfm.application.features"):
                continue
            violations.append(
                f"{file_path.relative_to(PROJECT_ROOT)} imports non-feature dependency '{imported}'"
            )

    assert not violations, "\n".join(violations)


def test_repository_interfaces_must_not_depend_on_sqlalchemy() -> None:
    violations = _violations("repositories", ("sqlalchemy",))
    assert not violations, "\n".join(violations)

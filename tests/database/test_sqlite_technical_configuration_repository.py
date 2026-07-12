from __future__ import annotations

from datetime import date
import weakref
from uuid import UUID
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.technical_configuration.component_link_role import ComponentLinkRole
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
)
from mfm.domain.technical_configuration.technical_configuration_status import (
    TechnicalConfigurationStatus,
)
from mfm.domain.technical_configuration.technical_specification import (
    SpecificationEntry,
)
from mfm.domain.technical_configuration.technical_specification import (
    TechnicalSpecification,
)
from mfm.domain.technical_configuration.value_objects import BuildYear
from mfm.domain.technical_configuration.value_objects import ComponentModelName
from mfm.domain.technical_configuration.value_objects import ComponentNotes
from mfm.domain.technical_configuration.value_objects import ManufacturerName
from mfm.domain.technical_configuration.value_objects import ReplacementReason
from mfm.domain.technical_configuration.value_objects import SerialNumber
from mfm.infrastructure.persistence.sqlite.sqlite_technical_configuration_repository import (
    SQLiteTechnicalConfigurationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return engine, session


def _create_uow(session: Session) -> UnitOfWork:
    return UnitOfWork(session)


def _build_configuration(vessel_id: UUID | None = None) -> TechnicalConfiguration:
    configuration = TechnicalConfiguration(vessel_id=vessel_id or uuid4())
    install_date = date(2022, 2, 1)

    engine = TechnicalComponent(
        component_type=TechnicalComponentType.PROPULSION_ENGINE,
        name="Propulsion Engine",
        manufacturer=ManufacturerName("Maker A"),
        model=ComponentModelName("E-100"),
        serial_number=SerialNumber("ENG-001"),
        build_year=BuildYear(2021),
        installed_date=install_date,
        status=TechnicalComponentStatus.INSTALLED,
        notes=ComponentNotes("Primary propulsion engine"),
        specification=TechnicalSpecification(
            schema_key="ENGINE_V1",
            entries=(
                SpecificationEntry(key="power_kw", value=2400, unit="kW"),
                SpecificationEntry(key="rpm", value=720, unit="rpm"),
            ),
        ),
    )

    gearbox_a = TechnicalComponent(
        component_type=TechnicalComponentType.GEARBOX,
        name="Gear Arrangement A",
        serial_number=SerialNumber("GEAR-001"),
        installed_date=install_date,
        status=TechnicalComponentStatus.INSTALLED,
    )

    shaft = TechnicalComponent(
        component_type=TechnicalComponentType.SHAFT,
        name="Shaft",
        installed_date=install_date,
        status=TechnicalComponentStatus.INSTALLED,
    )

    propeller = TechnicalComponent(
        component_type=TechnicalComponentType.PROPELLER,
        name="Controllable Pitch Propeller",
        installed_date=install_date,
        status=TechnicalComponentStatus.INSTALLED,
    )

    configuration.add_component(engine)
    configuration.add_component(gearbox_a)
    configuration.add_component(shaft)
    configuration.add_component(propeller)

    engine_to_gear = configuration.link_components(
        engine.id,
        gearbox_a.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=install_date,
    )
    gear_to_shaft = configuration.link_components(
        gearbox_a.id,
        shaft.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=install_date,
    )
    configuration.link_components(
        shaft.id,
        propeller.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=install_date,
    )

    replaced_on = date(2025, 1, 10)
    gearbox_b = TechnicalComponent(
        component_type=TechnicalComponentType.GEARBOX,
        name="Gear Arrangement B",
        serial_number=SerialNumber("GEAR-002"),
        status=TechnicalComponentStatus.PLANNED,
        specification=TechnicalSpecification(
            schema_key="GEARBOX_V1",
            entries=(SpecificationEntry(key="ratio", value=4.1),),
        ),
    )

    configuration.replace_component(
        gearbox_a.id,
        gearbox_b,
        replaced_on,
        reason=ReplacementReason("Wear"),
        notes=ComponentNotes("Planned replacement"),
    )

    configuration.close_component_link(engine_to_gear.id, replaced_on)
    configuration.close_component_link(gear_to_shaft.id, replaced_on)

    configuration.link_components(
        engine.id,
        gearbox_b.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=replaced_on,
    )
    configuration.link_components(
        gearbox_b.id,
        shaft.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=replaced_on,
    )

    configuration.activate()
    return configuration


def test_technical_configuration_repository_add_and_get_by_id() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    loaded = repository.get_by_id(configuration.id.value)

    assert loaded is not None
    assert loaded.id == configuration.id
    assert loaded.vessel_id == configuration.vessel_id


def test_technical_configuration_repository_get_by_vessel_id() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    loaded = repository.get_by_vessel_id(configuration.vessel_id)

    assert loaded is not None
    assert loaded.id == configuration.id


def test_technical_configuration_repository_not_found_behaviour() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))
    missing_id = uuid4()

    assert repository.get_by_id(missing_id) is None
    assert repository.get_by_vessel_id(uuid4()) is None


def test_technical_configuration_repository_exists_true_and_false() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    assert repository.exists(configuration.id.value) is True
    assert repository.exists(uuid4()) is False


def test_technical_configuration_repository_list_and_search() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    first = _build_configuration()
    second = _build_configuration()
    second.update_component_details(
        next(
            component.id
            for component in second.current_components(
                component_type=TechnicalComponentType.PROPULSION_ENGINE
            )
        ),
        name="Auxiliary Search Marker",
    )

    repository.add(first)
    repository.add(second)
    session.commit()

    items = repository.list()
    assert len(items) == 2
    assert all(isinstance(item, TechnicalConfiguration) for item in items)

    hits = repository.search("Search Marker")
    assert len(hits) == 1
    assert hits[0].id == second.id


def test_technical_configuration_repository_update_preserves_historical_components() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    configuration.archive()
    repository.update(configuration)
    session.commit()

    loaded = repository.get_by_id(configuration.id.value)
    assert loaded is not None
    assert loaded.status is TechnicalConfigurationStatus.ARCHIVED

    historical = [
        component
        for component in loaded.historical_components()
        if component.component_type is TechnicalComponentType.GEARBOX
    ]
    assert len(historical) == 1
    assert historical[0].name == "Gear Arrangement A"

    current = loaded.current_components(component_type=TechnicalComponentType.GEARBOX)
    assert len(current) == 1
    assert current[0].name == "Gear Arrangement B"


def test_technical_configuration_repository_delete() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    repository.delete(configuration.id.value)
    session.commit()

    assert repository.get_by_id(configuration.id.value) is None
    assert repository.exists(configuration.id.value) is False


def test_technical_configuration_repository_duplicate_vessel_handling() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    vessel_id = uuid4()
    first = _build_configuration(vessel_id=vessel_id)
    second = _build_configuration(vessel_id=vessel_id)

    repository.add(first)
    session.commit()

    try:
        repository.add(second)
    except ValueError as exc:
        assert "already exists" in str(exc)
    else:  # pragma: no cover - defensive
        raise AssertionError("Expected duplicate vessel configuration ValueError")


def test_technical_configuration_repository_historical_replacement_roundtrip() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    loaded = repository.get_by_id(configuration.id.value)
    assert loaded is not None

    all_components = loaded.list_components()
    assert len(all_components) == 5

    historical = [
        component
        for component in loaded.historical_components()
        if component.component_type is TechnicalComponentType.GEARBOX
    ]
    assert len(historical) == 1
    assert historical[0].status is TechnicalComponentStatus.REMOVED
    assert historical[0].replacement_successor_id is not None

    replacement_history = loaded.replacement_history()
    assert len(replacement_history) == 1
    assert replacement_history[0].replaced_component_id == historical[0].id


def test_technical_configuration_repository_vessel_id_preserved() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    vessel_id = uuid4()
    configuration = _build_configuration(vessel_id=vessel_id)
    repository.add(configuration)
    session.commit()

    loaded = repository.get_by_id(configuration.id.value)
    assert loaded is not None
    assert loaded.vessel_id == vessel_id


def test_technical_configuration_repository_propulsion_chain_roundtrip() -> None:
    _, session = _create_session()
    repository = SQLiteTechnicalConfigurationRepository(_create_uow(session))

    configuration = _build_configuration()
    repository.add(configuration)
    session.commit()

    loaded = repository.get_by_id(configuration.id.value)
    assert loaded is not None

    engine = next(
        component
        for component in loaded.current_components(
            component_type=TechnicalComponentType.PROPULSION_ENGINE
        )
    )

    chain = loaded.get_downstream_chain(engine.id)

    assert [component.name for component in chain] == [
        "Propulsion Engine",
        "Gear Arrangement B",
        "Shaft",
        "Controllable Pitch Propeller",
    ]

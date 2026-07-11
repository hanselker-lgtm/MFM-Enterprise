from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.technical_configuration.component_link_role import ComponentLinkRole
from mfm.domain.technical_configuration.exceptions import DuplicateTechnicalComponentError
from mfm.domain.technical_configuration.exceptions import InvalidChronologyError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentLifecycleError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentTypeError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalConfigurationVesselIdError
from mfm.domain.technical_configuration.exceptions import TechnicalComponentAlreadyInstalledError
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId
from mfm.domain.technical_configuration.identifiers import TechnicalConfigurationId
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_component_status import TechnicalComponentStatus
from mfm.domain.technical_configuration.technical_component_type import TechnicalComponentType
from mfm.domain.technical_configuration.technical_configuration import TechnicalConfiguration
from mfm.domain.technical_configuration.technical_specification import SpecificationEntry
from mfm.domain.technical_configuration.technical_specification import TechnicalSpecification


def _planned_component(
    *,
    component_type: TechnicalComponentType,
    name: str,
    serial_number: str,
) -> TechnicalComponent:
    return TechnicalComponent(
        component_type=component_type,
        name=name,
        serial_number=serial_number,
        specification=TechnicalSpecification(
            schema_key=f"{component_type.value}_V1",
            entries=(
                SpecificationEntry(key="manufacturer", value="Generic"),
            ),
        ),
    )


def test_create_technical_configuration() -> None:
    vessel_id = uuid4()
    config = TechnicalConfiguration(vessel_id=vessel_id)

    assert isinstance(config.id, TechnicalConfigurationId)
    assert config.vessel_id == vessel_id
    assert config.list_components() == ()


def test_invalid_vessel_identity() -> None:
    with pytest.raises(InvalidTechnicalConfigurationVesselIdError):
        TechnicalConfiguration(vessel_id="bad")  # type: ignore[arg-type]


def test_add_component() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    engine = _planned_component(
        component_type=TechnicalComponentType.PROPULSION_ENGINE,
        name="Main Engine",
        serial_number="SN-MAIN-001",
    )

    config.add_component(engine)

    loaded = config.get_component(engine.id)
    assert loaded is not None
    assert loaded.name == "Main Engine"


def test_duplicate_component_handling() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    shared_id = TechnicalComponentId.new()

    first = TechnicalComponent(
        id=shared_id,
        component_type=TechnicalComponentType.GEARBOX,
        name="Gearbox A",
        serial_number="GBX-001",
        specification=TechnicalSpecification(schema_key="GEARBOX_V1"),
    )
    second = TechnicalComponent(
        id=shared_id,
        component_type=TechnicalComponentType.GEARBOX,
        name="Gearbox B",
        serial_number="GBX-002",
        specification=TechnicalSpecification(schema_key="GEARBOX_V1"),
    )

    config.add_component(first)
    with pytest.raises(DuplicateTechnicalComponentError):
        config.add_component(second)


def test_install_component() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    pump = _planned_component(
        component_type=TechnicalComponentType.PUMP,
        name="Cooling Pump",
        serial_number="PUMP-001",
    )
    config.add_component(pump)

    config.install_component(pump.id, date(2026, 1, 10))

    installed = config.get_component(pump.id)
    assert installed is not None
    assert installed.status is TechnicalComponentStatus.INSTALLED
    assert installed.installed_date == date(2026, 1, 10)
    assert installed.is_current is True


def test_install_component_twice_is_invalid() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    generator = _planned_component(
        component_type=TechnicalComponentType.GENERATOR,
        name="Aux Generator",
        serial_number="GEN-001",
    )
    config.add_component(generator)
    config.install_component(generator.id, date(2026, 2, 1))

    with pytest.raises(TechnicalComponentAlreadyInstalledError):
        config.install_component(generator.id, date(2026, 2, 2))


def test_remove_component() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    tank = _planned_component(
        component_type=TechnicalComponentType.TANK,
        name="Fuel Tank",
        serial_number="TNK-001",
    )
    config.add_component(tank)
    config.install_component(tank.id, date(2025, 1, 1))

    config.remove_component(tank.id, date(2026, 1, 1))

    removed = config.get_component(tank.id)
    assert removed is not None
    assert removed.status is TechnicalComponentStatus.REMOVED
    assert removed.removed_date == date(2026, 1, 1)
    assert removed.is_current is False


def test_replace_component_and_preserve_history() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    original = _planned_component(
        component_type=TechnicalComponentType.PROPULSION_ENGINE,
        name="Engine Mk1",
        serial_number="ENG-001",
    )
    config.add_component(original)
    config.install_component(original.id, date(1998, 5, 1))

    replacement = _planned_component(
        component_type=TechnicalComponentType.PROPULSION_ENGINE,
        name="Engine Mk2",
        serial_number="ENG-002",
    )

    current = config.replace_component(
        original.id,
        replacement,
        date(2026, 6, 1),
        reason="major overhaul",
    )

    assert current.id == replacement.id

    old_state = config.get_component(original.id)
    new_state = config.get_component(replacement.id)
    assert old_state is not None and new_state is not None

    assert old_state.status is TechnicalComponentStatus.REMOVED
    assert old_state.removed_date == date(2026, 6, 1)
    assert old_state.replacement_successor_id == replacement.id
    assert old_state.is_current is False

    assert new_state.status is TechnicalComponentStatus.INSTALLED
    assert new_state.installed_date == date(2026, 6, 1)
    assert new_state.is_current is True

    history = config.replacement_history()
    assert len(history) == 1
    assert history[0].replaced_component_id == original.id
    assert history[0].replacement_component_id == replacement.id


def test_current_component_state_query() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())

    active = _planned_component(
        component_type=TechnicalComponentType.STEERING_GEAR,
        name="Steering",
        serial_number="STG-001",
    )
    retired = _planned_component(
        component_type=TechnicalComponentType.PUMP,
        name="Old Pump",
        serial_number="PUMP-OLD-001",
    )

    config.add_component(active)
    config.add_component(retired)
    config.install_component(active.id, date(2026, 1, 1))
    config.install_component(retired.id, date(2024, 1, 1))
    config.remove_component(retired.id, date(2025, 1, 1), retired=True)

    current = config.current_components()
    assert len(current) == 1
    assert current[0].id == active.id


def test_removed_component_state_query() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    shaft = _planned_component(
        component_type=TechnicalComponentType.SHAFT,
        name="Shaft A",
        serial_number="SHF-001",
    )
    config.add_component(shaft)
    config.install_component(shaft.id, date(2020, 1, 1))
    config.remove_component(shaft.id, date(2021, 1, 1))

    historical = config.historical_components()
    assert len(historical) == 1
    assert historical[0].id == shaft.id
    assert historical[0].status is TechnicalComponentStatus.REMOVED


def test_invalid_lifecycle_transition() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    propeller = _planned_component(
        component_type=TechnicalComponentType.PROPELLER,
        name="CPP",
        serial_number="PRP-001",
    )
    config.add_component(propeller)

    with pytest.raises(InvalidTechnicalComponentLifecycleError):
        config.remove_component(propeller.id, date(2026, 1, 1))


def test_chronological_date_validation() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())
    gearbox = _planned_component(
        component_type=TechnicalComponentType.GEARBOX,
        name="Gearbox",
        serial_number="GBX-CHRONO-001",
    )
    config.add_component(gearbox)
    config.install_component(gearbox.id, date(2026, 1, 10))

    with pytest.raises(InvalidChronologyError):
        config.remove_component(gearbox.id, date(2026, 1, 9))


def test_technical_component_type_validation() -> None:
    with pytest.raises(InvalidTechnicalComponentTypeError):
        TechnicalComponent(
            component_type="BAD_TYPE",  # type: ignore[arg-type]
            name="Invalid Type",
            serial_number="BAD-001",
            specification=TechnicalSpecification(schema_key="OTHER_V1"),
        )


def test_value_object_equality_and_immutability() -> None:
    left = TechnicalSpecification(
        schema_key="ENGINE_V1",
        entries=(
            SpecificationEntry(key="power", value=220, unit="kW"),
            SpecificationEntry(key="rpm", value=1800, unit="rpm"),
        ),
    )
    right = TechnicalSpecification(
        schema_key="engine_v1",
        entries=(
            SpecificationEntry(key="power", value=220, unit="kW"),
            SpecificationEntry(key="rpm", value=1800, unit="rpm"),
        ),
    )

    assert left == right
    assert left.get("POWER") == 220

    with pytest.raises(FrozenInstanceError):
        left.schema_key = "X"  # type: ignore[misc]


def test_propulsion_chain_design_scenario() -> None:
    config = TechnicalConfiguration(vessel_id=uuid4())

    engine = _planned_component(
        component_type=TechnicalComponentType.PROPULSION_ENGINE,
        name="Main Engine",
        serial_number="DRV-ENG-001",
    )
    gearbox = _planned_component(
        component_type=TechnicalComponentType.GEARBOX,
        name="Reversing Gear",
        serial_number="DRV-GBX-001",
    )
    shaft = _planned_component(
        component_type=TechnicalComponentType.SHAFT,
        name="Main Shaft",
        serial_number="DRV-SHF-001",
    )
    propeller = _planned_component(
        component_type=TechnicalComponentType.PROPELLER,
        name="CPP",
        serial_number="DRV-PRP-001",
    )

    for component in (engine, gearbox, shaft, propeller):
        config.add_component(component)
        config.install_component(component.id, date(2026, 1, 1))

    config.link_components(engine.id, gearbox.id, role=ComponentLinkRole.DRIVES)
    config.link_components(gearbox.id, shaft.id, role=ComponentLinkRole.COUPLED_TO)
    config.link_components(shaft.id, propeller.id, role=ComponentLinkRole.DRIVES)

    chain = config.get_downstream_chain(engine.id)

    assert len(chain) == 4
    assert [component.component_type for component in chain] == [
        TechnicalComponentType.PROPULSION_ENGINE,
        TechnicalComponentType.GEARBOX,
        TechnicalComponentType.SHAFT,
        TechnicalComponentType.PROPELLER,
    ]


def test_component_identity_is_stable() -> None:
    component = _planned_component(
        component_type=TechnicalComponentType.AUXILIARY_ENGINE,
        name="Aux Engine",
        serial_number="AUX-001",
    )
    initial_id = component.id

    component.update_details(name="Aux Engine Updated")

    assert component.id == initial_id
    assert isinstance(component.id.value, UUID)

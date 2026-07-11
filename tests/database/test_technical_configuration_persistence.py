from __future__ import annotations

from datetime import date
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.orm import Session

import mfm.database.models  # noqa: F401
from mfm.database.mappers.technical_configuration_mapper import TechnicalConfigurationMapper
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.technical_component_link_model import TechnicalComponentLinkModel
from mfm.database.models.technical_component_model import TechnicalComponentModel
from mfm.database.models.technical_component_replacement_model import (
    TechnicalComponentReplacementModel,
)
from mfm.database.models.technical_configuration_model import TechnicalConfigurationModel
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


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def _build_configuration_with_history() -> TechnicalConfiguration:
    configuration = TechnicalConfiguration(vessel_id=uuid4())
    base_install = date(2021, 1, 10)

    engine = TechnicalComponent(
        component_type=TechnicalComponentType.PROPULSION_ENGINE,
        name="Main Engine",
        manufacturer=ManufacturerName("Wartsila"),
        model=ComponentModelName("8L32"),
        serial_number=SerialNumber("ME-001"),
        build_year=BuildYear(2020),
        installed_date=base_install,
        status=TechnicalComponentStatus.INSTALLED,
        notes=ComponentNotes("Primary propulsion"),
        specification=TechnicalSpecification(
            schema_key="ENGINE_V1",
            entries=(
                SpecificationEntry(key="power_kw", value=2800, unit="kW"),
                SpecificationEntry(key="rpm", value=750, unit="rpm"),
            ),
        ),
    )

    gearbox_old = TechnicalComponent(
        component_type=TechnicalComponentType.GEARBOX,
        name="Gearbox Mk1",
        serial_number=SerialNumber("GB-001"),
        installed_date=base_install,
        status=TechnicalComponentStatus.INSTALLED,
    )

    shaft = TechnicalComponent(
        component_type=TechnicalComponentType.SHAFT,
        name="Shaft Line",
        installed_date=base_install,
        status=TechnicalComponentStatus.INSTALLED,
    )

    propeller = TechnicalComponent(
        component_type=TechnicalComponentType.PROPELLER,
        name="CPP Propeller",
        installed_date=base_install,
        status=TechnicalComponentStatus.INSTALLED,
    )

    configuration.add_component(engine)
    configuration.add_component(gearbox_old)
    configuration.add_component(shaft)
    configuration.add_component(propeller)

    engine_to_old = configuration.link_components(
        engine.id,
        gearbox_old.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=base_install,
    )
    old_to_shaft = configuration.link_components(
        gearbox_old.id,
        shaft.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=base_install,
    )
    configuration.link_components(
        shaft.id,
        propeller.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=base_install,
    )

    replacement_date = date(2024, 6, 1)
    gearbox_new = TechnicalComponent(
        component_type=TechnicalComponentType.GEARBOX,
        name="Gearbox Mk2",
        serial_number=SerialNumber("GB-002"),
        status=TechnicalComponentStatus.PLANNED,
        specification=TechnicalSpecification(
            schema_key="GEARBOX_V1",
            entries=(SpecificationEntry(key="ratio", value=4.2),),
        ),
    )
    configuration.replace_component(
        gearbox_old.id,
        gearbox_new,
        replacement_date,
        reason=ReplacementReason("Wear"),
        notes=ComponentNotes("Scheduled drydock replacement"),
    )

    configuration.close_component_link(engine_to_old.id, replacement_date)
    configuration.close_component_link(old_to_shaft.id, replacement_date)

    configuration.link_components(
        engine.id,
        gearbox_new.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=replacement_date,
    )
    configuration.link_components(
        gearbox_new.id,
        shaft.id,
        role=ComponentLinkRole.DRIVES,
        effective_from=replacement_date,
    )

    configuration.activate()
    return configuration


def test_technical_configuration_persistence_roundtrip() -> None:
    _, session = _create_session()
    configuration = _build_configuration_with_history()

    orm = TechnicalConfigurationMapper.to_orm_configuration(configuration)
    session.add(orm)
    session.commit()

    loaded = session.get(TechnicalConfigurationModel, orm.id)
    assert loaded is not None
    assert loaded.vessel_id == configuration.vessel_id
    assert loaded.status is TechnicalConfigurationStatus.ACTIVE
    assert len(loaded.components) == 5
    assert len(loaded.links) == 5
    assert len(loaded.replacements) == 1

    restored = TechnicalConfigurationMapper.to_domain_configuration(loaded)

    assert restored.id == configuration.id
    assert restored.vessel_id == configuration.vessel_id
    assert len(restored.list_components()) == 5
    assert len(restored.historical_components()) == 1
    assert len(restored.replacement_history()) == 1

    engine = next(
        component
        for component in restored.current_components(
            component_type=TechnicalComponentType.PROPULSION_ENGINE
        )
    )
    chain = restored.get_downstream_chain(engine.id)
    assert [component.name for component in chain] == [
        "Main Engine",
        "Gearbox Mk2",
        "Shaft Line",
        "CPP Propeller",
    ]


def test_technical_configuration_persistence_keeps_replaced_component_history() -> None:
    _, session = _create_session()
    configuration = _build_configuration_with_history()

    session.add(TechnicalConfigurationMapper.to_orm_configuration(configuration))
    session.commit()

    loaded = session.scalars(select(TechnicalConfigurationModel)).one()
    restored = TechnicalConfigurationMapper.to_domain_configuration(loaded)

    historical_gearboxes = [
        component
        for component in restored.historical_components()
        if component.component_type is TechnicalComponentType.GEARBOX
    ]
    assert len(historical_gearboxes) == 1
    assert historical_gearboxes[0].name == "Gearbox Mk1"
    assert historical_gearboxes[0].removed_date == date(2024, 6, 1)
    assert historical_gearboxes[0].replacement_successor_id is not None


def test_technical_configuration_delete_cascades_children() -> None:
    _, session = _create_session()
    configuration = _build_configuration_with_history()

    orm = TechnicalConfigurationMapper.to_orm_configuration(configuration)
    session.add(orm)
    session.commit()

    component_count = session.scalar(select(func.count()).select_from(TechnicalComponentModel))
    link_count = session.scalar(select(func.count()).select_from(TechnicalComponentLinkModel))
    replacement_count = session.scalar(
        select(func.count()).select_from(TechnicalComponentReplacementModel)
    )

    assert component_count == 5
    assert link_count == 5
    assert replacement_count == 1

    loaded = session.get(TechnicalConfigurationModel, orm.id)
    assert loaded is not None
    session.delete(loaded)
    session.commit()

    assert session.scalar(select(func.count()).select_from(TechnicalConfigurationModel)) == 0
    assert session.scalar(select(func.count()).select_from(TechnicalComponentModel)) == 0
    assert session.scalar(select(func.count()).select_from(TechnicalComponentLinkModel)) == 0
    assert session.scalar(select(func.count()).select_from(TechnicalComponentReplacementModel)) == 0

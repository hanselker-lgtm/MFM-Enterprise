"""Mapper between technical configuration domain and persistence models."""

from __future__ import annotations

from mfm.database.models.technical_component_link_model import (
    TechnicalComponentLinkModel,
)
from mfm.database.models.technical_component_model import TechnicalComponentModel
from mfm.database.models.technical_component_replacement_model import (
    TechnicalComponentReplacementModel,
)
from mfm.database.models.technical_configuration_model import (
    TechnicalConfigurationModel,
)
from mfm.domain.technical_configuration.component_link import ComponentLink
from mfm.domain.technical_configuration.component_replacement_record import (
    ComponentReplacementRecord,
)
from mfm.domain.technical_configuration.identifiers import ComponentLinkId
from mfm.domain.technical_configuration.identifiers import ComponentReplacementRecordId
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId
from mfm.domain.technical_configuration.identifiers import TechnicalConfigurationId
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
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


class TechnicalConfigurationMapper:
    """Map technical configuration aggregate to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_configuration(
        configuration: TechnicalConfiguration,
    ) -> TechnicalConfigurationModel:
        orm = TechnicalConfigurationModel(
            id=configuration.id.value,
            vessel_id=configuration.vessel_id,
            status=configuration.status,
        )

        for component in configuration.list_components():
            orm.components.append(
                TechnicalComponentModel(
                    id=component.id.value,
                    technical_configuration_id=configuration.id.value,
                    component_type=component.component_type,
                    name=component.name,
                    manufacturer=(
                        component.manufacturer.value
                        if component.manufacturer is not None
                        else None
                    ),
                    model=component.model.value if component.model is not None else None,
                    serial_number=(
                        component.serial_number.value
                        if component.serial_number is not None
                        else None
                    ),
                    build_year=(
                        component.build_year.value
                        if component.build_year is not None
                        else None
                    ),
                    installed_date=component.installed_date,
                    removed_date=component.removed_date,
                    status=component.status,
                    notes=component.notes.value if component.notes is not None else None,
                    specification_schema_key=component.specification.schema_key,
                    specification_entries=[
                        {
                            "key": entry.key,
                            "value": entry.value,
                            "unit": entry.unit,
                        }
                        for entry in component.specification.entries
                    ],
                    replacement_successor_component_id=(
                        component.replacement_successor_id.value
                        if component.replacement_successor_id is not None
                        else None
                    ),
                )
            )

        for link in configuration._links.values():
            orm.links.append(
                TechnicalComponentLinkModel(
                    id=link.id.value,
                    technical_configuration_id=configuration.id.value,
                    upstream_component_id=link.upstream_component_id.value,
                    downstream_component_id=link.downstream_component_id.value,
                    role=link.role,
                    effective_from=link.effective_from,
                    effective_to=link.effective_to,
                )
            )

        for replacement in configuration.replacement_history():
            orm.replacements.append(
                TechnicalComponentReplacementModel(
                    id=replacement.id.value,
                    technical_configuration_id=configuration.id.value,
                    replaced_component_id=replacement.replaced_component_id.value,
                    replacement_component_id=replacement.replacement_component_id.value,
                    replaced_on=replacement.replaced_on,
                    reason=replacement.reason.value,
                    notes=(replacement.notes.value if replacement.notes is not None else None),
                )
            )

        return orm

    @staticmethod
    def to_domain_configuration(
        orm: TechnicalConfigurationModel,
    ) -> TechnicalConfiguration:
        configuration = TechnicalConfiguration(
            id=TechnicalConfigurationId(orm.id),
            vessel_id=orm.vessel_id,
            status=orm.status,
        )

        for component_orm in orm.components:
            specification = TechnicalSpecification(
                schema_key=component_orm.specification_schema_key,
                entries=tuple(
                    SpecificationEntry(
                        key=str(entry.get("key", "")),
                        value=entry.get("value"),
                        unit=(
                            None
                            if entry.get("unit") is None
                            else str(entry.get("unit"))
                        ),
                    )
                    for entry in (component_orm.specification_entries or [])
                ),
            )

            component = TechnicalComponent(
                id=TechnicalComponentId(component_orm.id),
                component_type=component_orm.component_type,
                name=component_orm.name,
                manufacturer=(
                    ManufacturerName(component_orm.manufacturer)
                    if component_orm.manufacturer is not None
                    else None
                ),
                model=(
                    ComponentModelName(component_orm.model)
                    if component_orm.model is not None
                    else None
                ),
                serial_number=(
                    SerialNumber(component_orm.serial_number)
                    if component_orm.serial_number is not None
                    else None
                ),
                build_year=(
                    BuildYear(component_orm.build_year)
                    if component_orm.build_year is not None
                    else None
                ),
                installed_date=component_orm.installed_date,
                removed_date=component_orm.removed_date,
                status=component_orm.status,
                notes=(
                    ComponentNotes(component_orm.notes)
                    if component_orm.notes is not None
                    else None
                ),
                specification=specification,
                replacement_successor_id=(
                    TechnicalComponentId(component_orm.replacement_successor_component_id)
                    if component_orm.replacement_successor_component_id is not None
                    else None
                ),
            )
            configuration.add_component(component)

        for link_orm in orm.links:
            configuration._links[ComponentLinkId(link_orm.id)] = ComponentLink(
                id=ComponentLinkId(link_orm.id),
                upstream_component_id=TechnicalComponentId(link_orm.upstream_component_id),
                downstream_component_id=TechnicalComponentId(link_orm.downstream_component_id),
                role=link_orm.role,
                effective_from=link_orm.effective_from,
                effective_to=link_orm.effective_to,
            )

        for replacement_orm in orm.replacements:
            configuration._replacements.append(
                ComponentReplacementRecord(
                    id=ComponentReplacementRecordId(replacement_orm.id),
                    replaced_component_id=TechnicalComponentId(
                        replacement_orm.replaced_component_id
                    ),
                    replacement_component_id=TechnicalComponentId(
                        replacement_orm.replacement_component_id
                    ),
                    replaced_on=replacement_orm.replaced_on,
                    reason=ReplacementReason(replacement_orm.reason),
                    notes=(
                        ComponentNotes(replacement_orm.notes)
                        if replacement_orm.notes is not None
                        else None
                    ),
                )
            )

        return configuration

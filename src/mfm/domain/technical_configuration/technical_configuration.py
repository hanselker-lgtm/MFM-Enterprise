"""TechnicalConfiguration aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from uuid import UUID
from uuid import uuid4

from mfm.domain.technical_configuration.component_link import ComponentLink
from mfm.domain.technical_configuration.component_link_role import ComponentLinkRole
from mfm.domain.technical_configuration.component_replacement_record import (
    ComponentReplacementRecord,
)
from mfm.domain.technical_configuration.exceptions import ComponentLinkNotFoundError
from mfm.domain.technical_configuration.exceptions import DuplicateTechnicalComponentError
from mfm.domain.technical_configuration.exceptions import InvalidComponentLinkError
from mfm.domain.technical_configuration.exceptions import InvalidReplacementRelationError
from mfm.domain.technical_configuration.exceptions import (
    InvalidTechnicalConfigurationStatusTransitionError,
)
from mfm.domain.technical_configuration.exceptions import (
    InvalidTechnicalConfigurationVesselIdError,
)
from mfm.domain.technical_configuration.exceptions import TechnicalComponentNotFoundError
from mfm.domain.technical_configuration.identifiers import ComponentLinkId
from mfm.domain.technical_configuration.identifiers import ComponentReplacementRecordId
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId
from mfm.domain.technical_configuration.identifiers import TechnicalConfigurationId
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.domain.technical_configuration.technical_configuration_status import (
    TechnicalConfigurationStatus,
)
from mfm.domain.technical_configuration.value_objects import ComponentNotes
from mfm.domain.technical_configuration.value_objects import ReplacementReason


@dataclass(slots=True)
class TechnicalConfiguration:
    """Aggregate root for vessel technical configuration and history."""

    id: TechnicalConfigurationId = field(default_factory=TechnicalConfigurationId.new)
    vessel_id: UUID = field(default_factory=uuid4)
    status: TechnicalConfigurationStatus = TechnicalConfigurationStatus.DRAFT
    _components: dict[TechnicalComponentId, TechnicalComponent] = field(
        default_factory=dict,
        init=False,
        repr=False,
    )
    _links: dict[ComponentLinkId, ComponentLink] = field(
        default_factory=dict,
        init=False,
        repr=False,
    )
    _replacements: list[ComponentReplacementRecord] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        if not isinstance(self.id, TechnicalConfigurationId):
            self.id = TechnicalConfigurationId(self.id)
        if not isinstance(self.vessel_id, UUID):
            raise InvalidTechnicalConfigurationVesselIdError("vessel_id must be UUID")
        if not isinstance(self.status, TechnicalConfigurationStatus):
            self.status = TechnicalConfigurationStatus(str(self.status).upper())

    def activate(self) -> None:
        if self.status is TechnicalConfigurationStatus.ARCHIVED:
            raise InvalidTechnicalConfigurationStatusTransitionError(
                "archived configuration cannot be activated"
            )
        self.status = TechnicalConfigurationStatus.ACTIVE

    def archive(self) -> None:
        self.status = TechnicalConfigurationStatus.ARCHIVED

    def add_component(self, component: TechnicalComponent) -> None:
        if not isinstance(component, TechnicalComponent):
            raise TypeError("component must be TechnicalComponent")

        if component.id in self._components:
            raise DuplicateTechnicalComponentError(
                f"component {component.id.value} already exists"
            )

        if component.serial_number is not None and component.is_current:
            for existing in self._components.values():
                if not existing.is_current:
                    continue
                if existing.serial_number == component.serial_number:
                    raise DuplicateTechnicalComponentError(
                        f"current serial {component.serial_number.value} already exists"
                    )

        self._components[component.id] = component

    def get_component(self, component_id: TechnicalComponentId | UUID | str) -> TechnicalComponent | None:
        identifier = self._normalize_component_id(component_id)
        return self._components.get(identifier)

    def install_component(
        self,
        component_id: TechnicalComponentId | UUID | str,
        installed_on: date,
    ) -> None:
        component = self._require_component(component_id)
        component.install(installed_on)

    def remove_component(
        self,
        component_id: TechnicalComponentId | UUID | str,
        removed_on: date,
        *,
        retired: bool = False,
    ) -> None:
        component = self._require_component(component_id)
        component.remove(removed_on, retired=retired)

    def replace_component(
        self,
        component_id: TechnicalComponentId | UUID | str,
        replacement_component: TechnicalComponent,
        replaced_on: date,
        *,
        reason: ReplacementReason | str,
        notes: ComponentNotes | str | None = None,
    ) -> TechnicalComponent:
        replaced = self._require_component(component_id)
        if not replaced.is_current:
            raise InvalidReplacementRelationError("only current component can be replaced")

        if not isinstance(replacement_component, TechnicalComponent):
            raise TypeError("replacement_component must be TechnicalComponent")
        if replacement_component.id in self._components:
            raise DuplicateTechnicalComponentError(
                f"component {replacement_component.id.value} already exists"
            )

        replacement_component.install(replaced_on)
        replaced.mark_replaced_by(replacement_component.id)
        replaced.remove(replaced_on)

        self.add_component(replacement_component)

        replacement_reason = (
            reason if isinstance(reason, ReplacementReason) else ReplacementReason(str(reason))
        )
        replacement_notes = None
        if notes is not None:
            replacement_notes = notes if isinstance(notes, ComponentNotes) else ComponentNotes(str(notes))

        self._replacements.append(
            ComponentReplacementRecord(
                id=ComponentReplacementRecordId.new(),
                replaced_component_id=replaced.id,
                replacement_component_id=replacement_component.id,
                replaced_on=replaced_on,
                reason=replacement_reason,
                notes=replacement_notes,
            )
        )

        return replacement_component

    def update_component_details(
        self,
        component_id: TechnicalComponentId | UUID | str,
        **kwargs,
    ) -> None:
        component = self._require_component(component_id)
        component.update_details(**kwargs)

    def link_components(
        self,
        upstream_component_id: TechnicalComponentId | UUID | str,
        downstream_component_id: TechnicalComponentId | UUID | str,
        *,
        role: ComponentLinkRole,
        effective_from: date | None = None,
        effective_to: date | None = None,
    ) -> ComponentLink:
        upstream = self._normalize_component_id(upstream_component_id)
        downstream = self._normalize_component_id(downstream_component_id)

        if upstream not in self._components:
            raise TechnicalComponentNotFoundError(f"component {upstream.value} not found")
        if downstream not in self._components:
            raise TechnicalComponentNotFoundError(f"component {downstream.value} not found")

        if upstream == downstream:
            raise InvalidComponentLinkError("component cannot link to itself")

        for existing in self._links.values():
            if (
                existing.upstream_component_id == upstream
                and existing.downstream_component_id == downstream
                and existing.role == role
                and existing.is_active
            ):
                raise InvalidComponentLinkError(
                    "an active identical link already exists"
                )

        link = ComponentLink(
            id=ComponentLinkId.new(),
            upstream_component_id=upstream,
            downstream_component_id=downstream,
            role=role,
            effective_from=effective_from,
            effective_to=effective_to,
        )
        self._links[link.id] = link
        return link

    def close_component_link(
        self,
        link_id: ComponentLinkId | UUID | str,
        closed_on: date,
    ) -> None:
        identifier = self._normalize_link_id(link_id)
        link = self._links.get(identifier)
        if link is None:
            raise ComponentLinkNotFoundError(f"link {identifier.value} not found")
        link.close(closed_on)

    def list_components(self) -> tuple[TechnicalComponent, ...]:
        return tuple(self._components.values())

    def current_components(
        self,
        *,
        component_type: TechnicalComponentType | None = None,
    ) -> tuple[TechnicalComponent, ...]:
        components = [component for component in self._components.values() if component.is_current]
        if component_type is None:
            return tuple(components)
        return tuple(
            component
            for component in components
            if component.component_type is component_type
        )

    def historical_components(self) -> tuple[TechnicalComponent, ...]:
        return tuple(
            component
            for component in self._components.values()
            if component.removed_date is not None or component.replacement_successor_id is not None
        )

    def replacement_history(self) -> tuple[ComponentReplacementRecord, ...]:
        return tuple(self._replacements)

    def get_downstream_chain(
        self,
        start_component_id: TechnicalComponentId | UUID | str,
    ) -> tuple[TechnicalComponent, ...]:
        current = self._normalize_component_id(start_component_id)
        if current not in self._components:
            raise TechnicalComponentNotFoundError(f"component {current.value} not found")

        chain: list[TechnicalComponent] = [self._components[current]]
        visited: set[TechnicalComponentId] = {current}

        while True:
            next_links = [
                link
                for link in self._links.values()
                if link.upstream_component_id == current and link.is_active
            ]
            if not next_links:
                break
            next_id = next_links[0].downstream_component_id
            if next_id in visited:
                raise InvalidComponentLinkError("component link cycle detected")
            visited.add(next_id)
            chain.append(self._components[next_id])
            current = next_id

        return tuple(chain)

    def _require_component(
        self,
        component_id: TechnicalComponentId | UUID | str,
    ) -> TechnicalComponent:
        identifier = self._normalize_component_id(component_id)
        component = self._components.get(identifier)
        if component is None:
            raise TechnicalComponentNotFoundError(f"component {identifier.value} not found")
        return component

    @staticmethod
    def _normalize_component_id(
        component_id: TechnicalComponentId | UUID | str,
    ) -> TechnicalComponentId:
        return component_id if isinstance(component_id, TechnicalComponentId) else TechnicalComponentId(component_id)

    @staticmethod
    def _normalize_link_id(link_id: ComponentLinkId | UUID | str) -> ComponentLinkId:
        return link_id if isinstance(link_id, ComponentLinkId) else ComponentLinkId(link_id)

"""Technical component structural link entity."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.domain.technical_configuration.component_link_role import ComponentLinkRole
from mfm.domain.technical_configuration.exceptions import InvalidChronologyError
from mfm.domain.technical_configuration.exceptions import InvalidComponentLinkError
from mfm.domain.technical_configuration.identifiers import ComponentLinkId
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId


@dataclass(slots=True)
class ComponentLink:
    """Structural relationship between two components in one configuration."""

    id: ComponentLinkId
    upstream_component_id: TechnicalComponentId
    downstream_component_id: TechnicalComponentId
    role: ComponentLinkRole
    effective_from: date | None = None
    effective_to: date | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.id, ComponentLinkId):
            self.id = ComponentLinkId(self.id)
        if not isinstance(self.upstream_component_id, TechnicalComponentId):
            self.upstream_component_id = TechnicalComponentId(self.upstream_component_id)
        if not isinstance(self.downstream_component_id, TechnicalComponentId):
            self.downstream_component_id = TechnicalComponentId(self.downstream_component_id)
        if self.upstream_component_id == self.downstream_component_id:
            raise InvalidComponentLinkError("upstream and downstream component cannot be same")

        if not isinstance(self.role, ComponentLinkRole):
            try:
                self.role = ComponentLinkRole(str(self.role).upper())
            except Exception as exc:
                raise InvalidComponentLinkError("invalid component link role") from exc

        if self.effective_from is not None and not isinstance(self.effective_from, date):
            raise InvalidComponentLinkError("effective_from must be date or None")
        if self.effective_to is not None and not isinstance(self.effective_to, date):
            raise InvalidComponentLinkError("effective_to must be date or None")
        if self.effective_from is not None and self.effective_to is not None:
            if self.effective_to < self.effective_from:
                raise InvalidChronologyError("effective_to cannot be before effective_from")

    def close(self, closed_on: date) -> None:
        if not isinstance(closed_on, date):
            raise InvalidComponentLinkError("closed_on must be date")
        if self.effective_from is not None and closed_on < self.effective_from:
            raise InvalidChronologyError("closed_on cannot be before effective_from")
        if self.effective_to is not None and closed_on < self.effective_to:
            raise InvalidChronologyError("closed_on cannot move effective_to backwards")
        self.effective_to = closed_on

    @property
    def is_active(self) -> bool:
        return self.effective_to is None

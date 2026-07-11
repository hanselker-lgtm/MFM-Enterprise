"""Component replacement history entity."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.domain.technical_configuration.exceptions import InvalidChronologyError
from mfm.domain.technical_configuration.exceptions import InvalidReplacementRelationError
from mfm.domain.technical_configuration.identifiers import ComponentReplacementRecordId
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId
from mfm.domain.technical_configuration.value_objects import ComponentNotes
from mfm.domain.technical_configuration.value_objects import ReplacementReason


@dataclass(slots=True)
class ComponentReplacementRecord:
    """Historical replacement relation from one component to another."""

    id: ComponentReplacementRecordId
    replaced_component_id: TechnicalComponentId
    replacement_component_id: TechnicalComponentId
    replaced_on: date
    reason: ReplacementReason
    notes: ComponentNotes | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.id, ComponentReplacementRecordId):
            self.id = ComponentReplacementRecordId(self.id)
        if not isinstance(self.replaced_component_id, TechnicalComponentId):
            self.replaced_component_id = TechnicalComponentId(self.replaced_component_id)
        if not isinstance(self.replacement_component_id, TechnicalComponentId):
            self.replacement_component_id = TechnicalComponentId(
                self.replacement_component_id
            )
        if self.replaced_component_id == self.replacement_component_id:
            raise InvalidReplacementRelationError("replacement cannot target same component")
        if not isinstance(self.replaced_on, date):
            raise InvalidChronologyError("replaced_on must be date")

        if not isinstance(self.reason, ReplacementReason):
            self.reason = ReplacementReason(str(self.reason))

        if self.notes is not None and not isinstance(self.notes, ComponentNotes):
            self.notes = ComponentNotes(str(self.notes))

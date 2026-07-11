"""MaintenancePlan aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from uuid import UUID

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.maintenance.events import MaintenanceBecameDue
from mfm.domain.maintenance.events import MaintenanceRequirementCreated
from mfm.domain.maintenance.exceptions import DuplicateMaintenanceRequirementError
from mfm.domain.maintenance.exceptions import InvalidMaintenancePlanStateError
from mfm.domain.maintenance.exceptions import MaintenanceRequirementNotFoundError
from mfm.domain.maintenance.identifiers import MaintenancePlanId
from mfm.domain.maintenance.identifiers import MaintenanceRequirementId
from mfm.domain.maintenance.maintenance_plan_status import MaintenancePlanStatus
from mfm.domain.maintenance.maintenance_requirement import MaintenanceRequirement
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget


@dataclass(slots=True)
class MaintenancePlan(AggregateRoot):
    """Aggregate root for maintenance planning and requirement invariants."""

    maintenance_target: MaintenanceTarget
    id: MaintenancePlanId = field(default_factory=MaintenancePlanId.new)
    status: MaintenancePlanStatus = MaintenancePlanStatus.DRAFT
    _requirements: dict[MaintenanceRequirementId, MaintenanceRequirement] = field(
        default_factory=dict,
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, MaintenancePlanId):
            self.id = MaintenancePlanId(self.id)
        if not isinstance(self.maintenance_target, MaintenanceTarget):
            raise InvalidMaintenancePlanStateError(
                "maintenance_target must be MaintenanceTarget"
            )

        if not isinstance(self.status, MaintenancePlanStatus):
            self.status = MaintenancePlanStatus(str(self.status).upper())

    def activate(self) -> None:
        if self.status is MaintenancePlanStatus.ARCHIVED:
            raise InvalidMaintenancePlanStateError(
                "archived maintenance plan cannot be activated"
            )
        self.status = MaintenancePlanStatus.ACTIVE

    def archive(self) -> None:
        self.status = MaintenancePlanStatus.ARCHIVED

    def add_requirement(self, requirement: MaintenanceRequirement) -> None:
        if self.status is MaintenancePlanStatus.ARCHIVED:
            raise InvalidMaintenancePlanStateError(
                "cannot add requirement to archived maintenance plan"
            )
        if not isinstance(requirement, MaintenanceRequirement):
            raise TypeError("requirement must be MaintenanceRequirement")

        if requirement.maintenance_target != self.maintenance_target:
            raise InvalidMaintenancePlanStateError(
                "requirement maintenance_target must match plan maintenance_target"
            )

        if requirement.id in self._requirements:
            raise DuplicateMaintenanceRequirementError(
                f"requirement {requirement.id.value} already exists"
            )

        signature = requirement.signature()
        for existing in self._requirements.values():
            if existing.signature() == signature:
                raise DuplicateMaintenanceRequirementError(
                    "duplicate requirement signature in maintenance plan"
                )

        self._requirements[requirement.id] = requirement
        self.add_event(
            MaintenanceRequirementCreated(
                requirement_id=requirement.id.value,
                maintenance_plan_id=self.id.value,
            )
        )

    def get_requirement(
        self,
        requirement_id: MaintenanceRequirementId | UUID | str,
    ) -> MaintenanceRequirement | None:
        identifier = self._normalize_requirement_id(requirement_id)
        return self._requirements.get(identifier)

    def list_requirements(self) -> tuple[MaintenanceRequirement, ...]:
        return tuple(self._requirements.values())

    def update_requirement(
        self,
        requirement_id: MaintenanceRequirementId | UUID | str,
        **kwargs,
    ) -> None:
        requirement = self._require_requirement(requirement_id)
        requirement.update(**kwargs)

    def record_requirement_completion(
        self,
        requirement_id: MaintenanceRequirementId | UUID | str,
        *,
        completed_on: date | None = None,
        completed_running_hours: int | None = None,
    ) -> None:
        requirement = self._require_requirement(requirement_id)
        requirement.record_completion(
            completed_on=completed_on,
            completed_running_hours=completed_running_hours,
        )

    def calculate_due(
        self,
        *,
        as_of_date: date,
        running_hours_by_requirement_id: dict[UUID, int] | None = None,
    ) -> tuple[MaintenanceRequirement, ...]:
        due_requirements: list[MaintenanceRequirement] = []
        running_hours_by_requirement_id = running_hours_by_requirement_id or {}

        for requirement in self._requirements.values():
            current_hours = running_hours_by_requirement_id.get(requirement.id.value)
            if requirement.is_due(
                as_of_date=as_of_date,
                current_running_hours=current_hours,
            ):
                due_requirements.append(requirement)
                self.add_event(
                    MaintenanceBecameDue(
                        requirement_id=requirement.id.value,
                        maintenance_plan_id=self.id.value,
                    )
                )

        return tuple(due_requirements)

    def _require_requirement(
        self,
        requirement_id: MaintenanceRequirementId | UUID | str,
    ) -> MaintenanceRequirement:
        identifier = self._normalize_requirement_id(requirement_id)
        requirement = self._requirements.get(identifier)
        if requirement is None:
            raise MaintenanceRequirementNotFoundError(
                f"requirement {identifier.value} not found"
            )
        return requirement

    @staticmethod
    def _normalize_requirement_id(
        requirement_id: MaintenanceRequirementId | UUID | str,
    ) -> MaintenanceRequirementId:
        if isinstance(requirement_id, MaintenanceRequirementId):
            return requirement_id
        return MaintenanceRequirementId(requirement_id)

"""Project aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.projects.external_reference import ExternalReference
from mfm.domain.projects.events import ProjectArchived
from mfm.domain.projects.events import ProjectCreated
from mfm.domain.projects.events import ProjectStatusChanged
from mfm.domain.projects.events import ProjectUpdated
from mfm.domain.projects.exceptions import InvalidProjectError
from mfm.domain.projects.exceptions import InvalidProjectStateError
from mfm.domain.projects.project_activity import ProjectActivity
from mfm.domain.projects.project_assignment import ProjectAssignment
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_milestone import ProjectMilestone
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_status import ProjectStatus


@dataclass(slots=True)
class Project(AggregateRoot):
    """Aggregate root for cross-capability project governance."""

    project_number: ProjectNumber
    project_name: ProjectName
    id: ProjectId = field(default_factory=ProjectId.new)
    status: ProjectStatus = ProjectStatus.DRAFT
    priority: ProjectPriority = ProjectPriority.NORMAL
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    archived_at: datetime | None = None
    milestones: list[ProjectMilestone] = field(default_factory=list)
    activities: list[ProjectActivity] = field(default_factory=list)
    assignments: list[ProjectAssignment] = field(default_factory=list)
    references: list[ExternalReference] = field(default_factory=list)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        if not isinstance(self.project_number, ProjectNumber):
            self.project_number = ProjectNumber(self.project_number)

        if not isinstance(self.project_name, ProjectName):
            self.project_name = ProjectName(self.project_name)

        if not isinstance(self.status, ProjectStatus):
            self.status = ProjectStatus(str(self.status).upper())

        if not isinstance(self.priority, ProjectPriority):
            self.priority = ProjectPriority(str(self.priority).upper())

        self.description = self._normalize_optional_text(self.description)
        self.start_date = self._normalize_optional_datetime(self.start_date)
        self.end_date = self._normalize_optional_datetime(self.end_date)
        self.created_at = self._normalize_optional_datetime(self.created_at) or datetime.now(
            UTC
        )
        self.updated_at = self._normalize_optional_datetime(self.updated_at)
        self.archived_at = self._normalize_optional_datetime(self.archived_at)

        if self.start_date is not None and self.end_date is not None and self.start_date > self.end_date:
            raise InvalidProjectError("start_date cannot be after end_date")

        if self.status is ProjectStatus.ARCHIVED and self.archived_at is None:
            raise InvalidProjectStateError("archived projects require archived_at")

        if self.status is not ProjectStatus.ARCHIVED and self.archived_at is not None:
            raise InvalidProjectStateError("archived_at is only allowed for ARCHIVED status")

        self.milestones = [
            milestone
            if isinstance(milestone, ProjectMilestone)
            else ProjectMilestone(**milestone)
            for milestone in self.milestones
        ]
        self.activities = [
            activity
            if isinstance(activity, ProjectActivity)
            else ProjectActivity(**activity)
            for activity in self.activities
        ]
        self.assignments = [
            assignment
            if isinstance(assignment, ProjectAssignment)
            else ProjectAssignment(**assignment)
            for assignment in self.assignments
        ]
        self.references = [
            reference
            if isinstance(reference, ExternalReference)
            else ExternalReference(**reference)
            for reference in self.references
        ]

        self.add_event(ProjectCreated(project_id=self.id.value))

    def update_details(
        self,
        *,
        project_name: ProjectName | str | None = None,
        description: str | None = None,
        priority: ProjectPriority | str | None = None,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        """Update mutable project details while preserving aggregate invariants."""
        if project_name is not None:
            self.project_name = (
                project_name
                if isinstance(project_name, ProjectName)
                else ProjectName(project_name)
            )

        if priority is not None:
            self.priority = (
                priority if isinstance(priority, ProjectPriority) else ProjectPriority(str(priority).upper())
            )

        if description is not None:
            self.description = self._normalize_optional_text(description)

        if start_date is not None:
            self.start_date = self._normalize_optional_datetime(start_date)

        if end_date is not None:
            self.end_date = self._normalize_optional_datetime(end_date)

        if self.start_date is not None and self.end_date is not None and self.start_date > self.end_date:
            raise InvalidProjectError("start_date cannot be after end_date")

        self.updated_at = self._normalize_optional_datetime(updated_at) or datetime.now(UTC)
        self.add_event(ProjectUpdated(project_id=self.id.value))

    def change_status(self, status: ProjectStatus | str, *, when: datetime | None = None) -> None:
        """Change lifecycle state while enforcing allowed transitions."""
        new_status = status if isinstance(status, ProjectStatus) else ProjectStatus(str(status).upper())

        allowed_transitions: dict[ProjectStatus, set[ProjectStatus]] = {
            ProjectStatus.DRAFT: {ProjectStatus.PLANNED, ProjectStatus.ARCHIVED},
            ProjectStatus.PLANNED: {ProjectStatus.ACTIVE, ProjectStatus.ON_HOLD, ProjectStatus.ARCHIVED},
            ProjectStatus.ACTIVE: {ProjectStatus.ON_HOLD, ProjectStatus.COMPLETED, ProjectStatus.ARCHIVED},
            ProjectStatus.ON_HOLD: {ProjectStatus.ACTIVE, ProjectStatus.COMPLETED, ProjectStatus.ARCHIVED},
            ProjectStatus.COMPLETED: {ProjectStatus.ARCHIVED},
            ProjectStatus.ARCHIVED: set(),
        }

        if new_status is self.status:
            return

        if new_status not in allowed_transitions[self.status]:
            raise InvalidProjectStateError(
                f"invalid project status transition: {self.status} -> {new_status}"
            )

        previous_status = self.status
        changed_at = self._normalize_optional_datetime(when) or datetime.now(UTC)
        self.status = new_status
        self.updated_at = changed_at

        if new_status is ProjectStatus.ARCHIVED:
            self.archived_at = changed_at
            self.add_event(ProjectArchived(project_id=self.id.value, archived_at=changed_at))
        else:
            self.add_event(
                ProjectStatusChanged(
                    project_id=self.id.value,
                    previous_status=str(previous_status),
                    new_status=str(new_status),
                )
            )

    @staticmethod
    def _normalize_optional_text(value: str | None) -> str | None:
        if value is None:
            return None
        normalized = str(value).strip()
        return normalized or None

    @staticmethod
    def _normalize_optional_datetime(value: datetime | None) -> datetime | None:
        if value is None:
            return None
        if value.tzinfo is None:
            raise InvalidProjectError("datetime values must be timezone-aware")
        return value.astimezone(UTC)

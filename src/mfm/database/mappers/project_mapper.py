"""Mapper between projects domain and persistence models."""

from __future__ import annotations

from datetime import UTC
from datetime import datetime

from mfm.database.models.external_reference_model import ExternalReferenceModel
from mfm.database.models.project_activity_model import ProjectActivityModel
from mfm.database.models.project_assignment_model import ProjectAssignmentModel
from mfm.database.models.project_milestone_model import ProjectMilestoneModel
from mfm.database.models.project_model import ProjectModel
from mfm.domain.projects.external_reference import ExternalReference
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_activity import ProjectActivity
from mfm.domain.projects.project_assignment import ProjectAssignment
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_milestone import ProjectMilestone
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber


class ProjectMapper:
    """Map Project aggregate to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_project(project: Project) -> ProjectModel:
        orm = ProjectModel(
            id=project.id.value,
            project_number=project.project_number.value,
            project_name=project.project_name.value,
            description=project.description,
            status=project.status,
            priority=project.priority,
            start_date=project.start_date,
            end_date=project.end_date,
            project_created_at=project.created_at,
            project_updated_at=project.updated_at,
            archived_at=project.archived_at,
            version=project.version,
        )

        for milestone in project.milestones:
            orm.milestones.append(
                ProjectMilestoneModel(
                    id=milestone.id,
                    project_id=project.id.value,
                    sequence=milestone.sequence,
                    name=milestone.name,
                    description=milestone.description,
                    status=milestone.status,
                    due_date=milestone.due_date,
                    completed_date=milestone.completed_date,
                )
            )

        for activity_order, activity in enumerate(project.activities):
            orm.activities.append(
                ProjectActivityModel(
                    id=activity.id,
                    project_id=project.id.value,
                    activity_order=activity_order,
                    title=activity.title,
                    description=activity.description,
                    status=activity.status,
                    priority=activity.priority,
                    estimated_hours=activity.estimated_hours,
                    actual_hours=activity.actual_hours,
                    planned_start=activity.planned_start,
                    planned_finish=activity.planned_finish,
                    actual_start=activity.actual_start,
                    actual_finish=activity.actual_finish,
                )
            )

        for assignment in project.assignments:
            orm.assignments.append(
                ProjectAssignmentModel(
                    id=assignment.id,
                    project_id=project.id.value,
                    organisation_id=assignment.organisation_id,
                    contact_id=assignment.contact_id,
                    role=assignment.role,
                    assigned_from=assignment.assigned_from,
                    assigned_until=assignment.assigned_until,
                )
            )

        for reference_order, reference in enumerate(project.references):
            orm.references.append(
                ExternalReferenceModel(
                    id=reference.id,
                    project_id=project.id.value,
                    reference_order=reference_order,
                    reference_type=reference.reference_type,
                    external_id=reference.external_id,
                    description=reference.description,
                    reference_created_at=reference.created_at,
                )
            )

        return orm

    @staticmethod
    def to_domain_project(orm: ProjectModel) -> Project:
        milestones = [
            ProjectMilestone(
                id=milestone_orm.id,
                name=milestone_orm.name,
                sequence=milestone_orm.sequence,
                status=milestone_orm.status,
                description=milestone_orm.description,
                due_date=ProjectMapper._normalize_timestamp_or_none(milestone_orm.due_date),
                completed_date=ProjectMapper._normalize_timestamp_or_none(
                    milestone_orm.completed_date
                ),
            )
            for milestone_orm in sorted(orm.milestones, key=lambda item: item.sequence)
        ]

        activities = [
            ProjectActivity(
                id=activity_orm.id,
                title=activity_orm.title,
                status=activity_orm.status,
                description=activity_orm.description,
                planned_start=ProjectMapper._normalize_timestamp_or_none(
                    activity_orm.planned_start
                ),
                planned_finish=ProjectMapper._normalize_timestamp_or_none(
                    activity_orm.planned_finish
                ),
                actual_start=ProjectMapper._normalize_timestamp_or_none(
                    activity_orm.actual_start
                ),
                actual_finish=ProjectMapper._normalize_timestamp_or_none(
                    activity_orm.actual_finish
                ),
                priority=activity_orm.priority,
                estimated_hours=activity_orm.estimated_hours,
                actual_hours=activity_orm.actual_hours,
            )
            for activity_orm in sorted(orm.activities, key=lambda item: item.activity_order)
        ]

        assignments = [
            ProjectAssignment(
                id=assignment_orm.id,
                organisation_id=assignment_orm.organisation_id,
                contact_id=assignment_orm.contact_id,
                role=assignment_orm.role,
                assigned_from=ProjectMapper._normalize_timestamp_or_none(
                    assignment_orm.assigned_from
                ),
                assigned_until=ProjectMapper._normalize_timestamp_or_none(
                    assignment_orm.assigned_until
                ),
            )
            for assignment_orm in orm.assignments
        ]

        references = [
            ExternalReference(
                id=reference_orm.id,
                reference_type=reference_orm.reference_type,
                external_id=reference_orm.external_id,
                description=reference_orm.description,
                created_at=ProjectMapper._normalize_timestamp(
                    reference_orm.reference_created_at
                ),
            )
            for reference_orm in sorted(orm.references, key=lambda item: item.reference_order)
        ]

        project = Project(
            id=ProjectId(orm.id),
            project_number=ProjectNumber(orm.project_number),
            project_name=ProjectName(orm.project_name),
            status=orm.status,
            priority=orm.priority,
            description=orm.description,
            start_date=ProjectMapper._normalize_timestamp_or_none(orm.start_date),
            end_date=ProjectMapper._normalize_timestamp_or_none(orm.end_date),
            created_at=ProjectMapper._normalize_timestamp(orm.project_created_at),
            updated_at=ProjectMapper._normalize_timestamp_or_none(orm.project_updated_at),
            archived_at=ProjectMapper._normalize_timestamp_or_none(orm.archived_at),
            milestones=milestones,
            activities=activities,
            assignments=assignments,
            references=references,
        )
        project.version = orm.version
        project.pull_events()
        return project

    @staticmethod
    def _normalize_timestamp(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    @staticmethod
    def _normalize_timestamp_or_none(value: datetime | None) -> datetime | None:
        if value is None:
            return None
        return ProjectMapper._normalize_timestamp(value)

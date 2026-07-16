"""Projects domain package."""

from mfm.domain.projects.external_reference import ExternalReference
from mfm.domain.projects.events import ProjectArchived
from mfm.domain.projects.events import ProjectCreated
from mfm.domain.projects.events import ProjectStatusChanged
from mfm.domain.projects.events import ProjectUpdated
from mfm.domain.projects.exceptions import InvalidProjectAssignmentError
from mfm.domain.projects.exceptions import InvalidProjectError
from mfm.domain.projects.exceptions import InvalidProjectNameError
from mfm.domain.projects.exceptions import InvalidProjectNumberError
from mfm.domain.projects.exceptions import InvalidProjectReferenceError
from mfm.domain.projects.exceptions import InvalidProjectStateError
from mfm.domain.projects.exceptions import ProjectError
from mfm.domain.projects.project_activity import ProjectActivity
from mfm.domain.projects.project_assignment import ProjectAssignment
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_milestone import ProjectMilestone
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_repository import ProjectRepository
from mfm.domain.projects.project_status import ProjectStatus
from mfm.domain.projects.reference_type import ReferenceType

__all__ = [
    "ExternalReference",
    "InvalidProjectAssignmentError",
    "InvalidProjectError",
    "InvalidProjectNameError",
    "InvalidProjectNumberError",
    "InvalidProjectReferenceError",
    "InvalidProjectStateError",
    "Project",
    "ProjectActivity",
    "ProjectAssignment",
    "ProjectArchived",
    "ProjectCreated",
    "ProjectError",
    "ProjectId",
    "ProjectMilestone",
    "ProjectName",
    "ProjectNumber",
    "ProjectPriority",
    "ProjectRepository",
    "ProjectStatusChanged",
    "ProjectStatus",
    "ProjectUpdated",
    "ReferenceType",
]
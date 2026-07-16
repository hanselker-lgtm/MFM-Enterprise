"""Domain exceptions for the Projects capability."""


class ProjectError(Exception):
    """Base exception for project domain errors."""


class InvalidProjectError(ProjectError):
    """Raised when project aggregate state is invalid."""


class InvalidProjectStateError(ProjectError):
    """Raised when project lifecycle state is invalid."""


class InvalidProjectNumberError(ProjectError):
    """Raised when project number data is invalid."""


class InvalidProjectNameError(ProjectError):
    """Raised when project name data is invalid."""


class InvalidProjectReferenceError(ProjectError):
    """Raised when project external reference data is invalid."""


class InvalidProjectAssignmentError(ProjectError):
    """Raised when project assignment data is invalid."""
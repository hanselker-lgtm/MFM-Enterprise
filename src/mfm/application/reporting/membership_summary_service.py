"""Application reporting service for membership management summary."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol

from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryCategoryTotalsDTO,
)
from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryResponse,
)
from mfm.application.reporting.models.membership_summary_dto import (
    MembershipSummaryStatusTotalsDTO,
)
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_status import MembershipStatus


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository dependencies fail."""


@dataclass(frozen=True, slots=True)
class MembershipSummaryRequest:
    include_inactive: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_inactive, bool):
            raise ValidationException("include_inactive must be bool")


class ListMembershipsPort(Protocol):
    def list(self): ...

    def list_active(self): ...


class MembershipSummaryService:
    """Build membership summary metrics from membership aggregate data."""

    def __init__(self, *, membership_repository: ListMembershipsPort) -> None:
        self._membership_repository = membership_repository

    def execute(self, request: MembershipSummaryRequest) -> MembershipSummaryResponse:
        request.validate()

        try:
            if request.include_inactive:
                memberships = self._membership_repository.list()
            else:
                memberships = self._membership_repository.list_active()
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("Membership summary data retrieval failed") from exc

        status_totals = MembershipSummaryStatusTotalsDTO(
            total=len(memberships),
            active=sum(1 for item in memberships if item.status is MembershipStatus.ACTIVE),
            suspended=sum(1 for item in memberships if item.status is MembershipStatus.SUSPENDED),
            ended=sum(1 for item in memberships if item.status is MembershipStatus.ENDED),
            expired=sum(1 for item in memberships if item.status is MembershipStatus.EXPIRED),
        )

        category_totals = MembershipSummaryCategoryTotalsDTO(
            general=sum(
                1
                for item in memberships
                if item.membership_type.category is MembershipCategory.GENERAL
            ),
            youth=sum(
                1
                for item in memberships
                if item.membership_type.category is MembershipCategory.YOUTH
            ),
            senior=sum(
                1
                for item in memberships
                if item.membership_type.category is MembershipCategory.SENIOR
            ),
            family=sum(
                1
                for item in memberships
                if item.membership_type.category is MembershipCategory.FAMILY
            ),
            corporate=sum(
                1
                for item in memberships
                if item.membership_type.category is MembershipCategory.CORPORATE
            ),
        )

        return MembershipSummaryResponse(
            status_totals=status_totals,
            category_totals=category_totals,
            generated_at=datetime.now(UTC),
        )

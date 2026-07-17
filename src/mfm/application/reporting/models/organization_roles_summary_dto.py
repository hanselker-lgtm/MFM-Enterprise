"""DTOs for Organization & Roles reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class OrganizationRolesSummaryResponse:
    organization_id: UUID
    total_roles: int
    total_assignments: int
    total_committees: int
    has_board: bool
    total_election_periods: int
    generated_at: datetime

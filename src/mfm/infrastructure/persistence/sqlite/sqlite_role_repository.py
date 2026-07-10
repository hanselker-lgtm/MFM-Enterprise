"""SQLite repository for Role aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.organization_mapper import OrganizationMapper
from mfm.database.models.role_assignment_model import RoleAssignmentModel
from mfm.database.models.role_model import RoleModel
from mfm.domain.organization.role import Role
from mfm.repositories.role_repository import RoleRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteRoleRepository(RoleRepository):
    """SQLAlchemy-backed repository for Role aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, role: Role) -> None:
        if self._session.scalar(
            select(RoleModel).where(RoleModel.role_code == role.role_code.value)
        ) is not None:
            raise ValueError(f"Role code {role.role_code.value} already exists")

        organization_id = self._resolve_organization_id(role)
        self._session.add(OrganizationMapper.to_orm_role(role, organization_id=organization_id))
        self._session.flush()

    def get_by_id(self, role_id: UUID) -> Role | None:
        orm = self._session.scalar(select(RoleModel).where(RoleModel.id == role_id))
        if orm is None:
            return None
        return OrganizationMapper.to_domain_role(orm)

    def update(self, role: Role) -> None:
        orm = self._session.get(RoleModel, role.id.value)
        if orm is None:
            raise ValueError(f"Role {role.id.value} does not exist")

        if orm.role_code != role.role_code.value:
            duplicate = self._session.scalar(
                select(RoleModel).where(
                    RoleModel.role_code == role.role_code.value,
                    RoleModel.id != role.id.value,
                )
            )
            if duplicate is not None:
                raise ValueError(f"Role code {role.role_code.value} already exists")

        orm.organization_id = self._resolve_organization_id(
            role,
            fallback=orm.organization_id,
        )
        orm.role_code = role.role_code.value
        orm.name = role.name
        orm.description = role.description
        orm.category = role.category
        orm.status = role.status
        orm.assignments = [
            RoleAssignmentModel(
                role_id=role.id.value,
                assignee_id=assignment.assignee_id,
                organization_id=assignment.organization_id,
                valid_from=assignment.valid_from,
                valid_to=assignment.valid_to,
            )
            for assignment in role.assignments
        ]
        self._session.flush()

    def delete(self, role_id: UUID) -> None:
        orm = self._session.get(RoleModel, role_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, role_id: UUID) -> bool:
        return self._session.get(RoleModel, role_id) is not None

    def list(self) -> list[Role]:
        orm_entities = self._session.scalars(select(RoleModel)).all()
        return [OrganizationMapper.to_domain_role(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Role]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(RoleModel).where(
                or_(
                    RoleModel.role_code.ilike(query),
                    RoleModel.name.ilike(query),
                    RoleModel.description.ilike(query),
                )
            )
        ).all()
        return [OrganizationMapper.to_domain_role(orm) for orm in orm_entities]

    @staticmethod
    def _resolve_organization_id(role: Role, fallback: UUID | None = None) -> UUID:
        if role.assignments:
            return role.assignments[0].organization_id
        if fallback is not None:
            return fallback
        raise ValueError("Role requires at least one assignment to resolve organization_id")

"""Rename Vessel use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.fleet.create_vessel import ApplicationException
from mfm.application.fleet.create_vessel import BusinessRuleViolation
from mfm.application.fleet.create_vessel import RepositoryException
from mfm.application.fleet.create_vessel import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.fleet.exceptions import VesselError
from mfm.repositories.vessel_repository import VesselRepository


@dataclass(frozen=True, slots=True)
class RenameVesselRequest:
    vessel_id: UUID
    name: str

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")


@dataclass(frozen=True, slots=True)
class RenameVesselResponse:
    vessel_id: UUID
    name: str


class RenameVesselUseCase:
    """Rename vessel in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: RenameVesselRequest) -> RenameVesselResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VesselRepository = uow.vessel_repository

                vessel = repository.get_by_id(request.vessel_id)
                if vessel is None:
                    raise BusinessRuleViolation(f"Vessel {request.vessel_id} does not exist")

                vessel.rename(request.name)
                repository.update(vessel)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VesselError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Rename vessel failed") from exc

        return RenameVesselResponse(vessel_id=vessel.id.value, name=vessel.name)

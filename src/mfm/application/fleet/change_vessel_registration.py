"""Change Vessel registration use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.fleet.create_vessel import ApplicationException
from mfm.application.fleet.create_vessel import BusinessRuleViolation
from mfm.application.fleet.create_vessel import RepositoryException
from mfm.application.fleet.create_vessel import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.fleet.exceptions import VesselError
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.repositories.vessel_repository import VesselRepository


@dataclass(frozen=True, slots=True)
class ChangeVesselRegistrationRequest:
    vessel_id: UUID
    registration: str

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.registration, str) or not self.registration.strip():
            raise ValidationException("registration must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ChangeVesselRegistrationResponse:
    vessel_id: UUID
    registration: str


class ChangeVesselRegistrationUseCase:
    """Change vessel registration in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self, request: ChangeVesselRegistrationRequest
    ) -> ChangeVesselRegistrationResponse:
        request.validate()

        registration = VesselRegistration(request.registration)

        try:
            with self._unit_of_work as uow:
                repository: VesselRepository = uow.vessel_repository

                vessel = repository.get_by_id(request.vessel_id)
                if vessel is None:
                    raise BusinessRuleViolation(f"Vessel {request.vessel_id} does not exist")

                duplicate = repository.get_by_registration(registration.value)
                if duplicate is not None and duplicate.id != vessel.id:
                    raise BusinessRuleViolation(
                        f"Vessel registration {registration.value} already exists"
                    )

                vessel.change_registration(registration)
                repository.update(vessel)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VesselError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Change vessel registration failed") from exc

        return ChangeVesselRegistrationResponse(
            vessel_id=vessel.id.value,
            registration=vessel.registration.value,
        )

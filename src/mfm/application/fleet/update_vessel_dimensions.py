"""Update Vessel dimensions use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.fleet.create_vessel import ApplicationException
from mfm.application.fleet.create_vessel import BusinessRuleViolation
from mfm.application.fleet.create_vessel import RepositoryException
from mfm.application.fleet.create_vessel import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.fleet.exceptions import VesselError
from mfm.domain.fleet.vessel_dimensions import VesselDimensions
from mfm.repositories.vessel_repository import VesselRepository


@dataclass(frozen=True, slots=True)
class UpdateVesselDimensionsRequest:
    vessel_id: UUID
    length: float
    beam: float
    draft: float

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.length, (int, float)):
            raise ValidationException("length must be numeric")
        if not isinstance(self.beam, (int, float)):
            raise ValidationException("beam must be numeric")
        if not isinstance(self.draft, (int, float)):
            raise ValidationException("draft must be numeric")


@dataclass(frozen=True, slots=True)
class UpdateVesselDimensionsResponse:
    vessel_id: UUID
    length: float
    beam: float
    draft: float


class UpdateVesselDimensionsUseCase:
    """Update vessel dimensions in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self, request: UpdateVesselDimensionsRequest
    ) -> UpdateVesselDimensionsResponse:
        request.validate()

        dimensions = VesselDimensions(
            length=float(request.length),
            beam=float(request.beam),
            draft=float(request.draft),
        )

        try:
            with self._unit_of_work as uow:
                repository: VesselRepository = uow.vessel_repository

                vessel = repository.get_by_id(request.vessel_id)
                if vessel is None:
                    raise BusinessRuleViolation(f"Vessel {request.vessel_id} does not exist")

                vessel.update_dimensions(dimensions)
                repository.update(vessel)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VesselError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update vessel dimensions failed") from exc

        return UpdateVesselDimensionsResponse(
            vessel_id=vessel.id.value,
            length=vessel.length,
            beam=vessel.beam,
            draft=vessel.draft,
        )

"""Update Vessel use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.fleet.create_vessel import ApplicationException
from mfm.application.fleet.create_vessel import BusinessRuleViolation
from mfm.application.fleet.create_vessel import RepositoryException
from mfm.application.fleet.create_vessel import ValidationException
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.fleet.exceptions import VesselError
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.repositories.vessel_repository import VesselRepository


@dataclass(frozen=True, slots=True)
class UpdateVesselRequest:
    vessel_id: UUID
    shipyard: str
    build_year: int | None
    construction_material: VesselMaterial

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.shipyard, str):
            raise ValidationException("shipyard must be a string")
        if self.build_year is not None and (
            not isinstance(self.build_year, int) or self.build_year <= 0
        ):
            raise ValidationException("build_year must be positive int or None")
        if not isinstance(self.construction_material, VesselMaterial):
            raise ValidationException("construction_material must be VesselMaterial")


@dataclass(frozen=True, slots=True)
class UpdateVesselResponse:
    vessel_id: UUID
    shipyard: str
    build_year: int | None
    construction_material: str


class UpdateVesselUseCase:
    """Update vessel metadata in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: UpdateVesselRequest) -> UpdateVesselResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VesselRepository = uow.vessel_repository

                vessel = repository.get_by_id(request.vessel_id)
                if vessel is None:
                    raise BusinessRuleViolation(f"Vessel {request.vessel_id} does not exist")

                vessel.shipyard = request.shipyard.strip()
                vessel.build_year = request.build_year
                vessel.construction_material = request.construction_material

                repository.update(vessel)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VesselError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update vessel failed") from exc

        return UpdateVesselResponse(
            vessel_id=vessel.id.value,
            shipyard=vessel.shipyard,
            build_year=vessel.build_year,
            construction_material=vessel.construction_material.value,
        )

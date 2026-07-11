"""Create Vessel use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.fleet.exceptions import VesselError
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus
from mfm.repositories.vessel_repository import VesselRepository


class ApplicationException(Exception):
    """Base exception for vessel application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository/persistence failures."""


@dataclass(frozen=True, slots=True)
class CreateVesselRequest:
    asset_id: UUID
    registration: str
    name: str
    shipyard: str
    build_year: int | None
    construction_material: VesselMaterial
    length: float
    beam: float
    draft: float
    status: VesselStatus = VesselStatus.ACTIVE

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if not isinstance(self.registration, str) or not self.registration.strip():
            raise ValidationException("registration must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.shipyard, str):
            raise ValidationException("shipyard must be a string")
        if self.build_year is not None and (
            not isinstance(self.build_year, int) or self.build_year <= 0
        ):
            raise ValidationException("build_year must be positive int or None")
        if not isinstance(self.construction_material, VesselMaterial):
            raise ValidationException("construction_material must be VesselMaterial")
        if not isinstance(self.length, (int, float)):
            raise ValidationException("length must be numeric")
        if not isinstance(self.beam, (int, float)):
            raise ValidationException("beam must be numeric")
        if not isinstance(self.draft, (int, float)):
            raise ValidationException("draft must be numeric")
        if not isinstance(self.status, VesselStatus):
            raise ValidationException("status must be VesselStatus")


@dataclass(frozen=True, slots=True)
class CreateVesselResponse:
    vessel_id: UUID
    asset_id: UUID
    registration: str
    name: str
    status: str


class CreateVesselUseCase:
    """Create vessel aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateVesselRequest) -> CreateVesselResponse:
        request.validate()

        registration = VesselRegistration(request.registration)

        try:
            with self._unit_of_work as uow:
                repository: VesselRepository = uow.vessel_repository

                if repository.get_by_registration(registration.value) is not None:
                    raise BusinessRuleViolation(
                        f"Vessel registration {registration.value} already exists"
                    )

                vessel = Vessel(
                    asset_id=request.asset_id,
                    registration=registration,
                    name=request.name,
                    shipyard=request.shipyard,
                    build_year=request.build_year,
                    construction_material=request.construction_material,
                    length=float(request.length),
                    beam=float(request.beam),
                    draft=float(request.draft),
                    status=request.status,
                )

                repository.add(vessel)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except VesselError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create vessel failed") from exc

        return CreateVesselResponse(
            vessel_id=vessel.id.value,
            asset_id=vessel.asset_id,
            registration=vessel.registration.value,
            name=vessel.name,
            status=vessel.status.value,
        )

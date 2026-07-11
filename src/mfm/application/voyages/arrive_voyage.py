"""Arrive Voyage use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.voyages.create_voyage import ApplicationException
from mfm.application.voyages.create_voyage import BusinessRuleViolation
from mfm.application.voyages.create_voyage import RepositoryException
from mfm.application.voyages.create_voyage import ValidationException
from mfm.application.voyages.create_voyage import VoyageLocationInput
from mfm.application.voyages.create_voyage import VoyageResponse
from mfm.application.voyages.create_voyage import to_location_snapshot
from mfm.application.voyages.create_voyage import to_voyage_response
from mfm.domain.voyages.exceptions import VoyageError
from mfm.repositories.voyage_repository import VoyageRepository


@dataclass(frozen=True, slots=True)
class ArriveVoyageRequest:
    voyage_id: UUID
    arrived_at: datetime
    actual_arrival_location: VoyageLocationInput

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")
        if not isinstance(self.arrived_at, datetime):
            raise ValidationException("arrived_at must be datetime")
        self.actual_arrival_location.validate(field_name="actual_arrival_location")


@dataclass(frozen=True, slots=True)
class ArriveVoyageResponse:
    voyage: VoyageResponse


class ArriveVoyageUseCase:
    """Arrive underway voyage through domain lifecycle API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ArriveVoyageRequest) -> ArriveVoyageResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VoyageRepository = uow.voyage_repository
                voyage = repository.get_by_id(request.voyage_id)
                if voyage is None:
                    raise BusinessRuleViolation(f"Voyage {request.voyage_id} does not exist")

                voyage.arrive(
                    arrived_at=request.arrived_at,
                    actual_arrival_location=to_location_snapshot(
                        request.actual_arrival_location
                    ),
                )
                repository.update(voyage)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VoyageError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Arrive voyage failed") from exc

        return ArriveVoyageResponse(voyage=to_voyage_response(voyage))

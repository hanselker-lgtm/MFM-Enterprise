"""Get Voyage use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.voyages.create_voyage import ApplicationException
from mfm.application.voyages.create_voyage import BusinessRuleViolation
from mfm.application.voyages.create_voyage import RepositoryException
from mfm.application.voyages.create_voyage import ValidationException
from mfm.application.voyages.create_voyage import VoyageResponse
from mfm.application.voyages.create_voyage import to_voyage_response
from mfm.repositories.voyage_repository import VoyageRepository


@dataclass(frozen=True, slots=True)
class GetVoyageRequest:
    voyage_id: UUID

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetVoyageResponse:
    voyage: VoyageResponse


class GetVoyageUseCase:
    """Load one voyage through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: GetVoyageRequest) -> GetVoyageResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VoyageRepository = uow.voyage_repository
                voyage = repository.get_by_id(request.voyage_id)
                if voyage is None:
                    raise BusinessRuleViolation(f"Voyage {request.voyage_id} does not exist")
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get voyage failed") from exc

        return GetVoyageResponse(voyage=to_voyage_response(voyage))

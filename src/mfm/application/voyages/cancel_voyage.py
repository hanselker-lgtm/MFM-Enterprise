"""Cancel Voyage use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.voyages.create_voyage import ApplicationException
from mfm.application.voyages.create_voyage import BusinessRuleViolation
from mfm.application.voyages.create_voyage import RepositoryException
from mfm.application.voyages.create_voyage import ValidationException
from mfm.application.voyages.create_voyage import VoyageResponse
from mfm.application.voyages.create_voyage import to_voyage_response
from mfm.domain.voyages.exceptions import VoyageError
from mfm.repositories.voyage_repository import VoyageRepository


@dataclass(frozen=True, slots=True)
class CancelVoyageRequest:
    voyage_id: UUID
    cancellation_reason: str
    cancelled_at: datetime
    cancelled_by_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")
        if not isinstance(self.cancellation_reason, str) or not self.cancellation_reason.strip():
            raise ValidationException("cancellation_reason must be a non-empty string")
        if not isinstance(self.cancelled_at, datetime):
            raise ValidationException("cancelled_at must be datetime")
        if self.cancelled_by_reference is not None and not isinstance(
            self.cancelled_by_reference,
            str,
        ):
            raise ValidationException("cancelled_by_reference must be string or None")


@dataclass(frozen=True, slots=True)
class CancelVoyageResponse:
    voyage: VoyageResponse


class CancelVoyageUseCase:
    """Cancel draft/planned voyage through domain lifecycle API."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CancelVoyageRequest) -> CancelVoyageResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VoyageRepository = uow.voyage_repository
                voyage = repository.get_by_id(request.voyage_id)
                if voyage is None:
                    raise BusinessRuleViolation(f"Voyage {request.voyage_id} does not exist")

                voyage.cancel(
                    cancellation_reason=request.cancellation_reason,
                    cancelled_at=request.cancelled_at,
                    cancelled_by_reference=request.cancelled_by_reference,
                )
                repository.update(voyage)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VoyageError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Cancel voyage failed") from exc

        return CancelVoyageResponse(voyage=to_voyage_response(voyage))

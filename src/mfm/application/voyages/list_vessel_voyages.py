"""List Vessel Voyages use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.voyages.create_voyage import ApplicationException
from mfm.application.voyages.create_voyage import RepositoryException
from mfm.application.voyages.create_voyage import ValidationException
from mfm.application.voyages.create_voyage import VoyageResponse
from mfm.application.voyages.create_voyage import to_voyage_response
from mfm.repositories.voyage_repository import VoyageRepository


@dataclass(frozen=True, slots=True)
class ListVesselVoyagesRequest:
    vessel_id: UUID

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")


@dataclass(frozen=True, slots=True)
class ListVesselVoyagesResponse:
    voyages: tuple[VoyageResponse, ...]


class ListVesselVoyagesUseCase:
    """List voyages for one vessel through repository contract."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: ListVesselVoyagesRequest) -> ListVesselVoyagesResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VoyageRepository = uow.voyage_repository
                voyages = repository.get_by_vessel(request.vessel_id)
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("List vessel voyages failed") from exc

        return ListVesselVoyagesResponse(
            voyages=tuple(to_voyage_response(item) for item in voyages)
        )

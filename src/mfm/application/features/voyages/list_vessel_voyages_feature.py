"""List vessel voyages feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.voyages.create_voyage_feature import RepositoryException
from mfm.application.features.voyages.create_voyage_feature import ValidationException
from mfm.application.features.voyages.create_voyage_feature import VoyageResponse
from mfm.application.features.voyages.create_voyage_feature import to_feature_voyage_response
from mfm.application.voyages.create_voyage import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.voyages.create_voyage import (
    ValidationException as ServiceValidationException,
)
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesRequest as ServiceRequest
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesResponse as ServiceResponse
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesUseCase


@dataclass(frozen=True, slots=True)
class ListVesselVoyagesRequest:
    vessel_id: UUID

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")


@dataclass(frozen=True, slots=True)
class ListVesselVoyagesResponse:
    voyages: tuple[VoyageResponse, ...]


class ListVesselVoyagesService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ListVesselVoyagesFeature:
    """Feature facade for vessel voyage listing."""

    def __init__(self, *, service: ListVesselVoyagesService) -> None:
        self._service = service

    def execute(self, request: ListVesselVoyagesRequest) -> ListVesselVoyagesResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(vessel_id=request.vessel_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("List vessel voyages feature failed") from exc

        return ListVesselVoyagesResponse(
            voyages=tuple(to_feature_voyage_response(item) for item in service_response.voyages)
        )

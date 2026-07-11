"""Remove technical component feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    RepositoryException,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    TechnicalConfigurationResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    ValidationException,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    to_feature_configuration_response,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ValidationException as ServiceValidationException,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentRequest as ServiceRequest,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentResponse as ServiceResponse,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentUseCase,
)


@dataclass(frozen=True, slots=True)
class RemoveTechnicalComponentRequest:
    configuration_id: UUID
    component_id: UUID
    removed_on: date
    retired: bool = False

    def validate(self) -> None:
        if not isinstance(self.configuration_id, UUID):
            raise ValidationException("configuration_id must be UUID")
        if not isinstance(self.component_id, UUID):
            raise ValidationException("component_id must be UUID")
        if not isinstance(self.removed_on, date):
            raise ValidationException("removed_on must be date")
        if not isinstance(self.retired, bool):
            raise ValidationException("retired must be bool")


@dataclass(frozen=True, slots=True)
class RemoveTechnicalComponentResponse:
    configuration: TechnicalConfigurationResponse


class RemoveTechnicalComponentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RemoveTechnicalComponentFeature:
    """Feature facade for component removal."""

    def __init__(self, *, service: RemoveTechnicalComponentService) -> None:
        self._service = service

    def execute(
        self,
        request: RemoveTechnicalComponentRequest,
    ) -> RemoveTechnicalComponentResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    configuration_id=request.configuration_id,
                    component_id=request.component_id,
                    removed_on=request.removed_on,
                    retired=request.retired,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Remove technical component feature failed") from exc

        return RemoveTechnicalComponentResponse(
            configuration=to_feature_configuration_response(service_response.configuration)
        )

"""Install technical component feature facade following Public API Standard."""

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
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentRequest as ServiceRequest,
)
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentResponse as ServiceResponse,
)
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentUseCase,
)


@dataclass(frozen=True, slots=True)
class InstallTechnicalComponentRequest:
    configuration_id: UUID
    component_id: UUID
    installed_on: date

    def validate(self) -> None:
        if not isinstance(self.configuration_id, UUID):
            raise ValidationException("configuration_id must be UUID")
        if not isinstance(self.component_id, UUID):
            raise ValidationException("component_id must be UUID")
        if not isinstance(self.installed_on, date):
            raise ValidationException("installed_on must be date")


@dataclass(frozen=True, slots=True)
class InstallTechnicalComponentResponse:
    configuration: TechnicalConfigurationResponse


class InstallTechnicalComponentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class InstallTechnicalComponentFeature:
    """Feature facade for component installation."""

    def __init__(self, *, service: InstallTechnicalComponentService) -> None:
        self._service = service

    def execute(
        self,
        request: InstallTechnicalComponentRequest,
    ) -> InstallTechnicalComponentResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    configuration_id=request.configuration_id,
                    component_id=request.component_id,
                    installed_on=request.installed_on,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Install technical component feature failed") from exc

        return InstallTechnicalComponentResponse(
            configuration=to_feature_configuration_response(service_response.configuration)
        )

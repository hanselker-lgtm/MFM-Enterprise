"""Install Technical Component use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.technical_configuration.create_technical_configuration import (
    ApplicationException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    TechnicalConfigurationResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ValidationException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    to_configuration_response,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.technical_configuration.exceptions import TechnicalConfigurationError
from mfm.repositories.technical_configuration_repository import (
    TechnicalConfigurationRepository,
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


class InstallTechnicalComponentUseCase:
    """Install component in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: InstallTechnicalComponentRequest,
    ) -> InstallTechnicalComponentResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: TechnicalConfigurationRepository = (
                    uow.technical_configuration_repository
                )

                configuration = repository.get_by_id(request.configuration_id)
                if configuration is None:
                    raise BusinessRuleViolation(
                        f"Technical configuration {request.configuration_id} does not exist"
                    )

                configuration.install_component(request.component_id, request.installed_on)
                repository.update(configuration)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except TechnicalConfigurationError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Install technical component failed") from exc

        return InstallTechnicalComponentResponse(
            configuration=to_configuration_response(configuration)
        )

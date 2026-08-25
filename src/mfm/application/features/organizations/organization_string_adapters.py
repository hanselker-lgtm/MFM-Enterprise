"""String-friendly adapters over CreateOrganizationFeature/UpdateOrganizationFeature.

Those two features (in ``mfm.application.features.organization``) type
their ``organization_type``/``status`` fields as the actual domain
enums (``OrganizationType``/``OrganizationStatus``) rather than plain
strings -- unlike the equivalent Projects features, which accept
plain ``str`` and convert internally. Requiring the presentation
layer to import a domain enum just to call them would violate this
codebase's own boundary rule (presentation may only depend on
``mfm.application.features``/``reporting.models``, never
``mfm.domain``). These adapters do the str -> enum conversion here
in the application layer instead, so presentation-layer code only
ever deals with plain strings.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.organization.create_organization_feature import (
    ApplicationException,
    BusinessRuleViolation,
    CreateOrganizationFeature,
    CreateOrganizationResponse,
    RepositoryException,
    ValidationException,
)
from mfm.application.features.organization.create_organization_feature import (
    CreateOrganizationRequest as _EnumCreateOrganizationRequest,
)
from mfm.application.features.organization.update_organization_feature import (
    UpdateOrganizationFeature,
    UpdateOrganizationResponse,
)
from mfm.application.features.organization.update_organization_feature import (
    UpdateOrganizationRequest as _EnumUpdateOrganizationRequest,
)
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


@dataclass(frozen=True, slots=True)
class CreateOrganizationRequest:
    organization_number: str
    name: str
    organization_type: str

    def validate(self) -> None:
        if not isinstance(self.organization_number, str) or not self.organization_number.strip():
            raise ValidationException("organization_number must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        try:
            OrganizationType(self.organization_type.strip().upper())
        except ValueError as exc:
            raise ValidationException(
                f"organization_type is invalid: {self.organization_type}"
            ) from exc


@dataclass(frozen=True, slots=True)
class UpdateOrganizationRequest:
    organization_id: UUID
    name: str | None = None
    organization_type: str | None = None
    status: str | None = None

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        if self.organization_type is not None:
            try:
                OrganizationType(self.organization_type.strip().upper())
            except ValueError as exc:
                raise ValidationException(
                    f"organization_type is invalid: {self.organization_type}"
                ) from exc
        if self.status is not None:
            try:
                OrganizationStatus(self.status.strip().upper())
            except ValueError as exc:
                raise ValidationException(f"status is invalid: {self.status}") from exc


class CreateOrganizationServicePort(Protocol):
    def execute(self, request: _EnumCreateOrganizationRequest) -> CreateOrganizationResponse: ...


class UpdateOrganizationServicePort(Protocol):
    def execute(self, request: _EnumUpdateOrganizationRequest) -> UpdateOrganizationResponse: ...


class CreateOrganizationStringFeature:
    """String-typed facade over :class:`CreateOrganizationFeature`."""

    def __init__(self, *, feature: CreateOrganizationServicePort) -> None:
        self._feature = feature

    def execute(self, request: CreateOrganizationRequest) -> CreateOrganizationResponse:
        request.validate()
        try:
            return self._feature.execute(
                _EnumCreateOrganizationRequest(
                    organization_number=request.organization_number,
                    name=request.name,
                    organization_type=OrganizationType(request.organization_type.strip().upper()),
                )
            )
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Create organization feature failed") from exc


class UpdateOrganizationStringFeature:
    """String-typed facade over :class:`UpdateOrganizationFeature`."""

    def __init__(self, *, feature: UpdateOrganizationServicePort) -> None:
        self._feature = feature

    def execute(self, request: UpdateOrganizationRequest) -> UpdateOrganizationResponse:
        request.validate()
        try:
            return self._feature.execute(
                _EnumUpdateOrganizationRequest(
                    organization_id=request.organization_id,
                    name=request.name,
                    organization_type=(
                        OrganizationType(request.organization_type.strip().upper())
                        if request.organization_type is not None
                        else None
                    ),
                    status=(
                        OrganizationStatus(request.status.strip().upper())
                        if request.status is not None
                        else None
                    ),
                )
            )
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Update organization feature failed") from exc

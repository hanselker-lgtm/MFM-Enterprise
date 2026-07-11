"""Get Certificate history use case."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.certificates.create_certificate import ApplicationException
from mfm.application.certificates.create_certificate import BusinessRuleViolation
from mfm.application.certificates.create_certificate import CertificateResponse
from mfm.application.certificates.create_certificate import RepositoryException
from mfm.application.certificates.create_certificate import ValidationException
from mfm.application.certificates.create_certificate import to_certificate_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.certificate_repository import CertificateRepository


@dataclass(frozen=True, slots=True)
class GetCertificateHistoryRequest:
    certificate_id: UUID

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetCertificateHistoryResponse:
    certificates: tuple[CertificateResponse, ...]


class GetCertificateHistoryUseCase:
    """Load renewal history as separate historical certificate records."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: GetCertificateHistoryRequest,
    ) -> GetCertificateHistoryResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: CertificateRepository = uow.certificate_repository

                if repository.get_by_id(request.certificate_id) is None:
                    raise BusinessRuleViolation(
                        f"Certificate {request.certificate_id} does not exist"
                    )

                history = repository.get_renewal_history(request.certificate_id)
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get certificate history failed") from exc

        return GetCertificateHistoryResponse(
            certificates=tuple(to_certificate_response(item) for item in history)
        )

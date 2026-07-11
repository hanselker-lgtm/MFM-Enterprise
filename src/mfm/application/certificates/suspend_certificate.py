"""Suspend Certificate use case."""

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
from mfm.domain.certificates.exceptions import CertificateError
from mfm.repositories.certificate_repository import CertificateRepository


@dataclass(frozen=True, slots=True)
class SuspendCertificateRequest:
    certificate_id: UUID
    notes: str | None = None

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")


@dataclass(frozen=True, slots=True)
class SuspendCertificateResponse:
    certificate: CertificateResponse


class SuspendCertificateUseCase:
    """Suspend certificate through domain lifecycle operation."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: SuspendCertificateRequest) -> SuspendCertificateResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: CertificateRepository = uow.certificate_repository

                certificate = repository.get_by_id(request.certificate_id)
                if certificate is None:
                    raise BusinessRuleViolation(
                        f"Certificate {request.certificate_id} does not exist"
                    )

                certificate.suspend(notes=request.notes)
                repository.update(certificate)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except CertificateError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Suspend certificate failed") from exc

        return SuspendCertificateResponse(certificate=to_certificate_response(certificate))

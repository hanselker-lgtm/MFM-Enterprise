"""Evaluate Certificate status use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.certificates.create_certificate import ApplicationException
from mfm.application.certificates.create_certificate import BusinessRuleViolation
from mfm.application.certificates.create_certificate import RepositoryException
from mfm.application.certificates.create_certificate import ValidationException
from mfm.application.certificates.create_certificate import (
    EvaluateCertificateStatusResponse,
)
from mfm.application.certificates.create_certificate import to_evaluated_status_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.certificates.exceptions import CertificateError
from mfm.repositories.certificate_repository import CertificateRepository


@dataclass(frozen=True, slots=True)
class EvaluateCertificateStatusRequest:
    certificate_id: UUID
    as_of_date: date
    expiring_threshold_days: int = 30

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")
        if not isinstance(self.as_of_date, date):
            raise ValidationException("as_of_date must be date")
        if (
            not isinstance(self.expiring_threshold_days, int)
            or self.expiring_threshold_days < 0
        ):
            raise ValidationException("expiring_threshold_days must be non-negative int")


class EvaluateCertificateStatusUseCase:
    """Evaluate certificate status with explicit reference date."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: EvaluateCertificateStatusRequest,
    ) -> EvaluateCertificateStatusResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: CertificateRepository = uow.certificate_repository

                certificate = repository.get_by_id(request.certificate_id)
                if certificate is None:
                    raise BusinessRuleViolation(
                        f"Certificate {request.certificate_id} does not exist"
                    )

                previous_status = certificate.status
                evaluated_status = certificate.evaluate_status(
                    as_of_date=request.as_of_date,
                    expiring_threshold_days=request.expiring_threshold_days,
                )

                if certificate.status != previous_status:
                    repository.update(certificate)
                    uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except CertificateError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Evaluate certificate status failed") from exc

        return to_evaluated_status_response(
            certificate=certificate,
            evaluated_status=evaluated_status,
        )

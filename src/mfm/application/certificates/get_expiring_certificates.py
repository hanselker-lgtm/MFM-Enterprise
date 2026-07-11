"""Get expiring Certificates use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.application.certificates.create_certificate import ApplicationException
from mfm.application.certificates.create_certificate import CertificateResponse
from mfm.application.certificates.create_certificate import RepositoryException
from mfm.application.certificates.create_certificate import ValidationException
from mfm.application.certificates.create_certificate import to_certificate_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.repositories.certificate_repository import CertificateRepository


@dataclass(frozen=True, slots=True)
class GetExpiringCertificatesRequest:
    as_of_date: date
    within_days: int

    def validate(self) -> None:
        if not isinstance(self.as_of_date, date):
            raise ValidationException("as_of_date must be date")
        if not isinstance(self.within_days, int) or self.within_days < 0:
            raise ValidationException("within_days must be non-negative int")


@dataclass(frozen=True, slots=True)
class GetExpiringCertificatesResponse:
    certificates: tuple[CertificateResponse, ...]


class GetExpiringCertificatesUseCase:
    """Load expiring certificates for explicit reference date and threshold."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: GetExpiringCertificatesRequest,
    ) -> GetExpiringCertificatesResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: CertificateRepository = uow.certificate_repository
                certificates = repository.get_expiring(
                    as_of_date=request.as_of_date,
                    within_days=request.within_days,
                )
        except (ValidationException, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Get expiring certificates failed") from exc

        return GetExpiringCertificatesResponse(
            certificates=tuple(to_certificate_response(item) for item in certificates)
        )

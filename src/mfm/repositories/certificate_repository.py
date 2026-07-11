"""Repository contract for Certificate aggregates."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from datetime import date
from uuid import UUID

from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_target import CertificateTarget


class CertificateRepository(ABC):
    """Persistence contract for Certificate aggregate roots."""

    @abstractmethod
    def add(self, certificate: Certificate) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, certificate_id: UUID) -> Certificate | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, certificate: Certificate) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, certificate_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def get_by_target(self, target: CertificateTarget) -> list[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def get_active_by_target(self, target: CertificateTarget) -> list[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def get_expiring(
        self,
        *,
        as_of_date: date,
        within_days: int,
    ) -> list[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def get_expired(self, *, as_of_date: date) -> list[Certificate]:
        raise NotImplementedError

    @abstractmethod
    def get_renewal_history(self, certificate_id: UUID) -> list[Certificate]:
        raise NotImplementedError

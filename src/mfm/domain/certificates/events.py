"""Certificates domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class CertificateCreated(DomainEvent):
    certificate_id: UUID | None = None


@dataclass(slots=True)
class CertificateActivated(DomainEvent):
    certificate_id: UUID | None = None


@dataclass(slots=True)
class CertificateExpired(DomainEvent):
    certificate_id: UUID | None = None
    as_of_date: date | None = None


@dataclass(slots=True)
class CertificateSuspended(DomainEvent):
    certificate_id: UUID | None = None


@dataclass(slots=True)
class CertificateRevoked(DomainEvent):
    certificate_id: UUID | None = None


@dataclass(slots=True)
class CertificateRenewed(DomainEvent):
    certificate_id: UUID | None = None
    renewed_certificate_id: UUID | None = None

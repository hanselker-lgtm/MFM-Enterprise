"""Voyages domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class VoyageCreated(DomainEvent):
    voyage_id: UUID | None = None


@dataclass(slots=True)
class VoyagePlanned(DomainEvent):
    voyage_id: UUID | None = None


@dataclass(slots=True)
class VoyageDeparted(DomainEvent):
    voyage_id: UUID | None = None
    departed_at: datetime | None = None


@dataclass(slots=True)
class VoyageArrived(DomainEvent):
    voyage_id: UUID | None = None
    arrived_at: datetime | None = None


@dataclass(slots=True)
class VoyageCancelled(DomainEvent):
    voyage_id: UUID | None = None
    cancelled_at: datetime | None = None
"""Procurement domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class PurchaseOrderCreated(DomainEvent):
    purchase_order_id: UUID | None = None
    purchase_order_number: str | None = None


@dataclass(slots=True)
class PurchaseOrderAmended(DomainEvent):
    purchase_order_id: UUID | None = None
    purchase_order_line_id: UUID | None = None
    amendment_kind: str | None = None


@dataclass(slots=True)
class PurchaseOrderSubmitted(DomainEvent):
    purchase_order_id: UUID | None = None
    submitted_at: datetime | None = None


@dataclass(slots=True)
class PurchaseOrderApproved(DomainEvent):
    purchase_order_id: UUID | None = None
    approved_at: datetime | None = None
    approved_by_reference: str | None = None


@dataclass(slots=True)
class PurchaseOrderOrdered(DomainEvent):
    purchase_order_id: UUID | None = None
    ordered_at: datetime | None = None
    external_order_reference: str | None = None


@dataclass(slots=True)
class PurchaseReceiptRecorded(DomainEvent):
    purchase_order_id: UUID | None = None
    purchase_receipt_id: UUID | None = None
    received_at: datetime | None = None


@dataclass(slots=True)
class PurchaseOrderCancelled(DomainEvent):
    purchase_order_id: UUID | None = None
    cancelled_at: datetime | None = None
    cancelled_by_reference: str | None = None

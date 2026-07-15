"""Mapper between procurement domain and persistence models."""

from __future__ import annotations

from datetime import UTC
from datetime import datetime

from mfm.database.models.purchase_order_line_model import PurchaseOrderLineModel
from mfm.database.models.purchase_order_model import PurchaseOrderModel
from mfm.database.models.purchase_receipt_line_model import PurchaseReceiptLineModel
from mfm.database.models.purchase_receipt_model import PurchaseReceiptModel
from mfm.domain.finance.money import Money
from mfm.domain.procurement.identifiers import PurchaseOrderId
from mfm.domain.procurement.identifiers import PurchaseOrderLineId
from mfm.domain.procurement.identifiers import PurchaseOrderNumber
from mfm.domain.procurement.identifiers import PurchaseReceiptId
from mfm.domain.procurement.identifiers import SupplierReference
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_line import PurchaseOrderLine
from mfm.domain.procurement.purchase_receipt import PurchaseReceipt
from mfm.domain.procurement.purchase_receipt import PurchaseReceiptLine


class PurchaseOrderMapper:
    """Map PurchaseOrder aggregate to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_purchase_order(order: PurchaseOrder) -> PurchaseOrderModel:
        orm = PurchaseOrderModel(
            id=order.id.value,
            purchase_order_number=order.purchase_order_number.value,
            supplier_reference=order.supplier_reference.value,
            status=order.status,
            currency=order.currency,
            order_created_at=order.created_at,
            supplier_name_snapshot=order.supplier_name_snapshot,
            supplier_contact_snapshot=order.supplier_contact_snapshot,
            notes=order.notes,
            requested_by_reference=order.requested_by_reference,
            approved_by_reference=order.approved_by_reference,
            approved_at=order.approved_at,
            ordered_at=order.ordered_at,
            external_order_reference=order.external_order_reference,
            cancelled_at=order.cancelled_at,
            cancellation_reason=order.cancellation_reason,
        )

        for line_order, line in enumerate(order.lines):
            orm.lines.append(
                PurchaseOrderLineModel(
                    id=line.id.value,
                    purchase_order_id=order.id.value,
                    line_order=line_order,
                    description_snapshot=line.description_snapshot,
                    quantity=line.quantity,
                    unit_price_amount=line.unit_price.amount,
                    unit_price_currency=line.unit_price.currency,
                    inventory_item_reference=line.inventory_item_reference,
                    expected_delivery_at=line.expected_delivery_at,
                    line_note=line.line_note,
                    received_quantity=line.received_quantity,
                )
            )

        for receipt_order, receipt in enumerate(order.receipts):
            receipt_orm = PurchaseReceiptModel(
                id=receipt.id.value,
                purchase_order_id=order.id.value,
                receipt_order=receipt_order,
                receipt_reference=receipt.receipt_reference,
                received_at=receipt.received_at,
            )
            for receipt_line_order, receipt_line in enumerate(receipt.lines):
                receipt_orm.lines.append(
                    PurchaseReceiptLineModel(
                        purchase_receipt_id=receipt.id.value,
                        purchase_order_line_id=receipt_line.purchase_order_line_id.value,
                        receipt_line_order=receipt_line_order,
                        quantity=receipt_line.quantity,
                    )
                )
            orm.receipts.append(receipt_orm)

        return orm

    @staticmethod
    def to_domain_purchase_order(orm: PurchaseOrderModel) -> PurchaseOrder:
        lines = [
            PurchaseOrderLine(
                id=PurchaseOrderLineId(line_orm.id),
                description_snapshot=line_orm.description_snapshot,
                quantity=line_orm.quantity,
                unit_price=Money(
                    amount=line_orm.unit_price_amount,
                    currency=line_orm.unit_price_currency,
                ),
                inventory_item_reference=line_orm.inventory_item_reference,
                expected_delivery_at=(
                    None
                    if line_orm.expected_delivery_at is None
                    else PurchaseOrderMapper._normalize_timestamp(
                        line_orm.expected_delivery_at,
                    )
                ),
                line_note=line_orm.line_note,
                received_quantity=line_orm.received_quantity,
            )
            for line_orm in sorted(orm.lines, key=lambda item: item.line_order)
        ]

        receipts = []
        for receipt_orm in sorted(orm.receipts, key=lambda item: item.receipt_order):
            receipt_lines = [
                PurchaseReceiptLine(
                    purchase_order_line_id=PurchaseOrderLineId(
                        receipt_line_orm.purchase_order_line_id,
                    ),
                    quantity=receipt_line_orm.quantity,
                )
                for receipt_line_orm in sorted(
                    receipt_orm.lines,
                    key=lambda item: item.receipt_line_order,
                )
            ]

            receipts.append(
                PurchaseReceipt(
                    id=PurchaseReceiptId(receipt_orm.id),
                    receipt_reference=receipt_orm.receipt_reference,
                    received_at=PurchaseOrderMapper._normalize_timestamp(
                        receipt_orm.received_at,
                    ),
                    lines=receipt_lines,
                )
            )

        order = PurchaseOrder(
            id=PurchaseOrderId(orm.id),
            purchase_order_number=PurchaseOrderNumber(orm.purchase_order_number),
            supplier_reference=SupplierReference(orm.supplier_reference),
            status=orm.status,
            currency=orm.currency,
            created_at=PurchaseOrderMapper._normalize_timestamp(orm.order_created_at),
            lines=lines,
            supplier_name_snapshot=orm.supplier_name_snapshot,
            supplier_contact_snapshot=orm.supplier_contact_snapshot,
            notes=orm.notes,
            requested_by_reference=orm.requested_by_reference,
            approved_by_reference=orm.approved_by_reference,
            approved_at=(
                None
                if orm.approved_at is None
                else PurchaseOrderMapper._normalize_timestamp(orm.approved_at)
            ),
            ordered_at=(
                None
                if orm.ordered_at is None
                else PurchaseOrderMapper._normalize_timestamp(orm.ordered_at)
            ),
            external_order_reference=orm.external_order_reference,
            cancelled_at=(
                None
                if orm.cancelled_at is None
                else PurchaseOrderMapper._normalize_timestamp(orm.cancelled_at)
            ),
            cancellation_reason=orm.cancellation_reason,
            receipts=receipts,
        )
        order.pull_events()
        return order

    @staticmethod
    def _normalize_timestamp(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

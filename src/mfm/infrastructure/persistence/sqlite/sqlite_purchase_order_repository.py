"""SQLite repository for PurchaseOrder aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.database.mappers.purchase_order_mapper import PurchaseOrderMapper
from mfm.database.models.purchase_order_line_model import PurchaseOrderLineModel
from mfm.database.models.purchase_order_model import PurchaseOrderModel
from mfm.database.models.purchase_receipt_model import PurchaseReceiptModel
from mfm.domain.procurement.identifiers import PurchaseOrderNumber
from mfm.domain.procurement.identifiers import SupplierReference
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLitePurchaseOrderRepository(PurchaseOrderRepository):
    """SQLAlchemy-backed repository for PurchaseOrder aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, order: PurchaseOrder) -> None:
        number = order.purchase_order_number.value
        if self.exists_by_number(number):
            raise ValueError(f"Purchase order number {number} already exists")

        self._session.add(PurchaseOrderMapper.to_orm_purchase_order(order))
        self._session.flush()

    def get_by_id(self, purchase_order_id: UUID) -> PurchaseOrder | None:
        orm = self._session.scalar(
            self._base_query().where(PurchaseOrderModel.id == purchase_order_id)
        )
        if orm is None:
            return None
        return PurchaseOrderMapper.to_domain_purchase_order(orm)

    def get_by_number(
        self,
        purchase_order_number: PurchaseOrderNumber | str,
    ) -> PurchaseOrder | None:
        number = self._normalize_number(purchase_order_number)
        orm = self._session.scalar(
            self._base_query().where(PurchaseOrderModel.purchase_order_number == number)
        )
        if orm is None:
            return None
        return PurchaseOrderMapper.to_domain_purchase_order(orm)

    def update(self, order: PurchaseOrder) -> None:
        existing = self._session.scalar(
            self._base_query().where(PurchaseOrderModel.id == order.id.value)
        )
        if existing is None:
            raise ValueError(f"Purchase order {order.id.value} does not exist")

        duplicate = self._session.scalar(
            select(PurchaseOrderModel.id).where(
                PurchaseOrderModel.purchase_order_number == order.purchase_order_number.value,
                PurchaseOrderModel.id != order.id.value,
            )
        )
        if duplicate is not None:
            raise ValueError(
                f"Purchase order number {order.purchase_order_number.value} already exists"
            )

        self._session.merge(PurchaseOrderMapper.to_orm_purchase_order(order))
        self._session.flush()

    def exists_by_number(
        self,
        purchase_order_number: PurchaseOrderNumber | str,
    ) -> bool:
        number = self._normalize_number(purchase_order_number)
        return self._session.scalar(
            select(PurchaseOrderModel.id).where(
                PurchaseOrderModel.purchase_order_number == number
            )
        ) is not None

    def list(self) -> list[PurchaseOrder]:
        orm_entities = self._session.scalars(
            self._base_query().order_by(
                PurchaseOrderModel.purchase_order_number,
                PurchaseOrderModel.order_created_at,
            )
        ).unique().all()
        return [PurchaseOrderMapper.to_domain_purchase_order(orm) for orm in orm_entities]

    def list_by_state(
        self,
        status: PurchaseOrderStatus | str,
    ) -> list[PurchaseOrder]:
        normalized_status = self._normalize_status(status)
        orm_entities = self._session.scalars(
            self._base_query()
            .where(PurchaseOrderModel.status == normalized_status)
            .order_by(
                PurchaseOrderModel.purchase_order_number,
                PurchaseOrderModel.order_created_at,
            )
        ).unique().all()
        return [PurchaseOrderMapper.to_domain_purchase_order(orm) for orm in orm_entities]

    def list_by_supplier_reference(
        self,
        supplier_reference: SupplierReference | str,
    ) -> list[PurchaseOrder]:
        normalized_supplier = self._normalize_supplier_reference(supplier_reference)
        orm_entities = self._session.scalars(
            self._base_query()
            .where(PurchaseOrderModel.supplier_reference == normalized_supplier)
            .order_by(
                PurchaseOrderModel.purchase_order_number,
                PurchaseOrderModel.order_created_at,
            )
        ).unique().all()
        return [PurchaseOrderMapper.to_domain_purchase_order(orm) for orm in orm_entities]

    @staticmethod
    def _normalize_number(purchase_order_number: PurchaseOrderNumber | str) -> str:
        if isinstance(purchase_order_number, PurchaseOrderNumber):
            return purchase_order_number.value
        return PurchaseOrderNumber(purchase_order_number).value

    @staticmethod
    def _normalize_status(status: PurchaseOrderStatus | str) -> PurchaseOrderStatus:
        if isinstance(status, PurchaseOrderStatus):
            return status
        return PurchaseOrderStatus(status)

    @staticmethod
    def _normalize_supplier_reference(supplier_reference: SupplierReference | str) -> str:
        if isinstance(supplier_reference, SupplierReference):
            return supplier_reference.value
        return SupplierReference(supplier_reference).value

    @staticmethod
    def _base_query():
        return select(PurchaseOrderModel).options(
            joinedload(PurchaseOrderModel.lines).joinedload(
                PurchaseOrderLineModel.receipt_lines
            ),
            joinedload(PurchaseOrderModel.receipts).joinedload(
                PurchaseReceiptModel.lines
            ),
        )

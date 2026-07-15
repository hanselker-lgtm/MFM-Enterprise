"""Repository contract for PurchaseOrder aggregates."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.procurement.identifiers import PurchaseOrderNumber
from mfm.domain.procurement.identifiers import SupplierReference
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus


class PurchaseOrderRepository(ABC):
    """Persistence contract for PurchaseOrder aggregate roots."""

    @abstractmethod
    def add(self, order: PurchaseOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, purchase_order_id: UUID) -> PurchaseOrder | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_number(
        self,
        purchase_order_number: PurchaseOrderNumber | str,
    ) -> PurchaseOrder | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, order: PurchaseOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists_by_number(
        self,
        purchase_order_number: PurchaseOrderNumber | str,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[PurchaseOrder]:
        raise NotImplementedError

    @abstractmethod
    def list_by_state(
        self,
        status: PurchaseOrderStatus | str,
    ) -> list[PurchaseOrder]:
        raise NotImplementedError

    @abstractmethod
    def list_by_supplier_reference(
        self,
        supplier_reference: SupplierReference | str,
    ) -> list[PurchaseOrder]:
        raise NotImplementedError

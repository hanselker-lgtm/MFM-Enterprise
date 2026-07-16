from datetime import date
from decimal import Decimal

import pytest

from mfm.domain.accounting.cost_center_code import CostCenterCode
from mfm.domain.accounting.currency import Currency
from mfm.domain.accounting.document_reference import DocumentReference
from mfm.domain.accounting.exceptions import InvalidJournalReferenceError
from mfm.domain.accounting.money import Money
from mfm.domain.accounting.posting_date import PostingDate
from mfm.domain.accounting.project_reference import ProjectReference
from mfm.domain.accounting.vat_code import VatCode
from mfm.domain.accounting.voucher_number import VoucherNumber


def test_voucher_number_normalizes_uppercase():
    value = VoucherNumber(" vch-001 ")
    assert value.value == "VCH-001"


def test_posting_date_wraps_date_value():
    value = PostingDate(date(2026, 1, 15))
    assert value.year == 2026


def test_code_value_objects_normalize_uppercase():
    assert VatCode(" dk25 ").value == "DK25"
    assert CostCenterCode(" cc-100 ").value == "CC-100"
    assert ProjectReference(" proj-77 ").value == "PROJ-77"
    assert DocumentReference(" doc-abc ").value == "DOC-ABC"


def test_value_objects_reject_empty_or_spaced_values():
    with pytest.raises(InvalidJournalReferenceError):
        VoucherNumber(" ")
    with pytest.raises(InvalidJournalReferenceError):
        VatCode("A B")
    with pytest.raises(InvalidJournalReferenceError):
        CostCenterCode("A B")
    with pytest.raises(InvalidJournalReferenceError):
        ProjectReference("A B")
    with pytest.raises(InvalidJournalReferenceError):
        DocumentReference("A B")


def test_accounting_money_and_currency_reexports_work():
    amount = Money(amount="12.34", currency=Currency.DKK)
    assert amount.amount == Decimal("12.34")
    assert amount.currency == Currency.DKK

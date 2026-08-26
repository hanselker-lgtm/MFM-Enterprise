"""Primary membership billing workspace: fee schedules and billing runs."""

from __future__ import annotations

from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QDialogButtonBox
from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QSpinBox
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.membership_billing.membership_billing_controller import (
    MembershipBillingController,
)
from mfm.presentation.membership_billing.membership_billing_viewmodels import (
    FeeScheduleListItemViewModel,
    RunBillingCommandViewModel,
    SetupFeeScheduleCommandViewModel,
)


class _SetupFeeScheduleDialog(QDialog):
    """Form dialog for defining a fee schedule for a membership type."""

    def __init__(self, *, membership_types, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Opsæt gebyrplan")
        self._membership_types = membership_types

        self._type_combo = QComboBox()
        for mt in membership_types:
            self._type_combo.addItem(f"{mt.code} \u2014 {mt.name}", mt.membership_type_id)

        self._amount_input = QLineEdit()
        self._amount_input.setPlaceholderText("e.g. 250.00")

        self._currency_input = QLineEdit("DKK")
        self._currency_input.setMaxLength(3)

        self._due_days_input = QSpinBox()
        self._due_days_input.setRange(0, 365)
        self._due_days_input.setValue(30)

        form = QFormLayout()
        form.addRow("Medlemskabstype", self._type_combo)
        form.addRow("Gebyrbeløb", self._amount_input)
        form.addRow("Valuta", self._currency_input)
        form.addRow("Betalingsfrist (dage)", self._due_days_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def command(self) -> SetupFeeScheduleCommandViewModel | None:
        if self._type_combo.count() == 0:
            return None
        amount = self._amount_input.text().strip()
        currency = self._currency_input.text().strip().upper()
        if not amount or len(currency) != 3:
            return None
        selected = self._membership_types[self._type_combo.currentIndex()]
        return SetupFeeScheduleCommandViewModel(
            membership_type_id=selected.membership_type_id,
            membership_type_code=selected.code,
            membership_type_name=selected.name,
            amount=amount,
            currency=currency,
            due_days=self._due_days_input.value(),
        )


class _RunBillingDialog(QDialog):
    """Form dialog for running a billing pass against a fee schedule."""

    def __init__(self, *, membership_type_id, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Kør fakturering")
        self._membership_type_id = membership_type_id

        self._fiscal_year_input = QSpinBox()
        self._fiscal_year_input.setRange(2000, 2100)
        self._fiscal_year_input.setValue(date.today().year)

        self._dry_run_checkbox = QCheckBox("Prøvekørsel (kun forhåndsvisning, ingen fakturaer oprettes)")
        self._dry_run_checkbox.setChecked(True)

        form = QFormLayout()
        form.addRow("Regnskabsår", self._fiscal_year_input)
        form.addRow("", self._dry_run_checkbox)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def command(self) -> RunBillingCommandViewModel:
        return RunBillingCommandViewModel(
            membership_type_id=self._membership_type_id,
            fiscal_year=self._fiscal_year_input.value(),
            billing_date=date.today(),
            dry_run=self._dry_run_checkbox.isChecked(),
        )


class MembershipBillingWorkspace(QWidget):
    """Operational workspace for membership fee schedules and billing runs."""

    def __init__(self, *, controller: MembershipBillingController) -> None:
        super().__init__()
        self._controller = controller
        self._items: tuple[FeeScheduleListItemViewModel, ...] = ()

        toolbar = QHBoxLayout()
        refresh_button = QPushButton("Opdatér")
        refresh_button.setShortcut("F5")
        refresh_button.clicked.connect(self._handle_refresh)
        setup_button = QPushButton("Opsæt gebyrplan")
        setup_button.clicked.connect(self._handle_setup_fee_schedule)
        run_button = QPushButton("Kør fakturering")
        run_button.clicked.connect(self._handle_run_billing)
        toolbar.addWidget(refresh_button)
        toolbar.addWidget(setup_button)
        toolbar.addWidget(run_button)
        toolbar.addStretch(1)

        self._list = QListWidget()

        layout = QVBoxLayout(self)
        layout.addLayout(toolbar)
        layout.addWidget(QLabel("Gebyrplaner"))
        layout.addWidget(self._list)

        self._handle_refresh()

    def _handle_refresh(self) -> None:
        list_vm = self._controller.load_fee_schedule_list()
        self._items = list_vm.items
        self._list.clear()
        for item in self._items:
            list_item = QListWidgetItem(
                f"{item.membership_type_code} \u2014 {item.membership_type_name}: "
                f"{item.fee_amount} {item.currency}, due in {item.due_days} days "
                f"({item.reminder_count} reminders)"
            )
            list_item.setData(Qt.ItemDataRole.UserRole, item.membership_type_id)
            self._list.addItem(list_item)

    def _handle_setup_fee_schedule(self) -> None:
        membership_types = self._controller.load_membership_type_options()
        if not membership_types:
            QMessageBox.information(
                self,
                "Opsæt gebyrplan",
                "Der er endnu ikke oprettet nogen medlemskabstyper. Opret én under Medlemskaber først.",
            )
            return

        dialog = _SetupFeeScheduleDialog(membership_types=membership_types, parent=self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        command = dialog.command()
        if command is None:
            QMessageBox.warning(self, "Opsæt gebyrplan", "Beløb og valuta skal udfyldes.")
            return
        try:
            self._controller.setup_fee_schedule(command)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user, not swallowed
            QMessageBox.critical(self, "Opsæt gebyrplan", str(exc))
            return
        self._handle_refresh()

    def _handle_run_billing(self) -> None:
        current_row = self._list.currentRow()
        if current_row < 0 or current_row >= len(self._items):
            QMessageBox.information(
                self, "Kør fakturering", "Vælg en gebyrplan at fakturere for."
            )
            return

        membership_type_id = self._items[current_row].membership_type_id
        dialog = _RunBillingDialog(membership_type_id=membership_type_id, parent=self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        try:
            result = self._controller.run_billing(dialog.command())
        except Exception as exc:  # noqa: BLE001 - surfaced to the user, not swallowed
            QMessageBox.critical(self, "Kør fakturering", str(exc))
            return

        QMessageBox.information(
            self,
            "Kør fakturering",
            f"Behandlede {result.processed} medlem(mer), oprettede {result.invoices_created} faktura(er).",
        )
        self._handle_refresh()

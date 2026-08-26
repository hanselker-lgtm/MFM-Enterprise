"""Primary organization management workspace."""

from __future__ import annotations

from PySide6.QtCore import Qt
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
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.organizations.organization_controller import OrganizationController
from mfm.presentation.organizations.organization_viewmodels import (
    CreateOrganizationCommandViewModel,
    OrganizationListItemViewModel,
    UpdateOrganizationCommandViewModel,
)

_ORGANIZATION_TYPES = ("ASSOCIATION", "FOUNDATION", "COMPANY", "COMMITTEE", "OTHER")
_ORGANIZATION_STATUSES = ("ACTIVE", "INACTIVE", "ARCHIVED")

_ORGANIZATION_TYPE_LABELS = {
    "ASSOCIATION": "Forening",
    "FOUNDATION": "Fond",
    "COMPANY": "Virksomhed",
    "COMMITTEE": "Udvalg",
    "OTHER": "Andet",
}
_ORGANIZATION_STATUS_LABELS = {
    "ACTIVE": "Aktiv",
    "INACTIVE": "Inaktiv",
    "ARCHIVED": "Arkiveret",
}


def _populate_type_combo(combo: QComboBox) -> None:
    for value in _ORGANIZATION_TYPES:
        combo.addItem(_ORGANIZATION_TYPE_LABELS[value], value)


def _populate_status_combo(combo: QComboBox) -> None:
    for value in _ORGANIZATION_STATUSES:
        combo.addItem(_ORGANIZATION_STATUS_LABELS[value], value)


def _select_by_value(combo: QComboBox, value: str) -> None:
    index = combo.findData(value)
    if index >= 0:
        combo.setCurrentIndex(index)


class _CreateOrganizationDialog(QDialog):
    """Form dialog for registering a new organization."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Ny organisation")

        self._number_input = QLineEdit()
        self._name_input = QLineEdit()
        self._type_combo = QComboBox()
        _populate_type_combo(self._type_combo)

        form = QFormLayout()
        form.addRow("Organisationsnummer", self._number_input)
        form.addRow("Navn", self._name_input)
        form.addRow("Type", self._type_combo)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def command(self) -> CreateOrganizationCommandViewModel | None:
        number = self._number_input.text().strip()
        name = self._name_input.text().strip()
        if not number or not name:
            return None
        return CreateOrganizationCommandViewModel(
            organization_number=number,
            name=name,
            organization_type=self._type_combo.currentData(),
        )


class _EditOrganizationDialog(QDialog):
    """Form dialog for editing an existing organization's name/type/status."""

    def __init__(self, *, item: OrganizationListItemViewModel, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"Redigér {item.name}")
        self._organization_id = item.organization_id

        self._name_input = QLineEdit(item.name)
        self._type_combo = QComboBox()
        _populate_type_combo(self._type_combo)
        _select_by_value(self._type_combo, item.organization_type)
        self._status_combo = QComboBox()
        _populate_status_combo(self._status_combo)
        _select_by_value(self._status_combo, item.status)

        form = QFormLayout()
        form.addRow("Navn", self._name_input)
        form.addRow("Type", self._type_combo)
        form.addRow("Status", self._status_combo)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def command(self) -> UpdateOrganizationCommandViewModel | None:
        name = self._name_input.text().strip()
        if not name:
            return None
        return UpdateOrganizationCommandViewModel(
            organization_id=self._organization_id,
            name=name,
            organization_type=self._type_combo.currentData(),
            status=self._status_combo.currentData(),
        )


class OrganizationWorkspace(QWidget):
    """Operational workspace for organization management."""

    def __init__(self, *, controller: OrganizationController) -> None:
        super().__init__()
        self._controller = controller
        self._items: tuple[OrganizationListItemViewModel, ...] = ()

        toolbar = QHBoxLayout()
        refresh_button = QPushButton("Opdatér")
        refresh_button.setShortcut("F5")
        refresh_button.clicked.connect(self._handle_refresh)
        create_button = QPushButton("Ny organisation")
        create_button.clicked.connect(self._handle_create)
        edit_button = QPushButton("Redigér valgte")
        edit_button.clicked.connect(self._handle_edit)
        toolbar.addWidget(refresh_button)
        toolbar.addWidget(create_button)
        toolbar.addWidget(edit_button)
        toolbar.addStretch(1)

        self._list = QListWidget()

        layout = QVBoxLayout(self)
        layout.addLayout(toolbar)
        layout.addWidget(QLabel("Organisationer"))
        layout.addWidget(self._list)

        self._handle_refresh()

    def _handle_refresh(self) -> None:
        list_vm = self._controller.load_organization_list()
        self._items = list_vm.items
        self._list.clear()
        for item in self._items:
            type_label = _ORGANIZATION_TYPE_LABELS.get(item.organization_type, item.organization_type)
            status_label = _ORGANIZATION_STATUS_LABELS.get(item.status, item.status)
            list_item = QListWidgetItem(
                f"{item.organization_number} \u2014 {item.name} "
                f"({type_label}, {status_label})"
            )
            list_item.setData(Qt.ItemDataRole.UserRole, item.organization_id)
            self._list.addItem(list_item)

    def _handle_create(self) -> None:
        dialog = _CreateOrganizationDialog(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        command = dialog.command()
        if command is None:
            QMessageBox.warning(self, "Ny organisation", "Nummer og navn skal udfyldes.")
            return
        try:
            self._controller.create_organization(command)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user, not swallowed
            QMessageBox.critical(self, "Ny organisation", str(exc))
            return
        self._handle_refresh()

    def _handle_edit(self) -> None:
        row = self._list.currentRow()
        if row < 0 or row >= len(self._items):
            QMessageBox.information(self, "Redigér organisation", "Vælg en organisation at redigere.")
            return

        dialog = _EditOrganizationDialog(item=self._items[row], parent=self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        command = dialog.command()
        if command is None:
            QMessageBox.warning(self, "Redigér organisation", "Navn skal udfyldes.")
            return
        try:
            self._controller.update_organization(command)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user, not swallowed
            QMessageBox.critical(self, "Redigér organisation", str(exc))
            return
        self._handle_refresh()

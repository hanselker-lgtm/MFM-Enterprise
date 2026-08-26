"""Primary membership management workspace."""

from __future__ import annotations

from datetime import date
from uuid import UUID

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
from PySide6.QtWidgets import QSplitter
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from mfm.presentation.memberships.membership_controller import MembershipController
from mfm.presentation.memberships.membership_viewmodels import (
    CreateMemberCommandViewModel,
    MemberListItemViewModel,
    RegisterMembershipCommandViewModel,
)


class _CreateMemberDialog(QDialog):
    """Small form dialog for registering a new member."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Nyt medlem")

        self._contact_number = QLineEdit()
        self._member_number = QLineEdit()
        self._first_name = QLineEdit()
        self._last_name = QLineEdit()

        form = QFormLayout()
        form.addRow("Kontaktnummer", self._contact_number)
        form.addRow("Medlemsnummer", self._member_number)
        form.addRow("Fornavn", self._first_name)
        form.addRow("Efternavn", self._last_name)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def command(self) -> CreateMemberCommandViewModel | None:
        contact_number = self._contact_number.text().strip()
        member_number = self._member_number.text().strip()
        first_name = self._first_name.text().strip()
        last_name = self._last_name.text().strip()
        if not (contact_number and member_number and first_name and last_name):
            return None
        return CreateMemberCommandViewModel(
            contact_number=contact_number,
            member_number=member_number,
            first_name=first_name,
            last_name=last_name,
            join_date=date.today(),
        )


class MembershipToolbar(QWidget):
    """Search box and primary actions for the Memberships workspace."""

    def __init__(self, *, on_search, on_refresh, on_create_member) -> None:
        super().__init__()
        self._on_search = on_search

        self._search_input = QLineEdit()
        self._search_input.setPlaceholderText("Filtrér efter navn eller medlemsnummer")
        self._search_input.textChanged.connect(lambda _: self._on_search())

        refresh_button = QPushButton("Opdatér")
        refresh_button.setShortcut("F5")
        refresh_button.clicked.connect(on_refresh)

        create_button = QPushButton("Nyt medlem")
        create_button.clicked.connect(on_create_member)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel("Søg"))
        layout.addWidget(self._search_input)
        layout.addStretch(1)
        layout.addWidget(refresh_button)
        layout.addWidget(create_button)

    def filter_text(self) -> str:
        return self._search_input.text().strip().lower()


class MemberListView(QListWidget):
    """List of members; selecting one loads its detail."""

    def __init__(self, *, on_select) -> None:
        super().__init__()
        self._on_select = on_select
        self._items: tuple[MemberListItemViewModel, ...] = ()
        self.currentRowChanged.connect(self._handle_row_changed)

    def set_items(self, items: tuple[MemberListItemViewModel, ...]) -> None:
        self._items = items
        self.clear()
        for item in items:
            list_item = QListWidgetItem(
                f"{item.member_number} \u2014 {item.display_name} ({item.status})"
            )
            list_item.setData(Qt.ItemDataRole.UserRole, item.member_id)
            self.addItem(list_item)

    def _handle_row_changed(self, row: int) -> None:
        if row < 0 or row >= len(self._items):
            return
        self._on_select(self._items[row].member_id)


class MemberDetailView(QWidget):
    """Detail panel for the selected member, including their memberships."""

    def __init__(self, *, on_register_membership) -> None:
        super().__init__()
        self._on_register_membership = on_register_membership
        self._current_member_id: UUID | None = None

        self._title = QLabel("Vælg et medlem")
        self._title.setStyleSheet("font-weight: bold; font-size: 14px;")
        self._number_label = QLabel("")
        self._status_label = QLabel("")
        self._join_date_label = QLabel("")

        self._memberships_list = QListWidget()

        register_button = QPushButton("Registrér medlemskab")
        register_button.clicked.connect(self._handle_register_membership)

        layout = QVBoxLayout(self)
        layout.addWidget(self._title)
        layout.addWidget(self._number_label)
        layout.addWidget(self._status_label)
        layout.addWidget(self._join_date_label)
        layout.addWidget(QLabel("Medlemskaber"))
        layout.addWidget(self._memberships_list)
        layout.addWidget(register_button)
        layout.addStretch(1)

    def show_detail(self, detail) -> None:
        self._current_member_id = detail.member_id
        self._title.setText(detail.display_name)
        self._number_label.setText(f"Member number: {detail.member_number}")
        self._status_label.setText(f"Status: {detail.status}")
        self._join_date_label.setText(f"Joined: {detail.join_date.isoformat()}")

        self._memberships_list.clear()
        for record in detail.memberships:
            self._memberships_list.addItem(
                f"{record.membership_type_name} ({record.status}) "
                f"from {record.start_date.isoformat()}"
            )

    def _handle_register_membership(self) -> None:
        if self._current_member_id is not None:
            self._on_register_membership(self._current_member_id)


class MembershipWorkspace(QWidget):
    """Operational workspace for member and membership management."""

    def __init__(self, *, controller: MembershipController) -> None:
        super().__init__()
        self._controller = controller
        self._all_items: tuple[MemberListItemViewModel, ...] = ()

        self._toolbar = MembershipToolbar(
            on_search=self._handle_filter_changed,
            on_refresh=self._handle_refresh,
            on_create_member=self._handle_create_member,
        )
        self._list = MemberListView(on_select=self._handle_select_member)
        self._detail = MemberDetailView(on_register_membership=self._handle_register_membership)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self._list)
        splitter.addWidget(self._detail)
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)

        layout = QVBoxLayout(self)
        layout.addWidget(self._toolbar)
        layout.addWidget(splitter)

        self._handle_refresh()

    def _handle_refresh(self) -> None:
        list_vm = self._controller.load_member_list()
        self._all_items = list_vm.items
        self._apply_filter()

    def _handle_filter_changed(self) -> None:
        self._apply_filter()

    def _apply_filter(self) -> None:
        text = self._toolbar.filter_text()
        if not text:
            visible = self._all_items
        else:
            visible = tuple(
                item
                for item in self._all_items
                if text in item.display_name.lower() or text in item.member_number.lower()
            )
        self._list.set_items(visible)

    def _handle_select_member(self, member_id: UUID) -> None:
        detail = self._controller.load_member_detail(member_id)
        self._detail.show_detail(detail)

    def _handle_create_member(self) -> None:
        dialog = _CreateMemberDialog(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        command = dialog.command()
        if command is None:
            QMessageBox.warning(self, "Nyt medlem", "Alle felter skal udfyldes.")
            return
        try:
            self._controller.create_member(command)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user, not swallowed
            QMessageBox.critical(self, "Nyt medlem", str(exc))
            return
        self._handle_refresh()

    def _handle_register_membership(self, member_id: UUID) -> None:
        options = self._controller.load_membership_type_options()
        if not options:
            QMessageBox.information(
                self,
                "Registrér medlemskab",
                "Der er endnu ikke oprettet nogen medlemskabstyper.",
            )
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Registrér medlemskab")
        combo = QComboBox()
        for option in options:
            combo.addItem(f"{option.code} \u2014 {option.name}", option.membership_type_id)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel("Medlemskabstype"))
        layout.addWidget(combo)
        layout.addWidget(buttons)

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        membership_type_id = combo.currentData()
        try:
            self._controller.register_membership(
                RegisterMembershipCommandViewModel(
                    member_id=member_id, membership_type_id=membership_type_id
                )
            )
        except Exception as exc:  # noqa: BLE001 - surfaced to the user, not swallowed
            QMessageBox.critical(self, "Registrér medlemskab", str(exc))
            return

        self._handle_select_member(member_id)

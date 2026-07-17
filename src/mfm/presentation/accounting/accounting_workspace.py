"""Operational accounting workspace."""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget
from PySide6.QtWidgets import QInputDialog
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QSplitter
from PySide6.QtWidgets import QTabWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.presentation.accounting.accounting_controller import AccountingController
from mfm.presentation.accounting.accounting_toolbar import AccountingToolbar
from mfm.presentation.accounting.accounting_viewmodels import CreateJournalCommandViewModel
from mfm.presentation.accounting.accounting_viewmodels import JournalListFilterViewModel
from mfm.presentation.accounting.journal_detail_view import JournalDetailView
from mfm.presentation.accounting.journal_list_view import JournalListView


class AccountingWorkspace(QWidget):
    """Operational workspace for accounting management."""

    def __init__(self, *, controller: AccountingController) -> None:
        super().__init__()
        self._controller = controller
        self._current_filters = JournalListFilterViewModel()

        self._toolbar = AccountingToolbar(
            on_search=self._handle_search,
            on_refresh=self._handle_refresh,
            on_create_journal=self._handle_create_journal,
            on_post_journal=self._handle_post_journal,
        )
        self._list = JournalListView(
            on_open_journal=self._handle_open_journal,
            on_page_change=self._handle_page_change,
        )
        self._detail = JournalDetailView(
            on_open_project=self._controller.open_project,
            on_open_fiscal_year=self._controller.open_fiscal_year,
        )

        journals_split = QSplitter(Qt.Orientation.Horizontal)
        journals_split.addWidget(self._list)
        journals_split.addWidget(self._detail)
        journals_split.setStretchFactor(0, 2)
        journals_split.setStretchFactor(1, 3)

        tabs = QTabWidget()
        tabs.addTab(journals_split, "Journals")
        tabs.addTab(self._placeholder("Ledger pane reserved for future capability"), "Ledger")
        tabs.addTab(self._placeholder("Reporting pane reserved for future capability"), "Reporting")

        layout = QVBoxLayout(self)
        layout.addWidget(self._toolbar)
        layout.addWidget(tabs)

        self._handle_search()

    def create_detail_dock_widget(self, parent: QMainWindow | None = None) -> QDockWidget:
        """Provide a future-ready detachable detail pane."""
        dock = QDockWidget("Journal Detail", parent)
        dock.setWidget(self._detail)
        dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea
            | Qt.DockWidgetArea.RightDockWidgetArea
            | Qt.DockWidgetArea.BottomDockWidgetArea
        )
        return dock

    def _handle_search(self) -> None:
        filters = self._toolbar.filters(page=self._current_filters.page, page_size=self._current_filters.page_size)
        self._current_filters = filters
        list_vm = self._controller.load_journal_list(filters=filters)
        self._list.set_view_model(list_vm)

    def _handle_refresh(self) -> None:
        list_vm, detail_vm = self._controller.refresh()
        self._list.set_view_model(list_vm)
        if detail_vm is not None:
            self._detail.set_view_model(detail_vm)

    def _handle_open_journal(self, journal_id: UUID) -> None:
        detail_vm = self._controller.open_journal(journal_id)
        self._detail.set_view_model(detail_vm)

    def _handle_page_change(self, direction: int) -> None:
        next_page = max(self._current_filters.page + direction, 1)
        filters = JournalListFilterViewModel(
            text=self._current_filters.text,
            status=self._current_filters.status,
            fiscal_year=self._current_filters.fiscal_year,
            sort_by=self._current_filters.sort_by,
            descending=self._current_filters.descending,
            page=next_page,
            page_size=self._current_filters.page_size,
        )
        self._current_filters = filters
        list_vm = self._controller.load_journal_list(filters=filters)
        self._list.set_view_model(list_vm)

    def _handle_create_journal(self) -> None:
        project_id_text, ok_project = QInputDialog.getText(self, "Create Journal", "Project ID")
        if not ok_project:
            return

        journal_number, ok_journal = QInputDialog.getText(self, "Create Journal", "Journal number")
        if not ok_journal or not journal_number.strip():
            return

        amount_text, ok_amount = QInputDialog.getText(self, "Create Journal", "Amount")
        if not ok_amount or not amount_text.strip():
            return

        try:
            project_id = UUID(project_id_text.strip())
            amount = Decimal(amount_text.strip())
        except (ValueError, ArithmeticError):
            QMessageBox.warning(self, "Create Journal", "Invalid project id or amount")
            return

        debit_account_id = UUID("00000000-0000-0000-0000-000000000101")
        credit_account_id = UUID("00000000-0000-0000-0000-000000000202")

        journal_id = self._controller.create_journal(
            CreateJournalCommandViewModel(
                project_id=project_id,
                journal_number=journal_number.strip(),
                posting_date=date.today(),
                description=f"Journal {journal_number.strip()}",
                debit_account_id=debit_account_id,
                credit_account_id=credit_account_id,
                amount=amount,
            )
        )
        QMessageBox.information(self, "Journal Created", f"Journal created: {journal_id}")
        self._handle_refresh()

    def _handle_post_journal(self) -> None:
        if self._controller.last_selected_journal_id is None:
            QMessageBox.warning(self, "Post Journal", "No journal selected")
            return
        self._controller.post_journal(self._controller.last_selected_journal_id)
        self._handle_refresh()

    @staticmethod
    def _placeholder(text: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel(text))
        return widget

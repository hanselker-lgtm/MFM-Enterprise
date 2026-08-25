# MFM Product v0.1

A first working product baseline for MaritimForeningsManager.

## What is implemented

- SQLite database with migrations
- Dashboard
- Projects
- Tasks
- Risks
- Decisions
- Accounting core: chart of accounts, balanced journals, posting, trial balance, fiscal years, periods, automatic journal numbering, income statement, balance sheet, project budgets and budget-vs-actual
- Members: member register, membership types, memberships and membership invoices
- Application/service/repository separation
- No external dependency for the first GUI baseline (Tkinter)

## Start

From the project root:

```text
python run.py
```

The database is created automatically in `data/mfm.db`.

## First product principle

This release is deliberately small. It implements working business functions rather than additional governance documents.

Next implementation target:
- accounting core
- members
- documents
- reporting
- backup/restore
- AI assistant

- Membership payments: payment registration, invoice status and automatic bank/receivable posting

- Bank: bank accounts, bank transactions, unmatched items and journal reconciliation

- Management dashboard: operational snapshot and prioritized attention items

- Security foundation: users, roles and password hashing with PBKDF2-HMAC-SHA256

- System: SQLite backup/restore foundation and application settings

- Global search: members, projects, tasks, risks, decisions, accounts, journals and invoices

- Export: UTF-8 CSV exports for members, projects, journals, invoices, bank transactions and trial balance

- Organization setup: name, registration number, address, contact details, currency and fiscal-year start

- Role permissions: granular permissions for Administrator, Manager and User

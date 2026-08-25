# MFM v1.1-150 – Accounting Module Implementation

Version: 1.1

Document ID: MFM-v1.1-150

Status: Technical Implementation

---

# 1. Purpose

The Accounting Module is the financial core of MaritimForeningsManager (MFM) v1.1.

It is the **only authoritative financial ledger** within the application.

All actual financial transactions originate, are validated, posted and reported from this module.

No other module may maintain parallel financial records.

---

# 2. Responsibilities

The Accounting Module is responsible for:

- Chart of Accounts
- Journal Entries
- Double-Entry Bookkeeping
- Fiscal Years
- General Ledger
- Trial Balance
- Balance Sheet
- Income Statement
- VAT Registration (optional)
- Bank Reconciliation
- Financial Reporting

---

# 3. Architectural Principles

Accounting follows four fundamental principles.

## Single Financial Truth

Only one financial ledger exists.

## Double Entry Bookkeeping

Every financial transaction consists of balanced debit and credit entries.

## Immutable Posting

Posted vouchers cannot be edited.

Corrections are made through reversing entries.

## Complete Auditability

Every financial operation is traceable.

---

# 4. Module Architecture

```
Accounting GUI

↓

Accounting Controller

↓

Accounting Service

↓

Voucher Service

↓

Repositories

↓

SQLite Database
```

Business rules exist only in the Service Layer.

---

# 5. Core Entities

```
ChartOfAccount

Account

FiscalYear

Voucher

VoucherLine

Journal

Posting

BankTransaction

VATCode

CostCenter

ProjectReference
```

---

# 6. Chart of Accounts

Each account contains:

```
Account Number

Account Name

Account Type

Parent Account

VAT Code

Normal Balance

Active Status
```

Account types:

- Assets
- Liabilities
- Equity
- Income
- Expenses

---

# 7. Fiscal Years

Each fiscal year contains:

```
Fiscal Year

Start Date

End Date

Status

Opening Date

Closing Date
```

Status:

- Planned
- Open
- Closed
- Archived

Closed fiscal years are read-only.

---

# 8. Voucher Lifecycle

```
Draft

↓

Validated

↓

Posted

↓

Locked

↓

Archived
```

Only validated vouchers may be posted.

---

# 9. Voucher Structure

Voucher Header

```
Voucher Number

Voucher Date

Description

Reference

Created By

Approved By

Posting Date
```

Voucher Lines

```
Account

Debit

Credit

Description

Project Reference

Grant Reference

Member Reference
```

---

# 10. Posting Rules

The following rules always apply:

- Debit equals Credit.
- Voucher must contain at least two lines.
- Accounts must exist.
- Fiscal Year must be open.
- Posting date must be valid.
- User must have posting permission.

Posting is atomic.

---

# 11. Journal Types

Supported journals:

- General Journal
- Cash Journal
- Bank Journal
- Membership Journal
- Grant Journal
- Adjustment Journal
- Opening Journal
- Closing Journal

Journal numbering is automatic.

---

# 12. Bank Transactions

Bank records include:

```
Transaction Date

Reference

Amount

Description

Bank Account

Reconciliation Status
```

Supported states:

- Imported
- Matched
- Posted
- Reconciled

---

# 13. VAT Handling

VAT support includes:

- VAT Codes
- VAT Rates
- VAT Reports
- VAT Validation

VAT functionality can be disabled for associations not registered for VAT.

---

# 14. Cost Centres

Optional support for:

- Departments
- Activities
- Events
- Operational Areas

Cost Centres support management reporting but do not replace project accounting.

---

# 15. Project References

Accounting entries may reference:

- Project
- Grant
- Member
- Document

References are informational and do not create duplicate financial records.

---

# 16. Financial Statements

The module generates:

- Trial Balance
- Balance Sheet
- Income Statement
- General Ledger
- Account Specification
- Journal Report

Reports are generated directly from posted accounting entries.

---

# 17. Bank Reconciliation

The reconciliation process:

```
Import Bank Transactions

↓

Match Transactions

↓

Validate

↓

Approve

↓

Reconciled
```

Manual matching is supported.

---

# 18. Period Closing

Closing procedure:

```
Verify Ledger

↓

Verify Trial Balance

↓

Post Adjustments

↓

Close Fiscal Year

↓

Archive
```

Closed periods cannot be modified.

---

# 19. Security

Permissions include:

- View Accounts
- Create Voucher
- Edit Draft Voucher
- Post Voucher
- Reverse Voucher
- Close Fiscal Year
- Export Financial Reports

Financial authority is role-based.

---

# 20. Audit

The following actions are audited:

- Voucher Created
- Voucher Edited
- Voucher Posted
- Voucher Reversed
- Fiscal Year Opened
- Fiscal Year Closed
- Bank Reconciliation
- Report Export

Audit records are immutable.

---

# 21. Integration

## Membership

Membership fees generate accounting requests.

Accounting performs the actual posting.

---

## Projects

Projects provide references only.

No financial balances are stored in the Project Module.

---

## Grants

Grant awards provide funding references.

Cash receipts and expenditure are recorded only in Accounting.

---

## Documents

Every voucher may reference one or more supporting documents.

Document storage remains the responsibility of the Document Service.

---

## Reporting

Reporting retrieves financial data exclusively from posted accounting entries.

---

# 22. Validation Rules

Examples:

- Debit equals Credit.
- Voucher Number is unique.
- Account exists.
- Posting Date belongs to an open fiscal year.
- Negative debit or credit values are not permitted.
- Closed fiscal years reject new postings.

---

# 23. Performance

Target capacities:

- 1,000 Accounts
- 250 Fiscal Years
- 1,000,000 Journal Lines
- 250,000 Vouchers

Performance target:

Voucher posting below one second under normal operating conditions.

---

# 24. Future Enhancements

Future releases may support:

- Electronic Bank Import (ISO 20022/CAMT)
- OCR Invoice Recognition
- Electronic Invoice Export (OIOUBL/Peppol)
- Payment File Generation
- Budget Forecasting
- Multi-Currency
- Fixed Asset Register

These features shall extend the Accounting Module without compromising its role as the single financial authority.

---

# 25. Summary

The Accounting Module is the financial foundation of MFM v1.1.

It provides a complete double-entry bookkeeping system with strong validation, comprehensive audit logging and seamless integration with the Membership, Project, Grant, Document and Reporting modules.

The architecture guarantees that all financial information originates from one authoritative ledger while allowing other modules to reference financial information without creating duplicate accounting records.

---

# Next Document

**MFM v1.1-160 – Project Management Module Implementation**

---

# END OF DOCUMENT
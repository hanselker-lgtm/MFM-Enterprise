# MFM v1.0 ACCOUNTING CORE IMPLEMENTATION

## MaritimForeningsManager — Konkret implementeringsgrundlag for kontoplan, bilag, postering, finansår, kasse/bank og regnskabsrapportering

**Version:** 1.0  
**Status:** Implementation Baseline  
**Parent:** MFM v1.0 Security & User Implementation  
**Purpose:** Establish a simple, reliable and auditable accounting core for a small non-profit association

---

# 1. Purpose

This document defines the concrete implementation baseline for the MFM v1.0 accounting module.

The accounting core SHALL provide:

```text
CHART OF ACCOUNTS
FINANCIAL YEARS
VOUCHERS
VOUCHER LINES
DEBIT / CREDIT
POSTING
REVERSAL
GENERAL LEDGER
TRIAL BALANCE
INCOME STATEMENT
BALANCE SHEET
CASH / BANK
RECONCILIATION
ACCOUNTING AUDIT
```

The design SHALL remain appropriate for a small non-profit association.

---

# 2. Accounting Principle

> **Financial correctness is more important than convenience.**

MFM SHALL never silently create an unbalanced posted transaction.

---

# 3. Scope

Mandatory v1.0:

```text
Chart of Accounts
Financial Year
Voucher
Voucher Lines
Draft
Validation
Posting
Reversal
General Ledger
Trial Balance
Income Statement
Balance Sheet
Cash / Bank Accounts
Basic Bank Reconciliation
Project Tagging
Audit
```

Optional later:

```text
advanced budgeting
automatic bank import
OCR
electronic invoicing
VAT automation
multi-currency
```

---

# 4. Accounting Architecture

```text
GUI
 ↓
AccountingService
 ↓
Accounting Security Check
 ↓
Validation
 ↓
Transaction
 ↓
AccountingRepository
 ↓
SQLite
 ↓
AuditService
```

Reports read the posted accounting data.

---

# 5. Financial Truth

The authoritative accounting record is:

```text
POSTED VOUCHER
+
POSTED VOUCHER LINES
```

Drafts do not affect official reports.

---

# 6. Double-Entry Principle

Every posted voucher SHALL satisfy:

```text
TOTAL DEBIT = TOTAL CREDIT
```

If:

```text
Debit = 1,000.00
Credit = 900.00
```

posting SHALL be rejected.

---

# 7. Currency

Default currency:

```text
DKK
```

The v1.0 accounting core SHALL assume one primary currency.

---

# 8. Money Representation

Authoritative financial calculations SHALL use:

```text
Decimal
```

or integer minor units.

Python `float` SHALL not be used for authoritative accounting arithmetic.

---

# 9. Decimal Precision

A practical baseline:

```text
2 decimal places
```

for DKK amounts.

---

# 10. Rounding

Rounding SHALL occur deliberately at defined financial boundaries.

Avoid repeated intermediate rounding.

---

# 11. Financial Year

MFM SHALL support financial years.

Minimum:

```text
year
start_date
end_date
status
```

---

# 12. Financial Year Status

Recommended:

```text
OPEN
CLOSED
```

A closed financial year SHALL not accept normal new postings.

---

# 13. Current Financial Year

The application SHALL identify the active financial year.

Only one financial year should normally be open for ordinary posting unless future requirements explicitly support multiple open years.

---

# 14. Closing Financial Year

Closing a year SHALL be an authorised administrative operation.

Before closure:

```text
trial balance
reports
reconciliation
```

SHOULD be reviewed.

---

# 15. Reopening Year

Reopening a closed financial year SHALL require explicit permission.

It SHALL be audited.

---

# 16. Financial Year Validation

A voucher date SHALL belong to an appropriate financial year.

If no applicable year exists:

```text
posting denied
```

---

# 17. Chart of Accounts

The chart of accounts defines:

```text
account number
account name
account type
active status
```

Optional:

```text
description
```

---

# 18. Account Types

Minimum:

```text
ASSET
LIABILITY
EQUITY
INCOME
EXPENSE
```

---

# 19. Account Number

Account numbers SHALL be unique.

The association may choose its own numbering scheme.

---

# 20. Example Chart

Illustrative only:

```text
1000 Bank
1100 Cash
1200 Receivables
2000 Payables
3000 Equity / Opening Balance
4000 Membership Income
4100 Grants
5000 Materials
5100 Maintenance
5200 Administration
5300 Insurance
5400 Bank Fees
```

The actual chart SHALL be configurable.

---

# 21. Account Active Status

An account MAY be:

```text
ACTIVE
INACTIVE
```

Inactive accounts SHALL not be used for new postings.

Historical postings remain valid.

---

# 22. Account Deletion

Accounts with accounting history SHALL not be physically deleted.

They should be deactivated.

---

# 23. Account Repository

`AccountRepository` SHOULD support:

```text
get_by_id()
get_by_number()
list_active()
create()
update()
deactivate()
```

---

# 24. Account Service

`AccountingService` or a dedicated `AccountService` SHALL enforce:

```text
unique number
valid name
valid type
active status
```

---

# 25. Voucher

A voucher represents one accounting event.

Minimum:

```text
id
voucher_number
financial_year_id
voucher_date
description
status
created_by
created_at
posted_by
posted_at
```

---

# 26. Voucher Status

Recommended:

```text
DRAFT
POSTED
REVERSED
```

---

# 27. Draft Voucher

Draft vouchers MAY be:

```text
created
edited
validated
deleted
```

subject to permissions.

They do not affect official reports.

---

# 28. Posted Voucher

A posted voucher is authoritative accounting history.

It SHALL not be silently edited.

---

# 29. Reversed Voucher

A reversed voucher remains in the historical record.

A separate reversal voucher SHALL offset the original.

---

# 30. Voucher Number

Voucher numbers SHALL be unique within the defined numbering scope.

A simple v1.0 model:

```text
financial year + sequential number
```

Example:

```text
2026-0001
2026-0002
```

---

# 31. Voucher Number Generation

Voucher numbers SHALL be generated safely to avoid duplicates.

The number SHALL not depend solely on GUI state.

---

# 32. Voucher Date

Voucher date SHALL be a valid calendar date.

---

# 33. Voucher Description

Description SHALL provide enough context to identify the transaction.

---

# 34. Voucher Line

Each voucher contains one or more lines.

Minimum:

```text
id
voucher_id
line_number
account_id
debit
credit
description
project_id
```

`project_id` may be nullable.

---

# 35. Debit and Credit

Each line SHALL have:

```text
debit >= 0
credit >= 0
```

A normal line SHALL not have both debit and credit greater than zero.

---

# 36. Zero Line

A voucher line with:

```text
debit = 0
credit = 0
```

SHALL normally be rejected.

---

# 37. Voucher Minimum Lines

A valid posted voucher SHALL have at least:

```text
2 lines
```

---

# 38. Balanced Voucher

Posting condition:

```text
SUM(debit) = SUM(credit)
```

---

# 39. Positive Total

Total debit and total credit SHALL be greater than zero for a posted voucher.

---

# 40. Example

Valid:

```text
Debit  Bank        1,000
Credit Grant       1,000
```

Invalid:

```text
Debit  Bank        1,000
Credit Grant         900
```

---

# 41. Voucher Validation

Before posting:

```text
date valid
financial year valid
description valid
lines exist
accounts valid
accounts active
amounts valid
debit = credit
```

---

# 42. Validation Service

A dedicated validation method MAY return:

```text
ValidationResult
```

containing:

```text
valid
errors
warnings
```

---

# 43. Validation Errors

Examples:

```text
Voucher has no lines.
Voucher is not balanced.
Account is inactive.
Amount must be positive.
Financial year is closed.
```

---

# 44. Validation Warnings

Warnings SHALL not silently override hard accounting rules.

Example:

```text
Description is unusually short.
```

---

# 45. Posting Permission

Posting SHALL require:

```text
POST_VOUCHER
```

---

# 46. Draft Permission

Creating a draft SHOULD require:

```text
CREATE_VOUCHER
```

---

# 47. Editing Draft

Editing a draft SHOULD require:

```text
EDIT_VOUCHER
```

---

# 48. Reversal Permission

Reversal SHALL require:

```text
REVERSE_VOUCHER
```

---

# 49. Posting Workflow

```text
CREATE DRAFT
      ↓
EDIT
      ↓
VALIDATE
      ↓
AUTHORISE
      ↓
POST
      ↓
AUDIT
```

---

# 50. Posting Transaction

Posting SHALL be atomic:

```text
BEGIN
 ↓
validate
 ↓
lock/check relevant state
 ↓
update voucher status
 ↓
store posting metadata
 ↓
audit
 ↓
COMMIT
```

---

# 51. Posting Failure

If any mandatory part fails:

```text
ROLLBACK
```

The voucher SHALL remain unposted.

---

# 52. Posting Idempotency

A voucher already marked:

```text
POSTED
```

SHALL not be posted again.

---

# 53. Double Posting Protection

Attempting to post the same voucher twice SHALL result in:

```text
controlled rejection
```

---

# 54. Posted Data Immutability

Posted voucher lines SHALL not be directly editable.

---

# 55. Correction Principle

Corrections SHALL use:

```text
reversal
+
correct replacement
```

or another controlled adjustment process.

---

# 56. Reversal

A reversal creates an offsetting transaction.

Example:

Original:

```text
Debit Bank      1,000
Credit Income   1,000
```

Reversal:

```text
Debit Income    1,000
Credit Bank     1,000
```

---

# 57. Reversal Link

The reversal voucher SHOULD reference:

```text
reversed_voucher_id
```

---

# 58. Reversal Audit

Reversal SHALL record:

```text
actor
original voucher
reversal voucher
reason
timestamp
```

---

# 59. Reversal Reason

A reversal SHALL require a meaningful reason.

---

# 60. Accounting Period

A posted voucher SHALL belong to a financial year.

Future versions may add monthly periods.

---

# 61. Period Closure

For v1.0, financial-year closure is sufficient.

Monthly closing is optional.

---

# 62. General Ledger

The general ledger provides transaction history by account.

Minimum fields:

```text
date
voucher
description
debit
credit
balance
```

---

# 63. Ledger Balance

For each account, balance SHALL be calculated according to account type and debit/credit convention.

---

# 64. Trial Balance

Trial balance SHALL show:

```text
account
debit total
credit total
```

---

# 65. Trial Balance Rule

Overall:

```text
TOTAL DEBIT = TOTAL CREDIT
```

---

# 66. Trial Balance Acceptance

A trial balance that does not balance indicates a critical integrity problem.

The system SHALL flag it.

---

# 67. Income Statement

The income statement SHALL summarise:

```text
INCOME
-
EXPENSES
=
RESULT
```

for a selected period.

---

# 68. Result

For a non-profit association, the result may be described as:

```text
SURPLUS
```

or:

```text
DEFICIT
```

rather than commercial profit.

---

# 69. Balance Sheet

The balance sheet SHALL summarise:

```text
ASSETS
=
LIABILITIES
+
EQUITY
```

subject to the selected accounting model.

---

# 70. Non-Profit Presentation

The application SHOULD allow report labels suitable for an association.

---

# 71. Cash Account

Cash accounts represent physical or petty cash.

Example:

```text
1100 Cash
```

---

# 72. Bank Account

Bank accounts represent association bank accounts.

Example:

```text
1000 Bank
```

---

# 73. Multiple Bank Accounts

MFM MAY support multiple bank accounts through separate ledger accounts.

---

# 74. Bank Reconciliation

Basic reconciliation SHALL compare:

```text
bank statement balance
```

against:

```text
ledger bank balance
```

for a selected date.

---

# 75. Reconciliation Record

Minimum:

```text
account
statement_date
statement_balance
ledger_balance
difference
status
reconciled_by
reconciled_at
```

---

# 76. Reconciliation Status

Recommended:

```text
OPEN
RECONCILED
```

---

# 77. Reconciliation Rule

A reconciliation SHALL only be marked complete when:

```text
difference = 0
```

unless a documented exception workflow is introduced.

---

# 78. Bank Difference

If:

```text
statement = 25,000
ledger = 24,500
```

then:

```text
difference = 500
```

The reconciliation remains open.

---

# 79. Bank Reconciliation Permission

Require:

```text
RECONCILE_BANK
```

---

# 80. Accounting Reports

Minimum:

```text
General Ledger
Trial Balance
Income Statement
Balance Sheet
Account Activity
Bank Reconciliation
```

---

# 81. Period Filter

Reports SHALL support:

```text
start date
end date
financial year
```

where relevant.

---

# 82. Account Filter

General ledger SHALL support:

```text
account
```

filtering.

---

# 83. Project Filter

Accounting reports MAY filter by:

```text
project
```

when project tagging is used.

---

# 84. Posted-Only Rule

Official financial reports SHALL use:

```text
POSTED
```

transactions only.

---

# 85. Draft Visibility

Draft vouchers MAY be visible in a separate draft report.

They SHALL not contaminate official financial reports.

---

# 86. Reversed Transactions

Reports SHALL correctly include the effect of reversal transactions.

The original remains historical.

---

# 87. Accounting Audit

Material accounting actions SHALL be audited:

```text
voucher created
voucher posted
voucher reversed
financial year closed
financial year reopened
bank reconciliation completed
chart of accounts changed
```

---

# 88. Audit Actor

Every material accounting action SHALL have a known actor.

---

# 89. Unknown Actor

If an accounting operation cannot identify an authenticated actor:

```text
operation denied
```

---

# 90. Accounting Security

The accounting service SHALL use the security context from the security implementation.

---

# 91. Service Dependency

Conceptually:

```text
AccountingService
    ↓
SecurityContext
    ↓
AccountingRepository
    ↓
AuditService
```

---

# 92. Accounting Repository

`AccountingRepository` MAY handle:

```text
voucher persistence
voucher line persistence
ledger queries
trial balance queries
```

---

# 93. Account Repository

Account persistence MAY remain separate:

```text
AccountRepository
```

---

# 94. Financial Year Repository

Recommended:

```text
FinancialYearRepository
```

---

# 95. Reconciliation Repository

Recommended:

```text
BankReconciliationRepository
```

---

# 96. Accounting Service API

Recommended:

```text
create_voucher()
update_draft_voucher()
validate_voucher()
post_voucher()
reverse_voucher()
get_general_ledger()
get_trial_balance()
get_income_statement()
get_balance_sheet()
reconcile_bank()
close_financial_year()
reopen_financial_year()
```

---

# 97. Account Service API

Recommended:

```text
create_account()
update_account()
deactivate_account()
list_accounts()
```

---

# 98. Financial Year API

Recommended:

```text
create_financial_year()
get_current_year()
close_year()
reopen_year()
```

---

# 99. Voucher Query API

Recommended:

```text
get_voucher()
list_drafts()
list_posted()
list_by_period()
```

---

# 100. Posting API

`post_voucher(voucher_id)` SHALL:

```text
authenticate
authorise
load draft
validate
check year
post
audit
return result
```

---

# 101. Posting Result

The service MAY return:

```text
voucher_id
voucher_number
posted_at
```

---

# 102. Posting Error

Posting errors SHALL identify the business reason without exposing database internals.

---

# 103. Database Constraint

A database constraint SHOULD reinforce:

```text
voucher status
```

and:

```text
foreign keys
```

---

# 104. Financial Year Constraint

A voucher SHALL reference a valid financial year.

---

# 105. Voucher Line Constraint

A voucher line SHALL reference a valid account.

---

# 106. Project Reference

A voucher line MAY reference a project.

If project is deleted or archived, historical accounting references SHALL remain valid.

---

# 107. Project Deletion

A project with accounting history SHALL not be physically deleted.

---

# 108. Account History

Accounts with posted history SHALL remain available for historical reporting.

---

# 109. Accounting Database Tables

Recommended:

```text
financial_years
accounts
vouchers
voucher_lines
bank_reconciliations
```

Optional:

```text
accounting_periods
```

for future use.

---

# 110. Financial Years Table

Conceptual:

```text
id
year
start_date
end_date
status
created_at
closed_at
closed_by
```

---

# 111. Accounts Table

Conceptual:

```text
id
account_number
name
account_type
description
active
created_at
updated_at
```

---

# 112. Vouchers Table

Conceptual:

```text
id
financial_year_id
voucher_number
voucher_date
description
status
created_by
created_at
posted_by
posted_at
reversed_voucher_id
```

---

# 113. Voucher Lines Table

Conceptual:

```text
id
voucher_id
line_number
account_id
debit
credit
description
project_id
```

---

# 114. Bank Reconciliations Table

Conceptual:

```text
id
account_id
statement_date
statement_balance
ledger_balance
difference
status
reconciled_by
reconciled_at
```

---

# 115. Indexes

Recommended indexes:

```text
accounts.account_number
vouchers.voucher_number
vouchers.voucher_date
vouchers.financial_year_id
vouchers.status
voucher_lines.voucher_id
voucher_lines.account_id
voucher_lines.project_id
```

---

# 116. Unique Constraints

Recommended:

```text
account_number UNIQUE
financial_year.year UNIQUE
```

Voucher number uniqueness SHALL match the chosen numbering model.

---

# 117. Decimal Storage

SQLite does not provide a native decimal type equivalent to Python Decimal.

The implementation SHALL choose one consistent storage model.

Recommended simple model:

```text
integer minor units
```

for authoritative DKK amounts.

Example:

```text
1,234.56 DKK
→
123456 øre
```

---

# 118. Minor Unit Conversion

Conversion:

```text
Decimal("1234.56") × 100
=
123456
```

The conversion SHALL use exact decimal arithmetic.

---

# 119. Display Conversion

Database:

```text
123456
```

Display:

```text
1,234.56 DKK
```

---

# 120. Money Utility

A central money utility SHOULD provide:

```text
to_minor_units()
from_minor_units()
validate_amount()
```

---

# 121. Negative Amounts

Negative accounting amounts SHOULD not be represented in debit/credit fields.

Instead:

```text
debit
credit
```

remain non-negative.

The direction is represented by the appropriate column.

---

# 122. Voucher Line Validation

For each line:

```text
debit >= 0
credit >= 0
not both > 0
at least one > 0
```

---

# 123. Voucher Validation Example

```text
Line 1:
Bank
Debit 1000
Credit 0

Line 2:
Grant Income
Debit 0
Credit 1000
```

Valid.

---

# 124. Multi-Line Voucher

Example:

```text
Debit Materials      700
Debit Bank Fees       50
Credit Bank          750
```

Valid.

---

# 125. Split Transaction

The accounting engine SHALL support multiple debit and credit lines.

---

# 126. Voucher Description

Description belongs to the voucher and may also be repeated or supplemented on lines.

---

# 127. Posting Date

The posting date is the voucher date for v1.0.

Future versions may distinguish document date and posting date.

---

# 128. Backdated Voucher

Backdated posting MAY be allowed within an open financial year.

The action SHALL be auditable.

---

# 129. Future-Dated Voucher

Future-dated posting MAY be allowed only if the financial year is open.

---

# 130. Closed Year Protection

No new normal posting SHALL enter a closed year.

---

# 131. Reopening Year Protection

Reopening a year SHALL require:

```text
REOPEN_FINANCIAL_YEAR
```

or equivalent administrative permission.

---

# 132. Year Closure Audit

Closing a year SHALL record:

```text
year
actor
timestamp
```

---

# 133. Trial Balance Query

The trial balance SHALL aggregate posted lines:

```text
SUM(debit)
SUM(credit)
GROUP BY account
```

---

# 134. General Ledger Query

The general ledger SHALL return posted lines ordered by:

```text
date
voucher number
line number
```

---

# 135. Running Balance

A running balance MAY be calculated in the service/reporting layer.

---

# 136. Income Statement Query

Income accounts:

```text
account_type = INCOME
```

Expense accounts:

```text
account_type = EXPENSE
```

---

# 137. Balance Sheet Query

Balance sheet includes:

```text
ASSET
LIABILITY
EQUITY
```

---

# 138. Result Treatment

For v1.0, the result may be displayed separately in the income statement.

Year-end closing mechanics may be implemented later if the association requires formal closing entries.

---

# 139. Non-Profit Year-End

The application SHALL not assume commercial profit distribution.

Any surplus/deficit remains within the association's accounting model.

---

# 140. Opening Balances

MFM SHALL support initial opening balances through controlled opening vouchers.

---

# 141. Opening Balance Voucher

Recommended description:

```text
Opening balance 2026
```

---

# 142. Opening Balance Permission

Opening balances SHALL require elevated accounting authority.

---

# 143. Opening Balance Audit

The operation SHALL be audited.

---

# 144. Bank Opening Balance

Bank opening balance SHALL be entered through the accounting mechanism rather than directly modifying the bank account balance.

---

# 145. Cash Opening Balance

Same principle applies to cash.

---

# 146. No Stored Account Balance

The authoritative account balance SHALL be derived from posted transactions rather than manually maintained as a mutable number.

---

# 147. Performance

For a small association, recalculating balances from posted ledger data is acceptable.

Indexes SHALL support normal query performance.

---

# 148. Accounting Cache

No accounting balance cache is required for v1.0.

---

# 149. Report Consistency

All financial reports SHALL use the same accounting query conventions.

---

# 150. Report Reconciliation

The following SHALL reconcile:

```text
Trial Balance
Income Statement
Balance Sheet
General Ledger
```

---

# 151. Trial Balance vs Ledger

For every account:

```text
ledger debit/credit totals
=
trial balance totals
```

---

# 152. Balance Sheet Test

The balance sheet SHALL satisfy:

```text
Assets = Liabilities + Equity + applicable result treatment
```

according to the chosen accounting model.

---

# 153. Income Statement Test

The income statement SHALL equal:

```text
Total Income - Total Expenses
```

---

# 154. Bank Ledger Test

Bank account balance SHALL equal:

```text
opening balance
+
debits
-
credits
```

according to the configured account convention.

---

# 155. Reconciliation Test

A reconciled account SHALL have:

```text
difference = 0
```

---

# 156. Accounting GUI

Minimum screens:

```text
Chart of Accounts
Financial Years
Voucher List
Voucher Editor
General Ledger
Trial Balance
Income Statement
Balance Sheet
Bank Reconciliation
```

---

# 157. Accounting Dashboard

A compact accounting dashboard MAY show:

```text
Bank Balance
Cash Balance
Current Result
Outstanding Reconciliation
Draft Vouchers
Current Year
```

---

# 158. Voucher Editor

Minimum:

```text
date
description
lines
account
debit
credit
project
```

---

# 159. Voucher Editor Validation

The user SHALL see:

```text
total debit
total credit
difference
```

before posting.

---

# 160. Posting Button

Posting SHALL be disabled or rejected when:

```text
unbalanced
invalid account
closed year
missing permission
```

---

# 161. Draft Save

Drafts may be saved while incomplete if the application clearly marks them as:

```text
DRAFT
```

---

# 162. Draft Delete

Draft deletion SHALL require:

```text
EDIT_VOUCHER
```

or a dedicated delete permission.

---

# 163. Posted Voucher View

Posted voucher screen SHALL be read-only except for:

```text
Create Reversal
```

if authorised.

---

# 164. Reversal UI

Reversal action SHALL require:

```text
reason
confirmation
permission
```

---

# 165. Financial Year UI

Show:

```text
year
period
status
```

and authorised close/reopen actions.

---

# 166. Account UI

Show:

```text
account number
name
type
status
```

---

# 167. Account Deactivation

Deactivation SHALL warn if the account has historical activity.

---

# 168. General Ledger UI

Filters:

```text
account
date from
date to
project
```

---

# 169. Trial Balance UI

Filters:

```text
financial year
date to
```

---

# 170. Income Statement UI

Filters:

```text
period
financial year
```

---

# 171. Balance Sheet UI

Filter:

```text
as-of date
```

---

# 172. Bank Reconciliation UI

Show:

```text
account
statement date
statement balance
ledger balance
difference
status
```

---

# 173. Accounting Export

Reports SHOULD support:

```text
XLSX
PDF
CSV
```

where applicable.

---

# 174. Export Security

Exports SHALL require appropriate permissions.

---

# 175. Export Audit

Material financial exports MAY be audited:

```text
report
period
actor
timestamp
```

---

# 176. Accounting Error Handling

User-facing errors:

```text
Voucher is not balanced.
Financial year is closed.
Account is inactive.
You do not have permission to post.
```

Technical errors remain in logs.

---

# 177. Database Error Handling

A database failure during posting SHALL result in:

```text
rollback
error
audit/log where possible
```

No partial posting.

---

# 178. Posting Atomicity Test

Test:

```text
voucher status update succeeds
line operation fails
```

Expected:

```text
voucher remains draft
```

---

# 179. Audit Atomicity

If mandatory posting audit cannot be persisted:

```text
posting rolls back
```

---

# 180. Concurrency

MFM v1.0 is primarily a local association application.

Complex distributed concurrency is not required.

---

# 181. Duplicate Posting Concurrency

The database/service logic SHALL still prevent duplicate posting.

---

# 182. Voucher Number Concurrency

Voucher number allocation SHALL be transactional.

---

# 183. Financial Year Concurrency

Closing a year SHALL prevent concurrent new postings after closure.

---

# 184. Accounting Negative Testing

Mandatory negative tests:

```text
unbalanced voucher
zero line
negative line amount
both debit and credit
inactive account
closed year
missing financial year
missing account
duplicate voucher number
double posting
unauthorised posting
```

---

# 185. Accounting Scenario Test 1

```text
Create voucher
 ↓
Debit Bank 1,000
 ↓
Credit Grant Income 1,000
 ↓
Post
```

Expected:

```text
success
trial balance balances
```

---

# 186. Accounting Scenario Test 2

```text
Create voucher
 ↓
Debit Bank 1,000
 ↓
Credit Grant Income 900
 ↓
Post
```

Expected:

```text
rejected
```

---

# 187. Accounting Scenario Test 3

```text
Post voucher
 ↓
Attempt edit
```

Expected:

```text
rejected
```

---

# 188. Accounting Scenario Test 4

```text
Post voucher
 ↓
Reverse voucher
```

Expected:

```text
reversal created
net financial effect = 0
history retained
```

---

# 189. Accounting Scenario Test 5

```text
Close year
 ↓
Attempt posting
```

Expected:

```text
rejected
```

---

# 190. Accounting Scenario Test 6

```text
Read-only user
 ↓
Attempt posting
```

Expected:

```text
permission denied
```

---

# 191. Accounting Scenario Test 7

```text
Bank statement 10,000
Ledger 10,000
```

Expected:

```text
RECONCILED
```

---

# 192. Accounting Scenario Test 8

```text
Bank statement 10,000
Ledger 9,500
```

Expected:

```text
OPEN
difference 500
```

---

# 193. Accounting Scenario Test 9

```text
Create opening balance
 ↓
Post
 ↓
Review balance sheet
```

Expected:

```text
opening balance represented in accounting
```

---

# 194. Accounting Scenario Test 10

```text
Create draft
 ↓
Close application
 ↓
Restart
 ↓
Open draft
```

Expected:

```text
draft persists
```

---

# 195. Accounting Unit Tests

Minimum:

```text
money conversion
voucher balance
line validation
financial year validation
account status validation
```

---

# 196. Accounting Repository Tests

Minimum:

```text
account CRUD
financial year CRUD
voucher persistence
line persistence
ledger query
trial balance query
```

---

# 197. Accounting Service Tests

Minimum:

```text
create voucher
validate
post
reverse
close year
reopen year
reconcile
```

---

# 198. Accounting Integration Tests

Minimum:

```text
security
+
voucher
+
database
+
audit
```

---

# 199. Report Integration Test

Post transactions.

Generate:

```text
ledger
trial balance
income statement
balance sheet
```

Verify consistency.

---

# 200. Project Integration

If a voucher line contains:

```text
project_id
```

the project reporting layer SHALL be able to use it.

---

# 201. Membership Integration

Future membership fee transactions SHALL post through the same accounting engine.

---

# 202. Grant Integration

Grant receipts SHALL post through the same accounting engine.

---

# 203. Document Integration

A voucher MAY have linked documents in the document module.

---

# 204. Accounting as Shared Core

The accounting engine SHALL not be duplicated inside:

```text
membership
projects
grants
```

---

# 205. Financial Source of Truth

Membership payment:

```text
MembershipService
 ↓
AccountingService
```

Project expense:

```text
ProjectService
 ↓
AccountingService
```

Grant receipt:

```text
GrantService
 ↓
AccountingService
```

---

# 206. No Direct Accounting SQL

Business modules SHALL not insert accounting records directly into:

```text
vouchers
voucher_lines
```

They SHALL use `AccountingService`.

---

# 207. Accounting API Boundary

Only accounting services/repositories own accounting persistence.

---

# 208. Accounting Audit Boundary

Accounting actions are audited centrally.

---

# 209. Accounting Governance

Human authority remains above automation.

MFM SHALL not autonomously:

```text
post unknown transactions
change account permissions
close financial year
reopen financial year
```

---

# 210. AI Boundary

Future AI may:

```text
suggest account
detect anomaly
explain variance
```

but SHALL not automatically post financial transactions in v1.0.

---

# 211. AI Recommendation Flow

If AI is added:

```text
AI suggestion
 ↓
human review
 ↓
authorisation
 ↓
AccountingService
 ↓
post
```

---

# 212. Accounting Circuit Breaker

If a critical integrity check fails:

```text
STOP POSTING
```

The system SHALL not continue creating financial records.

---

# 213. Economic Safe State

If trial balance integrity cannot be established:

```text
reports flagged
posting may be blocked
administrator notified
```

---

# 214. Reconciliation Safe State

If bank reconciliation data is inconsistent:

```text
status = OPEN
```

not falsely marked reconciled.

---

# 215. Accounting Recovery

Recovery from database failure SHALL use:

```text
backup
restore
integrity verification
```

---

# 216. Accounting Backup

Financial database backup SHALL be part of the standard MFM backup process.

---

# 217. Accounting Restore

After restore verify:

```text
voucher count
posted totals
trial balance
financial year
audit
```

---

# 218. Accounting Migration

Schema migrations involving accounting SHALL be tested on a copy of representative data.

---

# 219. Migration Blocker

If an accounting migration cannot be verified:

```text
do not release
```

---

# 220. Accounting Performance

For a normal association dataset, the following should remain responsive:

```text
voucher entry
ledger query
trial balance
income statement
balance sheet
```

---

# 221. Example Test Volume

Use a test dataset such as:

```text
10 financial years
20,000 voucher lines
5,000 vouchers
100 accounts
100 projects
```

These are test values, not imposed limits.

---

# 222. Report Performance

Indexes SHALL support:

```text
date filtering
account filtering
voucher lookup
project filtering
```

---

# 223. Accounting UI Simplicity

The accounting interface SHALL prioritise:

```text
clear
simple
safe
```

over visual complexity.

---

# 224. Treasurer Workflow

The ordinary treasurer workflow should be:

```text
Login
 ↓
Accounting
 ↓
New Voucher
 ↓
Enter Date
 ↓
Enter Description
 ↓
Enter Lines
 ↓
Review Debit/Credit
 ↓
Save Draft
 ↓
Validate
 ↓
Post
```

---

# 225. Ordinary User Workflow

Users who only need reports should not be exposed to unnecessary accounting controls.

---

# 226. Board Workflow

Board user:

```text
Login
 ↓
Reports
 ↓
Financial Overview
 ↓
Income Statement
 ↓
Balance Sheet
 ↓
Project/Grant Overview
```

---

# 227. Accounting Dashboard

The dashboard SHOULD answer:

```text
Is the accounting balanced?
What is the current result?
What is the bank position?
Are there drafts?
Is reconciliation complete?
```

---

# 228. Accounting Alerts

Useful warnings:

```text
unreconciled bank account
draft vouchers
closed financial year
unusual balance
```

Alerts SHALL not create automatic transactions.

---

# 229. Accounting Acceptance Criteria

The accounting implementation is accepted when:

```text
accounts can be created
financial year can be created
voucher can be drafted
voucher validates
balanced voucher posts
unbalanced voucher is rejected
posted voucher cannot be edited
reversal works
ledger works
trial balance balances
income statement works
balance sheet works
bank reconciliation works
audit works
permissions work
```

---

# 230. Accounting Release Blockers

Release SHALL be blocked by:

```text
unbalanced posted voucher
duplicate posting
editable posted transaction
broken reversal
incorrect trial balance
incorrect report totals
unauthorised posting
missing accounting audit
float-based authoritative arithmetic
```

---

# 231. Implementation Order

Implement:

```text
1. financial_years
2. accounts
3. money utility
4. vouchers
5. voucher_lines
6. validation
7. posting
8. reversal
9. ledger
10. trial balance
11. income statement
12. balance sheet
13. bank reconciliation
14. GUI
15. tests
```

---

# 232. First Accounting Milestone

```text
Create account
 ↓
Create financial year
 ↓
Create draft voucher
 ↓
Validate
 ↓
Post
 ↓
View ledger
```

---

# 233. Second Accounting Milestone

Add:

```text
trial balance
income statement
balance sheet
```

---

# 234. Third Accounting Milestone

Add:

```text
reversal
bank reconciliation
opening balances
```

---

# 235. Fourth Accounting Milestone

Integrate:

```text
membership
projects
grants
documents
```

---

# 236. Accounting Test Data

Create representative accounts:

```text
1000 Bank
1100 Cash
4000 Membership Income
4100 Grant Income
5000 Maintenance
5100 Administration
```

---

# 237. Test Voucher Data

Example:

```text
Voucher 2026-0001
Date 2026-01-10
Description Membership income

Debit  1000 Bank       500
Credit 4000 Membership 500
```

---

# 238. Expense Test

```text
Voucher 2026-0002
Date 2026-01-11
Description Maintenance

Debit  5000 Maintenance 250
Credit 1000 Bank        250
```

---

# 239. Grant Test

```text
Debit  1000 Bank       10,000
Credit 4100 Grant      10,000
```

---

# 240. Project Tag Test

Expense line:

```text
account = 5000
debit = 2,000
project_id = PROJECT-001
```

The accounting report remains correct while project reporting can aggregate the cost.

---

# 241. Membership Integration Example

Membership payment:

```text
Debit Bank
Credit Membership Income
```

---

# 242. Grant Integration Example

Grant receipt:

```text
Debit Bank
Credit Grant Income
```

The exact account treatment SHALL be configurable according to the association's bookkeeping policy.

---

# 243. Accounting Policy Boundary

MFM implements accounting mechanics.

The association's accountant/bookkeeper remains responsible for choosing the appropriate accounting treatment.

---

# 244. Tax/VAT Boundary

VAT handling is not mandatory for v1.0.

If the association becomes VAT-liable, the accounting model can be extended.

---

# 245. Multi-Currency Boundary

Multi-currency is not required for v1.0.

---

# 246. Accrual Boundary

Basic cash-oriented association accounting may be supported initially.

More advanced accrual accounting can be added if required.

---

# 247. Accounting Simplicity

The module SHALL not become a commercial ERP.

The goal is:

```text
correct association bookkeeping
```

---

# 248. No Overengineering

Do not add:

```text
general ledger engine framework
event sourcing
distributed transactions
microservices
```

for v1.0.

---

# 249. Source Control

Recommended accounting commits:

```text
accounting-schema
account-model
voucher-model
posting-engine
reports
bank-reconciliation
accounting-tests
```

---

# 250. Definition of Done

Accounting is done when:

```text
CODE
+
DATABASE
+
SECURITY
+
AUDIT
+
GUI
+
TESTS
+
REPORTS
```

are integrated.

---

# 251. Final Accounting Architecture

```text
                  SECURITY
                      ↓
USER → GUI → AccountingService
                ↓
             VALIDATION
                ↓
            TRANSACTION
                ↓
       ┌────────┴────────┐
       ↓                 ↓
   Vouchers          AuditService
       ↓
 Voucher Lines
       ↓
 Accounts
       ↓
    SQLite
       ↓
   REPORTS
```

---

# 252. Final Accounting Rules

```text
RULE 1
Every posted voucher must balance.

RULE 2
Drafts do not affect official reports.

RULE 3
Posted vouchers are immutable.

RULE 4
Corrections use controlled reversal.

RULE 5
Financial-year closure prevents normal posting.

RULE 6
Authoritative money calculations use Decimal or minor units.

RULE 7
Accounting operations require authentication and permission.

RULE 8
Material accounting actions are audited.

RULE 9
Business modules use AccountingService rather than direct accounting SQL.

RULE 10
Accounting integrity failure stops further posting.
```

---

# 253. Next Implementation Layer

After this accounting implementation, the next concrete implementation file SHALL be:

```text
MFM v1.0 Membership & Member Management Implementation
```

It will use the existing:

```text
Database Foundation
+
Security
+
Audit
+
Accounting Core
```

and implement members, memberships, fees and payment integration.

---

# 254. Final Governing Principle

> **MFM accounting must make the correct transaction easy, the incorrect transaction difficult, and every material financial action traceable.**

# END OF MFM v1.0 ACCOUNTING CORE IMPLEMENTATION

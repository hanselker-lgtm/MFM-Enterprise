# MFM v1.0 PROJECT & BUDGET IMPLEMENTATION

## MaritimForeningsManager — Konkret implementeringsgrundlag for projekter, budgetter, projektøkonomi, finansiering og regnskabsintegration

**Version:** 1.0  
**Status:** Implementation Baseline  
**Parent:** MFM v1.0 Membership & Member Management Implementation  
**Purpose:** Provide a simple, controlled project and budget subsystem for a small non-profit association

---

# 1. Purpose

This document defines the concrete implementation baseline for:

```text
PROJECTS
PROJECT STATUS
PROJECT OWNERS
PROJECT PERIODS
PROJECT BUDGETS
BUDGET LINES
PROJECT COSTS
PROJECT FUNDING
PROJECT REVENUE
PROJECT ACCOUNTING LINKS
PROJECT DOCUMENT LINKS
PROJECT REPORTING
PROJECT AUDIT
```

The implementation SHALL remain proportionate to the needs of a small non-profit association.

---

# 2. Project Principle

> **A project is a controlled organisational unit for planning, executing and reporting a defined activity; accounting remains the authoritative source for posted money.**

---

# 3. Scope

Mandatory v1.0:

```text
Project register
Project status
Project dates
Project owner
Project description
Project budget
Budget lines
Budget vs actual
Project income
Project expenses
Funding sources
Accounting integration
Project reporting
Audit
```

Optional later:

```text
resource planning
time registration
advanced forecasting
multi-stage approvals
external project portals
automated grant reporting
```

---

# 4. Project Architecture

```text
PROJECT
   ↓
PROJECT PLAN
   ↓
BUDGET
   ↓
ACTUAL TRANSACTIONS
   ↓
ACCOUNTING
   ↓
PROJECT REPORT
```

---

# 5. Security Architecture

```text
USER
 ↓
SECURITY CONTEXT
 ↓
PROJECT SERVICE
 ↓
PROJECT REPOSITORY
 ↓
ACCOUNTING SERVICE
 ↓
AUDIT
```

---

# 6. Project Entity

Minimum:

```text
id
project_number
name
status
start_date
end_date
description
created_by
created_at
updated_at
```

Recommended:

```text
owner_user_id
contact_name
notes
```

---

# 7. Project Number

Project number SHALL be unique.

Example:

```text
P-2026-001
P-2026-002
```

The format SHALL be configurable.

---

# 8. Project Number Stability

Once a project has accounting history, its project number SHALL not be silently changed.

---

# 9. Project Status

Recommended:

```text
PLANNED
ACTIVE
ON_HOLD
COMPLETED
CANCELLED
ARCHIVED
```

---

# 10. Planned Project

A planned project exists before execution.

It may have:

```text
description
budget
funding plan
documents
```

but should not normally contain final project accounting until authorised activity begins.

---

# 11. Active Project

An active project may:

```text
receive income
incur expenses
use budget
link documents
```

subject to permissions.

---

# 12. On-Hold Project

An on-hold project remains visible but new project activity may be restricted.

---

# 13. Completed Project

A completed project SHALL remain available for historical reporting.

---

# 14. Cancelled Project

A cancelled project SHALL retain its history.

---

# 15. Archived Project

Archived projects are hidden from normal active lists but remain available to authorised users.

---

# 16. No Physical Project Deletion

A project with accounting or document history SHALL not be physically deleted.

---

# 17. Project Owner

A project MAY have an owner.

The owner is responsible operationally but does not automatically receive accounting authority.

---

# 18. Project Authority

Project ownership and financial authority are separate concepts.

```text
PROJECT OWNER
≠
ACCOUNTING AUTHORITY
```

---

# 19. Project Dates

Minimum:

```text
start_date
end_date
```

where applicable.

---

# 20. Date Validation

If both exist:

```text
start_date <= end_date
```

---

# 21. Project Description

The description SHOULD explain:

```text
purpose
scope
expected result
```

without becoming a second document-management system.

---

# 22. Project Budget

A project budget describes planned financial resources.

Minimum:

```text
id
project_id
name
status
created_at
updated_at
```

---

# 23. Budget Status

Recommended:

```text
DRAFT
APPROVED
ACTIVE
CLOSED
```

---

# 24. Budget Lines

Each budget contains lines.

Minimum:

```text
id
budget_id
category
description
amount
account_id
```

Optional:

```text
funding_source_id
```

---

# 25. Budget Amount

Budget amounts use the same authoritative money representation as accounting.

Recommended:

```text
integer minor units
```

---

# 26. Budget Currency

Default:

```text
DKK
```

---

# 27. Budget Categories

Example:

```text
MATERIALS
LABOUR
TRANSPORT
INSURANCE
EQUIPMENT
COMMUNICATION
ADMINISTRATION
OTHER
```

The categories SHALL be configurable.

---

# 28. No Hard-Coded Budget Categories

The implementation SHALL not assume that every association uses the same project cost categories.

---

# 29. Budget Account Mapping

A budget line MAY map to an accounting account.

This supports:

```text
budget
vs
actual
```

comparison.

---

# 30. Budget Line Example

```text
Category: MATERIALS
Description: Timber
Budget: 25,000
Account: Maintenance/Materials
```

---

# 31. Budget Totals

Budget total:

```text
SUM(all budget lines)
```

The total SHALL be derived, not manually maintained as a second source of truth.

---

# 32. Approved Budget

An approved budget becomes the baseline for project reporting.

---

# 33. Budget Immutability

An approved budget SHOULD not be silently edited.

Changes should use:

```text
budget revision
```

or a controlled update mechanism.

---

# 34. Budget Revision

A revision MAY contain:

```text
revision number
reason
created_by
created_at
```

---

# 35. Budget Versioning

For v1.0, simple revision history is sufficient.

A full financial planning engine is not required.

---

# 36. Budget Approval

Approval SHALL require an explicit permission.

Recommended:

```text
APPROVE_PROJECT_BUDGET
```

---

# 37. Project Permissions

Recommended:

```text
VIEW_PROJECTS
CREATE_PROJECT
EDIT_PROJECT
CLOSE_PROJECT
MANAGE_PROJECT_BUDGET
APPROVE_PROJECT_BUDGET
VIEW_PROJECT_FINANCE
EXPORT_PROJECT_REPORTS
```

---

# 38. Project Role

The existing:

```text
PROJECT_MANAGER
```

role SHOULD receive normal project management permissions.

---

# 39. Treasurer Integration

The treasurer MAY receive:

```text
VIEW_PROJECT_FINANCE
```

and relevant accounting permissions.

---

# 40. Board Integration

The board MAY receive:

```text
VIEW_PROJECTS
VIEW_PROJECT_FINANCE
EXPORT_PROJECT_REPORTS
```

without receiving edit authority.

---

# 41. Service-Level Security

Project permissions SHALL be checked in services.

GUI restrictions alone are insufficient.

---

# 42. ProjectService

Recommended API:

```text
create_project()
update_project()
change_status()
close_project()
get_project()
list_projects()
```

---

# 43. ProjectBudgetService

Recommended:

```text
create_budget()
add_budget_line()
update_budget_line()
submit_budget()
approve_budget()
revise_budget()
close_budget()
get_budget()
```

---

# 44. ProjectFinanceService

Recommended:

```text
get_project_actuals()
get_budget_vs_actual()
get_project_income()
get_project_expenses()
get_project_balance()
```

---

# 45. Project Funding

A project may have one or more funding sources.

Examples:

```text
ASSOCIATION_FUNDS
MEMBERS
GRANT
DONATION
SPONSOR
PUBLIC_SUPPORT
OTHER
```

---

# 46. Funding Source Entity

Minimum:

```text
id
project_id
name
source_type
planned_amount
confirmed_amount
received_amount
status
```

---

# 47. Funding Status

Recommended:

```text
PLANNED
APPLIED
APPROVED
PARTIALLY_RECEIVED
RECEIVED
CANCELLED
```

---

# 48. Funding Principle

Funding is a planning/reporting concept.

Actual money received remains an accounting transaction.

---

# 49. Grant Integration

Grant funding MAY reference the future grant module.

The project module SHALL not duplicate grant administration.

---

# 50. Funding Source Link

A project funding record MAY reference:

```text
grant_id
```

when the grant module exists.

---

# 51. Donation Funding

A donation may be recorded as project funding.

If money is received, it SHALL be posted through AccountingService.

---

# 52. Sponsor Funding

Sponsor funding follows the same separation:

```text
project planning
+
accounting
```

---

# 53. Project Income

Project income is income associated with a project.

It SHALL normally be represented by an accounting transaction with:

```text
project_id
```

on the relevant line.

---

# 54. Project Expense

Project expense is a posted accounting transaction associated with a project.

---

# 55. Project Accounting Link

Project accounting SHALL use the existing accounting line:

```text
project_id
```

rather than maintaining a duplicate transaction ledger.

---

# 56. Source of Financial Truth

```text
ACCOUNTING
```

is authoritative for:

```text
actual income
actual expense
cash
bank
balances
```

---

# 57. Project Source of Planning Truth

```text
PROJECT BUDGET
```

is authoritative for planned amounts.

---

# 58. Budget vs Actual

Core project calculation:

```text
Budget
-
Actual
=
Variance
```

---

# 59. Variance

Positive/negative presentation SHALL be clearly labelled.

The application SHALL avoid ambiguous signs.

---

# 60. Budget Utilisation

Example:

```text
Budget: 100,000
Actual: 60,000
Utilisation: 60%
Remaining: 40,000
```

---

# 61. Overspend

If:

```text
Actual > Budget
```

the project SHALL be flagged.

---

# 62. Overspend Policy

The system SHALL not automatically block every overspend.

The association decides whether project budgets are:

```text
hard limits
```

or:

```text
planning limits
```

---

# 63. Hard Budget Control

If configured as a hard limit, the project service MAY block authorised project expenses exceeding the approved budget.

However, accounting corrections SHALL remain possible through authorised accounting operations.

---

# 64. Soft Budget Control

Soft budget mode:

```text
allow
+
warn
+
audit/report
```

---

# 65. Default v1.0

For a small association:

```text
SOFT BUDGET CONTROL
```

is recommended.

This avoids blocking legitimate bookkeeping while still highlighting overspending.

---

# 66. Budget Warning

Example:

```text
Project is 92% utilised.
```

or:

```text
Projected overspend: 5,000 DKK.
```

---

# 67. Project Forecast

A simple forecast MAY be:

```text
Actual to date
+
remaining planned cost
=
expected final cost
```

---

# 68. Forecast

Example:

```text
Budget = 100,000
Actual = 60,000
Remaining planned = 50,000
Forecast = 110,000
```

---

# 69. Forecast Status

Recommended:

```text
ON_TRACK
AT_RISK
OVER_BUDGET
```

---

# 70. Forecast is Not Accounting

Forecast values SHALL never modify the accounting ledger.

---

# 71. Project Expense Entry

Project expenses SHALL normally be entered through:

```text
AccountingService
```

with:

```text
project_id
```

---

# 72. No Direct Project Ledger

The project module SHALL not create a second financial ledger.

---

# 73. Expense Example

```text
Debit Maintenance 2,000
Credit Bank        2,000
Project P-2026-001
```

The project receives:

```text
Actual expense = 2,000
```

---

# 74. Project Income Example

```text
Debit Bank          10,000
Credit Grant Income 10,000
Project P-2026-001
```

The project receives:

```text
Actual income = 10,000
```

---

# 75. Project Net Position

Simple project result:

```text
Project Income
-
Project Expense
=
Project Net
```

---

# 76. Project Funding Position

A funding report may show:

```text
Planned Funding
Confirmed Funding
Received Funding
```

---

# 77. Funding Gap

```text
Project Budget
-
Confirmed Funding
=
Funding Gap
```

---

# 78. Funding Gap Example

```text
Budget: 100,000
Confirmed: 70,000
Gap: 30,000
```

---

# 79. Funding Coverage

```text
Confirmed Funding / Budget
```

Example:

```text
70%
```

---

# 80. Project Financial Dashboard

Recommended indicators:

```text
Budget
Actual
Remaining
Utilisation
Forecast
Funding
Funding Gap
Project Result
```

---

# 81. Project Dashboard Security

Financial project information SHALL require:

```text
VIEW_PROJECT_FINANCE
```

or equivalent authority.

---

# 82. Project List

Minimum:

```text
project number
name
status
start
end
owner
budget
actual
```

---

# 83. Project Detail

Sections:

```text
Overview
Budget
Funding
Actuals
Documents
Reports
History
```

---

# 84. Project History

Record important changes:

```text
created
status changed
budget approved
budget revised
closed
```

---

# 85. Project Audit Events

Minimum:

```text
PROJECT_CREATED
PROJECT_UPDATED
PROJECT_STATUS_CHANGED
PROJECT_BUDGET_CREATED
PROJECT_BUDGET_APPROVED
PROJECT_BUDGET_REVISED
PROJECT_CLOSED
PROJECT_FUNDING_CHANGED
PROJECT_REPORT_EXPORTED
```

---

# 86. Accounting Audit

Accounting transactions linked to a project are already audited by the accounting core.

The project module SHALL not duplicate accounting audit records.

---

# 87. Project Documents

Project documents SHALL be managed by the document module.

The project module stores only references.

---

# 88. Document Link

A project MAY have:

```text
document_id
```

references.

---

# 89. No Document Duplication

Project module SHALL not duplicate the physical document store.

---

# 90. Project Membership

A project MAY optionally reference members.

Example:

```text
project participants
```

This is optional and should not create a second member database.

---

# 91. Project Owner User

A project owner MAY reference:

```text
user_id
```

not a free-text duplicate of the user identity.

---

# 92. Project Contacts

External contacts may be stored separately if needed.

For v1.0, simple contact fields are sufficient.

---

# 93. Project Budget Database Tables

Recommended:

```text
projects
project_budgets
project_budget_lines
project_funding
```

---

# 94. Projects Table

Conceptual:

```text
id
project_number
name
status
start_date
end_date
description
owner_user_id
created_by
created_at
updated_at
```

---

# 95. Project Budgets Table

```text
id
project_id
name
status
version
approved_at
approved_by
created_at
updated_at
```

---

# 96. Project Budget Lines Table

```text
id
budget_id
category
description
amount_minor
account_id
created_at
updated_at
```

---

# 97. Project Funding Table

```text
id
project_id
name
source_type
planned_amount_minor
confirmed_amount_minor
received_amount_minor
status
grant_id
created_at
updated_at
```

---

# 98. Foreign Keys

Enforce:

```text
project_budgets.project_id → projects.id
project_budget_lines.budget_id → project_budgets.id
project_budget_lines.account_id → accounts.id
project_funding.project_id → projects.id
project_funding.grant_id → grants.id
```

The grant reference is optional until the grant module exists.

---

# 99. Indexes

Recommended:

```text
projects.project_number
projects.status
projects.start_date
projects.end_date
project_budgets.project_id
project_budget_lines.budget_id
project_budget_lines.account_id
project_funding.project_id
project_funding.status
```

---

# 100. Unique Constraints

Recommended:

```text
project_number UNIQUE
```

Budget version uniqueness:

```text
(project_id, version) UNIQUE
```

---

# 101. Project Budget Lifecycle

```text
DRAFT
 ↓
SUBMITTED
 ↓
APPROVED
 ↓
ACTIVE
 ↓
CLOSED
```

`SUBMITTED` is optional if a formal approval workflow is desired.

---

# 102. Budget Approval

Approval SHALL record:

```text
approved_by
approved_at
```

---

# 103. Budget Revision

Revision SHALL create a new version rather than silently changing the approved baseline.

---

# 104. Active Budget

A project SHOULD have one active approved budget baseline.

---

# 105. Multiple Budgets

Historical budget versions remain available.

---

# 106. Budget Comparison

Reports MAY compare:

```text
original budget
current approved budget
actual
forecast
```

---

# 107. Project Cost Categories

Categories SHALL support the association's practical needs.

Do not create an excessive hierarchy.

---

# 108. Project Cost Classification

Where an accounting account is linked to a budget category, actuals can be mapped by:

```text
account_id
+
project_id
```

---

# 109. Unmapped Actual

If a project transaction uses an account with no budget mapping:

```text
actual still exists
```

but the report may show:

```text
UNMAPPED
```

rather than inventing a category.

---

# 110. Budget Mapping Warning

The project dashboard SHOULD warn about material unmapped actual costs.

---

# 111. Budget Line Validation

Require:

```text
budget exists
category exists
amount >= 0
```

Account mapping is optional if the project uses category-only planning.

---

# 112. Zero Budget Line

Zero lines may be rejected or allowed as placeholders.

For simplicity, reject zero lines unless explicitly needed.

---

# 113. Negative Budget

Negative budget lines SHALL be rejected.

---

# 114. Funding Amount

Funding amounts SHALL be non-negative.

---

# 115. Funding Consistency

Recommended warnings:

```text
received > confirmed
confirmed > planned
```

These may be allowed with explicit explanation.

---

# 116. Funding Validation

The service SHALL prevent impossible states unless authorised adjustment rules exist.

---

# 117. Project Closure

Closing a project SHALL check:

```text
status
open budget
unreconciled project funding
```

and display warnings.

---

# 118. Project Closure Rule

Closure does not delete history.

---

# 119. Closed Project Accounting

Historical accounting entries remain reportable.

New project costs SHOULD normally be blocked or require explicit reopening.

---

# 120. Reopen Project

If supported:

```text
REOPEN_PROJECT
```

permission SHALL be required.

---

# 121. Cancelled Project

Cancellation should require:

```text
reason
```

and audit.

---

# 122. Project Status Transition

Allowed baseline:

```text
PLANNED → ACTIVE
PLANNED → CANCELLED
ACTIVE → ON_HOLD
ACTIVE → COMPLETED
ACTIVE → CANCELLED
ON_HOLD → ACTIVE
ON_HOLD → CANCELLED
```

Archived status follows closure.

---

# 123. Invalid Status Transition

The service SHALL reject invalid transitions.

---

# 124. Project Creation

Create flow:

```text
validate
 ↓
allocate number
 ↓
create project
 ↓
audit
```

---

# 125. Project Budget Creation

```text
create project
 ↓
create draft budget
 ↓
add lines
 ↓
validate
 ↓
approve
```

---

# 126. Budget Approval Validation

Before approval:

```text
project active/planned
budget has lines
totals valid
funding information available if required
```

---

# 127. Project Funding Approval

Funding status may be updated independently of budget approval.

---

# 128. Grant Integration Boundary

Grant approval remains a grant-module function.

Project funding reflects the project's relationship to that funding.

---

# 129. Donation Integration

Donations may be represented as project funding and separately as accounting transactions.

---

# 130. Accounting Integration Boundary

ProjectService requests accounting operations but does not own accounting posting.

---

# 131. Project Actual Query

Actual project costs:

```text
SUM(posted voucher lines where project_id = project)
```

restricted to expense accounts where required.

---

# 132. Project Income Query

Actual project income:

```text
SUM(posted voucher lines where project_id = project)
```

for income accounts.

---

# 133. Project Financial Result

```text
income - expense
```

---

# 134. Project Cost Query

Expenses may be grouped by:

```text
account
budget category
month
```

---

# 135. Project Revenue Query

Income may be grouped by:

```text
account
funding source
month
```

where the data is available.

---

# 136. Project Monthly Report

Recommended:

```text
month
income
expense
net
cumulative expense
budget utilisation
```

---

# 137. Project Annual Report

For each project:

```text
budget
actual income
actual expense
result
funding
variance
```

---

# 138. Budget Variance Report

Show:

```text
category
budget
actual
variance
utilisation
```

---

# 139. Project Funding Report

Show:

```text
source
planned
confirmed
received
remaining
status
```

---

# 140. Project Summary

A one-page summary SHOULD show:

```text
purpose
period
status
owner
budget
funding
actual
forecast
variance
```

---

# 141. Project Report Export

May support:

```text
PDF
XLSX
CSV
```

depending on the existing export capabilities.

---

# 142. Export Permission

Require:

```text
EXPORT_PROJECT_REPORTS
```

---

# 143. Export Audit

Material project report exports SHOULD be auditable.

---

# 144. Project GUI

Minimum screens:

```text
Project List
Project Detail
Budget Editor
Funding
Actuals
Budget vs Actual
Project Reports
```

---

# 145. Project List Filters

```text
status
owner
date
```

---

# 146. Project Detail Tabs

Recommended:

```text
Overview
Budget
Funding
Actuals
Documents
History
```

---

# 147. Budget Editor

Show:

```text
category
description
budget amount
account
```

and:

```text
total
```

---

# 148. Budget Editor Validation

The UI SHOULD show:

```text
total budget
```

and validation status.

---

# 149. Funding Editor

Show:

```text
source
planned
confirmed
received
status
```

---

# 150. Actuals View

Show posted transactions:

```text
date
voucher
account
description
amount
```

---

# 151. Actuals Read-Only

Project actuals SHALL be read-only in the project module.

Corrections occur in accounting.

---

# 152. Budget vs Actual View

Show:

```text
budget
actual
variance
```

by category.

---

# 153. Forecast View

Show:

```text
budget
actual
remaining budget
forecast
```

---

# 154. Project Alert View

Potential alerts:

```text
budget > 80%
budget exceeded
funding gap
unmapped actual
project end approaching
```

---

# 155. Alert Principle

Alerts inform users.

They do not automatically modify data.

---

# 156. Project Dashboard Simplicity

The dashboard SHALL remain understandable to volunteers and board members.

---

# 157. No ERP Complexity

Do not add:

```text
work breakdown structure engine
resource planning suite
procurement module
complex project scheduling
```

for v1.0.

---

# 158. Project Documents

Document references may include:

```text
grant application
quotes
invoices
contracts
photos
completion report
```

Actual files belong to document management.

---

# 159. Invoice Link

A project may link a document to an accounting voucher.

The project module should not duplicate the invoice file.

---

# 160. Project and Membership

Membership-funded projects may report membership income through project-tagged accounting transactions if the association chooses.

---

# 161. Project and Grant

Grant income can be tagged to a project.

---

# 162. Project and Donation

Donation income can be tagged to a project.

---

# 163. Project and Expense

Any qualifying accounting expense can be tagged to a project.

---

# 164. Project Tagging Rule

A project tag is metadata on the accounting line.

It does not change the accounting account.

---

# 165. Project Tag Validation

If a project is:

```text
CLOSED
```

new project-tagged postings SHOULD be rejected unless explicit reopening is authorised.

---

# 166. Accounting Service Example

Conceptually:

```python
accounting_service.post_voucher(
    ...,
    project_id=project_id
)
```

The accounting service remains responsible for posting.

---

# 167. No Direct SQL

Project code SHALL not directly insert into:

```text
vouchers
voucher_lines
```

---

# 168. Project Repository

Recommended:

```text
get_by_id()
get_by_number()
list()
create()
update()
update_status()
```

---

# 169. Budget Repository

Recommended:

```text
create()
get_current()
get_versions()
save_line()
approve()
close()
```

---

# 170. Funding Repository

Recommended:

```text
create()
update()
list_by_project()
```

---

# 171. Project Finance Repository

A read-only query repository MAY provide:

```text
actuals
budget_vs_actual
funding_summary
```

---

# 172. Service Dependencies

```text
ProjectService
 ↓
SecurityContext
 ↓
ProjectRepository
 ↓
AuditService
```

Budget:

```text
ProjectBudgetService
 ↓
SecurityContext
 ↓
BudgetRepository
 ↓
AuditService
```

Finance:

```text
ProjectFinanceService
 ↓
AccountingRepository
 ↓
ProjectRepository
```

---

# 173. Circular Dependency Avoidance

AccountingService SHALL not depend on ProjectService.

Project services depend on accounting interfaces for financial execution.

---

# 174. Project Transaction

Creating a project and audit may be atomic.

---

# 175. Budget Approval Transaction

```text
BEGIN
 ↓
validate budget
 ↓
set approved
 ↓
audit
 ↓
COMMIT
```

---

# 176. Budget Revision Transaction

```text
BEGIN
 ↓
copy previous baseline
 ↓
create new version
 ↓
apply changes
 ↓
audit
 ↓
COMMIT
```

---

# 177. Funding Update Transaction

```text
validate
 ↓
update
 ↓
audit
 ↓
commit
```

---

# 178. Project Close Transaction

```text
validate
 ↓
set completed/closed
 ↓
audit
 ↓
commit
```

---

# 179. Project Closure Failure

If validation or audit fails:

```text
ROLLBACK
```

---

# 180. Budget Calculation

Budget total:

```text
Σ budget line amounts
```

---

# 181. Actual Calculation

Actual:

```text
Σ posted accounting lines
```

---

# 182. Variance Calculation

```text
variance = budget - actual
```

Display label SHALL make direction clear.

---

# 183. Utilisation Calculation

```text
utilisation = actual / budget × 100
```

If budget is zero, display:

```text
N/A
```

not division by zero.

---

# 184. Funding Coverage Calculation

```text
coverage = confirmed / budget × 100
```

If budget is zero:

```text
N/A
```

---

# 185. Forecast Calculation

Simple baseline:

```text
forecast = actual + remaining planned
```

---

# 186. Forecast Warning

If:

```text
forecast > budget
```

status:

```text
AT_RISK
```

or:

```text
OVER_BUDGET
```

depending on actuals.

---

# 187. Project Health

Optional combined status:

```text
GREEN
AMBER
RED
```

based on budget and funding indicators.

---

# 188. Health is Advisory

Project health SHALL not automatically change project status.

---

# 189. Budget Alerts

Thresholds MAY be configured:

```text
80%
90%
100%
```

---

# 190. No Hard-Coded Threshold

Thresholds should be configuration values.

---

# 191. Funding Alerts

Alert if:

```text
confirmed funding < budget
```

at a configurable threshold.

---

# 192. Project End Alert

Alert if:

```text
end date approaching
```

without changing status automatically.

---

# 193. Negative Testing

Mandatory:

```text
duplicate project number
invalid status transition
negative budget
invalid budget account
budget approval without lines
duplicate budget version
actual on closed project
unauthorised budget approval
invalid funding amount
accounting posting failure
```

---

# 194. Project Scenario 1

```text
Create project
 ↓
Create budget
 ↓
Approve budget
```

Expected:

```text
project exists
budget approved
audit events exist
```

---

# 195. Project Scenario 2

```text
Budget 100,000
Actual 25,000
```

Expected:

```text
remaining 75,000
utilisation 25%
```

---

# 196. Project Scenario 3

```text
Budget 100,000
Actual 110,000
```

Expected:

```text
overspend 10,000
alert
```

---

# 197. Project Scenario 4

```text
Budget 100,000
Confirmed funding 70,000
```

Expected:

```text
funding gap 30,000
```

---

# 198. Project Scenario 5

```text
Expense voucher 2,000
project_id = P-2026-001
```

Expected:

```text
project actual = 2,000
```

---

# 199. Project Scenario 6

```text
Project closed
 ↓
attempt new project-tagged expense
```

Expected:

```text
rejected
```

unless explicitly reopened.

---

# 200. Project Scenario 7

```text
Budget approved
 ↓
revise budget
```

Expected:

```text
old version retained
new version created
audit recorded
```

---

# 201. Project Scenario 8

```text
Unauthorised user
 ↓
approve budget
```

Expected:

```text
DENIED
```

---

# 202. Project Scenario 9

```text
Accounting posting fails
```

Expected:

```text
no partial project financial state
```

---

# 203. Project Scenario 10

```text
Project report export
```

Expected:

```text
authorised user → success
unauthorised user → denied
```

---

# 204. Security Tests

Test:

```text
VIEW_PROJECTS
CREATE_PROJECT
EDIT_PROJECT
MANAGE_PROJECT_BUDGET
APPROVE_PROJECT_BUDGET
VIEW_PROJECT_FINANCE
EXPORT_PROJECT_REPORTS
```

---

# 205. Audit Tests

Verify:

```text
project creation
budget approval
budget revision
status change
closure
funding update
report export
```

---

# 206. Accounting Integration Test

Create:

```text
project
+
expense voucher
```

Then verify:

```text
project actual
=
accounting posted amount
```

---

# 207. Report Integration Test

Post:

```text
income
expense
```

for a project.

Verify:

```text
project result
=
income - expense
```

---

# 208. Budget Integration Test

Create:

```text
budget 50,000
expense 10,000
```

Verify:

```text
remaining 40,000
utilisation 20%
```

---

# 209. Funding Integration Test

Create:

```text
budget 50,000
confirmed funding 40,000
```

Verify:

```text
funding gap 10,000
```

---

# 210. Restore Test

After database restore verify:

```text
projects
budgets
funding
project tags
accounting
audit
```

remain consistent.

---

# 211. Migration Test

Migrations SHALL preserve project IDs and accounting project references.

---

# 212. Performance

For a small association, the project module should comfortably support:

```text
hundreds of projects
thousands of budget lines
tens of thousands of accounting lines
```

without specialised infrastructure.

---

# 213. Test Dataset

Recommended:

```text
500 projects
2,000 budgets
10,000 budget lines
50,000 accounting lines
```

These are test volumes, not product limits.

---

# 214. Project Search

Search by:

```text
project number
name
status
owner
```

---

# 215. Project Sorting

Sort by:

```text
project number
name
start date
status
```

---

# 216. Budget Sorting

Budget lines may sort by:

```text
category
account
description
```

---

# 217. Funding Sorting

Funding sources may sort by:

```text
status
planned amount
received amount
```

---

# 218. Project Report Simplicity

A board report should be understandable without accounting expertise.

---

# 219. Board Project Summary

Example:

```text
Project: Restoration
Budget: 250,000
Confirmed Funding: 200,000
Actual Expense: 125,000
Remaining Budget: 125,000
Funding Gap: 50,000
Status: Active
```

---

# 220. Treasurer Project View

Treasurer may need:

```text
account-level actuals
voucher references
budget variance
```

---

# 221. Project Manager View

Project manager may need:

```text
budget
actual
remaining
forecast
funding
```

without unrestricted accounting administration.

---

# 222. Separation of Duties

Project manager does not automatically receive:

```text
POST_VOUCHER
```

---

# 223. Board Oversight

Board can view project financial status without necessarily being able to modify project accounting.

---

# 224. Project Approval

Budget approval may be performed by an authorised board or treasurer role according to association policy.

---

# 225. Governance Boundary

MFM enforces permissions.

The association defines the actual authority matrix.

---

# 226. No Autonomous Budget Approval

AI or automated processes SHALL not approve a project budget.

---

# 227. AI Project Analysis

Future AI MAY:

```text
detect overspend
forecast completion
identify funding gap
summarise project status
compare budget vs actual
```

---

# 228. AI Project Execution Boundary

AI SHALL not:

```text
approve budget
change funding authority
post accounting transaction
close project
```

without explicit human authorisation.

---

# 229. AI Recommendation Flow

```text
ANALYSIS
 ↓
RECOMMENDATION
 ↓
HUMAN REVIEW
 ↓
AUTHORISATION
 ↓
EXECUTION
```

---

# 230. Project Circuit Breaker

If project financial integrity cannot be established:

```text
stop automatic financial action
```

---

# 231. Project Safe State

If budget data is unavailable:

```text
do not display guessed budget
```

Display:

```text
Budget unavailable
```

---

# 232. Accounting Safe State

If accounting actuals cannot be loaded:

```text
do not report stale actuals as current
```

---

# 233. Funding Safe State

If funding data is incomplete:

```text
show incomplete status
```

rather than assuming full funding.

---

# 234. Recovery

After an error:

```text
verify project
verify budget
verify accounting
verify audit
```

before retry.

---

# 235. Idempotency

Repeated:

```text
budget approval
funding update
project close
```

shall not create duplicate state changes.

---

# 236. Project Closure Idempotency

A completed project cannot be completed again without controlled rejection.

---

# 237. Budget Approval Idempotency

An already approved budget cannot be approved again as a new approval event.

---

# 238. Funding Update Idempotency

Update operations should use current state validation.

---

# 239. Project Number Allocation

Use the existing application number-generation pattern.

---

# 240. No GUI Number Generation

Project numbers SHALL be allocated by the service/database layer.

---

# 241. Project Budget Numbering

Budget versions may be:

```text
1
2
3
```

---

# 242. Project Document Links

Document references should be auditable where links are created/removed.

---

# 243. Project Contact Data

Do not duplicate member records when a contact is already a member.

---

# 244. Member Link

A project MAY reference:

```text
member_id
```

for a project participant.

---

# 245. Participant Scope

Participant management is optional and not required for financial project operation.

---

# 246. Project Import

CSV/XLSX project import is optional.

---

# 247. Import Validation

If implemented:

```text
preview
validate
confirm
commit
audit
```

---

# 248. Project Export

Exports may include:

```text
project summary
budget
actual
funding
```

---

# 249. Export Privacy

Do not export unnecessary personal data about project owners or contacts.

---

# 250. Project Backup

Projects, budgets and funding SHALL be included in the normal database backup.

---

# 251. Project Restore

Restore verification SHALL include:

```text
project count
budget totals
funding totals
project-accounting links
```

---

# 252. Project Data Integrity

Foreign keys SHALL be enabled.

---

# 253. SQLite Requirement

Every SQLite connection SHALL enable foreign key enforcement.

---

# 254. Transaction Boundary

Project mutations SHALL use the existing database transaction framework.

---

# 255. No Direct Database Connections

Project services SHALL use the established database abstraction.

---

# 256. Configuration

Project configuration MAY include:

```text
project_number_prefix
budget_warning_threshold
budget_critical_threshold
```

---

# 257. Default Thresholds

Illustrative:

```text
80%
90%
100%
```

These are configuration values.

---

# 258. No Hard-Coded Policy

Budget approval policy SHALL remain configurable.

---

# 259. Project Status Configuration

The baseline statuses may be fixed in v1.0.

Custom status workflows are not required.

---

# 260. Project Health Configuration

Health calculation thresholds may be configured.

---

# 261. Project Reports

Minimum reports:

```text
Project Register
Project Summary
Budget vs Actual
Funding Status
Project Expenses
Project Income
Project Result
Project History
```

---

# 262. Project Register

Show:

```text
number
name
status
owner
period
budget
```

---

# 263. Budget Report

Show:

```text
category
budget
actual
variance
```

---

# 264. Funding Report

Show:

```text
source
planned
confirmed
received
gap
```

---

# 265. Expense Report

Show:

```text
date
voucher
account
description
amount
```

---

# 266. Income Report

Show:

```text
date
voucher
account
description
amount
```

---

# 267. Project Result Report

Show:

```text
income
expense
net
```

---

# 268. Project History Report

Show:

```text
status changes
budget revisions
funding changes
```

---

# 269. Project Acceptance Criteria

The implementation is accepted when:

```text
project can be created
project status works
budget can be created
budget can be approved
budget revisions preserve history
actuals come from accounting
funding can be tracked
budget vs actual works
funding gap works
project reports work
security works
audit works
```

---

# 270. Release Blockers

Release SHALL be blocked by:

```text
duplicate project number
incorrect budget totals
incorrect actual totals
project accounting not linked
unauthorised budget approval
loss of budget history
project closure losing accounting references
```

---

# 271. Implementation Order

Implement:

```text
1. projects
2. project status
3. project budgets
4. budget lines
5. funding
6. ProjectService
7. BudgetService
8. accounting query integration
9. project GUI
10. reports
11. audit
12. tests
```

---

# 272. First Project Milestone

```text
Create project
 ↓
Set dates
 ↓
Assign owner
 ↓
View project
```

---

# 273. Second Project Milestone

```text
Create budget
 ↓
Add budget lines
 ↓
Approve budget
```

---

# 274. Third Project Milestone

```text
Post project expense
 ↓
View actual
 ↓
Compare budget
```

---

# 275. Fourth Project Milestone

```text
Add funding
 ↓
Calculate funding gap
 ↓
Generate project report
```

---

# 276. Fifth Project Milestone

Integrate:

```text
documents
grants
membership
```

where applicable.

---

# 277. End-to-End Scenario

```text
Create project
 ↓
Create budget 100,000
 ↓
Confirm funding 80,000
 ↓
Post expense 25,000
 ↓
View budget vs actual
 ↓
View funding gap
 ↓
Export project summary
 ↓
Audit
```

Expected:

```text
Budget = 100,000
Actual = 25,000
Remaining = 75,000
Funding = 80,000
Funding gap = 20,000
```

---

# 278. Project Accounting Reconciliation

For all project-tagged posted accounting lines:

```text
sum by project
```

must equal the project finance report.

---

# 279. Project Budget Reconciliation

Budget report total:

```text
sum budget lines
```

must equal displayed budget total.

---

# 280. Funding Reconciliation

Funding report total:

```text
sum funding records
```

must equal project funding summary.

---

# 281. No Duplicate Financial Truth

Do not store:

```text
project_actual_balance
```

as an independently editable value.

Derive it from accounting.

---

# 282. No Duplicate Budget Truth

Do not maintain:

```text
budget_total
```

as a manually editable field.

Derive it from budget lines.

---

# 283. No Duplicate Funding Truth

Funding totals may be derived from funding records.

---

# 284. Project Financial Digital Twin

A project summary can combine:

```text
planned
funded
actual
forecast
```

but it is a reporting view, not a second ledger.

---

# 285. Project Economic Model

```text
BUDGET
   ↓
FUNDING
   ↓
ACTUAL
   ↓
FORECAST
   ↓
DECISION
```

---

# 286. Strategic Boundary

Project analysis may support strategy but SHALL not change strategic priorities automatically.

---

# 287. Resilience Boundary

A project budget should not automatically consume organisational reserves.

Reserve decisions remain human governance decisions.

---

# 288. Capital Boundary

Project investment may use capital resources, but capital allocation remains subject to the accounting and governance layers.

---

# 289. Resource Boundary

Resource requirements may be added later.

v1.0 focuses on financial project control.

---

# 290. Project Risk

Optional project risk fields may include:

```text
risk_status
risk_summary
```

A full risk management system is not required.

---

# 291. Project Risk Alerts

Risk alerts are informational.

They do not automatically alter budgets.

---

# 292. Project Completion

Completion may require:

```text
final actuals
final funding
final report
```

The exact checklist is configurable.

---

# 293. Project Final Report

Recommended:

```text
purpose
activities
budget
actual
funding
result
documents
```

---

# 294. Final Project Closure

After completion:

```text
status = COMPLETED
```

Historical reporting remains available.

---

# 295. Final Governing Principle

> **Project management in MFM is a planning and reporting layer above accounting: budgets describe intent, funding describes capacity, accounting records reality, and reports connect the three without duplicating financial truth.**

# END OF MFM v1.0 PROJECT & BUDGET IMPLEMENTATION

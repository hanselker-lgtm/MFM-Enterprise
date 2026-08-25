# MFM v1.0 REPORTING & MANAGEMENT DASHBOARD

## MaritimForeningsManager — Rapportering, ledelsesoverblik og informationspræsentation

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Documents & Grants  
**Purpose:** Define the practical reporting and management-dashboard layer for an almennyttig association

---

# 1. Purpose

The Reporting & Management Dashboard module SHALL transform authoritative MFM data into clear information for daily administration, financial management and board oversight.

It SHALL provide:

- operational dashboards;
- financial reports;
- membership reports;
- project reports;
- grant reports;
- budget reports;
- accounting reports;
- document status;
- deadline overview;
- management KPIs;
- exports;
- traceability to source records.

The module SHALL be a read-oriented presentation and reporting layer.

It SHALL NOT become a second data store or accounting system.

---

# 2. Core Principle

> **Reports explain the data; they do not create the data.**

Authoritative sources remain:

```text
MEMBERSHIP
    ↓
MembershipService

ACCOUNTING
    ↓
AccountingService

PROJECTS
    ↓
ProjectService

GRANTS
    ↓
GrantService

DOCUMENTS
    ↓
DocumentService
```

The reporting layer combines these sources.

---

# 3. Architectural Position

```text
DATABASE FOUNDATION
        ↓
ACCOUNTING CORE
        ↓
MEMBERSHIP
        ↓
PROJECTS & BUDGET
        ↓
DOCUMENTS & GRANTS
        ↓
REPORTING & DASHBOARD
```

The dashboard is therefore downstream of the operational modules.

---

# 4. Reporting Architecture

```text
                 +----------------+
                 |   DASHBOARD    |
                 +--------+-------+
                          |
                 +--------+-------+
                 | REPORT SERVICE |
                 +--------+-------+
                          |
       +------------------+------------------+
       |          |          |        |      |
   ACCOUNTING MEMBERSHIP PROJECTS GRANTS DOCUMENTS
       |          |          |        |      |
       +----------+----------+--------+------+
                          |
                   AUTHORITATIVE DATA
```

---

# 5. Reporting Principles

Reports SHALL be:

- accurate;
- reproducible;
- understandable;
- traceable;
- filterable;
- exportable;
- permission-aware.

Reports SHOULD avoid unnecessary complexity.

---

# 6. Management Dashboard

The main dashboard SHOULD provide a concise association overview.

Recommended areas:

```text
FINANCIAL
MEMBERSHIP
PROJECTS
GRANTS
DOCUMENTS
DEADLINES
SYSTEM HEALTH
```

---

# 7. Financial Dashboard

Recommended indicators:

```text
BANK BALANCE
INCOME YTD
EXPENSE YTD
RESULT YTD
OPEN MEMBERSHIP FEES
OUTSTANDING FEES
ACTIVE PROJECT BUDGET
PROJECT ACTUAL
FUNDING GAP
```

Financial values SHALL originate from AccountingService and related authoritative services.

---

# 8. Membership Dashboard

Recommended:

```text
TOTAL MEMBERS
ACTIVE MEMBERS
NEW MEMBERS THIS YEAR
MEMBERS LEFT THIS YEAR
OPEN FEES
PAID FEES
OUTSTANDING FEES
```

---

# 9. Project Dashboard

Recommended:

```text
ACTIVE PROJECTS
PROJECT BUDGET
PROJECT ACTUAL
PROJECT VARIANCE
PROJECTS OVER BUDGET
TOTAL FUNDING GAP
```

---

# 10. Grant Dashboard

Recommended:

```text
OPEN APPLICATIONS
REQUESTED FUNDING
APPROVED FUNDING
RECEIVED FUNDING
PENDING FUNDING
DEADLINES
REPORTS DUE
```

---

# 11. Document Dashboard

Recommended:

```text
RECENT DOCUMENTS
MISSING FILES
INTEGRITY WARNINGS
ACTIVE DOCUMENTS
ARCHIVED DOCUMENTS
```

---

# 12. Deadline Dashboard

The system SHOULD combine relevant deadlines:

```text
GRANT APPLICATION
GRANT REPORT
PROJECT DEADLINE
MEMBERSHIP DEADLINE
ACCOUNTING DEADLINE
```

Each deadline SHALL identify its source.

---

# 13. Deadline Status

Recommended:

```text
OK
DUE_SOON
TODAY
OVERDUE
COMPLETED
```

Thresholds SHALL be configurable.

---

# 14. Dashboard Date Context

Every financial dashboard SHALL clearly indicate its period.

Example:

```text
Financial Year: 2027
Period: 01-01-2027 to 31-12-2027
```

Avoid displaying financial totals without a clear time context.

---

# 15. Dashboard Refresh

The dashboard SHOULD refresh from authoritative services when opened or manually refreshed.

A refresh SHALL not modify business data.

---

# 16. Dashboard Caching

Caching MAY be introduced for performance.

Cached values SHALL never become authoritative.

The system SHALL be able to recalculate figures from source data.

---

# 17. Accounting Reports

Minimum financial reports:

1. Trial balance
2. General ledger
3. Journal
4. Income statement
5. Balance sheet
6. Budget versus actual
7. Account statement
8. Voucher list
9. Bank reconciliation
10. Project financial report

---

# 18. Trial Balance

The trial balance SHALL show:

```text
ACCOUNT
DEBIT
CREDIT
```

Total debit SHALL equal total credit.

The report SHALL provide a clear status:

```text
BALANCED
```

or:

```text
ERROR
```

---

# 19. General Ledger

The general ledger SHALL provide:

```text
Account
Date
Voucher
Description
Debit
Credit
Balance
```

Filters:

```text
Account
Date range
Project
Voucher
```

---

# 20. Journal

The journal SHALL list transactions chronologically.

Minimum:

```text
Date
Voucher number
Description
Account
Debit
Credit
```

---

# 21. Income Statement

The income statement SHALL show:

```text
INCOME
-
EXPENSES
=
RESULT
```

It SHOULD support:

- current period;
- year-to-date;
- previous year;
- budget comparison.

---

# 22. Balance Sheet

The balance sheet SHALL show:

```text
ASSETS
LIABILITIES
EQUITY
```

and verify:

```text
ASSETS = LIABILITIES + EQUITY
```

If the report does not balance, the system SHALL clearly identify an accounting integrity issue.

---

# 23. Budget versus Actual

The report SHALL show:

```text
ACCOUNT
BUDGET
ACTUAL
VARIANCE
UTILISATION
```

For expenses:

```text
Variance = Budget - Actual
```

For income:

```text
Variance = Actual - Budget
```

---

# 24. Account Statement

The account statement SHALL provide transaction detail for one account.

Example:

```text
Account: 5020 Telephone

Opening balance
Transactions
Closing balance
```

---

# 25. Voucher Report

The voucher report SHALL support:

```text
Date
Voucher number
Description
Status
Amount
Project
Created by
```

Users SHOULD be able to open the source voucher.

---

# 26. Bank Reconciliation Report

The report SHALL show:

```text
Statement balance
Book balance
Difference
Status
Reconciliation date
```

---

# 27. Membership Reports

Minimum:

1. Member list
2. Active members
3. New members
4. Members who left
5. Membership by type
6. Fee status
7. Outstanding fees
8. Payment report
9. Membership history

---

# 28. Member List Report

Recommended fields:

```text
Member number
Name
Membership type
Status
Email
Phone
Join date
```

Fields SHALL be permission-aware.

---

# 29. Active Member Report

The active member report SHALL derive status from the MembershipService.

It SHALL not rely on manually maintained dashboard totals.

---

# 30. Membership Movement Report

The report SHOULD show:

```text
Opening members
New members
Members leaving
Closing members
```

This provides a simple annual membership development overview.

---

# 31. Fee Status Report

Minimum:

```text
Member
Fee
Paid
Outstanding
Status
```

Filters:

```text
Year
Membership type
Status
```

---

# 32. Outstanding Fee Report

The report SHALL identify:

```text
Member
Due date
Amount
Paid
Outstanding
Days overdue
```

The report SHALL use authoritative fee and payment information.

---

# 33. Project Reports

Minimum:

1. Project overview
2. Project budget
3. Project actual
4. Budget versus actual
5. Project income
6. Project expenditure
7. Funding overview
8. Funding gap
9. Project transactions
10. Final project report

---

# 34. Project Overview

Recommended:

```text
Project number
Name
Status
Responsible
Start
End
Budget
Actual
Variance
Funding
Funding gap
```

---

# 35. Project Budget Report

The report SHALL show:

```text
Budget line
Account
Budget amount
Actual amount
Variance
```

---

# 36. Project Financial Report

The project financial report SHALL calculate:

```text
Project income
Project expenditure
Project result
Project budget
Budget variance
Confirmed funding
Funding gap
```

Actual financial values SHALL come from posted accounting transactions.

---

# 37. Project Transaction Report

Each transaction SHALL be traceable to:

```text
Project
 ↓
Voucher line
 ↓
Voucher
 ↓
Account
```

---

# 38. Grant Reports

Minimum:

1. Grant register
2. Open applications
3. Grant deadline report
4. Requested funding
5. Approved funding
6. Received funding
7. Outstanding grant payments
8. Grant reporting deadlines
9. Grant/project overview

---

# 39. Grant Register

Recommended:

```text
Grant number
Funder
Project
Application date
Deadline
Requested
Approved
Received
Status
```

---

# 40. Grant Funding Report

The report SHALL distinguish:

```text
REQUESTED
APPROVED
RECEIVED
OUTSTANDING
```

These figures SHALL not be conflated.

---

# 41. Grant Deadline Report

The report SHALL list:

```text
Funder
Grant
Project
Deadline
Status
Responsible
```

Sort by nearest deadline first.

---

# 42. Document Reports

Minimum:

1. Document register
2. Missing documents
3. Integrity report
4. Project documents
5. Grant documents
6. Archived documents

---

# 43. Document Register

Recommended:

```text
Document
Type
Date
Related entity
Status
Version
Checksum status
```

---

# 44. Missing Document Report

The report SHALL show:

```text
Document ID
File name
Expected path
Entity
Last known status
```

It SHALL not remove missing document records.

---

# 45. Integrity Report

The report SHALL distinguish:

```text
VALID
MISSING
CHANGED
ERROR
NOT VERIFIED
```

---

# 46. Management Summary

The association SHOULD have a concise management report containing:

```text
Membership
Financial position
Current result
Budget status
Projects
Funding
Upcoming deadlines
Risks / warnings
```

This report is intended for board meetings.

---

# 47. Board Report

The board report SHOULD be understandable without technical knowledge.

Recommended sections:

```text
1. Executive Summary
2. Membership
3. Financial Result
4. Cash / Bank
5. Budget
6. Projects
7. Grants / Funding
8. Important Deadlines
9. Exceptions / Warnings
```

---

# 48. Executive Summary

The executive summary SHALL highlight only material information.

Examples:

```text
Membership increased by 8 members.
Operating result is DKK 24,000 positive.
One project is above budget.
Two grant applications are awaiting response.
One grant report is due next month.
```

Exact wording SHALL be generated from current data.

---

# 49. Management Exceptions

The dashboard SHOULD prioritise exceptions.

Examples:

```text
PROJECT OVER BUDGET
FUNDING GAP
OVERDUE GRANT REPORT
UNRECONCILED BANK
OUTSTANDING FEES
MISSING DOCUMENT
BACKUP OUTDATED
```

Normal conditions should not overwhelm the user.

---

# 50. Exception Severity

Recommended:

```text
INFO
WARNING
CRITICAL
```

Example:

```text
INFO      Upcoming deadline
WARNING   Budget > 90%
CRITICAL  Database backup unavailable
```

---

# 51. KPI Principles

KPIs SHALL be:

- understandable;
- actionable;
- derived from authoritative data;
- clearly defined.

The application SHALL avoid KPI inflation.

---

# 52. Core KPIs

Recommended:

```text
ACTIVE MEMBERS
MEMBERSHIP CHANGE
INCOME YTD
EXPENSE YTD
RESULT YTD
BANK BALANCE
OPEN FEES
PROJECT BUDGET
PROJECT ACTUAL
FUNDING GAP
APPROVED GRANTS
UPCOMING DEADLINES
```

---

# 53. KPI Definitions

Every KPI SHOULD have a defined calculation.

Example:

```text
Active Members
= count of members with active membership status
```

```text
Funding Gap
= Project Budget - Confirmed Funding
```

---

# 54. KPI Source Traceability

A user SHOULD be able to open the underlying report from a KPI.

Example:

```text
Outstanding Fees: DKK 12,500
          ↓
Open Fee Report
```

---

# 55. Dashboard Navigation

Recommended:

```text
Dashboard
 ├── Finance
 ├── Members
 ├── Projects
 ├── Grants
 ├── Documents
 └── Deadlines
```

---

# 56. Report Service

`ReportService` SHALL coordinate report generation.

Recommended methods:

```text
get_trial_balance()
get_general_ledger()
get_income_statement()
get_balance_sheet()
get_budget_actual()
get_member_report()
get_fee_report()
get_project_report()
get_grant_report()
get_document_report()
get_management_summary()
```

---

# 57. Dashboard Service

`DashboardService` SHALL calculate dashboard-level summaries.

Recommended:

```text
get_financial_summary()
get_membership_summary()
get_project_summary()
get_grant_summary()
get_document_summary()
get_deadline_summary()
get_system_health()
```

---

# 58. Reporting Repository

Reporting queries MAY use specialised read-only repository methods.

Example:

```text
FinancialReportRepository
MembershipReportRepository
ProjectReportRepository
GrantReportRepository
DocumentReportRepository
```

These repositories SHALL not modify business data.

---

# 59. Read-Only Principle

The reporting layer SHALL be read-only with respect to operational data.

A report generation action SHALL not:

- post accounting;
- change members;
- change projects;
- approve grants;
- alter documents.

---

# 60. Report Parameters

Reports SHALL use explicit parameters.

Examples:

```text
financial_year
from_date
to_date
account
project
member_status
grant_status
```

Parameters SHOULD be saved only when useful.

---

# 61. Report Presets

The application MAY provide presets:

```text
Current Year
Last Month
Current Quarter
Year to Date
Previous Year
```

---

# 62. Custom Date Range

All relevant reports SHOULD support custom date ranges.

The application SHALL validate:

```text
from_date <= to_date
```

---

# 63. Report Reproducibility

Given the same:

```text
source data
report parameters
```

the report SHOULD produce the same result.

---

# 64. Report Timestamp

Generated reports SHOULD contain:

```text
Generated at
Generated by
Parameters
```

This improves auditability.

---

# 65. Export Formats

Minimum useful exports:

```text
XLSX
PDF
CSV
```

The format SHALL depend on report type.

---

# 66. Excel Export

Excel reports SHOULD contain:

- clear headers;
- totals;
- filters where useful;
- report date;
- source period.

The export SHALL not modify the database.

---

# 67. PDF Export

PDF reports SHOULD be suitable for:

- board meetings;
- annual reports;
- grant reporting;
- financial review.

---

# 68. CSV Export

CSV is useful for:

- member lists;
- accounting data;
- project transactions;
- grant registers.

CSV exports SHALL use a predictable encoding.

---

# 69. Print Support

Reports MAY be printed through the operating system print workflow.

Printing SHALL not alter data.

---

# 70. Board Report Generation

The system SHOULD provide:

```text
Generate Board Report
```

with a selectable reporting period.

The report SHALL combine the relevant modules.

---

# 71. Annual Report Support

MFM v1.0 SHOULD support preparation of information for an annual report.

Potential sections:

```text
Membership
Activities
Projects
Financial result
Assets
Funding
Grants
```

The application SHALL not attempt to automatically write a legally complete annual report.

---

# 72. Financial Year Comparison

Financial reports SHOULD support:

```text
Current Year
Previous Year
Variance
```

Example:

```text
Income 2027
Income 2026
Change
```

---

# 73. Membership Year Comparison

Membership reports MAY compare:

```text
Active members 2027
Active members 2026
Change
```

---

# 74. Project Portfolio Comparison

The dashboard MAY compare project totals across periods.

The report SHALL clearly identify whether projects are comparable.

---

# 75. Grant Pipeline

The grant dashboard MAY show:

```text
Preparing
Submitted
Under Review
Approved
Rejected
```

This is a workflow overview, not a financial forecast.

---

# 76. Funding Pipeline

The system MAY distinguish:

```text
Confirmed
Pending
Potential
```

Only confirmed funding SHALL affect official funding figures.

---

# 77. Financial Forecast

MFM v1.0 MAY provide simple forecast information.

Example:

```text
Actual YTD
+
Known committed income
-
Known committed expenses
=
Indicative Forecast
```

Forecast values SHALL be labelled clearly.

They SHALL not appear as actual accounting values.

---

# 78. Dashboard Colour Use

Colour MAY be used sparingly to indicate:

```text
normal
warning
critical
```

The system SHALL not rely solely on colour for meaning.

---

# 79. Accessibility

Dashboard and reports SHOULD provide:

- readable fonts;
- sufficient contrast;
- clear labels;
- keyboard navigation;
- non-colour indicators.

---

# 80. User Role Filtering

The dashboard SHALL respect permissions.

Example:

```text
READ_ONLY
```

may see:

```text
reports
```

but not:

```text
financial configuration
```

---

# 81. Sensitive Information

Reports containing personal or financial information SHALL require appropriate permission.

Export permissions SHOULD be separate from view permissions where practical.

---

# 82. Audit of Exports

Important exports SHOULD create an audit event.

Example:

```text
REPORT_EXPORTED
```

with:

```text
user
report
format
timestamp
parameters
```

---

# 83. Report Security

Generated files SHALL be written to a controlled export directory.

Temporary files SHOULD be removed after use.

---

# 84. Dashboard Performance

The dashboard SHOULD load quickly for expected association data volumes.

Queries SHALL use appropriate indexes.

Expensive reports SHOULD be generated on demand rather than on every screen refresh.

---

# 85. Query Separation

Dashboard queries SHALL be separate from transactional write logic.

Example:

```text
DashboardService
    ↓
Read-only query
```

not:

```text
Dashboard
    ↓
Business transaction
```

---

# 86. Reporting Data Consistency

If multiple source modules change during a report operation, the report SHOULD use a consistent database snapshot where practical.

This is particularly important for financial reports.

---

# 87. Financial Report Locking

Official financial reports SHOULD be generated from posted transactions only.

Draft transactions SHALL be excluded unless the report is explicitly labelled:

```text
INCLUDING DRAFTS
```

---

# 88. Management Dashboard Refresh

The user SHOULD be able to:

```text
Refresh
```

The interface SHOULD display:

```text
Last refreshed
```

---

# 89. System Health Dashboard

The management dashboard MAY include technical health:

```text
Database
Backup
Documents
Schema
Storage
```

Example:

```text
Database: OK
Last Backup: Today
Documents: 0 missing
Schema: Current
Storage: OK
```

---

# 90. Backup Warning

If the last successful backup exceeds the configured threshold:

```text
WARNING
```

The dashboard SHOULD surface this prominently.

---

# 91. Database Integrity Warning

If database integrity fails:

```text
CRITICAL
```

The dashboard SHALL not hide the problem.

---

# 92. Document Integrity Warning

If document integrity fails:

```text
WARNING
```

The dashboard SHOULD provide a link to the integrity report.

---

# 93. Report Error Handling

User-facing messages SHOULD be understandable.

Examples:

```text
"The report could not be generated."
"No accounting data exists for the selected period."
"You do not have permission to view this report."
"The selected date range is invalid."
```

Technical details SHALL be logged separately.

---

# 94. Negative Testing

```text
Invalid date range → BLOCK
Unauthorised report → BLOCK
Unauthorised export → BLOCK
Draft voucher included in official report → TEST FAILURE
Unbalanced trial balance hidden → TEST FAILURE
Wrong financial period → TEST FAILURE
Project actual differs from ledger → TEST FAILURE
Funding gap incorrect → TEST FAILURE
Member count inconsistent → TEST FAILURE
Missing document not reported → TEST FAILURE
Database unavailable → CONTROLLED ERROR
Report export failure → NO DATA MODIFICATION
```

---

# 95. Acceptance Test — Trial Balance

Given balanced posted vouchers.

Expected:

```text
Total debit = total credit
Status = BALANCED
```

---

# 96. Acceptance Test — Income Statement

Given:

```text
Income = 100,000
Expense = 70,000
```

Expected:

```text
Result = 30,000
```

---

# 97. Acceptance Test — Project Report

Given:

```text
Budget = 200,000
Actual = 150,000
```

Expected:

```text
Variance = 50,000
Utilisation = 75%
```

---

# 98. Acceptance Test — Membership

Given:

```text
Active = 120
New = 15
Left = 5
```

Expected:

```text
Closing = 130
```

assuming the opening population is 120 before the movement.

---

# 99. Acceptance Test — Grant Funding

Given:

```text
Requested = 100,000
Approved = 75,000
Received = 50,000
```

Expected:

```text
Approved outstanding = 25,000
```

---

# 100. Acceptance Test — Dashboard Traceability

Click:

```text
Outstanding Fees
```

Expected:

```text
Fee Report
```

Click a fee.

Expected:

```text
Member / Payment details
```

Financial transaction link SHALL open the relevant accounting record where available.

---

# 101. Acceptance Test — Export

Generate XLSX report.

Expected:

```text
File created
Correct report data
Correct period
No database changes
Audit event if configured
```

---

# 102. Acceptance Test — Permissions

Read-only user attempts financial configuration.

Expected:

```text
BLOCK
```

Read-only user opens an authorised report.

Expected:

```text
ALLOW
```

---

# 103. Acceptance Test — Backup Warning

Set backup threshold exceeded.

Expected:

```text
Dashboard warning
```

---

# 104. Management Exception Logic

The dashboard SHOULD calculate exceptions from defined rules.

Example:

```text
If project actual > budget
    OVER_BUDGET

If grant deadline < today
    OVERDUE

If funding gap > 0
    FUNDING_GAP

If backup age > threshold
    BACKUP_WARNING
```

Rules SHALL be configurable where appropriate.

---

# 105. No Autonomous Decisions

The reporting layer SHALL never automatically:

```text
close projects
approve budgets
approve grants
post accounting
change membership
delete documents
```

It may identify conditions and recommend actions.

---

# 106. AI Assistance

Future AI functionality MAY assist with:

```text
summarisation
anomaly detection
trend explanation
report drafting
question answering
```

AI-generated information SHALL remain clearly distinguishable from authoritative accounting data.

---

# 107. AI Reporting Rule

AI SHALL NOT be treated as the financial source.

Correct hierarchy:

```text
AUTHORITATIVE DATA
       ↓
REPORT
       ↓
OPTIONAL AI EXPLANATION
```

Not:

```text
AI
 ↓
FINANCIAL TRUTH
```

---

# 108. Management Summary Generation

An optional summary service MAY produce:

```text
What changed?
What is unusual?
What needs attention?
What deadlines are approaching?
```

The underlying figures SHALL remain linked to reports.

---

# 109. Dashboard Configuration

The association MAY configure:

```text
visible widgets
warning thresholds
default period
default dashboard
```

Configuration SHALL not change accounting rules.

---

# 110. Board Dashboard

A dedicated board view MAY show only:

```text
Financial Result
Bank
Membership
Projects
Funding
Key Warnings
Deadlines
```

This avoids exposing unnecessary operational details.

---

# 111. Treasurer Dashboard

Treasurer view MAY additionally show:

```text
Unposted Vouchers
Bank Reconciliation
Outstanding Fees
Budget Variance
Grant Payments
```

---

# 112. Administrator Dashboard

Administrator view MAY additionally show:

```text
Database
Backup
Documents
Users
Schema
System Health
```

---

# 113. Read-Only Dashboard

Read-only users MAY receive:

```text
Approved Reports
Basic Dashboard
Project Overview
Membership Overview
```

No modification controls SHALL be presented.

---

# 114. Report Templates

Report layouts SHOULD be centralised.

Example:

```text
ReportHeader
ReportParameters
ReportBody
ReportTotals
ReportFooter
```

This ensures consistent presentation.

---

# 115. Report Numbering

Generated official reports MAY receive an identifier.

Example:

```text
RPT-2027-0001
```

This is optional for v1.0 but useful for formal board documentation.

---

# 116. Report Archive

Important generated reports MAY be archived as documents.

Example:

```text
Annual Accounts 2027
Board Report March 2027
Project Final Report
```

The report file SHALL be linked to its originating parameters.

---

# 117. Report Metadata

Archived reports SHOULD record:

```text
report_type
period
generated_by
generated_at
parameters
file
```

---

# 118. Annual Accounts Support

The reporting layer SHALL provide the underlying figures required for annual financial reporting.

It SHALL not claim that automatically generated reports are a substitute for professional accounting review where such review is required.

---

# 119. Audit Support

The report layer SHALL make it possible to move from summary to detail.

Example:

```text
Annual Result
 ↓
Income Statement
 ↓
Account
 ↓
Ledger
 ↓
Voucher
 ↓
Voucher Line
```

This drill-down capability is a core MFM feature.

---

# 120. Drill-Down Rules

Every financial summary SHOULD expose a drill-down path where practical.

No summary figure should be impossible to explain from underlying records.

---

# 121. Management Information Hierarchy

```text
SUMMARY
  ↓
CATEGORY
  ↓
ACCOUNT / PROJECT
  ↓
TRANSACTION
  ↓
SOURCE DOCUMENT
```

This hierarchy provides transparency.

---

# 122. Reporting and Governance

Reports support governance by making information visible.

They do not replace:

- board decisions;
- financial approval;
- association policy;
- legal obligations.

---

# 123. Reporting and Human Authority

Correct relationship:

```text
DATA
 ↓
REPORT
 ↓
HUMAN REVIEW
 ↓
DECISION
```

Not:

```text
DATA
 ↓
AUTOMATIC DECISION
```

---

# 124. Development Sequence

```text
1. Report models
2. Report service
3. Financial reports
4. Membership reports
5. Project reports
6. Grant reports
7. Document reports
8. Dashboard service
9. Main dashboard
10. Board dashboard
11. Export engine
12. PDF templates
13. Excel templates
14. Drill-down
15. Tests
```

---

# 125. Suggested Files

```text
src/
├── reports/
│   ├── report_service.py
│   ├── financial_reports.py
│   ├── membership_reports.py
│   ├── project_reports.py
│   ├── grant_reports.py
│   └── document_reports.py
│
├── services/
│   └── dashboard_service.py
│
└── gui/
    ├── dashboard.py
    ├── reports.py
    └── board_dashboard.py
```

Existing modules MAY be reused and refactored.

---

# 126. Definition of Done

Reporting & Management Dashboard v1.0 is complete when:

- dashboard loads;
- financial summary works;
- membership summary works;
- project summary works;
- grant summary works;
- document summary works;
- deadlines work;
- trial balance works;
- general ledger works;
- income statement works;
- balance sheet works;
- budget versus actual works;
- project reports work;
- grant reports work;
- membership reports work;
- document reports work;
- exports work;
- permissions work;
- drill-down works;
- audit of important exports works;
- negative tests pass.

---

# 127. Relationship to Previous Modules

```text
Architecture Baseline
       ↓
Database Foundation
       ↓
Accounting Core
       ↓
Membership
       ↓
Projects & Budget
       ↓
Documents & Grants
       ↓
Reporting & Dashboard
```

The reporting layer consumes these modules.

It does not replace them.

---

# 128. Practical Association Focus

The reporting module is deliberately designed to answer the questions a small association actually needs answered:

```text
How are we doing financially?
How many members do we have?
Which projects are active?
Are projects within budget?
How much funding have we secured?
What grants are pending?
What deadlines are coming?
Is anything wrong that needs attention?
```

The system SHALL not bury these answers under unnecessary enterprise complexity.

---

# 129. Final Governing Principle

> **MFM reporting exists to make the association understandable to the people responsible for running it.**

The architecture SHALL therefore follow:

```text
AUTHORITATIVE DATA
        ↓
CLEAR REPORTING
        ↓
EXCEPTION VISIBILITY
        ↓
HUMAN REVIEW
        ↓
DECISION
```

# END OF MFM v1.0 REPORTING & MANAGEMENT DASHBOARD

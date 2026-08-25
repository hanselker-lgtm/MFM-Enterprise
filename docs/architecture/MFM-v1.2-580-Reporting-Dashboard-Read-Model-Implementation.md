# MFM v1.2-580 – Reporting, Dashboard & Read-Model Implementation

Version: 1.2

Document ID: MFM-v1.2-580

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the implementation baseline for Reporting, Dashboard and Read-Model capabilities in MaritimForeningsManager (MFM) v1.2.

It follows:

- MFM v1.2-500 – Architecture Consolidation & Implementation Readiness
- MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability
- MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow
- MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution
- MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution
- MFM v1.2-550 – Core Services & Domain Logic Implementation
- MFM v1.2-560 – Repository, Persistence Services & Data Access Implementation
- MFM v1.2-570 – GUI, Presentation Layer & User Workflow Implementation

The purpose is to define how MFM converts authoritative domain data into reports, dashboards and controlled read models without creating parallel business truth.

The document establishes:

- Reporting Architecture
- Dashboard Architecture
- Read Models
- Data Provenance
- Accounting Reporting
- Membership Reporting
- Project Reporting
- Grant Reporting
- Document Reporting
- Operational Reporting
- Filters
- Aggregation
- Period Logic
- Caching
- Export
- Permissions
- Refresh
- Testing
- Performance
- Reconciliation
- Traceability

---

# 2. Scope

This document covers:

- Standard Reports
- Management Reports
- Operational Dashboards
- Financial Dashboards
- Membership Dashboards
- Project Dashboards
- Grant Dashboards
- Document Dashboards
- Read-Only Query Models
- Report Exports
- Report Filters
- Derived Metrics
- Cached Read Models

It does not create a new authoritative business-data store.

---

# 3. Core Reporting Principle

Reporting is a read-oriented capability.

The basic flow is:

```text
Authoritative Domain

↓

Query Service

↓

Read Model / Report Model

↓

Report / Dashboard

↓

Export / Display
```

Reports must not modify authoritative business state.

---

# 4. Authoritative Data Rule

Each report must have a clearly identified source.

Examples:

```text
Financial Actuals
→ Accounting Core

Members
→ Membership

Projects
→ Project Domain

Grant Applications
→ Grants

Documents
→ Document Domain
```

---

# 5. Financial Authority

The following rule is mandatory:

> **Accounting Core is the sole authoritative financial ledger.**

Any report showing actual financial transactions, balances, revenue, expenses, assets, liabilities or cash positions must derive those values from Accounting Core.

---

# 6. Report Data Provenance

Important report values should have traceable provenance.

A report definition should identify:

```text
Metric

Source Domain

Source Query

Period

Filters

Calculation
```

---

# 7. Read Model Principle

A read model is a representation optimized for reading.

It may contain:

- Aggregated Values
- Denormalized Fields
- Calculated Metrics
- Search-Friendly Structures

It must remain derived from authoritative sources.

---

# 8. Read Model Authority

A read model must never become the authoritative owner of a business fact merely because it is faster to query.

Example:

```text
Dashboard Balance

→ Derived

Accounting Ledger

→ Authoritative
```

---

# 9. Read Model Refresh

A read model may be:

- Calculated On Demand
- Refreshed Periodically
- Refreshed After Relevant Events
- Rebuilt Completely

The selected approach depends on performance requirements.

---

# 10. Initial MFM Strategy

For the current scale of MFM, prefer simple on-demand queries unless performance evidence justifies persistent read models.

Do not introduce a complex analytics platform prematurely.

---

# 11. Reporting Service

The Reporting Service coordinates report generation.

Responsibilities:

- Select Report
- Validate Permissions
- Apply Filters
- Query Authoritative Sources
- Calculate Derived Values
- Format Results
- Export
- Provide Provenance

---

# 12. Dashboard Service

The Dashboard Service provides concise read-oriented summaries.

Responsibilities:

- Load Dashboard
- Retrieve Metrics
- Apply User Scope
- Refresh Data
- Provide Status
- Indicate Data Time

---

# 13. Query Service

Query services expose controlled read operations.

Examples:

```text
get_member_summary()

get_project_actuals()

get_grant_deadlines()

get_account_balance()

get_document_summary()
```

---

# 14. Query Service Rule

Query services must not silently modify data.

A query should remain side-effect free.

---

# 15. Report Definition

A report definition should specify:

```text
Report ID

Name

Purpose

Source

Filters

Columns

Calculations

Permissions

Export Options
```

---

# 16. Report Categories

MFM may organize reports into:

```text
Financial

Membership

Projects

Grants

Documents

Operations

Administration
```

---

# 17. Financial Reports

Possible reports include:

- Trial Balance
- Profit and Loss
- Balance Sheet where implemented
- General Ledger
- Account Activity
- Cash / Bank Overview
- Project Financial Overview
- Grant Financial Overview

The exact report set follows the Accounting Core implementation.

---

# 18. Trial Balance

A trial balance should be generated from Accounting Core.

At minimum it should show:

```text
Account

Debit

Credit

Balance
```

The report must preserve accounting correctness.

---

# 19. Trial Balance Validation

The report should support validation that:

```text
Total Debits

=

Total Credits
```

where applicable to the selected reporting scope.

---

# 20. General Ledger Report

The general ledger report should show authoritative ledger activity.

Typical fields:

```text
Date

Voucher

Account

Description

Debit

Credit

Reference
```

---

# 21. Account Activity Report

The account activity report may provide:

```text
Opening Balance

Transactions

Closing Balance
```

The calculation must use Accounting Core data.

---

# 22. Financial Period

Financial reports must explicitly identify:

```text
From Date

To Date
```

or an equivalent accounting period.

---

# 23. Closed Period Reporting

Closed periods remain reportable.

Closing a period restricts posting; it must not make historical reporting unavailable.

---

# 24. Financial Comparison

Reports may compare:

```text
Current Period

Previous Period

Budget

Actual

Forecast
```

The source and semantics of each value must remain clear.

---

# 25. Project Financial Reporting

Project reports may combine:

```text
Project Budget

+

Accounting Actuals

+

Derived Variance
```

The budget remains project planning data.

Actuals remain Accounting Core data.

---

# 26. Grant Financial Reporting

Grant reports may combine:

```text
Grant Award

+

Grant Budget / Plan

+

Accounting Actuals
```

Actuals must originate from Accounting Core.

---

# 27. Membership Reports

Possible membership reports:

- Active Members
- Membership by Category
- Membership Status
- New Members
- Inactive Members
- Membership History
- Contact / Administration Lists

Sensitive information must be permission-controlled.

---

# 28. Membership Summary

A dashboard may display:

```text
Total Members

Active Members

Inactive Members

New This Period
```

---

# 29. Membership Trend

Where historical data is available, show:

```text
Period

Member Count
```

The report should identify the measurement date or period.

---

# 30. Project Reports

Possible reports:

- Project Status
- Project Portfolio
- Tasks
- Milestones
- Budget vs Actual
- Project Timeline
- Project Documents

---

# 31. Project Portfolio

A portfolio report may show:

```text
Project

Status

Responsible

Start

End

Budget

Actual

Variance
```

Actual values must be sourced from Accounting Core.

---

# 32. Project Task Report

Possible columns:

```text
Project

Task

Responsible

Due Date

Status

Priority
```

---

# 33. Project Status Dashboard

The dashboard may summarize:

```text
Planned

Active

Completed

Overdue
```

---

# 34. Grant Reports

Possible reports:

- Grant Pipeline
- Application Status
- Upcoming Deadlines
- Awards
- Reporting Requirements
- Grant Portfolio

---

# 35. Grant Pipeline

A grant pipeline may show:

```text
Grant

Provider

Stage

Deadline

Requested

Awarded
```

---

# 36. Grant Deadline Dashboard

The dashboard should emphasize:

```text
Due Soon

Upcoming

Overdue
```

The exact threshold should be configurable or defined by the grant domain.

---

# 37. Grant Award Summary

The report may summarize:

```text
Applications

Awards

Requested Amount

Awarded Amount
```

Financial actuals remain separate and authoritative in Accounting Core.

---

# 38. Document Reports

Possible reports:

- Document Inventory
- Documents by Category
- Documents by Project
- Documents by Grant
- Version Status
- Retention / Hold Status
- Missing File References

---

# 39. Document Integrity Report

A document integrity report may identify:

```text
Metadata Without File

File Without Metadata

Checksum Mismatch where applicable

Invalid Reference
```

---

# 40. Operational Reports

Operational reports may include:

- Open Tasks
- Notifications
- Failed Jobs
- Backup Status
- Migration Status
- Maintenance Status

---

# 41. Administration Reports

Administrative reports may include:

- User Access
- Roles
- Privileged Users
- Security Events
- Configuration Changes

Access must be restricted.

---

# 42. Dashboard Design

Dashboards should answer practical questions.

Examples:

```text
What needs attention?

What is overdue?

What changed?

How are finances performing?

Which grants need action?
```

---

# 43. Dashboard Sections

A practical MFM dashboard may contain:

```text
Attention

Finance

Membership

Projects

Grants

Documents

System
```

---

# 44. Attention Section

Possible items:

```text
Overdue Tasks

Grant Deadlines

Failed Backups

Failed Notifications

Pending Administrative Actions
```

---

# 45. Finance Dashboard

Possible metrics:

```text
Cash / Bank Position

Income

Expenses

Net Result

Budget Variance

Open Accounting Items
```

Every actual financial metric must have Accounting Core provenance.

---

# 46. Finance Dashboard Date

Financial dashboard values should indicate their effective date.

Example:

```text
Balance as of:
17 August 2026
```

This prevents confusion between live and cached values.

---

# 47. Membership Dashboard

Possible:

```text
Active Members

New Members

Inactive Members

Membership Distribution
```

---

# 48. Project Dashboard

Possible:

```text
Active Projects

Overdue Tasks

Upcoming Milestones

Budget Variances
```

---

# 49. Grant Dashboard

Possible:

```text
Open Applications

Deadlines

Awards

Reporting Due
```

---

# 50. Document Dashboard

Possible:

```text
Documents Added

Documents Requiring Review

Retention Holds

Missing Files
```

---

# 51. System Dashboard

Administrative users may see:

```text
Database Status

Backup Status

Migration Status

Notification Failures

Security Events
```

---

# 52. Metric Definition

Every important metric should have a clear definition.

Example:

```text
Active Members

Definition:
Members whose current membership status is Active.
```

---

# 53. Metric Source

Every metric should have a source.

Example:

```text
Metric:
Active Members

Source:
MembershipRepository / MembershipQueryService
```

---

# 54. Metric Calculation

Calculated metrics should document the calculation.

Example:

```text
Budget Variance

= Budget - Actual
```

The sign convention must be consistent across reports.

---

# 55. Financial Metric Calculation

Financial calculations must use Accounting Core data.

Do not calculate actual financial totals from unrelated operational tables.

---

# 56. Metric Time Basis

Metrics may be:

```text
Point in Time

Period Total

Rolling Period

Cumulative
```

The report must make the time basis clear.

---

# 57. Point-in-Time Metric

Example:

```text
Active Members
as of 17 August 2026
```

---

# 58. Period Metric

Example:

```text
Expenses
01 August 2026 – 17 August 2026
```

---

# 59. Cumulative Metric

Example:

```text
Grant Applications
Year to Date
```

The report must state the period.

---

# 60. Filters

Reports should provide appropriate filters.

Common filters:

```text
Date

Status

Category

Project

Grant

Account

Member
```

---

# 61. Filter Validation

Invalid filters should be rejected.

Examples:

```text
From Date > To Date

Invalid Project

Unauthorized Account Scope
```

---

# 62. Filter Persistence

The UI may remember recent filters.

However, saved filters must not become hidden business state.

---

# 63. Report Sorting

Users may sort results where appropriate.

Sorting must remain controlled and should not expose arbitrary SQL behavior.

---

# 64. Report Pagination

Large reports should support:

- Pagination
- Controlled Loading
- Export without GUI limitations

---

# 65. Report Export

Exports may include:

```text
PDF

CSV

Excel
```

according to the existing MFM capabilities.

---

# 66. Export Permissions

Export may expose more data than normal viewing.

Therefore export must be separately considered in authorization.

---

# 67. Export Audit

Sensitive reports may record:

```text
User

Report

Filter Scope

Time

Format
```

---

# 68. Report Formatting

Reports should use consistent:

- Titles
- Dates
- Currency
- Number Formats
- Page Headers
- Page Footers
- Organization Identity

---

# 69. Report Metadata

Generated reports should identify:

```text
Report Name

Generated At

Reporting Period

Filters

Source
```

---

# 70. Financial Report Metadata

Financial reports should additionally identify:

```text
Accounting Source:
Accounting Core

Period:
...

Generated:
...
```

---

# 71. Reconciliation

Reports containing derived financial information should support reconciliation to Accounting Core.

Example:

```text
Project Actuals

=

Accounting Core Transactions
```

for the defined project scope.

---

# 72. Report Reconciliation Test

A financial report should be testable against an authoritative ledger query.

---

# 73. Dashboard Reconciliation

Dashboard financial metrics should be reconciled to the same Accounting Core query services used by detailed reports where appropriate.

---

# 74. Read Model Refresh

A persistent read model should have:

```text
Last Refresh

Source Version / Timestamp

Refresh Status
```

---

# 75. Stale Data Indicator

If a dashboard uses cached data, it should indicate when appropriate:

```text
Updated:
09:15
```

This is particularly important for operational users.

---

# 76. Cache Invalidation

A read model cache may be invalidated after relevant changes.

Example:

```text
Voucher Posted

↓

Invalidate Financial Dashboard Cache
```

---

# 77. Event-Driven Refresh

Where domain events are implemented:

```text
VoucherPosted

↓

Dashboard Refresh Request
```

This may improve responsiveness without making the dashboard authoritative.

---

# 78. On-Demand Refresh

For the current MFM scale, manual or on-demand refresh is acceptable where performance is sufficient.

---

# 79. Read Model Storage

If persistent read models are introduced, they should have clear ownership and rebuild procedures.

---

# 80. Rebuild Principle

A read model should be reconstructible from authoritative data where practical.

```text
Authoritative Data

↓

Rebuild

↓

Read Model
```

---

# 81. Read Model Failure

If a read model becomes corrupted:

```text
Discard / Rebuild

↓

Validate

↓

Resume
```

Do not modify authoritative data to repair a derived read model.

---

# 82. Reporting Error Handling

If a report fails:

```text
Report generation failed.

No business data was changed.
```

Technical details should be logged.

---

# 83. Missing Source Data

If source data is incomplete, the report should indicate the limitation where meaningful.

Do not silently substitute invented values.

---

# 84. Report Null Handling

Reports should distinguish:

```text
0

No Data

Not Applicable

Unknown
```

These are not always equivalent.

---

# 85. Financial Zero vs Missing

For example:

```text
Expenses = 0
```

is different from:

```text
No accounting data available
```

---

# 86. Report Security

Reports must respect:

- User Role
- Permission
- Organization Scope
- Confidentiality
- Export Permission

---

# 87. Row-Level Reporting Security

Where record-level access is required, filters must be applied before data leaves the authorized query boundary.

---

# 88. Sensitive Reports

Sensitive reports may include:

- Member Contact Lists
- Financial Reports
- Security Reports
- User Access Reports
- Confidential Grant Information

These require appropriate permissions.

---

# 89. Dashboard Security

Dashboards must not expose sensitive metrics merely because the user can access the main application.

---

# 90. Reporting and Audit

Report generation is normally read-only.

However, generation or export of sensitive reports may be audited.

---

# 91. Report Scheduling

Future scheduled reporting may be supported.

Examples:

```text
Monthly Financial Report

Annual Membership Report

Grant Deadline Summary
```

Scheduled reports must use the same authoritative query services.

---

# 92. Scheduled Report Security

Scheduled reports must execute under a defined authorized context.

They must not use a personal user's unrestricted credentials without controlled design.

---

# 93. Report Delivery

Where reports are delivered by email:

```text
Generate

↓

Validate

↓

Deliver

↓

Record Status
```

Failed delivery must not alter source data.

---

# 94. Report Archive

Reports may be archived where organizational policy requires historical evidence.

Archived reports should identify:

- Generation Date
- Reporting Period
- Source
- Version where relevant

---

# 95. Report Versioning

If report definitions change materially, the system should be able to distinguish versions where historical reproducibility matters.

---

# 96. Reproducibility

Important historical reports should be reproducible where practical.

This may require retaining:

- Report Definition
- Filters
- Source Period
- Generation Date
- Data Snapshot Reference where required

---

# 97. Accounting Reproducibility

Financial reports must be based on immutable posted accounting history and defined reporting rules.

---

# 98. Dashboard Snapshot

A dashboard generally represents current or recent state.

It should not be treated as a historical financial record.

---

# 99. Dashboard vs Report

Dashboard:

```text
Fast

Current

Action-Oriented
```

Report:

```text
Detailed

Filtered

Exportable

Historical
```

---

# 100. Read Model vs Report

Read Model:

```text
Reusable Query Representation
```

Report:

```text
User-Facing Output
```

They are related but not identical.

---

# 101. Query Reuse

The same authoritative query service may support:

```text
Dashboard

Report

Export
```

This reduces duplicated calculation logic.

---

# 102. Calculation Reuse

Important calculations should exist in one controlled place.

Avoid:

```text
Dashboard calculates one way

Report calculates another way

Export calculates a third way
```

---

# 103. Financial Calculation Reuse

Financial calculations should use Accounting Core query services and shared definitions.

---

# 104. Report Testing

Reports should be tested with known datasets.

Tests should verify:

- Filters
- Totals
- Sorting
- Dates
- Permissions
- Export
- Provenance

---

# 105. Financial Report Tests

Minimum:

```text
Trial Balance

General Ledger

Account Activity

Period Filter

Debit / Credit

Project Actuals

Grant Actuals
```

---

# 106. Membership Report Tests

Minimum:

```text
Active Count

Status Filter

Category

Period

History
```

---

# 107. Project Report Tests

Minimum:

```text
Portfolio

Status

Tasks

Budget

Actual

Variance
```

---

# 108. Grant Report Tests

Minimum:

```text
Pipeline

Deadline

Application Status

Award

Reporting
```

---

# 109. Document Report Tests

Minimum:

```text
Inventory

Category

Relationship

Retention

Missing Files
```

---

# 110. Dashboard Tests

Dashboard tests should verify:

```text
Metric Source

Metric Calculation

Authorization

Refresh

Stale State

Error State
```

---

# 111. Read Model Tests

Where persistent read models exist:

```text
Build

Refresh

Rebuild

Corruption Recovery

Source Consistency
```

---

# 112. Reporting Performance

Reports should remain responsive for expected data volumes.

Potential optimization:

- Query Projection
- Indexes
- Pagination
- Caching
- Background Generation

Use only where evidence supports the need.

---

# 113. Large Export

Large exports should use streaming or controlled batching where practical.

Avoid loading an unnecessarily large dataset into memory.

---

# 114. Dashboard Performance

Dashboards should avoid loading every module's complete dataset.

Use targeted queries.

---

# 115. Query Performance

A dashboard should prefer:

```text
COUNT

SUM

Targeted Aggregate

```

over loading thousands of records merely to calculate a count.

---

# 116. Financial Dashboard Query

Example:

```text
SELECT / Query

→ authoritative Accounting Core aggregate
```

rather than:

```text
Load all ledger rows

→ calculate in GUI
```

---

# 117. Reporting Architecture

The recommended flow is:

```text
Report Screen

↓

ReportingService

↓

Domain Query Service

↓

Repository

↓

Authoritative Data

↓

Report Model

↓

Presentation / Export
```

---

# 118. Dashboard Architecture

```text
Dashboard Screen

↓

DashboardService

↓

Metric Query Services

↓

Authoritative Domains

↓

Dashboard Model

↓

Presentation
```

---

# 119. Read Model Architecture

Where needed:

```text
Authoritative Domain

↓

Event / Refresh Trigger

↓

Read Model Builder

↓

Read Store

↓

Query Service

↓

Dashboard / Report
```

---

# 120. Read Model Security

Read models must inherit appropriate access restrictions.

A denormalized read model must not accidentally expose fields that the source domain would restrict.

---

# 121. Read Model Retention

Derived read models generally do not require long-term retention unless they are explicitly used as historical snapshots.

---

# 122. Reporting Data Retention

Generated reports may require retention according to organizational policy.

The report archive must remain distinct from live read models.

---

# 123. Report Deletion

Deleting a generated report must not delete the source business data.

---

# 124. Dashboard Failure Isolation

If one dashboard metric fails:

```text
Metric Failure

↓

Show Unavailable

↓

Other Metrics Continue
```

where practical.

A single optional metric should not necessarily prevent the whole dashboard from loading.

---

# 125. Critical Dashboard Failure

If a critical financial metric cannot be loaded, clearly indicate:

```text
Financial data unavailable
```

Do not display stale or guessed values as current.

---

# 126. Stale Data Policy

If cached data is older than the defined acceptable interval:

```text
Stale

```

The dashboard should communicate the state where it could affect decisions.

---

# 127. Data Timestamp

Important dashboards may show:

```text
Data as of:
17 August 2026 09:15
```

---

# 128. Report Filter Security

Filters must not allow a user to bypass access restrictions.

Example:

```text
User selects another Organization

↓

Authorization Check

↓

Unauthorized Scope Rejected
```

---

# 129. Report Injection Security

Report generation must use parameterized queries and controlled templates.

---

# 130. Export File Security

Generated exports should be stored in controlled locations.

Temporary exports should not remain indefinitely.

---

# 131. Export Naming

Use safe names such as:

```text
Financial-Report-2026-08-17.pdf
```

Do not use raw user input as unrestricted file paths.

---

# 132. Report Job

Long report generation may run as a background job:

```text
Request

↓

Job Created

↓

Generate

↓

Store Result

↓

Notify User
```

---

# 133. Report Job Failure

A failed report job should show:

```text
Report generation failed.

Reference:
JOB-12345
```

Technical detail belongs in logs.

---

# 134. Report Job Retry

Retries should be used only when the failure is transient and the report generation is safe to repeat.

---

# 135. Reporting Configuration

Configuration may include:

- Default Date Range
- Dashboard Refresh Interval
- Export Formats
- Report Retention

These settings must not change business accounting rules.

---

# 136. Financial Reporting Configuration

Report configuration may affect presentation and filters.

It must not alter the underlying accounting ledger.

---

# 137. Dashboard Configuration

Administrators may configure which widgets are displayed where practical.

---

# 138. User Dashboard Preferences

If supported, users may configure:

- Widget Order
- Visible Widgets
- Filter Defaults

Preferences are user-interface state, not business truth.

---

# 139. Reporting Accessibility

Reports and dashboards should provide:

- Clear Labels
- Accessible Tables
- Textual Status
- Keyboard Access
- Non-Color-Only Indicators

---

# 140. Dashboard Accessibility

Important metrics should have meaningful text labels.

Icons alone are insufficient.

---

# 141. Report Definition of Ready

A report is Ready when:

- Purpose Is Defined
- Source Is Defined
- Filters Are Defined
- Calculations Are Defined
- Permissions Are Defined
- Export Requirement Is Defined
- Test Data Exists

---

# 142. Report Definition of Done

A report is Done when:

- Query Implemented
- Calculations Verified
- Permissions Tested
- Output Verified
- Export Tested where required
- Provenance Documented

---

# 143. Dashboard Definition of Ready

A dashboard metric is Ready when:

- Metric Definition Is Clear
- Source Is Known
- Time Basis Is Known
- Authorization Is Known
- Refresh Strategy Is Known

---

# 144. Dashboard Definition of Done

A dashboard metric is Done when:

- Query Works
- Value Reconciles
- Permission Works
- Refresh Works
- Error State Works
- UI Is Clear

---

# 145. Read Model Definition of Ready

A read model is Ready when:

- Source Data Is Defined
- Refresh Strategy Is Defined
- Rebuild Strategy Is Defined
- Security Scope Is Defined
- Staleness Requirement Is Defined

---

# 146. Read Model Definition of Done

A read model is Done when:

- Builder Works
- Refresh Works
- Rebuild Works
- Source Consistency Is Tested
- Security Is Tested
- Failure Recovery Is Defined

---

# 147. Reporting Release Gate

Before release:

```text
Source Authority

Calculations

Filters

Permissions

Performance

Exports

Reconciliation

Accessibility

Regression
```

must be reviewed.

---

# 148. Financial Reporting Release Gate

Additional:

```text
Accounting Core Reconciliation

Debit / Credit Validation

Period Validation

Historical Accuracy

No Parallel Ledger
```

---

# 149. Traceability

Reporting changes should trace:

```text
Requirement

↓

Report / Metric Definition

↓

Query Service

↓

Repository

↓

Authoritative Source

↓

Test

↓

Release
```

---

# 150. Small-Association Principle

MFM reporting should remain practical.

The current scale does not justify:

- Enterprise Data Warehouse
- Complex BI Platform
- Distributed Analytics Cluster
- Large Streaming Infrastructure

unless actual organizational requirements change.

---

# 151. Future Analytics

If future reporting needs grow significantly:

```text
Operational Database

↓

Controlled Extraction

↓

Analytics Store

↓

Reports / BI
```

The operational system's authoritative business ownership remains unchanged.

---

# 152. Final Reporting Principle

Reporting converts authoritative data into understandable information.

It must not redefine the underlying truth.

---

# 153. Final Dashboard Principle

Dashboards prioritize:

```text
Current State

Attention

Trends

Action
```

They should remain concise.

---

# 154. Final Read-Model Principle

Read models improve read performance.

They remain:

```text
Derived

Rebuildable

Traceable

Non-Authoritative
```

where practical.

---

# 155. Final Financial Reporting Principle

> **Every actual financial value presented by a report, dashboard or read model must ultimately trace back to Accounting Core.**

No dashboard cache, project budget table, grant table or reporting table may become a competing financial ledger.

---

# 156. Summary

MFM v1.2-580 establishes the Reporting, Dashboard and Read-Model implementation baseline.

It defines:

- Reporting Service
- Dashboard Service
- Query Services
- Read Models
- Data Provenance
- Financial Reports
- Membership Reports
- Project Reports
- Grant Reports
- Document Reports
- Operational Reports
- Dashboards
- Metrics
- Filters
- Exports
- Reconciliation
- Caching
- Refresh
- Security
- Testing
- Performance
- Traceability

The central rule remains:

> **Reports and dashboards present derived information from authoritative domains; they do not own the underlying business truth.**

And:

> **Accounting Core remains the sole authoritative financial ledger.**

---

# 157. Next Document

**MFM v1.2-590 – Notifications, Background Jobs & Asynchronous Processing Implementation**

---

# END OF DOCUMENT

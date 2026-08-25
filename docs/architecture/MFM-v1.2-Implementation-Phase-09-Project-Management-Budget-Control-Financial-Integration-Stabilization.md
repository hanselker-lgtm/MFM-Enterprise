# MFM v1.2-Implementation-Phase-09
## Project Management, Budget Control & Project Financial Integration Stabilization

**Version:** 1.2  
**Document ID:** MFM-v1.2-Implementation-Phase-09  
**Status:** Implementation Phase Baseline  
**Phase:** Project Management & Financial Integration Stabilization  
**Document Type:** Implementation Execution Document  

---

# 1. Purpose

This document defines the ninth implementation phase following:

- MFM v1.2-Implementation-Phase-01 – Source Tree, Database & Baseline Validation
- MFM v1.2-Implementation-Phase-02 – Test Foundation, Regression Baseline & Quality Gate
- MFM v1.2-Implementation-Phase-03 – Core Service Stabilization & Domain Boundary Validation
- MFM v1.2-Implementation-Phase-04 – Repository, Persistence & Transaction Integrity Stabilization
- MFM v1.2-Implementation-Phase-05 – GUI Stabilization, Presentation Layer & User Workflow Validation
- MFM v1.2-Implementation-Phase-06 – Security Hardening, Identity, Authorization & Audit Validation
- MFM v1.2-Implementation-Phase-07 – Accounting Core Stabilization, Financial Controls & Regression Validation
- MFM v1.2-Implementation-Phase-08 – Membership & Member Management Stabilization

The purpose of this phase is to stabilize the MFM project-management domain and establish controlled integration between projects, budgets, costs, grants, documents and Accounting Core.

The implementation sequence is:

```text
Source / Database Baseline
        ↓
Test Foundation
        ↓
Core Service Stabilization
        ↓
Persistence Stabilization
        ↓
GUI Stabilization
        ↓
Security & Audit Stabilization
        ↓
Accounting Core Stabilization
        ↓
Membership Stabilization
        ↓
Project Management Stabilization
        ↓
Controlled Feature Implementation
```

The central objective is:

> **Project Core shall remain the authoritative source for project identity, project lifecycle, ownership, scope and project-management state, while Accounting Core remains authoritative for financial facts.**

---

# 2. Scope

This phase covers:

- Project master data
- Project lifecycle
- Project status
- Project ownership
- Project tasks
- Project milestones
- Project budgets
- Budget versions
- Budget control
- Project costs
- Project financial references
- Accounting integration
- Grant integration
- Project documents
- Project permissions
- Project reporting
- Project history
- Project audit
- Project testing
- Project regression
- Project quality gates

---

# 3. Project Authority

The fundamental project rule is:

> **Project Core is the authoritative source for project identity, lifecycle and project-management state.**

Accounting Core remains authoritative for posted financial facts.

---

# 4. Project Architecture

The preferred project flow is:

```text
GUI
 ↓
Project Application Service
 ↓
Project Domain Service
 ↓
Project Repository
 ↓
Database
```

Financial integration follows:

```text
Project
 ↓
Financial Reference / Cost Request
 ↓
Accounting Core
 ↓
Authoritative Financial Record
```

---

# 5. Project Master Record

A project record should provide controlled identity.

Typical information may include:

```text
Project ID
Project Number
Project Name
Description
Owner
Status
Start Date
End Date
Created Date
```

Additional fields may include:

```text
Project Type
Priority
Department / Area
Grant Reference
Document Reference
```

The exact fields shall follow the approved MFM model.

---

# 6. Project Identifier

Every project shall have a unique controlled identifier.

Project identifiers must remain stable throughout the project lifecycle.

---

# 7. Project Number

Where a separate project number is used, it shall be uniquely controlled.

Project numbers should not be reused for unrelated projects.

---

# 8. Project Status

Project status shall be centrally controlled.

A baseline lifecycle may be:

```text
Draft
 ↓
Planned
 ↓
Active
 ↓
On Hold
 ↓
Completed
 ↓
Closed
```

Additional states may be introduced where required.

---

# 9. Status Transition

Status transitions must be explicit and validated.

Examples:

```text
Draft → Planned
Planned → Active
Active → On Hold
On Hold → Active
Active → Completed
Completed → Closed
```

---

# 10. Invalid Transitions

Invalid project-state transitions must be rejected.

The rejection shall produce a controlled business error.

---

# 11. Project Ownership

Every active project should have a defined owner or responsible role.

Ownership may identify:

```text
Responsible User
Responsible Role
Department / Organizational Unit
```

---

# 12. Ownership Changes

Ownership changes shall be controlled and, where material, audited.

Historical ownership information should remain traceable.

---

# 13. Project Scope

A project should define its approved scope sufficiently to distinguish it from unrelated work.

Scope information may include:

```text
Objective
Description
Deliverables
Boundaries
Expected Outcome
```

---

# 14. Project Tasks

Projects may contain tasks.

A task should identify:

```text
Task ID
Description
Owner
Status
Start Date
Due Date
Completion Date
```

---

# 15. Task Status

Task status should be controlled.

A baseline may be:

```text
Open
In Progress
Blocked
Completed
Cancelled
```

---

# 16. Task Ownership

Tasks may be assigned to users or roles.

Assignments must respect authorization and project scope.

---

# 17. Project Milestones

Milestones represent significant project events.

Examples:

```text
Project Start
Funding Approval
Major Delivery
Inspection
Final Report
Project Completion
```

---

# 18. Milestone Control

Milestones should be traceable and should not silently disappear when project status changes.

---

# 19. Project Dates

Projects should distinguish:

```text
Planned Start
Actual Start
Planned End
Actual End
```

where applicable.

---

# 20. Date Validation

The project service should prevent invalid date combinations according to the approved project model.

---

# 21. Project Budget

A project budget represents an approved planning baseline.

Budget data may include:

```text
Budget ID
Project
Version
Amount
Currency
Period
Category
Status
```

---

# 22. Budget Authority

Project budgets are planning and control information.

Accounting Core remains authoritative for actual posted financial transactions.

---

# 23. Budget Versioning

Material budget changes should create controlled versions where required.

A budget version may have:

```text
Draft
Proposed
Approved
Superseded
```

---

# 24. Budget History

Previous approved budget versions must remain traceable.

A new budget must not silently overwrite the historical approved baseline.

---

# 25. Budget Approval

Budget approval should be controlled by appropriate roles.

The approval process should distinguish:

```text
Prepare
Review
Approve
```

where segregation of duties is required.

---

# 26. Budget Categories

Budget categories may include:

```text
Personnel
Materials
Equipment
Services
Travel
Administration
Other Approved Costs
```

The actual catalogue shall remain configurable.

---

# 27. Budget Periods

Where budgets are time-phased, each budget amount should be associated with an appropriate period.

---

# 28. Budget Currency

Budget currency must be explicit where multiple currencies are possible.

---

# 29. Budget Control

Budget control should compare planning information with authoritative actuals.

Examples:

```text
Budget
Actual
Committed
Remaining
Variance
```

---

# 30. Actuals Authority

Actual financial values must come from Accounting Core or approved financial services.

Project tables must not become an alternative ledger.

---

# 31. Commitment Data

If project commitments are supported, their definition and relationship to accounting data must be explicit.

---

# 32. Budget Variance

Variance may be calculated as:

```text
Budget - Actual
```

or according to the approved MFM reporting convention.

The convention must be consistent across project reports.

---

# 33. Negative Variance

The system should clearly define whether a negative variance indicates:

```text
Under Budget
```

or:

```text
Over Budget
```

The display convention must remain consistent.

---

# 34. Budget Thresholds

Projects may define control thresholds.

Examples:

```text
Warning
Approval Required
Critical
```

Thresholds must be configurable rather than duplicated across GUI components.

---

# 35. Budget Exception

A budget exception should identify:

```text
Project
Budget
Amount
Threshold
Reason
Status
Approver
Date
```

---

# 36. Project Cost References

Project costs may reference:

```text
Journal
Transaction
Invoice
Payment
Expense
```

but the financial source remains Accounting Core.

---

# 37. Cost Allocation

If costs are allocated to projects, allocation must follow controlled rules.

The project service should not independently alter accounting balances.

---

# 38. Accounting Integration

Project financial integration should use explicit service contracts.

Preferred:

```text
Project Service
      ↓
Accounting Query / Command
      ↓
Accounting Core
```

---

# 39. Financial Traceability

Every material project financial reference should be traceable to the authoritative accounting record.

---

# 40. Project-to-Accounting Link

Where supported, financial records may contain a project reference.

The reference must be valid and controlled.

---

# 41. Project Reporting

Project reporting may include:

```text
Project Status
Budget
Actual
Variance
Tasks
Milestones
Funding
Documents
Risks
```

Financial values must be derived from authoritative sources.

---

# 42. Project Dashboard

The project dashboard may show:

```text
Status
Progress
Budget
Actual
Variance
Open Tasks
Upcoming Milestones
Funding
```

---

# 43. Dashboard Currency

Financial values must display the appropriate currency context.

---

# 44. Dashboard Freshness

Project financial information should not appear current if it is based on stale data.

---

# 45. Project Documents

Projects may reference documents such as:

```text
Plans
Contracts
Applications
Grant Documents
Invoices
Receipts
Reports
Approvals
```

The Document Service remains authoritative for document storage and versioning.

---

# 46. Document Security

Project documents must respect both:

```text
Project Access
Document Access
```

---

# 47. Grant Integration

Projects may be linked to grants.

The relationship should identify:

```text
Project
Grant
Funding Reference
Eligibility / Conditions where applicable
```

---

# 48. Grant Financial Boundary

Grant financial information remains governed by Accounting Core for actual financial recognition.

---

# 49. Project Funding

Funding information may include:

```text
Funding Source
Award
Budget
Eligible Cost
Reporting Requirement
```

The exact funding model remains governed by the approved MFM grant architecture.

---

# 50. Project Permissions

Project access should be controlled through permissions and, where applicable, project-level scope.

---

# 51. Project Permissions Examples

Possible permissions:

```text
project.read
project.create
project.update
project.archive
project.manage_budget
project.approve_budget
project.manage_tasks
project.export
project.view_financials
```

---

# 52. Project Role

Roles may include:

```text
Project Manager
Project Contributor
Board Member
Treasurer
Grant Manager
Read-only User
Administrator
```

The actual role model shall follow approved MFM governance.

---

# 53. Project-Level Access

Where project-level access is supported, users should only access projects within their authorized scope.

---

# 54. Project Audit

Material project operations should be auditable.

Examples:

```text
Project Created
Project Updated
Owner Changed
Status Changed
Budget Created
Budget Approved
Budget Superseded
Task Assigned
Project Closed
Project Exported
```

---

# 55. Audit Record

Audit records should identify:

```text
User
Timestamp
Action
Project
Previous State where applicable
New State
Reason where required
Correlation ID
```

---

# 56. Project History

Project history should preserve important changes.

Examples:

```text
Status
Owner
Budget
Milestones
Major Scope Changes
Closure
```

---

# 57. Project Closure

Project closure should verify relevant completion conditions.

Possible checks:

```text
Tasks Completed
Financial Review Completed
Grant Reporting Completed
Required Documents Present
Outstanding Issues Resolved
```

The exact closure checklist shall follow MFM governance.

---

# 58. Reopening a Project

Reopening a closed project should be a controlled operation.

It should require:

- Authorization
- Reason
- Audit evidence

---

# 59. Project Cancellation

Cancellation must preserve historical project information.

---

# 60. Project Archive

Archiving should preserve required history while removing the project from ordinary active workflows.

---

# 61. Project Risk

Projects may contain risk information.

A risk record may include:

```text
Risk
Impact
Probability
Owner
Mitigation
Status
```

---

# 62. Project Issue

Issues may be recorded separately from risks.

An issue should identify:

```text
Issue
Owner
Priority
Status
Due Date
Resolution
```

---

# 63. Task and Issue Separation

Tasks, risks and issues should remain distinguishable.

---

# 64. Project Dependencies

Projects or tasks may depend on other projects or tasks.

Dependencies should be explicit where used.

---

# 65. Dependency Validation

The system should prevent invalid dependency structures where they create impossible workflows.

---

# 66. Project Search

Search may support:

```text
Project Number
Name
Owner
Status
Type
Grant
Date
```

---

# 67. Project Filtering

Filtering may support:

```text
Active
On Hold
Completed
Closed
Owner
Budget Status
Grant
```

---

# 68. Project Sorting

Sorting should be deterministic.

---

# 69. Project Pagination

Large project lists should use pagination or controlled loading.

---

# 70. Project Import

Project imports should validate:

- Identifiers
- Required fields
- Dates
- Status
- Owners
- Budget references
- Grant references

---

# 71. Project Import Preview

Where practical, imported project data should be previewed before committing.

---

# 72. Project Import Audit

Material project imports should record:

```text
User
Source
Timestamp
Record Count
Success
Failure
Result
```

---

# 73. Project Export

Project exports shall be permission-controlled.

Sensitive financial and grant information should be included only where authorized.

---

# 74. Project Data Protection

Project information may contain confidential operational or financial information.

Access and export shall follow the established security model.

---

# 75. Project Transaction Boundary

Project operations that modify multiple project records should use controlled transactions.

Example:

```text
Create Project
 ↓
Assign Owner
 ↓
Create Initial Budget
 ↓
Create Project References
```

If designed as atomic, failure must roll back the entire operation.

---

# 76. Project / Accounting Boundary

Project database transactions must not directly modify Accounting Core records.

Cross-domain financial actions shall use controlled interfaces.

---

# 77. Financial Failure Handling

If a project workflow requires a financial action and that action fails, the application must expose the correct partial-state result and follow the defined recovery strategy.

---

# 78. Concurrency

Concurrent project updates must be controlled.

Examples:

```text
Two users edit project
Two users approve budget
Two users change owner
```

---

# 79. Optimistic Concurrency

Where appropriate, project records should use version checks.

---

# 80. Budget Concurrency

Two users must not silently overwrite the same approved budget version.

---

# 81. Budget Approval Integrity

An approved budget version should be immutable or controlled against unauthorized modification.

---

# 82. Superseding Budget

A new approved budget should supersede the previous version without destroying its historical record.

---

# 83. Budget Recalculation

Where budget summaries are cached or materialized, a controlled recalculation or verification mechanism should exist.

---

# 84. Project Service Tests

Service tests shall cover:

```text
Create
Update
Status Change
Ownership
Task Management
Milestones
Budget
Closure
Reopening
Authorization
Audit
```

---

# 85. Project Repository Tests

Repository tests shall cover:

- Project persistence
- Status
- Ownership
- Tasks
- Milestones
- Budget versions
- References
- Constraints
- Search
- Filtering
- Concurrency

---

# 86. Project Integration Tests

Integration tests should verify:

```text
GUI
 ↓
Project Service
 ↓
Repository
 ↓
Database
```

for critical workflows.

---

# 87. Project Accounting Integration Tests

Tests should verify:

```text
Project
 ↓
Financial Reference
 ↓
Accounting Core
 ↓
Actual Financial Information
```

---

# 88. Budget Regression

Regression shall cover:

- Create budget
- Create new version
- Approve budget
- Supersede budget
- Prevent unauthorized changes
- Compare budget with actual

---

# 89. Project Status Regression

Regression shall cover:

```text
Valid Transition
Invalid Transition
Unauthorized Transition
Concurrent Transition
```

---

# 90. Project Closure Regression

Closure tests should verify required closure conditions and authorization.

---

# 91. Project Import Regression

Import regression shall cover:

- Valid import
- Invalid identifiers
- Invalid dates
- Invalid status
- Missing owner
- Duplicate project
- Rollback

---

# 92. Project Search Regression

Search regression shall verify:

- Exact match
- Partial match
- Multiple filters
- Empty results
- Permission scope

---

# 93. Project Export Regression

Export regression shall verify:

- Authorization
- Scope
- Fields
- Format
- Audit

---

# 94. Project Smoke Test

The project smoke test should verify:

```text
Open Projects
 ↓
Search Project
 ↓
Open Project
 ↓
Create Test Project
 ↓
Assign Owner
 ↓
Create Budget
 ↓
Add Task
 ↓
Add Milestone
 ↓
View Financial Reference
 ↓
Close Test Project
```

The test must use isolated test data.

---

# 95. Project Invariants

The implementation shall preserve:

```text
Project ID Is Unique
Project Number Is Controlled
Status Transitions Are Valid
Approved Budget History Is Preserved
Financial Authority Remains Accounting Core
Project Documents Remain Under Document Authority
```

---

# 96. Budget Invariants

The system shall preserve:

```text
Approved Budget Version Is Traceable
Historical Versions Are Preserved
Actuals Come From Accounting Core
Budget Variance Is Reproducible
```

---

# 97. Financial Traceability Invariant

Every project financial summary must be traceable to the underlying authoritative accounting information.

---

# 98. Grant Traceability

Project grant references must remain traceable to the relevant grant records.

---

# 99. Project Performance

Project searches and dashboards should remain efficient for expected association-scale workloads.

---

# 100. Caching

Project caching may be used where appropriate.

Cache invalidation must occur after material project changes.

Financial data must follow the established freshness policy.

---

# 101. Technical Debt

Project technical debt shall be recorded.

Examples:

```text
Business Logic in GUI
Duplicated Budget Logic
Direct SQL
Unclear Project Authority
Duplicated Financial Calculations
Missing Budget History
Missing Audit
Uncontrolled Grant Integration
```

---

# 102. Project Defect Register

Each material project defect should contain:

| Field | Requirement |
|---|---|
| ID | Unique |
| Severity | P0–P3 |
| Component | Project area |
| Description | Problem |
| Reproduction | Steps |
| Expected | Expected result |
| Actual | Actual result |
| Financial Impact | Where applicable |
| Grant Impact | Where applicable |
| Security Impact | Where applicable |
| Test | Regression test |
| Status | Lifecycle |
| Resolution | Correction |

---

# 103. Project Quality Gate

Project Core passes when:

```text
Project Master Data       ✓
Lifecycle                 ✓
Ownership                 ✓
Tasks / Milestones        ✓
Budget                    ✓
Budget Versioning         ✓
Budget Control            ✓
Accounting Integration    ✓
Grant Integration         ✓
Documents                 ✓
Authorization             ✓
Audit                     ✓
Reporting                 ✓
Regression                ✓
```

---

# 104. Data Integrity Gate

Project data integrity passes when:

- Project identifiers are unique.
- Status transitions are valid.
- Ownership is traceable.
- Budget history is preserved.
- Project references remain valid.
- Grant references remain valid.
- Financial references remain traceable.

---

# 105. Budget Control Gate

Budget control passes when:

- Approved baseline is identifiable.
- Versions are traceable.
- Actuals come from Accounting Core.
- Variances are reproducible.
- Thresholds are controlled.
- Unauthorized budget changes are rejected.

---

# 106. Accounting Integration Gate

Project accounting integration passes when:

- Financial references are explicit.
- Actuals are authoritative.
- Project does not maintain an independent ledger.
- Financial queries are controlled.
- Financial failures are handled correctly.

---

# 107. Grant Integration Gate

Grant integration passes when:

- Project-to-grant relationships are traceable.
- Funding information is controlled.
- Grant restrictions remain visible.
- Financial authority remains Accounting Core.
- Access is authorized.

---

# 108. Document Gate

Project document integration passes when:

- Documents are registered through Document Service.
- Access is controlled.
- Versions are preserved.
- Project references are valid.

---

# 109. Security Gate

Project security passes when:

- Project permissions work.
- Project-level access works where applicable.
- Financial data is protected.
- Grant data is protected.
- Export is controlled.
- Material changes are auditable.

---

# 110. Definition of Ready

A project work item is Ready when:

- Project purpose is defined.
- Owner is known.
- Lifecycle state is defined.
- Budget impact is known.
- Accounting impact is known.
- Grant impact is known.
- Security requirements are known.
- Audit requirements are known.
- Regression tests are planned.

---

# 111. Definition of Done

A project work item is Done when:

```text
Project Rule Defined
        ↓
Implementation Complete
        ↓
Unit Tested
        ↓
Service Tested
        ↓
Repository Tested
        ↓
Budget Tested
        ↓
Accounting Integration Tested
        ↓
Security Tested
        ↓
Audit Tested
        ↓
Regression Tested
        ↓
Documentation Updated
        ↓
Project Quality Gate Passed
```

---

# 112. Final Project Authority Principle

> **Project Core is the authoritative source for project identity, lifecycle, ownership and project-management state.**

---

# 113. Final Financial Principle

> **Accounting Core remains the sole authority for actual posted financial information.**

---

# 114. Final Budget Principle

> **Project budgets are controlled planning baselines and must remain historically traceable.**

---

# 115. Final Budget History Principle

> **An approved budget version must not be silently overwritten by a later version.**

---

# 116. Final Integration Principle

> **Projects shall integrate with Accounting, Grants and Documents through explicit service contracts rather than direct access to internal data.**

---

# 117. Final Security Principle

> **Project access must be authorized according to role and, where applicable, project-level scope.**

---

# 118. Final Audit Principle

> **Material project, ownership, budget and closure changes must be traceable through appropriate audit evidence.**

---

# 119. Final Reporting Principle

> **Project financial reporting must derive actuals from authoritative Accounting Core information.**

---

# 120. Final Testing Principle

> **Project lifecycle, budget control and financial integration require dedicated regression coverage because they form a major cross-domain dependency.**

---

# 121. Final Implementation Principle

> **Stabilize project identity, lifecycle, budget control and financial integration before expanding project functionality.**

---

# 122. Summary

MFM v1.2-Implementation-Phase-09 establishes the Project Management, Budget Control and Project Financial Integration Stabilization baseline.

It defines:

- Project Master Data
- Project Identifiers
- Project Lifecycle
- Project Status
- Ownership
- Scope
- Tasks
- Milestones
- Project Dates
- Budgets
- Budget Versioning
- Budget Approval
- Budget Categories
- Budget Periods
- Budget Control
- Actuals
- Commitments
- Variance
- Thresholds
- Cost References
- Accounting Integration
- Financial Traceability
- Project Reporting
- Project Dashboard
- Project Documents
- Grant Integration
- Project Permissions
- Project Audit
- Project History
- Project Closure / Reopening / Cancellation / Archive
- Risks / Issues / Dependencies
- Search / Filtering / Sorting / Pagination
- Project Import / Export
- Data Protection
- Transactions
- Concurrency
- Budget Concurrency
- Project / Repository / Integration Testing
- Budget / Status / Closure / Import / Search / Export Regression
- Project Smoke Testing
- Project and Budget Invariants
- Financial / Grant Traceability
- Performance and Caching
- Technical Debt
- Project Defect Register
- Project Quality Gates
- Data Integrity Gate
- Budget Control Gate
- Accounting Integration Gate
- Grant Integration Gate
- Document Gate
- Security Gate
- Definition of Ready
- Definition of Done

---

# 123. Next Implementation Phase

The next document shall be:

**MFM v1.2-Implementation-Phase-10 – Grant & Funding Management Stabilization**

It shall establish the controlled implementation and validation of:

- Grant master data
- Funding sources
- Grant applications
- Grant lifecycle
- Awards
- Funding conditions
- Eligible costs
- Grant budgets
- Project / grant relationships
- Accounting integration
- Grant reporting
- Grant documents
- Deadlines
- Compliance requirements
- Grant permissions
- Grant audit
- Grant testing
- Grant regression
- Grant quality gates

---

# 124. Document Control

**Document:** MFM v1.2-Implementation-Phase-09  
**Version:** 1.2  
**Status:** Implementation Phase Baseline  
**Previous Document:** MFM v1.2-Implementation-Phase-08  
**Next Document:** MFM v1.2-Implementation-Phase-10  
**Primary Transition:** Membership Stabilization → Project Management Stabilization  
**Financial Authority:** Accounting Core  
**Project Authority:** Project Core  
**Principle:** Project state and budget control must remain authoritative, traceable and securely integrated with financial services

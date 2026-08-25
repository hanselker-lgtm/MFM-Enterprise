# PRODUCT-004 Reporting Architecture

Scope: reporting architecture based strictly on LOCKED capabilities and completed workflows.

Locked capabilities:
- Organization
- Projects
- Documents
- Accounting

Completed workflows used as reporting foundations:
- WF-001 Organization Onboarding
- WF-002 Project Creation
- WF-003 Project Document Registration
- WF-004 Project Budget Initialization
- WF-005 Project Accounting
- WF-006 Project Closure & Archive

Constraints:
- No production code changes.
- Feature API contracts and reporting architecture only.
- Read-time composition preferred; write paths remain owned by capability feature APIs.

## Reporting Model

### Reporting Dimensions
- Organization dimension: organization identity, type, lifecycle.
- Project dimension: lifecycle status, ownership, references, closure markers.
- Document dimension: document metadata, versioning state, project linkage, archive manifests.
- Accounting dimension: fiscal year, journal status, posting integrity, project-linked transactions.
- Workflow evidence dimension: derived markers written by completed workflows (budget readiness, reconciliation, closure status, archive manifest linkage).

### Canonical Correlation Keys
- organization_id
- project_id
- document_id
- fiscal_year_id
- journal_id
- journal_number
- workflow markers encoded in project/document references (for example BUDGET_STATUS:READY, BUDGET_RECONCILIATION:COMPLETED, PROJECT_CLOSURE_STATUS:CLOSED)

### Report Delivery Strategy
- Online views via composed feature API reads.
- Export-oriented reports via asynchronous generation against report read models.
- Deterministic snapshots for audit and executive reporting.

---

## REP-001 Organization Dashboard

Report ID:
- REP-001

Business purpose:
- Provide a top-level organization health view across onboarding completeness, active projects, document coverage, and accounting readiness.

Intended users:
- Organization administrators
- Portfolio managers
- Executives

Data sources:
- Organization master data
- Projects linked to organization references
- Documents linked to organization/project scope
- Accounting fiscal year and journal aggregates

Required Feature APIs:
- Organization: GetOrganizationFeature, ListOrganizationsFeature
- Projects: ListProjectsFeature, SearchProjectsFeature, GetProjectFeature
- Documents: search_documents(...), list_documents(...)
- Accounting: list_fiscal_years(...), search_journals(...)

Filtering options:
- organization_id
- organization_type
- organization_status
- time period

Sorting options:
- organization_name
- created_at
- active_project_count
- financial_activity_volume

Export formats:
- CSV
- XLSX
- PDF

Security considerations:
- organization-level tenant boundary
- role-based access to financial aggregates
- redaction of sensitive governance metadata in broad views

Performance considerations:
- pre-aggregated organization KPIs
- cache of project/document/accounting counts
- incremental refresh by capability event timestamps

Missing Feature APIs:
- organization KPI summary API

Missing indexes:
- project references by organization_id
- document references by organization and project scope

Missing query capabilities:
- cross-capability organization-level aggregate query endpoint

Missing integrations:
- unified reporting read model for organization-to-project-to-finance rollup

---

## REP-002 Active Projects

Report ID:
- REP-002

Business purpose:
- List active projects with operational and financial status indicators.

Intended users:
- PMO
- Project managers
- Delivery leads

Data sources:
- Projects lifecycle/status
- Documents linked to projects
- Posted journals by project reference

Required Feature APIs:
- Projects: ListProjectsFeature, SearchProjectsFeature, GetProjectFeature
- Documents: search_documents(...)
- Accounting: search_journals(...)

Filtering options:
- project_status (default ACTIVE)
- priority
- organization
- date range

Sorting options:
- project_number
- project_name
- priority
- last_activity

Export formats:
- CSV
- XLSX

Security considerations:
- project-level access controls
- suppress accounting totals for non-finance users

Performance considerations:
- indexed project status and priority lookups
- batched project detail hydration

Missing Feature APIs:
- project list with embedded reporting metrics

Missing indexes:
- project status + priority composite index
- journal reference text index for project correlation

Missing query capabilities:
- direct project-to-posted-journal count/amount query

Missing integrations:
- event-driven project activity timestamp materialization

---

## REP-003 Project Status

Report ID:
- REP-003

Business purpose:
- Show per-project readiness and lifecycle progression through creation, documentation, budgeting, accounting, and closure.

Intended users:
- Project managers
- Program managers
- Audit/compliance analysts

Data sources:
- Project lifecycle status
- Project references for workflow markers
- Linked documents and their statuses
- Linked journals and posting statuses

Required Feature APIs:
- Projects: GetProjectFeature, SearchProjectsFeature
- Documents: list_documents(...), get_document(...)
- Accounting: search_journals(...)

Filtering options:
- project_id
- status
- organization
- readiness flags

Sorting options:
- status
- closure_readiness
- budget_readiness

Export formats:
- CSV
- PDF

Security considerations:
- read restrictions for archive and audit markers
- controlled visibility of reconciliation metadata

Performance considerations:
- derive readiness flags in read model, not per-request fan-out

Missing Feature APIs:
- consolidated project readiness API

Missing indexes:
- project reference description index for workflow markers

Missing query capabilities:
- query by readiness marker family (budget/accounting/closure)

Missing integrations:
- centralized workflow-state projection from WF-001..WF-006 events

---

## REP-004 Budget vs Actual

Report ID:
- REP-004

Business purpose:
- Compare initialized project budget baselines to posted accounting actuals.

Intended users:
- Finance controllers
- Project managers
- Executives

Data sources:
- Budget markers/categories from project references (WF-004)
- Posted journals linked to project references (WF-005)
- Fiscal year metadata

Required Feature APIs:
- Projects: GetProjectFeature, SearchProjectsFeature
- Accounting: search_journals(...), get_fiscal_year(...), list_fiscal_years(...)

Filtering options:
- project_id
- fiscal_year
- accounting period
- budget category

Sorting options:
- variance amount
- variance percentage
- project_number

Export formats:
- CSV
- XLSX
- PDF

Security considerations:
- finance role required for monetary detail
- separation of duties for reconciliation adjustments

Performance considerations:
- pre-computed budget category mapping
- period-based journal aggregation snapshots

Missing Feature APIs:
- explicit project budget aggregate APIs (create/get/list/update)
- project journal aggregate totals API

Missing indexes:
- project-reference marker index for budget categories
- accounting journal reference + posting_date index

Missing query capabilities:
- native variance query (budget baseline vs posted actual)

Missing integrations:
- mapping layer between budget category markers and accounting account dimensions

---

## REP-005 Accounting Summary

Report ID:
- REP-005

Business purpose:
- Provide summary of journal activity, posting status distribution, and account movement by project and fiscal scope.

Intended users:
- Accountants
- Controllers
- Finance leads

Data sources:
- Journals
- Ledger accounts
- Fiscal year state
- Project references in journal reference fields

Required Feature APIs:
- Accounting: list_journals(...), search_journals(...), list_ledger_accounts(...), get_fiscal_year(...)
- Projects: GetProjectFeature (for project context enrichment)

Filtering options:
- fiscal_year
- posting status
- account
- project reference

Sorting options:
- posting_date
- journal_number
- amount

Export formats:
- CSV
- XLSX

Security considerations:
- strict finance authorization
- immutable audit extract option

Performance considerations:
- accounting-side pagination and status filtering
- summary caches by fiscal year and status

Missing Feature APIs:
- accounting summary aggregate API with grouped totals

Missing indexes:
- journal status + fiscal_year index
- journal_number + posting_date index

Missing query capabilities:
- grouped totals by project reference and account

Missing integrations:
- standardized project reference schema in journals for robust joins

---

## REP-006 Fiscal Year Summary

Report ID:
- REP-006

Business purpose:
- Summarize fiscal year state, period closures, posting completeness, and project financial footprint.

Intended users:
- Finance leadership
- Auditors
- Governance board

Data sources:
- Fiscal years and periods
- Posted journals
- Project-linked journal references

Required Feature APIs:
- Accounting: list_fiscal_years(...), get_fiscal_year(...), search_journals(...)
- Projects: SearchProjectsFeature (optional project scope overlay)

Filtering options:
- fiscal_year
- period
- status (OPEN/CLOSED/ARCHIVED)

Sorting options:
- fiscal_year
- close_progress
- posted_volume

Export formats:
- CSV
- PDF

Security considerations:
- close-control data visible only to finance governance roles

Performance considerations:
- fiscal-year snapshots for heavy summary queries

Missing Feature APIs:
- fiscal year summary endpoint with posting KPI fields

Missing indexes:
- fiscal year period boundaries and status access paths

Missing query capabilities:
- period-level posting completeness query by project

Missing integrations:
- linkage between fiscal-period closure and project closure-readiness checkpoints

---

## REP-007 Document Register

Report ID:
- REP-007

Business purpose:
- Provide complete register of project/organization documents with version status and reference coverage.

Intended users:
- Document controllers
- Project administrators
- Compliance officers

Data sources:
- Documents metadata
- Versions
- Document references to projects/organizations/accounting artifacts

Required Feature APIs:
- Documents: list_documents(...), search_documents(...), get_document(...)
- Projects: GetProjectFeature (for context)
- Accounting: get_journal(...) (for evidence links where required)

Filtering options:
- document_status
- document_type
- target_capability
- project_id

Sorting options:
- document_number
- created_at
- updated_at

Export formats:
- CSV
- XLSX

Security considerations:
- sensitive document metadata masking by role
- archived/disposed visibility controls

Performance considerations:
- full-text search index for document number/title
- reference join denormalization for report queries

Missing Feature APIs:
- document register endpoint with linked-target projections

Missing indexes:
- document status + type index
- document reference target capability/aggregate index

Missing query capabilities:
- query documents by project + finalized evidence completeness

Missing integrations:
- common evidence model between Documents and Accounting journal attachments

---

## REP-008 Audit Trail

Report ID:
- REP-008

Business purpose:
- Deliver end-to-end audit trace across workflows WF-001..WF-006 for a selected organization/project.

Intended users:
- Internal audit
- External audit
- Compliance and risk

Data sources:
- Project references containing workflow markers
- Archive manifest references and audit metadata
- Documents and versions
- Journal lifecycle states and reversals

Required Feature APIs:
- Projects: GetProjectFeature, SearchProjectsFeature
- Documents: get_document(...), search_documents(...), list_documents(...)
- Accounting: search_journals(...), get_journal(...), list_fiscal_years(...)

Filtering options:
- organization_id
- project_id
- workflow stage
- date range

Sorting options:
- chronological event order
- workflow stage
- capability source

Export formats:
- PDF (signed audit pack)
- CSV
- JSON

Security considerations:
- immutable export mode
- strict least-privilege and access auditing
- tamper-evident hash chain for audit pack generation

Performance considerations:
- append-only audit read model
- pre-built timeline segments per project

Missing Feature APIs:
- canonical audit timeline API across capabilities

Missing indexes:
- marker-description index for workflow/audit tags
- journal reference index for project correlation

Missing query capabilities:
- timeline query across capabilities with deterministic ordering

Missing integrations:
- unified event envelope contract across Organization/Projects/Documents/Accounting

---

## REP-009 Archive Register

Report ID:
- REP-009

Business purpose:
- Track archived projects and archive package completeness/readiness for retrieval.

Intended users:
- Records managers
- Compliance officers
- PMO governance

Data sources:
- Archived project states
- Archive manifest documents
- Manifest references to documents/journals/fiscal year/audit metadata

Required Feature APIs:
- Projects: SearchProjectsFeature, GetProjectFeature
- Documents: search_documents(...), get_document(...)
- Accounting: search_journals(...), get_fiscal_year(...)

Filtering options:
- archived date range
- organization
- archive manifest presence
- retrieval readiness

Sorting options:
- archived_at
- project_number
- manifest_completeness

Export formats:
- CSV
- PDF

Security considerations:
- role-restricted archive retrieval metadata
- legal-hold flags and retention controls

Performance considerations:
- dedicated archive register projection
- lazy-load deep manifest dependencies

Missing Feature APIs:
- archive register API exposing manifest completeness metrics

Missing indexes:
- project archived_at index
- manifest document_type + project reference index

Missing query capabilities:
- query archived projects with missing package elements

Missing integrations:
- lifecycle integration to retention/legal-hold systems

---

## REP-010 Executive Dashboard

Report ID:
- REP-010

Business purpose:
- Provide strategic executive view of delivery, compliance, financial posture, and archival maturity.

Intended users:
- Executive leadership
- Board committees
- Governance office

Data sources:
- Aggregated outputs from REP-001..REP-009
- cross-capability KPI snapshots

Required Feature APIs:
- Projects: SearchProjectsFeature, ListProjectsFeature
- Documents: search_documents(...)
- Accounting: search_journals(...), list_fiscal_years(...)
- Organization: ListOrganizationsFeature

Filtering options:
- organization portfolio
- fiscal year
- time period
- risk/compliance dimension

Sorting options:
- KPI variance severity
- financial exposure
- closure/archival backlog

Export formats:
- PDF (board pack)
- XLSX
- JSON

Security considerations:
- aggregate-only data by default
- drill-down guarded by role scopes

Performance considerations:
- materialized KPI cubes
- scheduled snapshot generation

Missing Feature APIs:
- executive KPI composition API with standardized metric contracts

Missing indexes:
- metric snapshot time-series index

Missing query capabilities:
- multi-report blended KPI query with drill-through identifiers

Missing integrations:
- unified semantic metric layer over capability read models

---

## Cross-Report Architectural Gaps (Prioritized)

1. Missing project budget domain APIs (highest functional gap)
- No first-class budget aggregate/read model APIs; current workflow markers are not sufficient for deep reporting.

2. Missing cross-capability reporting query layer
- Existing APIs are command/read-entity focused, not analytical; heavy fan-out composition is required today.

3. Missing standardized workflow/audit event model
- Workflow traceability currently depends on marker conventions; there is no canonical event timeline contract.

4. Missing reporting-focused indexes
- Project reference descriptions, journal references, and manifest lookups need explicit indexing for scale.

5. Missing archive and executive read models
- Archive and executive dashboards require denormalized projections not present in current capability APIs.

## Highest Priority Report
- REP-004 Budget vs Actual

Rationale:
- It is central to project financial governance, directly depends on WF-004 and WF-005 outcomes, and exposes the largest current functional/API gap.

## Biggest Architectural Gap
- Absence of a first-class Project Budget capability slice (budget aggregate + reporting APIs + query model), causing budget reporting to rely on workflow markers rather than authoritative budget entities.

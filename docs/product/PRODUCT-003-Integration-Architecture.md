# PRODUCT-003 Integration Architecture

Scope: Integration architecture across currently LOCKED capabilities.

Locked capabilities:
- Organization
- Projects
- Documents
- Accounting

Constraints:
- No production code changes in this milestone.
- Architecture-first contracts only (Feature APIs, Domain Events, references, ownership, consistency, failure semantics).

## Integration Principles

1. Capability ownership is strict.
   - Organization owns organization lifecycle and governance metadata.
   - Projects owns project lifecycle and project state machine.
   - Documents owns document metadata, version history, and references.
   - Accounting owns fiscal years, ledgers, journals, and posting state.

2. Cross-capability writes are prohibited inside a single database transaction.
   - Each capability commits its own transaction boundary.
   - Cross-capability effects are propagated through events and idempotent handlers.

3. Read-time composition is preferred over write-time coupling.
   - Synchronous calls are for validation/lookups and immediate command preconditions.
   - Asynchronous events are for propagation, denormalized views, and reconciliation.

4. All asynchronous contracts require idempotency and replay safety.

---

## INT-001 Organization ↔ Projects

### Dependency Direction
- Primary dependency: Projects -> Organization.
- Reverse dependency: none for command handling; optional Organization read models may subscribe to project events.

### Synchronous Interactions
- Projects validates organization existence/active status before create/update project.
- Projects may resolve organization governance metadata for policy checks.

### Asynchronous Interactions
- Organization publishes lifecycle changes consumed by Projects.
- Projects publishes project lifecycle changes optionally consumed by Organization reporting.

### Required Feature APIs
- Organization:
  - GetOrganizationFeature.execute(GetOrganizationRequest)
  - ListOrganizationsFeature.execute(ListOrganizationsRequest)
- Projects:
  - CreateProjectFeature.execute(CreateProjectRequest)
  - UpdateProjectFeature.execute(UpdateProjectRequest)
  - GetProjectFeature.execute(GetProjectRequest)

### Required Domain Events
- OrganizationCreated
- OrganizationUpdated
- OrganizationActivated
- OrganizationSuspended
- OrganizationArchived
- ProjectCreated
- ProjectCompleted
- ProjectArchived

### References Exchanged
- `organization_id` (required foreign reference in project aggregate)
- Optional: governance metadata snapshot (board/committee references)

### Ownership of Data
- Organization owns organization master data and status.
- Projects owns project data and cached organization projection (if any).

### Transaction Boundaries
- Project create/update transaction is local to Projects repository.
- Organization validation is pre-commit read; no distributed transaction.

### Consistency Model
- Strong consistency for command preconditions (sync validation).
- Eventual consistency for downstream projections and reporting.

### Failure Handling
- Sync validation failure: reject command with business validation error.
- Organization event delivery failure: retry with exponential backoff + dead-letter queue.
- Stale cache detection: version check on organization snapshot.

### Required Repositories (if any)
- Projects repository (authoritative).
- Optional Projects-side read model repository for organization snapshot/cache.

### Eventual Consistency Requirements
- Organization status changes must propagate to Projects projections within operational SLA (target <= 60 seconds).

---

## INT-002 Projects ↔ Documents

### Dependency Direction
- Primary dependency: Documents -> Projects for target validation.
- Reverse dependency: Projects -> Documents for closure/archive evidence checks.

### Synchronous Interactions
- Document attach-reference validates project target existence.
- Project close/archive checks required document evidence existence.

### Asynchronous Interactions
- Projects emits lifecycle events consumed by Documents for retention policy/materialized links.
- Documents emits document lifecycle events consumed by Projects for readiness views.

### Required Feature APIs
- Projects:
  - GetProjectFeature.execute(GetProjectRequest)
  - CompleteProjectFeature.execute(CompleteProjectRequest)
  - ArchiveProjectFeature.execute(ArchiveProjectRequest)
- Documents:
  - create_document(...)
  - register_document_version(...)
  - attach_reference(...)
  - search_documents(...)
  - archive_document(...)

### Required Domain Events
- ProjectCreated
- ProjectCompleted
- ProjectArchived
- DocumentCreated
- DocumentVersionRegistered
- DocumentReferenceAttached
- DocumentArchived

### References Exchanged
- `project_id` in document reference payload.
- `document_id` set associated with project evidence checklist.

### Ownership of Data
- Projects owns project lifecycle state.
- Documents owns document metadata, versions, and reference records.

### Transaction Boundaries
- Document create/version/attach occurs in Documents local transaction.
- Project close/archive occurs in Projects local transaction.
- Cross-capability checks are read-only preconditions.

### Consistency Model
- Strong consistency for command-time precondition checks.
- Eventual consistency for evidence-readiness dashboards and aggregate counters.

### Failure Handling
- Attach validation failure: return target-not-found/invalid-reference error.
- Project close blocked: deterministic validation response with missing-evidence details.
- Event processing failure: retry, then dead-letter + operator reconciliation workflow.

### Required Repositories (if any)
- Documents repository (authoritative docs + references).
- Projects repository (authoritative lifecycle).
- Optional read model repository for project evidence readiness.

### Eventual Consistency Requirements
- Evidence readiness projections must converge before close/archive automation is triggered.

---

## INT-003 Projects ↔ Accounting

### Dependency Direction
- Primary dependency: Projects -> Accounting for budget/actual and posting checks.
- Reverse dependency: Accounting -> Projects for project reference validation during posting.

### Synchronous Interactions
- Accounting posting flow validates referenced project existence/status.
- Project close/archive validates accounting obligations complete.

### Asynchronous Interactions
- Accounting publishes journal posted/reversed events consumed by project financial summaries.
- Projects publishes lifecycle events consumed by accounting policy/readiness logic.

### Required Feature APIs
- Projects:
  - GetProjectFeature.execute(GetProjectRequest)
  - CompleteProjectFeature.execute(CompleteProjectRequest)
  - ArchiveProjectFeature.execute(ArchiveProjectRequest)
- Accounting:
  - create_journal(...)
  - post_journal(...)
  - reverse_journal(...)
  - get_journal(...)
  - search_journals(...)
  - list_ledger_accounts(...)
  - get_fiscal_year(...)

### Required Domain Events
- ProjectCreated
- ProjectCompleted
- ProjectArchived
- JournalCreated
- JournalPosted
- JournalReversed
- FiscalYearOpened
- FiscalYearClosed

### References Exchanged
- `project_id` on accounting journal header/lines (project dimension).
- `journal_id` references in project finance timeline/projections.

### Ownership of Data
- Projects owns project business lifecycle.
- Accounting owns financial truth (journals, ledgers, fiscal periods).

### Transaction Boundaries
- Posting transaction is local to Accounting.
- Project transition transaction is local to Projects.
- No shared transaction across both capabilities.

### Consistency Model
- Strong consistency for posting/business-rule checks at command time.
- Eventual consistency for project-level budget-vs-actual and financial snapshots.

### Failure Handling
- Unbalanced or closed-period posting: reject synchronously with business-rule violation.
- Event propagation delay: mark project financial summary as pending refresh.
- Replay/duplication: enforce idempotency via event ID + handler dedupe store.

### Required Repositories (if any)
- Accounting repositories (journal/ledger/fiscal year authoritative stores).
- Projects repository.
- Optional project-finance projection repository.

### Eventual Consistency Requirements
- Project financial projection may lag source journals; close/archive commands must re-validate against authoritative Accounting API.

---

## INT-004 Projects ↔ Archive

Note: Archive is an integration concern, not a locked standalone capability. The architecture treats Archive as a cross-capability workflow orchestration boundary.

### Dependency Direction
- Primary dependency: Archive workflow -> Projects.
- Secondary dependencies: Archive workflow -> Documents and Archive workflow -> Accounting for evidence package completeness.

### Synchronous Interactions
- Archive workflow calls project archive command.
- Archive workflow performs readiness checks via Projects, Documents, and Accounting feature APIs.

### Asynchronous Interactions
- ProjectArchived event triggers evidence package generation and immutable retention records.
- Archive package completion event updates project archive metadata view.

### Required Feature APIs
- Projects:
  - ArchiveProjectFeature.execute(ArchiveProjectRequest)
  - GetProjectFeature.execute(GetProjectRequest)
- Documents:
  - search_documents(...)
  - archive_document(...)
- Accounting:
  - search_journals(...)
  - get_journal(...)

### Required Domain Events
- ProjectArchiveRequested
- ProjectArchived
- ArchivePackageGenerationStarted
- ArchivePackageGenerationCompleted
- ArchivePackageGenerationFailed

### References Exchanged
- `project_id`
- `document_ids[]`
- `journal_ids[]`
- `archive_package_id`

### Ownership of Data
- Projects owns archival state of project lifecycle.
- Documents/Accounting own underlying evidence records.
- Archive workflow owns package manifest metadata only.

### Transaction Boundaries
- Project archive transition and package generation are separate transactions.
- Package generation is asynchronous and resumable.

### Consistency Model
- Eventual consistency by design for package materialization.
- Project archive state may become effective before package completion.

### Failure Handling
- Package generation failure: keep project archived but mark package status FAILED/RETRYABLE.
- Partial evidence retrieval: produce deterministic failure reason and compensation task.
- Retry policy with backoff; dead-letter after threshold and manual remediation path.

### Required Repositories (if any)
- Projects repository.
- Optional Archive manifest repository (workflow-owned).
- Existing Documents/Accounting repositories via feature APIs only.

### Eventual Consistency Requirements
- Archive package completion is eventually consistent; audit operations must inspect package status before export.

---

## INT-005 Documents ↔ Accounting

### Dependency Direction
- Bidirectional by reference; no direct ownership crossover.
- Documents references accounting artifacts for evidence.
- Accounting references documents for supporting vouchers/attachments.

### Synchronous Interactions
- Document reference attachment validates accounting target existence (journal).
- Accounting command flow validates linked supporting document IDs when policy requires.

### Asynchronous Interactions
- JournalPosted events trigger document compliance checks/indexing.
- DocumentArchived events update accounting evidence-readiness projections.

### Required Feature APIs
- Documents:
  - attach_reference(...)
  - remove_reference(...)
  - search_documents(...)
  - get_document(...)
- Accounting:
  - get_journal(...)
  - search_journals(...)
  - post_journal(...)

### Required Domain Events
- JournalPosted
- JournalReversed
- AccountingEvidenceLinked
- DocumentReferenceAttached
- DocumentArchived

### References Exchanged
- `journal_id` on document references.
- `document_id` on accounting evidence metadata.

### Ownership of Data
- Documents owns document and reference records.
- Accounting owns journal and posting state.

### Transaction Boundaries
- Reference attach/remove local to Documents.
- Posting local to Accounting.
- Cross-checks are precondition reads.

### Consistency Model
- Strong consistency for command-level validation where required by policy.
- Eventual consistency for compliance dashboards and evidence completeness views.

### Failure Handling
- Missing linked evidence: reject posting when policy mandates strict evidence.
- Non-mandatory evidence unavailable: accept posting and emit follow-up compliance event.
- Event failures handled via idempotent retries + dead-letter + reconciliation job.

### Required Repositories (if any)
- Documents repository.
- Accounting repositories.
- Optional evidence-compliance projection repository.

### Eventual Consistency Requirements
- Evidence completeness views are eventually consistent and must not be the sole source for blocking financial close.

---

## Canonical Transaction and Consistency Rules

1. No distributed transactions across capability boundaries.
2. Every cross-capability command precondition must be revalidated against authoritative source APIs.
3. All domain events require:
   - immutable event ID
   - aggregate ID
   - version/sequence
   - occurred-at timestamp
   - idempotent consumer contract
4. Dead-letter and replay operations are mandatory for operational resilience.

## Recommended First Integration

INT-001 Organization ↔ Projects.

Rationale:
- Lowest coupling complexity.
- Establishes canonical reference and dependency pattern used by all other integrations.
- Reduces risk before introducing document/accounting event-driven joins.

## Highest Architectural Risk

INT-003 Projects ↔ Accounting.

Risk drivers:
- Financial correctness requirements combined with project lifecycle transitions.
- High impact of eventual consistency lag on close/archive decisions.
- Need for strict idempotency, reconciliation, and authoritative revalidation under failure/replay conditions.

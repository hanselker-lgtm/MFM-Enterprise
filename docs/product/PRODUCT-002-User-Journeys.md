# PRODUCT-002 User Journeys

Scope: first complete user journeys based on currently LOCKED capabilities:
- Organization
- Projects
- Documents
- Accounting

Perspective: end-user workflow architecture (not implementation).

## UJ-001 Create Organization

User goal:
- Register a new organization as the root business entity.

Preconditions:
- User has organization admin permissions.
- Organization number/code is available and unique.

Happy path:
1. User opens Organization onboarding.
2. User enters organization profile data.
3. System validates required fields.
4. System creates organization.
5. System confirms creation and shows organization overview.

Alternative paths:
- User updates existing organization profile instead of creating a new one.
- User creates board/committee immediately after creation.

Validation failures:
- Missing required fields.
- Duplicate organization identifier.
- Invalid status/lifecycle transition input.

Result:
- Organization exists and is available for project ownership and governance.

Capabilities involved:
- Organization

Required Feature APIs:
- CreateOrganizationFeature.execute(CreateOrganizationRequest)
- UpdateOrganizationFeature.execute(UpdateOrganizationRequest)
- CreateBoardFeature.execute(CreateBoardRequest)
- CreateCommitteeFeature.execute(CreateCommitteeRequest)

Missing APIs:
- None required for core flow.

Missing integrations:
- App-level identity/authorization integration for admin role resolution.

UX risks:
- Unclear distinction between organization creation and governance setup (board/committee).

Technical risks:
- Low.

---

## UJ-002 Create Project

User goal:
- Create a project under an existing organization.

Preconditions:
- Organization exists.
- User has project manager permissions.

Happy path:
1. User opens Projects module.
2. User selects owning organization.
3. User enters project core fields (number, name, schedule, status).
4. System validates project payload.
5. System creates project and returns project overview.

Alternative paths:
- User creates project as DRAFT/PLANNED and defers milestones.
- User creates project with initial assignments/references.

Validation failures:
- Duplicate project number.
- Invalid status or date range.
- Invalid referenced IDs.

Result:
- Project is created and ready for lifecycle actions.

Capabilities involved:
- Organization
- Projects

Required Feature APIs:
- CreateProjectFeature.execute(CreateProjectRequest)
- GetProjectFeature.execute(GetProjectRequest)
- UpdateProjectFeature.execute(UpdateProjectRequest)

Missing APIs:
- None for initial creation.

Missing integrations:
- Organization-to-project lookup binding in UI/workflow layer.

UX risks:
- Overly complex first-step form if milestones/activities/assignments are required too early.

Technical risks:
- Low.

---

## UJ-003 Register Project Documents

User goal:
- Register and attach project-related documents for traceability.

Preconditions:
- Project exists.
- User has document management permission.

Happy path:
1. User opens Documents from a project context.
2. User creates document metadata.
3. User registers initial version.
4. User attaches project reference.
5. System confirms document is linked to project.

Alternative paths:
- User adds a new version to an existing document.
- User links one document to multiple targets.

Validation failures:
- Duplicate document number.
- Invalid target reference payload.
- Invalid version metadata.

Result:
- Document is stored with version history and linked to the project.

Capabilities involved:
- Projects
- Documents

Required Feature APIs:
- create_document(...)
- register_document_version(...)
- attach_reference(...)
- get_document(...)
- list_documents(...)

Missing APIs:
- None for registration + linking.

Missing integrations:
- Binary upload orchestration from UI to blob/storage port behind document metadata flow.
- Project context resolver for automatic target reference prefill.

UX risks:
- Users may not understand metadata-first flow before upload completion.

Technical risks:
- Medium (cross-flow consistency between metadata and binary storage lifecycle).

---

## UJ-004 Create Project Budget

User goal:
- Define budget lines for a project and prepare financial tracking.

Preconditions:
- Project exists.
- Accounting fiscal year and ledger setup exists.

Happy path:
1. User opens project budget screen.
2. User enters planned amounts by category/account.
3. System validates amounts and account references.
4. System saves budget baseline.

Alternative paths:
- User imports baseline budget from template.
- User revises budget after governance approval.

Validation failures:
- Unknown ledger account.
- Invalid amount format or negative constraints.
- Missing required budget dimensions.

Result:
- Project budget baseline established.

Capabilities involved:
- Projects
- Accounting

Required Feature APIs:
- get_project/list_projects (project context)
- list_ledger_accounts(...)

Missing APIs:
- Project budget aggregate and feature APIs (create/update/get/list budget).

Missing integrations:
- Projects-to-accounting budget mapping and budget-vs-actual query integration.

UX risks:
- Budget workflow may be blocked by missing conceptual model (budget vs actual, versioning, approvals).

Technical risks:
- High (new capability slice needed across project-accounting boundary).

---

## UJ-005 Register Project Accounting

User goal:
- Record project financial postings and keep auditable journal trail.

Preconditions:
- Project exists.
- Fiscal year open and relevant periods open.
- Ledger accounts available.

Happy path:
1. User opens project accounting posting screen.
2. User selects project and posting date.
3. User enters balanced journal lines.
4. System validates balance and fiscal constraints.
5. System creates journal and posts it.
6. System confirms posted journal with reference.

Alternative paths:
- Save as draft and post later.
- Reverse posted journal and repost corrected entry.

Validation failures:
- Unbalanced journal.
- Posting into closed period/year.
- Invalid account IDs or line amounts.

Result:
- Posted journal is recorded and linked to project traceability context.

Capabilities involved:
- Projects
- Accounting

Required Feature APIs:
- create_journal(...)
- post_journal(...)
- get_journal(...)
- reverse_journal(...)
- search_journals(...)

Missing APIs:
- Explicit project-tagged journal query/report APIs.

Missing integrations:
- Project reference propagation into accounting posting flow.
- Project-level financial summary integration.

UX risks:
- High risk of user confusion without project-centric accounting views.

Technical risks:
- Medium-High (integration/reporting gaps, not core posting engine gaps).

---

## UJ-006 Close Project

User goal:
- Mark a project complete once work and financial obligations are finalized.

Preconditions:
- Project exists and is in closable state.
- Required evidence documents are present.
- Required accounting postings are completed/reconciled.

Happy path:
1. User opens project close checklist.
2. System validates project state and completion criteria.
3. User confirms closure action.
4. System marks project complete.
5. System returns closed project status and summary.

Alternative paths:
- Close with pending non-blocking items flagged.
- Reopen correction path before archive.

Validation failures:
- Missing mandatory documents.
- Outstanding required accounting entries.
- Invalid lifecycle transition.

Result:
- Project status is COMPLETED with closure metadata.

Capabilities involved:
- Projects
- Documents
- Accounting

Required Feature APIs:
- CompleteProjectFeature.execute(CompleteProjectRequest)
- GetProjectFeature.execute(GetProjectRequest)
- search_documents(...)
- search_journals(...)

Missing APIs:
- Consolidated project close-readiness API.

Missing integrations:
- Cross-capability close checklist aggregator (project + document + accounting status).

UX risks:
- Manual cross-screen verification burden may cause closure errors.

Technical risks:
- Medium.

---

## UJ-007 Archive Project

User goal:
- Archive a completed project and preserve evidence for audit/governance.

Preconditions:
- Project is completed.
- Required documents are archived/retained.
- Financial trail is finalized.

Happy path:
1. User opens archive action on completed project.
2. System verifies archive preconditions.
3. User confirms archive.
4. System archives project.
5. System displays archived status and audit retrieval links.

Alternative paths:
- Archive with governance note attached.
- Deferred archive if preconditions fail.

Validation failures:
- Project not yet completed.
- Mandatory evidence missing.
- Accounting close dependencies unresolved.

Result:
- Project is archived and retained for lookup and audit preparation.

Capabilities involved:
- Projects
- Documents
- Accounting

Required Feature APIs:
- ArchiveProjectFeature.execute(ArchiveProjectRequest)
- GetProjectFeature.execute(GetProjectRequest)
- search_documents(...)
- search_journals(...)

Missing APIs:
- Explicit archive package export API.

Missing integrations:
- Unified archive evidence pack assembly (project + documents + accounting records).

UX risks:
- Archiving may feel irreversible without clear recovery/governance messaging.

Technical risks:
- Medium.

---

## Cross-Journey Integration Gaps (Consolidated)

1. Project Budget domain slice is not present as a first-class locked capability workflow.
   - Missing budget aggregate, APIs, and budget-vs-actual queries.

2. Project-to-accounting traceability/reporting integration is partial.
   - Posting exists, but project-centric accounting summaries and explicit linkage APIs are limited.

3. Cross-capability close/archive checklist orchestration is missing.
   - No single API to evaluate closure readiness across Projects, Documents, and Accounting.

4. Audit/export package assembly is missing.
   - No dedicated API to produce an end-to-end evidence package for project close/archive.

## Recommended First Implementation

Start with UJ-001 Create Organization.

Reason:
- It is the foundational workflow with lowest risk.
- Every downstream workflow depends on organization context.
- It delivers immediate user-visible value while enabling all subsequent journeys.

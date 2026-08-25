# PRODUCT-001 Product Roadmap

Scope: first end-user workflows for MFM Enterprise using the currently LOCKED capabilities only:
- Organization
- Projects
- Documents
- Accounting

This roadmap is ordered by recommended implementation priority for end-user value.

## Recommended Implementation Order

| Priority | Workflow ID | Workflow Name | Business Goal | User Roles Involved | Capabilities Used | Estimated Size | Business Value | Technical Risk | Missing Integrations | Missing Capabilities | Dependencies | Recommended Priority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | WF-001 | Create Organization | Onboard a new organization so all downstream work has a governed owner and identity anchor. | Admin, Organization Manager | Organization | S | 5 | 1 | User onboarding to the public Organization feature API; initial identity provisioning flow in the app shell. | None identified. | None. This is the foundational workflow. | Highest |
| 2 | WF-002 | Create Project | Start a governed project under an existing organization. | Project Manager, Organization Manager | Organization, Projects | S | 5 | 2 | Organization-to-Project selection, owner assignment, and project creation UX. | None identified within the locked capability set. | Requires an existing Organization. | High |
| 3 | WF-003 | Register Document | Capture and link a document as project or organization evidence. | Project Manager, Document Clerk, Organization Manager | Organization, Projects, Documents | S | 4 | 2 | Upload-to-metadata flow, document reference picker, and attachment UX across Projects/Documents. | None identified within the locked capability set. | Requires an Organization and usually a Project reference. | High |
| 4 | WF-004 | Project Budget | Define and track the approved budget for a project. | Project Manager, Finance Manager, Controller | Organization, Projects, Accounting | M | 5 | 3 | Project budget entry and budget-vs-actual view; allocation mapping from Project to Accounting. | Project budget object/reporting capability; budget-to-accounting allocation model. | Requires Organization, Project, and ledger context for budget tracking. | High |
| 5 | WF-005 | Project Accounting | Post project-related financial transactions and reconcile them to the project. | Accountant, Controller, Project Manager | Organization, Projects, Accounting | M | 5 | 4 | Project picker in accounting workflows; project-coded journal reporting and reconciliation view. | Project accounting/reporting capability for cost allocation and project balance queries. | Requires Organization, Project, and Accounting ledger setup. | High |
| 6 | WF-006 | Project Archive | Close a completed project, preserve evidence, and freeze it for lookup. | Project Manager, Document Clerk, Controller | Organization, Projects, Documents, Accounting | M | 4 | 3 | Archive checklist UI, final evidence pack assembly, and final accounting sign-off integration. | Project archive governance workflow; archive checklist/closure state reporting. | Requires completed Project, archived evidence documents, and reconciled accounting records. | Medium-High |
| 7 | WF-007 | Complete Project Lifecycle | Execute the full lifecycle from creation through delivery, evidence, budget, accounting, and closure. | Organization Manager, Project Manager, Document Clerk, Accountant, Controller | Organization, Projects, Documents, Accounting | L | 5 | 4 | Cross-capability workflow orchestration, status dashboard, and end-to-end handoff visibility. | Workflow orchestration/status capability for cross-capability delivery tracking. | Depends on Create Organization, Create Project, Register Document, Budget, Accounting, and Archive workflows. | Medium-High |
| 8 | WF-008 | Annual Closing | Close the fiscal year after all project activity and evidence are settled. | Accountant, Controller, Auditor | Organization, Projects, Accounting, Documents | M | 5 | 4 | Year-end close checklist, period close visibility, and audit evidence export. | Annual close reporting capability; year-end package generation. | Requires accounting period closure, project reconciliation, and supporting documents. | Medium |
| 9 | WF-009 | Audit Preparation | Assemble a complete audit package from project, document, and accounting evidence. | Auditor, Controller, Accountant, Document Clerk | Organization, Projects, Documents, Accounting | L | 4 | 3 | Evidence bundling, cross-capability search/export, and audit package delivery. | Audit package generation and evidence traceability capability. | Requires archived projects, linked documents, and closed/reconciled accounting records. | Medium |
| 10 | WF-010 | Restore Archived Project | Reopen an archived project when governance permits and restore its evidence trail. | Organization Manager, Project Manager, Auditor | Organization, Projects, Documents, Accounting | M | 3 | 4 | Restore workflow, status reversal UX, and document/accounting re-link validation. | Project restore/reopen governance capability. | Requires an archived project and governance approval; may depend on document restore and accounting adjustment flows. | Medium-Low |

## Workflow Notes

### WF-001 Create Organization
This is the root onboarding workflow for the product. It establishes the identity and governance boundary needed by every other workflow.

### WF-002 Create Project
This is the first meaningful business workflow after onboarding. It creates the delivery container that projects, documents, and accounting entries can attach to.

### WF-003 Register Document
This workflow starts the evidence trail. It is essential for project governance, audit preparation, and closure.

### WF-004 Project Budget
This is the first workflow that needs a richer project-to-accounting integration than the current locked capabilities expose out of the box.

### WF-005 Project Accounting
This workflow directly uses the Accounting capability to turn project activity into financial truth.

### WF-006 Project Archive
This workflow closes the operational project record and preserves the evidence needed for later audit or governance review.

### WF-007 Complete Project Lifecycle
This is the first full end-user journey that combines organization onboarding, project setup, evidence capture, accounting, and closure.

### WF-008 Annual Closing
This is a finance-led year-end workflow that depends on project closure discipline and supporting documents.

### WF-009 Audit Preparation
This is a cross-capability evidence workflow for controllers and auditors.

### WF-010 Restore Archived Project
This is an exception workflow and should be implemented after the standard forward lifecycle is stable.

## Recommendation Summary

The first workflow should be Create Organization because it is the foundation for every other end-user journey and has the lowest technical risk.

The next most valuable sequence is Create Project, Register Document, and then the project-budget/accounting path.

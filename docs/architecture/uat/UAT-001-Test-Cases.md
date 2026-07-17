# UAT-001 Test Cases

Date: 2026-07-17
Program: P1-001

## Test Case Matrix

| Test Case ID | Business Scenario | Preconditions | Steps (High-Level) | Expected Result | Evidence |
|---|---|---|---|---|---|
| UAT-001-TC-01 | Create organization | Organization feature/workflow stack available | Execute organization creation workflow with valid identifiers and organization metadata | Organization is created, persisted, and retrievable | tests/integration/test_organization_end_to_end.py |
| UAT-001-TC-02 | Register members | Membership onboarding workflow available | Execute member enrollment workflow with contact/member inputs | Member registration succeeds and member state is available for downstream workflows | tests/application/workflows/test_enroll_member_workflow.py |
| UAT-001-TC-03 | Assign board roles | Organization and role entities exist | Create board and assign role through public feature/workflow boundaries | Role assignment persists and organization governance graph remains valid | tests/integration/test_organization_end_to_end.py; tests/application/features/organization/test_organization_features.py |
| UAT-001-TC-04 | Create membership fee | Membership billing workflow available | Execute fee schedule setup through billing workflow | Fee schedule is created and available for billing run | tests/application/workflows/test_membership_billing_workflow.py |
| UAT-001-TC-05 | Register payment | Payment workflow available | Execute payment registration workflow against valid contingent/invoice context | Payment registration succeeds and workflow returns expected success state | tests/application/workflows/test_register_payment_workflow.py |
| UAT-001-TC-06 | Create event | Events activities workflow available | Execute event creation with required event metadata | Event is created and available for registration/attendance flow | tests/application/workflows/test_events_activities_workflow.py |
| UAT-001-TC-07 | Register attendance | Event and participant records exist | Register participant and record attendance through events workflow | Attendance is registered and reflected in workflow outputs | tests/application/workflows/test_events_activities_workflow.py |
| UAT-001-TC-08 | Upload documents | Document workflow available | Register document/version with storage reference and link to business context | Document registration and reference linkage succeed | tests/application/workflows/test_project_document_registration_workflow.py; tests/application/workflows/test_document_archive_workflow.py |
| UAT-001-TC-09 | Generate reports | Reporting features and dashboard host wired | Load reporting snapshots/routes and query report services | Reports render/load successfully with expected route behavior | tests/presentation/test_dashboard_host.py; tests/application/reporting/test_organization_dashboard_service.py; tests/application/reporting/test_project_status_service.py; tests/application/reporting/test_budget_vs_actual_service.py; tests/application/reporting/test_active_projects_service.py |
| UAT-001-TC-10 | Verify archive | Archive workflows available | Execute project/document archive workflows and verify retrieval state | Archived artifacts are preserved with expected archive semantics | tests/application/workflows/test_project_closure_archive_workflow.py; tests/application/workflows/test_document_archive_workflow.py |

## Workflow Validation Summary

| Workflow Area | Validation Status | Notes |
|---|---|---|
| Organization onboarding and governance | PASS | End-to-end organization integration and role assignment validated |
| Membership and billing chain | PASS | Enrollment, fee setup, and payment registration workflows covered |
| Events lifecycle | PASS | Event creation and attendance registration covered |
| Document and archive chain | PASS | Document registration/archive and project closure archive covered |
| Reporting and dashboard | PASS | Report generation pathways covered via dashboard/reporting tests |

## Acceptance Notes

1. Scenario language "Upload documents" is validated via current document registration/version workflows that capture storage keys and archive references.
2. UAT coverage is evidence-driven and based on executable automated suites in current repository baseline.

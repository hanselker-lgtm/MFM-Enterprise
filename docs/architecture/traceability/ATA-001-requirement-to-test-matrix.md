# ATA-001 Requirement-to-Test Matrix

Date: 2026-07-17

| Requirement ID | Capability | Requirement Statement | Test Evidence |
|---|---|---|---|
| CAP001-REQ-001 | CAP-001 | Register/list/change membership through service + feature boundary | tests/application/membership/test_membership_management_service.py; tests/application/features/membership/test_manage_membership_feature.py |
| CAP001-REQ-002 | CAP-001 | Membership workflow/reporting/GUI wiring exists | tests/application/workflows/test_membership_management_workflow.py; tests/application/reporting/test_membership_summary_service.py; tests/presentation/test_application_shell_memberships_route.py |
| CAP002-REQ-001 | CAP-002 | Manage organization roles foundation via feature boundary | tests/application/features/organization_roles/test_manage_organization_roles_feature.py |
| CAP002-REQ-002 | CAP-002 | Organization roles workflow/reporting/GUI integration exists | tests/application/workflows/test_organization_roles_workflow.py; tests/application/reporting/test_organization_roles_summary_service.py; tests/presentation/test_application_shell_organization_roles_route.py |
| CAP003-REQ-001 | CAP-003 | Configure contact communication profile via feature boundary | tests/application/features/contact_communication/test_manage_contact_communication_feature.py |
| CAP003-REQ-002 | CAP-003 | Contact communication workflow/reporting/GUI integration exists | tests/application/workflows/test_contact_communication_workflow.py; tests/application/reporting/test_contact_communication_summary_service.py; tests/presentation/test_application_shell_contact_communication_route.py |
| CAP004-REQ-001 | CAP-004 | Setup fee schedule and run billing through feature/service contracts | tests/application/membership_billing/test_membership_billing_service.py; tests/application/features/membership_billing/test_manage_membership_billing_feature.py |
| CAP004-REQ-002 | CAP-004 | Billing workflow/reporting/GUI integration exists | tests/application/workflows/test_membership_billing_workflow.py; tests/application/reporting/test_membership_billing_summary_service.py; tests/presentation/test_application_shell_membership_billing_route.py |
| CAP004-REQ-003 | CAP-004 | Billing integrates with accounting contract via annual contingent feature | tests/integration/test_platform_integration_review.py |
| CAP005-REQ-001 | CAP-005 | Event creation/activity/registration/attendance flow works | tests/application/events_activities/test_events_activities_service.py; tests/application/features/events_activities/test_manage_events_activities_feature.py |
| CAP005-REQ-002 | CAP-005 | Events workflow/reporting/GUI integration exists | tests/application/workflows/test_events_activities_workflow.py; tests/application/reporting/test_events_activities_summary_service.py; tests/presentation/test_application_shell_events_activities_route.py |
| CAP005-REQ-003 | CAP-005 | Events capability supports membership reference contract | tests/integration/test_platform_integration_review.py |
| CAP006-REQ-001 | CAP-006 | Document archive create/version/attach/archive flow works | tests/application/document_archive/test_document_archive_service.py; tests/application/features/document_archive/test_manage_document_archive_feature.py |
| CAP006-REQ-002 | CAP-006 | Document archive workflow/reporting/GUI integration exists | tests/application/workflows/test_document_archive_workflow.py; tests/application/reporting/test_document_archive_summary_service.py; tests/presentation/test_application_shell_document_archive_route.py |
| CAP006-REQ-003 | CAP-006 | Document archive cross-capability attachment contracts are enforced | tests/integration/test_platform_integration_review.py |
| CAP006-REQ-004 | CAP-006 | Projects-documents feature-level integration remains valid | tests/application/features/onboarding/test_project_document_registration_feature_e2e.py |

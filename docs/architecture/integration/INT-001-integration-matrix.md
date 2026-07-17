# INT-001 Integration Matrix

Date: 2026-07-17

| Pair | Integration Type | Boundary Mechanism | Evidence | Status |
|---|---|---|---|---|
| Membership ↔ Billing | Service/feature orchestration | membership_type_id reference + annual contingent result contract | tests/integration/test_platform_integration_review.py | PASS |
| Membership ↔ Events | Reference-based participation | member_id in event registration | tests/integration/test_platform_integration_review.py | PASS |
| Membership ↔ Documents | Reference attachment | target_capability=MEMBERSHIP in archive attachments | tests/integration/test_platform_integration_review.py | PASS |
| Organization ↔ Membership | Reference-level identity compatibility | UUID identity boundaries across capabilities | tests/integration/test_platform_integration_review.py | PASS |
| Organization ↔ Events | Reference-level coordination | capability-local ownership with transport-safe references | tests/integration/test_platform_integration_review.py | PASS |
| Communication ↔ All capabilities | Shared contact boundary | contact_id profile setup across capability contexts | tests/integration/test_platform_integration_review.py | PASS |
| Accounting ↔ Billing | Feature/service integration | annual contingent output consumed by billing service | tests/integration/test_platform_integration_review.py | PASS |
| Projects ↔ Documents | Workflow orchestration | ProjectDocumentRegistrationWorkflow + document reference linking | tests/application/features/onboarding/test_project_document_registration_feature_e2e.py | PASS |

# UAT-001 Defect Log

Date: 2026-07-17
Program: P1-001

## Defect Register

| Defect ID | Area | Severity | Status | Description | Evidence | Disposition |
|---|---|---|---|---|---|---|
| UAT-001-DEF-001 | Documentation semantics | Low | Accepted | Scenario wording "Upload documents" maps to current document registration/version/storage-key workflow semantics rather than explicit binary-upload UI automation. | tests/application/workflows/test_project_document_registration_workflow.py; tests/application/workflows/test_document_archive_workflow.py | Accepted as in-scope behavior for current architecture; no blocking impact |
| UAT-001-DEF-002 | Reporting evidence granularity | Low | Accepted | Reporting scenario is validated through dashboard host and reporting services; no separate UAT-only report-generation script exists. | tests/presentation/test_dashboard_host.py; tests/application/reporting/* | Accepted; existing automated evidence considered sufficient for UAT-001 |

## Summary

1. Blocking defects: 0
2. Major defects: 0
3. Minor/Low defects: 2 (accepted)

## Defect Triage Decision

All logged defects are non-blocking and do not prevent go-live decision for UAT scope.

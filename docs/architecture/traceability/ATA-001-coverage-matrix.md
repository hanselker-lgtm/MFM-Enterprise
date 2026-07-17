# ATA-001 Coverage Matrix

Date: 2026-07-17

Legend:
- Y = traceability evidence present
- P = partially explicit (inferred from capability architecture/tests)

| Capability | Business Requirement | Domain Objects | Feature API | Workflow | Reporting API | GUI Integration | Integration Contracts | Test Coverage | ADR Reference | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| CAP-001 Membership Management | Y | Y | Y | Y | Y | Y | P | Y | Y | PASS |
| CAP-002 Organization Roles | Y | Y | Y | Y | Y | Y | P | Y | Y | PASS |
| CAP-003 Contact Communication | Y | Y | Y | Y | Y | Y | P | Y | Y | PASS |
| CAP-004 Membership Billing | Y | Y | Y | Y | Y | Y | Y | Y | Y | PASS |
| CAP-005 Events Activities | Y | Y | Y | Y | Y | Y | Y | Y | Y | PASS |
| CAP-006 Document Archive | Y | Y | Y | Y | Y | Y | Y | Y | Y | PASS |

Notes:
1. CAP-001..CAP-003 integration contracts are reference-boundary contracts (UUID/reference DTO contracts) and not separate capability integration report files.
2. CAP-004..CAP-006 include explicit capability integration reports under docs/architecture/capabilities.

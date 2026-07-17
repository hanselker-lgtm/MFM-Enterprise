# INT-001 Dependency Matrix

Date: 2026-07-17

Legend:
- F = Feature API dependency
- R = Reference-only identity dependency
- . = no direct dependency

Rows are dependers. Columns are dependee capabilities.

| From \ To | Membership | Billing | Events | Documents | Organization | Communication | Accounting | Projects |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Membership | . | R | R | R | R | R | . | . |
| Billing | R | . | . | . | . | . | F | . |
| Events | R | . | . | R | R | R | . | . |
| Documents (Archive) | R | R | R | . | R | . | . | R |
| Organization | R | . | R | R | . | R | . | R |
| Communication | R | R | R | R | R | . | R | R |
| Accounting | . | R | . | . | . | . | . | . |
| Projects | . | . | . | F | R | . | . | . |

Notes:
1. Documents row reflects CAP-006 archive attachment targets and feature-mediated document lifecycle calls.
2. Billing depends on accounting integration result contract through annual contingent generation feature usage.
3. Projects ↔ Documents is validated by workflow-level feature orchestration evidence.
4. Communication dependencies are contact-reference compatibility expectations, not repository coupling.

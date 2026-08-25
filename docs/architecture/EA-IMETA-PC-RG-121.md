# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-CLOSURE-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-121`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-121` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-CLOSURE-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Response Closure Determination |
| Parent | EA-IMETA-PC-RG-120 — Mandatory Post-Closure Regression Response Resolution Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory closure-determination layer that determines whether a resolved post-closure regression case may be formally closed, whether all required records, obligations, residual risks, controls, acceptance and follow-up requirements have been completed, and whether the case has entered a controlled post-closure monitoring state.

## Core Principle
Resolution establishes that the underlying condition has reached the required resolved state. Closure establishes that the governed response case and its associated obligations may formally leave the active response state. Closure shall therefore be a separate, evidence-based and authority-approved determination and shall not erase monitoring, residual-risk or reopening obligations.

```text
RESOLUTION VERIFIED + ACCEPTED
        ↓
CLOSURE PRECONDITIONS SATISFIED?
├── NO → COMPLETE OUTSTANDING REQUIREMENTS
└── YES
     ↓
RECORDS COMPLETE?
├── NO → COMPLETE / CORRECT RECORDS
└── YES
     ↓
OBLIGATIONS COMPLETE?
├── NO → COMPLETE / ESCALATE
└── YES
     ↓
RESIDUAL RISK GOVERNED?
├── NO → GOVERN / ACCEPT / MITIGATE
└── YES
     ↓
FOLLOW-UP MONITORING DEFINED?
├── NO → ESTABLISH MONITORING
└── YES
     ↓
CLOSURE AUTHORITY ACCEPTS?
├── NO → REMAIN OPEN / ESCALATE
└── YES
     ↓
CASE CLOSED
     ↓
POST-CLOSURE MONITORING ACTIVE
```

## Closure Quality Test
```text
VALID RESOLUTION
+
CLOSURE CRITERIA SATISFIED
+
RECORDS COMPLETE
+
MANDATORY OBLIGATIONS COMPLETE
+
RESIDUAL RISK IDENTIFIED AND GOVERNED
+
FOLLOW-UP REQUIREMENTS DEFINED
+
REOPENING CONDITIONS DEFINED
+
AUTHORIZED ACCEPTANCE
+
TRACEABLE CLOSURE EVIDENCE
=
VALID GOVERNED CLOSURE DETERMINATION
```

## Resolution vs Closure vs Post-Closure Monitoring
```text
RESOLUTION
→ UNDERLYING CONDITION REACHED REQUIRED RESOLVED STATE

CLOSURE
→ ACTIVE GOVERNANCE CASE FORMALLY LEAVES ACTIVE RESPONSE STATE

POST-CLOSURE MONITORING
→ CLOSED CONDITION REMAINS SUBJECT TO DEFINED OBSERVATION AND REOPENING CONTROLS
```

## Closure States
```text
C0 — NOT CLOSABLE / ACTIVE
C1 — CLOSURE PRECONDITIONS PENDING
C2 — CLOSURE ASSESSMENT IN PROGRESS
C3 — CLOSURE READY
C4 — CLOSURE AUTHORIZED
C5 — CLOSED
C6 — CLOSED WITH CONTROLLED RESIDUAL OBLIGATIONS
CX — UNKNOWN / INVALID CLOSURE EVIDENCE
CF — CLOSURE FAILED / REJECTED
CR — CLOSED CASE REOPENED
```

## Closure Dimensions
| Dimension | Required determination |
|---|---|
| Resolution | Valid resolved state |
| Criteria | Closure acceptance criteria |
| Records | Complete authoritative record |
| Obligations | Required duties completed or governed |
| Residual Risk | Remaining risk and acceptance |
| Monitoring | Post-closure monitoring requirements |
| Reopening | Trigger and authority |
| Retention | Record retention requirements |
| Acceptance | Closure authority acceptance |
| Evidence | Closure evidence |
| Transition | Controlled move to post-closure state |

## Closure Invariants

```text
CLOSURE SHALL BE DISTINCT FROM RESOLUTION
```

```text
CLOSURE SHALL REQUIRE EXPLICIT CLOSURE CRITERIA
```

```text
CLOSURE SHALL NOT ERASE RESIDUAL RISK OR OUTSTANDING CONTROLLED OBLIGATIONS
```

```text
MANDATORY RECORDS SHALL BE COMPLETE AND TRACEABLE BEFORE CLOSURE WHERE REQUIRED
```

```text
MANDATORY OBLIGATIONS SHALL BE COMPLETED OR EXPLICITLY GOVERNED BEFORE CLOSURE
```

```text
RESIDUAL RISK SHALL BE IDENTIFIED AND ACCEPTED BY THE AUTHORIZED PARTY WHERE ACCEPTANCE IS REQUIRED
```

```text
POST-CLOSURE MONITORING REQUIREMENTS SHALL BE DEFINED BEFORE CLOSURE WHERE REQUIRED
```

```text
REOPENING CONDITIONS SHALL BE DEFINED BEFORE CLOSURE WHERE MATERIAL
```

```text
UNKNOWN OR INSUFFICIENT EVIDENCE SHALL NOT SUPPORT CLOSURE
```

```text
CLOSURE SHALL NOT BE USED TO SUPPRESS ACTIVE REGRESSION OR UNRESOLVED CONSEQUENCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE CLOSURE SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT CLOSURE SHALL INCLUDE REQUIRED HUMAN GOVERNANCE, AUDIT AND OVERSIGHT CONDITIONS
```

```text
CLOSURE SHALL PRESERVE COMPLETE TRACEABILITY TO REGRESSION, RESPONSE, EFFECTIVENESS AND RESOLUTION
```

```text
CLOSURE SHALL NOT PREVENT LATER REOPENING WHEN DEFINED CONDITIONS OCCUR
```

```text
CLOSED STATUS SHALL NOT BE EQUIVALENT TO ZERO RISK
```

```text
CLOSURE CONTROLS SHALL BE REVIEWED AFTER PREMATURE, FALSE OR REPEATED REOPENING
```

## 1. Closure Domain — Post-Closure Regression Response Closure Governance

**Control family:** `PCRC-001`

The Post-Closure Regression Response Closure Governance domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-001-01` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-001-02` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-001-03` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-001-04` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-001-05` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-001-06` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-001-07` — Establish and maintain the post-closure regression response closure governance control.
- `PCRC-001-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 2. Closure Domain — Post-Closure Regression Response Closure Objective

**Control family:** `PCRC-002`

The Post-Closure Regression Response Closure Objective domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-002-01` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-002-02` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-002-03` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-002-04` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-002-05` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-002-06` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-002-07` — Establish and maintain the post-closure regression response closure objective control.
- `PCRC-002-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 3. Closure Domain — Post-Closure Regression Response Closure Definition

**Control family:** `PCRC-003`

The Post-Closure Regression Response Closure Definition domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-003-01` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-003-02` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-003-03` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-003-04` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-003-05` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-003-06` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-003-07` — Establish and maintain the post-closure regression response closure definition control.
- `PCRC-003-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 4. Closure Domain — Post-Closure Regression Response Closure Scope

**Control family:** `PCRC-004`

The Post-Closure Regression Response Closure Scope domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-004-01` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-004-02` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-004-03` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-004-04` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-004-05` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-004-06` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-004-07` — Establish and maintain the post-closure regression response closure scope control.
- `PCRC-004-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 5. Closure Domain — Post-Closure Regression Response Closure Authority

**Control family:** `PCRC-005`

The Post-Closure Regression Response Closure Authority domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-005-01` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-005-02` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-005-03` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-005-04` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-005-05` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-005-06` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-005-07` — Establish and maintain the post-closure regression response closure authority control.
- `PCRC-005-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 6. Closure Domain — Post-Closure Regression Response Closure Criteria

**Control family:** `PCRC-006`

The Post-Closure Regression Response Closure Criteria domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-006-01` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-006-02` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-006-03` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-006-04` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-006-05` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-006-06` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-006-07` — Establish and maintain the post-closure regression response closure criteria control.
- `PCRC-006-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 7. Closure Domain — Post-Closure Regression Response Closure Preconditions

**Control family:** `PCRC-007`

The Post-Closure Regression Response Closure Preconditions domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-007-01` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-007-02` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-007-03` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-007-04` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-007-05` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-007-06` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-007-07` — Establish and maintain the post-closure regression response closure preconditions control.
- `PCRC-007-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 8. Closure Domain — Post-Closure Regression Response Closure Evidence

**Control family:** `PCRC-008`

The Post-Closure Regression Response Closure Evidence domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-008-01` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-008-02` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-008-03` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-008-04` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-008-05` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-008-06` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-008-07` — Establish and maintain the post-closure regression response closure evidence control.
- `PCRC-008-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 9. Closure Domain — Post-Closure Regression Response Closure Method

**Control family:** `PCRC-009`

The Post-Closure Regression Response Closure Method domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-009-01` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-009-02` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-009-03` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-009-04` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-009-05` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-009-06` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-009-07` — Establish and maintain the post-closure regression response closure method control.
- `PCRC-009-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 10. Closure Domain — Post-Closure Regression Response Closure Decision

**Control family:** `PCRC-010`

The Post-Closure Regression Response Closure Decision domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-010-01` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-010-02` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-010-03` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-010-04` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-010-05` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-010-06` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-010-07` — Establish and maintain the post-closure regression response closure decision control.
- `PCRC-010-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 11. Closure Domain — Post-Closure Regression Response Closure Accountability

**Control family:** `PCRC-011`

The Post-Closure Regression Response Closure Accountability domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-011-01` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-011-02` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-011-03` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-011-04` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-011-05` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-011-06` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-011-07` — Establish and maintain the post-closure regression response closure accountability control.
- `PCRC-011-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 12. Closure Domain — Post-Closure Regression Response Closure Timing

**Control family:** `PCRC-012`

The Post-Closure Regression Response Closure Timing domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-012-01` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-012-02` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-012-03` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-012-04` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-012-05` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-012-06` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-012-07` — Establish and maintain the post-closure regression response closure timing control.
- `PCRC-012-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 13. Closure Domain — Security Post-Closure Regression Response Closure

**Control family:** `PCRC-013`

The Security Post-Closure Regression Response Closure domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-013-01` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-013-02` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-013-03` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-013-04` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-013-05` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-013-06` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-013-07` — Establish and maintain the security post-closure regression response closure control.
- `PCRC-013-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 14. Closure Domain — Resilience Post-Closure Regression Response Closure

**Control family:** `PCRC-014`

The Resilience Post-Closure Regression Response Closure domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-014-01` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-014-02` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-014-03` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-014-04` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-014-05` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-014-06` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-014-07` — Establish and maintain the resilience post-closure regression response closure control.
- `PCRC-014-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 15. Closure Domain — Compliance Post-Closure Regression Response Closure

**Control family:** `PCRC-015`

The Compliance Post-Closure Regression Response Closure domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-015-01` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-015-02` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-015-03` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-015-04` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-015-05` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-015-06` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-015-07` — Establish and maintain the compliance post-closure regression response closure control.
- `PCRC-015-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 16. Closure Domain — Data Post-Closure Regression Response Closure

**Control family:** `PCRC-016`

The Data Post-Closure Regression Response Closure domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-016-01` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-016-02` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-016-03` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-016-04` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-016-05` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-016-06` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-016-07` — Establish and maintain the data post-closure regression response closure control.
- `PCRC-016-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 17. Closure Domain — AI and Agent Post-Closure Regression Response Closure

**Control family:** `PCRC-017`

The AI and Agent Post-Closure Regression Response Closure domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-017-01` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-017-02` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-017-03` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-017-04` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-017-05` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-017-06` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-017-07` — Establish and maintain the ai and agent post-closure regression response closure control.
- `PCRC-017-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 18. Closure Domain — Post-Closure Regression Response Closure Failure

**Control family:** `PCRC-018`

The Post-Closure Regression Response Closure Failure domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-018-01` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-018-02` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-018-03` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-018-04` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-018-05` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-018-06` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-018-07` — Establish and maintain the post-closure regression response closure failure control.
- `PCRC-018-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 19. Closure Domain — Post-Closure Regression Response Closure Independence

**Control family:** `PCRC-019`

The Post-Closure Regression Response Closure Independence domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-019-01` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-019-02` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-019-03` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-019-04` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-019-05` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-019-06` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-019-07` — Establish and maintain the post-closure regression response closure independence control.
- `PCRC-019-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## 20. Closure Domain — Post-Closure Regression Response Closure Review and Learning

**Control family:** `PCRC-020`

The Post-Closure Regression Response Closure Review and Learning domain establishes governed mandatory closure-determination requirements.

### Required controls
- `PCRC-020-01` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-01-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-020-02` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-02-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-020-03` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-03-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-020-04` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-04-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-020-05` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-05-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-020-06` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-06-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.
- `PCRC-020-07` — Establish and maintain the post-closure regression response closure review and learning control.
- `PCRC-020-07-E` — Preserve resolution, criteria, records, obligations, residual risk, monitoring, reopening, retention, acceptance, transition and evidence traceability.

```text
RESOLVE → QUALIFY → ACCEPT → CLOSE → MONITOR → REOPEN IF REQUIRED
```

## Post-Closure Regression Response Closure Structure

| Element | Required definition |
|---|---|
| Resolution | Valid resolved state |
| Criteria | Closure criteria |
| Records | Complete authoritative record |
| Obligations | Completed / governed obligations |
| Residual Risk | Remaining accepted exposure |
| Monitoring | Post-closure monitoring |
| Reopening | Reopening triggers |
| Retention | Record retention |
| Acceptance | Closure authority |
| Transition | Post-closure state |

## Post-Closure Regression Response Closure Objective

Ensure a resolved regression case formally leaves the active response state only after all closure criteria, records, obligations, residual-risk, acceptance, monitoring and reopening requirements have been satisfied.

## Post-Closure Regression Response Closure Definition

Closure is the governed act of formally ending the active response case while preserving all required records, residual obligations, monitoring requirements, residual risk controls and reopening authority.

## Post-Closure Regression Response Closure Scope

Scope includes case status, records, obligations, residual risk, monitoring, retention, acceptance, communication, reopening and post-closure transition.

## Post-Closure Regression Response Closure Authority

Authority shall define who may recommend, verify, accept, reject, revoke or reopen closure.

## Post-Closure Regression Response Closure Criteria

Criteria shall define resolution validity, record completeness, obligations, residual risk, monitoring, reopening, retention and authorized acceptance.
```text
RESOLVED
↓
CRITERIA MET?
↓
RECORDS COMPLETE?
↓
OBLIGATIONS COMPLETE?
↓
RESIDUAL RISK GOVERNED?
↓
MONITORING DEFINED?
↓
REOPENING DEFINED?
↓
ACCEPTANCE
↓
CLOSED
```

## Post-Closure Regression Response Closure Preconditions

Preconditions include valid resolution, sufficient evidence, complete records, defined residual risk, closure authority and post-closure monitoring requirements.

## Post-Closure Regression Response Closure Evidence

Evidence shall preserve resolution, criteria, records, obligations, residual risk, monitoring plan, reopening criteria, acceptance and closure timestamp.

## Post-Closure Regression Response Closure Method

Methods may include closure checklist, independent review, record reconciliation, residual-risk acceptance, formal approval and controlled transition.
```text
VERIFY
↓
RECONCILE
↓
ACCEPT
↓
CLOSE
↓
TRANSFER TO POST-CLOSURE MONITORING
```

## Post-Closure Regression Response Closure Decision

Decision shall determine C0, C1, C2, C3, C4, C5, C6, CX, CF or CR and the associated action.

## Post-Closure Regression Response Closure Accountability

Accountability shall remain explicit for closure criteria, evidence, residual risk, acceptance and post-closure obligations.

## Post-Closure Regression Response Closure Timing

Closure timing shall reflect evidence sufficiency, consequence, residual risk, monitoring requirements and mandatory retention or reporting obligations.

## Security Post-Closure Regression Response Closure

Security closure shall preserve incident records, evidence, residual exposure controls, access decisions, lessons learned and reopening triggers.

## Resilience Post-Closure Regression Response Closure

Resilience closure shall preserve recovery evidence, residual capacity constraints, continuity controls and follow-up monitoring.

## Compliance Post-Closure Regression Response Closure

Compliance closure shall preserve required records, reports, approvals, remediation evidence and any continuing obligations.

## Data Post-Closure Regression Response Closure

Data closure shall preserve data integrity evidence, lineage, retention, access decisions, recovery records and downstream reliance controls.

## AI and Agent Post-Closure Regression Response Closure

AI/agent closure shall preserve relevant behavior evidence, authority boundaries, tool actions, data impacts, human oversight and audit records.
```text
AI / AGENT CASE
↓
BEHAVIOR ACCEPTED
+
AUTHORITY RESTORED
+
TOOLS CONTROLLED
+
DATA IMPACT GOVERNED
+
HUMAN OVERSIGHT COMPLETE
↓
CLOSURE
↓
POST-CLOSURE MONITORING
```

## Post-Closure Regression Response Closure Failure

Failure includes unresolved condition, incomplete records, outstanding obligations, ungoverned residual risk, missing monitoring, rejected acceptance or insufficient evidence.
```text
CLOSURE FAILURE
↓
CASE REMAINS ACTIVE
↓
COMPLETE / CORRECT / ESCALATE
```

## Post-Closure Regression Response Closure Independence

Independent closure verification may be required for high-consequence cases, contested evidence, material residual risk or conflicted closure authority.

## Post-Closure Regression Response Closure Review and Learning

Reviews shall examine premature closure, missing records, weak residual-risk controls, ineffective monitoring, repeated reopening and cases where closure criteria were insufficient.

## Closure Determination Model
```text
RESOLUTION VERIFIED + ACCEPTED
↓
CLOSURE PRECONDITIONS SATISFIED?
├── NO → COMPLETE OUTSTANDING REQUIREMENTS
└── YES
     ↓
RECORDS COMPLETE?
├── NO → COMPLETE / CORRECT
└── YES
     ↓
OBLIGATIONS COMPLETE?
├── NO → COMPLETE / ESCALATE
└── YES
     ↓
RESIDUAL RISK GOVERNED?
├── NO → GOVERN / ACCEPT / MITIGATE
└── YES
     ↓
POST-CLOSURE MONITORING DEFINED?
├── NO → ESTABLISH
└── YES
     ↓
REOPENING CONDITIONS DEFINED?
├── NO → DEFINE
└── YES
     ↓
CLOSURE AUTHORITY ACCEPTS?
├── NO → REMAIN OPEN / ESCALATE
└── YES
     ↓
CLOSED
     ↓
POST-CLOSURE MONITORING ACTIVE
```

## Closure Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| C0 | Not closable / active | Continue governance |
| C1 | Preconditions pending | Complete prerequisites |
| C2 | Assessment in progress | Validate closure evidence |
| C3 | Closure ready | Obtain authorization |
| C4 | Closure authorized | Execute closure transition |
| C5 | Closed | Activate post-closure monitoring |
| C6 | Closed with controlled residual obligations | Maintain explicit obligations |
| CX | Unknown / invalid evidence | Treat as not closable |
| CF | Closure failed / rejected | Remain active / correct |
| CR | Closed case reopened | Reactivate governance |

## Closure Record
| Field | Required |
|---|---|
| Closure ID | Yes |
| Regression ID | Yes |
| Response ID | Yes |
| Resolution ID | Yes |
| Criteria | Yes |
| Records Complete | Yes |
| Obligations | Yes |
| Residual Risk | Yes |
| Monitoring Plan | Where required |
| Reopening Criteria | Yes |
| Retention | Yes |
| Acceptance Authority | Yes |
| Acceptance | Yes |
| Closure Timestamp | Yes |
| Evidence | Yes |

## Resolution Is Not Closure
Resolution establishes the underlying condition is resolved. Closure establishes that the active governance case may formally leave the active response state.
```text
RESOLVED
≠
CLOSED
```

## Closure Is Not Zero Risk
A closed case may retain governed residual risk and continuing monitoring obligations.
```text
CLOSED
≠
ZERO RISK
```

## Record Completeness
Closure shall require authoritative records to be complete, internally consistent, traceable and retained according to applicable requirements.

## Outstanding Obligations
Obligations that continue after closure shall be explicitly identified, assigned, timed and governed.

## Residual Risk
Residual risk shall be identified and accepted by the appropriate authority where acceptance is required. Closure shall not conceal material residual exposure.

## Post-Closure Monitoring
Where required, monitoring shall be defined before closure, including owner, measures, frequency, thresholds, evidence and escalation.

## Reopening Conditions
Reopening conditions shall be explicit before closure where material, including recurrence, threshold breach, new evidence, control degradation or consequence escalation.
```text
CLOSED
↓
MONITOR
↓
TRIGGER?
├── NO → REMAIN CLOSED
└── YES → REOPEN
```

## Retention
Closure shall preserve the authoritative record for the required retention period and shall not destroy evidence necessary for later verification or reopening.

## Communication
Where closure communication is mandatory, the required recipients and acknowledgement requirements shall remain governed by the applicable notification architecture.

## Closure Revocation
A closed case may be reopened when defined conditions occur. Reopening shall preserve the prior closure record and establish the new active state.

## AI and Agent Closure
AI/agent systems shall not independently declare material governance cases closed unless the architecture explicitly authorizes such action and all human governance requirements are satisfied.

## Relationship to Post-Closure Monitoring
RG-121 is the transition point from active response governance into controlled post-closure monitoring.
```text
ACTIVE RESPONSE
↓
RESOLUTION
↓
CLOSURE
↓
POST-CLOSURE MONITORING
↓
REGRESSION DETECTION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure regression response-closure layer beneath resolution and above post-closure monitoring, reacceptance and reliance restoration. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Closure Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → MANDATORY CLOSURE DETERMINATION → POST-CLOSURE MONITORING → REACCEPTANCE → RELIANCE RESTORATION → REGRESSION DETECTION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION DETERMINATION → AUTHORITY TRANSFER DETERMINATION → RESPONSE EXECUTION DETERMINATION → EFFECTIVENESS DETERMINATION → RESOLUTION DETERMINATION → CLOSURE DETERMINATION → REOPENING
```

## Complete Closure Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ENTER POST-CLOSURE MONITORING → DETECT REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → ASSESS EFFECTIVENESS → DETERMINE RESOLUTION → DETERMINE CLOSURE → REOPEN / CONTINUE MONITORING AS REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-122` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Response Post-Closure Monitoring Activation Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION CASE TO SATISFY EXPLICIT, EVIDENCED AND AUTHORITY-ACCEPTED CLOSURE CRITERIA BEFORE LEAVING THE ACTIVE RESPONSE STATE, WHILE PRESERVING RESIDUAL-RISK GOVERNANCE, RECORD RETENTION, POST-CLOSURE MONITORING AND REOPENING CONDITIONS, SO THAT CLOSURE DOES NOT BECOME LOSS OF CONTROL OR LOSS OF TRACEABILITY.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-CLOSURE-DETERMINATION-01

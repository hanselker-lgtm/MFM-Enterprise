# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-RESOLUTION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-120`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-120` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-RESOLUTION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Response Resolution Determination |
| Parent | EA-IMETA-PC-RG-119 — Mandatory Post-Closure Regression Response Effectiveness Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory resolution-determination layer that determines whether the underlying post-closure regression condition and its material consequences have been sufficiently controlled, whether required controls and obligations have been restored, and whether the condition may move from active response into a governed resolved state.

## Core Principle
Effectiveness establishes that the response achieved its required outcome. Resolution establishes that the governed condition itself has reached an explicitly defined, evidenced and accepted resolved state. A response may be effective without the condition being fully resolved, and resolution shall never be inferred solely from response completion or effectiveness.

```text
RESPONSE EFFECTIVE?
├── NO / UNKNOWN → CONTINUE / ADJUST / ESCALATE
└── YES
     ↓
UNDERLYING CONDITION CONTROLLED?
├── NO → CONTINUE / REOPEN RESPONSE
└── YES
     ↓
CONSEQUENCE ACCEPTABLY REDUCED?
├── NO → CONTINUE / ESCALATE
└── YES
     ↓
REQUIRED CONTROLS RESTORED?
├── NO → RESTORE / COMPENSATE / ESCALATE
└── YES
     ↓
OBLIGATIONS SATISFIED?
├── NO → COMPLETE REQUIRED ACTIONS
└── YES
     ↓
RESOLUTION CRITERIA SATISFIED?
├── NO → CONTINUE GOVERNANCE
└── YES
     ↓
AUTHORIZED RESOLUTION ACCEPTED
     ↓
RESOLVED STATE ENTERED
```

## Resolution Quality Test
```text
VALID RESOLUTION OBJECTIVE
+
EFFECTIVE RESPONSE
+
UNDERLYING CONDITION CONTROLLED
+
RESIDUAL CONSEQUENCE WITHIN ACCEPTED LIMITS
+
REQUIRED CONTROLS RESTORED OR COMPENSATED
+
MANDATORY OBLIGATIONS SATISFIED
+
SUFFICIENT EVIDENCE
+
AUTHORIZED ACCEPTANCE
+
SUSTAINABILITY WHERE REQUIRED
=
VALID GOVERNED RESOLUTION DETERMINATION
```

## Effectiveness vs Resolution vs Closure
```text
EFFECTIVENESS
→ RESPONSE ACHIEVED ITS REQUIRED OUTCOME

RESOLUTION
→ UNDERLYING GOVERNED CONDITION REACHED REQUIRED RESOLVED STATE

CLOSURE
→ CASE / GOVERNANCE PROCESS IS FORMALLY CLOSED UNDER ITS CLOSURE CRITERIA
```

## Resolution States
```text
L0 — NOT RESOLVED / ACTIVE
L1 — RESOLUTION PRECONDITIONS PENDING
L2 — RESOLUTION ASSESSMENT IN PROGRESS
L3 — CONDITION CONTROLLED / RESOLUTION PENDING ACCEPTANCE
L4 — RESOLVED
L5 — RESOLVED WITH CONTROLLED RESIDUAL CONDITION
L6 — RESOLUTION VERIFIED AND ACCEPTED
LX — UNKNOWN / INVALID RESOLUTION EVIDENCE
LF — RESOLUTION FAILED
LR — RESOLUTION REVOKED / REOPENED
```

## Resolution Dimensions
| Dimension | Required determination |
|---|---|
| Condition | Underlying regression state |
| Objective | Required resolved outcome |
| Criteria | Resolution acceptance criteria |
| Consequence | Residual consequence |
| Controls | Restored / compensated controls |
| Obligations | Mandatory duties / commitments |
| Evidence | Resolution evidence |
| Acceptance | Authorized acceptance |
| Sustainability | Persistence requirement |
| Residual Risk | Remaining accepted exposure |
| Reopening | Conditions for reversal |

## Resolution Invariants

```text
RESOLUTION SHALL BE DISTINCT FROM RESPONSE EFFECTIVENESS
```

```text
RESOLUTION SHALL BE BASED ON THE UNDERLYING GOVERNED CONDITION, NOT ONLY ON ACTION COMPLETION
```

```text
RESOLUTION CRITERIA SHALL BE EXPLICIT
```

```text
MATERIAL RESIDUAL CONSEQUENCE SHALL BE IDENTIFIED AND GOVERNED
```

```text
REQUIRED CONTROLS SHALL BE RESTORED OR AN EXPLICITLY AUTHORIZED COMPENSATING CONTROL SHALL EXIST
```

```text
MANDATORY OBLIGATIONS SHALL BE SATISFIED BEFORE RESOLUTION WHERE APPLICABLE
```

```text
UNKNOWN OR INSUFFICIENT EVIDENCE SHALL NOT BE TREATED AS RESOLVED
```

```text
PARTIAL OR CONTROLLED RESIDUAL CONDITIONS SHALL NOT BE MISREPRESENTED AS FULL RESOLUTION
```

```text
RESOLUTION ACCEPTANCE SHALL BE PERFORMED BY THE REQUIRED AUTHORITY
```

```text
SUSTAINABILITY SHALL BE REQUIRED WHERE A TRANSIENT STATE IS INSUFFICIENT
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE RESOLUTION SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT RESOLUTION SHALL INCLUDE RELEVANT BEHAVIOR, AUTHORITY, TOOL, DATA AND OVERSIGHT CONDITIONS
```

```text
RESOLUTION SHALL REMAIN TRACEABLE TO THE REGRESSION, CONSEQUENCE, RESPONSE AND EFFECTIVENESS DETERMINATIONS
```

```text
RESOLUTION SHALL NOT AUTOMATICALLY CONSTITUTE FORMAL CASE CLOSURE
```

```text
RESOLUTION MAY BE REVOKED OR REOPENED WHEN NEW EVIDENCE INVALIDATES THE DETERMINATION
```

```text
RESOLUTION CONTROLS SHALL BE REVIEWED AFTER PREMATURE, FALSE OR REVERSED RESOLUTIONS
```

## 1. Resolution Domain — Post-Closure Regression Response Resolution Governance

**Control family:** `PCR-001`

The Post-Closure Regression Response Resolution Governance domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-001-01` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-001-02` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-001-03` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-001-04` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-001-05` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-001-06` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-001-07` — Establish and maintain the post-closure regression response resolution governance control.
- `PCR-001-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 2. Resolution Domain — Post-Closure Regression Response Resolution Objective

**Control family:** `PCR-002`

The Post-Closure Regression Response Resolution Objective domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-002-01` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-002-02` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-002-03` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-002-04` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-002-05` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-002-06` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-002-07` — Establish and maintain the post-closure regression response resolution objective control.
- `PCR-002-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 3. Resolution Domain — Post-Closure Regression Response Resolution Definition

**Control family:** `PCR-003`

The Post-Closure Regression Response Resolution Definition domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-003-01` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-003-02` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-003-03` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-003-04` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-003-05` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-003-06` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-003-07` — Establish and maintain the post-closure regression response resolution definition control.
- `PCR-003-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 4. Resolution Domain — Post-Closure Regression Response Resolution Scope

**Control family:** `PCR-004`

The Post-Closure Regression Response Resolution Scope domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-004-01` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-004-02` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-004-03` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-004-04` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-004-05` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-004-06` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-004-07` — Establish and maintain the post-closure regression response resolution scope control.
- `PCR-004-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 5. Resolution Domain — Post-Closure Regression Response Resolution Authority

**Control family:** `PCR-005`

The Post-Closure Regression Response Resolution Authority domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-005-01` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-005-02` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-005-03` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-005-04` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-005-05` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-005-06` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-005-07` — Establish and maintain the post-closure regression response resolution authority control.
- `PCR-005-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 6. Resolution Domain — Post-Closure Regression Response Resolution Criteria

**Control family:** `PCR-006`

The Post-Closure Regression Response Resolution Criteria domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-006-01` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-006-02` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-006-03` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-006-04` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-006-05` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-006-06` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-006-07` — Establish and maintain the post-closure regression response resolution criteria control.
- `PCR-006-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 7. Resolution Domain — Post-Closure Regression Response Resolution Preconditions

**Control family:** `PCR-007`

The Post-Closure Regression Response Resolution Preconditions domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-007-01` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-007-02` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-007-03` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-007-04` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-007-05` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-007-06` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-007-07` — Establish and maintain the post-closure regression response resolution preconditions control.
- `PCR-007-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 8. Resolution Domain — Post-Closure Regression Response Resolution Evidence

**Control family:** `PCR-008`

The Post-Closure Regression Response Resolution Evidence domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-008-01` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-008-02` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-008-03` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-008-04` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-008-05` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-008-06` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-008-07` — Establish and maintain the post-closure regression response resolution evidence control.
- `PCR-008-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 9. Resolution Domain — Post-Closure Regression Response Resolution Method

**Control family:** `PCR-009`

The Post-Closure Regression Response Resolution Method domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-009-01` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-009-02` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-009-03` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-009-04` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-009-05` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-009-06` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-009-07` — Establish and maintain the post-closure regression response resolution method control.
- `PCR-009-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 10. Resolution Domain — Post-Closure Regression Response Resolution Decision

**Control family:** `PCR-010`

The Post-Closure Regression Response Resolution Decision domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-010-01` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-010-02` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-010-03` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-010-04` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-010-05` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-010-06` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-010-07` — Establish and maintain the post-closure regression response resolution decision control.
- `PCR-010-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 11. Resolution Domain — Post-Closure Regression Response Resolution Accountability

**Control family:** `PCR-011`

The Post-Closure Regression Response Resolution Accountability domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-011-01` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-011-02` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-011-03` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-011-04` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-011-05` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-011-06` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-011-07` — Establish and maintain the post-closure regression response resolution accountability control.
- `PCR-011-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 12. Resolution Domain — Post-Closure Regression Response Resolution Timing

**Control family:** `PCR-012`

The Post-Closure Regression Response Resolution Timing domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-012-01` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-012-02` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-012-03` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-012-04` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-012-05` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-012-06` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-012-07` — Establish and maintain the post-closure regression response resolution timing control.
- `PCR-012-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 13. Resolution Domain — Security Post-Closure Regression Response Resolution

**Control family:** `PCR-013`

The Security Post-Closure Regression Response Resolution domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-013-01` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-013-02` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-013-03` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-013-04` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-013-05` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-013-06` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-013-07` — Establish and maintain the security post-closure regression response resolution control.
- `PCR-013-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 14. Resolution Domain — Resilience Post-Closure Regression Response Resolution

**Control family:** `PCR-014`

The Resilience Post-Closure Regression Response Resolution domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-014-01` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-014-02` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-014-03` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-014-04` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-014-05` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-014-06` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-014-07` — Establish and maintain the resilience post-closure regression response resolution control.
- `PCR-014-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 15. Resolution Domain — Compliance Post-Closure Regression Response Resolution

**Control family:** `PCR-015`

The Compliance Post-Closure Regression Response Resolution domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-015-01` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-015-02` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-015-03` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-015-04` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-015-05` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-015-06` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-015-07` — Establish and maintain the compliance post-closure regression response resolution control.
- `PCR-015-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 16. Resolution Domain — Data Post-Closure Regression Response Resolution

**Control family:** `PCR-016`

The Data Post-Closure Regression Response Resolution domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-016-01` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-016-02` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-016-03` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-016-04` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-016-05` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-016-06` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-016-07` — Establish and maintain the data post-closure regression response resolution control.
- `PCR-016-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 17. Resolution Domain — AI and Agent Post-Closure Regression Response Resolution

**Control family:** `PCR-017`

The AI and Agent Post-Closure Regression Response Resolution domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-017-01` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-017-02` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-017-03` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-017-04` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-017-05` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-017-06` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-017-07` — Establish and maintain the ai and agent post-closure regression response resolution control.
- `PCR-017-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 18. Resolution Domain — Post-Closure Regression Response Resolution Failure

**Control family:** `PCR-018`

The Post-Closure Regression Response Resolution Failure domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-018-01` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-018-02` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-018-03` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-018-04` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-018-05` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-018-06` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-018-07` — Establish and maintain the post-closure regression response resolution failure control.
- `PCR-018-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 19. Resolution Domain — Post-Closure Regression Response Resolution Independence

**Control family:** `PCR-019`

The Post-Closure Regression Response Resolution Independence domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-019-01` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-019-02` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-019-03` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-019-04` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-019-05` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-019-06` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-019-07` — Establish and maintain the post-closure regression response resolution independence control.
- `PCR-019-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## 20. Resolution Domain — Post-Closure Regression Response Resolution Review and Learning

**Control family:** `PCR-020`

The Post-Closure Regression Response Resolution Review and Learning domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCR-020-01` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-01-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-020-02` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-02-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-020-03` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-03-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-020-04` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-04-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-020-05` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-05-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-020-06` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-06-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.
- `PCR-020-07` — Establish and maintain the post-closure regression response resolution review and learning control.
- `PCR-020-07-E` — Preserve condition, objective, criteria, consequence, control state, obligations, evidence, acceptance, sustainability and reopening traceability.

```text
CONTROL → VERIFY → ACCEPT → RESOLVE → SUSTAIN → REOPEN IF REQUIRED
```

## Post-Closure Regression Response Resolution Structure

| Element | Required definition |
|---|---|
| Condition | Underlying regression condition |
| Objective | Required resolved outcome |
| Criteria | Resolution criteria |
| Consequence | Residual consequence |
| Controls | Restored / compensating controls |
| Obligations | Mandatory duties |
| Evidence | Resolution evidence |
| Acceptance | Required authority acceptance |
| Sustainability | Persistence requirement |
| Reopening | Reversal criteria |

## Post-Closure Regression Response Resolution Objective

Determine whether the underlying regression condition has reached a sufficiently controlled and governed state that satisfies all applicable resolution criteria and may proceed toward formal closure.

## Post-Closure Regression Response Resolution Definition

Resolution is the evidence-based determination that the underlying governed regression condition has been brought into the required resolved state, including applicable consequence, control, obligation and acceptance requirements.

## Post-Closure Regression Response Resolution Scope

Scope includes the underlying condition, residual consequence, control restoration, compensating controls, mandatory obligations, acceptance, sustainability and reopening conditions.

## Post-Closure Regression Response Resolution Authority

Authority shall define who may determine, independently verify, accept, reject, revoke or reopen a resolution.

## Post-Closure Regression Response Resolution Criteria

Criteria shall define the required condition, residual consequence limits, restored controls, obligations, evidence, acceptance and sustainability.
```text
EFFECTIVE RESPONSE
↓
CONDITION CONTROLLED?
↓
CONSEQUENCE ACCEPTABLE?
↓
CONTROLS RESTORED?
↓
OBLIGATIONS SATISFIED?
↓
CRITERIA MET?
↓
AUTHORIZED ACCEPTANCE
↓
RESOLVED
```

## Post-Closure Regression Response Resolution Preconditions

Preconditions include effectiveness determination, sufficient evidence, defined resolution criteria, consequence assessment, control assessment and appropriate authority.

## Post-Closure Regression Response Resolution Evidence

Evidence shall preserve condition state, criteria, measurements, consequence, control state, obligations, acceptance, sustainability and reopening basis.

## Post-Closure Regression Response Resolution Method

Methods may include condition verification, control testing, residual consequence assessment, compliance verification, independent assurance and sustained observation.
```text
CONDITION
↓
VERIFY
↓
ASSESS CONSEQUENCE
↓
ASSESS CONTROLS
↓
VERIFY OBLIGATIONS
↓
ACCEPT
↓
RESOLVE
```

## Post-Closure Regression Response Resolution Decision

Decision shall determine L0, L1, L2, L3, L4, L5, L6, LX, LF or LR and the associated continuation, acceptance, closure or reopening action.

## Post-Closure Regression Response Resolution Accountability

Accountability shall remain explicit for resolution criteria, evidence sufficiency, residual consequence, acceptance and reopening decisions.

## Post-Closure Regression Response Resolution Timing

Resolution shall be determined when evidence is sufficient and shall be reassessed where sustainability or delayed consequence requires continued observation.

## Security Post-Closure Regression Response Resolution

Security resolution shall consider residual exposure, restored controls, access state, evidence integrity and the absence or governance of remaining attack paths.

## Resilience Post-Closure Regression Response Resolution

Resilience resolution shall consider restored capability, fallback readiness, redundancy, recovery capacity and sustained operational stability.

## Compliance Post-Closure Regression Response Resolution

Compliance resolution shall consider completed obligations, required reporting, approvals, remediation evidence and formal acceptance where applicable.

## Data Post-Closure Regression Response Resolution

Data resolution shall consider integrity, confidentiality, availability, quality, lineage, recovery and downstream reliance impacts.

## AI and Agent Post-Closure Regression Response Resolution

AI/agent resolution shall assess whether the underlying behavioral, authority, tool, data and oversight conditions are restored to the required governed state.
```text
AI / AGENT CONDITION
↓
BEHAVIOR CONTROLLED
+
AUTHORITY BOUNDARY RESTORED
+
TOOLS CONTROLLED
+
DATA CONDITION ACCEPTABLE
+
HUMAN OVERSIGHT RESTORED
↓
RESOLUTION
```

## Post-Closure Regression Response Resolution Failure

Failure includes unresolved condition, excessive residual consequence, missing controls, unsatisfied obligations, insufficient evidence, rejected acceptance or recurrence.
```text
RESOLUTION FAILURE
↓
MATERIAL CONDITION REMAINS?
├── YES → CONTINUE / ADJUST / ESCALATE / REOPEN
└── NO → REASSESS EVIDENCE / CRITERIA
```

## Post-Closure Regression Response Resolution Independence

Independent resolution verification may be required for high-consequence conditions, contested evidence, significant residual risk or conflicted acceptance.

## Post-Closure Regression Response Resolution Review and Learning

Reviews shall examine premature resolution, false resolution, weak criteria, residual consequence, recurring conditions and cases where closure followed an invalid resolution.

## Resolution Determination Model
```text
RESPONSE EFFECTIVE?
├── NO / UNKNOWN → CONTINUE / ADJUST / ESCALATE
└── YES
     ↓
UNDERLYING CONDITION CONTROLLED?
├── NO → CONTINUE / REOPEN RESPONSE
└── YES
     ↓
CONSEQUENCE WITHIN ACCEPTED LIMITS?
├── NO → CONTINUE / ESCALATE
└── YES
     ↓
REQUIRED CONTROLS RESTORED?
├── NO → RESTORE / COMPENSATE / ESCALATE
└── YES
     ↓
MANDATORY OBLIGATIONS SATISFIED?
├── NO → COMPLETE REQUIRED ACTIONS
└── YES
     ↓
RESOLUTION CRITERIA SATISFIED?
├── NO → CONTINUE GOVERNANCE
└── YES
     ↓
AUTHORIZED ACCEPTANCE
     ↓
RESOLUTION VERIFIED
```

## Resolution Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| L0 | Not resolved / active | Continue response / monitoring |
| L1 | Preconditions pending | Complete prerequisites |
| L2 | Assessment in progress | Gather / validate evidence |
| L3 | Condition controlled; acceptance pending | Obtain required acceptance |
| L4 | Resolved | Proceed to governed transition |
| L5 | Resolved with controlled residual condition | Maintain explicit residual governance |
| L6 | Resolution verified and accepted | Eligible for next governed state |
| LX | Unknown / invalid evidence | Treat as unresolved |
| LF | Resolution failed | Continue / escalate / reopen |
| LR | Resolution revoked / reopened | Reactivate governance |

## Resolution Record
| Field | Required |
|---|---|
| Resolution ID | Yes |
| Regression ID | Yes |
| Response ID | Yes |
| Effectiveness ID | Yes |
| Condition | Yes |
| Objective | Yes |
| Criteria | Yes |
| Residual Consequence | Yes |
| Control State | Yes |
| Obligations | Yes where applicable |
| Evidence | Yes |
| Acceptance Authority | Yes |
| Acceptance | Yes where required |
| Sustainability | Where applicable |
| Reopening Criteria | Yes |
| Decision | Yes |

## Effectiveness Is Not Resolution
An effective response establishes that the response achieved its required outcome. Resolution additionally establishes that the underlying governed condition has reached the required resolved state.
```text
EFFECTIVE
≠
RESOLVED
```

## Resolution Is Not Closure
A resolved condition does not automatically mean that the formal governance case is closed. Closure remains a separate governed determination.
```text
RESOLVED
≠
CLOSED
```

## Residual Consequence
Residual consequence shall be explicitly identified, measured where practicable and accepted only by the authority authorized to accept it.

## Compensating Controls
Where original controls cannot immediately be restored, a compensating control may support resolution only where explicitly authorized, sufficiently effective and appropriately governed.

## Mandatory Obligations
Resolution shall not be declared where mandatory obligations remain outstanding unless the governing framework explicitly permits controlled residual status.

## Sustainability
Where the resolved state can regress quickly, sustained observation shall be required before the state is treated as stable.
```text
RESOLVED?
↓
SUSTAINED?
├── NO → L5 / CONTINUE MONITORING
└── YES → L6
```

## Acceptance
Where formal acceptance is required, resolution shall not be considered fully accepted until the designated authority records acceptance.

## Unknown Evidence
Unknown, incomplete or contradictory evidence shall not support a positive resolution determination.
```text
UNKNOWN
≠
RESOLVED
```

## Resolution Revocation
If new evidence demonstrates that the resolved state was incorrect or has materially degraded, resolution shall be revoked or reopened according to the defined reopening criteria.

## AI and Agent Resolution
AI/agent resolution shall not rely solely on self-assessment. The governed external condition and required human oversight state must be verified where applicable.

## Relationship to Closure
RG-120 establishes the resolved state. The next layer determines whether the case may formally transition into closure.
```text
EFFECTIVENESS
↓
RESOLUTION
↓
CLOSURE
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure regression response-resolution layer beneath effectiveness and above closure, reacceptance and reliance restoration. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Resolution Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → MANDATORY RESOLUTION DETERMINATION → CLOSURE → REACCEPTANCE → RELIANCE RESTORATION → MONITORING CONTINUITY → REGRESSION DETECTION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION DETERMINATION → AUTHORITY TRANSFER DETERMINATION → RESPONSE EXECUTION DETERMINATION → EFFECTIVENESS DETERMINATION → RESOLUTION DETERMINATION → REOPENING
```

## Complete Resolution Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → REACCEPT → RESTORE RELIANCE → MAINTAIN MONITORING → DETECT REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → ASSESS EFFECTIVENESS → DETERMINE RESOLUTION → CLOSE / CONTINUE / REOPEN AS REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-121` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Response Closure Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION TO REACH AN EXPLICIT, EVIDENCED AND AUTHORITY-ACCEPTED RESOLUTION STATE BEFORE IT MAY PROCEED TOWARD FORMAL CLOSURE, WITH THE UNDERLYING CONDITION, RESIDUAL CONSEQUENCE, CONTROL RESTORATION, MANDATORY OBLIGATIONS, SUSTAINABILITY AND REOPENING CONDITIONS DISTINCTLY DETERMINED, SO THAT RESPONSE EFFECTIVENESS CANNOT BE MISTAKEN FOR RESOLUTION AND RESOLUTION CANNOT BE MISTAKEN FOR CLOSURE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-RESOLUTION-DETERMINATION-01

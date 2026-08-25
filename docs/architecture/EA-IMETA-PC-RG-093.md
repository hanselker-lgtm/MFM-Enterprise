# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-RESOLUTION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-093`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-093` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-RESOLUTION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Resolution Determination |
| Parent | EA-IMETA-PC-RG-092 — Mandatory Post-Closure Effectiveness Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory resolution-determination layer that decides whether an effectively addressed post-closure condition is sufficiently resolved to proceed toward closure, continued monitoring, revalidation, reliance restoration or reopening.

## Core Principle
Effectiveness answers whether the response achieved the required outcome. Resolution answers whether the underlying condition is sufficiently addressed that the response lifecycle can leave active remediation and enter a governed resolution state. Resolution shall therefore consider effectiveness, residual deviation, dependencies, sustainability, evidence and outstanding obligations.

```text
EFFECTIVENESS DETERMINED
      ↓
UNDERLYING CONDITION SUFFICIENTLY RESOLVED?
├── NO → CONTINUE / MODIFY / REOPEN
└── YES
     ↓
RESIDUAL OBLIGATIONS / DEVIATIONS?
├── MATERIAL → CONTINUE GOVERNED RESPONSE
└── NONE / ACCEPTABLE
     ↓
DEPENDENCIES + SUSTAINABILITY SATISFIED?
├── NO → CONTINUE MONITORING / REVALIDATE
└── YES
     ↓
RESOLUTION DETERMINED
     ↓
CLOSURE / POST-CLOSURE TRANSITION PATH
```

## Resolution Quality Test
```text
VALID EFFECTIVENESS DETERMINATION
+
UNDERLYING CONDITION ADDRESSED
+
RESIDUAL DEVIATION ASSESSED
+
OUTSTANDING OBLIGATIONS IDENTIFIED
+
DEPENDENCIES VERIFIED
+
SUSTAINABILITY ACCEPTABLE
+
AUTHORIZED RESOLUTION DECISION
=
VALID GOVERNED RESOLUTION DETERMINATION
```

## Effectiveness vs Resolution vs Closure
```text
EFFECTIVENESS
→ DID THE RESPONSE ACHIEVE THE REQUIRED OUTCOME?

RESOLUTION
→ IS THE UNDERLYING CONDITION SUFFICIENTLY ADDRESSED?

CLOSURE
→ MAY THE ACTIVE LIFECYCLE BE FORMALLY ENDED?
```

## Resolution State Model
```text
NOT READY
UNDER ASSESSMENT
EFFECTIVE BUT UNRESOLVED
PARTIALLY RESOLVED
RESOLVED
RESOLVED WITH ACCEPTED RESIDUAL
RESOLUTION REJECTED
REOPENED
PENDING REVALIDATION
PENDING RELIANCE RESTORATION
READY FOR CLOSURE
```

## Resolution Invariants

```text
RESOLUTION SHALL BE BASED ON THE UNDERLYING CONDITION, NOT ONLY THE RESPONSE ACTION
```

```text
EFFECTIVENESS SHALL BE CONSIDERED BUT SHALL NOT AUTOMATICALLY EQUAL RESOLUTION
```

```text
RESIDUAL DEVIATION SHALL BE EXPLICITLY ASSESSED
```

```text
OUTSTANDING ACTIONS AND OBLIGATIONS SHALL BE IDENTIFIED
```

```text
DEPENDENCIES SHALL BE ASSESSED WHERE THEY CAN PREVENT RESOLUTION
```

```text
SUSTAINABILITY SHALL BE CONSIDERED WHERE TEMPORARY RECOVERY IS INSUFFICIENT
```

```text
RESOLUTION SHALL BE ATTRIBUTABLE TO AN AUTHORIZED DECISION
```

```text
RESOLVED WITH ACCEPTED RESIDUAL SHALL REMAIN TRACEABLE TO THE ACCEPTANCE AUTHORITY AND CRITERIA
```

```text
RESOLUTION SHALL NOT AUTOMATICALLY MEAN CLOSURE
```

```text
REOPENING SHALL REMAIN POSSIBLE WHEN NEW MATERIAL EVIDENCE INVALIDATES RESOLUTION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE CONDITIONS SHALL RECEIVE APPROPRIATE RESOLUTION RIGOR
```

```text
AI AND AGENT RESOLUTION SHALL CONSIDER OUTCOME, CONTROL BOUNDARIES AND CONTINUING GOVERNANCE OBLIGATIONS
```

```text
UNRESOLVED DEPENDENCIES SHALL PREVENT FALSE RESOLUTION
```

```text
RESOLUTION CRITERIA SHALL BE VERSIONED
```

```text
RESOLUTION HISTORY SHALL PRESERVE THE CONDITION, RESPONSE, EFFECTIVENESS AND ACCEPTANCE CHAIN
```

## 1. Resolution Domain — Post-Closure Resolution Determination Governance

**Control family:** `PCRD-001`

The Post-Closure Resolution Determination Governance domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-001-01` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-001-02` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-001-03` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-001-04` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-001-05` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-001-06` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-001-07` — Establish and maintain the post-closure resolution determination governance control.
- `PCRD-001-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 2. Resolution Domain — Post-Closure Resolution Determination Objective

**Control family:** `PCRD-002`

The Post-Closure Resolution Determination Objective domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-002-01` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-002-02` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-002-03` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-002-04` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-002-05` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-002-06` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-002-07` — Establish and maintain the post-closure resolution determination objective control.
- `PCRD-002-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 3. Resolution Domain — Post-Closure Resolution Determination Definition

**Control family:** `PCRD-003`

The Post-Closure Resolution Determination Definition domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-003-01` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-003-02` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-003-03` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-003-04` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-003-05` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-003-06` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-003-07` — Establish and maintain the post-closure resolution determination definition control.
- `PCRD-003-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 4. Resolution Domain — Post-Closure Resolution Determination Scope

**Control family:** `PCRD-004`

The Post-Closure Resolution Determination Scope domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-004-01` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-004-02` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-004-03` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-004-04` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-004-05` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-004-06` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-004-07` — Establish and maintain the post-closure resolution determination scope control.
- `PCRD-004-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 5. Resolution Domain — Post-Closure Resolution Determination Authority

**Control family:** `PCRD-005`

The Post-Closure Resolution Determination Authority domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-005-01` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-005-02` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-005-03` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-005-04` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-005-05` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-005-06` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-005-07` — Establish and maintain the post-closure resolution determination authority control.
- `PCRD-005-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 6. Resolution Domain — Post-Closure Resolution Determination Criteria

**Control family:** `PCRD-006`

The Post-Closure Resolution Determination Criteria domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-006-01` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-006-02` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-006-03` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-006-04` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-006-05` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-006-06` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-006-07` — Establish and maintain the post-closure resolution determination criteria control.
- `PCRD-006-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 7. Resolution Domain — Post-Closure Resolution Determination Preconditions

**Control family:** `PCRD-007`

The Post-Closure Resolution Determination Preconditions domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-007-01` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-007-02` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-007-03` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-007-04` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-007-05` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-007-06` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-007-07` — Establish and maintain the post-closure resolution determination preconditions control.
- `PCRD-007-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 8. Resolution Domain — Post-Closure Resolution Determination Evidence

**Control family:** `PCRD-008`

The Post-Closure Resolution Determination Evidence domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-008-01` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-008-02` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-008-03` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-008-04` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-008-05` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-008-06` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-008-07` — Establish and maintain the post-closure resolution determination evidence control.
- `PCRD-008-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 9. Resolution Domain — Post-Closure Resolution Determination Method

**Control family:** `PCRD-009`

The Post-Closure Resolution Determination Method domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-009-01` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-009-02` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-009-03` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-009-04` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-009-05` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-009-06` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-009-07` — Establish and maintain the post-closure resolution determination method control.
- `PCRD-009-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 10. Resolution Domain — Post-Closure Resolution Determination Decision

**Control family:** `PCRD-010`

The Post-Closure Resolution Determination Decision domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-010-01` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-010-02` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-010-03` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-010-04` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-010-05` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-010-06` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-010-07` — Establish and maintain the post-closure resolution determination decision control.
- `PCRD-010-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 11. Resolution Domain — Post-Closure Resolution Determination Accountability

**Control family:** `PCRD-011`

The Post-Closure Resolution Determination Accountability domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-011-01` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-011-02` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-011-03` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-011-04` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-011-05` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-011-06` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-011-07` — Establish and maintain the post-closure resolution determination accountability control.
- `PCRD-011-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 12. Resolution Domain — Post-Closure Resolution Determination Timing

**Control family:** `PCRD-012`

The Post-Closure Resolution Determination Timing domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-012-01` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-012-02` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-012-03` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-012-04` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-012-05` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-012-06` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-012-07` — Establish and maintain the post-closure resolution determination timing control.
- `PCRD-012-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 13. Resolution Domain — Security Post-Closure Resolution Determination

**Control family:** `PCRD-013`

The Security Post-Closure Resolution Determination domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-013-01` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-013-02` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-013-03` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-013-04` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-013-05` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-013-06` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-013-07` — Establish and maintain the security post-closure resolution determination control.
- `PCRD-013-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 14. Resolution Domain — Resilience Post-Closure Resolution Determination

**Control family:** `PCRD-014`

The Resilience Post-Closure Resolution Determination domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-014-01` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-014-02` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-014-03` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-014-04` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-014-05` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-014-06` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-014-07` — Establish and maintain the resilience post-closure resolution determination control.
- `PCRD-014-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 15. Resolution Domain — Compliance Post-Closure Resolution Determination

**Control family:** `PCRD-015`

The Compliance Post-Closure Resolution Determination domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-015-01` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-015-02` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-015-03` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-015-04` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-015-05` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-015-06` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-015-07` — Establish and maintain the compliance post-closure resolution determination control.
- `PCRD-015-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 16. Resolution Domain — Data Post-Closure Resolution Determination

**Control family:** `PCRD-016`

The Data Post-Closure Resolution Determination domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-016-01` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-016-02` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-016-03` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-016-04` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-016-05` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-016-06` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-016-07` — Establish and maintain the data post-closure resolution determination control.
- `PCRD-016-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 17. Resolution Domain — AI and Agent Post-Closure Resolution Determination

**Control family:** `PCRD-017`

The AI and Agent Post-Closure Resolution Determination domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-017-01` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-017-02` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-017-03` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-017-04` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-017-05` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-017-06` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-017-07` — Establish and maintain the ai and agent post-closure resolution determination control.
- `PCRD-017-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 18. Resolution Domain — Post-Closure Resolution Determination Failure

**Control family:** `PCRD-018`

The Post-Closure Resolution Determination Failure domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-018-01` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-018-02` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-018-03` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-018-04` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-018-05` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-018-06` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-018-07` — Establish and maintain the post-closure resolution determination failure control.
- `PCRD-018-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 19. Resolution Domain — Post-Closure Resolution Determination Independence

**Control family:** `PCRD-019`

The Post-Closure Resolution Determination Independence domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-019-01` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-019-02` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-019-03` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-019-04` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-019-05` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-019-06` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-019-07` — Establish and maintain the post-closure resolution determination independence control.
- `PCRD-019-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## 20. Resolution Domain — Post-Closure Resolution Determination Review and Learning

**Control family:** `PCRD-020`

The Post-Closure Resolution Determination Review and Learning domain establishes governed mandatory resolution-determination requirements.

### Required controls
- `PCRD-020-01` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-01-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-020-02` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-02-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-020-03` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-03-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-020-04` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-04-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-020-05` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-05-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-020-06` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-06-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.
- `PCRD-020-07` — Establish and maintain the post-closure resolution determination review and learning control.
- `PCRD-020-07-E` — Preserve condition, effectiveness, residual deviation, obligations, dependencies, resolution criteria, authority and decision traceability.

```text
EFFECTIVE → ASSESS RESOLUTION → ACCEPT / CONTINUE / REOPEN
```

## Post-Closure Resolution Determination Structure

| Element | Required definition |
|---|---|
| Condition | Underlying condition |
| Response | Corrective intervention |
| Effectiveness | Outcome achievement |
| Residual Deviation | Remaining gap |
| Obligations | Outstanding requirements |
| Dependencies | Conditions affecting resolution |
| Sustainability | Durability requirement |
| Resolution Criteria | Required conditions |
| Determination | Resolution state |
| Authority | Authorized decision-maker |

## Post-Closure Resolution Determination Objective

Determine whether the underlying condition has been sufficiently addressed to leave active response execution and enter the appropriate governed resolution and lifecycle transition path.

## Post-Closure Resolution Determination Definition

Resolution determination is the authorized decision that the underlying condition is resolved, partially resolved, resolved with accepted residual, or remains unresolved.

## Post-Closure Resolution Determination Scope

Scope shall include the original condition, response scope, affected outcomes, residual deviations, dependencies, obligations, controls and downstream consequences.

## Post-Closure Resolution Determination Authority

Authority shall define who may determine resolution, accept residual conditions, require further response, authorize transition toward closure and reopen a previously resolved condition.

## Post-Closure Resolution Determination Criteria

Criteria shall address effectiveness, residual deviation, outstanding obligations, dependencies, sustainability, acceptance thresholds and required evidence.

```text
EFFECTIVE RESPONSE
↓
UNDERLYING CONDITION ADDRESSED?
├── NO → CONTINUE / REOPEN
└── YES
     ↓
MATERIAL RESIDUAL?
├── YES → RESOLUTION NOT READY / ACCEPT RESIDUAL IF AUTHORIZED
└── NO
     ↓
DEPENDENCIES SATISFIED?
├── NO → CONTINUE / REVALIDATE
└── YES
     ↓
SUSTAINABILITY ACCEPTABLE?
├── NO → MONITOR / REASSESS
└── YES → RESOLUTION DETERMINED
```

## Post-Closure Resolution Determination Preconditions

Preconditions include effectiveness determination, sufficient evidence, defined resolution criteria, residual assessment, dependency assessment and appropriate authority.

## Post-Closure Resolution Determination Evidence

Evidence shall preserve original condition, baseline, response, effectiveness, residual deviation, obligations, dependencies, criteria version, determination rationale and authority.

## Post-Closure Resolution Determination Method

Methods may include condition verification, residual gap analysis, obligation review, dependency validation, sustained observation and independent confirmation.

```text
CONDITION
↓
RESPONSE
↓
EFFECTIVENESS
↓
RESIDUAL / OBLIGATIONS / DEPENDENCIES
↓
RESOLUTION CRITERIA
↓
RESOLUTION DETERMINATION
```

## Post-Closure Resolution Determination Decision

Decision shall explicitly state resolved, partially resolved, resolved with accepted residual, unresolved, pending revalidation or reopened.

```text
RESOLUTION
├── RESOLVED → READY FOR NEXT LIFECYCLE STATE
├── ACCEPTED RESIDUAL → CONTROL + MONITOR
├── PARTIAL → CONTINUE RESPONSE
└── UNRESOLVED → REOPEN / ESCALATE
```

## Post-Closure Resolution Determination Accountability

Accountability shall remain explicit for the resolution decision, evidence sufficiency, residual acceptance and lifecycle transition recommendation.

## Post-Closure Resolution Determination Timing

Resolution timing shall reflect consequence and the time needed to verify that the underlying condition, not merely the immediate symptom, has been addressed.

## Security Post-Closure Resolution Determination

Security resolution shall confirm that the underlying exposure or control deficiency is addressed, not merely that an immediate alert has cleared.

## Resilience Post-Closure Resolution Determination

Resilience resolution shall confirm stable recovery and restored capability, including dependencies and capacity where relevant.

## Compliance Post-Closure Resolution Determination

Compliance resolution shall confirm that the underlying obligation or control deficiency is addressed and required evidence or reporting conditions are satisfied.

## Data Post-Closure Resolution Determination

Data resolution shall confirm that underlying integrity, quality, access, confidentiality, lineage, retention or authorized-use conditions are addressed.

## AI and Agent Post-Closure Resolution Determination

AI/agent resolution shall consider outcome, authority, policy, data, tool, autonomy and behavioural controls, including whether continuing governance constraints remain.

```text
AI / AGENT CONDITION
↓
OUTCOME RESTORED?
+
CONTROL BOUNDARIES RESTORED?
+
CONTINUING OBLIGATIONS SATISFIED?
↓
RESOLUTION DETERMINATION
```

## Post-Closure Resolution Determination Failure

Failure includes premature resolution, hidden residual deviation, unresolved dependency, incomplete evidence, temporary symptom removal, conflicting determinations or unauthorized residual acceptance.

```text
RESOLUTION FAILURE
↓
CONDITION ACTUALLY RESOLVED?
├── YES → CORRECT DETERMINATION RECORD
└── NO → CONTINUE / REOPEN / ESCALATE
```

## Post-Closure Resolution Determination Independence

Independent resolution validation may be required for high-consequence conditions, disputed residuals, conflicts of interest or material acceptance decisions.

## Post-Closure Resolution Determination Review and Learning

Reviews shall identify premature resolution, recurring residual conditions, weak criteria, unresolved dependencies, inappropriate residual acceptance and systemic response deficiencies.

## Resolution Determination Model
```text
EFFECTIVENESS DETERMINED
↓
UNDERLYING CONDITION ADDRESSED?
├── NO → CONTINUE / REOPEN
└── YES
     ↓
RESIDUAL DEVIATION ACCEPTABLE?
├── NO → CONTINUE / ESCALATE
└── YES
     ↓
OUTSTANDING OBLIGATIONS SATISFIED?
├── NO → CONTINUE / GOVERN
└── YES
     ↓
DEPENDENCIES SATISFIED?
├── NO → REVALIDATE / CONTINUE
└── YES
     ↓
SUSTAINABILITY ACCEPTABLE?
├── NO → MONITOR / REASSESS
└── YES
     ↓
RESOLUTION DETERMINED
↓
READY FOR CLOSURE / TRANSITION
```

## Resolution Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Not Ready | Resolution criteria not satisfied | Continue response |
| Under Assessment | Evidence / criteria being evaluated | Complete assessment |
| Effective but Unresolved | Response worked but condition remains | Continue / investigate |
| Partially Resolved | Material elements remain | Continue / modify |
| Resolved | Underlying condition sufficiently addressed | Transition |
| Resolved with Accepted Residual | Residual formally accepted | Monitor / govern residual |
| Resolution Rejected | Evidence insufficient or criteria unmet | Continue / reopen |
| Reopened | Previous resolution invalidated | Re-enter response lifecycle |
| Pending Revalidation | Further validation required | Monitor / verify |
| Pending Reliance Restoration | Resolution achieved but reliance not restored | Continue post-closure governance |
| Ready for Closure | Resolution conditions satisfied | Proceed to closure decision |

## Resolution Record
| Field | Required |
|---|---|
| Resolution ID | Yes |
| Condition ID | Yes |
| Response ID | Yes |
| Effectiveness ID | Yes |
| Resolution Criteria Version | Yes |
| Residual Deviation | Yes |
| Obligations | Yes |
| Dependencies | Yes |
| Sustainability | Where relevant |
| Determination | Yes |
| Authority | Yes |
| Rationale | Yes |
| Transition State | Yes |
| Reopening Conditions | Where applicable |

## Resolution Is Not Closure
A condition may be resolved while closure still requires additional governance decisions, documentation, revalidation, acceptance or transition controls.

```text
RESOLVED
≠
CLOSED
```

## Resolved with Accepted Residual
Residual conditions may be accepted only where explicitly authorized criteria permit them and the residual is visible, bounded, monitored and attributable to an acceptance authority.

## Outstanding Obligations
Open obligations, reporting, corrective actions, evidence requirements or control commitments may prevent resolution even when the principal technical symptom has disappeared.

## Dependencies
A condition shall not be declared resolved if a material dependency remains unresolved and can recreate or materially affect the condition.

## Sustainability
Where restoration must persist, resolution requires appropriate evidence that the condition remains controlled beyond the immediate response window.

## Symptom Removal vs Underlying Resolution
Removal of a visible symptom does not prove that the underlying cause or governed condition has been resolved.

```text
SYMPTOM CLEARED
↓
UNDERLYING CONDITION ADDRESSED?
├── YES → CONTINUE RESOLUTION ASSESSMENT
└── NO → NOT RESOLVED
```

## Reopening
New material evidence, regression, failed sustainability, hidden dependency or invalid criteria may reopen a resolved condition.

```text
RESOLVED
↓
NEW MATERIAL EVIDENCE?
├── NO → TRANSITION
└── YES
     ↓
RESOLUTION STILL VALID?
├── YES → CONTINUE
└── NO → REOPEN
```

## AI and Agent Resolution
A successful AI/agent outcome does not establish resolution if authority, policy, data, tool or autonomy controls remain degraded.

## Resolution Anti-Gaming
Resolution shall not be declared merely to close cases, improve closure metrics, reduce backlog or avoid continued monitoring.

## Relationship to Closure
RG-093 determines whether the condition is resolved. The next lifecycle layer determines whether it may be formally closed and what closure evidence and acceptance are required.

```text
EFFECTIVENESS
↓
RESOLUTION
↓
CLOSURE DETERMINATION
↓
POST-CLOSURE TRANSITION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure resolution-determination layer beneath effectiveness determination and above closure determination and post-closure transition. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, effectiveness, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Resolution Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → ASSESSMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → MANDATORY RESOLUTION DETERMINATION → CLOSURE → POST-CLOSURE TRANSITION → BASELINE → MONITORING → COMPARISON → DEVIATION DETECTION → REGRESSION → REOPENING
```

## Complete Resolution Chain
```text
BASELINE → OBSERVE → COMPARE → DETECT DEVIATION → VALIDATE → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → INITIATE RESPONSE → ESCALATE → TRANSFER AUTHORITY → EXECUTE → CONTROL → OBSERVE EFFECTS → DETERMINE EFFECTIVENESS → DETERMINE RESOLUTION → CLOSE → TRANSITION → MONITOR → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-094` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Closure Determination

## Final Principle
EA-IMETA SHALL REQUIRE THE UNDERLYING POST-CLOSURE CONDITION TO BE EXPLICITLY ASSESSED FOR RESOLUTION AFTER EFFECTIVENESS IS DETERMINED, INCLUDING RESIDUAL DEVIATION, OUTSTANDING OBLIGATIONS, DEPENDENCIES, SUSTAINABILITY AND CONTINUING GOVERNANCE CONDITIONS, SO THAT A SUCCESSFUL RESPONSE CANNOT BE MISTAKEN FOR RESOLUTION AND RESOLUTION CANNOT BE MISTAKEN FOR CLOSURE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-RESOLUTION-DETERMINATION-01

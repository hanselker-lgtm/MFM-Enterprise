# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-01

## Physical File ID
`EA-IMETA-PC-RG-060`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-060` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Resolution Verification |
| Parent | EA-IMETA-PC-RG-059 — Mandatory Escalation Resolution |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory verification layer defining how a claimed resolution is tested against current requirements, evidence, observed outcomes and boundaries before the condition may progress to revalidation, reacceptance or reliance restoration.

## Core Principle
Resolution is a governed claim about current state; verification is the controlled demonstration that the claimed state actually exists and satisfies applicable criteria. A closed action, completed remediation or management declaration shall not substitute for verification where verification is required.

```text
RESOLUTION CLAIM
      ↓
DEFINE REQUIRED CURRENT STATE
      ↓
SELECT VERIFICATION METHOD
      ↓
OBSERVE / TEST / MEASURE
      ↓
COMPARE WITH CURRENT CRITERIA
      ↓
VERIFICATION RESULT
├── VERIFIED → REVALIDATION
├── PARTIAL → COMPLETE GAPS
├── FAILED → REOPEN / REMEDIATE
└── UNKNOWN → COMPLETE EVIDENCE
```

## Verification Quality Test
```text
RESOLUTION CLAIM
+
CURRENT CRITERIA
+
APPROPRIATE METHOD
+
SUFFICIENT EVIDENCE
+
CURRENT OBSERVATION
+
BOUNDARY CHECK
+
RESIDUAL-RISK REVIEW
+
AUTHORIZED DETERMINATION
=
VALID GOVERNED RESOLUTION VERIFICATION
```

## Verification Status Model
```text
NOT READY
PLANNED
IN VERIFICATION
VERIFIED
PARTIALLY VERIFIED
FAILED
UNKNOWN
REOPENED
SUPERSEDED
```

## Verification Invariants

```text
RESOLUTION CLAIMS SHALL BE VERIFIED WHERE REQUIRED BY MATERIALITY OR GOVERNANCE
```

```text
VERIFICATION SHALL TEST CURRENT STATE, NOT ONLY ACTION COMPLETION
```

```text
CURRENT CRITERIA SHALL GOVERN THE DETERMINATION
```

```text
VERIFICATION METHOD SHALL BE APPROPRIATE TO THE CONDITION AND MATERIALITY
```

```text
EVIDENCE SHALL BE CURRENT, SUFFICIENT, ATTRIBUTABLE AND TRACEABLE
```

```text
PARTIAL VERIFICATION SHALL NOT BE PRESENTED AS FULL VERIFICATION
```

```text
UNKNOWN SHALL REMAIN DISTINCT FROM VERIFIED
```

```text
FAILED VERIFICATION SHALL BLOCK UNCONTROLLED PROGRESSION
```

```text
VERIFICATION SHALL CONSIDER CONTROL, OUTCOME AND RELEVANT BOUNDARIES
```

```text
VERIFICATION SHALL REMAIN DISTINCT FROM REVALIDATION AND REACCEPTANCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE VERIFICATION SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT VERIFICATION SHALL CHECK AUTHORITY, POLICY, TOOLS, DATA, AUTONOMY AND BEHAVIOURAL CONDITIONS
```

```text
INDEPENDENCE SHALL BE USED WHERE MATERIALITY REQUIRES IT
```

```text
VERIFICATION RECORDS SHALL REMAIN TRACEABLE THROUGH THE GOVERNANCE LIFECYCLE
```

```text
REPEATED VERIFICATION FAILURE SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Verification Domain — Resolution Verification Governance

**Control family:** `PCRV2-001`

The Resolution Verification Governance domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-001-01` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-001-02` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-001-03` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-001-04` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-001-05` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-001-06` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-001-07` — Establish and maintain the resolution verification governance control.
- `PCRV2-001-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 2. Verification Domain — Resolution Verification Objective

**Control family:** `PCRV2-002`

The Resolution Verification Objective domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-002-01` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-002-02` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-002-03` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-002-04` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-002-05` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-002-06` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-002-07` — Establish and maintain the resolution verification objective control.
- `PCRV2-002-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 3. Verification Domain — Resolution Verification Definition

**Control family:** `PCRV2-003`

The Resolution Verification Definition domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-003-01` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-003-02` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-003-03` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-003-04` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-003-05` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-003-06` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-003-07` — Establish and maintain the resolution verification definition control.
- `PCRV2-003-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 4. Verification Domain — Resolution Verification Scope

**Control family:** `PCRV2-004`

The Resolution Verification Scope domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-004-01` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-004-02` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-004-03` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-004-04` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-004-05` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-004-06` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-004-07` — Establish and maintain the resolution verification scope control.
- `PCRV2-004-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 5. Verification Domain — Resolution Verification Authority

**Control family:** `PCRV2-005`

The Resolution Verification Authority domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-005-01` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-005-02` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-005-03` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-005-04` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-005-05` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-005-06` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-005-07` — Establish and maintain the resolution verification authority control.
- `PCRV2-005-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 6. Verification Domain — Resolution Verification Criteria

**Control family:** `PCRV2-006`

The Resolution Verification Criteria domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-006-01` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-006-02` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-006-03` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-006-04` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-006-05` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-006-06` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-006-07` — Establish and maintain the resolution verification criteria control.
- `PCRV2-006-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 7. Verification Domain — Resolution Verification Preconditions

**Control family:** `PCRV2-007`

The Resolution Verification Preconditions domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-007-01` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-007-02` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-007-03` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-007-04` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-007-05` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-007-06` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-007-07` — Establish and maintain the resolution verification preconditions control.
- `PCRV2-007-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 8. Verification Domain — Resolution Verification Evidence

**Control family:** `PCRV2-008`

The Resolution Verification Evidence domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-008-01` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-008-02` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-008-03` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-008-04` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-008-05` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-008-06` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-008-07` — Establish and maintain the resolution verification evidence control.
- `PCRV2-008-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 9. Verification Domain — Resolution Verification Method

**Control family:** `PCRV2-009`

The Resolution Verification Method domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-009-01` — Establish and maintain the resolution verification method control.
- `PCRV2-009-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-009-02` — Establish and maintain the resolution verification method control.
- `PCRV2-009-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-009-03` — Establish and maintain the resolution verification method control.
- `PCRV2-009-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-009-04` — Establish and maintain the resolution verification method control.
- `PCRV2-009-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-009-05` — Establish and maintain the resolution verification method control.
- `PCRV2-009-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-009-06` — Establish and maintain the resolution verification method control.
- `PCRV2-009-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-009-07` — Establish and maintain the resolution verification method control.
- `PCRV2-009-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 10. Verification Domain — Resolution Verification Decision

**Control family:** `PCRV2-010`

The Resolution Verification Decision domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-010-01` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-010-02` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-010-03` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-010-04` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-010-05` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-010-06` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-010-07` — Establish and maintain the resolution verification decision control.
- `PCRV2-010-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 11. Verification Domain — Resolution Verification Accountability

**Control family:** `PCRV2-011`

The Resolution Verification Accountability domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-011-01` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-011-02` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-011-03` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-011-04` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-011-05` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-011-06` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-011-07` — Establish and maintain the resolution verification accountability control.
- `PCRV2-011-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 12. Verification Domain — Resolution Verification Timing

**Control family:** `PCRV2-012`

The Resolution Verification Timing domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-012-01` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-012-02` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-012-03` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-012-04` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-012-05` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-012-06` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-012-07` — Establish and maintain the resolution verification timing control.
- `PCRV2-012-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 13. Verification Domain — Security Resolution Verification

**Control family:** `PCRV2-013`

The Security Resolution Verification domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-013-01` — Establish and maintain the security resolution verification control.
- `PCRV2-013-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-013-02` — Establish and maintain the security resolution verification control.
- `PCRV2-013-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-013-03` — Establish and maintain the security resolution verification control.
- `PCRV2-013-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-013-04` — Establish and maintain the security resolution verification control.
- `PCRV2-013-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-013-05` — Establish and maintain the security resolution verification control.
- `PCRV2-013-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-013-06` — Establish and maintain the security resolution verification control.
- `PCRV2-013-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-013-07` — Establish and maintain the security resolution verification control.
- `PCRV2-013-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 14. Verification Domain — Resilience Resolution Verification

**Control family:** `PCRV2-014`

The Resilience Resolution Verification domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-014-01` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-014-02` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-014-03` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-014-04` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-014-05` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-014-06` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-014-07` — Establish and maintain the resilience resolution verification control.
- `PCRV2-014-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 15. Verification Domain — Compliance Resolution Verification

**Control family:** `PCRV2-015`

The Compliance Resolution Verification domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-015-01` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-015-02` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-015-03` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-015-04` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-015-05` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-015-06` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-015-07` — Establish and maintain the compliance resolution verification control.
- `PCRV2-015-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 16. Verification Domain — Data Resolution Verification

**Control family:** `PCRV2-016`

The Data Resolution Verification domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-016-01` — Establish and maintain the data resolution verification control.
- `PCRV2-016-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-016-02` — Establish and maintain the data resolution verification control.
- `PCRV2-016-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-016-03` — Establish and maintain the data resolution verification control.
- `PCRV2-016-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-016-04` — Establish and maintain the data resolution verification control.
- `PCRV2-016-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-016-05` — Establish and maintain the data resolution verification control.
- `PCRV2-016-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-016-06` — Establish and maintain the data resolution verification control.
- `PCRV2-016-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-016-07` — Establish and maintain the data resolution verification control.
- `PCRV2-016-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 17. Verification Domain — AI and Agent Resolution Verification

**Control family:** `PCRV2-017`

The AI and Agent Resolution Verification domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-017-01` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-017-02` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-017-03` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-017-04` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-017-05` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-017-06` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-017-07` — Establish and maintain the ai and agent resolution verification control.
- `PCRV2-017-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 18. Verification Domain — Resolution Verification Failure

**Control family:** `PCRV2-018`

The Resolution Verification Failure domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-018-01` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-018-02` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-018-03` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-018-04` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-018-05` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-018-06` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-018-07` — Establish and maintain the resolution verification failure control.
- `PCRV2-018-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 19. Verification Domain — Resolution Verification Independence

**Control family:** `PCRV2-019`

The Resolution Verification Independence domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-019-01` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-019-02` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-019-03` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-019-04` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-019-05` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-019-06` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-019-07` — Establish and maintain the resolution verification independence control.
- `PCRV2-019-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## 20. Verification Domain — Resolution Verification Review and Learning

**Control family:** `PCRV2-020`

The Resolution Verification Review and Learning domain establishes governed mandatory verification requirements.

### Required controls
- `PCRV2-020-01` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-01-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-020-02` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-02-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-020-03` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-03-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-020-04` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-04-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-020-05` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-05-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-020-06` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-06-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.
- `PCRV2-020-07` — Establish and maintain the resolution verification review and learning control.
- `PCRV2-020-07-E` — Preserve resolution claim, criteria, method, evidence, observations, determination and follow-on traceability.

```text
RESOLVE → VERIFY → REVALIDATE
```

## Resolution Verification Structure

| Element | Required definition |
|---|---|
| Resolution Claim | State claimed to be established |
| Required State | Current target state |
| Criteria | Requirements against which the state is tested |
| Method | Verification approach |
| Evidence | Supporting verification basis |
| Observation | Actual observed current state |
| Determination | Verification result |
| Follow-on | Revalidation / reopening / restriction |

## Resolution Verification Objective

Determine whether the resolved condition has actually reached the required current state and whether the evidence supports progression to the next lifecycle stage.

## Resolution Verification Definition

Verification is the controlled examination of a resolution claim against current requirements, evidence, observations and boundaries to determine whether the claimed state is demonstrated.

## Resolution Verification Scope

Scope shall identify systems, services, users, data, decisions, dependencies, environments and boundaries included in the resolution claim.

## Resolution Verification Authority

Authority shall define who may perform, review, challenge, approve or reject verification and who may require additional testing.

## Resolution Verification Criteria

Criteria shall distinguish verified, partially verified, failed and unknown states.

```text
RESOLUTION CLAIM
↓
CURRENT CRITERIA DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
METHOD APPROPRIATE?
├── NO → REDESIGN
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → UNKNOWN
└── YES
     ↓
CONTROL + OUTCOME + BOUNDARY VERIFIED?
├── NO → PARTIAL / FAIL
└── YES → VERIFIED
```

## Resolution Verification Preconditions

Preconditions include a defined required state, current criteria, verification method, evidence availability, scope, authority and independence requirements.

## Resolution Verification Evidence

Evidence shall be current, attributable, reproducible where appropriate, traceable to the resolution and sufficient to support the determination.

## Resolution Verification Method

Methods may include inspection, testing, sampling, observation, measurement, replay, comparison, control testing, outcome validation and independent assurance.

```text
RESOLUTION
↓
SELECT METHOD
↓
OBSERVE / TEST / MEASURE
↓
COMPARE WITH CRITERIA
↓
DETERMINE
```

## Resolution Verification Decision

Verification decisions shall distinguish verified, partial, failed and unknown outcomes.

```text
VERIFIED → REVALIDATION PATH
PARTIAL → COMPLETE GAPS
FAILED → REOPEN / REMEDIATE
UNKNOWN → COMPLETE EVIDENCE
```

## Resolution Verification Accountability

Accountability shall remain explicit for method selection, evidence sufficiency, determination and recommendation for follow-on action.

## Resolution Verification Timing

Verification shall occur before a resolution is treated as fully effective where required. Delay shall not imply validity.

## Security Resolution Verification

Verify security controls, access, exposure, threat conditions, containment and required security outcomes against current criteria.

## Resilience Resolution Verification

Verify availability, recovery, continuity, capacity, dependency stability and service outcomes against current criteria.

## Compliance Resolution Verification

Verify obligations, controls, evidence, reporting and policy conditions against current criteria.

## Data Resolution Verification

Verify integrity, quality, lineage, access, retention, authorized use and downstream effects against current criteria.

## AI and Agent Resolution Verification

Verify AI/agent authority, policy, tool access, data boundaries, autonomy and behavioural outcomes against current criteria.

```text
AI / AGENT RESOLUTION
↓
AUTHORITY + POLICY + TOOLS + DATA + AUTONOMY + BEHAVIOUR
↓
CURRENTLY VALID?
├── YES → VERIFIED
└── NO → FAIL / REOPEN / RESTRICT
```

## Resolution Verification Failure

Failure includes insufficient evidence, failed tests, unexpected outcomes, boundary breaches, invalid criteria or inability to establish current state.

```text
VERIFICATION FAILURE
↓
NO UNCONTROLLED PROGRESSION
↓
IDENTIFY GAP
↓
REMEDIATE / COMPLETE EVIDENCE
↓
VERIFY AGAIN
```

## Resolution Verification Independence

Where materiality requires it, verification shall be performed or reviewed independently of the remediation role to reduce confirmation bias.

## Resolution Verification Review and Learning

Reviews shall identify recurring verification failures, weak methods, insufficient evidence, blind spots and opportunities to improve resolution quality.

## Verification Determination Model
```text
RESOLUTION CLAIM
↓
CURRENT CRITERIA DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
METHOD APPROPRIATE?
├── NO → REDESIGN
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → UNKNOWN / COMPLETE EVIDENCE
└── YES
     ↓
CONTROL + OUTCOME + BOUNDARY VERIFIED?
├── NO → PARTIAL / FAIL
└── YES → VERIFIED
```

## Verification Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Verified | Required state demonstrated | Proceed to revalidation |
| Partially Verified | Some requirements demonstrated | Complete gaps |
| Failed | Required state not demonstrated | Reopen / remediate |
| Unknown | Evidence insufficient | Investigate / complete evidence |

## Verification Record
| Field | Required |
|---|---|
| Verification ID | Yes |
| Resolution ID | Yes |
| Scope | Yes |
| Criteria Version | Yes |
| Method | Yes |
| Evidence References | Yes |
| Observations | Yes |
| Result | Yes |
| Reviewer | Yes |
| Residual Risk | Yes |
| Follow-on Decision | Yes |

## Verification Blind Spots
Known blind spots shall be documented. Material blind spots may require additional testing, compensating controls, restricted progression or reopening.

```text
KNOWN BLIND SPOT
↓
MATERIAL?
├── NO → DOCUMENT / MONITOR
└── YES → ADD TEST / CONTROL / RESTRICT
```

## Verification Scope Control
Verification shall not silently expand or contract the resolution claim. Material scope changes shall be governed and reflected in criteria and records.

## Verification Change Control
Changes to criteria, methods, evidence requirements, reviewer independence or decision thresholds shall be governed, approved, versioned and effective-dated.

```text
CURRENT VERIFICATION MODEL
↓
CHANGE PROPOSAL
↓
IMPACT / RISK ASSESSMENT
↓
AUTHORITY APPROVAL
↓
NEW VERSION
↓
EFFECTIVE DATE
```

## Verification Anti-Gaming Control
Verification shall not be reduced to checking that remediation tasks were completed. It shall establish whether the resulting current state meets the required criteria.

Historical verification records, methods, evidence, observations, failures, blind spots, reviewer decisions and follow-on determinations shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory resolution-verification layer beneath resolution and above revalidation. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, reacceptance, reliance restoration, monitoring, alerting, escalation, closure, post-closure monitoring or regression detection layers.

## Governance-to-Verification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → MANDATORY VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → MONITORING → ALERTING → ESCALATION → RESOLUTION
```

## Complete Verification Chain
```text
ALERT → ESCALATE → RESOLVE → VERIFY → REVALIDATE → REACCEPT IF REQUIRED → RESTORE / RESTRICT RELIANCE → MONITOR
```

## Next Document
`EA-IMETA-PC-RG-061` — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification Revalidation

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL RESOLUTIONS TO BE VERIFIED AGAINST CURRENT REQUIREMENTS, SUFFICIENT EVIDENCE, OBSERVED OUTCOMES AND APPLICABLE BOUNDARIES BEFORE THEY MAY PROGRESS TO REVALIDATION, REACCEPTANCE OR RELIANCE RESTORATION, WITH UNKNOWN, PARTIAL AND FAILED RESULTS REMAINING DISTINCT FROM VERIFIED STATE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-01

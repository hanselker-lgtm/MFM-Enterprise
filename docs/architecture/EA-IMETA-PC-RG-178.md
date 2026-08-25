# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-RELIANCE-RESTORATION-REACCEPTANCE-REVALIDATION-REACCEPTANCE-REVALIDATION-VERIFICATION-VALIDATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-178`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-178` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-RELIANCE-RESTORATION-REACCEPTANCE-REVALIDATION-REACCEPTANCE-REVALIDATION-VERIFICATION-VALIDATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Determination |
| Parent | EA-IMETA-PC-RG-177 — Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Validation Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory verification-validation determination layer that determines whether a substantively validated reacceptance revalidation has both procedural integrity and substantive effectiveness, and therefore qualifies as a reliable current basis for continued governed reliance.

## Core Principle
RG-176 verifies that reacceptance revalidation was correctly performed and implemented. RG-177 validates whether that verified revalidation is substantively true in the current state. RG-178 establishes the combined verification-validation determination without collapsing the two assurance dimensions into one.

```text
REACCEPTANCE REVALIDATION
        ↓
REVALIDATION VERIFICATION
        ↓
REVALIDATION VALIDATION
        ↓
COMBINED ASSURANCE DETERMINATION
├── VERIFIED + VALID
├── VERIFIED + VALID WITH CONDITIONS
├── VERIFIED BUT NOT VALIDATED
├── NOT VERIFIED
├── VERIFICATION FAILED
├── VALIDATION FAILED
└── INCONCLUSIVE
        ↓
MAINTAIN / CORRECT / REVALIDATE / REACCEPT / RESTRICT / REVOKE / REOPEN
```

## Combined Assurance Quality Test
```text
PROCEDURAL INTEGRITY
+ SUBSTANTIVE EFFECTIVENESS
+ CURRENT BASIS
+ CURRENT OUTCOME
+ MATERIAL CHANGE EFFECTS
+ CONTROL EFFECTIVENESS
+ RESIDUAL RISK
+ DEPENDENCIES
+ OBLIGATIONS
+ CONDITIONS
+ PERSISTENCE
+ NO MATERIAL INVALIDATING CONDITION
= QUALIFIED CURRENT REACCEPTANCE REVALIDATION
```

## Verification and Validation Must Remain Distinct
```text
VERIFICATION
→ WAS THE REVALIDATION CORRECTLY PERFORMED AND IMPLEMENTED?

VALIDATION
→ IS THE REVALIDATION CONCLUSION ACTUALLY TRUE AND EFFECTIVE?

COMBINED DETERMINATION
→ DO BOTH ASSURANCE DIMENSIONS SUPPORT THE SAME CURRENT GOVERNED STATE?
```

## Combined Determination States
```text
RRRARRVV0 — DETERMINATION NOT REQUIRED
RRRARRVV1 — DETERMINATION TRIGGER IDENTIFIED
RRRARRVV2 — VERIFICATION BASIS CONFIRMED
RRRARRVV3 — VALIDATION BASIS CONFIRMED
RRRARRVV4 — CURRENT STATE CONFIRMED
RRRARRVV5 — PROCEDURAL INTEGRITY CONFIRMED
RRRARRVV6 — SUBSTANTIVE EFFECTIVENESS CONFIRMED
RRRARRVV7 — MATERIAL CHANGE EFFECTS CONFIRMED
RRRARRVV8 — CURRENT RELIANCE OUTCOME CONFIRMED
RRRARRVV9 — CONTROL EFFECTIVENESS CONFIRMED
RRRARRVV10 — RESIDUAL RISK CONFIRMED
RRRARRVV11 — DEPENDENCIES CONFIRMED
RRRARRVV12 — OBLIGATIONS CONFIRMED
RRRARRVV13 — CONDITIONS CONFIRMED
RRRARRVV14 — PERSISTENCE CONFIRMED
RRRARRVV15 — NO MATERIAL INVALIDATING CONDITION CONFIRMED
RRRARRVV16 — VERIFIED + VALID
RRRARRVV17 — VERIFIED + VALID WITH CONDITIONS
RRRARRVV18 — VERIFIED BUT NOT VALIDATED
RRRARRVV19 — NOT VERIFIED
RRRARRVV20 — VERIFICATION FAILED
RRRARRVV21 — VALIDATION FAILED
RRRARRVV22 — INCONCLUSIVE
RRRARRVV23 — CORRECTION REQUIRED
RRRARRVV24 — REVALIDATION REQUIRED
RRRARRVV25 — REACCEPTANCE REQUIRED
RRRARRVV26 — RESTRICTION REQUIRED
RRRARRVV27 — REVOCATION REQUIRED
RRRARRVV28 — REOPENING REQUIRED
RRRARRVV29 — DETERMINATION COMPLETE
RRRARRVVX — UNKNOWN / INSUFFICIENT BASIS
RRRARRVVS — DETERMINATION SUSPENDED
```

## Assurance Dimensions
| Dimension | Required determination |
|---|---|
| Revalidation | Current revalidation state |
| Verification | Procedural and implementation integrity |
| Validation | Substantive current effectiveness |
| Current State | Actual current state |
| Material Change | Actual change effects |
| Reliance Outcome | Current governed outcome |
| Controls | Current effectiveness |
| Residual Risk | Current supportable risk |
| Dependencies | Current effectiveness |
| Obligations | Current effectiveness |
| Conditions | Current effectiveness |
| Persistence | Continued stability |
| Invalidating Conditions | Contradictions / failures |
| Scope | Current reliance boundary |
| Authority | Decision authority |
| Evidence | Complete assurance evidence |
| Combined Result | Final determination |
| Next State | Governed consequence |

## Combined Assurance Invariants

```text
VERIFICATION AND VALIDATION SHALL REMAIN DISTINCT ASSURANCE DIMENSIONS
```

```text
VERIFIED STATUS SHALL NOT AUTOMATICALLY IMPLY VALIDATED STATUS
```

```text
VALIDATED STATUS SHALL NOT AUTOMATICALLY PROVE PROCEDURAL VERIFICATION
```

```text
THE COMBINED DETERMINATION SHALL CONSIDER BOTH ASSURANCE DIMENSIONS
```

```text
THE CURRENT STATE SHALL BE COMPARED AGAINST THE CURRENT REVALIDATED BASIS
```

```text
MATERIAL CHANGE EFFECTS SHALL BE ASSESSED FOR BOTH PROCEDURAL COMPLETENESS AND SUBSTANTIVE EFFECT
```

```text
CURRENT RELIANCE OUTCOME SHALL SUPPORT THE COMBINED DETERMINATION
```

```text
CONTROL EFFECTIVENESS AND RESIDUAL RISK SHALL BE CURRENT AND SUPPORTABLE
```

```text
DEPENDENCIES, OBLIGATIONS, CONDITIONS AND PERSISTENCE SHALL BE INCLUDED WHERE MATERIAL
```

```text
NOT VERIFIED SHALL NOT BE TREATED AS VERIFIED + VALID
```

```text
VERIFIED BUT NOT VALIDATED SHALL NOT AUTHORIZE UNQUALIFIED CONTINUED RELIANCE
```

```text
VALIDATED BUT PROCEDURALLY UNVERIFIED SHALL NOT AUTHORIZE UNQUALIFIED CONTINUED RELIANCE WHERE VERIFICATION IS REQUIRED
```

```text
INCONCLUSIVE RESULTS SHALL REMAIN DISTINCT FROM POSITIVE DETERMINATIONS
```

```text
AI AND AGENT ASSURANCE SHALL ADDRESS BOTH PROCEDURAL GOVERNANCE AND SUBSTANTIVE CURRENT EFFECTIVENESS
```

```text
THE COMBINED DETERMINATION SHALL PRESERVE TRACEABILITY TO RG-175, RG-176 AND RG-177
```

## 1. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Governance
**Control family:** `PCRRRRARR-VV-001`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-001-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-001-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-001-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-001-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-001-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-001-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-001-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation governance control.
- `PCRRRRARR-VV-001-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 2. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Objective
**Control family:** `PCRRRRARR-VV-002`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-002-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-002-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-002-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-002-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-002-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-002-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-002-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation objective control.
- `PCRRRRARR-VV-002-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 3. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Definition
**Control family:** `PCRRRRARR-VV-003`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-003-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-003-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-003-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-003-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-003-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-003-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-003-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation definition control.
- `PCRRRRARR-VV-003-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 4. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Scope
**Control family:** `PCRRRRARR-VV-004`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-004-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-004-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-004-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-004-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-004-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-004-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-004-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation scope control.
- `PCRRRRARR-VV-004-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 5. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Authority
**Control family:** `PCRRRRARR-VV-005`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-005-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-005-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-005-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-005-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-005-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-005-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-005-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation authority control.
- `PCRRRRARR-VV-005-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 6. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Criteria
**Control family:** `PCRRRRARR-VV-006`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-006-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-006-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-006-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-006-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-006-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-006-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-006-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation criteria control.
- `PCRRRRARR-VV-006-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 7. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Preconditions
**Control family:** `PCRRRRARR-VV-007`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-007-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-007-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-007-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-007-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-007-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-007-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-007-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation preconditions control.
- `PCRRRRARR-VV-007-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 8. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Evidence
**Control family:** `PCRRRRARR-VV-008`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-008-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-008-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-008-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-008-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-008-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-008-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-008-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation evidence control.
- `PCRRRRARR-VV-008-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 9. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Method
**Control family:** `PCRRRRARR-VV-009`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-009-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-009-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-009-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-009-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-009-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-009-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-009-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation method control.
- `PCRRRRARR-VV-009-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 10. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Decision
**Control family:** `PCRRRRARR-VV-010`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-010-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-010-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-010-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-010-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-010-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-010-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-010-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation decision control.
- `PCRRRRARR-VV-010-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 11. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Accountability
**Control family:** `PCRRRRARR-VV-011`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-011-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-011-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-011-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-011-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-011-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-011-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-011-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation accountability control.
- `PCRRRRARR-VV-011-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 12. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Timing
**Control family:** `PCRRRRARR-VV-012`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-012-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-012-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-012-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-012-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-012-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-012-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-012-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation timing control.
- `PCRRRRARR-VV-012-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 13. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Security
**Control family:** `PCRRRRARR-VV-013`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-013-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-013-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-013-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-013-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-013-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-013-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-013-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation security control.
- `PCRRRRARR-VV-013-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 14. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Resilience
**Control family:** `PCRRRRARR-VV-014`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-014-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-014-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-014-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-014-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-014-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-014-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-014-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation resilience control.
- `PCRRRRARR-VV-014-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 15. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Compliance
**Control family:** `PCRRRRARR-VV-015`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-015-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-015-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-015-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-015-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-015-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-015-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-015-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation compliance control.
- `PCRRRRARR-VV-015-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 16. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Data
**Control family:** `PCRRRRARR-VV-016`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-016-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-016-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-016-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-016-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-016-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-016-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-016-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation data control.
- `PCRRRRARR-VV-016-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 17. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation AI and Agent
**Control family:** `PCRRRRARR-VV-017`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-017-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-017-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-017-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-017-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-017-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-017-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-017-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation ai and agent control.
- `PCRRRRARR-VV-017-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 18. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Failure
**Control family:** `PCRRRRARR-VV-018`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-018-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-018-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-018-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-018-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-018-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-018-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-018-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation failure control.
- `PCRRRRARR-VV-018-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 19. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Independence
**Control family:** `PCRRRRARR-VV-019`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-019-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-019-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-019-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-019-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-019-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-019-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-019-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation independence control.
- `PCRRRRARR-VV-019-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## 20. Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Review and Learning
**Control family:** `PCRRRRARR-VV-020`

The post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning domain establishes governed mandatory combined assurance requirements.

### Required controls
- `PCRRRRARR-VV-020-01` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-01-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-020-02` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-02-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-020-03` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-03-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-020-04` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-04-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-020-05` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-05-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-020-06` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-06-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.
- `PCRRRRARR-VV-020-07` — Establish and maintain the post-closure regression reliance restoration reacceptance revalidation reacceptance revalidation verification validation review and learning control.
- `PCRRRRARR-VV-020-07-E` — Preserve verification, validation, current state, change effects, outcome, controls, risk, dependencies, obligations, conditions, evidence, authority, scope and combined-determination traceability.

```text
REVALIDATE → VERIFY → VALIDATE → COMBINED DETERMINE → REACCEPT / RELY / RESTRICT / CORRECT / REVOKE / REOPEN
```

## Combined Assurance Objective
Determine whether both procedural verification and substantive validation support the same current reacceptance revalidation state and therefore support continued governed reliance.

## Combined Assurance Definition
The combined verification-validation determination is the governed conclusion that a reacceptance revalidation is both correctly performed and substantively effective for its current intended purpose.

## Combined Assurance Scope
Scope includes revalidation, verification, validation, current state, material changes, reliance outcome, controls, residual risk, dependencies, obligations, conditions, persistence and invalidating conditions.

## Combined Assurance Authority
The determination shall be made or authorized by the competent governance authority, with assurance independence proportionate to materiality and consequence.

## Combined Assurance Criteria
Criteria shall distinguish verified and valid, verified with conditions, verified but not validated, not verified, verification failed, validation failed and inconclusive states.

## Combined Assurance Preconditions
Preconditions include completed revalidation verification and validation, current evidence, defined criteria and a clear decision scope.

## Combined Assurance Evidence
Evidence shall provide traceable support for both procedural integrity and substantive effectiveness.

## Combined Assurance Method
Methods shall combine verification evidence review with substantive validation evidence, while keeping the tests independently identifiable.

## Combined Assurance Decision
The combined decision shall establish whether the current reacceptance revalidation is qualified for continued governed reliance and under what conditions.

## Combined Assurance Accountability
Accountability shall remain explicit for the verification result, validation result, combined decision and resulting corrective or governance action.

## Combined Assurance Timing
Combined determination shall occur after the required verification and validation results are available and before reliance depends on the final determination where required.

## Combined Assurance Security
Security assurance shall combine correct governance execution with actual current security effectiveness.

## Combined Assurance Resilience
Resilience assurance shall combine procedural correctness with actual current continuity, recovery and dependency effectiveness.

## Combined Assurance Compliance
Compliance assurance shall combine correct evidence and authorization with substantive current compliance.

## Combined Assurance Data
Data assurance shall combine procedural traceability with actual current data integrity, provenance, access and protection.

## Combined Assurance AI and Agent
AI/agent assurance shall combine governance verification with substantive current behavior and outcome validation.

## Combined Assurance Failure
Failure includes disagreement between verification and validation, unsupported positive states, material evidence gaps, current-state mismatch or invalidating conditions.

## Combined Assurance Independence
Independent assurance shall be used where materiality, consequence, conflict or governance requires separation of verification and validation.

## Combined Assurance Review and Learning
Reviews shall identify recurring divergence between procedural correctness and substantive effectiveness, false assurance and weaknesses in combined decision criteria.

## Combined Determination Model
```text
REACCEPTANCE REVALIDATION
↓
VERIFY PROCEDURAL INTEGRITY
↓
VALIDATE SUBSTANTIVE EFFECTIVENESS
↓
COMPARE RESULTS
├── VERIFIED + VALID → QUALIFIED
├── VERIFIED + VALID WITH CONDITIONS → QUALIFIED WITH CONDITIONS
├── VERIFIED + NOT VALIDATED → NOT QUALIFIED
├── NOT VERIFIED → NOT QUALIFIED
├── VERIFICATION FAILED → CORRECT / REVERIFY
├── VALIDATION FAILED → CORRECT / REVALIDATE
└── INCONCLUSIVE → RESOLVE EVIDENCE GAP
```

## Combined Outcome Matrix
| Verification | Validation | Combined determination | Treatment |
|---|---|---|---|
| Verified | Valid | Qualified | Maintain governed reliance |
| Verified | Valid with conditions | Qualified with conditions | Monitor / restrict |
| Verified | Not validated | Not qualified | Correct / revalidate |
| Verified | Failed | Not qualified | Correct / revalidate / revoke |
| Not verified | Valid | Not qualified | Verify / correct |
| Not verified | Valid with conditions | Not qualified | Verify / correct / restrict |
| Not verified | Not validated | Not qualified | Resolve both assurance gaps |
| Failed | Valid | Not qualified | Correct / reverify |
| Failed | Valid with conditions | Not qualified | Correct / restrict / reverify |
| Failed | Failed | Not qualified | Correct / revoke / reopen |
| Inconclusive | Any | Inconclusive | Resolve evidence / assurance gap |

## Combined Assurance Record
| Field | Required |
|---|---|
| Combined Determination ID | Yes |
| Revalidation ID | Yes |
| Verification ID | Yes |
| Validation ID | Yes |
| Prior Reacceptance ID | Yes |
| Current State | Yes |
| Material Change Effects | Yes |
| Reliance Outcome | Yes |
| Verification Result | Yes |
| Validation Result | Yes |
| Controls | Yes |
| Residual Risk | Yes |
| Dependencies | Yes |
| Obligations | Yes |
| Conditions | Where applicable |
| Persistence | Where applicable |
| Invalidating Conditions | Yes |
| Evidence | Yes |
| Authority | Yes |
| Scope | Yes |
| Combined Result | Yes |
| Next State | Yes |
| Corrective Actions | Where applicable |
| Timestamp | Yes |
| Audit Trail | Yes |

## Verified + Valid
The strongest positive state requires both procedural integrity and substantive effectiveness.
```text
VERIFIED + VALID = QUALIFIED CURRENT REACCEPTANCE REVALIDATION
```

## Verified + Valid With Conditions
Conditional qualification shall preserve all conditions, owners, limits, monitoring requirements and failure consequences.
```text
VERIFIED + VALID WITH CONDITIONS → QUALIFIED WITH CONDITIONS
```

## Verified But Not Validated
A correctly performed revalidation that does not substantively demonstrate effectiveness shall not authorize unqualified continued reliance.
```text
VERIFIED + NOT VALIDATED = NOT QUALIFIED
```

## Not Verified But Validated
Substantive effectiveness alone shall not substitute for required procedural verification.
```text
NOT VERIFIED + VALID = NOT QUALIFIED WHERE VERIFICATION IS REQUIRED
```

## Verification Failure
Where procedural verification fails, the current state shall not receive a positive combined determination until the verification defect is corrected and the required verification is completed.

## Validation Failure
Where substantive validation fails, the current state shall not receive a positive combined determination until effectiveness is restored and the required validation is completed.

## Inconclusive
Inconclusive results shall remain explicitly unresolved and shall not be silently converted into qualified reliance.

## Current State
The combined determination shall address the actual current state rather than relying solely on historical governance records.

## Material Change
Material changes shall be evaluated both for completeness of procedural assessment and for actual substantive effect.

## Reliance Outcome
The combined determination shall consider whether the current reliance outcome is both correctly governed and substantively effective.

## Control and Risk Assurance
Controls and residual risk shall be assessed through both assurance dimensions where material.

## Dependencies and Obligations
Material dependencies and continuing obligations shall be both correctly governed and substantively effective.

## Conditions and Persistence
Conditions and persistence requirements shall be verified and validated for actual current effectiveness.

## AI and Agent Combined Assurance
AI/agent systems shall require both procedural governance assurance and substantive behavioral/effectiveness assurance.
```text
GOVERNANCE CORRECT?
        ↓
BEHAVIOR EFFECTIVE?
        ↓
BOTH?
├── YES → QUALIFIED
└── NO → NOT QUALIFIED
```

## Evidence Retention
Combined assurance evidence shall preserve separate verification and validation records while providing a traceable combined determination.

## Relationship to RG-176
RG-176 provides procedural verification of reacceptance revalidation. RG-178 consumes that verification result as one of two independent assurance dimensions.

## Relationship to RG-177
RG-177 provides substantive validation of reacceptance revalidation. RG-178 consumes that validation result as the second independent assurance dimension.

## Relationship to RG-175
RG-175 establishes the reacceptance revalidation conclusion that RG-176 verifies and RG-177 validates.

## Relationship to RG-174
RG-174 establishes substantive validation of the renewed acceptance before its subsequent revalidation.

## Relationship to Reliance
Only a qualified combined determination, or an explicitly governed conditional qualification, shall provide the assurance basis for continued reliance where this determination is mandatory.

## Relationship to Revocation
A failed combined determination may require restriction or revocation where correction cannot restore the required assurance basis.

## Relationship to Reopening
Where the assurance conflict reveals that the underlying lifecycle state must be revisited, governed reopening shall be initiated.

## Governance-to-Combined-Assurance Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → DELIVERY → ACKNOWLEDGEMENT → RESPONSE INITIATION → RESPONSE AUTHORITY → AUTHORITY TRANSFER → RESPONSE EXECUTION → RESPONSE EFFECTIVENESS → RESOLUTION → CLOSURE → CLOSURE VERIFICATION → CLOSURE VALIDATION → REVALIDATION → REACCEPTANCE → REACCEPTANCE VERIFICATION → REACCEPTANCE VALIDATION → REACCEPTANCE REVALIDATION → REVALIDATION VERIFICATION → REVALIDATION VALIDATION → REACCEPTANCE RENEWAL → REACCEPTANCE VERIFICATION → REACCEPTANCE VALIDATION → REACCEPTANCE REVALIDATION → REACCEPTANCE REVALIDATION VERIFICATION → REACCEPTANCE REVALIDATION VALIDATION → MANDATORY COMBINED REVALIDATION ASSURANCE → RELIANCE RESTORATION → RELIANCE RESTORATION VERIFICATION → RELIANCE RESTORATION VALIDATION → RELIANCE RESTORATION REVALIDATION → POST-RESTORATION MONITORING → REOPENING
```

## Next Document
`EA-IMETA-PC-RG-179` — Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation Reacceptance Revalidation Verification Validation Revalidation Determination

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL POST-CLOSURE REGRESSION RELIANCE RESTORATION REACCEPTANCE REVALIDATION TO RECEIVE A COMBINED DETERMINATION THAT PRESERVES DISTINCT PROCEDURAL VERIFICATION AND SUBSTANTIVE VALIDATION, REQUIRES BOTH DIMENSIONS TO SUPPORT AN UNQUALIFIED POSITIVE STATE, TREATS VERIFIED BUT NOT VALIDATED AND NOT VERIFIED BUT VALID AS NOT QUALIFIED WHERE BOTH ASSURANCES ARE REQUIRED, KEEPS CONDITIONAL AND INCONCLUSIVE STATES DISTINCT, AND PROVIDES A TRACEABLE GOVERNED BASIS FOR CONTINUED RELIANCE, RESTRICTION, CORRECTION, REVOCATION OR REOPENING.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-RELIANCE-RESTORATION-REACCEPTANCE-REVALIDATION-REACCEPTANCE-REVALIDATION-VERIFICATION-VALIDATION-DETERMINATION-01

# EA-IMETA-PC-RG-204

## Physical File ID
`EA-IMETA-PC-RG-204`

## Document Registry Entry

| Field | Value |
|---|---|
| Short File ID | EA-IMETA-PC-RG-204 |
| Parent | EA-IMETA-PC-RG-203 |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose

Establish the authoritative mandatory substantive validation layer for RG-203, determining whether the procedural verification of RG-202 validation is itself substantively true, effective, complete and supportable in the actual current operating state.

## Core Principle

RG-203 verifies that RG-202 validation was correctly performed and implemented. RG-204 validates whether the RG-203 verification remains substantively effective and provides reliable assurance.

```text
RG-202 → VALIDATE
RG-203 → VERIFY
RG-204 → VALIDATE
```

```text
RG-203 PROCEDURAL VERIFICATION
        ↓
RG-204 SUBSTANTIVE VALIDATION
        ↓
IS THE RG-203 VERIFICATION ACTUALLY EFFECTIVE AND TRUE?
```

A positive RG-203 verification SHALL NOT automatically establish substantive current effectiveness.

## Validation Quality Test

```text
RG-203 VERIFIED RG-202 VALIDATION
+ CURRENT STATE CONFIRMED
+ VERIFICATION EFFECT CONFIRMED
+ CURRENT OUTCOME CONFIRMED
+ VERIFICATION INTEGRITY CONFIRMED
+ VALIDATION EFFECTIVENESS CONFIRMED
+ CONTROLS + RISK CONFIRMED
+ DEPENDENCIES + OBLIGATIONS CONFIRMED
+ CONDITIONS + PERSISTENCE CONFIRMED
+ NO MATERIAL INVALIDATING CONDITION
= VALIDATED RG-203 VERIFICATION
```

## Main Decision Flow

```text
RG-203 VERIFIED VALIDATION
        ↓
VALIDATE VERIFIED BASIS
        ↓
VALIDATE CURRENT STATE
        ↓
VALIDATE WHETHER RG-203 DETECTED MATERIAL DEFECTS IN RG-202
        ↓
VALIDATE VERIFICATION EFFECT
        ↓
VALIDATE CURRENT OUTCOME
        ↓
VALIDATE VERIFICATION INTEGRITY
        ↓
VALIDATE VALIDATION EFFECTIVENESS
        ↓
VALIDATE CONTROLS + RISK
        ↓
VALIDATE DEPENDENCIES + OBLIGATIONS
        ↓
VALIDATE CONDITIONS + PERSISTENCE
        ↓
VALIDATE INVALIDATING CONDITIONS
        ↓
VALID / VALID WITH CONDITIONS / NOT VALIDATED / FAILED / INCONCLUSIVE
```

## Validation States

00 — VALIDATION NOT REQUIRED
01 — VALIDATION TRIGGER IDENTIFIED
02 — VALIDATION PENDING
03 — VALIDATION IN PROGRESS
04 — VERIFIED VERIFICATION BASIS CONFIRMED
05 — CURRENT STATE CONFIRMED
06 — VERIFICATION EFFECT CONFIRMED
07 — CURRENT OUTCOME CONFIRMED
08 — VERIFICATION INTEGRITY CONFIRMED
09 — VALIDATION EFFECTIVENESS CONFIRMED
10 — CONTROL EFFECTIVENESS CONFIRMED
11 — RESIDUAL RISK CONFIRMED
12 — DEPENDENCIES CONFIRMED
13 — OBLIGATIONS CONFIRMED
14 — CONDITIONS CONFIRMED
15 — PERSISTENCE CONFIRMED
16 — NO MATERIAL INVALIDATING CONDITION CONFIRMED
17 — VALID
18 — VALID WITH CONDITIONS
19 — NOT VALIDATED
20 — VALIDATION FAILED
21 — VERIFICATION-VALIDATION EFFECT MISMATCH
22 — VERIFICATION INTEGRITY INSUFFICIENT
23 — VALIDATION EFFECTIVENESS INSUFFICIENT
24 — CONTROL EFFECTIVENESS INSUFFICIENT
25 — RESIDUAL RISK UNSUPPORTABLE
26 — DEPENDENCY FAILURE
27 — OBLIGATION FAILURE
28 — CONDITION FAILURE
29 — PERSISTENCE FAILURE
30 — REVERIFICATION REQUIRED
31 — REVALIDATION REQUIRED
32 — REQUALIFICATION REQUIRED
33 — REACCEPTANCE REQUIRED
34 — REVOCATION / CORRECTION REQUIRED
35 — REOPENING REQUIRED
36 — VALIDATION COMPLETE
37 — UNKNOWN / INSUFFICIENT BASIS
38 — VALIDATION SUSPENDED

## 20 Control Families

### 1. Validation of Verification-Validation — Governance

**Control family:** `EA-IMETA-PC-RG-204-001`

This family establishes mandatory governance requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-001-01` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-02` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-03` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-04` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-05` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-06` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-07` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-001-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 2. Validation of Verification-Validation — Objective

**Control family:** `EA-IMETA-PC-RG-204-002`

This family establishes mandatory objective requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-002-01` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-02` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-03` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-04` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-05` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-06` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-07` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-002-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 3. Validation of Verification-Validation — Definition

**Control family:** `EA-IMETA-PC-RG-204-003`

This family establishes mandatory definition requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-003-01` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-02` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-03` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-04` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-05` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-06` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-07` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-003-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 4. Validation of Verification-Validation — Scope

**Control family:** `EA-IMETA-PC-RG-204-004`

This family establishes mandatory scope requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-004-01` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-02` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-03` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-04` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-05` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-06` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-07` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-004-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 5. Validation of Verification-Validation — Authority

**Control family:** `EA-IMETA-PC-RG-204-005`

This family establishes mandatory authority requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-005-01` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-02` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-03` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-04` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-05` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-06` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-07` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-005-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 6. Validation of Verification-Validation — Criteria

**Control family:** `EA-IMETA-PC-RG-204-006`

This family establishes mandatory criteria requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-006-01` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-02` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-03` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-04` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-05` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-06` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-07` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-006-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 7. Validation of Verification-Validation — Preconditions

**Control family:** `EA-IMETA-PC-RG-204-007`

This family establishes mandatory preconditions requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-007-01` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-02` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-03` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-04` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-05` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-06` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-07` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-007-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 8. Validation of Verification-Validation — Evidence

**Control family:** `EA-IMETA-PC-RG-204-008`

This family establishes mandatory evidence requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-008-01` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-02` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-03` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-04` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-05` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-06` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-07` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-008-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 9. Validation of Verification-Validation — Method

**Control family:** `EA-IMETA-PC-RG-204-009`

This family establishes mandatory method requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-009-01` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-02` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-03` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-04` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-05` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-06` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-07` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-009-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 10. Validation of Verification-Validation — Decision

**Control family:** `EA-IMETA-PC-RG-204-010`

This family establishes mandatory decision requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-010-01` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-02` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-03` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-04` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-05` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-06` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-07` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-010-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 11. Validation of Verification-Validation — Accountability

**Control family:** `EA-IMETA-PC-RG-204-011`

This family establishes mandatory accountability requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-011-01` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-02` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-03` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-04` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-05` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-06` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-07` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-011-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 12. Validation of Verification-Validation — Timing

**Control family:** `EA-IMETA-PC-RG-204-012`

This family establishes mandatory timing requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-012-01` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-02` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-03` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-04` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-05` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-06` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-07` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-012-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 13. Validation of Verification-Validation — Security

**Control family:** `EA-IMETA-PC-RG-204-013`

This family establishes mandatory security requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-013-01` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-02` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-03` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-04` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-05` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-06` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-07` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-013-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 14. Validation of Verification-Validation — Resilience

**Control family:** `EA-IMETA-PC-RG-204-014`

This family establishes mandatory resilience requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-014-01` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-02` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-03` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-04` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-05` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-06` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-07` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-014-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 15. Validation of Verification-Validation — Compliance

**Control family:** `EA-IMETA-PC-RG-204-015`

This family establishes mandatory compliance requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-015-01` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-02` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-03` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-04` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-05` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-06` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-07` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-015-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 16. Validation of Verification-Validation — Data

**Control family:** `EA-IMETA-PC-RG-204-016`

This family establishes mandatory data requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-016-01` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-02` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-03` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-04` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-05` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-06` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-07` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-016-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 17. Validation of Verification-Validation — AI and Agent

**Control family:** `EA-IMETA-PC-RG-204-017`

This family establishes mandatory ai and agent requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-017-01` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-02` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-03` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-04` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-05` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-06` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-07` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-017-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 18. Validation of Verification-Validation — Failure

**Control family:** `EA-IMETA-PC-RG-204-018`

This family establishes mandatory failure requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-018-01` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-02` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-03` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-04` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-05` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-06` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-07` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-018-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 19. Validation of Verification-Validation — Independence

**Control family:** `EA-IMETA-PC-RG-204-019`

This family establishes mandatory independence requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-019-01` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-02` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-03` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-04` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-05` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-06` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-07` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-019-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

### 20. Validation of Verification-Validation — Review and Learning

**Control family:** `EA-IMETA-PC-RG-204-020`

This family establishes mandatory review and learning requirements for substantive validation of the RG-203 verification.

- `EA-IMETA-PC-RG-204-020-01` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-02` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-03` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-04` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-05` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-06` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-07` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-204-020-E` — Preserve traceability from current evidence through RG-203 verification to the RG-204 validation result.

## Core Validation Tests

### Verified Basis
RG-204 SHALL confirm that RG-203 used the correct RG-202 validation as its basis and preserved complete upstream traceability.

### Current State
The actual current state SHALL be tested sufficiently to determine whether RG-203 remains substantively credible.

```text
RG-203 VERIFICATION → CURRENT REALITY → MATCH?
├── YES → CONTINUE
└── NO → VERIFICATION-VALIDATION EFFECT MISMATCH
```

### Verification Effect
RG-204 SHALL determine whether RG-203 actually detected material weaknesses in RG-202 when such weaknesses existed.

```text
MATERIAL DEFECT PRESENT
        ↓
DID RG-203 DETECT IT?
├── YES → VERIFICATION EFFECT CONFIRMED
└── NO → VERIFICATION EFFECT MISMATCH
```

### Current Outcome
The actual current assurance outcome SHALL be compared with the outcome supported by RG-203.

### Verification Integrity
The substantive integrity of RG-203 evidence, independence, method and reasoning SHALL be assessed.

### Validation Effectiveness
RG-204 SHALL determine whether RG-203 provided meaningful assurance rather than merely procedural completion.

### Controls and Risk
Current controls SHALL be substantively effective and residual risk SHALL remain supportable.

### Dependencies, Obligations, Conditions and Persistence
Material dependencies and obligations SHALL be tested for actual effect. Conditions and persistence requirements SHALL be validated for actual compliance and continued applicability.

### Invalidating Conditions
Material contradictions or failures SHALL prevent unqualified validation.

```text
INVALIDATING CONDITION → MATERIAL?
├── NO → RECORD / CONTROL
└── YES → CORRECT / REVERIFY / REVALIDATE / REQUALIFY / REVOKE / REOPEN
```

## Administrative Completion Is Not Substantive Validation

```text
RG-203 COMPLETE
+ RECORD CLOSED
+ STATUS UPDATED
≠
RG-203 SUBSTANTIVELY VALIDATED
```

## Conditional Validation

Where RG-203 is VALID WITH CONDITIONS, RG-204 SHALL preserve exact conditions, responsible owner, evidence requirements, monitoring, review interval, escalation threshold, restriction consequence, revocation consequence and reopening trigger.

## Validation Failure

```text
RG-204 VALIDATION FAILURE
        ↓
IS THE FAILURE CORRECTABLE?
├── YES → CORRECT + REVERIFY + REVALIDATE
└── NO → REQUALIFY / REACCEPT / RESTRICT / REVOKE / REOPEN
```

## AI and Agent Validation

RG-204 SHALL substantively test whether RG-203 correctly verified RG-202 treatment of:

- model
- policy
- tools
- data
- configuration
- behavior
- monitoring
- operating context
- permissions
- safeguards
- human oversight

```text
RG-203 AI / AGENT VERIFICATION
        ↓
CURRENT REALITY
        ↓
DID VERIFICATION PROVIDE EFFECTIVE ASSURANCE?
├── YES → VALID
└── NO → VERIFICATION-EFFECT MISMATCH
```

## Validation Record

| Field | Required |
|---|---|
| Validation ID | Yes |
| RG-203 Verification ID | Yes |
| RG-202 Validation ID | Yes |
| RG-201 Verification ID | Yes |
| RG-200 Validation ID | Yes |
| RG-199 Verification ID | Yes |
| RG-198 Validation ID | Yes |
| RG-197 Verification ID | Yes |
| RG-196 Validation ID | Yes |
| RG-195 Verification ID | Yes |
| RG-194 Validation ID | Yes |
| RG-193 Verification ID | Yes |
| Current Baseline | Yes |
| Verification Effect | Yes |
| Current Outcome | Yes |
| Verification Integrity | Yes |
| Validation Effectiveness | Yes |
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
| Criteria | Yes |
| Result | Yes |
| Corrective Actions | Where applicable |
| Reverification | Where applicable |
| Revalidation | Where applicable |
| Requalification | Where applicable |
| Reacceptance | Where applicable |
| Restriction | Where applicable |
| Revocation | Where applicable |
| Reopening | Where applicable |
| Timestamp | Yes |
| Audit Trail | Yes |

## Assurance Separation

```text
RG-196 → VALIDATE
RG-197 → VERIFY
RG-198 → VALIDATE
RG-199 → VERIFY
RG-200 → VALIDATE
RG-201 → VERIFY
RG-202 → VALIDATE
RG-203 → VERIFY
RG-204 → VALIDATE
```

Each layer SHALL preserve independent evidence, authority, criteria, decision and audit trail.

## Relationship to Reliance

A validated RG-203 verification strengthens assurance over RG-202, but reliance SHALL remain bounded by current validated state, conditions and risk tolerance.

## Relationship to Revocation and Reopening

Where RG-204 identifies a materially ineffective RG-203 verification, downstream assurance may require correction, restriction, revocation or governed reopening.

## Evidence Retention

RG-204 evidence SHALL remain linked to RG-203, RG-202, RG-201, RG-200 and all preceding lifecycle assurance records.

## Next Document

`EA-IMETA-PC-RG-205`

## Final Principle

EA-IMETA SHALL REQUIRE MATERIAL POST-CLOSURE REGRESSION RELIANCE RESTORATION REACCEPTANCE REVALIDATION STATES TO HAVE THEIR PROCEDURAL VERIFICATIONS SUBSTANTIVELY VALIDATED AGAINST CURRENT REALITY, VERIFICATION EFFECT, CURRENT OUTCOME, VERIFICATION INTEGRITY, VALIDATION EFFECTIVENESS, CONTROLS, RESIDUAL RISK, DEPENDENCIES, OBLIGATIONS, CONDITIONS, PERSISTENCE AND MATERIAL INVALIDATING CONDITIONS, WITH VALID, CONDITIONAL, NOT VALIDATED, FAILED AND INCONCLUSIVE STATES KEPT DISTINCT.

# END OF {short}

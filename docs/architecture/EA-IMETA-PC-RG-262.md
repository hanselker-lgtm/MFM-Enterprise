# EA-IMETA-PC-RG-262

## Physical File ID
`EA-IMETA-PC-RG-262`

## Document Registry Entry

| Field | Value |
|---|---|
| Short File ID | EA-IMETA-PC-RG-262 |
| Parent | EA-IMETA-PC-RG-261 |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose

Establish the authoritative mandatory substantive validation layer for RG-262, determining whether the procedural verification of RG-261 validation is itself substantively true, effective, complete and supportable in the actual current operating state.

## Core Principle

RG-261 verifies that RG-260 validation was correctly performed and implemented. RG-262 validates whether the RG-261 verification remains substantively effective and provides reliable assurance.

```text
RG-260 → VALIDATE
RG-261 → VERIFY
RG-262 → VALIDATE
```

```text
RG-261 PROCEDURAL VERIFICATION
        ↓
RG-262 SUBSTANTIVE VALIDATION
        ↓
IS THE RG-261 VERIFICATION ACTUALLY EFFECTIVE AND TRUE?
```

A positive RG-261 verification SHALL NOT automatically establish substantive current effectiveness.

## Validation Quality Test

```text
RG-261 VERIFIED RG-260 VALIDATION
+ CURRENT STATE CONFIRMED
+ VERIFICATION EFFECT CONFIRMED
+ CURRENT OUTCOME CONFIRMED
+ VERIFICATION INTEGRITY CONFIRMED
+ VALIDATION EFFECTIVENESS CONFIRMED
+ CONTROLS + RISK CONFIRMED
+ DEPENDENCIES + OBLIGATIONS CONFIRMED
+ CONDITIONS + PERSISTENCE CONFIRMED
+ NO MATERIAL INVALIDATING CONDITION
= VALIDATED RG-261 VERIFICATION
```

## Main Decision Flow

```text
RG-261 VERIFIED VALIDATION
        ↓
VALIDATE VERIFIED BASIS
        ↓
VALIDATE CURRENT STATE
        ↓
VALIDATE WHETHER RG-261 DETECTED MATERIAL DEFECTS IN RG-260
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

**Control family:** `EA-IMETA-PC-RG-262-001`

This family establishes mandatory governance requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-001-01` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-02` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-03` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-04` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-05` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-06` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-07` — Validate governance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-001-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 2. Validation of Verification-Validation — Objective

**Control family:** `EA-IMETA-PC-RG-262-002`

This family establishes mandatory objective requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-002-01` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-02` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-03` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-04` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-05` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-06` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-07` — Validate objective effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-002-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 3. Validation of Verification-Validation — Definition

**Control family:** `EA-IMETA-PC-RG-262-003`

This family establishes mandatory definition requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-003-01` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-02` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-03` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-04` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-05` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-06` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-07` — Validate definition effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-003-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 4. Validation of Verification-Validation — Scope

**Control family:** `EA-IMETA-PC-RG-262-004`

This family establishes mandatory scope requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-004-01` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-02` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-03` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-04` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-05` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-06` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-07` — Validate scope effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-004-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 5. Validation of Verification-Validation — Authority

**Control family:** `EA-IMETA-PC-RG-262-005`

This family establishes mandatory authority requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-005-01` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-02` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-03` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-04` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-05` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-06` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-07` — Validate authority effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-005-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 6. Validation of Verification-Validation — Criteria

**Control family:** `EA-IMETA-PC-RG-262-006`

This family establishes mandatory criteria requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-006-01` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-02` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-03` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-04` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-05` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-06` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-07` — Validate criteria effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-006-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 7. Validation of Verification-Validation — Preconditions

**Control family:** `EA-IMETA-PC-RG-262-007`

This family establishes mandatory preconditions requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-007-01` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-02` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-03` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-04` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-05` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-06` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-07` — Validate preconditions effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-007-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 8. Validation of Verification-Validation — Evidence

**Control family:** `EA-IMETA-PC-RG-262-008`

This family establishes mandatory evidence requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-008-01` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-02` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-03` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-04` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-05` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-06` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-07` — Validate evidence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-008-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 9. Validation of Verification-Validation — Method

**Control family:** `EA-IMETA-PC-RG-262-009`

This family establishes mandatory method requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-009-01` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-02` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-03` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-04` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-05` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-06` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-07` — Validate method effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-009-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 10. Validation of Verification-Validation — Decision

**Control family:** `EA-IMETA-PC-RG-262-010`

This family establishes mandatory decision requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-010-01` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-02` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-03` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-04` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-05` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-06` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-07` — Validate decision effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-010-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 11. Validation of Verification-Validation — Accountability

**Control family:** `EA-IMETA-PC-RG-262-011`

This family establishes mandatory accountability requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-011-01` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-02` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-03` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-04` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-05` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-06` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-07` — Validate accountability effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-011-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 12. Validation of Verification-Validation — Timing

**Control family:** `EA-IMETA-PC-RG-262-012`

This family establishes mandatory timing requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-012-01` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-02` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-03` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-04` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-05` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-06` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-07` — Validate timing effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-012-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 13. Validation of Verification-Validation — Security

**Control family:** `EA-IMETA-PC-RG-262-013`

This family establishes mandatory security requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-013-01` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-02` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-03` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-04` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-05` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-06` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-07` — Validate security effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-013-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 14. Validation of Verification-Validation — Resilience

**Control family:** `EA-IMETA-PC-RG-262-014`

This family establishes mandatory resilience requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-014-01` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-02` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-03` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-04` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-05` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-06` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-07` — Validate resilience effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-014-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 15. Validation of Verification-Validation — Compliance

**Control family:** `EA-IMETA-PC-RG-262-015`

This family establishes mandatory compliance requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-015-01` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-02` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-03` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-04` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-05` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-06` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-07` — Validate compliance effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-015-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 16. Validation of Verification-Validation — Data

**Control family:** `EA-IMETA-PC-RG-262-016`

This family establishes mandatory data requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-016-01` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-02` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-03` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-04` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-05` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-06` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-07` — Validate data effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-016-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 17. Validation of Verification-Validation — AI and Agent

**Control family:** `EA-IMETA-PC-RG-262-017`

This family establishes mandatory ai and agent requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-017-01` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-02` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-03` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-04` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-05` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-06` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-07` — Validate ai and agent effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-017-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 18. Validation of Verification-Validation — Failure

**Control family:** `EA-IMETA-PC-RG-262-018`

This family establishes mandatory failure requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-018-01` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-02` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-03` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-04` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-05` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-06` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-07` — Validate failure effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-018-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 19. Validation of Verification-Validation — Independence

**Control family:** `EA-IMETA-PC-RG-262-019`

This family establishes mandatory independence requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-019-01` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-02` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-03` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-04` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-05` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-06` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-07` — Validate independence effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-019-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n### 20. Validation of Verification-Validation — Review and Learning

**Control family:** `EA-IMETA-PC-RG-262-020`

This family establishes mandatory review and learning requirements for substantive validation of the RG-261 verification.

- `EA-IMETA-PC-RG-262-020-01` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-02` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-03` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-04` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-05` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-06` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-07` — Validate review and learning effectiveness, evidence, authority, scope, criteria, decision and implementation as applicable.\n- `EA-IMETA-PC-RG-262-020-E` — Preserve traceability from current evidence through RG-261 verification to the RG-262 validation result.\n\n## Core Validation Tests

### Verified Basis
RG-262 SHALL confirm that RG-261 used the correct RG-260 validation as its basis and preserved complete upstream traceability.

### Current State
The actual current state SHALL be tested sufficiently to determine whether RG-261 remains substantively credible.

```text
RG-261 VERIFICATION → CURRENT REALITY → MATCH?
├── YES → CONTINUE
└── NO → VERIFICATION-VALIDATION EFFECT MISMATCH
```

### Verification Effect
RG-262 SHALL determine whether RG-261 actually detected material weaknesses in RG-260 when such weaknesses existed.

```text
MATERIAL DEFECT PRESENT
        ↓
DID RG-261 DETECT IT?
├── YES → VERIFICATION EFFECT CONFIRMED
└── NO → VERIFICATION EFFECT MISMATCH
```

### Current Outcome
The actual current assurance outcome SHALL be compared with the outcome supported by RG-261.

### Verification Integrity
The substantive integrity of RG-261 evidence, independence, method and reasoning SHALL be assessed.

### Validation Effectiveness
RG-262 SHALL determine whether RG-261 provided meaningful assurance rather than merely procedural completion.

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
RG-261 COMPLETE
+ RECORD CLOSED
+ STATUS UPDATED
≠
RG-261 SUBSTANTIVELY VALIDATED
```

## Conditional Validation

Where RG-261 is VALID WITH CONDITIONS, RG-262 SHALL preserve exact conditions, responsible owner, evidence requirements, monitoring, review interval, escalation threshold, restriction consequence, revocation consequence and reopening trigger.

## Validation Failure

```text
RG-262 VALIDATION FAILURE
        ↓
IS THE FAILURE CORRECTABLE?
├── YES → CORRECT + REVERIFY + REVALIDATE
└── NO → REQUALIFY / REACCEPT / RESTRICT / REVOKE / REOPEN
```

## AI and Agent Validation

RG-262 SHALL substantively test whether RG-261 correctly verified RG-260 treatment of:

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

## Validation Record

| Field | Required |
|---|---|
| Validation ID | Yes |
| RG-261 Verification ID | Yes |
| RG-260 Validation ID | Yes |
| RG-259 Verification ID | Yes |
| RG-258 Validation ID | Yes |
| RG-257 Verification ID | Yes |
| RG-256 Validation ID | Yes |
| RG-255 Verification ID | Yes |
| RG-254 Validation ID | Yes |
| RG-253 Verification ID | Yes |
| RG-252 Validation ID | Yes |
| RG-251 Verification ID | Yes |
| RG-250 Validation ID | Yes |
| RG-249 Verification ID | Yes |
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
RG-250 → VALIDATE
RG-251 → VERIFY
RG-252 → VALIDATE
RG-253 → VERIFY
RG-254 → VALIDATE
RG-255 → VERIFY
RG-256 → VALIDATE
RG-257 → VERIFY
RG-258 → VALIDATE
RG-259 → VERIFY
RG-260 → VALIDATE
RG-261 → VERIFY
RG-262 → VALIDATE
```

Each layer SHALL preserve independent evidence, authority, criteria, decision and audit trail.

## Relationship to Reliance

A validated RG-261 verification strengthens assurance over RG-260, but reliance SHALL remain bounded by current validated state, conditions and risk tolerance.

## Relationship to Revocation and Reopening

Where RG-262 identifies a materially ineffective RG-261 verification, downstream assurance may require correction, restriction, revocation or governed reopening.

## Evidence Retention

RG-262 evidence SHALL remain linked to RG-261, RG-260, RG-259, RG-258, RG-257, RG-256, RG-255, RG-254, RG-253, RG-252, RG-251, RG-250, RG-249, RG-248 and all preceding lifecycle assurance records.

## Next Document

`EA-IMETA-PC-RG-263`

## Final Principle

EA-IMETA SHALL REQUIRE MATERIAL POST-CLOSURE REGRESSION RELIANCE RESTORATION REACCEPTANCE REVALIDATION STATES TO HAVE THEIR PROCEDURAL VERIFICATIONS SUBSTANTIVELY VALIDATED AGAINST CURRENT REALITY, VERIFICATION EFFECT, CURRENT OUTCOME, VERIFICATION INTEGRITY, VALIDATION EFFECTIVENESS, CONTROLS, RESIDUAL RISK, DEPENDENCIES, OBLIGATIONS, CONDITIONS, PERSISTENCE AND MATERIAL INVALIDATING CONDITIONS, WITH VALID, CONDITIONAL, NOT VALIDATED, FAILED AND INCONCLUSIVE STATES KEPT DISTINCT.

# END OF {short}

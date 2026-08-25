# EA-IMETA-PC-RG-201

## Physical File ID
`EA-IMETA-PC-RG-201`

## Document Registry Entry

| Field | Value |
|---|---|
| Short File ID | EA-IMETA-PC-RG-201 |
| Parent | EA-IMETA-PC-RG-200 |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation Verification |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose

Establish the authoritative mandatory procedural verification layer for RG-200, determining whether the substantive validation of RG-199 verification was correctly performed, evidenced, authorized, decided, recorded and implemented.

## Core Principle

RG-200 determines whether the RG-199 verification is substantively effective. RG-201 verifies that RG-200's validation of that verification was correctly performed and implemented.

```text
RG-198 → VALIDATE
RG-199 → VERIFY
RG-200 → VALIDATE
RG-201 → VERIFY
```

```text
RG-200 SUBSTANTIVE VALIDATION
        ↓
RG-201 PROCEDURAL VERIFICATION
        ↓
WAS RG-200 CORRECTLY PERFORMED?
```

A positive RG-200 validation SHALL NOT automatically prove that RG-200 was correctly verified.

## Verification Quality Test

```text
RG-200 VALIDATION
+ VALID TRIGGER
+ CORRECT RG-199 BASIS
+ CURRENT STATE
+ VERIFICATION EFFECT
+ CURRENT OUTCOME
+ VERIFICATION INTEGRITY
+ VALIDATION EFFECTIVENESS
+ CONTROLS + RISK
+ DEPENDENCIES + OBLIGATIONS
+ CONDITIONS + PERSISTENCE
+ INVALIDATING CONDITIONS
+ EVIDENCE + AUTHORITY + SCOPE + CRITERIA
+ DECISION + RECORDING + COMMUNICATION + IMPLEMENTATION
= VERIFIED RG-200 VALIDATION
```

## Main Decision Flow

```text
RG-200 VALIDATION
        ↓
VERIFY TRIGGER
        ↓
VERIFY RG-199 BASIS
        ↓
VERIFY CURRENT BASELINE
        ↓
VERIFY VERIFICATION EFFECT
        ↓
VERIFY CURRENT OUTCOME
        ↓
VERIFY VERIFICATION INTEGRITY
        ↓
VERIFY VALIDATION EFFECTIVENESS
        ↓
VERIFY CONTROLS + RISK
        ↓
VERIFY DEPENDENCIES + OBLIGATIONS
        ↓
VERIFY CONDITIONS + PERSISTENCE
        ↓
VERIFY INVALIDATING CONDITIONS
        ↓
VERIFY EVIDENCE + AUTHORITY + SCOPE + CRITERIA
        ↓
VERIFY DECISION + RECORDING + COMMUNICATION + IMPLEMENTATION
        ↓
VERIFIED / VERIFIED WITH CONDITIONS / NOT VERIFIED / FAILED / INCONCLUSIVE
```

## Verification States

00 — VERIFICATION NOT REQUIRED
01 — VERIFICATION TRIGGER IDENTIFIED
02 — VERIFICATION PENDING
03 — VERIFICATION IN PROGRESS
04 — VALIDATED VERIFICATION BASIS CONFIRMED
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
17 — VERIFIED
18 — VERIFIED WITH CONDITIONS
19 — NOT VERIFIED
20 — VERIFICATION FAILED
21 — VALIDATION-VERIFICATION EFFECT MISMATCH
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
36 — VERIFICATION COMPLETE
37 — UNKNOWN / INSUFFICIENT BASIS
38 — VERIFICATION SUSPENDED

## 20 Control Families

### 1. Verification of Validation-Verification — Governance

**Control family:** `EA-IMETA-PC-RG-201-001`

This family establishes mandatory governance requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-001-01` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-02` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-03` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-04` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-05` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-06` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-07` — Verify governance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-001-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 2. Verification of Validation-Verification — Objective

**Control family:** `EA-IMETA-PC-RG-201-002`

This family establishes mandatory objective requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-002-01` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-02` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-03` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-04` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-05` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-06` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-07` — Verify objective evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-002-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 3. Verification of Validation-Verification — Definition

**Control family:** `EA-IMETA-PC-RG-201-003`

This family establishes mandatory definition requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-003-01` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-02` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-03` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-04` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-05` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-06` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-07` — Verify definition evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-003-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 4. Verification of Validation-Verification — Scope

**Control family:** `EA-IMETA-PC-RG-201-004`

This family establishes mandatory scope requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-004-01` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-02` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-03` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-04` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-05` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-06` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-07` — Verify scope evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-004-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 5. Verification of Validation-Verification — Authority

**Control family:** `EA-IMETA-PC-RG-201-005`

This family establishes mandatory authority requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-005-01` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-02` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-03` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-04` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-05` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-06` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-07` — Verify authority evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-005-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 6. Verification of Validation-Verification — Criteria

**Control family:** `EA-IMETA-PC-RG-201-006`

This family establishes mandatory criteria requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-006-01` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-02` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-03` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-04` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-05` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-06` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-07` — Verify criteria evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-006-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 7. Verification of Validation-Verification — Preconditions

**Control family:** `EA-IMETA-PC-RG-201-007`

This family establishes mandatory preconditions requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-007-01` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-02` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-03` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-04` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-05` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-06` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-07` — Verify preconditions evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-007-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 8. Verification of Validation-Verification — Evidence

**Control family:** `EA-IMETA-PC-RG-201-008`

This family establishes mandatory evidence requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-008-01` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-02` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-03` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-04` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-05` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-06` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-07` — Verify evidence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-008-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 9. Verification of Validation-Verification — Method

**Control family:** `EA-IMETA-PC-RG-201-009`

This family establishes mandatory method requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-009-01` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-02` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-03` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-04` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-05` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-06` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-07` — Verify method evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-009-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 10. Verification of Validation-Verification — Decision

**Control family:** `EA-IMETA-PC-RG-201-010`

This family establishes mandatory decision requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-010-01` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-02` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-03` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-04` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-05` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-06` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-07` — Verify decision evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-010-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 11. Verification of Validation-Verification — Accountability

**Control family:** `EA-IMETA-PC-RG-201-011`

This family establishes mandatory accountability requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-011-01` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-02` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-03` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-04` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-05` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-06` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-07` — Verify accountability evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-011-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 12. Verification of Validation-Verification — Timing

**Control family:** `EA-IMETA-PC-RG-201-012`

This family establishes mandatory timing requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-012-01` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-02` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-03` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-04` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-05` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-06` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-07` — Verify timing evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-012-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 13. Verification of Validation-Verification — Security

**Control family:** `EA-IMETA-PC-RG-201-013`

This family establishes mandatory security requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-013-01` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-02` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-03` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-04` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-05` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-06` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-07` — Verify security evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-013-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 14. Verification of Validation-Verification — Resilience

**Control family:** `EA-IMETA-PC-RG-201-014`

This family establishes mandatory resilience requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-014-01` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-02` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-03` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-04` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-05` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-06` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-07` — Verify resilience evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-014-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 15. Verification of Validation-Verification — Compliance

**Control family:** `EA-IMETA-PC-RG-201-015`

This family establishes mandatory compliance requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-015-01` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-02` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-03` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-04` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-05` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-06` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-07` — Verify compliance evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-015-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 16. Verification of Validation-Verification — Data

**Control family:** `EA-IMETA-PC-RG-201-016`

This family establishes mandatory data requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-016-01` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-02` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-03` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-04` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-05` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-06` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-07` — Verify data evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-016-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 17. Verification of Validation-Verification — AI and Agent

**Control family:** `EA-IMETA-PC-RG-201-017`

This family establishes mandatory ai and agent requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-017-01` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-02` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-03` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-04` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-05` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-06` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-07` — Verify ai and agent evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-017-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 18. Verification of Validation-Verification — Failure

**Control family:** `EA-IMETA-PC-RG-201-018`

This family establishes mandatory failure requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-018-01` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-02` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-03` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-04` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-05` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-06` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-07` — Verify failure evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-018-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 19. Verification of Validation-Verification — Independence

**Control family:** `EA-IMETA-PC-RG-201-019`

This family establishes mandatory independence requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-019-01` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-02` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-03` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-04` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-05` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-06` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-07` — Verify independence evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-019-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

### 20. Verification of Validation-Verification — Review and Learning

**Control family:** `EA-IMETA-PC-RG-201-020`

This family establishes mandatory review and learning requirements for procedural verification of the RG-200 substantive validation.

- `EA-IMETA-PC-RG-201-020-01` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-02` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-03` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-04` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-05` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-06` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-07` — Verify review and learning evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-201-020-E` — Preserve traceability from RG-200 validation evidence through the RG-201 verification result.

## Key Verification Rules

- The RG-200 trigger SHALL be valid, applicable and timely.
- The RG-199 verification SHALL be the correct basis for RG-200.
- The current baseline SHALL be current, sufficient and traceable.
- Verification effect SHALL be supported by evidence and correct reasoning.
- Current outcome SHALL match the governed intended outcome or be explicitly dispositioned.
- Verification integrity SHALL remain distinct from validation effectiveness.
- Material controls and residual risk SHALL be supportable.
- Dependencies, obligations, conditions and persistence SHALL be verified where applicable.
- Material invalidating conditions SHALL prevent unqualified verification.
- Administrative completion SHALL NOT constitute verification.
- AI and agent validation-verification SHALL include material governance, behavioral and configuration changes.
- NOT VERIFIED, FAILED and INCONCLUSIVE SHALL NOT be treated as positive assurance.

## Administrative Completion Is Not Verification

```text
TASK COMPLETED
+ REGISTER UPDATED
+ STATUS CLOSED
≠
VERIFIED RG-200 VALIDATION
```

## Conditional Verification

Where RG-200 is VALID WITH CONDITIONS, RG-201 SHALL verify the conditions, owner, evidence requirements, monitoring, review interval, escalation threshold, restriction consequence, revocation consequence and reopening trigger.

## Verification Failure

```text
RG-201 VERIFICATION FAILURE
        ↓
CORRECTABLE?
├── YES → CORRECT + REVERIFY
└── NO → REVALIDATE / REQUALIFY / REACCEPT / RESTRICT / REVOKE / REOPEN
```

## AI and Agent Verification

RG-201 SHALL verify that RG-200 correctly validated RG-199 treatment of:

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

## Verification Record

| Field | Required |
|---|---|
| Verification ID | Yes |
| RG-200 Validation ID | Yes |
| RG-199 Verification ID | Yes |
| RG-198 Validation ID | Yes |
| RG-197 Verification ID | Yes |
| RG-196 Validation ID | Yes |
| RG-195 Verification ID | Yes |
| RG-194 Validation ID | Yes |
| RG-193 Verification ID | Yes |
| RG-192 Validation ID | Yes |
| RG-191 Verification ID | Yes |
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
| Decision | Yes |
| Recording | Yes |
| Communication | Where applicable |
| Implementation | Yes |
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
RG-190 → VALIDATE
RG-191 → VERIFY
RG-192 → VALIDATE
RG-193 → VERIFY
RG-194 → VALIDATE
RG-195 → VERIFY
RG-196 → VALIDATE
RG-197 → VERIFY
RG-198 → VALIDATE
RG-199 → VERIFY
RG-200 → VALIDATE
RG-201 → VERIFY
```

Each layer SHALL preserve independent evidence, authority, criteria, decision and audit trail.

## Relationship to Reliance

RG-201 provides procedural assurance over RG-200. It does not replace the substantive validation performed by RG-200.

## Relationship to Revocation and Reopening

A material RG-201 verification failure may require correction, restriction, revocation, revalidation, requalification, reacceptance or governed reopening.

## Evidence Retention

RG-201 evidence SHALL remain linked to RG-200 and all preceding lifecycle assurance records.

## Next Document

`EA-IMETA-PC-RG-202`

## Final Principle

EA-IMETA SHALL REQUIRE MATERIAL POST-CLOSURE REGRESSION RELIANCE RESTORATION REACCEPTANCE REVALIDATION STATES TO HAVE THEIR SUBSTANTIVE VALIDATIONS PROCEDURALLY VERIFIED, WITH CURRENT STATE, EVIDENCE, AUTHORITY, SCOPE, CRITERIA, DECISION, IMPLEMENTATION, RISK, DEPENDENCIES, CONDITIONS AND INVALIDATING CONDITIONS TRACEABLE AND WITH VERIFIED, CONDITIONAL, NOT VERIFIED, FAILED AND INCONCLUSIVE STATES KEPT DISTINCT.

# END OF EA-IMETA-PC-RG-201

# EA-IMETA-PC-RG-213

## Physical File ID
`EA-IMETA-PC-RG-213`

## Document Registry Entry

| Field | Value |
|---|---|
| Short File ID | EA-IMETA-PC-RG-213 |
| Parent | EA-IMETA-PC-RG-212 |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Reliance Restoration Reacceptance Revalidation |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose

Establish the authoritative mandatory procedural verification layer for RG-212, determining whether the substantive validation of RG-211 verification was correctly performed, evidenced, authorized, decided, recorded and implemented.

## Core Principle

RG-212 determines whether the RG-211 verification is substantively effective. RG-213 verifies that RG-212's validation of that verification was correctly performed and implemented.

```text
RG-210 → VALIDATE
RG-211 → VERIFY
RG-212 → VALIDATE
RG-213 → VERIFY
```

```text
RG-212 SUBSTANTIVE VALIDATION
        ↓
RG-213 PROCEDURAL VERIFICATION
        ↓
WAS RG-212 CORRECTLY PERFORMED?
```

A positive RG-212 validation SHALL NOT automatically prove that RG-212 was correctly verified.

## Verification Quality Test

```text
RG-212 VALIDATION
+ VALID TRIGGER
+ CORRECT RG-211 BASIS
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
= VERIFIED RG-212 VALIDATION
```

## Main Decision Flow

```text
RG-212 VALIDATION
        ↓
VERIFY TRIGGER
        ↓
VERIFY RG-211 BASIS
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

**Control family:** `EA-IMETA-PC-RG-213-001`

This family establishes mandatory governance requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-001-01` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-02` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-03` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-04` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-05` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-06` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-07` — Verify governance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-001-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 2. Verification of Validation-Verification — Objective

**Control family:** `EA-IMETA-PC-RG-213-002`

This family establishes mandatory objective requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-002-01` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-02` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-03` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-04` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-05` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-06` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-07` — Verify objective determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-002-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 3. Verification of Validation-Verification — Definition

**Control family:** `EA-IMETA-PC-RG-213-003`

This family establishes mandatory definition requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-003-01` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-02` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-03` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-04` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-05` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-06` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-07` — Verify definition determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-003-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 4. Verification of Validation-Verification — Scope

**Control family:** `EA-IMETA-PC-RG-213-004`

This family establishes mandatory scope requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-004-01` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-02` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-03` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-04` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-05` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-06` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-07` — Verify scope determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-004-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 5. Verification of Validation-Verification — Authority

**Control family:** `EA-IMETA-PC-RG-213-005`

This family establishes mandatory authority requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-005-01` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-02` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-03` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-04` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-05` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-06` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-07` — Verify authority determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-005-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 6. Verification of Validation-Verification — Criteria

**Control family:** `EA-IMETA-PC-RG-213-006`

This family establishes mandatory criteria requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-006-01` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-02` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-03` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-04` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-05` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-06` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-07` — Verify criteria determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-006-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 7. Verification of Validation-Verification — Preconditions

**Control family:** `EA-IMETA-PC-RG-213-007`

This family establishes mandatory preconditions requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-007-01` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-02` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-03` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-04` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-05` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-06` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-07` — Verify preconditions determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-007-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 8. Verification of Validation-Verification — Evidence

**Control family:** `EA-IMETA-PC-RG-213-008`

This family establishes mandatory evidence requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-008-01` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-02` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-03` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-04` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-05` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-06` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-07` — Verify evidence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-008-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 9. Verification of Validation-Verification — Method

**Control family:** `EA-IMETA-PC-RG-213-009`

This family establishes mandatory method requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-009-01` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-02` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-03` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-04` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-05` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-06` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-07` — Verify method determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-009-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 10. Verification of Validation-Verification — Decision

**Control family:** `EA-IMETA-PC-RG-213-010`

This family establishes mandatory decision requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-010-01` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-02` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-03` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-04` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-05` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-06` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-07` — Verify decision determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-010-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 11. Verification of Validation-Verification — Accountability

**Control family:** `EA-IMETA-PC-RG-213-011`

This family establishes mandatory accountability requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-011-01` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-02` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-03` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-04` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-05` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-06` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-07` — Verify accountability determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-011-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 12. Verification of Validation-Verification — Timing

**Control family:** `EA-IMETA-PC-RG-213-012`

This family establishes mandatory timing requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-012-01` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-02` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-03` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-04` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-05` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-06` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-07` — Verify timing determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-012-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 13. Verification of Validation-Verification — Security

**Control family:** `EA-IMETA-PC-RG-213-013`

This family establishes mandatory security requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-013-01` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-02` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-03` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-04` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-05` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-06` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-07` — Verify security determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-013-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 14. Verification of Validation-Verification — Resilience

**Control family:** `EA-IMETA-PC-RG-213-014`

This family establishes mandatory resilience requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-014-01` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-02` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-03` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-04` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-05` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-06` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-07` — Verify resilience determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-014-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 15. Verification of Validation-Verification — Compliance

**Control family:** `EA-IMETA-PC-RG-213-015`

This family establishes mandatory compliance requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-015-01` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-02` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-03` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-04` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-05` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-06` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-07` — Verify compliance determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-015-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 16. Verification of Validation-Verification — Data

**Control family:** `EA-IMETA-PC-RG-213-016`

This family establishes mandatory data requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-016-01` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-02` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-03` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-04` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-05` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-06` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-07` — Verify data determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-016-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 17. Verification of Validation-Verification — AI and Agent

**Control family:** `EA-IMETA-PC-RG-213-017`

This family establishes mandatory ai and agent requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-017-01` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-02` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-03` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-04` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-05` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-06` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-07` — Verify ai and agent determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-017-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 18. Verification of Validation-Verification — Failure

**Control family:** `EA-IMETA-PC-RG-213-018`

This family establishes mandatory failure requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-018-01` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-02` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-03` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-04` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-05` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-06` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-07` — Verify failure determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-018-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 19. Verification of Validation-Verification — Independence

**Control family:** `EA-IMETA-PC-RG-213-019`

This family establishes mandatory independence requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-019-01` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-02` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-03` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-04` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-05` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-06` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-07` — Verify independence determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-019-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

### 20. Verification of Validation-Verification — Review and Learning

**Control family:** `EA-IMETA-PC-RG-213-020`

This family establishes mandatory review and learning requirements for procedural verification of the RG-212 substantive validation.

- `EA-IMETA-PC-RG-213-020-01` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-02` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-03` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-04` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-05` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-06` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-07` — Verify review and learning determination, evidence, authority, scope, criteria, decision and implementation as applicable.
- `EA-IMETA-PC-RG-213-020-E` — Preserve complete traceability from RG-212 validation evidence through the RG-213 verification result.

## Key Verification Tests

### RG-212 Validation Trigger
The verifier SHALL confirm that RG-212 was initiated on a valid, applicable and timely basis.

### Correct Basis
The verifier SHALL confirm that RG-212 used the correct RG-211 verification as its basis and preserved upstream traceability.

### Current Baseline
The verifier SHALL confirm that the current reality used by RG-212 was actually current and sufficiently evidenced.

### Verification Effect
The verifier SHALL confirm that RG-212 correctly assessed whether RG-211 detected material weaknesses in RG-210.

```text
MATERIAL DEFECT
        ↓
RG-211 DETECTION
        ↓
RG-212 VALIDATION
        ↓
RG-213 VERIFICATION
        ↓
CORRECT?
├── YES → VERIFIED
└── NO → VERIFICATION FAILURE
```

### Current Outcome
The verifier SHALL confirm that RG-212 correctly assessed the actual current assurance outcome.

### Verification Integrity
The verifier SHALL confirm that RG-212 correctly assessed the integrity of RG-211 and did not confuse procedural completeness with substantive effectiveness.

### Validation Effectiveness
The verifier SHALL confirm that RG-212 used appropriate evidence and methods to determine actual effectiveness.

### Controls and Risk
Material controls and residual risk determinations SHALL be traceable to current evidence and criteria.

### Dependencies and Obligations
Material dependencies and continuing obligations SHALL be verified for correct treatment.

### Conditions and Persistence
Conditions, restrictions and persistence requirements SHALL be verified for correct assessment and implementation.

### Invalidating Conditions
Material contradictions and failures SHALL be correctly identified and acted upon.

### Evidence, Authority, Scope and Criteria
Evidence SHALL be current, relevant, sufficient and traceable. Authority, scope and criteria SHALL match the governed requirements.

### Decision, Recording, Communication and Implementation
The recorded, communicated and implemented state SHALL match the RG-212 validation decision.

```text
RG-212 DECISION
        ↓
RECORDED STATE
        ↓
COMMUNICATED STATE
        ↓
IMPLEMENTED STATE
        ↓
ALL MATCH?
├── YES → VERIFIED
└── NO → CORRECTION REQUIRED
```

## Administrative Completion Is Not Verification

```text
TASK COMPLETED
+ REGISTER UPDATED
+ STATUS CLOSED
≠
VERIFIED RG-212 VALIDATION
```

## Conditional Verification

Where RG-212 is VALID WITH CONDITIONS, RG-213 SHALL verify exact conditions, responsible owner, evidence requirements, monitoring, review interval, escalation threshold, restriction consequence, revocation consequence and reopening trigger.

## Verification Failure

```text
RG-213 VERIFICATION FAILURE
        ↓
CORRECTABLE?
├── YES → CORRECT + REVERIFY
└── NO → REVALIDATE / REQUALIFY / REACCEPT / RESTRICT / REVOKE / REOPEN
```

## AI and Agent Verification

RG-213 SHALL verify that RG-212 correctly validated RG-211 treatment of:

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
| RG-212 Validation ID | Yes |
| RG-211 Verification ID | Yes |
| RG-210 Validation ID | Yes |
| RG-209 Verification ID | Yes |
| RG-208 Validation ID | Yes |
| RG-207 Verification ID | Yes |
| RG-206 Validation ID | Yes |
| RG-205 Verification ID | Yes |
| RG-204 Validation ID | Yes |
| RG-203 Verification ID | Yes |
| RG-202 Validation ID | Yes |
| RG-201 Verification ID | Yes |
| RG-200 Validation ID | Yes |
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
RG-204 → VALIDATE
RG-205 → VERIFY
RG-206 → VALIDATE
RG-207 → VERIFY
RG-208 → VALIDATE
RG-209 → VERIFY
RG-210 → VALIDATE
RG-211 → VERIFY
RG-212 → VALIDATE
RG-213 → VERIFY
```

Each layer SHALL preserve independent evidence, authority, criteria, decision and audit trail.

## Relationship to Reliance

RG-213 provides procedural assurance over RG-212. It does not replace the substantive validation performed by RG-212.

## Relationship to Revocation and Reopening

A material RG-213 verification failure may require correction, restriction, revocation, revalidation, requalification, reacceptance or governed reopening.

## Evidence Retention

RG-213 evidence SHALL remain linked to RG-212, RG-211, RG-210, RG-209, RG-208, RG-207, RG-206, RG-205, RG-204, RG-203, RG-202, RG-201, RG-200 and all preceding lifecycle assurance records.

## Next Document

`EA-IMETA-PC-RG-214`

## Final Principle

EA-IMETA SHALL REQUIRE MATERIAL POST-CLOSURE REGRESSION RELIANCE RESTORATION REACCEPTANCE REVALIDATION STATES TO HAVE THEIR SUBSTANTIVE VALIDATIONS PROCEDURALLY VERIFIED, WITH CURRENT STATE, EVIDENCE, AUTHORITY, SCOPE, CRITERIA, DECISION, IMPLEMENTATION, RISK, DEPENDENCIES, CONDITIONS AND INVALIDATING CONDITIONS TRACEABLE AND WITH VERIFIED, CONDITIONAL, NOT VERIFIED, FAILED AND INCONCLUSIVE STATES KEPT DISTINCT.

# END OF {short}

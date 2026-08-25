# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-REGRESSION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-146`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-146` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-REGRESSION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Determination |
| Parent | EA-IMETA-PC-RG-145 — Mandatory Post-Closure Regression Monitoring Deviation Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory regression-determination layer that determines whether a confirmed post-closure deviation represents a recurrence, return, re-emergence, persistence or materially equivalent manifestation of the previously governed regression condition, and therefore requires renewed response, revalidation, reopening or other controlled treatment.

## Core Principle
A deviation is not automatically a regression. Regression determination requires explicit linkage between the current governed deviation and the previously identified regression condition, including identity, causal or characteristic relationship, recurrence criteria, materiality, context and evidence. The determination shall be conservative where evidence is insufficient: unknown shall not be treated as no regression.

```text
CONFIRMED DEVIATION
        ↓
REGRESSION REFERENCE / PRIOR CONDITION IDENTIFIED?
├── NO → DEFINE / ESCALATE / INCONCLUSIVE
└── YES
     ↓
CURRENT CONDITION COMPARABLE TO PRIOR REGRESSION?
├── NO → NO REGRESSION / DIFFERENT CONDITION
└── YES
     ↓
REGRESSION CRITERIA SATISFIED?
├── NO → NO REGRESSION / WATCH
└── YES
     ↓
REGRESSION CONFIRMED
     ↓
CLASSIFY
     ↓
CONSEQUENCE / RESPONSE / REVALIDATION / REOPENING
```
## Regression Determination Quality Test
```text
CONFIRMED DEVIATION
+
AUTHORIZED PRIOR REGRESSION REFERENCE
+
VALID COMPARABILITY
+
APPLICABLE REGRESSION CRITERIA
+
SUFFICIENT EVIDENCE
+
CONTEXT / PERSISTENCE
+
ACCOUNTABLE DECISION
=
VALID GOVERNED REGRESSION DETERMINATION
```
## Deviation vs Regression
```text
DEVIATION
→ CURRENT CONDITION VIOLATES A GOVERNED CONDITION

REGRESSION
→ CURRENT DEVIATION REPRESENTS RETURN / RE-EMERGENCE / RECURRENCE OF THE GOVERNED REGRESSION CONDITION

DIFFERENT DEVIATION
→ MAY BE MATERIAL WITHOUT BEING THE SAME REGRESSION
```
## Regression Determination States
```text
RGD0 — REGRESSION DETERMINATION NOT REQUIRED
RGD1 — REGRESSION ASSESSMENT PENDING
RGD2 — REGRESSION ASSESSMENT IN PROGRESS
RGD3 — PRIOR REGRESSION REFERENCE CONFIRMED
RGD4 — COMPARABILITY CONFIRMED
RGD5 — NO REGRESSION
RGD6 — DIFFERENT DEVIATION
RGD7 — BORDERLINE / WATCH
RGD8 — REGRESSION INDICATED
RGD9 — REGRESSION CONFIRMED
RGD10 — MATERIAL REGRESSION
RGD11 — CRITICAL REGRESSION
RGD12 — REGRESSION INCONCLUSIVE
RGD13 — REFERENCE INVALID / UNAVAILABLE
RGD14 — EVIDENCE REQUIRED
RGD15 — ESCALATION REQUIRED
RGD16 — CONSEQUENCE ASSESSMENT READY
RGD17 — RESPONSE ASSESSMENT READY
RGD18 — REVALIDATION REQUIRED
RGD19 — REOPENING ASSESSMENT REQUIRED
RGDX — UNKNOWN / INSUFFICIENT BASIS
RGDS — REGRESSION ASSESSMENT SUSPENDED

## Regression Dimensions
| Dimension | Required determination |
|---|---|
| Current Deviation | Valid input |
| Prior Condition | Regression reference |
| Identity | Same / related condition |
| Comparability | Like-for-like basis |
| Criteria | Regression criteria |
| Recurrence | Return pattern |
| Persistence | Duration |
| Context | Operating conditions |
| Materiality | Significance |
| Severity | Impact level |
| Evidence | Supporting proof |
| Relationship | Current-to-prior linkage |
| Decision | Regression outcome |
| Handover | Next governed use |

## Regression Invariants

```text
ONLY VALIDATED AND CONFIRMED DEVIATIONS SHALL BE USED AS PRIMARY REGRESSION INPUTS
```

```text
A PRIOR REGRESSION CONDITION OR AUTHORIZED REFERENCE SHALL BE IDENTIFIABLE
```

```text
REGRESSION SHALL NOT BE CONFIRMED SOLELY BECAUSE A NEW DEVIATION EXISTS
```

```text
CURRENT AND PRIOR CONDITIONS SHALL BE COMPARABLE BEFORE RECURRENCE IS DETERMINED
```

```text
REGRESSION CRITERIA SHALL BE EXPLICIT AND APPLICABLE
```

```text
DIFFERENT DEVIATIONS SHALL REMAIN DISTINCT FROM REGRESSION
```

```text
BORDERLINE REGRESSION INDICATIONS SHALL REMAIN DISTINCT FROM CONFIRMED REGRESSION
```

```text
PERSISTENCE, RECURRENCE AND CONTEXT SHALL BE CONSIDERED WHERE RELEVANT
```

```text
MATERIAL REGRESSION SHALL NOT BE DOWNGRADED TO PRESERVE CLOSURE OR RELIANCE
```

```text
UNKNOWN OR INSUFFICIENT EVIDENCE SHALL NOT BE RECORDED AS NO REGRESSION
```

```text
SECURITY, RESILIENCE, SAFETY, COMPLIANCE AND DATA REGRESSION SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT REGRESSION SHALL CONSIDER POLICY, AUTHORITY, BEHAVIOR, TOOL, DATA AND MODEL CONTEXT
```

```text
REGRESSION DETERMINATION SHALL REMAIN DISTINCT FROM CONSEQUENCE AND RESPONSE DETERMINATION
```

```text
CONFIRMED REGRESSION SHALL BE AVAILABLE AS INPUT TO CONSEQUENCE, RESPONSE, REVALIDATION AND REOPENING
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

```text
REGRESSION RECORDS SHALL PRESERVE CURRENT-TO-PRIOR LINKAGE FOR FUTURE LEARNING
```

## 1. Regression Domain — Post-Closure Regression Determination Governance

**Control family:** `PCRG-001`

The Post-Closure Regression Determination Governance domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-001-01` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-001-02` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-001-03` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-001-04` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-001-05` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-001-06` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-001-07` — Establish and maintain the post-closure regression determination governance control.
- `PCRG-001-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 2. Regression Domain — Post-Closure Regression Determination Objective

**Control family:** `PCRG-002`

The Post-Closure Regression Determination Objective domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-002-01` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-002-02` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-002-03` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-002-04` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-002-05` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-002-06` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-002-07` — Establish and maintain the post-closure regression determination objective control.
- `PCRG-002-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 3. Regression Domain — Post-Closure Regression Determination Definition

**Control family:** `PCRG-003`

The Post-Closure Regression Determination Definition domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-003-01` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-003-02` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-003-03` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-003-04` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-003-05` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-003-06` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-003-07` — Establish and maintain the post-closure regression determination definition control.
- `PCRG-003-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 4. Regression Domain — Post-Closure Regression Determination Scope

**Control family:** `PCRG-004`

The Post-Closure Regression Determination Scope domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-004-01` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-004-02` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-004-03` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-004-04` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-004-05` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-004-06` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-004-07` — Establish and maintain the post-closure regression determination scope control.
- `PCRG-004-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 5. Regression Domain — Post-Closure Regression Determination Authority

**Control family:** `PCRG-005`

The Post-Closure Regression Determination Authority domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-005-01` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-005-02` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-005-03` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-005-04` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-005-05` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-005-06` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-005-07` — Establish and maintain the post-closure regression determination authority control.
- `PCRG-005-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 6. Regression Domain — Post-Closure Regression Determination Criteria

**Control family:** `PCRG-006`

The Post-Closure Regression Determination Criteria domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-006-01` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-006-02` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-006-03` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-006-04` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-006-05` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-006-06` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-006-07` — Establish and maintain the post-closure regression determination criteria control.
- `PCRG-006-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 7. Regression Domain — Post-Closure Regression Determination Preconditions

**Control family:** `PCRG-007`

The Post-Closure Regression Determination Preconditions domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-007-01` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-007-02` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-007-03` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-007-04` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-007-05` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-007-06` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-007-07` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRG-007-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 8. Regression Domain — Post-Closure Regression Determination Evidence

**Control family:** `PCRG-008`

The Post-Closure Regression Determination Evidence domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-008-01` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-008-02` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-008-03` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-008-04` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-008-05` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-008-06` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-008-07` — Establish and maintain the post-closure regression determination evidence control.
- `PCRG-008-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 9. Regression Domain — Post-Closure Regression Determination Method

**Control family:** `PCRG-009`

The Post-Closure Regression Determination Method domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-009-01` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-009-02` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-009-03` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-009-04` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-009-05` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-009-06` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-009-07` — Establish and maintain the post-closure regression determination method control.
- `PCRG-009-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 10. Regression Domain — Post-Closure Regression Determination Decision

**Control family:** `PCRG-010`

The Post-Closure Regression Determination Decision domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-010-01` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-010-02` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-010-03` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-010-04` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-010-05` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-010-06` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-010-07` — Establish and maintain the post-closure regression determination decision control.
- `PCRG-010-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 11. Regression Domain — Post-Closure Regression Determination Accountability

**Control family:** `PCRG-011`

The Post-Closure Regression Determination Accountability domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-011-01` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-011-02` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-011-03` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-011-04` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-011-05` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-011-06` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-011-07` — Establish and maintain the post-closure regression determination accountability control.
- `PCRG-011-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 12. Regression Domain — Post-Closure Regression Determination Timing

**Control family:** `PCRG-012`

The Post-Closure Regression Determination Timing domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-012-01` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-012-02` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-012-03` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-012-04` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-012-05` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-012-06` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-012-07` — Establish and maintain the post-closure regression determination timing control.
- `PCRG-012-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 13. Regression Domain — Security Post-Closure Regression Determination

**Control family:** `PCRG-013`

The Security Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-013-01` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-013-02` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-013-03` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-013-04` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-013-05` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-013-06` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-013-07` — Establish and maintain the security post-closure regression determination control.
- `PCRG-013-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 14. Regression Domain — Resilience Post-Closure Regression Determination

**Control family:** `PCRG-014`

The Resilience Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-014-01` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-014-02` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-014-03` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-014-04` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-014-05` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-014-06` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-014-07` — Establish and maintain the resilience post-closure regression determination control.
- `PCRG-014-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 15. Regression Domain — Compliance Post-Closure Regression Determination

**Control family:** `PCRG-015`

The Compliance Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-015-01` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-015-02` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-015-03` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-015-04` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-015-05` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-015-06` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-015-07` — Establish and maintain the compliance post-closure regression determination control.
- `PCRG-015-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 16. Regression Domain — Data Post-Closure Regression Determination

**Control family:** `PCRG-016`

The Data Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-016-01` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-016-02` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-016-03` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-016-04` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-016-05` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-016-06` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-016-07` — Establish and maintain the data post-closure regression determination control.
- `PCRG-016-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 17. Regression Domain — AI and Agent Post-Closure Regression Determination

**Control family:** `PCRG-017`

The AI and Agent Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-017-01` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-017-02` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-017-03` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-017-04` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-017-05` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-017-06` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-017-07` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRG-017-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 18. Regression Domain — Post-Closure Regression Determination Failure

**Control family:** `PCRG-018`

The Post-Closure Regression Determination Failure domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-018-01` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-018-02` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-018-03` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-018-04` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-018-05` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-018-06` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-018-07` — Establish and maintain the post-closure regression determination failure control.
- `PCRG-018-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 19. Regression Domain — Post-Closure Regression Determination Independence

**Control family:** `PCRG-019`

The Post-Closure Regression Determination Independence domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-019-01` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-019-02` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-019-03` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-019-04` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-019-05` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-019-06` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-019-07` — Establish and maintain the post-closure regression determination independence control.
- `PCRG-019-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## 20. Regression Domain — Post-Closure Regression Determination Review and Learning

**Control family:** `PCRG-020`

The Post-Closure Regression Determination Review and Learning domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRG-020-01` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-01-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-020-02` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-02-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-020-03` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-03-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-020-04` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-04-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-020-05` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-05-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-020-06` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-06-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.
- `PCRG-020-07` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRG-020-07-E` — Preserve current deviation, prior condition, identity, comparability, criteria, recurrence, persistence, context, materiality, severity, evidence, relationship, decision and handover traceability.

```text
DEVIATION → PRIOR CONDITION → COMPARE → APPLY REGRESSION CRITERIA → CONFIRM / REJECT REGRESSION → HANDOVER
```

## Post-Closure Regression Determination Structure

| Element | Required definition |
|---|---|
| Current Deviation | Current governed condition |
| Prior Condition | Reference regression |
| Identity | Condition relationship |
| Comparability | Comparison basis |
| Criteria | Regression rules |
| Recurrence | Return pattern |
| Persistence | Duration |
| Context | Operating conditions |
| Materiality | Significance |
| Severity | Impact |
| Evidence | Proof |
| Relationship | Current-to-prior linkage |
| Decision | Outcome |

## Post-Closure Regression Determination Objective

Determine whether the current confirmed deviation is a recurrence, return, re-emergence or materially equivalent manifestation of the previously governed regression condition.

## Post-Closure Regression Determination Definition

Regression determination is the governed decision that a current deviation satisfies the applicable relationship, comparability, recurrence, persistence and materiality criteria linking it to a prior regression condition.

## Post-Closure Regression Determination Scope

Scope includes prior condition identification, current condition analysis, comparability, recurrence, persistence, context, materiality, severity, evidence and current-to-prior linkage.

## Post-Closure Regression Determination Authority

Authority shall define who may confirm, reject, classify, override, escalate or require further evidence for a regression determination.

## Post-Closure Regression Determination Criteria

Criteria shall distinguish no regression, different deviation, borderline indication, confirmed regression, material regression and critical regression.
```text
CONFIRMED DEVIATION
↓
PRIOR REGRESSION REFERENCE VALID?
├── NO → INCONCLUSIVE / DEFINE / ESCALATE
└── YES
     ↓
CURRENT CONDITION COMPARABLE?
├── NO → DIFFERENT DEVIATION
└── YES
     ↓
RECURRENCE / RETURN CRITERIA SATISFIED?
├── NO → NO REGRESSION / WATCH
└── YES → REGRESSION CONFIRMED
     ↓
MATERIALITY / SEVERITY
     ↓
CONSEQUENCE / RESPONSE / REVALIDATION / REOPENING
```

## Post-Closure Regression Determination Preconditions

Preconditions include confirmed deviation, authoritative prior regression reference where required, sufficient evidence, valid comparability and authorized criteria.

## Post-Closure Regression Determination Evidence

Evidence shall preserve current deviation, prior condition, timestamps, context, comparison basis, recurrence evidence, persistence, materiality, severity, decision and authority.

## Post-Closure Regression Determination Method

Methods may include condition fingerprinting, recurrence analysis, characteristic comparison, causal linkage, temporal analysis, trend/persistence analysis and independent review.
```text
CURRENT DEVIATION → PRIOR REGRESSION → ALIGN → COMPARE CHARACTERISTICS → ASSESS RECURRENCE → DETERMINE REGRESSION
```

## Post-Closure Regression Determination Decision

Decision shall determine RGD0, RGD1, RGD2, RGD3, RGD4, RGD5, RGD6, RGD7, RGD8, RGD9, RGD10, RGD11, RGD12, RGD13, RGD14, RGD15, RGD16, RGD17, RGD18, RGD19, RGDX or RGDS.

## Post-Closure Regression Determination Accountability

Accountability shall remain explicit for prior-condition selection, comparability, criteria, relationship assessment, classification and downstream handover.

## Post-Closure Regression Determination Timing

Regression determination shall occur within the required governance window where the current deviation may affect safety, security, resilience, compliance, reliance or other consequential conditions.

## Security Post-Closure Regression Determination

Security regression shall consider recurrence of unauthorized access, control bypass, exposure, integrity compromise or related security failure characteristics.

## Resilience Post-Closure Regression Determination

Resilience regression shall consider recurrence of service degradation, dependency failure, recovery failure, continuity loss or equivalent failure patterns.

## Compliance Post-Closure Regression Determination

Compliance regression shall consider recurrence of previously identified control failures, obligation breaches or evidence deficiencies.

## Data Post-Closure Regression Determination

Data regression shall consider recurrence of integrity, lineage, completeness, consistency, corruption, loss or unauthorized alteration conditions.

## AI and Agent Post-Closure Regression Determination

AI/agent regression shall consider recurrence of policy violations, authority overreach, unsafe behavior, tool misuse, data misuse, model drift or equivalent consequential behavior.
```text
CURRENT AI / AGENT DEVIATION
↓
PRIOR GOVERNED REGRESSION CONDITION
↓
MODEL / POLICY / AUTHORITY / TOOL / DATA / BEHAVIOR COMPARABILITY
↓
RECURRENCE?
├── NO → DIFFERENT CONDITION / WATCH
└── YES → REGRESSION CONFIRMED
```

## Post-Closure Regression Determination Failure

Failure includes invalid prior reference, incomparable conditions, insufficient recurrence evidence, hidden persistence or unsupported confirmation/rejection.
```text
REGRESSION ASSESSMENT FAILURE
↓
MATERIAL?
├── YES → HOLD / ESCALATE / REVALIDATE / REOPEN AS GOVERNED
└── NO → CORRECT / RECORD
```

## Post-Closure Regression Determination Independence

Independent determination shall be used where classification bias, organizational pressure, consequence or governance requirements make independence necessary.

## Post-Closure Regression Determination Review and Learning

Reviews shall examine false regression confirmations, missed recurrence, incorrect prior references, changed contexts, weak condition fingerprints and regressions discovered only after reopening.

## Regression Decision Model
```text
CONFIRMED DEVIATION
↓
IDENTIFY PRIOR REGRESSION CONDITION
↓
VALID REFERENCE?
├── NO → INCONCLUSIVE / ESCALATE
└── YES
     ↓
COMPARE CURRENT / PRIOR CONDITION
     ↓
COMPARABLE?
├── NO → DIFFERENT DEVIATION
└── YES
     ↓
RECURRENCE / RETURN / RE-EMERGENCE?
├── NO → NO REGRESSION / WATCH
└── YES
     ↓
MATERIALITY + SEVERITY + PERSISTENCE
     ↓
CLASSIFY
├── REGRESSION
├── MATERIAL REGRESSION
└── CRITICAL REGRESSION
     ↓
CONSEQUENCE / RESPONSE / REVALIDATION / REOPENING
```

## Regression Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| RGD0 | Not required | Record basis |
| RGD1 | Pending | Prepare assessment |
| RGD2 | In progress | Assess |
| RGD3 | Prior reference confirmed | Continue |
| RGD4 | Comparability confirmed | Continue |
| RGD5 | No regression | Continue / monitor |
| RGD6 | Different deviation | Govern separately |
| RGD7 | Borderline / watch | Increased monitoring / review |
| RGD8 | Regression indicated | Investigate / confirm |
| RGD9 | Regression confirmed | Govern regression |
| RGD10 | Material regression | Consequence / response |
| RGD11 | Critical regression | Immediate escalation |
| RGD12 | Inconclusive | Evidence / escalation |
| RGD13 | Reference invalid | Correct / reconstruct |
| RGD14 | Evidence required | Supplement |
| RGD15 | Escalation required | Escalate |
| RGD16 | Consequence ready | Determine consequence |
| RGD17 | Response ready | Determine response |
| RGD18 | Revalidation required | Revalidate |
| RGD19 | Reopening assessment | Assess reopening |
| RGDX | Unknown | Do not assume no regression |
| RGDS | Suspended | Restore assessment |

## Regression Record
| Field | Required |
|---|---|
| Regression ID | Yes |
| Deviation ID | Yes |
| Prior Regression ID | Where applicable |
| Prior Condition | Yes |
| Current Condition | Yes |
| Identity / Relationship | Yes |
| Comparability | Yes |
| Criteria Version | Yes |
| Recurrence | Yes |
| Persistence | Where applicable |
| Context | Yes |
| Materiality | Yes |
| Severity | Yes |
| Evidence | Yes |
| Regression State | Yes |
| Decision | Yes |
| Authority | Yes |
| Audit Trail | Yes |

## Regression Is Not Deviation
A current deviation may be material without being a recurrence of the prior regression condition.
```text
DEVIATION
≠
REGRESSION
```

## Regression Is Not Consequence
Regression identifies the recurrence relationship. Consequence determination establishes the governed effect.
```text
REGRESSION
≠
CONSEQUENCE
```

## Regression Is Not Response
A confirmed regression may require response, but response remains a separate governed layer.
```text
REGRESSION
≠
RESPONSE EXECUTED
```

## Regression Is Not Revalidation
Regression determination identifies recurrence. Revalidation determines whether the governed state can remain accepted or relied upon.
```text
REGRESSION
≠
REVALIDATED STATE
```

## Prior Condition Integrity
The prior regression condition shall be authoritative, traceable and sufficiently described to support current-to-prior assessment.

## Comparability
Current and prior conditions shall be compared using relevant dimensions and normalized where required. Material contextual changes shall be explicitly considered.

## Recurrence
Recurrence may include exact recurrence, functional recurrence, characteristic recurrence or materially equivalent manifestation where criteria permit.

## Persistence
A continuing condition shall be distinguished from a transient event where persistence affects the regression determination.

## Different Deviation
A different deviation shall not be forced into the prior regression category merely because it occurs in the same system or domain.

## AI and Agent Regression
AI/agent regression assessment shall preserve sufficient model, policy, authority, tool, data and behavior context to establish whether the current behavior is genuinely related to the prior condition.

## Relationship to Consequence
RG-146 supplies confirmed regression states to the subsequent consequence-determination layer.
```text
DEVIATION → REGRESSION → CONSEQUENCE
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression determination layer beneath deviation and above consequence determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, qualification, comparison, deviation, regression classification, consequence determination, alert determination, notification determination, acknowledgement determination, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring activation, monitoring execution, result validation, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Regression Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → DEVIATION → MANDATORY REGRESSION DETERMINATION → CONSEQUENCE → RESPONSE → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REOPENING
```

## Complete Regression Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ISSUE ALERT → DETERMINE NOTIFICATION → ISSUE NOTIFICATION → DELIVER → DETERMINE ACKNOWLEDGEMENT → VALIDATE ACTOR / TIMING / COMPLETENESS → ACKNOWLEDGE → ACCEPT / ASSIGN → DETERMINE RESPONSE INITIATION → AUTHORIZE → ASSIGN → ACTIVATE → VERIFY → DETERMINE AUTHORITY TRANSFER → IDENTIFY RECEIVER → PACKAGE STATE → ACCEPT → VERIFY → ACTIVATE RECEIVING AUTHORITY → DETERMINE EXECUTION → AUTHORIZE ACTION → EXECUTE → OBSERVE → VERIFY → ADJUST / ESCALATE / ROLLBACK / STOP → COMPLETE → DETERMINE EFFECTIVENESS → VERIFY → DETERMINE RESOLUTION → RESTORE / CONTROL CONDITION → VERIFY → DETERMINE CLOSURE → COMPLETE OBLIGATIONS → CONFIRM EVIDENCE / RISK / HANDOVER → AUTHORIZE → VERIFY → CLOSE → DETERMINE MONITORING REQUIREMENT → DEFINE OBJECTIVE / SCOPE / OWNER / AUTHORITY / SIGNALS / THRESHOLDS / CADENCE / DURATION / EVIDENCE / ESCALATION → AUTHORIZE → ACTIVATE → VERIFY → EXECUTE MONITORING → OBSERVE → MEASURE → VALIDATE EXECUTION DATA → DETERMINE RESULT → VALIDATE RESULT → QUALIFY RESULT → COMPARE RESULT WITH AUTHORIZED TARGET → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-147` — Mandatory Post-Closure Regression Consequence Determination

## Final Principle
EA-IMETA SHALL REQUIRE ALL MATERIAL POST-CLOSURE DEVIATIONS TO BE ASSESSED FOR REGRESSION ONLY THROUGH EXPLICIT CURRENT-TO-PRIOR CONDITION LINKAGE, VALID COMPARABILITY, APPLICABLE RECURRENCE CRITERIA, SUFFICIENT EVIDENCE, CONTEXT, PERSISTENCE, MATERIALITY AND SEVERITY, WITH DIFFERENT DEVIATIONS, BORDERLINE INDICATIONS, CONFIRMED REGRESSIONS, MATERIAL REGRESSIONS AND CRITICAL REGRESSIONS KEPT DISTINCT, AND WITH UNKNOWN OR INSUFFICIENT EVIDENCE NEVER TREATED AS NO REGRESSION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-REGRESSION-DETERMINATION-01

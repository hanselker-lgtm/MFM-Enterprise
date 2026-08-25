# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-128`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-128` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Determination |
| Parent | EA-IMETA-PC-RG-127 — Mandatory Post-Closure Monitoring Deviation Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory regression-determination layer that decides whether governed post-closure monitoring evidence demonstrates deterioration from a previously accepted, restored, resolved or controlled state, and therefore requires entry into the defined regression response governance path.

## Core Principle
A deviation is not automatically a regression. Regression determination requires evidence of deterioration against the relevant previously accepted or resolved state, with temporal context, persistence or recurrence, materiality and causal relevance assessed where applicable. The determination shall remain independent of the desire to preserve closure.

```text
VALIDATED RESULT
↓
QUALIFIED RESULT
↓
COMPARISON
↓
DEVIATION / REGRESSION-INDICATING CONDITION
↓
PREVIOUSLY ACCEPTED / RESOLVED STATE VALID?
├── NO → REGRESSION UNDETERMINED
└── YES
     ↓
CURRENT STATE WORSE THAN ACCEPTED STATE?
├── NO → NO REGRESSION
└── YES
     ↓
PERSISTENCE / RECURRENCE / MATERIALITY
     ↓
REGRESSION DETERMINATION
├── NOT REGRESSION
├── POTENTIAL REGRESSION
├── CONFIRMED REGRESSION
└── UNDETERMINED
     ↓
ENTER REGRESSION RESPONSE GOVERNANCE
```
## Regression Quality Test
```text
VALID MONITORING EVIDENCE
+
VALID PREVIOUSLY ACCEPTED / RESOLVED STATE
+
CONTEXT ALIGNMENT
+
EVIDENCE OF DETERIORATION
+
TEMPORAL / PERSISTENCE ASSESSMENT
+
MATERIALITY / CONSEQUENCE RELEVANCE
+
TRACEABLE DETERMINATION
+
AUTHORIZED GOVERNANCE DECISION
=
VALID GOVERNED REGRESSION DETERMINATION
```
## Deviation vs Regression
```text
DEVIATION
→ FAILURE TO MEET AN APPROVED CURRENT REQUIREMENT / TOLERANCE / THRESHOLD

REGRESSION
→ DETERIORATION FROM A PREVIOUSLY ACCEPTED, RESOLVED OR CONTROLLED STATE

A REGRESSION MAY ALSO BE A DEVIATION,
BUT A DEVIATION IS NOT AUTOMATICALLY A REGRESSION.
```
## Regression States
```text
R0 — REGRESSION NOT REQUIRED
R1 — REGRESSION ASSESSMENT PENDING
R2 — BASELINE / ACCEPTED STATE VALIDATION
R3 — TEMPORAL COMPARISON IN PROGRESS
R4 — NO REGRESSION
R5 — POTENTIAL REGRESSION
R6 — CONFIRMED REGRESSION
R7 — PERSISTENT REGRESSION
R8 — RECURRENT REGRESSION
R9 — MATERIAL / CRITICAL REGRESSION
RX — UNKNOWN / INSUFFICIENT BASIS
RR — REGRESSION DETERMINATION REJECTED / REASSESSMENT
RS — REGRESSION ASSESSMENT SUSPENDED
```
## Regression Dimensions
| Dimension | Required determination |
|---|---|
| Previous State | Accepted / resolved / controlled state |
| Current State | Current monitored state |
| Context | Context alignment |
| Difference | State deterioration |
| Time | Temporal relationship |
| Persistence | Sustained deterioration |
| Recurrence | Repeated deterioration |
| Materiality | Decision relevance |
| Consequence | Potential impact |
| Causality / Relevance | Relationship where required |
| Confidence | Determination confidence |
| Evidence | Supporting evidence |
| Authority | Determination authority |

## Regression Invariants

```text
REGRESSION SHALL REQUIRE A VALID REFERENCE TO A PREVIOUSLY ACCEPTED, RESOLVED OR CONTROLLED STATE WHERE SUCH REFERENCE IS MATERIAL
```

```text
REGRESSION SHALL BE DETERMINED FROM VALIDATED AND QUALIFIED MONITORING EVIDENCE
```

```text
CURRENT AND PREVIOUS STATES SHALL BE CONTEXTUALLY ALIGNED
```

```text
REGRESSION SHALL REQUIRE EVIDENCE OF DETERIORATION, NOT MERELY DIFFERENCE
```

```text
PERSISTENCE AND RECURRENCE SHALL BE CONSIDERED WHERE RELEVANT
```

```text
MATERIALITY AND CONSEQUENCE RELEVANCE SHALL BE ASSESSED WHERE THEY CAN CHANGE GOVERNANCE RESPONSE
```

```text
NO REGRESSION SHALL NOT MEAN NO FUTURE REGRESSION RISK
```

```text
UNKNOWN SHALL NOT BE TREATED AS NO REGRESSION
```

```text
REGRESSION DETERMINATION SHALL BE INDEPENDENT OF THE DESIRE TO PRESERVE CASE CLOSURE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE REGRESSION SHALL USE DOMAIN-APPROPRIATE ACCEPTED STATES
```

```text
AI AND AGENT REGRESSION SHALL CONSIDER BEHAVIOR, AUTHORITY, TOOL, DATA AND OVERSIGHT BASELINES
```

```text
CAUSALITY SHALL NOT BE CLAIMED WHERE EVIDENCE ONLY ESTABLISHES TEMPORAL OR CORRELATIONAL RELATIONSHIP
```

```text
OVERRIDES SHALL BE EXPLICITLY AUTHORIZED AND TRACEABLE
```

```text
CONFLICTING EVIDENCE SHALL BE RESOLVED OR ESCALATED
```

```text
REGRESSION RECORDS SHALL PRESERVE BOTH THE PREVIOUS STATE AND CURRENT EVIDENCE
```

```text
REGRESSION RULES SHALL BE REVIEWED AFTER FALSE POSITIVES, FALSE NEGATIVES OR MISSED REGRESSIONS
```

## 1. Regression Domain — Post-Closure Regression Determination Governance

**Control family:** `PCRD-001`

The Post-Closure Regression Determination Governance domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-001-01` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-001-02` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-001-03` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-001-04` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-001-05` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-001-06` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-001-07` — Establish and maintain the post-closure regression determination governance control.
- `PCRD-001-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 2. Regression Domain — Post-Closure Regression Determination Objective

**Control family:** `PCRD-002`

The Post-Closure Regression Determination Objective domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-002-01` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-002-02` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-002-03` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-002-04` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-002-05` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-002-06` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-002-07` — Establish and maintain the post-closure regression determination objective control.
- `PCRD-002-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 3. Regression Domain — Post-Closure Regression Determination Definition

**Control family:** `PCRD-003`

The Post-Closure Regression Determination Definition domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-003-01` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-003-02` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-003-03` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-003-04` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-003-05` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-003-06` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-003-07` — Establish and maintain the post-closure regression determination definition control.
- `PCRD-003-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 4. Regression Domain — Post-Closure Regression Determination Scope

**Control family:** `PCRD-004`

The Post-Closure Regression Determination Scope domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-004-01` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-004-02` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-004-03` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-004-04` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-004-05` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-004-06` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-004-07` — Establish and maintain the post-closure regression determination scope control.
- `PCRD-004-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 5. Regression Domain — Post-Closure Regression Determination Authority

**Control family:** `PCRD-005`

The Post-Closure Regression Determination Authority domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-005-01` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-005-02` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-005-03` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-005-04` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-005-05` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-005-06` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-005-07` — Establish and maintain the post-closure regression determination authority control.
- `PCRD-005-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 6. Regression Domain — Post-Closure Regression Determination Criteria

**Control family:** `PCRD-006`

The Post-Closure Regression Determination Criteria domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-006-01` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-006-02` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-006-03` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-006-04` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-006-05` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-006-06` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-006-07` — Establish and maintain the post-closure regression determination criteria control.
- `PCRD-006-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 7. Regression Domain — Post-Closure Regression Determination Preconditions

**Control family:** `PCRD-007`

The Post-Closure Regression Determination Preconditions domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-007-01` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-007-02` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-007-03` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-007-04` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-007-05` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-007-06` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-007-07` — Establish and maintain the post-closure regression determination preconditions control.
- `PCRD-007-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 8. Regression Domain — Post-Closure Regression Determination Evidence

**Control family:** `PCRD-008`

The Post-Closure Regression Determination Evidence domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-008-01` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-008-02` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-008-03` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-008-04` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-008-05` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-008-06` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-008-07` — Establish and maintain the post-closure regression determination evidence control.
- `PCRD-008-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 9. Regression Domain — Post-Closure Regression Determination Method

**Control family:** `PCRD-009`

The Post-Closure Regression Determination Method domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-009-01` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-009-02` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-009-03` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-009-04` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-009-05` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-009-06` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-009-07` — Establish and maintain the post-closure regression determination method control.
- `PCRD-009-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 10. Regression Domain — Post-Closure Regression Determination Decision

**Control family:** `PCRD-010`

The Post-Closure Regression Determination Decision domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-010-01` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-010-02` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-010-03` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-010-04` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-010-05` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-010-06` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-010-07` — Establish and maintain the post-closure regression determination decision control.
- `PCRD-010-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 11. Regression Domain — Post-Closure Regression Determination Accountability

**Control family:** `PCRD-011`

The Post-Closure Regression Determination Accountability domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-011-01` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-011-02` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-011-03` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-011-04` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-011-05` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-011-06` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-011-07` — Establish and maintain the post-closure regression determination accountability control.
- `PCRD-011-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 12. Regression Domain — Post-Closure Regression Determination Timing

**Control family:** `PCRD-012`

The Post-Closure Regression Determination Timing domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-012-01` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-012-02` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-012-03` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-012-04` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-012-05` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-012-06` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-012-07` — Establish and maintain the post-closure regression determination timing control.
- `PCRD-012-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 13. Regression Domain — Security Post-Closure Regression Determination

**Control family:** `PCRD-013`

The Security Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-013-01` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-013-02` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-013-03` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-013-04` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-013-05` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-013-06` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-013-07` — Establish and maintain the security post-closure regression determination control.
- `PCRD-013-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 14. Regression Domain — Resilience Post-Closure Regression Determination

**Control family:** `PCRD-014`

The Resilience Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-014-01` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-014-02` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-014-03` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-014-04` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-014-05` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-014-06` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-014-07` — Establish and maintain the resilience post-closure regression determination control.
- `PCRD-014-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 15. Regression Domain — Compliance Post-Closure Regression Determination

**Control family:** `PCRD-015`

The Compliance Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-015-01` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-015-02` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-015-03` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-015-04` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-015-05` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-015-06` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-015-07` — Establish and maintain the compliance post-closure regression determination control.
- `PCRD-015-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 16. Regression Domain — Data Post-Closure Regression Determination

**Control family:** `PCRD-016`

The Data Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-016-01` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-016-02` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-016-03` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-016-04` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-016-05` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-016-06` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-016-07` — Establish and maintain the data post-closure regression determination control.
- `PCRD-016-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 17. Regression Domain — AI and Agent Post-Closure Regression Determination

**Control family:** `PCRD-017`

The AI and Agent Post-Closure Regression Determination domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-017-01` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-017-02` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-017-03` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-017-04` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-017-05` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-017-06` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-017-07` — Establish and maintain the ai and agent post-closure regression determination control.
- `PCRD-017-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 18. Regression Domain — Post-Closure Regression Determination Failure

**Control family:** `PCRD-018`

The Post-Closure Regression Determination Failure domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-018-01` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-018-02` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-018-03` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-018-04` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-018-05` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-018-06` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-018-07` — Establish and maintain the post-closure regression determination failure control.
- `PCRD-018-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 19. Regression Domain — Post-Closure Regression Determination Independence

**Control family:** `PCRD-019`

The Post-Closure Regression Determination Independence domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-019-01` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-019-02` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-019-03` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-019-04` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-019-05` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-019-06` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-019-07` — Establish and maintain the post-closure regression determination independence control.
- `PCRD-019-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## 20. Regression Domain — Post-Closure Regression Determination Review and Learning

**Control family:** `PCRD-020`

The Post-Closure Regression Determination Review and Learning domain establishes governed mandatory regression-determination requirements.

### Required controls
- `PCRD-020-01` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-01-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-020-02` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-02-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-020-03` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-03-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-020-04` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-04-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-020-05` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-05-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-020-06` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-06-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.
- `PCRD-020-07` — Establish and maintain the post-closure regression determination review and learning control.
- `PCRD-020-07-E` — Preserve previous state, current state, context, difference, time, persistence, recurrence, materiality, consequence, causal/relevance assessment, confidence, evidence and authority traceability.

```text
ESTABLISH PREVIOUS STATE → COMPARE CURRENT STATE → ASSESS DETERIORATION → DETERMINE REGRESSION
```

## Post-Closure Regression Determination Structure

| Element | Required definition |
|---|---|
| Previous State | Accepted / resolved / controlled state |
| Current State | Current monitored state |
| Context | Context alignment |
| Difference | Deterioration |
| Time | Temporal relationship |
| Persistence | Sustained condition |
| Recurrence | Repeated condition |
| Materiality | Decision relevance |
| Consequence | Potential impact |
| Causality / Relevance | Relationship assessment |
| Confidence | Determination confidence |
| Evidence | Supporting evidence |

## Post-Closure Regression Determination Objective

Determine whether the current monitored state demonstrates governed deterioration from the relevant previously accepted, resolved or controlled state.

## Post-Closure Regression Determination Definition

Regression determination is the governed decision that a monitored condition has materially or otherwise meaningfully deteriorated from a previously accepted, resolved or controlled state according to approved criteria.

## Post-Closure Regression Determination Scope

Scope includes deterioration of restored controls, recurrence of previously resolved conditions, degradation of performance, reappearance of prior failure modes and material loss of reliance.

## Post-Closure Regression Determination Authority

Authority shall define who may determine, reject, override, escalate or independently review a regression determination.

## Post-Closure Regression Determination Criteria

Criteria shall define previous state, current state, context, deterioration, time, persistence, recurrence, materiality and consequence relevance.
```text
CURRENT STATE
↓
PREVIOUS ACCEPTED / RESOLVED STATE VALID?
├── NO → UNDETERMINED
└── YES
     ↓
DETERIORATION?
├── NO → NO REGRESSION
└── YES
     ↓
PERSISTENCE / RECURRENCE
     ↓
MATERIALITY / CONSEQUENCE
     ↓
POTENTIAL / CONFIRMED / MATERIAL REGRESSION
```

## Post-Closure Regression Determination Preconditions

Preconditions include validated monitoring results, qualification, comparison, deviation assessment where applicable, and a valid previous accepted/resolved state.

## Post-Closure Regression Determination Evidence

Evidence shall preserve previous state, current result, comparison, time relationship, persistence/recurrence, materiality, consequence relevance, determination and authority.

## Post-Closure Regression Determination Method

Methods may include state comparison, longitudinal analysis, trend analysis, recurrence analysis, control-effectiveness analysis, causal/relevance assessment and independent review.
```text
PREVIOUS STATE → CURRENT STATE → ALIGN CONTEXT → ASSESS DETERIORATION → ASSESS PERSISTENCE → ASSESS MATERIALITY → DETERMINE REGRESSION
```

## Post-Closure Regression Determination Decision

Decision shall determine R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, RX, RR or RS and the associated next action.

## Post-Closure Regression Determination Accountability

Accountability shall remain explicit for accepted-state integrity, criteria, determination quality, overrides and escalation.

## Post-Closure Regression Determination Timing

Regression determination shall occur early enough to initiate the defined response before material consequence becomes uncontrolled.

## Security Post-Closure Regression Determination

Security regression shall consider deterioration in access control, exposure, detection, prevention, containment or other approved security-state measures.

## Resilience Post-Closure Regression Determination

Resilience regression shall consider deterioration in availability, capacity, redundancy, recovery capability, fallback readiness and service resilience.

## Compliance Post-Closure Regression Determination

Compliance regression shall consider deterioration from previously accepted control effectiveness, obligation fulfillment or evidence conditions.

## Data Post-Closure Regression Determination

Data regression shall consider deterioration in integrity, quality, lineage, availability, confidentiality or downstream reliability from the accepted state.

## AI and Agent Post-Closure Regression Determination

AI/agent regression shall consider deterioration in approved behavior, authority boundaries, tool use, data handling, autonomy and oversight.
```text
AI / AGENT CURRENT STATE
↓
PREVIOUS APPROVED STATE
↓
COMPARE
↓
DETERIORATION?
↓
PERSISTENCE / MATERIALITY
↓
REGRESSION DETERMINATION
```

## Post-Closure Regression Determination Failure

Failure includes invalid previous state, context mismatch, insufficient evidence, ambiguous deterioration, conflicting evidence or inability to establish a reliable determination.
```text
REGRESSION ASSESSMENT FAILURE
↓
MATERIAL DECISION AFFECTED?
├── YES → REASSESS / INDEPENDENT REVIEW / ESCALATE
└── NO → CORRECT / RECORD
```

## Post-Closure Regression Determination Independence

Independent determination may be required where regression materially affects reopening, safety, security, compliance, reliance restoration or high-consequence response.

## Post-Closure Regression Determination Review and Learning

Reviews shall examine missed regressions, false positives, false negatives, baseline drift, recurrence patterns, monitoring blind spots and ineffective regression criteria.

## Regression Decision Model
```text
CURRENT VALIDATED STATE
↓
PREVIOUS ACCEPTED / RESOLVED STATE VALID?
├── NO → REGRESSION UNDETERMINED
└── YES
     ↓
CONTEXT ALIGNED?
├── NO → RECONTEXTUALIZE / REASSESS
└── YES
     ↓
CURRENT STATE WORSE?
├── NO → NO REGRESSION
└── YES
     ↓
PERSISTENT / RECURRENT?
├── NO → POTENTIAL REGRESSION
└── YES → CONFIRMED / MATERIAL REGRESSION
     ↓
MATERIALITY / CONSEQUENCE
├── LOW / CONTROLLED
├── MATERIAL
└── CRITICAL
     ↓
ENTER REGRESSION RESPONSE GOVERNANCE
```

## Regression Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| R0 | Not required | Record basis |
| R1 | Assessment pending | Assess |
| R2 | Previous state validation | Validate reference |
| R3 | Temporal comparison in progress | Complete comparison |
| R4 | No regression | Continue monitoring |
| R5 | Potential regression | Increase observation / investigate |
| R6 | Confirmed regression | Enter response governance |
| R7 | Persistent regression | Escalate / systemic assessment |
| R8 | Recurrent regression | Systemic / recurrence response |
| R9 | Material / critical regression | Priority response / authority escalation |
| RX | Unknown / insufficient | Do not treat as no regression |
| RR | Rejected / reassessment required | Correct / independent review |
| RS | Suspended | Restore assessment |

## Regression Record
| Field | Required |
|---|---|
| Regression ID | Yes |
| Deviation ID | Where applicable |
| Current Result | Yes |
| Previous State ID | Yes |
| Previous State Version | Yes |
| Context | Yes |
| Difference | Yes |
| Time Relationship | Yes |
| Persistence | Where applicable |
| Recurrence | Where applicable |
| Materiality | Yes |
| Consequence Relevance | Yes where applicable |
| Causal / Relevance Assessment | Where applicable |
| Confidence | Yes |
| Regression State | Yes |
| Authority | Yes |
| Evidence | Yes |

## Deviation Is Not Regression
A deviation establishes failure against an applicable current requirement or permitted boundary. Regression establishes deterioration from a relevant previous state.
```text
DEVIATION
≠
REGRESSION
```

## Regression Requires a Meaningful Previous State
Where deterioration is the decision basis, the previous accepted/resolved/controlled state shall be identifiable, versioned and contextually comparable.
```text
PREVIOUS STATE
+
CURRENT STATE
+
CONTEXT ALIGNMENT
=
REGRESSION BASIS
```

## No Regression Is Not Zero Risk
A no-regression determination describes the current evidence. It does not guarantee that the state cannot deteriorate later.
```text
NO REGRESSION
≠
ZERO FUTURE RISK
```

## Unknown Regression
Where the previous state or current evidence is insufficient, the determination shall remain unknown/undetermined rather than becoming no regression.
```text
UNKNOWN
≠
NO REGRESSION
```

## Temporal Relationship
Regression determination shall consider whether the current condition represents deterioration after restoration, resolution or acceptance and whether the timing is relevant to recurrence or persistence.

## Persistence and Recurrence
Sustained or repeated deterioration strengthens regression evidence. Repeated short-lived deviations may still indicate systemic regression where criteria establish that relationship.

## Materiality and Consequence
Materiality shall consider consequence, scope, duration, recurrence, dependency, exposure and downstream reliance where applicable.

## Causality vs Relevance
Regression determination may establish that a condition is relevant to a previously resolved state without claiming causality unless the evidence supports a causal conclusion.

## Confirmed Regression
Confirmed regression requires sufficient evidence that approved regression criteria are met. The response path then becomes mandatory according to the applicable governance controls.

## AI and Agent Regression
AI/agent regression shall evaluate deterioration against approved behavior, authority, tool, data and oversight states, not merely against model confidence or self-reporting.

## Relationship to Regression Response
RG-128 is the gateway from post-closure monitoring into the formal regression-response governance sequence.
```text
MONITORING → VALIDATION → QUALIFICATION → COMPARISON → DEVIATION → REGRESSION DETERMINATION → REGRESSION RESPONSE
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression-determination layer beneath deviation determination and above regression response governance. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, result validation, result qualification, deviation, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring activation, monitoring execution, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Regression Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → DEVIATION DETERMINATION → MANDATORY REGRESSION DETERMINATION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REOPENING
```

## Complete Regression Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → COMPARE CURRENT STATE TO PREVIOUS ACCEPTED STATE → DETERMINE REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-129` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Classification Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE DEVIATION OR REGRESSION-INDICATING CONDITION TO BE ASSESSED AGAINST A VALID, CONTEXT-ALIGNED PREVIOUSLY ACCEPTED, RESOLVED OR CONTROLLED STATE BEFORE REGRESSION IS DETERMINED, WITH DETERIORATION, TEMPORAL RELATIONSHIP, PERSISTENCE, RECURRENCE, MATERIALITY AND CONSEQUENCE RELEVANCE EXPLICITLY GOVERNED, SO THAT A SINGLE DIFFERENCE OR DEVIATION CANNOT SILENTLY BECOME A REGRESSION WITHOUT A TRACEABLE AND AUTHORIZED DETERMINATION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-DETERMINATION-01

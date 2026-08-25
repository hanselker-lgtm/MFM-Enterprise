# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-RESULT-COMPARISON-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-126`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-126` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-RESULT-COMPARISON-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Monitoring Result Comparison Determination |
| Parent | EA-IMETA-PC-RG-125 — Mandatory Post-Closure Monitoring Result Qualification Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory result-comparison layer that determines how a qualified post-closure monitoring result relates to its approved baseline, target, tolerance, threshold, reference state, prior accepted state or expected trajectory, producing a traceable comparison outcome for subsequent deviation, deterioration and regression determination.

## Core Principle
Qualification establishes what a validated result represents. Comparison establishes the governed relationship between that qualified result and an approved reference. Comparison shall preserve both the observed result and the reference state and shall not silently convert difference into deviation or regression.

```text
QUALIFIED RESULT
        ↓
REFERENCE VALID?
├── NO → COMPARISON UNDETERMINED
└── YES
     ↓
REFERENCE ALIGNED TO SAME CONTEXT?
├── NO → RECONTEXTUALIZE / REJECT
└── YES
     ↓
COMPARE
     ↓
DETERMINE DIFFERENCE
├── NONE / WITHIN EXPECTATION
├── ACCEPTABLE VARIATION
├── NEGATIVE / DEGRADING
├── THRESHOLD BREACH
├── MATERIAL DEVIATION
└── COMPARISON UNDETERMINED
     ↓
PRESERVE COMPARISON EVIDENCE
     ↓
PASS TO DEVIATION / REGRESSION DETERMINATION
```
## Comparison Quality Test
```text
VALIDATED RESULT
+
QUALIFIED RESULT
+
APPROVED REFERENCE
+
CONTEXT ALIGNMENT
+
COMPARISON METHOD
+
DEFINED TOLERANCE / THRESHOLD
+
TRACEABLE DIFFERENCE
+
VALID COMPARISON DECISION
=
VALID GOVERNED RESULT COMPARISON
```
## Qualification vs Comparison vs Deviation vs Regression
```text
QUALIFICATION
→ WHAT CATEGORY DOES THE RESULT REPRESENT?

COMPARISON
→ HOW DOES THE RESULT RELATE TO THE APPROVED REFERENCE?

DEVIATION DETERMINATION
→ HAS AN APPROVED DEVIATION CONDITION BEEN ESTABLISHED?

REGRESSION DETERMINATION
→ DOES THE COMPARISON ESTABLISH DETERIORATION FROM A PREVIOUSLY ACCEPTED STATE?
```
## Comparison States
```text
C0 — COMPARISON NOT REQUIRED
C1 — COMPARISON PENDING
C2 — REFERENCE VALIDATION IN PROGRESS
C3 — CONTEXT ALIGNMENT IN PROGRESS
C4 — COMPARISON IN PROGRESS
C5 — WITHIN EXPECTATION
C6 — ACCEPTABLE VARIATION
C7 — DEGRADING / NEGATIVE DIFFERENCE
C8 — THRESHOLD BREACH
C9 — MATERIAL DEVIATION-INDICATING
C10 — REGRESSION-INDICATING
CX — UNKNOWN / INSUFFICIENT COMPARISON BASIS
CR — COMPARISON REJECTED / REASSESSMENT REQUIRED
CS — COMPARISON SUSPENDED
```
## Comparison Dimensions
| Dimension | Required determination |
|---|---|
| Result | Qualified observed state |
| Reference | Approved comparison state |
| Context | Context equivalence |
| Baseline | Accepted baseline |
| Target | Required target |
| Tolerance | Permitted variation |
| Threshold | Trigger boundary |
| Difference | Calculated / assessed difference |
| Direction | Improving / stable / degrading |
| Persistence | Duration / recurrence |
| Confidence | Comparison confidence |
| Consequence Relevance | Materiality relevance |
| Evidence | Supporting evidence |

## Comparison Invariants

```text
COMPARISON SHALL USE A VALIDATED AND QUALIFIED RESULT
```

```text
THE COMPARISON REFERENCE SHALL BE APPROVED AND TRACEABLE
```

```text
RESULT AND REFERENCE SHALL BE CONTEXTUALLY ALIGNED BEFORE COMPARISON
```

```text
BASELINE, TARGET, TOLERANCE AND THRESHOLD SHALL NOT BE INTERCHANGED WITHOUT EXPLICIT GOVERNANCE
```

```text
COMPARISON SHALL PRESERVE THE ORIGINAL RESULT AND REFERENCE VALUES
```

```text
DIFFERENCE SHALL NOT AUTOMATICALLY EQUAL DEVIATION
```

```text
DEVIATION SHALL NOT AUTOMATICALLY EQUAL REGRESSION
```

```text
REGRESSION COMPARISON SHALL CONSIDER THE PREVIOUSLY ACCEPTED OR RESOLVED STATE WHERE REQUIRED
```

```text
COMPARISON SHALL DISTINGUISH IMPROVEMENT, STABILITY, ACCEPTABLE VARIATION AND DEGRADATION
```

```text
PERSISTENCE AND RECURRENCE SHALL BE CONSIDERED WHERE A SINGLE COMPARISON IS INSUFFICIENT
```

```text
UNKNOWN OR INVALID REFERENCE SHALL NOT PRODUCE A POSITIVE COMPARISON CONCLUSION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE COMPARISONS SHALL USE DOMAIN-APPROPRIATE REFERENCES
```

```text
AI AND AGENT COMPARISON SHALL CONSIDER BEHAVIOR, AUTHORITY, TOOL, DATA AND OVERSIGHT BASELINES
```

```text
COMPARISON SHALL NOT BE BIASED TO PRESERVE CLOSED STATUS OR AVOID REOPENING
```

```text
COMPARISON CHANGES SHALL BE TRACEABLE AND AUDITABLE
```

```text
COMPARISON CONTROLS SHALL BE REVIEWED AFTER FALSE POSITIVES, FALSE NEGATIVES, BASELINE DRIFT OR REFERENCE ERRORS
```

## 1. Comparison Domain — Post-Closure Monitoring Result Comparison Governance

**Control family:** `PCMC-001`

The Post-Closure Monitoring Result Comparison Governance domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-001-01` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-001-02` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-001-03` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-001-04` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-001-05` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-001-06` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-001-07` — Establish and maintain the post-closure monitoring result comparison governance control.
- `PCMC-001-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 2. Comparison Domain — Post-Closure Monitoring Result Comparison Objective

**Control family:** `PCMC-002`

The Post-Closure Monitoring Result Comparison Objective domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-002-01` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-002-02` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-002-03` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-002-04` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-002-05` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-002-06` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-002-07` — Establish and maintain the post-closure monitoring result comparison objective control.
- `PCMC-002-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 3. Comparison Domain — Post-Closure Monitoring Result Comparison Definition

**Control family:** `PCMC-003`

The Post-Closure Monitoring Result Comparison Definition domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-003-01` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-003-02` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-003-03` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-003-04` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-003-05` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-003-06` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-003-07` — Establish and maintain the post-closure monitoring result comparison definition control.
- `PCMC-003-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 4. Comparison Domain — Post-Closure Monitoring Result Comparison Scope

**Control family:** `PCMC-004`

The Post-Closure Monitoring Result Comparison Scope domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-004-01` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-004-02` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-004-03` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-004-04` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-004-05` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-004-06` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-004-07` — Establish and maintain the post-closure monitoring result comparison scope control.
- `PCMC-004-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 5. Comparison Domain — Post-Closure Monitoring Result Comparison Authority

**Control family:** `PCMC-005`

The Post-Closure Monitoring Result Comparison Authority domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-005-01` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-005-02` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-005-03` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-005-04` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-005-05` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-005-06` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-005-07` — Establish and maintain the post-closure monitoring result comparison authority control.
- `PCMC-005-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 6. Comparison Domain — Post-Closure Monitoring Result Comparison Criteria

**Control family:** `PCMC-006`

The Post-Closure Monitoring Result Comparison Criteria domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-006-01` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-006-02` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-006-03` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-006-04` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-006-05` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-006-06` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-006-07` — Establish and maintain the post-closure monitoring result comparison criteria control.
- `PCMC-006-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 7. Comparison Domain — Post-Closure Monitoring Result Comparison Preconditions

**Control family:** `PCMC-007`

The Post-Closure Monitoring Result Comparison Preconditions domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-007-01` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-007-02` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-007-03` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-007-04` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-007-05` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-007-06` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-007-07` — Establish and maintain the post-closure monitoring result comparison preconditions control.
- `PCMC-007-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 8. Comparison Domain — Post-Closure Monitoring Result Comparison Evidence

**Control family:** `PCMC-008`

The Post-Closure Monitoring Result Comparison Evidence domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-008-01` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-008-02` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-008-03` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-008-04` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-008-05` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-008-06` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-008-07` — Establish and maintain the post-closure monitoring result comparison evidence control.
- `PCMC-008-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 9. Comparison Domain — Post-Closure Monitoring Result Comparison Method

**Control family:** `PCMC-009`

The Post-Closure Monitoring Result Comparison Method domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-009-01` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-009-02` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-009-03` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-009-04` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-009-05` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-009-06` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-009-07` — Establish and maintain the post-closure monitoring result comparison method control.
- `PCMC-009-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 10. Comparison Domain — Post-Closure Monitoring Result Comparison Decision

**Control family:** `PCMC-010`

The Post-Closure Monitoring Result Comparison Decision domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-010-01` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-010-02` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-010-03` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-010-04` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-010-05` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-010-06` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-010-07` — Establish and maintain the post-closure monitoring result comparison decision control.
- `PCMC-010-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 11. Comparison Domain — Post-Closure Monitoring Result Comparison Accountability

**Control family:** `PCMC-011`

The Post-Closure Monitoring Result Comparison Accountability domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-011-01` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-011-02` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-011-03` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-011-04` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-011-05` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-011-06` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-011-07` — Establish and maintain the post-closure monitoring result comparison accountability control.
- `PCMC-011-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 12. Comparison Domain — Post-Closure Monitoring Result Comparison Timing

**Control family:** `PCMC-012`

The Post-Closure Monitoring Result Comparison Timing domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-012-01` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-012-02` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-012-03` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-012-04` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-012-05` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-012-06` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-012-07` — Establish and maintain the post-closure monitoring result comparison timing control.
- `PCMC-012-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 13. Comparison Domain — Security Post-Closure Monitoring Result Comparison

**Control family:** `PCMC-013`

The Security Post-Closure Monitoring Result Comparison domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-013-01` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-013-02` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-013-03` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-013-04` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-013-05` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-013-06` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-013-07` — Establish and maintain the security post-closure monitoring result comparison control.
- `PCMC-013-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 14. Comparison Domain — Resilience Post-Closure Monitoring Result Comparison

**Control family:** `PCMC-014`

The Resilience Post-Closure Monitoring Result Comparison domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-014-01` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-014-02` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-014-03` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-014-04` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-014-05` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-014-06` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-014-07` — Establish and maintain the resilience post-closure monitoring result comparison control.
- `PCMC-014-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 15. Comparison Domain — Compliance Post-Closure Monitoring Result Comparison

**Control family:** `PCMC-015`

The Compliance Post-Closure Monitoring Result Comparison domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-015-01` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-015-02` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-015-03` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-015-04` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-015-05` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-015-06` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-015-07` — Establish and maintain the compliance post-closure monitoring result comparison control.
- `PCMC-015-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 16. Comparison Domain — Data Post-Closure Monitoring Result Comparison

**Control family:** `PCMC-016`

The Data Post-Closure Monitoring Result Comparison domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-016-01` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-016-02` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-016-03` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-016-04` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-016-05` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-016-06` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-016-07` — Establish and maintain the data post-closure monitoring result comparison control.
- `PCMC-016-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 17. Comparison Domain — AI and Agent Post-Closure Monitoring Result Comparison

**Control family:** `PCMC-017`

The AI and Agent Post-Closure Monitoring Result Comparison domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-017-01` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-017-02` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-017-03` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-017-04` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-017-05` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-017-06` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-017-07` — Establish and maintain the ai and agent post-closure monitoring result comparison control.
- `PCMC-017-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 18. Comparison Domain — Post-Closure Monitoring Result Comparison Failure

**Control family:** `PCMC-018`

The Post-Closure Monitoring Result Comparison Failure domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-018-01` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-018-02` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-018-03` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-018-04` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-018-05` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-018-06` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-018-07` — Establish and maintain the post-closure monitoring result comparison failure control.
- `PCMC-018-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 19. Comparison Domain — Post-Closure Monitoring Result Comparison Independence

**Control family:** `PCMC-019`

The Post-Closure Monitoring Result Comparison Independence domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-019-01` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-019-02` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-019-03` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-019-04` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-019-05` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-019-06` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-019-07` — Establish and maintain the post-closure monitoring result comparison independence control.
- `PCMC-019-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## 20. Comparison Domain — Post-Closure Monitoring Result Comparison Review and Learning

**Control family:** `PCMC-020`

The Post-Closure Monitoring Result Comparison Review and Learning domain establishes governed mandatory result-comparison requirements.

### Required controls
- `PCMC-020-01` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-01-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-020-02` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-02-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-020-03` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-03-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-020-04` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-04-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-020-05` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-05-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-020-06` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-06-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.
- `PCMC-020-07` — Establish and maintain the post-closure monitoring result comparison review and learning control.
- `PCMC-020-07-E` — Preserve result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence, confidence, consequence relevance, evidence and escalation traceability.

```text
QUALIFY → ALIGN REFERENCE → COMPARE → MEASURE DIFFERENCE → INTERPRET → ESCALATE IF REQUIRED
```

## Post-Closure Monitoring Result Comparison Structure

| Element | Required definition |
|---|---|
| Result | Qualified observed state |
| Reference | Approved comparison state |
| Context | Context alignment |
| Baseline | Accepted baseline |
| Target | Required outcome |
| Tolerance | Permitted variation |
| Threshold | Trigger boundary |
| Difference | Result-reference relationship |
| Direction | Trend direction |
| Persistence | Duration / recurrence |
| Confidence | Comparison confidence |
| Consequence Relevance | Potential impact |
| Evidence | Supporting evidence |

## Post-Closure Monitoring Result Comparison Objective

Determine the governed relationship between a qualified post-closure monitoring result and its approved reference so that deterioration, deviation and regression can be distinguished from acceptable variation.

## Post-Closure Monitoring Result Comparison Definition

Result comparison is the governed determination of the relationship, difference, direction and materiality between a qualified observed result and an approved reference state.

## Post-Closure Monitoring Result Comparison Scope

Scope includes baseline comparisons, target comparisons, tolerance assessments, threshold comparisons, trend comparisons and comparison against previously accepted or resolved states.

## Post-Closure Monitoring Result Comparison Authority

Authority shall define who approves reference states, comparison rules, tolerances and overrides and who may resolve disputed comparison results.

## Post-Closure Monitoring Result Comparison Criteria

Criteria shall define result, reference, context, baseline, target, tolerance, threshold, difference, direction, persistence and consequence relevance.
```text
QUALIFIED RESULT
↓
REFERENCE VALID?
↓
CONTEXT ALIGNED?
↓
COMPARE
↓
DIFFERENCE
├── WITHIN EXPECTATION
├── ACCEPTABLE VARIATION
├── DEGRADING
├── THRESHOLD BREACH
├── DEVIATION-INDICATING
└── REGRESSION-INDICATING
↓
DEVIATION / REGRESSION DETERMINATION
```

## Post-Closure Monitoring Result Comparison Preconditions

Preconditions include validated and qualified result, approved reference, context alignment, applicable comparison method and defined tolerance or threshold where required.

## Post-Closure Monitoring Result Comparison Evidence

Evidence shall preserve observed result, reference value, reference version, context, method, calculated or assessed difference, direction, threshold status and decision.

## Post-Closure Monitoring Result Comparison Method

Methods may include direct comparison, normalized comparison, percentage difference, tolerance evaluation, trend analysis, control-chart methods, benchmark comparison and expert assessment.
```text
RESULT
↓
REFERENCE
↓
ALIGN
↓
NORMALIZE IF REQUIRED
↓
CALCULATE / ASSESS DIFFERENCE
↓
APPLY TOLERANCE / THRESHOLD
↓
COMPARE
```

## Post-Closure Monitoring Result Comparison Decision

Decision shall determine C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, CX, CR or CS and the permitted next action.

## Post-Closure Monitoring Result Comparison Accountability

Accountability shall remain explicit for reference integrity, comparison method, tolerance governance, interpretation and disputed results.

## Post-Closure Monitoring Result Comparison Timing

Comparison shall occur before material deviation, consequence or regression decisions, unless a controlled provisional path is explicitly authorized.

## Security Post-Closure Monitoring Result Comparison

Security comparison shall assess current exposure and control indicators against approved secure-state baselines, thresholds and previously accepted conditions.

## Resilience Post-Closure Monitoring Result Comparison

Resilience comparison shall assess capacity, availability, redundancy, recovery and fallback indicators against required service and resilience baselines.

## Compliance Post-Closure Monitoring Result Comparison

Compliance comparison shall assess current control and obligation state against approved requirements, thresholds and accepted compliance baselines.

## Data Post-Closure Monitoring Result Comparison

Data comparison shall assess integrity, quality, lineage, availability, confidentiality and downstream reliance against approved data-state references.

## AI and Agent Post-Closure Monitoring Result Comparison

AI/agent comparison shall assess observed behavior, authority boundaries, tool use, data handling, autonomy and oversight against approved governed baselines.
```text
AI / AGENT RESULT
↓
APPROVED BEHAVIOR BASELINE
+
AUTHORITY BASELINE
+
TOOL BASELINE
+
DATA BASELINE
+
OVERSIGHT BASELINE
↓
COMPARE
↓
DEVIATION / REGRESSION DETERMINATION
```

## Post-Closure Monitoring Result Comparison Failure

Failure includes invalid reference, context mismatch, baseline drift, incorrect normalization, unavailable comparison basis, contradictory inputs or inability to establish a reliable difference.
```text
COMPARISON FAILURE
↓
MATERIAL DECISION AFFECTED?
├── YES → REASSESS / INDEPENDENT REVIEW / ESCALATE
└── NO → CORRECT / RECORD
```

## Post-Closure Monitoring Result Comparison Independence

Independent comparison may be required where the comparison materially affects reopening, safety, security, compliance, reliance restoration or high-consequence decisions.

## Post-Closure Monitoring Result Comparison Review and Learning

Reviews shall examine baseline drift, tolerance bias, reference errors, normalization errors, false positives, false negatives and systematic comparison defects.

## Comparison Decision Model
```text
QUALIFIED RESULT
↓
REFERENCE VALID?
├── NO → COMPARISON UNDETERMINED
└── YES
     ↓
CONTEXT ALIGNED?
├── NO → RECONTEXTUALIZE / REJECT
└── YES
     ↓
REFERENCE VERSION CURRENT?
├── NO → UPDATE / GOVERN BASELINE
└── YES
     ↓
COMPARE
     ↓
DIFFERENCE
     ↓
TOLERANCE / THRESHOLD
├── WITHIN EXPECTATION
├── ACCEPTABLE VARIATION
├── DEGRADING
├── THRESHOLD BREACH
├── MATERIAL DEVIATION-INDICATING
└── REGRESSION-INDICATING
     ↓
PASS TO GOVERNED DEVIATION / REGRESSION DETERMINATION
```

## Comparison Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| C0 | Comparison not required | Record basis |
| C1 | Pending | Prepare comparison |
| C2 | Reference validation in progress | Validate reference |
| C3 | Context alignment in progress | Align / correct context |
| C4 | Comparison in progress | Complete comparison |
| C5 | Within expectation | Continue monitoring |
| C6 | Acceptable variation | Continue / observe |
| C7 | Degrading / negative difference | Investigate / escalate |
| C8 | Threshold breach | Enter governed response path |
| C9 | Material deviation-indicating | Deviation determination |
| C10 | Regression-indicating | Regression determination |
| CX | Unknown / insufficient basis | Do not treat as normal |
| CR | Rejected / reassessment required | Correct / independently review |
| CS | Suspended | Restore comparison |

## Result Comparison Record
| Field | Required |
|---|---|
| Comparison ID | Yes |
| Qualification ID | Yes |
| Result ID | Yes |
| Reference ID | Yes |
| Reference Version | Yes |
| Context | Yes |
| Baseline | Where applicable |
| Target | Where applicable |
| Tolerance | Where applicable |
| Threshold | Where applicable |
| Comparison Method | Yes |
| Difference | Yes |
| Direction | Where applicable |
| Persistence | Where applicable |
| Confidence | Yes |
| Consequence Relevance | Yes where applicable |
| Comparison State | Yes |
| Escalation | Where applicable |
| Evidence | Yes |

## Qualification Is Not Comparison
Qualification categorizes the validated result. Comparison determines the governed relationship between that result and its reference state.
```text
QUALIFIED
≠
COMPARED
```

## Comparison Is Not Deviation
A measurable difference does not automatically establish a governed deviation. Deviation criteria remain a separate determination.
```text
DIFFERENCE
≠
DEVIATION
```

## Deviation Is Not Regression
A deviation from a current reference is not automatically a regression from a previously accepted or resolved state.
```text
DEVIATION
≠
REGRESSION
```

## Baseline vs Target vs Tolerance vs Threshold
| Reference Type | Meaning |
|---|---|
| Baseline | Accepted reference state used for comparison |
| Target | Required desired outcome or performance level |
| Tolerance | Permitted variation around an accepted state |
| Threshold | Boundary that triggers a defined governed action |

## Reference Integrity
Comparison shall use an approved, version-controlled and contextually valid reference. A stale or uncontrolled reference shall not silently produce a valid comparison.

## Context Alignment
Result and reference must represent comparable scope, population, time window, operating mode and other material dimensions.
```text
SAME CONTEXT?
├── YES → COMPARE
└── NO → RECONTEXTUALIZE / REJECT
```

## Normalization
Where results and references use different scales, units, populations or conditions, normalization shall be explicit, reproducible and traceable.

## Difference
Difference may be expressed as absolute, relative, percentage, directional, categorical or otherwise appropriate measures. The chosen representation shall be fit for the decision.

## Direction
Where material, comparison shall identify whether the monitored condition is improving, stable, fluctuating or degrading.

## Persistence
Where transient differences are common, persistence or recurrence criteria shall distinguish temporary variation from sustained deterioration.

## Threshold Breach
A threshold breach shall invoke the defined governance path. It shall not be suppressed by averaging, smoothing or normalization unless such treatment is explicitly approved.

## Regression-Indicating Comparison
A comparison becomes regression-indicating when the evidence meets the approved criteria for deterioration from the relevant previously accepted or resolved state.

## Unknown Comparison
Where no valid reference exists, comparison shall be unknown or otherwise governed as undetermined. It shall not be silently treated as within expectation.
```text
NO VALID REFERENCE
≠
WITHIN EXPECTATION
```

## AI and Agent Comparison
AI/agent comparison shall consider the appropriate governed baseline for behavior, authority, tools, data and oversight. Model confidence alone shall not define a successful comparison.

## Independent Comparison
Where comparison materially affects reopening or other high-consequence decisions, independent validation or review may be required.

## Relationship to Deviation and Regression
RG-126 supplies the comparison outcome used by subsequent deviation and regression determination layers.
```text
VALIDATION
↓
QUALIFICATION
↓
COMPARISON
↓
DEVIATION / REGRESSION DETERMINATION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure monitoring-result comparison layer beneath result qualification and above deviation, deterioration and regression determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring activation, monitoring execution, result validation, result qualification, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Comparison Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → MANDATORY RESULT COMPARISON → DEVIATION DETERMINATION → REGRESSION DETECTION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REOPENING
```

## Complete Comparison Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE RESULT → QUALIFY RESULT → COMPARE → DETERMINE DIFFERENCE → ASSESS TOLERANCE / THRESHOLD → DETERMINE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE MONITORING → VALIDATE RESULT → QUALIFY RESULT → COMPARE → DETECT REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING AS REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-127` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Monitoring Deviation Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL QUALIFIED POST-CLOSURE MONITORING RESULT TO BE COMPARED AGAINST AN APPROVED, CONTEXT-ALIGNED AND TRACEABLE REFERENCE USING EXPLICIT BASELINE, TARGET, TOLERANCE AND THRESHOLD RULES WHERE APPLICABLE, WITH DIFFERENCE, DIRECTION, PERSISTENCE AND MATERIALITY DISTINGUISHED FROM DEVIATION AND REGRESSION, SO THAT COMPARISON REMAINS AN OBJECTIVE GOVERNANCE LAYER RATHER THAN AN IMPLICIT OR BIASED REGRESSION DECISION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-RESULT-COMPARISON-DETERMINATION-01

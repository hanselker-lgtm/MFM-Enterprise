# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-CLASSIFICATION-CONTROL-01

## Physical File ID
`EA-IMETA-PC-RG-111`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-111` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-CLASSIFICATION-CONTROL-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Classification Control |
| Parent | EA-IMETA-PC-RG-110 — Mandatory Post-Closure Regression Detection Control |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory classification layer that converts a detected or suspected post-closure regression into an explicit governed class based on materiality, consequence, scope, persistence, control-state impact, reliance impact and urgency, so that proportionate action can be selected without understating or overstating the condition.

## Core Principle
Detection establishes that something may have changed. Classification establishes what the change means for governance. Classification shall therefore be evidence-based, consequence-aware, traceable and capable of escalation when uncertainty itself creates material risk.

```text
REGRESSION DETECTED
      ↓
QUALIFY EVIDENCE
      ↓
CLASSIFICATION CRITERIA VALID?
├── NO → QUALIFY / ESCALATE
└── YES
     ↓
ASSESS MATERIALITY
     ↓
ASSESS CONSEQUENCE
     ↓
ASSESS SCOPE / PERSISTENCE / CONTROL IMPACT
     ↓
ASSIGN REGRESSION CLASS
     ↓
DETERMINE REQUIRED GOVERNANCE RESPONSE
     ↓
ALERT / RESTRICT / RESPOND / REASSESS
```

## Classification Quality Test
```text
VALID REGRESSION EVIDENCE
+
CURRENT CRITERIA
+
MATERIALITY ASSESSMENT
+
CONSEQUENCE ASSESSMENT
+
SCOPE ASSESSMENT
+
PERSISTENCE ASSESSMENT
+
CONTROL / RELIANCE IMPACT
+
AUTHORIZED CLASSIFICATION
+
TRACEABLE RATIONALE
=
VALID GOVERNED REGRESSION CLASSIFICATION
```

## Detection vs Classification
```text
DETECTION
→ SOMETHING DIFFERED FROM EXPECTED STATE

CLASSIFICATION
→ THE GOVERNED SIGNIFICANCE OF THAT DIFFERENCE
  HAS BEEN DETERMINED
```

## Regression Classification Model
```text
R0 — NO MATERIAL REGRESSION
R1 — MINOR REGRESSION
R2 — SIGNIFICANT REGRESSION
R3 — MAJOR REGRESSION
R4 — CRITICAL REGRESSION
RX — UNCLASSIFIED / INSUFFICIENT EVIDENCE
```

## Classification Dimensions
| Dimension | Examples |
|---|---|
| Materiality | Minor / Significant / Major / Critical |
| Consequence | Low / Moderate / High / Severe |
| Scope | Local / Component / Cross-domain / Systemic |
| Persistence | Transient / Repeated / Sustained / Unknown |
| Control Impact | None / Degraded / Materially impaired / Failed |
| Reliance Impact | None / Restricted / Suspended / Revoked |
| Urgency | Routine / Expedited / Immediate / Emergency |

## Classification Invariants

```text
CLASSIFICATION SHALL BE BASED ON CURRENT EVIDENCE AND CURRENT CRITERIA
```

```text
CLASSIFICATION SHALL NOT BE DETERMINED SOLELY BY THE SIZE OF A SINGLE METRIC DEVIATION
```

```text
CONSEQUENCE SHALL BE CONSIDERED TOGETHER WITH PROBABILITY, EXPOSURE AND CONTROL IMPACT WHERE RELEVANT
```

```text
UNCERTAINTY SHALL NOT BE USED TO DOWNGRADE A POTENTIALLY MATERIAL REGRESSION
```

```text
THE MOST MATERIAL APPLICABLE CLASS SHALL GOVERN WHEN MULTIPLE DIMENSIONS INDICATE DIFFERENT SEVERITIES
```

```text
CLASSIFICATION CRITERIA SHALL BE VERSIONED AND TRACEABLE
```

```text
CLASSIFICATION SHALL REMAIN REASSESSABLE AS EVIDENCE CHANGES
```

```text
CLASSIFICATION SHALL DETERMINE OR INFORM PROPORTIONATE RESPONSE, RESTRICTION AND ESCALATION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE REGRESSIONS SHALL RECEIVE DOMAIN-APPROPRIATE CLASSIFICATION
```

```text
AI AND AGENT REGRESSION SHALL CLASSIFY BOTH BEHAVIORAL AND CONTROL-STATE IMPACT
```

```text
CLASSIFICATION SHALL NOT BE LOWERED TO AVOID ALERTING OR ESCALATION
```

```text
CLASSIFICATION SHALL NOT BE RAISED WITHOUT A TRACEABLE EVIDENCE BASIS
```

```text
DEPENDENCY AND SECOND-ORDER CONSEQUENCE SHALL BE INCLUDED WHERE MATERIAL
```

```text
CLASSIFICATION HISTORY SHALL BE PRESERVED
```

```text
RECLASSIFICATION SHALL BE POSSIBLE WHEN CONDITIONS CHANGE
```

```text
CLASSIFICATION SHALL REMAIN LINKED TO THE RELIANCE STATE AND REQUIRED ACTION
```

## 1. Classification Domain — Post-Closure Regression Classification Governance

**Control family:** `PCRC-001`

The Post-Closure Regression Classification Governance domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-001-01` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-001-02` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-001-03` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-001-04` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-001-05` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-001-06` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-001-07` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 2. Classification Domain — Post-Closure Regression Classification Objective

**Control family:** `PCRC-002`

The Post-Closure Regression Classification Objective domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-002-01` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-002-02` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-002-03` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-002-04` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-002-05` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-002-06` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-002-07` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 3. Classification Domain — Post-Closure Regression Classification Definition

**Control family:** `PCRC-003`

The Post-Closure Regression Classification Definition domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-003-01` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-003-02` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-003-03` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-003-04` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-003-05` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-003-06` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-003-07` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 4. Classification Domain — Post-Closure Regression Classification Scope

**Control family:** `PCRC-004`

The Post-Closure Regression Classification Scope domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-004-01` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-004-02` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-004-03` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-004-04` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-004-05` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-004-06` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-004-07` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 5. Classification Domain — Post-Closure Regression Classification Authority

**Control family:** `PCRC-005`

The Post-Closure Regression Classification Authority domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-005-01` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-005-02` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-005-03` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-005-04` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-005-05` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-005-06` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-005-07` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 6. Classification Domain — Post-Closure Regression Classification Criteria

**Control family:** `PCRC-006`

The Post-Closure Regression Classification Criteria domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-006-01` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-006-02` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-006-03` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-006-04` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-006-05` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-006-06` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-006-07` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 7. Classification Domain — Post-Closure Regression Classification Preconditions

**Control family:** `PCRC-007`

The Post-Closure Regression Classification Preconditions domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-007-01` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-007-02` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-007-03` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-007-04` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-007-05` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-007-06` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-007-07` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 8. Classification Domain — Post-Closure Regression Classification Evidence

**Control family:** `PCRC-008`

The Post-Closure Regression Classification Evidence domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-008-01` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-008-02` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-008-03` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-008-04` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-008-05` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-008-06` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-008-07` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 9. Classification Domain — Post-Closure Regression Classification Method

**Control family:** `PCRC-009`

The Post-Closure Regression Classification Method domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-009-01` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-009-02` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-009-03` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-009-04` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-009-05` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-009-06` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-009-07` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 10. Classification Domain — Post-Closure Regression Classification Decision

**Control family:** `PCRC-010`

The Post-Closure Regression Classification Decision domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-010-01` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-010-02` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-010-03` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-010-04` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-010-05` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-010-06` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-010-07` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 11. Classification Domain — Post-Closure Regression Classification Accountability

**Control family:** `PCRC-011`

The Post-Closure Regression Classification Accountability domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-011-01` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-011-02` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-011-03` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-011-04` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-011-05` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-011-06` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-011-07` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 12. Classification Domain — Post-Closure Regression Classification Timing

**Control family:** `PCRC-012`

The Post-Closure Regression Classification Timing domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-012-01` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-012-02` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-012-03` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-012-04` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-012-05` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-012-06` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-012-07` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 13. Classification Domain — Security Post-Closure Regression Classification

**Control family:** `PCRC-013`

The Security Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-013-01` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-013-02` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-013-03` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-013-04` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-013-05` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-013-06` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-013-07` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 14. Classification Domain — Resilience Post-Closure Regression Classification

**Control family:** `PCRC-014`

The Resilience Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-014-01` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-014-02` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-014-03` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-014-04` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-014-05` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-014-06` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-014-07` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 15. Classification Domain — Compliance Post-Closure Regression Classification

**Control family:** `PCRC-015`

The Compliance Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-015-01` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-015-02` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-015-03` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-015-04` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-015-05` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-015-06` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-015-07` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 16. Classification Domain — Data Post-Closure Regression Classification

**Control family:** `PCRC-016`

The Data Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-016-01` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-016-02` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-016-03` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-016-04` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-016-05` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-016-06` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-016-07` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 17. Classification Domain — AI and Agent Post-Closure Regression Classification

**Control family:** `PCRC-017`

The AI and Agent Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-017-01` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-017-02` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-017-03` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-017-04` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-017-05` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-017-06` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-017-07` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 18. Classification Domain — Post-Closure Regression Classification Failure

**Control family:** `PCRC-018`

The Post-Closure Regression Classification Failure domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-018-01` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-018-02` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-018-03` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-018-04` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-018-05` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-018-06` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-018-07` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 19. Classification Domain — Post-Closure Regression Classification Independence

**Control family:** `PCRC-019`

The Post-Closure Regression Classification Independence domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-019-01` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-019-02` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-019-03` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-019-04` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-019-05` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-019-06` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-019-07` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## 20. Classification Domain — Post-Closure Regression Classification Review and Learning

**Control family:** `PCRC-020`

The Post-Closure Regression Classification Review and Learning domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-020-01` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-01-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-020-02` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-02-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-020-03` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-03-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-020-04` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-04-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-020-05` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-05-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-020-06` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-06-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.
- `PCRC-020-07` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-07-E` — Preserve detection evidence, criteria, materiality, consequence, scope, persistence, control impact, reliance impact, class, rationale and decision traceability.

```text
QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE → ACT
```

## Post-Closure Regression Classification Structure

| Element | Required definition |
|---|---|
| Detection | Identified deviation |
| Evidence | Supporting facts |
| Materiality | Significance |
| Consequence | Potential or realized impact |
| Scope | Affected boundary |
| Persistence | Duration / recurrence |
| Control Impact | Effect on required controls |
| Reliance Impact | Effect on permitted reliance |
| Class | Governed severity category |
| Action | Required governance treatment |

## Post-Closure Regression Classification Objective

Translate detected regression into a defensible severity and consequence class that drives proportionate alerting, restriction, response, escalation and reassessment.

## Post-Closure Regression Classification Definition

Regression classification is the governed determination of the significance, consequence and required treatment of a detected regression against approved criteria.

## Post-Closure Regression Classification Scope

Scope shall include direct effects, dependencies, downstream effects, affected controls, affected reliance, duration, recurrence and potential systemic impact.

## Post-Closure Regression Classification Authority

Authority shall define who may classify, approve, challenge, escalate, downgrade, upgrade or override a classification and under which conditions.

## Post-Closure Regression Classification Criteria

Criteria shall define class boundaries, materiality, consequence, persistence, scope, control impact, reliance impact and urgency.
```text
DETECTED REGRESSION
↓
EVIDENCE SUFFICIENT?
├── NO → RX / ESCALATE
└── YES
     ↓
MATERIALITY
     ↓
CONSEQUENCE
     ↓
SCOPE + PERSISTENCE
     ↓
CONTROL + RELIANCE IMPACT
     ↓
R0 / R1 / R2 / R3 / R4
     ↓
ACTION
```

## Post-Closure Regression Classification Preconditions

Preconditions include valid detection, current criteria, sufficient evidence, baseline reference, consequence framework and authorized classification roles.

## Post-Closure Regression Classification Evidence

Evidence shall preserve source observations, timestamps, baseline version, measurement, consequence analysis, affected scope, control impact and classification rationale.

## Post-Closure Regression Classification Method

Methods may include rule-based classification, risk matrices, consequence models, expert assessment, independent review and automated classification with human governance where required.
```text
OBSERVE → QUALIFY → ASSESS → CLASSIFY → VALIDATE → AUTHORIZE
```

## Post-Closure Regression Classification Decision

Decision shall assign R0, R1, R2, R3, R4 or RX and define the associated governance treatment.

## Post-Closure Regression Classification Accountability

Accountability shall remain explicit for class interpretation, consequence assessment, escalation and reclassification.

## Post-Closure Regression Classification Timing

Classification shall occur within a period proportionate to the maximum tolerable decision latency for the detected condition.

## Security Post-Closure Regression Classification

Security regression classification shall consider exposure, compromise, privilege impact, attack surface, control degradation and potential propagation.

## Resilience Post-Closure Regression Classification

Resilience classification shall consider availability, capacity, recovery capability, redundancy, dependency concentration and continuity impact.

## Compliance Post-Closure Regression Classification

Compliance classification shall consider mandatory obligations, regulatory exposure, control failure, reporting impact and required notification.

## Data Post-Closure Regression Classification

Data classification shall consider integrity, confidentiality, availability, quality, lineage, affected population and downstream decision impact.

## AI and Agent Post-Closure Regression Classification

AI/agent classification shall consider behavior drift, policy violation, authority expansion, tool misuse, data-boundary breach, autonomy change and human-oversight failure.
```text
AI / AGENT REGRESSION
↓
BEHAVIORAL IMPACT
+
CONTROL IMPACT
+
AUTHORITY / TOOL / DATA IMPACT
+
AUTONOMY IMPACT
↓
CLASSIFY
```

## Post-Closure Regression Classification Failure

Failure includes under-classification, over-classification, inconsistent classification, stale criteria, hidden consequence, unsupported override or delayed classification.
```text
CLASSIFICATION FAILURE
↓
MATERIALITY UNCERTAIN?
├── YES → CONSERVATIVE CLASS / ESCALATE
└── NO → CORRECT / RECLASSIFY
```

## Post-Closure Regression Classification Independence

Independent classification review may be required where the affected party has a material interest in the outcome, classification is disputed, or consequence is high.

## Post-Closure Regression Classification Review and Learning

Reviews shall examine misclassification, delayed escalation, recurring under-classification, false severity, weak criteria and cases where later evidence required major reclassification.

## Classification Decision Model
```text
REGRESSION DETECTED
↓
EVIDENCE SUFFICIENT?
├── NO → RX / ESCALATE
└── YES
     ↓
MATERIALITY
     ↓
CONSEQUENCE
     ↓
SCOPE / PERSISTENCE
     ↓
CONTROL / RELIANCE IMPACT
     ↓
ASSIGN CLASS
     ↓
R0 / R1 / R2 / R3 / R4
     ↓
AUTHORIZE
     ↓
ALERT / RESTRICT / RESPOND / REASSESS
```

## Regression Classification Matrix
| Class | General meaning | Typical governance treatment |
|---|---|---|
| R0 | No material regression | Record and continue monitoring |
| R1 | Minor regression | Correct / monitor |
| R2 | Significant regression | Escalate / controlled response |
| R3 | Major regression | Restrict reliance / urgent response |
| R4 | Critical regression | Immediate restriction / emergency governance |
| RX | Insufficient evidence / unclassified | Conservative treatment and evidence acquisition |

## Classification Dimension Matrix
| Dimension | Low | Medium | High | Critical |
|---|---|---|---|---|
| Consequence | Limited | Material | Severe | Catastrophic |
| Scope | Local | Multiple components | Cross-domain | Systemic |
| Persistence | Transient | Repeated | Sustained | Unknown / uncontrolled |
| Control Impact | Minor | Degraded | Materially impaired | Failed |
| Reliance Impact | None | Restricted | Suspended | Revoked |
| Urgency | Routine | Expedited | Immediate | Emergency |

## Classification Record
| Field | Required |
|---|---|
| Classification ID | Yes |
| Regression ID | Yes |
| Detection Time | Yes |
| Criteria Version | Yes |
| Evidence Set | Yes |
| Materiality | Yes |
| Consequence | Yes |
| Scope | Yes |
| Persistence | Yes |
| Control Impact | Yes |
| Reliance Impact | Yes |
| Assigned Class | Yes |
| Rationale | Yes |
| Authority | Yes |
| Effective Time | Yes |
| Reclassification History | Where applicable |

## Conservative Classification Under Uncertainty
When materiality cannot yet be conclusively determined, the classification shall not be artificially lowered merely because evidence is incomplete. The appropriate conservative class or RX status shall be selected according to consequence and authority.

## Maximum Applicable Severity
When multiple classification dimensions produce different severity indications, the most material applicable class shall govern unless an authorized documented exception exists.

## Reclassification
Classification shall be dynamic where evidence changes.
```text
R1
↓
NEW EVIDENCE
↓
R3
↓
RESTRICT / ESCALATE
```

## Classification Does Not Equal Response
Classification determines or informs required governance treatment; it does not replace the subsequent response execution, effectiveness, resolution or closure controls.

## Classification Does Not Equal Consequence
Classification incorporates consequence but remains a governed category used to drive action. Consequence analysis shall remain separately traceable.

## Dependency and Second-Order Impact
Classification shall consider whether a local regression can propagate through dependencies or create second-order effects that justify a higher class.

## AI and Agent Classification
AI/agent regressions shall not be classified solely from output accuracy. A small output deviation may become major if it indicates unauthorized authority, tool access, data-boundary or autonomy expansion.

## Anti-Gaming
Classification criteria and assigned classes shall not be manipulated to avoid alerting, reporting, restriction, escalation or mandatory response.

## Relationship to Consequence
RG-111 feeds the consequence determination layer that governs the impact and required response of the classified regression.
```text
DETECTION
↓
CLASSIFICATION
↓
CONSEQUENCE
↓
ALERT / RESPONSE
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure regression-classification layer beneath regression detection and above consequence, alerting, response and reopening. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Classification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REACCEPTANCE → RELIANCE RESTORATION → MONITORING CONTINUITY → REGRESSION DETECTION → MANDATORY REGRESSION CLASSIFICATION → REOPENING
```

## Complete Classification Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → REACCEPT → RESTORE RELIANCE → MAINTAIN MONITORING → DETECT REGRESSION → CLASSIFY REGRESSION → RESTRICT / RESPOND → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-112` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Consequence Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION TO BE CLASSIFIED THROUGH CURRENT, EVIDENCE-BASED AND CONSEQUENCE-AWARE CRITERIA, WITH EXPLICIT MATERIALITY, SCOPE, PERSISTENCE, CONTROL AND RELIANCE IMPACT, SO THAT UNCERTAINTY CANNOT BE USED TO DOWNGRADE MATERIAL CONDITIONS AND CLASSIFICATION DIRECTLY SUPPORTS PROPORTIONATE ALERTING, RESTRICTION, RESPONSE, ESCALATION AND REASSESSMENT.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-CLASSIFICATION-CONTROL-01

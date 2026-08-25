# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-DEVIATION-CLASSIFICATION-AND-CONSEQUENCE-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-087`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-087` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-DEVIATION-CLASSIFICATION-AND-CONSEQUENCE-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Deviation Classification and Consequence Determination |
| Parent | EA-IMETA-PC-RG-086 — Mandatory Post-Closure Comparison and Deviation Detection |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory classification layer that converts validated post-closure deviations into governed severity, materiality, consequence and response categories, ensuring that significant degradation is neither understated nor overstated and that classification drives the appropriate next governance action.

## Core Principle
Classification is not merely labeling. A validated deviation shall be interpreted against explicit criteria, consequence dimensions, persistence, recurrence, scope and context so that its governance significance and required action are determined consistently.

```text
VALIDATED DEVIATION
      ↓
ASSESS SCOPE + CONTEXT + MATERIALITY
      ↓
ASSESS CONSEQUENCE DIMENSIONS
      ↓
ASSESS PERSISTENCE / RECURRENCE
      ↓
CLASSIFY SEVERITY / TYPE / CONSEQUENCE
      ↓
DETERMINE GOVERNANCE ACTION
├── IMMATERIAL → RECORD / CONTINUE
├── MATERIAL → ALERT / ESCALATE
├── HIGH CONSEQUENCE → IMMEDIATE GOVERNED RESPONSE
└── REGRESSION → ENTER RESPONSE LIFECYCLE
```

## Classification Quality Test
```text
VALIDATED DEVIATION
+
DEFINED CLASSIFICATION CRITERIA
+
MATERIALITY ASSESSMENT
+
CONSEQUENCE ASSESSMENT
+
CONTEXT + SCOPE
+
PERSISTENCE / RECURRENCE
+
TRACEABLE EVIDENCE
+
AUTHORIZED DETERMINATION
=
VALID GOVERNED CLASSIFICATION
```

## Classification vs Consequence vs Response
```text
CLASSIFICATION
→ WHAT KIND OF DEVIATION IS THIS AND HOW SIGNIFICANT IS IT?

CONSEQUENCE
→ WHAT GOVERNANCE IMPACT DOES IT CREATE OR REPRESENT?

RESPONSE
→ WHAT MUST BE DONE ABOUT IT?
```

## Classification State Model
```text
UNCLASSIFIED
UNDER ASSESSMENT
CLASSIFIED
LOW
MODERATE
HIGH
CRITICAL
MATERIAL
IMMATERIAL
PERSISTENT
RECURRENT
REGRESSION CANDIDATE
REGRESSION CONFIRMED
RECLASSIFICATION REQUIRED
```

## Classification and Consequence Invariants

```text
CLASSIFICATION CRITERIA SHALL BE EXPLICIT
```

```text
CLASSIFICATION SHALL USE VALIDATED DEVIATION EVIDENCE
```

```text
MATERIALITY SHALL BE ASSESSED EXPLICITLY
```

```text
CONSEQUENCE SHALL CONSIDER RELEVANT IMPACT DIMENSIONS
```

```text
SEVERITY SHALL NOT BE BASED SOLELY ON A SINGLE METRIC WHERE MULTI-DIMENSIONAL IMPACT EXISTS
```

```text
PERSISTENCE AND RECURRENCE SHALL BE CONSIDERED WHERE MATERIAL
```

```text
CLASSIFICATION SHALL BE TRACEABLE TO BASELINE, OBSERVATION AND DEVIATION
```

```text
CLASSIFICATION RULES SHALL BE VERSIONED
```

```text
RECLASSIFICATION SHALL BE CONTROLLED AND HISTORICALLY TRACEABLE
```

```text
HIGH-CONSEQUENCE CONDITIONS SHALL NOT WAIT FOR ADMINISTRATIVE COMPLETION
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE CLASSIFICATION SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT CLASSIFICATION SHALL CONSIDER AUTHORITY, POLICY, DATA, TOOLS, AUTONOMY, BEHAVIOUR AND OUTCOMES
```

```text
UNCERTAINTY SHALL BE EXPLICITLY REPRESENTED WHERE CLASSIFICATION EVIDENCE IS INCOMPLETE
```

```text
CLASSIFICATION SHALL NOT BE MANIPULATED TO AVOID ALERTING OR ESCALATION
```

```text
CONSEQUENCE DETERMINATION SHALL REMAIN SEPARATE FROM DESIRED RESPONSE OUTCOME
```

```text
CLASSIFICATION SHALL SUPPORT CONSISTENT CROSS-CONTEXT GOVERNANCE
```

## 1. Classification Domain — Post-Closure Deviation Classification Governance

**Control family:** `PCCL-001`

The Post-Closure Deviation Classification Governance domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-001-01` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-001-02` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-001-03` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-001-04` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-001-05` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-001-06` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-001-07` — Establish and maintain the post-closure deviation classification governance control.
- `PCCL-001-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 2. Classification Domain — Post-Closure Deviation Classification Objective

**Control family:** `PCCL-002`

The Post-Closure Deviation Classification Objective domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-002-01` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-002-02` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-002-03` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-002-04` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-002-05` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-002-06` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-002-07` — Establish and maintain the post-closure deviation classification objective control.
- `PCCL-002-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 3. Classification Domain — Post-Closure Deviation Classification Definition

**Control family:** `PCCL-003`

The Post-Closure Deviation Classification Definition domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-003-01` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-003-02` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-003-03` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-003-04` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-003-05` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-003-06` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-003-07` — Establish and maintain the post-closure deviation classification definition control.
- `PCCL-003-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 4. Classification Domain — Post-Closure Deviation Classification Scope

**Control family:** `PCCL-004`

The Post-Closure Deviation Classification Scope domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-004-01` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-004-02` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-004-03` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-004-04` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-004-05` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-004-06` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-004-07` — Establish and maintain the post-closure deviation classification scope control.
- `PCCL-004-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 5. Classification Domain — Post-Closure Deviation Classification Authority

**Control family:** `PCCL-005`

The Post-Closure Deviation Classification Authority domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-005-01` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-005-02` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-005-03` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-005-04` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-005-05` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-005-06` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-005-07` — Establish and maintain the post-closure deviation classification authority control.
- `PCCL-005-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 6. Classification Domain — Post-Closure Deviation Classification Criteria

**Control family:** `PCCL-006`

The Post-Closure Deviation Classification Criteria domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-006-01` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-006-02` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-006-03` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-006-04` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-006-05` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-006-06` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-006-07` — Establish and maintain the post-closure deviation classification criteria control.
- `PCCL-006-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 7. Classification Domain — Post-Closure Deviation Classification Preconditions

**Control family:** `PCCL-007`

The Post-Closure Deviation Classification Preconditions domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-007-01` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-007-02` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-007-03` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-007-04` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-007-05` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-007-06` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-007-07` — Establish and maintain the post-closure deviation classification preconditions control.
- `PCCL-007-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 8. Classification Domain — Post-Closure Deviation Classification Evidence

**Control family:** `PCCL-008`

The Post-Closure Deviation Classification Evidence domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-008-01` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-008-02` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-008-03` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-008-04` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-008-05` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-008-06` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-008-07` — Establish and maintain the post-closure deviation classification evidence control.
- `PCCL-008-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 9. Classification Domain — Post-Closure Deviation Classification Method

**Control family:** `PCCL-009`

The Post-Closure Deviation Classification Method domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-009-01` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-009-02` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-009-03` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-009-04` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-009-05` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-009-06` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-009-07` — Establish and maintain the post-closure deviation classification method control.
- `PCCL-009-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 10. Classification Domain — Post-Closure Deviation Classification Decision

**Control family:** `PCCL-010`

The Post-Closure Deviation Classification Decision domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-010-01` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-010-02` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-010-03` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-010-04` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-010-05` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-010-06` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-010-07` — Establish and maintain the post-closure deviation classification decision control.
- `PCCL-010-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 11. Classification Domain — Post-Closure Deviation Classification Accountability

**Control family:** `PCCL-011`

The Post-Closure Deviation Classification Accountability domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-011-01` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-011-02` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-011-03` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-011-04` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-011-05` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-011-06` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-011-07` — Establish and maintain the post-closure deviation classification accountability control.
- `PCCL-011-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 12. Classification Domain — Post-Closure Deviation Classification Timing

**Control family:** `PCCL-012`

The Post-Closure Deviation Classification Timing domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-012-01` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-012-02` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-012-03` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-012-04` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-012-05` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-012-06` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-012-07` — Establish and maintain the post-closure deviation classification timing control.
- `PCCL-012-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 13. Classification Domain — Security Post-Closure Deviation Classification

**Control family:** `PCCL-013`

The Security Post-Closure Deviation Classification domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-013-01` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-013-02` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-013-03` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-013-04` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-013-05` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-013-06` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-013-07` — Establish and maintain the security post-closure deviation classification control.
- `PCCL-013-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 14. Classification Domain — Resilience Post-Closure Deviation Classification

**Control family:** `PCCL-014`

The Resilience Post-Closure Deviation Classification domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-014-01` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-014-02` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-014-03` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-014-04` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-014-05` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-014-06` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-014-07` — Establish and maintain the resilience post-closure deviation classification control.
- `PCCL-014-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 15. Classification Domain — Compliance Post-Closure Deviation Classification

**Control family:** `PCCL-015`

The Compliance Post-Closure Deviation Classification domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-015-01` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-015-02` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-015-03` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-015-04` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-015-05` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-015-06` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-015-07` — Establish and maintain the compliance post-closure deviation classification control.
- `PCCL-015-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 16. Classification Domain — Data Post-Closure Deviation Classification

**Control family:** `PCCL-016`

The Data Post-Closure Deviation Classification domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-016-01` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-016-02` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-016-03` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-016-04` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-016-05` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-016-06` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-016-07` — Establish and maintain the data post-closure deviation classification control.
- `PCCL-016-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 17. Classification Domain — AI and Agent Post-Closure Deviation Classification

**Control family:** `PCCL-017`

The AI and Agent Post-Closure Deviation Classification domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-017-01` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-017-02` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-017-03` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-017-04` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-017-05` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-017-06` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-017-07` — Establish and maintain the ai and agent post-closure deviation classification control.
- `PCCL-017-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 18. Classification Domain — Post-Closure Deviation Classification Failure

**Control family:** `PCCL-018`

The Post-Closure Deviation Classification Failure domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-018-01` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-018-02` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-018-03` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-018-04` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-018-05` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-018-06` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-018-07` — Establish and maintain the post-closure deviation classification failure control.
- `PCCL-018-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 19. Classification Domain — Post-Closure Deviation Classification Independence

**Control family:** `PCCL-019`

The Post-Closure Deviation Classification Independence domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-019-01` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-019-02` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-019-03` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-019-04` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-019-05` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-019-06` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-019-07` — Establish and maintain the post-closure deviation classification independence control.
- `PCCL-019-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## 20. Classification Domain — Post-Closure Deviation Classification Review and Learning

**Control family:** `PCCL-020`

The Post-Closure Deviation Classification Review and Learning domain establishes governed mandatory classification and consequence-determination requirements.

### Required controls
- `PCCL-020-01` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-01-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-020-02` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-02-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-020-03` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-03-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-020-04` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-04-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-020-05` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-05-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-020-06` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-06-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.
- `PCCL-020-07` — Establish and maintain the post-closure deviation classification review and learning control.
- `PCCL-020-07-E` — Preserve deviation, criteria, context, materiality, consequence, classification, authority and reclassification traceability.

```text
DEVIATION → ASSESS → CLASSIFY → DETERMINE CONSEQUENCE → GOVERN
```

## Post-Closure Deviation Classification Structure

| Element | Required definition |
|---|---|
| Deviation | Validated difference |
| Type | Nature of deviation |
| Materiality | Significance |
| Severity | Degree of concern |
| Consequence | Governance impact |
| Persistence | Duration / recurrence |
| Scope | Affected boundary |
| Action Class | Required governance path |

## Post-Closure Deviation Classification Objective

Provide a consistent and evidence-based method for determining the governance significance of post-closure deviations and selecting the appropriate next action.

## Post-Closure Deviation Classification Definition

Classification is the governed interpretation of a validated deviation against explicit criteria to determine type, severity, materiality and consequence.

## Post-Closure Deviation Classification Scope

Scope shall identify affected systems, services, users, data, decisions, dependencies, environments, consumers and governance boundaries.

## Post-Closure Deviation Classification Authority

Authority shall define who may classify, reclassify, accept uncertainty, override a classification and escalate high-consequence conditions.

## Post-Closure Deviation Classification Criteria

Criteria shall address magnitude, duration, recurrence, scope, likelihood, consequence, control degradation, affected obligations and uncertainty.

```text
VALIDATED DEVIATION
↓
MATERIALITY?
├── LOW → LOW / IMMATERIAL
└── YES
     ↓
CONSEQUENCE?
├── LIMITED → MODERATE / MATERIAL
├── SIGNIFICANT → HIGH
└── SEVERE / BROAD → CRITICAL
     ↓
PERSISTENT / RECURRENT?
├── YES → INCREASE GOVERNANCE ATTENTION
└── NO → CONTINUE AS CLASSIFIED
```

## Post-Closure Deviation Classification Preconditions

Preconditions include validated deviation, valid baseline and observation references, classification criteria, context and appropriate authority.

## Post-Closure Deviation Classification Evidence

Evidence shall preserve deviation details, baseline version, observation, calculation, context, classification rationale, consequence analysis and decision authority.

## Post-Closure Deviation Classification Method

Methods may include rule-based classification, matrix assessment, weighted consequence analysis, expert determination, multi-dimensional scoring and controlled escalation.

```text
DEVIATION
↓
TYPE
↓
MATERIALITY
↓
SEVERITY
↓
CONSEQUENCE
↓
ACTION CLASS
```

## Post-Closure Deviation Classification Decision

Decision shall explicitly record classification, consequence, confidence/uncertainty, required action class and any escalation requirement.

```text
CLASSIFICATION
├── IMMATERIAL → RECORD / MONITOR
├── MATERIAL → ALERT / GOVERN
├── HIGH → ESCALATE / RESPOND
└── CRITICAL → IMMEDIATE GOVERNED RESPONSE
```

## Post-Closure Deviation Classification Accountability

Accountability shall remain explicit for classification quality, consequence interpretation, escalation and reclassification.

## Post-Closure Deviation Classification Timing

Classification shall occur within a period appropriate to consequence and time-to-impact. High-consequence deviations shall not wait for routine review cycles.

## Security Post-Closure Deviation Classification

Security classification shall consider exposure, control degradation, exploitability, affected assets, data sensitivity and potential impact.

## Resilience Post-Closure Deviation Classification

Resilience classification shall consider availability, recoverability, capacity, continuity, dependency concentration and time-to-impact.

## Compliance Post-Closure Deviation Classification

Compliance classification shall consider obligation criticality, control failure, evidence deficiency, reporting impact and regulatory consequence.

## Data Post-Closure Deviation Classification

Data classification shall consider integrity, quality, access, confidentiality, lineage, retention, authorized use and downstream impact.

## AI and Agent Post-Closure Deviation Classification

AI/agent classification shall consider authority deviation, policy violation, data misuse, tool misuse, autonomy expansion, behavioural degradation and material outcomes.

```text
AI / AGENT DEVIATION
↓
AUTHORITY + POLICY + DATA + TOOLS
+
AUTONOMY + BEHAVIOUR + OUTCOME
↓
MATERIALITY + CONSEQUENCE
↓
CLASSIFICATION
```

## Post-Closure Deviation Classification Failure

Failure includes insufficient evidence, ambiguous criteria, conflicting classification results, hidden consequence, stale criteria or inability to determine materiality.

```text
CLASSIFICATION FAILURE
↓
CAN SAFE CLASSIFICATION BE MADE?
├── YES → QUALIFIED CLASSIFICATION
└── NO → ESCALATE / TREAT CONSERVATIVELY
```

## Post-Closure Deviation Classification Independence

Independent review may be required where classification materially affects risk acceptance, regulatory reporting, executive escalation or response authority.

## Post-Closure Deviation Classification Review and Learning

Reviews shall identify misclassification, delayed escalation, threshold weaknesses, consequence blind spots, recurring patterns and inconsistent treatment.

## Classification and Consequence Determination Model
```text
VALIDATED DEVIATION
↓
CLASSIFICATION CRITERIA VALID?
├── NO → GOVERNANCE GAP
└── YES
     ↓
MATERIALITY ASSESSED?
├── NO → ASSESS
└── YES
     ↓
CONSEQUENCE ASSESSED?
├── NO → ASSESS
└── YES
     ↓
PERSISTENCE / RECURRENCE RELEVANT?
├── YES → INCORPORATE
└── NO → CONTINUE
     ↓
CLASSIFY
↓
DETERMINE ACTION CLASS
↓
ALERT / ESCALATE / RESPOND AS REQUIRED
```

## Classification Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Unclassified | Assessment not complete | Complete classification |
| Immaterial | No material governance consequence | Record / monitor |
| Low | Limited consequence | Monitor / routine action |
| Moderate | Meaningful consequence | Govern / investigate |
| High | Significant consequence | Escalate / respond |
| Critical | Severe or immediate consequence | Immediate governed response |
| Persistent | Sustained deviation | Increase governance attention |
| Recurrent | Repeated deviation | Assess systemic regression |
| Regression Candidate | Evidence indicates degradation | Regression assessment |
| Regression Confirmed | Governed state materially degraded | Enter response lifecycle |
| Reclassification Required | Existing classification no longer valid | Reassess / update |

## Classification Record
| Field | Required |
|---|---|
| Classification ID | Yes |
| Deviation ID | Yes |
| Baseline ID / Version | Yes |
| Observation References | Yes |
| Classification Criteria Version | Yes |
| Type | Yes |
| Materiality | Yes |
| Severity | Yes |
| Consequence | Yes |
| Persistence / Recurrence | Where applicable |
| Confidence / Uncertainty | Yes where material |
| Classification Rationale | Yes |
| Authority | Yes |
| Action Class | Yes |

## Materiality
Materiality shall reflect whether the deviation can affect required outcomes, controls, obligations, reliance, safety, security, resilience, compliance, data integrity or other governed conditions.

## Consequence Dimensions
Where relevant, consequence assessment shall consider:
- operational impact
- security impact
- resilience impact
- compliance impact
- financial impact
- data impact
- safety impact
- reputational impact
- dependency impact
- governance impact
- time-to-impact
- reversibility

## Uncertainty
Uncertainty shall not be hidden. Where evidence is incomplete, classification shall explicitly state confidence and limitations and may require conservative escalation.

## Persistence and Recurrence
Persistent or recurrent deviations may warrant a higher governance classification even where individual observations appear moderate.

## Reclassification
Classification may change when new evidence, changed consequence, persistence, recurrence or corrected context becomes available. Every change shall preserve the previous classification and rationale.

```text
CLASSIFIED
↓
NEW MATERIAL EVIDENCE?
├── NO → CONTINUE
└── YES
     ↓
CLASSIFICATION STILL VALID?
├── YES → CONTINUE
└── NO → RECLASSIFY + TRACE
```

## Conservative Treatment
Where uncertainty could conceal a high-consequence condition, the architecture shall permit escalation or conservative treatment pending verification.

## Classification Consistency
Equivalent conditions shall receive materially consistent treatment across comparable contexts unless an explicit contextual reason is recorded.

## Classification Anti-Gaming
Classification shall not be manipulated to avoid alerting, escalation, reporting, ownership, resource allocation or mandatory response.

## Relationship to Alerting
Classification provides the consequence and action context required by the next alerting and notification layers.

```text
DEVIATION
↓
CLASSIFY
↓
CONSEQUENCE
↓
ACTION CLASS
↓
ALERT / ESCALATE / RESPOND
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure deviation classification and consequence-determination layer beneath comparison and deviation detection and above alerting, escalation and response. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, effectiveness, resolution, closure, transition, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Classification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → BASELINE → POST-CLOSURE MEASUREMENT / OBSERVATION → COMPARISON → DEVIATION DETECTION → MANDATORY CLASSIFICATION → ALERTING → ACKNOWLEDGEMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → POST-CLOSURE TRANSITION → REGRESSION DETECTION → REOPENING
```

## Complete Classification Chain
```text
BASELINE → OBSERVE → VALIDATE → COMPARE → DETECT DEVIATION → VALIDATE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → ACKNOWLEDGE → RESPOND → DETERMINE EFFECTIVENESS → RESOLVE → CLOSE → TRANSITION → MONITOR → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-088` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Alerting and Notification Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY VALIDATED POST-CLOSURE DEVIATION TO BE CLASSIFIED THROUGH EXPLICIT, VERSIONED AND EVIDENCE-BASED CRITERIA THAT CONSIDER MATERIALITY, CONSEQUENCE, SCOPE, CONTEXT, PERSISTENCE, RECURRENCE AND UNCERTAINTY, SO THAT SIGNIFICANT DEGRADATION RECEIVES THE REQUIRED GOVERNANCE ATTENTION AND CANNOT BE HIDDEN THROUGH MISCLASSIFICATION, THRESHOLD MANIPULATION OR ADMINISTRATIVE DELAY.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-DEVIATION-CLASSIFICATION-AND-CONSEQUENCE-DETERMINATION-01

# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CONSEQUENCE-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-130`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-130` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CONSEQUENCE-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Consequence Determination |
| Parent | EA-IMETA-PC-RG-129 — Mandatory Post-Closure Regression Classification Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory consequence-determination layer that determines the actual, potential, credible and material consequences associated with a classified post-closure regression, including impact, exposure, dependency, scope, severity, time-to-impact and containment implications, so that alert, notification, acknowledgement and response decisions are based on an explicit consequence model.

## Core Principle
Classification describes the significance and urgency of a regression. Consequence determination establishes what the regression has caused, may cause, threatens to cause or could cause under credible conditions. Consequence shall be determined independently of the desire to preserve closure and shall distinguish observed consequence from potential consequence.

```text
CLASSIFIED REGRESSION
        ↓
CONSEQUENCE CONTEXT VALID?
├── NO → CONSEQUENCE UNDETERMINED
└── YES
     ↓
ASSESS
├── ACTUAL IMPACT
├── POTENTIAL IMPACT
├── EXPOSURE
├── SCOPE
├── DEPENDENCY
├── SEVERITY
├── TIME-TO-IMPACT
├── CONTAINMENT
└── REVERSIBILITY
     ↓
CONSEQUENCE CLASS
├── NONE / CONTROLLED
├── LIMITED
├── SIGNIFICANT
├── MAJOR
├── CRITICAL
└── EXTREME
     ↓
CONSEQUENCE CONFIDENCE + EVIDENCE
     ↓
ALERT / NOTIFICATION / RESPONSE DETERMINATION
```
## Consequence Quality Test
```text
VALID REGRESSION CLASSIFICATION
+
VALID CONSEQUENCE CONTEXT
+
ACTUAL / POTENTIAL IMPACT ASSESSMENT
+
EXPOSURE / DEPENDENCY ASSESSMENT
+
TIME-TO-IMPACT
+
CONTAINMENT / REVERSIBILITY
+
TRACEABLE CONSEQUENCE DECISION
+
AUTHORIZED GOVERNANCE DETERMINATION
=
VALID GOVERNED REGRESSION CONSEQUENCE DETERMINATION
```
## Classification vs Consequence vs Response
```text
REGRESSION CLASSIFICATION
→ HOW SIGNIFICANT / URGENT / BROAD IS THE REGRESSION?

CONSEQUENCE DETERMINATION
→ WHAT HAS HAPPENED OR MAY HAPPEN BECAUSE OF IT?

ALERT / NOTIFICATION DETERMINATION
→ WHO MUST BE INFORMED AND WHEN?

RESPONSE DETERMINATION
→ WHAT GOVERNED ACTION IS REQUIRED?
```
## Consequence States
```text
CO0 — CONSEQUENCE NOT REQUIRED
CO1 — CONSEQUENCE ASSESSMENT PENDING
CO2 — CONSEQUENCE ASSESSMENT IN PROGRESS
CO3 — NO MATERIAL CONSEQUENCE
CO4 — LIMITED CONSEQUENCE
CO5 — SIGNIFICANT CONSEQUENCE
CO6 — MAJOR CONSEQUENCE
CO7 — CRITICAL CONSEQUENCE
CO8 — EXTREME CONSEQUENCE
CO9 — CATASTROPHIC CONSEQUENCE
CO10 — ACTUAL CONSEQUENCE CONFIRMED
CO11 — POTENTIAL CONSEQUENCE CONFIRMED
CO12 — CREDIBLE WORST-CASE CONSEQUENCE
COX — UNKNOWN / INSUFFICIENT BASIS
COR — CONSEQUENCE REJECTED / REASSESSMENT
COS — CONSEQUENCE ASSESSMENT SUSPENDED
```
## Consequence Dimensions
| Dimension | Required determination |
|---|---|
| Actual Impact | Observed consequence |
| Potential Impact | Credible future consequence |
| Exposure | Affected population / asset / service |
| Scope | Boundary of effect |
| Dependency | Downstream reliance |
| Severity | Degree of impact |
| Time-to-Impact | Expected time horizon |
| Containment | Existing limitation of impact |
| Reversibility | Ability to restore |
| Duration | Expected / actual persistence |
| Confidence | Assessment confidence |
| Evidence | Supporting evidence |
| Authority | Determination authority |

## Consequence Invariants

```text
CONSEQUENCE SHALL BE DETERMINED FROM VALID REGRESSION AND CLASSIFICATION EVIDENCE
```

```text
ACTUAL, POTENTIAL, CREDIBLE WORST-CASE AND HYPOTHETICAL CONSEQUENCE SHALL BE DISTINCT
```

```text
CONSEQUENCE SHALL NOT BE INFERRED SOLELY FROM CLASSIFICATION LABEL
```

```text
CONSEQUENCE SHALL CONSIDER EXPOSURE, SCOPE, DEPENDENCY AND TIME-TO-IMPACT WHERE MATERIAL
```

```text
CONTAINMENT SHALL BE ASSESSED WITHOUT ASSUMING THAT CONTAINMENT WILL REMAIN EFFECTIVE
```

```text
REVERSIBILITY AND RECOVERY EFFORT SHALL BE CONSIDERED WHERE THEY CHANGE GOVERNANCE RESPONSE
```

```text
UNKNOWN CONSEQUENCE SHALL NOT BE TREATED AS NO CONSEQUENCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE CONSEQUENCES SHALL USE DOMAIN-APPROPRIATE MODELS
```

```text
AI AND AGENT CONSEQUENCE SHALL CONSIDER AUTONOMY, SCALE, REACH, DATA, TOOL ACCESS AND OVERSIGHT
```

```text
CONSEQUENCE DETERMINATION SHALL NOT BE BIASED TO AVOID ALERTING OR REOPENING
```

```text
CONSEQUENCE UPDATES SHALL OCCUR WHEN MATERIAL NEW EVIDENCE CHANGES IMPACT OR EXPOSURE
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

```text
CONFLICTING CONSEQUENCE ASSESSMENTS SHALL BE RESOLVED OR ESCALATED
```

```text
CONSEQUENCE SHALL SUPPORT ALERT AND RESPONSE DECISIONS WITHOUT REPLACING THEM
```

```text
WORST-CASE SCENARIOS SHALL BE IDENTIFIED AS SUCH AND SHALL NOT BE PRESENTED AS OBSERVED FACT
```

```text
CONSEQUENCE RULES SHALL BE REVIEWED AFTER MISSED IMPACTS, FALSE ESCALATIONS OR FAILED CONTAINMENT
```

## 1. Consequence Domain — Post-Closure Regression Consequence Governance

**Control family:** `PCCO-001`

The Post-Closure Regression Consequence Governance domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-001-01` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-001-02` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-001-03` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-001-04` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-001-05` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-001-06` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-001-07` — Establish and maintain the post-closure regression consequence governance control.
- `PCCO-001-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 2. Consequence Domain — Post-Closure Regression Consequence Objective

**Control family:** `PCCO-002`

The Post-Closure Regression Consequence Objective domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-002-01` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-002-02` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-002-03` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-002-04` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-002-05` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-002-06` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-002-07` — Establish and maintain the post-closure regression consequence objective control.
- `PCCO-002-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 3. Consequence Domain — Post-Closure Regression Consequence Definition

**Control family:** `PCCO-003`

The Post-Closure Regression Consequence Definition domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-003-01` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-003-02` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-003-03` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-003-04` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-003-05` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-003-06` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-003-07` — Establish and maintain the post-closure regression consequence definition control.
- `PCCO-003-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 4. Consequence Domain — Post-Closure Regression Consequence Scope

**Control family:** `PCCO-004`

The Post-Closure Regression Consequence Scope domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-004-01` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-004-02` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-004-03` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-004-04` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-004-05` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-004-06` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-004-07` — Establish and maintain the post-closure regression consequence scope control.
- `PCCO-004-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 5. Consequence Domain — Post-Closure Regression Consequence Authority

**Control family:** `PCCO-005`

The Post-Closure Regression Consequence Authority domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-005-01` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-005-02` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-005-03` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-005-04` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-005-05` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-005-06` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-005-07` — Establish and maintain the post-closure regression consequence authority control.
- `PCCO-005-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 6. Consequence Domain — Post-Closure Regression Consequence Criteria

**Control family:** `PCCO-006`

The Post-Closure Regression Consequence Criteria domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-006-01` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-006-02` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-006-03` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-006-04` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-006-05` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-006-06` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-006-07` — Establish and maintain the post-closure regression consequence criteria control.
- `PCCO-006-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 7. Consequence Domain — Post-Closure Regression Consequence Preconditions

**Control family:** `PCCO-007`

The Post-Closure Regression Consequence Preconditions domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-007-01` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-007-02` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-007-03` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-007-04` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-007-05` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-007-06` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-007-07` — Establish and maintain the post-closure regression consequence preconditions control.
- `PCCO-007-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 8. Consequence Domain — Post-Closure Regression Consequence Evidence

**Control family:** `PCCO-008`

The Post-Closure Regression Consequence Evidence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-008-01` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-008-02` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-008-03` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-008-04` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-008-05` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-008-06` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-008-07` — Establish and maintain the post-closure regression consequence evidence control.
- `PCCO-008-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 9. Consequence Domain — Post-Closure Regression Consequence Method

**Control family:** `PCCO-009`

The Post-Closure Regression Consequence Method domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-009-01` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-009-02` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-009-03` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-009-04` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-009-05` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-009-06` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-009-07` — Establish and maintain the post-closure regression consequence method control.
- `PCCO-009-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 10. Consequence Domain — Post-Closure Regression Consequence Decision

**Control family:** `PCCO-010`

The Post-Closure Regression Consequence Decision domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-010-01` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-010-02` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-010-03` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-010-04` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-010-05` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-010-06` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-010-07` — Establish and maintain the post-closure regression consequence decision control.
- `PCCO-010-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 11. Consequence Domain — Post-Closure Regression Consequence Accountability

**Control family:** `PCCO-011`

The Post-Closure Regression Consequence Accountability domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-011-01` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-011-02` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-011-03` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-011-04` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-011-05` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-011-06` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-011-07` — Establish and maintain the post-closure regression consequence accountability control.
- `PCCO-011-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 12. Consequence Domain — Post-Closure Regression Consequence Timing

**Control family:** `PCCO-012`

The Post-Closure Regression Consequence Timing domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-012-01` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-012-02` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-012-03` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-012-04` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-012-05` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-012-06` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-012-07` — Establish and maintain the post-closure regression consequence timing control.
- `PCCO-012-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 13. Consequence Domain — Security Post-Closure Regression Consequence

**Control family:** `PCCO-013`

The Security Post-Closure Regression Consequence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-013-01` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-013-02` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-013-03` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-013-04` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-013-05` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-013-06` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-013-07` — Establish and maintain the security post-closure regression consequence control.
- `PCCO-013-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 14. Consequence Domain — Resilience Post-Closure Regression Consequence

**Control family:** `PCCO-014`

The Resilience Post-Closure Regression Consequence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-014-01` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-014-02` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-014-03` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-014-04` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-014-05` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-014-06` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-014-07` — Establish and maintain the resilience post-closure regression consequence control.
- `PCCO-014-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 15. Consequence Domain — Compliance Post-Closure Regression Consequence

**Control family:** `PCCO-015`

The Compliance Post-Closure Regression Consequence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-015-01` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-015-02` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-015-03` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-015-04` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-015-05` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-015-06` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-015-07` — Establish and maintain the compliance post-closure regression consequence control.
- `PCCO-015-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 16. Consequence Domain — Data Post-Closure Regression Consequence

**Control family:** `PCCO-016`

The Data Post-Closure Regression Consequence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-016-01` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-016-02` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-016-03` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-016-04` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-016-05` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-016-06` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-016-07` — Establish and maintain the data post-closure regression consequence control.
- `PCCO-016-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 17. Consequence Domain — AI and Agent Post-Closure Regression Consequence

**Control family:** `PCCO-017`

The AI and Agent Post-Closure Regression Consequence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-017-01` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-017-02` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-017-03` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-017-04` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-017-05` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-017-06` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-017-07` — Establish and maintain the ai and agent post-closure regression consequence control.
- `PCCO-017-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 18. Consequence Domain — Post-Closure Regression Consequence Failure

**Control family:** `PCCO-018`

The Post-Closure Regression Consequence Failure domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-018-01` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-018-02` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-018-03` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-018-04` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-018-05` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-018-06` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-018-07` — Establish and maintain the post-closure regression consequence failure control.
- `PCCO-018-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 19. Consequence Domain — Post-Closure Regression Consequence Independence

**Control family:** `PCCO-019`

The Post-Closure Regression Consequence Independence domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-019-01` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-019-02` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-019-03` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-019-04` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-019-05` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-019-06` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-019-07` — Establish and maintain the post-closure regression consequence independence control.
- `PCCO-019-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## 20. Consequence Domain — Post-Closure Regression Consequence Review and Learning

**Control family:** `PCCO-020`

The Post-Closure Regression Consequence Review and Learning domain establishes governed mandatory consequence-determination requirements.

### Required controls
- `PCCO-020-01` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-01-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-020-02` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-02-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-020-03` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-03-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-020-04` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-04-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-020-05` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-05-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-020-06` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-06-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.
- `PCCO-020-07` — Establish and maintain the post-closure regression consequence review and learning control.
- `PCCO-020-07-E` — Preserve regression classification, actual/potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility, duration, confidence, evidence and authority traceability.

```text
CLASSIFY → ASSESS IMPACT / EXPOSURE → DETERMINE CONSEQUENCE → DRIVE ALERT / RESPONSE GOVERNANCE
```

## Post-Closure Regression Consequence Structure

| Element | Required definition |
|---|---|
| Actual Impact | Observed consequence |
| Potential Impact | Credible future consequence |
| Exposure | Affected boundary |
| Scope | Effect boundary |
| Dependency | Downstream reliance |
| Severity | Degree of impact |
| Time-to-Impact | Expected horizon |
| Containment | Existing limitation |
| Reversibility | Recovery possibility |
| Duration | Actual / expected persistence |

## Post-Closure Regression Consequence Objective

Determine actual and credible potential consequences of regression so downstream alert, notification, acknowledgement and response governance can be proportionate and traceable.

## Post-Closure Regression Consequence Definition

Consequence determination is the governed assessment of actual, potential, credible worst-case or material impact arising from a classified regression.

## Post-Closure Regression Consequence Scope

Scope includes impact to security, resilience, safety, compliance, data, services, operations, assets, stakeholders, trust and downstream dependencies where applicable.

## Post-Closure Regression Consequence Authority

Authority shall define who may determine, approve, challenge, override or independently review consequence assessments.

## Post-Closure Regression Consequence Criteria

Criteria shall define actual impact, potential impact, exposure, scope, dependency, severity, time-to-impact, containment, reversibility and duration.
```text
REGRESSION CLASS
↓
ACTUAL IMPACT?
+
POTENTIAL IMPACT?
+
EXPOSURE
+
SCOPE
+
DEPENDENCY
+
TIME-TO-IMPACT
+
CONTAINMENT
+
REVERSIBILITY
↓
CONSEQUENCE CLASS
```

## Post-Closure Regression Consequence Preconditions

Preconditions include valid regression classification, consequence model, affected context, evidence and authority.

## Post-Closure Regression Consequence Evidence

Evidence shall preserve observed impacts, potential pathways, affected scope, dependencies, containment, recovery assumptions, time-to-impact and confidence.

## Post-Closure Regression Consequence Method

Methods may include impact assessment, dependency analysis, scenario analysis, exposure mapping, blast-radius analysis, time-to-impact analysis and expert review.
```text
REGRESSION
↓
IMPACT / EXPOSURE
↓
DEPENDENCY / SCOPE
↓
TIME-TO-IMPACT
↓
CONTAINMENT / REVERSIBILITY
↓
CONSEQUENCE
```

## Post-Closure Regression Consequence Decision

Decision shall determine CO0, CO1, CO2, CO3, CO4, CO5, CO6, CO7, CO8, CO9, CO10, CO11, CO12, COX, COR or COS.

## Post-Closure Regression Consequence Accountability

Accountability shall remain explicit for impact assumptions, consequence models, overrides, escalation and reassessment.

## Post-Closure Regression Consequence Timing

Consequence assessment shall occur early enough to support mandatory alert and response decisions before credible material impact becomes uncontrolled.

## Security Post-Closure Regression Consequence

Security consequence shall consider confidentiality, integrity, availability, privilege, exposure, attack reach, persistence and containment.

## Resilience Post-Closure Regression Consequence

Resilience consequence shall consider service loss, degraded capacity, recovery delay, redundancy loss, dependency failure and duration.

## Compliance Post-Closure Regression Consequence

Compliance consequence shall consider affected obligations, control failure, reporting impact, evidence validity, legal/regulatory exposure and duration.

## Data Post-Closure Regression Consequence

Data consequence shall consider scope, sensitivity, integrity, availability, lineage, downstream use and potential propagation.

## AI and Agent Post-Closure Regression Consequence

AI/agent consequence shall consider autonomy, action reach, authority, tool access, data scope, scale, repeatability, containment and oversight.
```text
AI / AGENT REGRESSION
↓
AUTONOMY + AUTHORITY + TOOLS + DATA + SCALE
↓
EXPOSURE / BLAST RADIUS
↓
TIME-TO-IMPACT
↓
CONSEQUENCE
```

## Post-Closure Regression Consequence Failure

Failure includes incomplete impact model, unknown exposure, invalid assumptions, conflicting evidence, missed dependency or failed containment assessment.
```text
CONSEQUENCE ASSESSMENT FAILURE
↓
MATERIAL DECISION AFFECTED?
├── YES → INDEPENDENT REVIEW / ESCALATE
└── NO → CORRECT / RECORD
```

## Post-Closure Regression Consequence Independence

Independent consequence assessment may be required where impact materially affects reopening, safety, security, compliance, public-facing services or high-consequence decisions.

## Post-Closure Regression Consequence Review and Learning

Reviews shall examine missed impacts, overestimated impacts, dependency blind spots, containment assumptions, time-to-impact errors and failed consequence models.

## Consequence Decision Model
```text
CLASSIFIED REGRESSION
↓
CONTEXT VALID?
├── NO → CONSEQUENCE UNDETERMINED
└── YES
     ↓
ACTUAL IMPACT?
├── YES → RECORD CONFIRMED ACTUAL CONSEQUENCE
└── NO
     ↓
POTENTIAL IMPACT?
├── NO → NO MATERIAL CONSEQUENCE
└── YES
     ↓
CREDIBLE PATHWAY?
├── NO → HYPOTHETICAL ONLY / RECORD LIMITATION
└── YES
     ↓
EXPOSURE + SCOPE + DEPENDENCY
     ↓
TIME-TO-IMPACT
     ↓
CONTAINMENT + REVERSIBILITY
     ↓
CONSEQUENCE CLASS
├── LIMITED
├── SIGNIFICANT
├── MAJOR
├── CRITICAL
└── EXTREME / CATASTROPHIC
     ↓
ALERT / NOTIFICATION / RESPONSE DETERMINATION
```

## Consequence Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| CO0 | Not required | Record basis |
| CO1 | Pending | Assess |
| CO2 | In progress | Complete assessment |
| CO3 | No material consequence | Continue governed monitoring |
| CO4 | Limited | Controlled response |
| CO5 | Significant | Formal response / escalation |
| CO6 | Major | Priority response |
| CO7 | Critical | Immediate high-authority response |
| CO8 | Extreme | Maximum governed response |
| CO9 | Catastrophic | Exceptional / highest governance |
| CO10 | Actual consequence confirmed | Act on observed impact |
| CO11 | Potential consequence confirmed | Act on credible risk |
| CO12 | Credible worst-case | Scenario-specific escalation |
| COX | Unknown / insufficient | Do not treat as none |
| COR | Rejected / reassessment | Correct / independent review |
| COS | Suspended | Restore assessment |

## Consequence Record
| Field | Required |
|---|---|
| Consequence ID | Yes |
| Regression ID | Yes |
| Classification | Yes |
| Actual Impact | Where applicable |
| Potential Impact | Yes where applicable |
| Exposure | Yes |
| Scope | Yes |
| Dependency | Where applicable |
| Severity | Yes |
| Time-to-Impact | Yes where applicable |
| Containment | Yes |
| Reversibility | Yes where applicable |
| Duration | Where applicable |
| Confidence | Yes |
| Consequence State | Yes |
| Authority | Yes |
| Evidence | Yes |

## Classification Is Not Consequence
Classification describes regression significance and urgency. Consequence determines actual or credible impact.
```text
CLASSIFICATION
≠
CONSEQUENCE
```

## Actual vs Potential Consequence
Actual consequence shall be supported by observed evidence. Potential consequence shall be supported by a credible pathway and explicit assumptions.
```text
OBSERVED
≠
POTENTIAL
≠
HYPOTHETICAL
```

## Credible Worst Case
Worst-case consequence shall be explicitly identified as a scenario and shall not be presented as observed fact.

## Exposure
Exposure identifies what can be affected if the regression persists or propagates, including assets, services, data, users, dependencies and downstream systems.

## Dependency
A seemingly limited regression can have material consequence through critical downstream dependencies.

## Time-to-Impact
Time-to-impact shall distinguish immediate, near-term, delayed and uncertain consequences where relevant to response priority.

## Containment
Existing containment shall be assessed, but governance shall not assume containment remains effective without evidence.

## Reversibility
Consequence assessment shall consider whether effects are reversible, partially reversible or effectively irreversible and the effort required to restore the accepted state.

## Duration
Long-duration consequences may be materially different from short-lived consequences even where peak severity is similar.

## Unknown Consequence
Insufficient evidence shall remain unknown and shall not be converted to no consequence merely because impact has not yet been observed.
```text
UNKNOWN
≠
NO CONSEQUENCE
```

## AI and Agent Consequence
AI/agent consequence shall account for autonomous reach, authority, tool permissions, data access, scale, repeatability and human oversight.

## Relationship to Alert and Response
RG-130 supplies consequence outcomes to the subsequent alert, notification and response determination layers.
```text
REGRESSION → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → RESPONSE
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression-consequence layer beneath regression classification and above alert, notification, acknowledgement and response determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, qualification, validation, deviation, regression determination, regression classification, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring activation, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Consequence Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → DEVIATION DETERMINATION → REGRESSION DETERMINATION → REGRESSION CLASSIFICATION → MANDATORY REGRESSION CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REOPENING
```

## Complete Consequence Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-131` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Alert Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION TO HAVE ITS ACTUAL, POTENTIAL AND CREDIBLE CONSEQUENCES EXPLICITLY ASSESSED FOR IMPACT, EXPOSURE, SCOPE, DEPENDENCY, SEVERITY, TIME-TO-IMPACT, CONTAINMENT, REVERSIBILITY AND DURATION BEFORE ALERT, NOTIFICATION OR RESPONSE DECISIONS ARE MADE, WITH OBSERVED, POTENTIAL AND HYPOTHETICAL CONSEQUENCES DISTINCTLY IDENTIFIED AND UNKNOWN CONSEQUENCE NEVER SILENTLY TREATED AS NO CONSEQUENCE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CONSEQUENCE-DETERMINATION-01

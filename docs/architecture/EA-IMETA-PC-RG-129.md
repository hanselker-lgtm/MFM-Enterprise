# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CLASSIFICATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-129`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-129` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CLASSIFICATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Classification Determination |
| Parent | EA-IMETA-PC-RG-128 — Mandatory Post-Closure Regression Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory regression-classification layer that categorizes a confirmed or materially potential post-closure regression according to severity, scope, persistence, recurrence, consequence, affected control domain, urgency and required governance response, without changing the underlying regression determination.

## Core Principle
Regression determination establishes whether deterioration from a previously accepted, resolved or controlled state exists. Classification establishes the governed significance and response category of that regression. Classification shall never be used to downgrade, conceal or bypass a valid regression determination.

```text
CONFIRMED / POTENTIAL REGRESSION
        ↓
CLASSIFICATION CONTEXT VALID?
├── NO → CLASSIFICATION UNDETERMINED
└── YES
     ↓
ASSESS
├── SEVERITY
├── SCOPE
├── PERSISTENCE
├── RECURRENCE
├── CONSEQUENCE
├── URGENCY
├── CONTROL DOMAIN
└── RESPONSE DEPENDENCY
     ↓
REGRESSION CLASS
├── MINOR
├── MODERATE
├── MAJOR
├── CRITICAL
└── CATASTROPHIC / EXTREME
     ↓
RESPONSE PRIORITY + AUTHORITY + ESCALATION
```
## Classification Quality Test
```text
VALID REGRESSION DETERMINATION
+
VALID CLASSIFICATION CONTEXT
+
APPROVED CLASSIFICATION CRITERIA
+
SEVERITY ASSESSMENT
+
SCOPE ASSESSMENT
+
PERSISTENCE / RECURRENCE
+
CONSEQUENCE / URGENCY
+
TRACEABLE CLASSIFICATION DECISION
=
VALID GOVERNED REGRESSION CLASSIFICATION
```
## Determination vs Classification vs Consequence
```text
REGRESSION DETERMINATION
→ HAS REGRESSION OCCURRED?

REGRESSION CLASSIFICATION
→ HOW SIGNIFICANT / URGENT / BROAD IS THE REGRESSION?

CONSEQUENCE DETERMINATION
→ WHAT CONSEQUENCE DOES THE REGRESSION CREATE OR THREATEN?

RESPONSE DETERMINATION
→ WHAT GOVERNED ACTION IS REQUIRED?
```
## Regression Classification States
```text
RC0 — CLASSIFICATION NOT REQUIRED
RC1 — CLASSIFICATION PENDING
RC2 — CLASSIFICATION IN PROGRESS
RC3 — MINOR REGRESSION
RC4 — MODERATE REGRESSION
RC5 — MAJOR REGRESSION
RC6 — CRITICAL REGRESSION
RC7 — EXTREME / CATASTROPHIC REGRESSION
RC8 — PERSISTENT REGRESSION
RC9 — RECURRENT REGRESSION
RC10 — SYSTEMIC REGRESSION
RC11 — MULTI-DOMAIN REGRESSION
RCX — UNKNOWN / INSUFFICIENT BASIS
RCR — CLASSIFICATION REJECTED / REASSESSMENT
RCS — CLASSIFICATION SUSPENDED
```
## Classification Dimensions
| Dimension | Required determination |
|---|---|
| Severity | Degree of regression |
| Scope | Affected boundary |
| Persistence | Sustained duration |
| Recurrence | Repeated occurrence |
| Consequence | Actual / threatened impact |
| Urgency | Required response speed |
| Domain | Security / resilience / compliance / data / AI etc. |
| Dependency | Critical downstream reliance |
| Detectability | Ability to identify progression |
| Containment | Existing control strength |
| Authority | Required escalation authority |
| Evidence | Supporting evidence |
| Confidence | Classification confidence |

## Classification Invariants

```text
CLASSIFICATION SHALL FOLLOW A VALID REGRESSION DETERMINATION OR AN EXPLICITLY GOVERNED POTENTIAL-REGRESSION PATH
```

```text
CLASSIFICATION SHALL NOT ALTER THE UNDERLYING REGRESSION EVIDENCE
```

```text
CLASSIFICATION CRITERIA SHALL BE APPROVED, EXPLICIT AND TRACEABLE
```

```text
SEVERITY, SCOPE, PERSISTENCE, RECURRENCE, CONSEQUENCE AND URGENCY SHALL BE CONSIDERED WHERE MATERIAL
```

```text
CLASSIFICATION SHALL NOT BE USED TO AVOID MANDATORY RESPONSE OR ESCALATION
```

```text
LOW SEVERITY SHALL NOT AUTOMATICALLY MEAN LOW SYSTEMIC RISK
```

```text
PERSISTENT OR RECURRENT REGRESSION MAY REQUIRE HIGHER CLASSIFICATION THAN A SINGLE EVENT
```

```text
UNKNOWN SHALL NOT BE CLASSIFIED AS MINOR BY DEFAULT
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE CLASSIFICATION SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT CLASSIFICATION SHALL CONSIDER AUTONOMY, AUTHORITY, TOOL ACCESS, DATA IMPACT AND OVERSIGHT
```

```text
CLASSIFICATION SHALL BE INDEPENDENT OF THE DESIRE TO PRESERVE CLOSURE OR AVOID REOPENING
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

```text
CONFLICTING CLASSIFICATION EVIDENCE SHALL BE RESOLVED OR ESCALATED
```

```text
CLASSIFICATION SHALL BE REVIEWED WHEN NEW EVIDENCE CHANGES SEVERITY, SCOPE OR CONSEQUENCE
```

```text
CLASSIFICATION SHALL SUPPORT RESPONSE PRIORITY WITHOUT REPLACING CONSEQUENCE DETERMINATION
```

```text
CLASSIFICATION RULES SHALL BE REVIEWED AFTER FALSE POSITIVES, FALSE NEGATIVES OR ESCALATION FAILURES
```

## 1. Classification Domain — Post-Closure Regression Classification Governance

**Control family:** `PCRC-001`

The Post-Closure Regression Classification Governance domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-001-01` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-001-02` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-001-03` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-001-04` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-001-05` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-001-06` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-001-07` — Establish and maintain the post-closure regression classification governance control.
- `PCRC-001-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 2. Classification Domain — Post-Closure Regression Classification Objective

**Control family:** `PCRC-002`

The Post-Closure Regression Classification Objective domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-002-01` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-002-02` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-002-03` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-002-04` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-002-05` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-002-06` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-002-07` — Establish and maintain the post-closure regression classification objective control.
- `PCRC-002-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 3. Classification Domain — Post-Closure Regression Classification Definition

**Control family:** `PCRC-003`

The Post-Closure Regression Classification Definition domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-003-01` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-003-02` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-003-03` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-003-04` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-003-05` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-003-06` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-003-07` — Establish and maintain the post-closure regression classification definition control.
- `PCRC-003-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 4. Classification Domain — Post-Closure Regression Classification Scope

**Control family:** `PCRC-004`

The Post-Closure Regression Classification Scope domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-004-01` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-004-02` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-004-03` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-004-04` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-004-05` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-004-06` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-004-07` — Establish and maintain the post-closure regression classification scope control.
- `PCRC-004-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 5. Classification Domain — Post-Closure Regression Classification Authority

**Control family:** `PCRC-005`

The Post-Closure Regression Classification Authority domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-005-01` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-005-02` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-005-03` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-005-04` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-005-05` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-005-06` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-005-07` — Establish and maintain the post-closure regression classification authority control.
- `PCRC-005-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 6. Classification Domain — Post-Closure Regression Classification Criteria

**Control family:** `PCRC-006`

The Post-Closure Regression Classification Criteria domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-006-01` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-006-02` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-006-03` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-006-04` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-006-05` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-006-06` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-006-07` — Establish and maintain the post-closure regression classification criteria control.
- `PCRC-006-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 7. Classification Domain — Post-Closure Regression Classification Preconditions

**Control family:** `PCRC-007`

The Post-Closure Regression Classification Preconditions domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-007-01` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-007-02` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-007-03` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-007-04` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-007-05` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-007-06` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-007-07` — Establish and maintain the post-closure regression classification preconditions control.
- `PCRC-007-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 8. Classification Domain — Post-Closure Regression Classification Evidence

**Control family:** `PCRC-008`

The Post-Closure Regression Classification Evidence domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-008-01` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-008-02` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-008-03` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-008-04` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-008-05` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-008-06` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-008-07` — Establish and maintain the post-closure regression classification evidence control.
- `PCRC-008-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 9. Classification Domain — Post-Closure Regression Classification Method

**Control family:** `PCRC-009`

The Post-Closure Regression Classification Method domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-009-01` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-009-02` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-009-03` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-009-04` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-009-05` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-009-06` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-009-07` — Establish and maintain the post-closure regression classification method control.
- `PCRC-009-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 10. Classification Domain — Post-Closure Regression Classification Decision

**Control family:** `PCRC-010`

The Post-Closure Regression Classification Decision domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-010-01` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-010-02` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-010-03` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-010-04` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-010-05` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-010-06` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-010-07` — Establish and maintain the post-closure regression classification decision control.
- `PCRC-010-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 11. Classification Domain — Post-Closure Regression Classification Accountability

**Control family:** `PCRC-011`

The Post-Closure Regression Classification Accountability domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-011-01` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-011-02` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-011-03` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-011-04` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-011-05` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-011-06` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-011-07` — Establish and maintain the post-closure regression classification accountability control.
- `PCRC-011-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 12. Classification Domain — Post-Closure Regression Classification Timing

**Control family:** `PCRC-012`

The Post-Closure Regression Classification Timing domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-012-01` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-012-02` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-012-03` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-012-04` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-012-05` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-012-06` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-012-07` — Establish and maintain the post-closure regression classification timing control.
- `PCRC-012-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 13. Classification Domain — Security Post-Closure Regression Classification

**Control family:** `PCRC-013`

The Security Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-013-01` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-013-02` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-013-03` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-013-04` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-013-05` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-013-06` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-013-07` — Establish and maintain the security post-closure regression classification control.
- `PCRC-013-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 14. Classification Domain — Resilience Post-Closure Regression Classification

**Control family:** `PCRC-014`

The Resilience Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-014-01` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-014-02` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-014-03` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-014-04` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-014-05` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-014-06` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-014-07` — Establish and maintain the resilience post-closure regression classification control.
- `PCRC-014-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 15. Classification Domain — Compliance Post-Closure Regression Classification

**Control family:** `PCRC-015`

The Compliance Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-015-01` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-015-02` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-015-03` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-015-04` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-015-05` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-015-06` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-015-07` — Establish and maintain the compliance post-closure regression classification control.
- `PCRC-015-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 16. Classification Domain — Data Post-Closure Regression Classification

**Control family:** `PCRC-016`

The Data Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-016-01` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-016-02` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-016-03` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-016-04` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-016-05` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-016-06` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-016-07` — Establish and maintain the data post-closure regression classification control.
- `PCRC-016-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 17. Classification Domain — AI and Agent Post-Closure Regression Classification

**Control family:** `PCRC-017`

The AI and Agent Post-Closure Regression Classification domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-017-01` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-017-02` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-017-03` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-017-04` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-017-05` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-017-06` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-017-07` — Establish and maintain the ai and agent post-closure regression classification control.
- `PCRC-017-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 18. Classification Domain — Post-Closure Regression Classification Failure

**Control family:** `PCRC-018`

The Post-Closure Regression Classification Failure domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-018-01` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-018-02` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-018-03` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-018-04` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-018-05` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-018-06` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-018-07` — Establish and maintain the post-closure regression classification failure control.
- `PCRC-018-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 19. Classification Domain — Post-Closure Regression Classification Independence

**Control family:** `PCRC-019`

The Post-Closure Regression Classification Independence domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-019-01` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-019-02` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-019-03` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-019-04` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-019-05` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-019-06` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-019-07` — Establish and maintain the post-closure regression classification independence control.
- `PCRC-019-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## 20. Classification Domain — Post-Closure Regression Classification Review and Learning

**Control family:** `PCRC-020`

The Post-Closure Regression Classification Review and Learning domain establishes governed mandatory regression-classification requirements.

### Required controls
- `PCRC-020-01` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-01-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-020-02` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-02-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-020-03` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-03-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-020-04` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-04-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-020-05` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-05-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-020-06` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-06-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.
- `PCRC-020-07` — Establish and maintain the post-closure regression classification review and learning control.
- `PCRC-020-07-E` — Preserve regression state, severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability, containment, authority, evidence and confidence.

```text
REGRESSION → ASSESS SEVERITY / SCOPE / CONSEQUENCE → CLASSIFY → PRIORITIZE RESPONSE
```

## Post-Closure Regression Classification Structure

| Element | Required definition |
|---|---|
| Severity | Degree of regression |
| Scope | Affected boundary |
| Persistence | Sustained duration |
| Recurrence | Repeated occurrence |
| Consequence | Actual / threatened impact |
| Urgency | Required response speed |
| Domain | Affected control domain |
| Dependency | Downstream reliance |
| Detectability | Ability to identify progression |
| Containment | Existing controls |
| Authority | Escalation authority |

## Post-Closure Regression Classification Objective

Categorize the significance, urgency, scope and governance priority of an established or governed potential regression so that response authority and escalation are proportionate and mandatory.

## Post-Closure Regression Classification Definition

Regression classification is the governed categorization of a regression according to approved severity, scope, persistence, recurrence, consequence, urgency and domain criteria.

## Post-Closure Regression Classification Scope

Scope includes minor, moderate, major, critical, extreme, persistent, recurrent, systemic and multi-domain regression classifications.

## Post-Closure Regression Classification Authority

Authority shall define who may classify, upgrade, downgrade, override, independently review or escalate a regression classification.

## Post-Closure Regression Classification Criteria

Criteria shall define severity, scope, persistence, recurrence, consequence, urgency, domain, dependency, detectability and containment.
```text
REGRESSION
↓
SEVERITY
+
SCOPE
+
PERSISTENCE
+
RECURRENCE
+
CONSEQUENCE
+
URGENCY
+
DOMAIN
↓
CLASSIFICATION
↓
RESPONSE PRIORITY / ESCALATION
```

## Post-Closure Regression Classification Preconditions

Preconditions include valid regression determination, classification criteria, relevant evidence, consequence context and authority model.

## Post-Closure Regression Classification Evidence

Evidence shall preserve regression determination, classification criteria, severity rationale, scope, persistence, recurrence, consequence, urgency, authority and confidence.

## Post-Closure Regression Classification Method

Methods may include rule-based scoring, severity matrices, consequence mapping, expert review, domain-specific classification and controlled decision support.
```text
REGRESSION
↓
ASSESS DIMENSIONS
↓
APPLY CLASSIFICATION RULES
↓
CLASS
↓
VERIFY ESCALATION
```

## Post-Closure Regression Classification Decision

Decision shall determine RC0, RC1, RC2, RC3, RC4, RC5, RC6, RC7, RC8, RC9, RC10, RC11, RCX, RCR or RCS.

## Post-Closure Regression Classification Accountability

Accountability shall remain explicit for classification quality, upgrades, downgrades, overrides, escalation and review.

## Post-Closure Regression Classification Timing

Classification shall occur promptly enough to determine mandatory response priority and authority before material consequence becomes uncontrolled.

## Security Post-Closure Regression Classification

Security regression classification shall consider exposure, privilege, attack-path reach, affected assets, containment and threat persistence.

## Resilience Post-Closure Regression Classification

Resilience regression classification shall consider service impact, capacity loss, redundancy loss, recovery degradation, duration and dependency.

## Compliance Post-Closure Regression Classification

Compliance regression classification shall consider obligation criticality, affected controls, reporting impact, duration and regulatory consequence.

## Data Post-Closure Regression Classification

Data regression classification shall consider affected data scope, integrity, availability, confidentiality, lineage and downstream reliance.

## AI and Agent Post-Closure Regression Classification

AI/agent regression classification shall consider autonomy, authority, tool access, data impact, scale, repeatability, containment and oversight.
```text
AI / AGENT REGRESSION
↓
AUTONOMY + AUTHORITY + TOOLS + DATA + SCALE + OVERSIGHT
↓
CLASSIFY
↓
ESCALATE / RESPOND
```

## Post-Closure Regression Classification Failure

Failure includes insufficient criteria, ambiguous severity, conflicting evidence, inappropriate downgrade, missed escalation or inability to classify reliably.
```text
CLASSIFICATION FAILURE
↓
MATERIAL DECISION AFFECTED?
├── YES → INDEPENDENT REVIEW / ESCALATE
└── NO → CORRECT / RECORD
```

## Post-Closure Regression Classification Independence

Independent classification may be required where the classification materially affects reopening, safety, security, compliance, reliance restoration or high-consequence response.

## Post-Closure Regression Classification Review and Learning

Reviews shall examine misclassification, escalation failures, severity drift, recurring patterns, systemic issues and inappropriate overrides.

## Classification Decision Model
```text
REGRESSION DETERMINED / GOVERNED POTENTIAL REGRESSION
↓
CLASSIFICATION CONTEXT VALID?
├── NO → CLASSIFICATION UNDETERMINED
└── YES
     ↓
ASSESS SEVERITY
     ↓
ASSESS SCOPE
     ↓
ASSESS PERSISTENCE / RECURRENCE
     ↓
ASSESS CONSEQUENCE
     ↓
ASSESS URGENCY
     ↓
ASSESS DOMAIN / DEPENDENCY / CONTAINMENT
     ↓
CLASSIFY
├── MINOR
├── MODERATE
├── MAJOR
├── CRITICAL
└── EXTREME / CATASTROPHIC
     ↓
CHECK PERSISTENT / RECURRENT / SYSTEMIC / MULTI-DOMAIN FLAGS
     ↓
SET RESPONSE PRIORITY + AUTHORITY + ESCALATION
```

## Classification Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| RC0 | Not required | Record basis |
| RC1 | Pending | Classify |
| RC2 | In progress | Complete assessment |
| RC3 | Minor | Controlled response / monitor |
| RC4 | Moderate | Formal response / escalation as required |
| RC5 | Major | Priority response |
| RC6 | Critical | Immediate high-authority response |
| RC7 | Extreme / catastrophic | Maximum governed response |
| RC8 | Persistent | Systemic assessment / sustained response |
| RC9 | Recurrent | Recurrence response / root-cause review |
| RC10 | Systemic | Cross-control / architecture response |
| RC11 | Multi-domain | Coordinated enterprise response |
| RCX | Unknown / insufficient | Do not default to minor |
| RCR | Rejected / reassessment | Correct / independent review |
| RCS | Suspended | Restore classification |

## Classification Record
| Field | Required |
|---|---|
| Classification ID | Yes |
| Regression ID | Yes |
| Regression State | Yes |
| Severity | Yes |
| Scope | Yes |
| Persistence | Where applicable |
| Recurrence | Where applicable |
| Consequence | Yes |
| Urgency | Yes |
| Domain | Yes |
| Dependency | Where applicable |
| Detectability | Where applicable |
| Containment | Yes where applicable |
| Classification State | Yes |
| Authority | Yes |
| Confidence | Yes |
| Evidence | Yes |

## Classification Is Not Regression Determination
Classification does not establish whether regression exists. It categorizes an already determined or governed potential regression.
```text
REGRESSION DETERMINATION
≠
CLASSIFICATION
```

## Classification Is Not Consequence Determination
Classification describes significance and urgency. Consequence determination establishes the actual or threatened consequence under the applicable consequence model.
```text
CLASSIFICATION
≠
CONSEQUENCE DETERMINATION
```

## Classification Is Not Response Determination
Classification determines priority and escalation needs; response determination specifies the required governed action.
```text
CLASSIFICATION
≠
RESPONSE
```

## Severity
Severity shall describe the degree of regression based on approved criteria. It shall not be reduced merely because immediate consequences have not yet materialized.

## Scope
Scope shall identify affected assets, controls, processes, services, data, users, domains or other relevant boundaries.

## Persistence
Persistent regression shall be classified with explicit consideration of duration and inability to restore the accepted state.

## Recurrence
Recurrent regression shall be treated as a potential systemic signal and shall not be repeatedly classified as isolated minor events without review.

## Systemic Regression
RC10 shall be available where regression indicates weakness in a common control, architecture, governance mechanism or shared dependency affecting multiple areas.

## Multi-Domain Regression
RC11 shall be available where regression crosses materially distinct domains and requires coordinated governance.

## Low Severity Does Not Mean Low Systemic Risk
A locally minor regression can have material systemic significance through dependency, scale, recurrence or aggregation.

## Unknown Classification
Insufficient evidence shall not default to minor. The classification shall remain unknown or require reassessment.
```text
UNKNOWN
≠
MINOR
```

## Upgrade / Downgrade
Classification shall be dynamically revisable when new evidence changes severity, scope, persistence, recurrence, consequence or urgency. All changes shall be traceable.

## AI and Agent Classification
AI/agent regression shall be classified using autonomy, authority, tool access, data impact, scale, repeatability, containment and oversight rather than model confidence alone.

## Relationship to Consequence Determination
RG-129 supplies classification and priority context to the subsequent consequence-determination layer.
```text
REGRESSION → CLASSIFICATION → CONSEQUENCE DETERMINATION → RESPONSE PRIORITY
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression-classification layer beneath regression determination and above consequence, alert, notification and response determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, qualification, validation, deviation, regression determination, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring activation, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Classification Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION → RESULT VALIDATION → RESULT QUALIFICATION → RESULT COMPARISON → DEVIATION DETERMINATION → REGRESSION DETERMINATION → MANDATORY REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → REOPENING
```

## Complete Classification Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-130` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Regression Consequence Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY CONFIRMED OR GOVERNED POTENTIAL POST-CLOSURE REGRESSION TO BE CLASSIFIED AGAINST EXPLICIT AND APPROVED CRITERIA FOR SEVERITY, SCOPE, PERSISTENCE, RECURRENCE, CONSEQUENCE, URGENCY, DOMAIN AND DEPENDENCY, WITH UNKNOWN, MINOR, MODERATE, MAJOR, CRITICAL, EXTREME, PERSISTENT, RECURRENT, SYSTEMIC AND MULTI-DOMAIN STATES DISTINGUISHED, SO THAT RESPONSE PRIORITY AND AUTHORITY ARE PROPORTIONATE, TRACEABLE AND CANNOT BE SILENTLY DOWNGRADED TO PRESERVE CLOSURE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CLASSIFICATION-DETERMINATION-01

# EA-IMETA-PRODUCTION-SERVICE-SECURITY-RESILIENCE-COMPLIANCE-CAPABILITY-TRANSFORMATION-PORTFOLIO-OPERATING-MODEL-CONTROL-ASSURANCE-TEST-RESULT-FINDING-REMEDIATION-VALIDATION-ACCEPTANCE-CLOSURE-MONITORING-REGRESSION-ASSESSMENT-DECISION-01

## Short File ID
`EA-IMETA-REGRESSION-ASSESSMENT-DECISION-01`

### Version 1.0
### Status: PRODUCTION REGRESSION ASSESSMENT DECISION BASELINE
### Governing Architecture: EA-IMETA-MASTER-01

## Purpose
Establish the authoritative decision architecture following regression assessment, ensuring that evidence, risk, materiality, authority and governance criteria produce an explicit and traceable disposition.

## Core Principle
A regression assessment produces an assessment conclusion; a decision converts that conclusion into an authorized action. The two stages shall remain logically distinct.

```text
REGRESSION ASSESSMENT
 ↓
EVIDENCE SUFFICIENCY
 ↓
RISK
 ↓
MATERIALITY
 ↓
AUTHORITY
 ↓
DECISION
 ├── NO REGRESSION
 ├── MONITOR
 ├── CONTAIN
 ├── NEW FINDING
 ├── REOPEN
 └── ESCALATE
```

## Decision Quality Test
```text
VALID ASSESSMENT
+
SUFFICIENT EVIDENCE
+
CURRENT RISK
+
MATERIALITY
+
AUTHORIZED DECISION MAKER
+
TRACEABLE RATIONALE
=
GOVERNED DECISION
```

## Decision Status Model
```text
NOT READY
READY FOR DECISION
UNDER REVIEW
UNDER CHALLENGE
DECISION PENDING
DECIDED
CONDITIONALLY DECIDED
ESCALATED
REJECTED
DEFERRED
EXECUTION ACTIVE
IMPLEMENTED
```

## Decision Invariants

```text
ASSESSMENT ≠ DECISION
```

```text
NO VALID ASSESSMENT → NO MATERIAL DECISION
```

```text
NO SUFFICIENT EVIDENCE → NO POSITIVE DECISION
```

```text
NO AUTHORITY → NO VALID DECISION
```

```text
DECISION SHALL REFLECT CURRENT RISK AND MATERIALITY
```

```text
CONTAINMENT ≠ REMEDIATION
```

```text
REOPENING ≠ AUTOMATIC REMEDIATION APPROVAL
```

```text
NEW FINDING SHALL BE USED WHEN THE CONDITION IS DISTINCT
```

```text
ESCALATION SHALL NOT BE USED TO AVOID DECISION OWNERSHIP
```

```text
DECISION RATIONALE SHALL BE TRACEABLE
```

```text
AI RECOMMENDATION ≠ GOVERNANCE DECISION
```

```text
AGENT EXECUTION ≠ DECISION AUTHORITY
```

```text
DECISIONS SHALL REMAIN IMMUTABLE AFTER APPROVAL; CHANGES CREATE NEW DECISION EVENTS
```

## 1. Decision Domain — Decision Governance

**Control family:** `RGD-001`

The Decision Governance domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-001-01` — Establish and operate the decision governance decision control.
- `RGD-001-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-001-02` — Establish and operate the decision governance decision control.
- `RGD-001-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-001-03` — Establish and operate the decision governance decision control.
- `RGD-001-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-001-04` — Establish and operate the decision governance decision control.
- `RGD-001-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-001-05` — Establish and operate the decision governance decision control.
- `RGD-001-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-001-06` — Establish and operate the decision governance decision control.
- `RGD-001-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-001-07` — Establish and operate the decision governance decision control.
- `RGD-001-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 2. Decision Domain — Decision Authority

**Control family:** `RGD-002`

The Decision Authority domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-002-01` — Establish and operate the decision authority decision control.
- `RGD-002-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-002-02` — Establish and operate the decision authority decision control.
- `RGD-002-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-002-03` — Establish and operate the decision authority decision control.
- `RGD-002-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-002-04` — Establish and operate the decision authority decision control.
- `RGD-002-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-002-05` — Establish and operate the decision authority decision control.
- `RGD-002-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-002-06` — Establish and operate the decision authority decision control.
- `RGD-002-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-002-07` — Establish and operate the decision authority decision control.
- `RGD-002-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 3. Decision Domain — Decision Rights

**Control family:** `RGD-003`

The Decision Rights domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-003-01` — Establish and operate the decision rights decision control.
- `RGD-003-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-003-02` — Establish and operate the decision rights decision control.
- `RGD-003-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-003-03` — Establish and operate the decision rights decision control.
- `RGD-003-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-003-04` — Establish and operate the decision rights decision control.
- `RGD-003-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-003-05` — Establish and operate the decision rights decision control.
- `RGD-003-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-003-06` — Establish and operate the decision rights decision control.
- `RGD-003-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-003-07` — Establish and operate the decision rights decision control.
- `RGD-003-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 4. Decision Domain — Decision Criteria

**Control family:** `RGD-004`

The Decision Criteria domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-004-01` — Establish and operate the decision criteria decision control.
- `RGD-004-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-004-02` — Establish and operate the decision criteria decision control.
- `RGD-004-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-004-03` — Establish and operate the decision criteria decision control.
- `RGD-004-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-004-04` — Establish and operate the decision criteria decision control.
- `RGD-004-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-004-05` — Establish and operate the decision criteria decision control.
- `RGD-004-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-004-06` — Establish and operate the decision criteria decision control.
- `RGD-004-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-004-07` — Establish and operate the decision criteria decision control.
- `RGD-004-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 5. Decision Domain — Evidence Sufficiency

**Control family:** `RGD-005`

The Evidence Sufficiency domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-005-01` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-005-02` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-005-03` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-005-04` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-005-05` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-005-06` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-005-07` — Establish and operate the evidence sufficiency decision control.
- `RGD-005-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 6. Decision Domain — Risk Decision

**Control family:** `RGD-006`

The Risk Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-006-01` — Establish and operate the risk decision decision control.
- `RGD-006-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-006-02` — Establish and operate the risk decision decision control.
- `RGD-006-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-006-03` — Establish and operate the risk decision decision control.
- `RGD-006-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-006-04` — Establish and operate the risk decision decision control.
- `RGD-006-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-006-05` — Establish and operate the risk decision decision control.
- `RGD-006-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-006-06` — Establish and operate the risk decision decision control.
- `RGD-006-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-006-07` — Establish and operate the risk decision decision control.
- `RGD-006-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 7. Decision Domain — Materiality Decision

**Control family:** `RGD-007`

The Materiality Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-007-01` — Establish and operate the materiality decision decision control.
- `RGD-007-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-007-02` — Establish and operate the materiality decision decision control.
- `RGD-007-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-007-03` — Establish and operate the materiality decision decision control.
- `RGD-007-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-007-04` — Establish and operate the materiality decision decision control.
- `RGD-007-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-007-05` — Establish and operate the materiality decision decision control.
- `RGD-007-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-007-06` — Establish and operate the materiality decision decision control.
- `RGD-007-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-007-07` — Establish and operate the materiality decision decision control.
- `RGD-007-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 8. Decision Domain — Security Decision

**Control family:** `RGD-008`

The Security Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-008-01` — Establish and operate the security decision decision control.
- `RGD-008-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-008-02` — Establish and operate the security decision decision control.
- `RGD-008-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-008-03` — Establish and operate the security decision decision control.
- `RGD-008-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-008-04` — Establish and operate the security decision decision control.
- `RGD-008-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-008-05` — Establish and operate the security decision decision control.
- `RGD-008-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-008-06` — Establish and operate the security decision decision control.
- `RGD-008-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-008-07` — Establish and operate the security decision decision control.
- `RGD-008-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 9. Decision Domain — Resilience Decision

**Control family:** `RGD-009`

The Resilience Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-009-01` — Establish and operate the resilience decision decision control.
- `RGD-009-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-009-02` — Establish and operate the resilience decision decision control.
- `RGD-009-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-009-03` — Establish and operate the resilience decision decision control.
- `RGD-009-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-009-04` — Establish and operate the resilience decision decision control.
- `RGD-009-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-009-05` — Establish and operate the resilience decision decision control.
- `RGD-009-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-009-06` — Establish and operate the resilience decision decision control.
- `RGD-009-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-009-07` — Establish and operate the resilience decision decision control.
- `RGD-009-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 10. Decision Domain — Data Decision

**Control family:** `RGD-010`

The Data Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-010-01` — Establish and operate the data decision decision control.
- `RGD-010-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-010-02` — Establish and operate the data decision decision control.
- `RGD-010-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-010-03` — Establish and operate the data decision decision control.
- `RGD-010-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-010-04` — Establish and operate the data decision decision control.
- `RGD-010-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-010-05` — Establish and operate the data decision decision control.
- `RGD-010-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-010-06` — Establish and operate the data decision decision control.
- `RGD-010-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-010-07` — Establish and operate the data decision decision control.
- `RGD-010-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 11. Decision Domain — AI and Agent Decision

**Control family:** `RGD-011`

The AI and Agent Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-011-01` — Establish and operate the ai and agent decision decision control.
- `RGD-011-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-011-02` — Establish and operate the ai and agent decision decision control.
- `RGD-011-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-011-03` — Establish and operate the ai and agent decision decision control.
- `RGD-011-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-011-04` — Establish and operate the ai and agent decision decision control.
- `RGD-011-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-011-05` — Establish and operate the ai and agent decision decision control.
- `RGD-011-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-011-06` — Establish and operate the ai and agent decision decision control.
- `RGD-011-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-011-07` — Establish and operate the ai and agent decision decision control.
- `RGD-011-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 12. Decision Domain — Compliance and Audit Decision

**Control family:** `RGD-012`

The Compliance and Audit Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-012-01` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-012-02` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-012-03` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-012-04` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-012-05` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-012-06` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-012-07` — Establish and operate the compliance and audit decision decision control.
- `RGD-012-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 13. Decision Domain — Financial and Benefit Decision

**Control family:** `RGD-013`

The Financial and Benefit Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-013-01` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-013-02` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-013-03` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-013-04` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-013-05` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-013-06` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-013-07` — Establish and operate the financial and benefit decision decision control.
- `RGD-013-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 14. Decision Domain — Architecture and Transformation Decision

**Control family:** `RGD-014`

The Architecture and Transformation Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-014-01` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-014-02` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-014-03` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-014-04` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-014-05` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-014-06` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-014-07` — Establish and operate the architecture and transformation decision decision control.
- `RGD-014-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 15. Decision Domain — Containment Decision

**Control family:** `RGD-015`

The Containment Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-015-01` — Establish and operate the containment decision decision control.
- `RGD-015-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-015-02` — Establish and operate the containment decision decision control.
- `RGD-015-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-015-03` — Establish and operate the containment decision decision control.
- `RGD-015-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-015-04` — Establish and operate the containment decision decision control.
- `RGD-015-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-015-05` — Establish and operate the containment decision decision control.
- `RGD-015-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-015-06` — Establish and operate the containment decision decision control.
- `RGD-015-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-015-07` — Establish and operate the containment decision decision control.
- `RGD-015-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 16. Decision Domain — Reopening Decision

**Control family:** `RGD-016`

The Reopening Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-016-01` — Establish and operate the reopening decision decision control.
- `RGD-016-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-016-02` — Establish and operate the reopening decision decision control.
- `RGD-016-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-016-03` — Establish and operate the reopening decision decision control.
- `RGD-016-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-016-04` — Establish and operate the reopening decision decision control.
- `RGD-016-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-016-05` — Establish and operate the reopening decision decision control.
- `RGD-016-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-016-06` — Establish and operate the reopening decision decision control.
- `RGD-016-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-016-07` — Establish and operate the reopening decision decision control.
- `RGD-016-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 17. Decision Domain — New Finding Decision

**Control family:** `RGD-017`

The New Finding Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-017-01` — Establish and operate the new finding decision decision control.
- `RGD-017-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-017-02` — Establish and operate the new finding decision decision control.
- `RGD-017-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-017-03` — Establish and operate the new finding decision decision control.
- `RGD-017-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-017-04` — Establish and operate the new finding decision decision control.
- `RGD-017-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-017-05` — Establish and operate the new finding decision decision control.
- `RGD-017-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-017-06` — Establish and operate the new finding decision decision control.
- `RGD-017-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-017-07` — Establish and operate the new finding decision decision control.
- `RGD-017-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 18. Decision Domain — Escalation Decision

**Control family:** `RGD-018`

The Escalation Decision domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-018-01` — Establish and operate the escalation decision decision control.
- `RGD-018-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-018-02` — Establish and operate the escalation decision decision control.
- `RGD-018-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-018-03` — Establish and operate the escalation decision decision control.
- `RGD-018-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-018-04` — Establish and operate the escalation decision decision control.
- `RGD-018-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-018-05` — Establish and operate the escalation decision decision control.
- `RGD-018-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-018-06` — Establish and operate the escalation decision decision control.
- `RGD-018-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-018-07` — Establish and operate the escalation decision decision control.
- `RGD-018-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 19. Decision Domain — Decision Recording

**Control family:** `RGD-019`

The Decision Recording domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-019-01` — Establish and operate the decision recording decision control.
- `RGD-019-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-019-02` — Establish and operate the decision recording decision control.
- `RGD-019-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-019-03` — Establish and operate the decision recording decision control.
- `RGD-019-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-019-04` — Establish and operate the decision recording decision control.
- `RGD-019-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-019-05` — Establish and operate the decision recording decision control.
- `RGD-019-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-019-06` — Establish and operate the decision recording decision control.
- `RGD-019-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-019-07` — Establish and operate the decision recording decision control.
- `RGD-019-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## 20. Decision Domain — Decision Learning

**Control family:** `RGD-020`

The Decision Learning domain establishes governed decision coverage after regression assessment.

### Required controls
- `RGD-020-01` — Establish and operate the decision learning decision control.
- `RGD-020-01-E` — Preserve decision evidence, authority and rationale.
- `RGD-020-02` — Establish and operate the decision learning decision control.
- `RGD-020-02-E` — Preserve decision evidence, authority and rationale.
- `RGD-020-03` — Establish and operate the decision learning decision control.
- `RGD-020-03-E` — Preserve decision evidence, authority and rationale.
- `RGD-020-04` — Establish and operate the decision learning decision control.
- `RGD-020-04-E` — Preserve decision evidence, authority and rationale.
- `RGD-020-05` — Establish and operate the decision learning decision control.
- `RGD-020-05-E` — Preserve decision evidence, authority and rationale.
- `RGD-020-06` — Establish and operate the decision learning decision control.
- `RGD-020-06-E` — Preserve decision evidence, authority and rationale.
- `RGD-020-07` — Establish and operate the decision learning decision control.
- `RGD-020-07-E` — Preserve decision evidence, authority and rationale.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → RECORD
```

## Decision Matrix
| Dimension | States |
|---|---|
| Assessment | Valid / Limited / Failed |
| Evidence | Missing / Partial / Sufficient / Invalid |
| Risk | Within Appetite / Elevated / Above Appetite / Critical |
| Materiality | Low / Medium / High / Critical |
| Authority | Confirmed / Delegated / Insufficient / Escalated |
| Decision | No Regression / Monitor / Contain / New Finding / Reopen / Escalate / Defer |
| Conditions | None / Open / Time-Bound / Verified |

## Decision Record Model
| Record | Minimum information |
|---|---|
| Decision Record | ID, assessment, evidence, risk, materiality, authority, decision, rationale, timestamp |
| Authority Record | role, authority level, delegation, scope, validity |
| Challenge Record | reviewer, challenge, response, resolution |
| Condition Record | condition, owner, due date, expiry, monitoring |
| Execution Record | action, owner, start, status, completion |
| Escalation Record | trigger, recipient, rationale, decision |

## Decision Lifecycle
```text
ASSESSMENT CONCLUSION
 ↓
PREPARE DECISION PACKAGE
 ↓
VERIFY EVIDENCE
 ↓
VERIFY RISK / MATERIALITY
 ↓
VERIFY AUTHORITY
 ↓
CHALLENGE
 ↓
DECIDE
 ↓
RECORD
 ↓
EXECUTE
 ↓
VERIFY OUTCOME
```

## Decision Outcomes
### 1. NO REGRESSION
Evidence supports that the deviation does not constitute regression. Monitoring continues with rationale retained.

### 2. MONITOR
Risk is controlled and no immediate reopening is required. Monitoring thresholds and review points shall be explicit.

### 3. CONTAIN
Immediate or short-term controls are required to limit impact while the permanent disposition is determined.

### 4. NEW FINDING
The condition is material but does not appropriately map to the previously closed finding. A new governed finding lifecycle is created.

### 5. REOPEN
The evidence demonstrates a material regression of the previously closed condition and the original lifecycle is reopened.

### 6. ESCALATE
Decision authority, risk, materiality or cross-domain impact exceeds the current decision level.

### 7. DEFER
A decision is intentionally postponed under explicit rationale, owner, due date and risk treatment.

## Reopening Decision Boundary
```text
CONFIRMED REGRESSION
 ↓
IS IT THE SAME CLOSED CONDITION?
 ├─ NO → NEW FINDING
 └─ YES
      ↓
IS MATERIALITY / RISK ABOVE GOVERNED THRESHOLD?
 ├─ NO → MONITOR / CONTAIN
 └─ YES → REOPEN
```

## AI and Agent Decision Governance
AI may recommend a disposition based on evidence and risk signals. Material decisions shall be authorized by the designated governance authority. Agents shall not exceed explicitly granted decision or execution authority.

```text
AI RECOMMENDATION
 ↓
HUMAN / GOVERNED REVIEW
 ↓
AUTHORIZED DECISION
 ↓
CONTROLLED EXECUTION
```

## Decision Learning
Decision outcomes shall be analyzed for recurring false positives, excessive escalation, delayed reopening, inappropriate containment, weak evidence, authority gaps and systemic control weaknesses.

## Complete Adaptive Assurance Loop
```text
CONTROL → ASSURANCE → TEST → RESULT → FINDING → REMEDIATION → VALIDATION → ACCEPTANCE → CLOSURE → MONITORING → REGRESSION → ASSESSMENT → DECISION → REOPENING / NEW FINDING / MONITORING → REMEDIATION → RE-VALIDATION → RE-ACCEPTANCE → RE-CLOSURE
```

## Next Document
`EA-IMETA-REGRESSION-DECISION-EXECUTION-01`

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL REGRESSION ASSESSMENT TO TERMINATE IN AN EXPLICIT, AUTHORIZED, EVIDENCE-BASED AND TRACEABLE DECISION, WITH CLEAR DISTINCTION BETWEEN MONITORING, CONTAINMENT, NEW FINDING, REOPENING, ESCALATION AND DEFERRAL.

# END OF EA-IMETA-PRODUCTION-SERVICE-SECURITY-RESILIENCE-COMPLIANCE-CAPABILITY-TRANSFORMATION-PORTFOLIO-OPERATING-MODEL-CONTROL-ASSURANCE-TEST-RESULT-FINDING-REMEDIATION-VALIDATION-ACCEPTANCE-CLOSURE-MONITORING-REGRESSION-ASSESSMENT-DECISION-01

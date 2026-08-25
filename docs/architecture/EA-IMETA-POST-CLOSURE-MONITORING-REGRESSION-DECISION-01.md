# EA-IMETA-PRODUCTION-SERVICE-SECURITY-RESILIENCE-COMPLIANCE-CAPABILITY-TRANSFORMATION-PORTFOLIO-OPERATING-MODEL-CONTROL-ASSURANCE-TEST-RESULT-FINDING-REMEDIATION-VALIDATION-ACCEPTANCE-CLOSURE-MONITORING-REGRESSION-DECISION-01

## Short File ID
`EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-DECISION-01`

### Version 1.0
### Status: POST-CLOSURE REGRESSION DECISION BASELINE
### Governing Architecture: EA-IMETA-MASTER-01

## Purpose
Establish the authoritative decision layer after post-closure regression assessment, converting an assessed condition into an explicit, authorized and traceable disposition while preserving the distinction between monitoring, containment, reopening, new finding and escalation.

## Core Principle
Post-closure regression assessment establishes what the signal means. The regression decision establishes what the organization is authorized to do about it.

```text
POST-CLOSURE REGRESSION ASSESSMENT
        ↓
DECISION PACKAGE
        ↓
EVIDENCE / RISK / MATERIALITY
        ↓
AUTHORITY
        ↓
DECISION
   ├── NO REGRESSION
   ├── CONTINUE MONITORING
   ├── CORRECT / CONTAIN
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
AUTHORIZED AUTHORITY
+
TRACEABLE RATIONALE
=
GOVERNED POST-CLOSURE REGRESSION DECISION
```

## Decision Status Model
```text
NOT READY
PACKAGE IN PREPARATION
READY FOR REVIEW
UNDER CHALLENGE
DECISION PENDING
DECIDED
CONDITIONAL
DEFERRED
ESCALATED
EXECUTION AUTHORIZED
MONITORING CONTINUES
REOPENING AUTHORIZED
```

## Decision Invariants

```text
ASSESSMENT ≠ DECISION
```

```text
NO VALID ASSESSMENT → NO MATERIAL DECISION
```

```text
NO SUFFICIENT EVIDENCE → NO POSITIVE REGRESSION DECISION
```

```text
AUTHORITY SHALL MATCH MATERIALITY AND RISK
```

```text
MONITORING CONTINUATION SHALL BE AN EXPLICIT DECISION
```

```text
CONTAINMENT ≠ REMEDIATION
```

```text
NEW FINDING ≠ REOPENING
```

```text
REOPENING SHALL REQUIRE EVIDENCE OF MATERIAL RECURRENCE
```

```text
ESCALATION SHALL NOT SUBSTITUTE FOR DECISION OWNERSHIP
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
DECISION RECORDS SHALL REMAIN IMMUTABLE
```

```text
DECISION OUTCOMES SHALL FEED EXECUTION OR MONITORING
```

## 1. Decision Domain — Regression Decision Governance

**Control family:** `PRD-001`

The Regression Decision Governance domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-001-01` — Establish and operate the regression decision governance control.
- `PRD-001-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-001-02` — Establish and operate the regression decision governance control.
- `PRD-001-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-001-03` — Establish and operate the regression decision governance control.
- `PRD-001-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-001-04` — Establish and operate the regression decision governance control.
- `PRD-001-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-001-05` — Establish and operate the regression decision governance control.
- `PRD-001-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-001-06` — Establish and operate the regression decision governance control.
- `PRD-001-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-001-07` — Establish and operate the regression decision governance control.
- `PRD-001-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 2. Decision Domain — Decision Trigger

**Control family:** `PRD-002`

The Decision Trigger domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-002-01` — Establish and operate the decision trigger control.
- `PRD-002-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-002-02` — Establish and operate the decision trigger control.
- `PRD-002-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-002-03` — Establish and operate the decision trigger control.
- `PRD-002-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-002-04` — Establish and operate the decision trigger control.
- `PRD-002-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-002-05` — Establish and operate the decision trigger control.
- `PRD-002-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-002-06` — Establish and operate the decision trigger control.
- `PRD-002-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-002-07` — Establish and operate the decision trigger control.
- `PRD-002-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 3. Decision Domain — Decision Package

**Control family:** `PRD-003`

The Decision Package domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-003-01` — Establish and operate the decision package control.
- `PRD-003-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-003-02` — Establish and operate the decision package control.
- `PRD-003-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-003-03` — Establish and operate the decision package control.
- `PRD-003-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-003-04` — Establish and operate the decision package control.
- `PRD-003-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-003-05` — Establish and operate the decision package control.
- `PRD-003-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-003-06` — Establish and operate the decision package control.
- `PRD-003-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-003-07` — Establish and operate the decision package control.
- `PRD-003-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 4. Decision Domain — Decision Authority

**Control family:** `PRD-004`

The Decision Authority domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-004-01` — Establish and operate the decision authority control.
- `PRD-004-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-004-02` — Establish and operate the decision authority control.
- `PRD-004-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-004-03` — Establish and operate the decision authority control.
- `PRD-004-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-004-04` — Establish and operate the decision authority control.
- `PRD-004-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-004-05` — Establish and operate the decision authority control.
- `PRD-004-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-004-06` — Establish and operate the decision authority control.
- `PRD-004-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-004-07` — Establish and operate the decision authority control.
- `PRD-004-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 5. Decision Domain — Decision Criteria

**Control family:** `PRD-005`

The Decision Criteria domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-005-01` — Establish and operate the decision criteria control.
- `PRD-005-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-005-02` — Establish and operate the decision criteria control.
- `PRD-005-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-005-03` — Establish and operate the decision criteria control.
- `PRD-005-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-005-04` — Establish and operate the decision criteria control.
- `PRD-005-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-005-05` — Establish and operate the decision criteria control.
- `PRD-005-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-005-06` — Establish and operate the decision criteria control.
- `PRD-005-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-005-07` — Establish and operate the decision criteria control.
- `PRD-005-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 6. Decision Domain — Evidence Sufficiency

**Control family:** `PRD-006`

The Evidence Sufficiency domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-006-01` — Establish and operate the evidence sufficiency control.
- `PRD-006-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-006-02` — Establish and operate the evidence sufficiency control.
- `PRD-006-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-006-03` — Establish and operate the evidence sufficiency control.
- `PRD-006-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-006-04` — Establish and operate the evidence sufficiency control.
- `PRD-006-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-006-05` — Establish and operate the evidence sufficiency control.
- `PRD-006-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-006-06` — Establish and operate the evidence sufficiency control.
- `PRD-006-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-006-07` — Establish and operate the evidence sufficiency control.
- `PRD-006-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 7. Decision Domain — Materiality Decision

**Control family:** `PRD-007`

The Materiality Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-007-01` — Establish and operate the materiality decision control.
- `PRD-007-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-007-02` — Establish and operate the materiality decision control.
- `PRD-007-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-007-03` — Establish and operate the materiality decision control.
- `PRD-007-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-007-04` — Establish and operate the materiality decision control.
- `PRD-007-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-007-05` — Establish and operate the materiality decision control.
- `PRD-007-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-007-06` — Establish and operate the materiality decision control.
- `PRD-007-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-007-07` — Establish and operate the materiality decision control.
- `PRD-007-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 8. Decision Domain — Risk Decision

**Control family:** `PRD-008`

The Risk Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-008-01` — Establish and operate the risk decision control.
- `PRD-008-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-008-02` — Establish and operate the risk decision control.
- `PRD-008-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-008-03` — Establish and operate the risk decision control.
- `PRD-008-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-008-04` — Establish and operate the risk decision control.
- `PRD-008-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-008-05` — Establish and operate the risk decision control.
- `PRD-008-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-008-06` — Establish and operate the risk decision control.
- `PRD-008-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-008-07` — Establish and operate the risk decision control.
- `PRD-008-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 9. Decision Domain — Security Decision

**Control family:** `PRD-009`

The Security Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-009-01` — Establish and operate the security decision control.
- `PRD-009-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-009-02` — Establish and operate the security decision control.
- `PRD-009-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-009-03` — Establish and operate the security decision control.
- `PRD-009-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-009-04` — Establish and operate the security decision control.
- `PRD-009-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-009-05` — Establish and operate the security decision control.
- `PRD-009-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-009-06` — Establish and operate the security decision control.
- `PRD-009-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-009-07` — Establish and operate the security decision control.
- `PRD-009-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 10. Decision Domain — Resilience Decision

**Control family:** `PRD-010`

The Resilience Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-010-01` — Establish and operate the resilience decision control.
- `PRD-010-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-010-02` — Establish and operate the resilience decision control.
- `PRD-010-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-010-03` — Establish and operate the resilience decision control.
- `PRD-010-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-010-04` — Establish and operate the resilience decision control.
- `PRD-010-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-010-05` — Establish and operate the resilience decision control.
- `PRD-010-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-010-06` — Establish and operate the resilience decision control.
- `PRD-010-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-010-07` — Establish and operate the resilience decision control.
- `PRD-010-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 11. Decision Domain — Data Decision

**Control family:** `PRD-011`

The Data Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-011-01` — Establish and operate the data decision control.
- `PRD-011-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-011-02` — Establish and operate the data decision control.
- `PRD-011-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-011-03` — Establish and operate the data decision control.
- `PRD-011-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-011-04` — Establish and operate the data decision control.
- `PRD-011-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-011-05` — Establish and operate the data decision control.
- `PRD-011-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-011-06` — Establish and operate the data decision control.
- `PRD-011-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-011-07` — Establish and operate the data decision control.
- `PRD-011-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 12. Decision Domain — AI and Agent Decision

**Control family:** `PRD-012`

The AI and Agent Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-012-01` — Establish and operate the ai and agent decision control.
- `PRD-012-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-012-02` — Establish and operate the ai and agent decision control.
- `PRD-012-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-012-03` — Establish and operate the ai and agent decision control.
- `PRD-012-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-012-04` — Establish and operate the ai and agent decision control.
- `PRD-012-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-012-05` — Establish and operate the ai and agent decision control.
- `PRD-012-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-012-06` — Establish and operate the ai and agent decision control.
- `PRD-012-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-012-07` — Establish and operate the ai and agent decision control.
- `PRD-012-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 13. Decision Domain — Compliance and Audit Decision

**Control family:** `PRD-013`

The Compliance and Audit Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-013-01` — Establish and operate the compliance and audit decision control.
- `PRD-013-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-013-02` — Establish and operate the compliance and audit decision control.
- `PRD-013-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-013-03` — Establish and operate the compliance and audit decision control.
- `PRD-013-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-013-04` — Establish and operate the compliance and audit decision control.
- `PRD-013-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-013-05` — Establish and operate the compliance and audit decision control.
- `PRD-013-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-013-06` — Establish and operate the compliance and audit decision control.
- `PRD-013-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-013-07` — Establish and operate the compliance and audit decision control.
- `PRD-013-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 14. Decision Domain — Financial and Benefit Decision

**Control family:** `PRD-014`

The Financial and Benefit Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-014-01` — Establish and operate the financial and benefit decision control.
- `PRD-014-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-014-02` — Establish and operate the financial and benefit decision control.
- `PRD-014-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-014-03` — Establish and operate the financial and benefit decision control.
- `PRD-014-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-014-04` — Establish and operate the financial and benefit decision control.
- `PRD-014-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-014-05` — Establish and operate the financial and benefit decision control.
- `PRD-014-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-014-06` — Establish and operate the financial and benefit decision control.
- `PRD-014-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-014-07` — Establish and operate the financial and benefit decision control.
- `PRD-014-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 15. Decision Domain — Architecture and Transformation Decision

**Control family:** `PRD-015`

The Architecture and Transformation Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-015-01` — Establish and operate the architecture and transformation decision control.
- `PRD-015-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-015-02` — Establish and operate the architecture and transformation decision control.
- `PRD-015-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-015-03` — Establish and operate the architecture and transformation decision control.
- `PRD-015-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-015-04` — Establish and operate the architecture and transformation decision control.
- `PRD-015-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-015-05` — Establish and operate the architecture and transformation decision control.
- `PRD-015-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-015-06` — Establish and operate the architecture and transformation decision control.
- `PRD-015-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-015-07` — Establish and operate the architecture and transformation decision control.
- `PRD-015-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 16. Decision Domain — Monitoring Continuation Decision

**Control family:** `PRD-016`

The Monitoring Continuation Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-016-01` — Establish and operate the monitoring continuation decision control.
- `PRD-016-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-016-02` — Establish and operate the monitoring continuation decision control.
- `PRD-016-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-016-03` — Establish and operate the monitoring continuation decision control.
- `PRD-016-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-016-04` — Establish and operate the monitoring continuation decision control.
- `PRD-016-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-016-05` — Establish and operate the monitoring continuation decision control.
- `PRD-016-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-016-06` — Establish and operate the monitoring continuation decision control.
- `PRD-016-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-016-07` — Establish and operate the monitoring continuation decision control.
- `PRD-016-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 17. Decision Domain — Containment Decision

**Control family:** `PRD-017`

The Containment Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-017-01` — Establish and operate the containment decision control.
- `PRD-017-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-017-02` — Establish and operate the containment decision control.
- `PRD-017-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-017-03` — Establish and operate the containment decision control.
- `PRD-017-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-017-04` — Establish and operate the containment decision control.
- `PRD-017-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-017-05` — Establish and operate the containment decision control.
- `PRD-017-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-017-06` — Establish and operate the containment decision control.
- `PRD-017-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-017-07` — Establish and operate the containment decision control.
- `PRD-017-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 18. Decision Domain — Reopening Decision

**Control family:** `PRD-018`

The Reopening Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-018-01` — Establish and operate the reopening decision control.
- `PRD-018-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-018-02` — Establish and operate the reopening decision control.
- `PRD-018-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-018-03` — Establish and operate the reopening decision control.
- `PRD-018-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-018-04` — Establish and operate the reopening decision control.
- `PRD-018-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-018-05` — Establish and operate the reopening decision control.
- `PRD-018-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-018-06` — Establish and operate the reopening decision control.
- `PRD-018-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-018-07` — Establish and operate the reopening decision control.
- `PRD-018-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 19. Decision Domain — Escalation Decision

**Control family:** `PRD-019`

The Escalation Decision domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-019-01` — Establish and operate the escalation decision control.
- `PRD-019-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-019-02` — Establish and operate the escalation decision control.
- `PRD-019-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-019-03` — Establish and operate the escalation decision control.
- `PRD-019-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-019-04` — Establish and operate the escalation decision control.
- `PRD-019-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-019-05` — Establish and operate the escalation decision control.
- `PRD-019-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-019-06` — Establish and operate the escalation decision control.
- `PRD-019-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-019-07` — Establish and operate the escalation decision control.
- `PRD-019-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## 20. Decision Domain — Decision Learning

**Control family:** `PRD-020`

The Decision Learning domain establishes governed decision coverage following post-closure regression assessment.

### Required controls
- `PRD-020-01` — Establish and operate the decision learning control.
- `PRD-020-01-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-020-02` — Establish and operate the decision learning control.
- `PRD-020-02-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-020-03` — Establish and operate the decision learning control.
- `PRD-020-03-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-020-04` — Establish and operate the decision learning control.
- `PRD-020-04-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-020-05` — Establish and operate the decision learning control.
- `PRD-020-05-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-020-06` — Establish and operate the decision learning control.
- `PRD-020-06-E` — Preserve evidence, authority, rationale and disposition traceability.
- `PRD-020-07` — Establish and operate the decision learning control.
- `PRD-020-07-E` — Preserve evidence, authority, rationale and disposition traceability.

```text
ASSESSMENT → CRITERIA → AUTHORITY → DECISION → DISPOSITION
```

## Decision Matrix
| Dimension | States |
|---|---|
| Assessment | Valid / Limited / Failed |
| Evidence | Missing / Partial / Sufficient / Invalid |
| Regression | Rejected / Suspected / Confirmed |
| Risk | Within Appetite / Elevated / Above Appetite / Critical |
| Materiality | Low / Medium / High / Critical |
| Authority | Confirmed / Delegated / Insufficient / Escalated |
| Decision | Monitor / Contain / New Finding / Reopen / Escalate / Reject |
| Conditions | None / Open / Time-Bound / Verified |

## Decision Record Model
| Record | Minimum information |
|---|---|
| Regression Decision | ID, assessment, evidence, risk, materiality, authority, decision, rationale |
| Decision Package | assessment, evidence, baseline, impact, risk, materiality, recommendation |
| Authority Record | role, authority, delegation, scope, validity |
| Challenge Record | challenger, issue, response, resolution |
| Condition Record | condition, owner, due date, expiry, monitoring |
| Execution Handoff | decision, scope, owner, authority, action, verification criteria |
| Monitoring Handoff | metric, threshold, owner, frequency, escalation |

## Decision Lifecycle
```text
ASSESSMENT COMPLETE
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
DISPOSITION
```

## Decision Outcomes
### NO REGRESSION
The assessment demonstrates that the signal does not represent regression. The closed lifecycle remains closed and monitoring continues.

### CONTINUE MONITORING
The condition requires observation but does not justify containment or reopening. Thresholds, owner and review point shall be explicit.

### CORRECT / CONTAIN
Controlled action is authorized to reduce an active deviation or exposure without necessarily reopening the original lifecycle.

### NEW FINDING
The condition is material but is not the same closed condition. A new finding lifecycle is created.

### REOPEN
The evidence demonstrates material recurrence of the previously closed condition and the original lifecycle is reopened.

### ESCALATE
Risk, materiality, authority or cross-domain impact exceeds the current governance level.

## Reopening Decision Boundary
```text
REGRESSION CONFIRMED
        ↓
SAME CLOSED CONDITION?
   ├── NO → NEW FINDING
   └── YES
        ↓
MATERIAL / ABOVE GOVERNED THRESHOLD?
   ├── NO → MONITOR / CONTAIN
   └── YES → REOPEN
```

## Monitoring Continuation Boundary
```text
NO REGRESSION / NON-MATERIAL
        ↓
REMAIN CLOSED
        ↓
UPDATE MONITORING IF REQUIRED
        ↓
CONTINUE POST-CLOSURE MONITORING
```

## AI and Agent Decision Governance
AI may synthesize evidence, calculate indicators, identify decision options and recommend a disposition. The formal decision shall remain with the designated governance authority.

```text
AI / AGENT RECOMMENDATION
        ↓
GOVERNED REVIEW
        ↓
AUTHORIZED DECISION
        ↓
CONTROLLED HANDOFF
```

## Decision Failure / Deferral
```text
DECISION NOT READY
        ↓
IDENTIFY GAP
        ↓
RISK TREATMENT / ADDITIONAL EVIDENCE
        ↓
REVIEW
        ↓
DECIDE
```

## Handoff to Execution
Where execution is required, the decision shall explicitly define scope, owner, authority, expected outcome, constraints, evidence requirements and verification criteria.

## Handoff to Monitoring
Where the lifecycle remains closed, the decision shall define any monitoring changes, thresholds, ownership, review frequency and escalation criteria.

## Relationship to Existing Architecture
This document specializes the decision layer for post-closure regression. It does not replace the generic regression assessment decision, execution, verification, re-validation, re-acceptance or re-closure architecture.

## Complete Adaptive Assurance Loop
```text
CONTROL → ASSURANCE → TEST → RESULT → FINDING → REMEDIATION → VALIDATION → ACCEPTANCE → CLOSURE → MONITORING → REGRESSION → ASSESSMENT → DECISION → EXECUTION → VERIFICATION → RE-VALIDATION → RE-ACCEPTANCE → RE-CLOSURE → POST-CLOSURE MONITORING → REGRESSION ASSESSMENT → REGRESSION DECISION
```

## Next Document
`EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-DECISION-EXECUTION-01`

## Final Principle
EA-IMETA SHALL REQUIRE POST-CLOSURE REGRESSION ASSESSMENTS TO TERMINATE IN AN EXPLICIT, AUTHORIZED AND TRACEABLE DECISION THAT CLEARLY DISTINGUISHES CONTINUED MONITORING, CONTAINMENT, NEW FINDING, REOPENING AND ESCALATION.

# END OF EA-IMETA-PRODUCTION-SERVICE-SECURITY-RESILIENCE-COMPLIANCE-CAPABILITY-TRANSFORMATION-PORTFOLIO-OPERATING-MODEL-CONTROL-ASSURANCE-TEST-RESULT-FINDING-REMEDIATION-VALIDATION-ACCEPTANCE-CLOSURE-MONITORING-REGRESSION-DECISION-01

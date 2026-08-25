# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-01

## Physical File ID
`EA-IMETA-PC-RG-019`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-019` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Escalation |
| Parent | EA-IMETA-PC-RG-018 — Mandatory Alerting |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory-escalation layer defining how material alerts, breaches, uncertainty, control failures, unresolved conditions and increasing risk are transferred to progressively higher or more appropriate authority so that the required state is protected and governed action occurs within the required time.

## Core Principle
Alerting communicates a material condition; escalation changes the level, urgency or authority of governance response. Escalation shall be explicit, time-bound where required, attributable and proportionate to materiality, risk and response urgency.

```text
MATERIAL ALERT / BREACH / UNCERTAINTY
      ↓
ESCALATION CRITERIA
      ↓
SEVERITY / URGENCY
      ↓
ESCALATION AUTHORITY
      ↓
ROUTE / TRANSFER
      ↓
ACKNOWLEDGE / DECIDE / ACT
      ↓
RESOLVE / REASSESS / FURTHER ESCALATE
```

## Escalation Quality Test
```text
DEFINED ESCALATION CONDITION
+
APPROPRIATE SEVERITY / URGENCY
+
IDENTIFIABLE AUTHORITY
+
TIME-BOUND RESPONSE EXPECTATION
+
TRACEABLE ROUTING
+
ACCOUNTABILITY
+
DECISION / ACTION PATH
+
FURTHER ESCALATION RULE
=
VALID GOVERNED ESCALATION
```

## Escalation Status Model
```text
NOT REQUIRED
READY
TRIGGERED
ROUTED
ACKNOWLEDGED
IN DECISION
IN ACTION
FURTHER ESCALATED
CONTAINED
RESOLVED
REASSESSED
UNRESOLVED
OVERDUE
FAILED
UNDER REVIEW
SUPERSEDED
```

## Escalation Invariants

```text
EVERY MATERIAL ESCALATION CONDITION SHALL HAVE AN EXPLICIT ESCALATION RULE
```

```text
ESCALATION AUTHORITY SHALL BE IDENTIFIABLE
```

```text
ESCALATION SHALL OCCUR WITHIN THE REQUIRED RESPONSE WINDOW
```

```text
ESCALATION SHALL BE PROPORTIONATE TO MATERIALITY, IMPACT, RISK AND URGENCY
```

```text
UNACKNOWLEDGED MATERIAL ALERTS SHALL ESCALATE ACCORDING TO DEFINED RULES
```

```text
ESCALATION SHALL NOT BE BLOCKED BY A SINGLE UNCONTROLLED PERSON OR CHANNEL WHERE MATERIAL
```

```text
ESCALATION SHALL PRESERVE THE ORIGINAL SIGNAL, CONTEXT, EVIDENCE AND DECISION HISTORY
```

```text
ESCALATION SHALL NOT AUTOMATICALLY TRANSFER ACCOUNTABILITY AWAY FROM THE ORIGINAL ACCOUNTABLE ROLE
```

```text
FURTHER ESCALATION SHALL OCCUR WHEN THE CURRENT AUTHORITY CANNOT RESOLVE OR CONTROL THE CONDITION
```

```text
ESCALATION FAILURE SHALL ITSELF BE TREATED AS A GOVERNED CONTROL FAILURE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE ESCALATIONS SHALL RECEIVE APPROPRIATE AUTHORITY AND URGENCY
```

```text
AI AND AGENT ESCALATION SHALL PROTECT HUMAN GOVERNANCE BOUNDARIES WHERE AUTONOMOUS BEHAVIOUR EXCEEDS AUTHORITY
```

```text
ESCALATION SHALL NOT BE USED TO DELAY OR AVOID REQUIRED RESPONSE
```

```text
ESCALATION CLOSURE SHALL REQUIRE EXPLICIT RESOLUTION OR A GOVERNED TRANSITION TO REASSESSMENT
```

```text
HISTORICAL ESCALATIONS SHALL REMAIN PRESERVED FOR TRACEABILITY AND LEARNING
```

## 1. Escalation Domain — Escalation Governance

**Control family:** `PCRME-001`

The Escalation Governance domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-001-01` — Establish and maintain the escalation governance control.
- `PCRME-001-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-001-02` — Establish and maintain the escalation governance control.
- `PCRME-001-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-001-03` — Establish and maintain the escalation governance control.
- `PCRME-001-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-001-04` — Establish and maintain the escalation governance control.
- `PCRME-001-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-001-05` — Establish and maintain the escalation governance control.
- `PCRME-001-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-001-06` — Establish and maintain the escalation governance control.
- `PCRME-001-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-001-07` — Establish and maintain the escalation governance control.
- `PCRME-001-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 2. Escalation Domain — Escalation Objective

**Control family:** `PCRME-002`

The Escalation Objective domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-002-01` — Establish and maintain the escalation objective control.
- `PCRME-002-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-002-02` — Establish and maintain the escalation objective control.
- `PCRME-002-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-002-03` — Establish and maintain the escalation objective control.
- `PCRME-002-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-002-04` — Establish and maintain the escalation objective control.
- `PCRME-002-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-002-05` — Establish and maintain the escalation objective control.
- `PCRME-002-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-002-06` — Establish and maintain the escalation objective control.
- `PCRME-002-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-002-07` — Establish and maintain the escalation objective control.
- `PCRME-002-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 3. Escalation Domain — Escalation Definition

**Control family:** `PCRME-003`

The Escalation Definition domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-003-01` — Establish and maintain the escalation definition control.
- `PCRME-003-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-003-02` — Establish and maintain the escalation definition control.
- `PCRME-003-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-003-03` — Establish and maintain the escalation definition control.
- `PCRME-003-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-003-04` — Establish and maintain the escalation definition control.
- `PCRME-003-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-003-05` — Establish and maintain the escalation definition control.
- `PCRME-003-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-003-06` — Establish and maintain the escalation definition control.
- `PCRME-003-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-003-07` — Establish and maintain the escalation definition control.
- `PCRME-003-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 4. Escalation Domain — Escalation Scope

**Control family:** `PCRME-004`

The Escalation Scope domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-004-01` — Establish and maintain the escalation scope control.
- `PCRME-004-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-004-02` — Establish and maintain the escalation scope control.
- `PCRME-004-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-004-03` — Establish and maintain the escalation scope control.
- `PCRME-004-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-004-04` — Establish and maintain the escalation scope control.
- `PCRME-004-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-004-05` — Establish and maintain the escalation scope control.
- `PCRME-004-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-004-06` — Establish and maintain the escalation scope control.
- `PCRME-004-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-004-07` — Establish and maintain the escalation scope control.
- `PCRME-004-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 5. Escalation Domain — Escalation Authority

**Control family:** `PCRME-005`

The Escalation Authority domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-005-01` — Establish and maintain the escalation authority control.
- `PCRME-005-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-005-02` — Establish and maintain the escalation authority control.
- `PCRME-005-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-005-03` — Establish and maintain the escalation authority control.
- `PCRME-005-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-005-04` — Establish and maintain the escalation authority control.
- `PCRME-005-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-005-05` — Establish and maintain the escalation authority control.
- `PCRME-005-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-005-06` — Establish and maintain the escalation authority control.
- `PCRME-005-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-005-07` — Establish and maintain the escalation authority control.
- `PCRME-005-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 6. Escalation Domain — Escalation Severity

**Control family:** `PCRME-006`

The Escalation Severity domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-006-01` — Establish and maintain the escalation severity control.
- `PCRME-006-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-006-02` — Establish and maintain the escalation severity control.
- `PCRME-006-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-006-03` — Establish and maintain the escalation severity control.
- `PCRME-006-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-006-04` — Establish and maintain the escalation severity control.
- `PCRME-006-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-006-05` — Establish and maintain the escalation severity control.
- `PCRME-006-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-006-06` — Establish and maintain the escalation severity control.
- `PCRME-006-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-006-07` — Establish and maintain the escalation severity control.
- `PCRME-006-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 7. Escalation Domain — Escalation Criteria

**Control family:** `PCRME-007`

The Escalation Criteria domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-007-01` — Establish and maintain the escalation criteria control.
- `PCRME-007-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-007-02` — Establish and maintain the escalation criteria control.
- `PCRME-007-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-007-03` — Establish and maintain the escalation criteria control.
- `PCRME-007-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-007-04` — Establish and maintain the escalation criteria control.
- `PCRME-007-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-007-05` — Establish and maintain the escalation criteria control.
- `PCRME-007-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-007-06` — Establish and maintain the escalation criteria control.
- `PCRME-007-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-007-07` — Establish and maintain the escalation criteria control.
- `PCRME-007-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 8. Escalation Domain — Escalation Timing

**Control family:** `PCRME-008`

The Escalation Timing domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-008-01` — Establish and maintain the escalation timing control.
- `PCRME-008-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-008-02` — Establish and maintain the escalation timing control.
- `PCRME-008-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-008-03` — Establish and maintain the escalation timing control.
- `PCRME-008-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-008-04` — Establish and maintain the escalation timing control.
- `PCRME-008-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-008-05` — Establish and maintain the escalation timing control.
- `PCRME-008-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-008-06` — Establish and maintain the escalation timing control.
- `PCRME-008-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-008-07` — Establish and maintain the escalation timing control.
- `PCRME-008-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 9. Escalation Domain — Escalation Routing

**Control family:** `PCRME-009`

The Escalation Routing domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-009-01` — Establish and maintain the escalation routing control.
- `PCRME-009-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-009-02` — Establish and maintain the escalation routing control.
- `PCRME-009-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-009-03` — Establish and maintain the escalation routing control.
- `PCRME-009-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-009-04` — Establish and maintain the escalation routing control.
- `PCRME-009-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-009-05` — Establish and maintain the escalation routing control.
- `PCRME-009-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-009-06` — Establish and maintain the escalation routing control.
- `PCRME-009-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-009-07` — Establish and maintain the escalation routing control.
- `PCRME-009-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 10. Escalation Domain — Escalation Evidence

**Control family:** `PCRME-010`

The Escalation Evidence domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-010-01` — Establish and maintain the escalation evidence control.
- `PCRME-010-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-010-02` — Establish and maintain the escalation evidence control.
- `PCRME-010-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-010-03` — Establish and maintain the escalation evidence control.
- `PCRME-010-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-010-04` — Establish and maintain the escalation evidence control.
- `PCRME-010-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-010-05` — Establish and maintain the escalation evidence control.
- `PCRME-010-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-010-06` — Establish and maintain the escalation evidence control.
- `PCRME-010-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-010-07` — Establish and maintain the escalation evidence control.
- `PCRME-010-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 11. Escalation Domain — Escalation Accountability

**Control family:** `PCRME-011`

The Escalation Accountability domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-011-01` — Establish and maintain the escalation accountability control.
- `PCRME-011-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-011-02` — Establish and maintain the escalation accountability control.
- `PCRME-011-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-011-03` — Establish and maintain the escalation accountability control.
- `PCRME-011-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-011-04` — Establish and maintain the escalation accountability control.
- `PCRME-011-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-011-05` — Establish and maintain the escalation accountability control.
- `PCRME-011-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-011-06` — Establish and maintain the escalation accountability control.
- `PCRME-011-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-011-07` — Establish and maintain the escalation accountability control.
- `PCRME-011-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 12. Escalation Domain — Escalation Decision

**Control family:** `PCRME-012`

The Escalation Decision domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-012-01` — Establish and maintain the escalation decision control.
- `PCRME-012-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-012-02` — Establish and maintain the escalation decision control.
- `PCRME-012-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-012-03` — Establish and maintain the escalation decision control.
- `PCRME-012-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-012-04` — Establish and maintain the escalation decision control.
- `PCRME-012-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-012-05` — Establish and maintain the escalation decision control.
- `PCRME-012-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-012-06` — Establish and maintain the escalation decision control.
- `PCRME-012-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-012-07` — Establish and maintain the escalation decision control.
- `PCRME-012-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 13. Escalation Domain — Security Escalation

**Control family:** `PCRME-013`

The Security Escalation domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-013-01` — Establish and maintain the security escalation control.
- `PCRME-013-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-013-02` — Establish and maintain the security escalation control.
- `PCRME-013-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-013-03` — Establish and maintain the security escalation control.
- `PCRME-013-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-013-04` — Establish and maintain the security escalation control.
- `PCRME-013-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-013-05` — Establish and maintain the security escalation control.
- `PCRME-013-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-013-06` — Establish and maintain the security escalation control.
- `PCRME-013-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-013-07` — Establish and maintain the security escalation control.
- `PCRME-013-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 14. Escalation Domain — Resilience Escalation

**Control family:** `PCRME-014`

The Resilience Escalation domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-014-01` — Establish and maintain the resilience escalation control.
- `PCRME-014-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-014-02` — Establish and maintain the resilience escalation control.
- `PCRME-014-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-014-03` — Establish and maintain the resilience escalation control.
- `PCRME-014-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-014-04` — Establish and maintain the resilience escalation control.
- `PCRME-014-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-014-05` — Establish and maintain the resilience escalation control.
- `PCRME-014-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-014-06` — Establish and maintain the resilience escalation control.
- `PCRME-014-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-014-07` — Establish and maintain the resilience escalation control.
- `PCRME-014-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 15. Escalation Domain — Compliance Escalation

**Control family:** `PCRME-015`

The Compliance Escalation domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-015-01` — Establish and maintain the compliance escalation control.
- `PCRME-015-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-015-02` — Establish and maintain the compliance escalation control.
- `PCRME-015-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-015-03` — Establish and maintain the compliance escalation control.
- `PCRME-015-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-015-04` — Establish and maintain the compliance escalation control.
- `PCRME-015-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-015-05` — Establish and maintain the compliance escalation control.
- `PCRME-015-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-015-06` — Establish and maintain the compliance escalation control.
- `PCRME-015-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-015-07` — Establish and maintain the compliance escalation control.
- `PCRME-015-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 16. Escalation Domain — Data Escalation

**Control family:** `PCRME-016`

The Data Escalation domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-016-01` — Establish and maintain the data escalation control.
- `PCRME-016-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-016-02` — Establish and maintain the data escalation control.
- `PCRME-016-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-016-03` — Establish and maintain the data escalation control.
- `PCRME-016-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-016-04` — Establish and maintain the data escalation control.
- `PCRME-016-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-016-05` — Establish and maintain the data escalation control.
- `PCRME-016-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-016-06` — Establish and maintain the data escalation control.
- `PCRME-016-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-016-07` — Establish and maintain the data escalation control.
- `PCRME-016-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 17. Escalation Domain — AI and Agent Escalation

**Control family:** `PCRME-017`

The AI and Agent Escalation domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-017-01` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-017-02` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-017-03` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-017-04` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-017-05` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-017-06` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-017-07` — Establish and maintain the ai and agent escalation control.
- `PCRME-017-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 18. Escalation Domain — Escalation Failure

**Control family:** `PCRME-018`

The Escalation Failure domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-018-01` — Establish and maintain the escalation failure control.
- `PCRME-018-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-018-02` — Establish and maintain the escalation failure control.
- `PCRME-018-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-018-03` — Establish and maintain the escalation failure control.
- `PCRME-018-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-018-04` — Establish and maintain the escalation failure control.
- `PCRME-018-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-018-05` — Establish and maintain the escalation failure control.
- `PCRME-018-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-018-06` — Establish and maintain the escalation failure control.
- `PCRME-018-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-018-07` — Establish and maintain the escalation failure control.
- `PCRME-018-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 19. Escalation Domain — Escalation Resolution

**Control family:** `PCRME-019`

The Escalation Resolution domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-019-01` — Establish and maintain the escalation resolution control.
- `PCRME-019-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-019-02` — Establish and maintain the escalation resolution control.
- `PCRME-019-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-019-03` — Establish and maintain the escalation resolution control.
- `PCRME-019-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-019-04` — Establish and maintain the escalation resolution control.
- `PCRME-019-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-019-05` — Establish and maintain the escalation resolution control.
- `PCRME-019-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-019-06` — Establish and maintain the escalation resolution control.
- `PCRME-019-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-019-07` — Establish and maintain the escalation resolution control.
- `PCRME-019-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## 20. Escalation Domain — Escalation Review and Learning

**Control family:** `PCRME-020`

The Escalation Review and Learning domain establishes governed mandatory-escalation requirements for post-closure regression.

### Required controls
- `PCRME-020-01` — Establish and maintain the escalation review and learning control.
- `PCRME-020-01-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-020-02` — Establish and maintain the escalation review and learning control.
- `PCRME-020-02-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-020-03` — Establish and maintain the escalation review and learning control.
- `PCRME-020-03-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-020-04` — Establish and maintain the escalation review and learning control.
- `PCRME-020-04-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-020-05` — Establish and maintain the escalation review and learning control.
- `PCRME-020-05-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-020-06` — Establish and maintain the escalation review and learning control.
- `PCRME-020-06-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.
- `PCRME-020-07` — Establish and maintain the escalation review and learning control.
- `PCRME-020-07-E` — Preserve trigger, severity, authority, routing, timestamps, accountability, decision, action and disposition traceability.

```text
TRIGGER → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## Escalation Structure

| Element | Required definition |
|---|---|
| Trigger | Condition requiring escalation |
| Severity | Materiality / impact level |
| Urgency | Required response time |
| Authority | Receiving decision authority |
| Route | Escalation path |
| Accountability | Accountable role retained or assigned |
| Evidence | Supporting context and proof |
| Decision | Required governance decision |
| Action | Required control or response |
| Further Escalation | Next authority if unresolved |
| Closure | Conditions for ending escalation |

## Escalation Objective

The objective is to ensure that conditions exceeding local authority, tolerance, capability, response time or governance boundaries receive timely intervention by an appropriate authority.

## Escalation Definition

Escalation is the governed transfer or elevation of a material condition, decision, risk or unresolved control issue to an authority or response level capable of controlling, deciding or resolving it.

## Escalation Scope

Scope shall identify the state, alert, service, system, control, process, data, environment, dependency or decision affected by the escalation.

## Escalation Authority

Authority shall define who receives escalation, who may decide, who may authorize containment, who may allocate resources and who may invoke further escalation. Escalation shall not silently create authority that did not previously exist.

## Escalation Severity

Severity shall reflect potential impact and materiality.

```text
LOW → LOCAL MANAGEMENT
MODERATE → FUNCTIONAL AUTHORITY
HIGH → SENIOR GOVERNANCE
CRITICAL → EXECUTIVE / EMERGENCY AUTHORITY
```

## Escalation Criteria

Criteria shall define when escalation is mandatory, optional, prohibited or automatically triggered. Typical triggers include material breach, unresolved critical alert, threshold exceedance, overdue response, control failure, uncertainty, authority boundary breach and increasing risk.

## Escalation Timing

Timing shall define acknowledgement, decision, action and further-escalation deadlines. Critical conditions shall not wait for routine reporting cycles.

## Escalation Routing

Routing shall provide primary and fallback paths to the appropriate authority.

```text
ESCALATION
↓
PRIMARY AUTHORITY
├── ACCEPTED → DECIDE / ACT
└── UNAVAILABLE / INSUFFICIENT → FALLBACK AUTHORITY
                         ↓
                      FURTHER ESCALATE
```

## Escalation Evidence

Escalation evidence shall preserve the original alert or trigger, relevant measurements, thresholds, context, impact, decisions, actions and timestamps. Evidence shall remain traceable through resolution.

## Escalation Accountability

Escalation does not automatically remove accountability from the originating accountable role. Responsibilities shall remain explicit while decision authority may move to a higher level.

## Escalation Decision

The receiving authority shall make or initiate the required decision. Decisions may include continue, contain, limit, suspend, remediate, invoke contingency, accept risk where authorized, reassess or escalate further.

```text
ESCALATED CONDITION
↓
DECISION
├── CONTAIN
├── REMEDIATE
├── LIMIT / SUSPEND
├── ACCEPT AUTHORIZED RISK
├── REASSESS
└── FURTHER ESCALATE
```

## Security Escalation

Security escalation shall protect against material security breaches, unauthorized access, control failure, significant exposure, policy violations and boundary compromise.

## Resilience Escalation

Resilience escalation shall address material service degradation, dependency failure, capacity constraints, recovery failure, continuity threats and loss of required operating state.

## Compliance Escalation

Compliance escalation shall address material non-conformance, regulatory or contractual exposure, repeated control failure and conditions requiring authorized legal, compliance or governance intervention.

## Data Escalation

Data escalation shall address material integrity, quality, lineage, access, retention, privacy or authorized-use conditions that exceed local control authority or tolerance.

## AI and Agent Escalation

AI and agent escalation shall protect human and governance authority when autonomous behaviour exceeds approved policy, tool, data, autonomy or decision boundaries.

```text
AI / AGENT EVENT
↓
WITHIN AUTHORITY?
├── YES → CONTINUE GOVERNED RESPONSE
└── NO → LIMIT / SUSPEND AUTONOMY
          ↓
       HUMAN / GOVERNANCE ESCALATION
          ↓
       DECIDE / CONTAIN / REASSESS
```

## Escalation Failure

Failure to route, acknowledge, decide or act on a mandatory escalation within the required time is itself a control failure.

```text
ESCALATION FAILURE
↓
PROTECT REQUIRED STATE
↓
FALLBACK AUTHORITY / OUT-OF-BAND RESPONSE
↓
ASSESS IMPACT
↓
REMEDIATE / REASSESS
```

## Escalation Resolution

Escalation shall close only when the triggering condition is resolved, contained under an authorized and governed state, or formally transferred to another governed lifecycle such as reassessment or remediation.

```text
ESCALATED
↓
CONDITION CONTROLLED?
├── NO → FURTHER ESCALATE
└── YES
     ↓
RESOLUTION EVIDENCE
     ↓
REASSESS / REVALIDATE IF REQUIRED
     ↓
CLOSE ESCALATION
```

## Escalation Review and Learning

Escalation patterns shall be reviewed for delayed escalation, incorrect routing, unclear authority, excessive thresholds, repeated unresolved events, weak fallback paths and systemic control deficiencies.

## Escalation Determination Model
```text
TRIGGER PRESENT?
├── NO → CONTINUE MONITORING
└── YES
     ↓
MANDATORY ESCALATION CRITERIA MET?
├── NO → LOCAL GOVERNANCE / RECORD
└── YES
     ↓
APPROPRIATE AUTHORITY AVAILABLE?
├── NO → FALLBACK / FURTHER ESCALATE
└── YES
     ↓
ACKNOWLEDGED WITHIN REQUIRED TIME?
├── NO → FURTHER ESCALATE
└── YES
     ↓
DECISION / ACTION EFFECTIVE?
├── YES → RESOLVE / REASSESS
└── NO → FURTHER ESCALATE / CONTAIN
```

## Escalation Record
| Field | Required |
|---|---|
| Escalation ID | Yes |
| Trigger / Alert ID | Yes |
| Trigger Timestamp | Yes |
| Severity | Yes |
| Urgency / Deadline | Yes |
| Originating Authority | Yes |
| Receiving Authority | Yes |
| Route | Yes |
| Acknowledgement | Yes |
| Decision | Yes |
| Action | Yes |
| Accountability | Yes |
| Further Escalation | Where applicable |
| Evidence References | Yes |
| Resolution | Yes |
| Reassessment Reference | Where applicable |

## Escalation Ladder
```text
LEVEL 0 — LOCAL CONTROL
      ↓ unresolved / exceeds authority
LEVEL 1 — FUNCTIONAL AUTHORITY
      ↓ unresolved / material risk
LEVEL 2 — SENIOR GOVERNANCE
      ↓ critical / cross-domain / enterprise impact
LEVEL 3 — EXECUTIVE / EMERGENCY AUTHORITY
      ↓
ENTERPRISE RESPONSE / CRISIS GOVERNANCE
```

## Escalation Accountability Model
```text
ORIGINATING ACCOUNTABLE ROLE
        │
        ├── PROVIDES CONTEXT / EVIDENCE
        ├── REMAINS ACCOUNTABLE FOR ORIGINATING CONTROL
        │
        ↓
RECEIVING DECISION AUTHORITY
        │
        ├── DECIDES / DIRECTS ACTION
        └── MAY FURTHER ESCALATE
```

## Escalation Anti-Gaming Control
Escalation shall not be delayed, downgraded, redirected or repeatedly reclassified to avoid accountability, reporting, governance scrutiny or operational impact. The severity and authority shall reflect the actual material condition.

## Escalation Change Control
Changes to escalation criteria, severity, authority, routing, timing, fallback paths, decision rights or closure rules shall be governed, approved, versioned and effective-dated.

```text
CURRENT ESCALATION MODEL
↓
CHANGE PROPOSAL
↓
IMPACT / RISK ASSESSMENT
↓
AUTHORITY APPROVAL
↓
NEW VERSION
↓
EFFECTIVE DATE
```

Historical escalation records, decisions, routing and rule versions shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory-escalation layer beneath mandatory alerting. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, acceptance, reliance, monitoring or alerting layers.

## Governance-to-Escalation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → ACCEPTANCE → RELIANCE → MONITORING → ALERTING → MANDATORY ESCALATION → DECISION → ACTION → RESOLUTION / REASSESSMENT
```

## Complete Escalation Chain
```text
MANDATORY STATE → VERIFY → EVIDENCE → MEASURE → THRESHOLD → CLASSIFY → CONSEQUENCE → RESPOND → EFFECTIVENESS → REASSESS → REVALIDATE → ACCEPT → RELY → MONITOR → ALERT → ESCALATE → DECIDE → ACT → RESOLVE / REASSESS
```

## Next Document
`EA-IMETA-PC-RG-020` — Mandatory Resolution

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL CONDITION THAT EXCEEDS LOCAL AUTHORITY, TOLERANCE, CAPABILITY, RESPONSE TIME OR GOVERNANCE BOUNDARIES TO BE ESCALATED TO AN APPROPRIATE AUTHORITY WITH DEFINED SEVERITY, URGENCY, ROUTING, ACCOUNTABILITY, DECISION RIGHTS, FALLBACK PATHS AND FURTHER-ESCALATION RULES, UNTIL THE CONDITION IS RESOLVED, CONTROLLED OR TRANSFERRED INTO A GOVERNED FOLLOW-ON LIFECYCLE.

# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-ACCEPTANCE-MANDATORY-RELIANCE-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-01

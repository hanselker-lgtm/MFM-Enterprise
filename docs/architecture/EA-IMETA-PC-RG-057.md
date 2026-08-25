# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-01

## Physical File ID
`EA-IMETA-PC-RG-057`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-057` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Monitoring Alerting |
| Parent | EA-IMETA-PC-RG-056 — Mandatory Reliance Restoration Monitoring |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory monitoring-alerting layer defining when monitored deviations must become governed alerts, how alert conditions are classified and routed, and how alerting preserves the evidence and context needed for escalation and control.

## Core Principle
Monitoring observes; alerting communicates a material condition requiring attention, investigation or action. A monitored deviation becomes an alert when governed criteria indicate that passive observation is no longer sufficient.

```text
MONITORING SIGNAL
      ↓
VALIDATE + CORRELATE
      ↓
DEVIATION?
├── NO → CONTINUE MONITORING
└── YES
     ↓
MATERIAL ALERT CRITERIA?
├── NO → RECORD / TREND / INVESTIGATE
└── YES
     ↓
CLASSIFY + ROUTE + ACKNOWLEDGE
     ↓
ACTION / ESCALATION
```

## Alerting Quality Test
```text
VALID SIGNAL
+
MATERIALITY CRITERION
+
CURRENT BASELINE
+
CLASSIFICATION
+
AUTHORIZED ROUTE
+
CONTEXT
+
RESPONSE EXPECTATION
+
TRACEABLE DELIVERY
=
VALID GOVERNED ALERT
```

## Alerting Status Model
```text
SIGNAL
CANDIDATE ALERT
VALIDATED
TRIGGERED
ROUTED
DELIVERED
ACKNOWLEDGED
IN ACTION
ESCALATED
RESOLVED
FAILED
```

## Alerting Invariants

```text
ALERTS SHALL BE GENERATED FROM GOVERNED MONITORING CRITERIA
```

```text
MATERIALITY SHALL DETERMINE WHEN OBSERVATION BECOMES ALERTING
```

```text
ALERT CONTEXT SHALL BE SUFFICIENT FOR THE RECEIVER TO UNDERSTAND THE CONDITION
```

```text
ALERT CLASSIFICATION SHALL BE TRACEABLE AND CONSISTENT
```

```text
ALERT ROUTING SHALL TARGET AUTHORIZED RECIPIENTS
```

```text
DELIVERY AND ACKNOWLEDGEMENT SHALL BE OBSERVABLE WHERE MATERIAL
```

```text
FAILED ALERT DELIVERY SHALL HAVE A FALLBACK OR ESCALATION PATH
```

```text
ALERT SUPPRESSION SHALL BE AUTHORIZED, VISIBLE, TIME-BOUNDED AND REVIEWABLE
```

```text
ALERTING SHALL NOT HIDE OR DELETE THE UNDERLYING MONITORING EVIDENCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE ALERTING SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT ALERTING SHALL SUPPORT HUMAN OR GOVERNANCE INTERVENTION WHERE REQUIRED
```

```text
ALERTING SHALL FEED ESCALATION WHEN THE CURRENT RESPONSE LEVEL IS INSUFFICIENT
```

```text
ALERT FATIGUE SHALL BE MANAGED THROUGH SIGNAL QUALITY, CORRELATION AND PRIORITIZATION
```

```text
ALERT THRESHOLDS SHALL NOT BE MANIPULATED TO HIDE REGRESSION
```

```text
REPEATED ALERT PATTERNS SHALL FEED GOVERNANCE AND REVALIDATION
```

## 1. Alerting Domain — Monitoring Alerting Governance

**Control family:** `PCRMA-001`

The Monitoring Alerting Governance domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-001-01` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-001-02` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-001-03` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-001-04` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-001-05` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-001-06` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-001-07` — Establish and maintain the monitoring alerting governance control.
- `PCRMA-001-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 2. Alerting Domain — Monitoring Alerting Objective

**Control family:** `PCRMA-002`

The Monitoring Alerting Objective domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-002-01` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-002-02` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-002-03` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-002-04` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-002-05` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-002-06` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-002-07` — Establish and maintain the monitoring alerting objective control.
- `PCRMA-002-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 3. Alerting Domain — Monitoring Alerting Definition

**Control family:** `PCRMA-003`

The Monitoring Alerting Definition domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-003-01` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-003-02` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-003-03` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-003-04` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-003-05` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-003-06` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-003-07` — Establish and maintain the monitoring alerting definition control.
- `PCRMA-003-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 4. Alerting Domain — Monitoring Alerting Scope

**Control family:** `PCRMA-004`

The Monitoring Alerting Scope domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-004-01` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-004-02` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-004-03` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-004-04` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-004-05` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-004-06` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-004-07` — Establish and maintain the monitoring alerting scope control.
- `PCRMA-004-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 5. Alerting Domain — Monitoring Alerting Authority

**Control family:** `PCRMA-005`

The Monitoring Alerting Authority domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-005-01` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-005-02` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-005-03` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-005-04` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-005-05` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-005-06` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-005-07` — Establish and maintain the monitoring alerting authority control.
- `PCRMA-005-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 6. Alerting Domain — Monitoring Alerting Criteria

**Control family:** `PCRMA-006`

The Monitoring Alerting Criteria domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-006-01` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-006-02` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-006-03` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-006-04` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-006-05` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-006-06` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-006-07` — Establish and maintain the monitoring alerting criteria control.
- `PCRMA-006-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 7. Alerting Domain — Monitoring Alerting Preconditions

**Control family:** `PCRMA-007`

The Monitoring Alerting Preconditions domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-007-01` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-007-02` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-007-03` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-007-04` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-007-05` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-007-06` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-007-07` — Establish and maintain the monitoring alerting preconditions control.
- `PCRMA-007-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 8. Alerting Domain — Monitoring Alerting Evidence

**Control family:** `PCRMA-008`

The Monitoring Alerting Evidence domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-008-01` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-008-02` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-008-03` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-008-04` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-008-05` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-008-06` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-008-07` — Establish and maintain the monitoring alerting evidence control.
- `PCRMA-008-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 9. Alerting Domain — Monitoring Alerting Method

**Control family:** `PCRMA-009`

The Monitoring Alerting Method domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-009-01` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-009-02` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-009-03` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-009-04` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-009-05` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-009-06` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-009-07` — Establish and maintain the monitoring alerting method control.
- `PCRMA-009-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 10. Alerting Domain — Monitoring Alerting Decision

**Control family:** `PCRMA-010`

The Monitoring Alerting Decision domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-010-01` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-010-02` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-010-03` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-010-04` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-010-05` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-010-06` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-010-07` — Establish and maintain the monitoring alerting decision control.
- `PCRMA-010-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 11. Alerting Domain — Monitoring Alerting Accountability

**Control family:** `PCRMA-011`

The Monitoring Alerting Accountability domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-011-01` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-011-02` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-011-03` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-011-04` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-011-05` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-011-06` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-011-07` — Establish and maintain the monitoring alerting accountability control.
- `PCRMA-011-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 12. Alerting Domain — Monitoring Alerting Timing

**Control family:** `PCRMA-012`

The Monitoring Alerting Timing domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-012-01` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-012-02` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-012-03` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-012-04` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-012-05` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-012-06` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-012-07` — Establish and maintain the monitoring alerting timing control.
- `PCRMA-012-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 13. Alerting Domain — Security Monitoring Alerting

**Control family:** `PCRMA-013`

The Security Monitoring Alerting domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-013-01` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-013-02` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-013-03` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-013-04` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-013-05` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-013-06` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-013-07` — Establish and maintain the security monitoring alerting control.
- `PCRMA-013-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 14. Alerting Domain — Resilience Monitoring Alerting

**Control family:** `PCRMA-014`

The Resilience Monitoring Alerting domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-014-01` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-014-02` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-014-03` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-014-04` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-014-05` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-014-06` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-014-07` — Establish and maintain the resilience monitoring alerting control.
- `PCRMA-014-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 15. Alerting Domain — Compliance Monitoring Alerting

**Control family:** `PCRMA-015`

The Compliance Monitoring Alerting domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-015-01` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-015-02` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-015-03` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-015-04` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-015-05` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-015-06` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-015-07` — Establish and maintain the compliance monitoring alerting control.
- `PCRMA-015-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 16. Alerting Domain — Data Monitoring Alerting

**Control family:** `PCRMA-016`

The Data Monitoring Alerting domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-016-01` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-016-02` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-016-03` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-016-04` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-016-05` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-016-06` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-016-07` — Establish and maintain the data monitoring alerting control.
- `PCRMA-016-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 17. Alerting Domain — AI and Agent Monitoring Alerting

**Control family:** `PCRMA-017`

The AI and Agent Monitoring Alerting domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-017-01` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-017-02` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-017-03` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-017-04` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-017-05` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-017-06` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-017-07` — Establish and maintain the ai and agent monitoring alerting control.
- `PCRMA-017-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 18. Alerting Domain — Monitoring Alerting Failure

**Control family:** `PCRMA-018`

The Monitoring Alerting Failure domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-018-01` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-018-02` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-018-03` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-018-04` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-018-05` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-018-06` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-018-07` — Establish and maintain the monitoring alerting failure control.
- `PCRMA-018-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 19. Alerting Domain — Monitoring Alerting Independence

**Control family:** `PCRMA-019`

The Monitoring Alerting Independence domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-019-01` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-019-02` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-019-03` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-019-04` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-019-05` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-019-06` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-019-07` — Establish and maintain the monitoring alerting independence control.
- `PCRMA-019-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## 20. Alerting Domain — Monitoring Alerting Review and Learning

**Control family:** `PCRMA-020`

The Monitoring Alerting Review and Learning domain establishes governed mandatory alerting requirements.

### Required controls
- `PCRMA-020-01` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-01-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-020-02` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-02-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-020-03` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-03-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-020-04` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-04-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-020-05` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-05-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-020-06` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-06-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.
- `PCRMA-020-07` — Establish and maintain the monitoring alerting review and learning control.
- `PCRMA-020-07-E` — Preserve signal, threshold, classification, context, route, delivery, acknowledgement and follow-on traceability.

```text
MONITOR → ALERT → ESCALATE
```

## Monitoring Alerting Structure

| Element | Required definition |
|---|---|
| Signal | Observable monitoring condition |
| Baseline | Current expected state |
| Trigger | Governed alert condition |
| Classification | Materiality / priority |
| Context | What, why, where, when, impact |
| Route | Authorized recipient |
| Delivery | Communication status |
| Follow-on | Action / escalation |

## Monitoring Alerting Objective

Ensure material monitoring deviations are communicated in time and with sufficient context to support appropriate investigation, control or escalation.

## Monitoring Alerting Definition

Alerting is the governed transformation of a qualifying monitoring condition into an actionable communication with defined materiality, context, route and response expectation.

## Monitoring Alerting Scope

Scope shall cover material deviations from the restored baseline, acceptance conditions, control boundaries, dependencies and defined outcomes.

## Monitoring Alerting Authority

Authority shall define who may establish alert criteria, classify severity, change routes, suppress alerts and initiate mandatory escalation.

## Monitoring Alerting Criteria

Criteria shall distinguish normal observations, warning signals, material alerts and critical alerts.

```text
SIGNAL
↓
VALID?
├── NO → INVESTIGATE
└── YES
     ↓
ALERT CRITERION MET?
├── NO → RECORD / TREND
└── YES
     ↓
CLASSIFY
├── WARNING → INVESTIGATE
├── MATERIAL → ACTION / ESCALATE
└── CRITICAL → PROTECT / RESTRICT / SUSPEND
```

## Monitoring Alerting Preconditions

Preconditions include valid monitoring signals, current baseline, defined criteria, classification model, routes, recipients and response expectations.

## Monitoring Alerting Evidence

Evidence shall preserve source signal, baseline, threshold, classification, context, timestamp, route, delivery and acknowledgement where applicable.

## Monitoring Alerting Method

Methods may include automated alerting, correlated event alerts, threshold alerts, anomaly alerts, rule-based alerts and human-triggered alerts.

```text
SIGNAL
↓
VALIDATE
↓
CORRELATE
↓
CLASSIFY
↓
ROUTE
↓
ACKNOWLEDGE
```

## Monitoring Alerting Decision

Alerting decisions shall distinguish record-only, warning, material, critical and failed-delivery outcomes.

```text
NORMAL → RECORD
WARNING → INVESTIGATE
MATERIAL → ALERT / ESCALATE
CRITICAL → PROTECT / RESTRICT
FAILED DELIVERY → FALLBACK / ESCALATE
```

## Monitoring Alerting Accountability

Accountability shall remain explicit for alert criteria, classification, routing, suppression, delivery assurance and escalation initiation.

## Monitoring Alerting Timing

Alert timing shall reflect time-to-impact, materiality and required response window. Critical conditions shall not be delayed by nonessential processing.

## Security Monitoring Alerting

Alert on material access violations, exposure, threat indicators, security-control failures and boundary breaches.

## Resilience Monitoring Alerting

Alert on material availability, capacity, recovery, continuity and dependency degradation.

## Compliance Monitoring Alerting

Alert on material obligation, control, reporting and policy deviations requiring attention or action.

## Data Monitoring Alerting

Alert on material integrity, quality, access, lineage, retention or authorized-use deviations.

## AI and Agent Monitoring Alerting

Alert on material deviations in AI/agent authority, policy adherence, tool use, data boundaries, autonomy, behaviour or outputs.

```text
AI / AGENT SIGNAL
↓
MATERIAL DEVIATION?
├── NO → MONITOR
└── YES → ALERT
             ↓
       HUMAN / GOVERNANCE ROUTE
             ↓
       LIMIT / ESCALATE / SUSPEND
```

## Monitoring Alerting Failure

Failure includes lost signals, failed routing, missing context, delayed delivery, no acknowledgement or incorrect recipient.

```text
ALERT FAILURE
↓
CAN CONDITION STILL BE COMMUNICATED?
├── YES → FALLBACK ROUTE
└── NO → PROTECT / RESTRICT / ESCALATE
```

## Monitoring Alerting Independence

Where materiality requires it, alert criteria, suppression decisions or alert effectiveness shall receive independent review.

## Monitoring Alerting Review and Learning

Reviews shall identify false negatives, false positives, alert fatigue, routing failures, suppression problems and opportunities to improve signal-to-action quality.

## Alert Determination Model
```text
MONITORING SIGNAL
↓
SIGNAL VALID?
├── NO → INVESTIGATE / RECORD
└── YES
     ↓
DEVIATION MATERIAL?
├── NO → TREND / RECORD
└── YES
     ↓
CLASSIFY
├── WARNING → INVESTIGATE
├── MATERIAL → ALERT / ESCALATE
└── CRITICAL → PROTECT / RESTRICT / SUSPEND
```

## Alert Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Record | Non-material observation | Trend / monitor |
| Warning | Developing condition | Investigate |
| Material | Action required | Alert / escalate |
| Critical | Immediate material concern | Protect / restrict / suspend |
| Failed | Alert communication not established | Fallback / escalate |

## Alert Record
| Field | Required |
|---|---|
| Alert ID | Yes |
| Monitoring ID | Yes |
| Baseline Version | Yes |
| Trigger Version | Yes |
| Signal Source | Yes |
| Timestamp | Yes |
| Classification | Yes |
| Context | Yes |
| Route | Yes |
| Delivery | Where material |
| Acknowledgement | Where material |
| Follow-on | Yes |

## Alert Context Integrity
A material alert shall communicate enough information to support immediate understanding and appropriate action.

```text
ALERT CONTEXT
=
WHAT + WHY + WHERE + WHEN + IMPACT + EVIDENCE + RESPONSE WINDOW
```

## Alert Routing Resilience
Material alerts shall have a fallback route where primary delivery failure could create unacceptable delay.

```text
ALERT
↓
PRIMARY ROUTE
├── DELIVERED → ACKNOWLEDGE
└── FAILED
     ↓
FALLBACK ROUTE
     ↓
ACKNOWLEDGED?
├── YES → ACTION
└── NO → FURTHER ESCALATION
```

## Alert Suppression
Suppression shall be authorized, visible, justified, time-bounded and reviewable. The underlying monitoring signal shall remain preserved.

## Alert Fatigue
Alert volume shall be managed through correlation, prioritization, signal-quality improvement and threshold governance rather than concealment of material conditions.

## Alert Threshold Governance
Thresholds shall be versioned, justified and protected against unauthorized changes. Material thresholds shall have explicit ownership and approval.

## Delivery and Acknowledgement
For material alerts, delivery and acknowledgement status shall be observable. Failure to acknowledge within the required window shall initiate fallback or escalation.

## Alert Change Control
Changes to alert criteria, classification, routes, recipients, suppression, thresholds or response expectations shall be governed, approved, versioned and effective-dated.

```text
CURRENT ALERT MODEL
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

## Alerting Anti-Gaming Control
Alert criteria, thresholds and suppression shall not be weakened merely to reduce incident counts, avoid escalation or improve reported operational metrics.

Historical alerts, underlying monitoring signals, classifications, routing decisions, delivery status, acknowledgements, suppressions and follow-on actions shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory monitoring-alerting layer beneath monitoring and above escalation. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, reacceptance, reliance restoration, monitoring, escalation, resolution, closure, post-closure monitoring or regression detection layers.

## Governance-to-Alerting Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → MONITORING → MANDATORY ALERTING → ESCALATION → RESOLUTION
```

## Complete Alerting Chain
```text
RESTORE RELIANCE → MONITOR → DETECT DEVIATION → CLASSIFY → ALERT → ACKNOWLEDGE → ESCALATE IF REQUIRED → RESOLVE → VERIFY → REVALIDATE
```

## Next Document
`EA-IMETA-PC-RG-058` — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification Revalidation Reacceptance Reliance Restoration Monitoring Alerting Escalation

## Final Principle
EA-IMETA SHALL REQUIRE MATERIAL MONITORING DEVIATIONS TO BECOME GOVERNED ALERTS WHEN DEFINED CRITERIA ARE MET, WITH VALIDATED SIGNALS, CURRENT BASELINES, MATERIALITY CLASSIFICATION, SUFFICIENT CONTEXT, AUTHORIZED ROUTING, DELIVERY AND ACKNOWLEDGEMENT CONTROLS, FALLBACK PATHS AND TRACEABLE FOLLOW-ON ACTION SO THAT MATERIAL CONDITIONS CANNOT REMAIN MERELY OBSERVED WHEN ACTION IS REQUIRED.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-01

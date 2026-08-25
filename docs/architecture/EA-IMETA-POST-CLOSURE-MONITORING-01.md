# EA-IMETA-PRODUCTION-SERVICE-SECURITY-RESILIENCE-COMPLIANCE-CAPABILITY-TRANSFORMATION-PORTFOLIO-OPERATING-MODEL-CONTROL-ASSURANCE-TEST-RESULT-FINDING-REMEDIATION-VALIDATION-ACCEPTANCE-CLOSURE-MONITORING-REGRESSION-REOPENING-REMEDIATION-VALIDATION-REACCEPTANCE-CLOSURE-POST-CLOSURE-MONITORING-01

## Short File ID
`EA-IMETA-POST-CLOSURE-MONITORING-01`

### Version 1.0
### Status: PRODUCTION POST-CLOSURE MONITORING BASELINE
### Governing Architecture: EA-IMETA-MASTER-01

## Purpose
Establish the authoritative post-closure monitoring architecture that continuously verifies the stability of a re-closed condition, detects regression or material change, activates governed response when thresholds are breached, and preserves the ability to reopen the lifecycle when justified.

## Core Principle
Re-closure does not terminate assurance. It changes the lifecycle from active remediation and acceptance into controlled post-closure monitoring.

```text
RE-CLOSED
 ↓
POST-CLOSURE MONITORING
 ↓
BASELINE
 ↓
METRICS / THRESHOLDS
 ↓
OBSERVE
 ↓
CORRELATE
 ↓
EARLY WARNING / REGRESSION
 ↓
ASSESS
 ↓
NO MATERIAL CHANGE → REMAIN CLOSED
REGRESSION / MATERIAL CHANGE → REOPENING ASSESSMENT
```

## Monitoring Quality Test
```text
KNOWN BASELINE
+
MEASURABLE SIGNAL
+
DEFINED THRESHOLD
+
OWNED RESPONSE
+
TRACEABLE EVIDENCE
+
REOPENING PATH
=
GOVERNED POST-CLOSURE MONITORING
```

## Monitoring Status Model
```text
NOT ACTIVE
INITIALIZING
ACTIVE
DEGRADED
WARNING
BREACH
UNDER ASSESSMENT
REGRESSION SUSPECTED
REGRESSION CONFIRMED
REOPENING RECOMMENDED
REOPENED
CLOSED / STABLE
```

## Monitoring Invariants

```text
RE-CLOSURE ≠ END OF ASSURANCE
```

```text
NO BASELINE → NO RELIABLE REGRESSION DETECTION
```

```text
NO THRESHOLD → NO GOVERNED ALERT
```

```text
NO OWNER → NO GOVERNED RESPONSE
```

```text
WARNING ≠ CONFIRMED REGRESSION
```

```text
CONFIRMED REGRESSION → REOPENING ASSESSMENT
```

```text
MONITORING EVIDENCE SHALL REMAIN TRACEABLE
```

```text
POST-CLOSURE MONITORING SHALL NOT ALTER HISTORICAL CLOSURE RECORDS
```

```text
AI DETECTION ≠ AUTOMATIC REOPENING AUTHORITY
```

```text
AGENT RESPONSE SHALL REMAIN WITHIN DEFINED AUTHORITY
```

```text
MATERIAL CHANGE SHALL TRIGGER GOVERNED ASSESSMENT
```

```text
MONITORING BASELINES SHALL BE UPDATED ONLY THROUGH GOVERNED CHANGE
```

## 1. Monitoring Domain — Post-Closure Monitoring Governance

**Control family:** `PCM-001`

The Post-Closure Monitoring Governance domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-001-01` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-001-02` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-001-03` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-001-04` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-001-05` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-001-06` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-001-07` — Establish and operate the post-closure monitoring governance control.
- `PCM-001-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 2. Monitoring Domain — Monitoring Scope

**Control family:** `PCM-002`

The Monitoring Scope domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-002-01` — Establish and operate the monitoring scope control.
- `PCM-002-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-002-02` — Establish and operate the monitoring scope control.
- `PCM-002-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-002-03` — Establish and operate the monitoring scope control.
- `PCM-002-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-002-04` — Establish and operate the monitoring scope control.
- `PCM-002-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-002-05` — Establish and operate the monitoring scope control.
- `PCM-002-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-002-06` — Establish and operate the monitoring scope control.
- `PCM-002-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-002-07` — Establish and operate the monitoring scope control.
- `PCM-002-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 3. Monitoring Domain — Monitoring Baseline

**Control family:** `PCM-003`

The Monitoring Baseline domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-003-01` — Establish and operate the monitoring baseline control.
- `PCM-003-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-003-02` — Establish and operate the monitoring baseline control.
- `PCM-003-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-003-03` — Establish and operate the monitoring baseline control.
- `PCM-003-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-003-04` — Establish and operate the monitoring baseline control.
- `PCM-003-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-003-05` — Establish and operate the monitoring baseline control.
- `PCM-003-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-003-06` — Establish and operate the monitoring baseline control.
- `PCM-003-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-003-07` — Establish and operate the monitoring baseline control.
- `PCM-003-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 4. Monitoring Domain — Monitoring Metrics

**Control family:** `PCM-004`

The Monitoring Metrics domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-004-01` — Establish and operate the monitoring metrics control.
- `PCM-004-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-004-02` — Establish and operate the monitoring metrics control.
- `PCM-004-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-004-03` — Establish and operate the monitoring metrics control.
- `PCM-004-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-004-04` — Establish and operate the monitoring metrics control.
- `PCM-004-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-004-05` — Establish and operate the monitoring metrics control.
- `PCM-004-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-004-06` — Establish and operate the monitoring metrics control.
- `PCM-004-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-004-07` — Establish and operate the monitoring metrics control.
- `PCM-004-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 5. Monitoring Domain — Monitoring Thresholds

**Control family:** `PCM-005`

The Monitoring Thresholds domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-005-01` — Establish and operate the monitoring thresholds control.
- `PCM-005-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-005-02` — Establish and operate the monitoring thresholds control.
- `PCM-005-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-005-03` — Establish and operate the monitoring thresholds control.
- `PCM-005-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-005-04` — Establish and operate the monitoring thresholds control.
- `PCM-005-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-005-05` — Establish and operate the monitoring thresholds control.
- `PCM-005-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-005-06` — Establish and operate the monitoring thresholds control.
- `PCM-005-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-005-07` — Establish and operate the monitoring thresholds control.
- `PCM-005-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 6. Monitoring Domain — Early Warning

**Control family:** `PCM-006`

The Early Warning domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-006-01` — Establish and operate the early warning control.
- `PCM-006-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-006-02` — Establish and operate the early warning control.
- `PCM-006-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-006-03` — Establish and operate the early warning control.
- `PCM-006-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-006-04` — Establish and operate the early warning control.
- `PCM-006-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-006-05` — Establish and operate the early warning control.
- `PCM-006-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-006-06` — Establish and operate the early warning control.
- `PCM-006-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-006-07` — Establish and operate the early warning control.
- `PCM-006-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 7. Monitoring Domain — Regression Detection

**Control family:** `PCM-007`

The Regression Detection domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-007-01` — Establish and operate the regression detection control.
- `PCM-007-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-007-02` — Establish and operate the regression detection control.
- `PCM-007-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-007-03` — Establish and operate the regression detection control.
- `PCM-007-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-007-04` — Establish and operate the regression detection control.
- `PCM-007-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-007-05` — Establish and operate the regression detection control.
- `PCM-007-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-007-06` — Establish and operate the regression detection control.
- `PCM-007-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-007-07` — Establish and operate the regression detection control.
- `PCM-007-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 8. Monitoring Domain — Control Health

**Control family:** `PCM-008`

The Control Health domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-008-01` — Establish and operate the control health control.
- `PCM-008-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-008-02` — Establish and operate the control health control.
- `PCM-008-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-008-03` — Establish and operate the control health control.
- `PCM-008-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-008-04` — Establish and operate the control health control.
- `PCM-008-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-008-05` — Establish and operate the control health control.
- `PCM-008-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-008-06` — Establish and operate the control health control.
- `PCM-008-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-008-07` — Establish and operate the control health control.
- `PCM-008-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 9. Monitoring Domain — Security Monitoring

**Control family:** `PCM-009`

The Security Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-009-01` — Establish and operate the security monitoring control.
- `PCM-009-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-009-02` — Establish and operate the security monitoring control.
- `PCM-009-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-009-03` — Establish and operate the security monitoring control.
- `PCM-009-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-009-04` — Establish and operate the security monitoring control.
- `PCM-009-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-009-05` — Establish and operate the security monitoring control.
- `PCM-009-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-009-06` — Establish and operate the security monitoring control.
- `PCM-009-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-009-07` — Establish and operate the security monitoring control.
- `PCM-009-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 10. Monitoring Domain — Resilience Monitoring

**Control family:** `PCM-010`

The Resilience Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-010-01` — Establish and operate the resilience monitoring control.
- `PCM-010-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-010-02` — Establish and operate the resilience monitoring control.
- `PCM-010-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-010-03` — Establish and operate the resilience monitoring control.
- `PCM-010-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-010-04` — Establish and operate the resilience monitoring control.
- `PCM-010-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-010-05` — Establish and operate the resilience monitoring control.
- `PCM-010-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-010-06` — Establish and operate the resilience monitoring control.
- `PCM-010-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-010-07` — Establish and operate the resilience monitoring control.
- `PCM-010-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 11. Monitoring Domain — Data Monitoring

**Control family:** `PCM-011`

The Data Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-011-01` — Establish and operate the data monitoring control.
- `PCM-011-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-011-02` — Establish and operate the data monitoring control.
- `PCM-011-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-011-03` — Establish and operate the data monitoring control.
- `PCM-011-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-011-04` — Establish and operate the data monitoring control.
- `PCM-011-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-011-05` — Establish and operate the data monitoring control.
- `PCM-011-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-011-06` — Establish and operate the data monitoring control.
- `PCM-011-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-011-07` — Establish and operate the data monitoring control.
- `PCM-011-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 12. Monitoring Domain — AI and Agent Monitoring

**Control family:** `PCM-012`

The AI and Agent Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-012-01` — Establish and operate the ai and agent monitoring control.
- `PCM-012-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-012-02` — Establish and operate the ai and agent monitoring control.
- `PCM-012-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-012-03` — Establish and operate the ai and agent monitoring control.
- `PCM-012-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-012-04` — Establish and operate the ai and agent monitoring control.
- `PCM-012-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-012-05` — Establish and operate the ai and agent monitoring control.
- `PCM-012-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-012-06` — Establish and operate the ai and agent monitoring control.
- `PCM-012-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-012-07` — Establish and operate the ai and agent monitoring control.
- `PCM-012-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 13. Monitoring Domain — Compliance and Audit Monitoring

**Control family:** `PCM-013`

The Compliance and Audit Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-013-01` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-013-02` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-013-03` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-013-04` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-013-05` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-013-06` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-013-07` — Establish and operate the compliance and audit monitoring control.
- `PCM-013-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 14. Monitoring Domain — Financial and Benefit Monitoring

**Control family:** `PCM-014`

The Financial and Benefit Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-014-01` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-014-02` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-014-03` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-014-04` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-014-05` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-014-06` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-014-07` — Establish and operate the financial and benefit monitoring control.
- `PCM-014-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 15. Monitoring Domain — Architecture and Transformation Monitoring

**Control family:** `PCM-015`

The Architecture and Transformation Monitoring domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-015-01` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-015-02` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-015-03` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-015-04` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-015-05` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-015-06` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-015-07` — Establish and operate the architecture and transformation monitoring control.
- `PCM-015-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 16. Monitoring Domain — Event Correlation

**Control family:** `PCM-016`

The Event Correlation domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-016-01` — Establish and operate the event correlation control.
- `PCM-016-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-016-02` — Establish and operate the event correlation control.
- `PCM-016-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-016-03` — Establish and operate the event correlation control.
- `PCM-016-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-016-04` — Establish and operate the event correlation control.
- `PCM-016-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-016-05` — Establish and operate the event correlation control.
- `PCM-016-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-016-06` — Establish and operate the event correlation control.
- `PCM-016-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-016-07` — Establish and operate the event correlation control.
- `PCM-016-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 17. Monitoring Domain — Alert Management

**Control family:** `PCM-017`

The Alert Management domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-017-01` — Establish and operate the alert management control.
- `PCM-017-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-017-02` — Establish and operate the alert management control.
- `PCM-017-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-017-03` — Establish and operate the alert management control.
- `PCM-017-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-017-04` — Establish and operate the alert management control.
- `PCM-017-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-017-05` — Establish and operate the alert management control.
- `PCM-017-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-017-06` — Establish and operate the alert management control.
- `PCM-017-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-017-07` — Establish and operate the alert management control.
- `PCM-017-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 18. Monitoring Domain — Monitoring Response

**Control family:** `PCM-018`

The Monitoring Response domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-018-01` — Establish and operate the monitoring response control.
- `PCM-018-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-018-02` — Establish and operate the monitoring response control.
- `PCM-018-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-018-03` — Establish and operate the monitoring response control.
- `PCM-018-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-018-04` — Establish and operate the monitoring response control.
- `PCM-018-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-018-05` — Establish and operate the monitoring response control.
- `PCM-018-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-018-06` — Establish and operate the monitoring response control.
- `PCM-018-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-018-07` — Establish and operate the monitoring response control.
- `PCM-018-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 19. Monitoring Domain — Reopening Assessment

**Control family:** `PCM-019`

The Reopening Assessment domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-019-01` — Establish and operate the reopening assessment control.
- `PCM-019-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-019-02` — Establish and operate the reopening assessment control.
- `PCM-019-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-019-03` — Establish and operate the reopening assessment control.
- `PCM-019-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-019-04` — Establish and operate the reopening assessment control.
- `PCM-019-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-019-05` — Establish and operate the reopening assessment control.
- `PCM-019-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-019-06` — Establish and operate the reopening assessment control.
- `PCM-019-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-019-07` — Establish and operate the reopening assessment control.
- `PCM-019-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## 20. Monitoring Domain — Continuous Improvement

**Control family:** `PCM-020`

The Continuous Improvement domain establishes controlled post-closure monitoring coverage.

### Required controls
- `PCM-020-01` — Establish and operate the continuous improvement control.
- `PCM-020-01-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-020-02` — Establish and operate the continuous improvement control.
- `PCM-020-02-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-020-03` — Establish and operate the continuous improvement control.
- `PCM-020-03-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-020-04` — Establish and operate the continuous improvement control.
- `PCM-020-04-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-020-05` — Establish and operate the continuous improvement control.
- `PCM-020-05-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-020-06` — Establish and operate the continuous improvement control.
- `PCM-020-06-E` — Preserve monitoring evidence, ownership and disposition traceability.
- `PCM-020-07` — Establish and operate the continuous improvement control.
- `PCM-020-07-E` — Preserve monitoring evidence, ownership and disposition traceability.

```text
BASELINE → SIGNAL → THRESHOLD → ASSESSMENT → RESPONSE
```

## Post-Closure Monitoring Decision Matrix
| Dimension | States |
|---|---|
| Monitoring | Not Active / Initializing / Active / Degraded |
| Signal | Normal / Warning / Breach / Unknown |
| Regression | None / Suspected / Confirmed |
| Material Change | No / Possible / Confirmed |
| Response | Observe / Assess / Contain / Reopen |
| Closure State | Closed / Under Assessment / Reopened |

## Monitoring Record Model
| Record | Minimum information |
|---|---|
| Monitoring Record | ID, closure, baseline, metric, threshold, owner, status |
| Metric Record | metric, source, frequency, value, timestamp, quality |
| Threshold Record | threshold, rationale, severity, owner, escalation |
| Alert Record | signal, threshold, timestamp, severity, disposition |
| Regression Assessment | condition, evidence, comparison, conclusion |
| Reopening Assessment | trigger, finding linkage, risk, recommendation, authority |
| Monitoring Change | baseline, threshold, metric, approval, effective date |

## Normal Post-Closure Operating Cycle
```text
RE-CLOSED
 ↓
ACTIVATE MONITORING
 ↓
OBSERVE
 ↓
MEASURE
 ↓
COMPARE TO BASELINE
 ↓
EVALUATE THRESHOLDS
 ↓
NO MATERIAL CHANGE → CONTINUE MONITORING
MATERIAL CHANGE → ASSESS
 ↓
REGRESSION CONFIRMED → REOPENING
```

## Early Warning Model
```text
NORMAL
 ↓
DEVIATION
 ↓
WARNING
 ↓
BREACH
 ↓
ASSESSMENT
 ↓
REGRESSION?
 ├─ NO → CONTROLLED RETURN TO MONITORING
 └─ YES → REOPENING ASSESSMENT
```

## Monitoring and Reopening Boundary
Post-closure monitoring shall not reopen a finding merely because a signal is unusual. A governed assessment shall establish whether the deviation represents regression, a new risk, an expected variation, a baseline change or an unrelated condition.

## AI and Agent Monitoring
AI may correlate signals, detect anomalies, prioritize alerts and recommend assessment. Agent actions shall remain constrained by identity, authority, tool scope, data access, action limits, approval requirements and stop conditions.

```text
AI DETECTION
 ↓
HUMAN / GOVERNED ASSESSMENT
 ↓
REOPENING DECISION
```

## Complete Adaptive Assurance Loop
```text
CONTROL → ASSURANCE → TEST → RESULT → FINDING → REMEDIATION → VALIDATION → ACCEPTANCE → CLOSURE → MONITORING → REGRESSION → REOPENING → REMEDIATION → RE-VALIDATION → RE-ACCEPTANCE → RE-CLOSURE → POST-CLOSURE MONITORING
```

## Historical Integrity
Monitoring events shall be linked to the re-closure record but shall not overwrite the historical remediation, validation, acceptance or closure records.

## Next Document
`EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-01`

## Final Principle
EA-IMETA SHALL MAINTAIN GOVERNED POST-CLOSURE MONITORING AFTER RE-CLOSURE, USING CURRENT BASELINES, MEASURABLE SIGNALS, DEFINED THRESHOLDS AND CONTROLLED REGRESSION ASSESSMENT TO ENSURE THAT VALID REGRESSION CAN REOPEN THE ASSURANCE LIFECYCLE.

# END OF EA-IMETA-PRODUCTION-SERVICE-SECURITY-RESILIENCE-COMPLIANCE-CAPABILITY-TRANSFORMATION-PORTFOLIO-OPERATING-MODEL-CONTROL-ASSURANCE-TEST-RESULT-FINDING-REMEDIATION-VALIDATION-ACCEPTANCE-CLOSURE-MONITORING-REGRESSION-REOPENING-REMEDIATION-VALIDATION-REACCEPTANCE-CLOSURE-POST-CLOSURE-MONITORING-01

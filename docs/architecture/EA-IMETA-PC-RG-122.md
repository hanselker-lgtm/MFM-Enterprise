# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-ACTIVATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-122`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-122` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-ACTIVATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Monitoring Activation Determination |
| Parent | EA-IMETA-PC-RG-121 — Mandatory Post-Closure Regression Response Closure Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory post-closure monitoring activation layer that ensures every closed regression case requiring continued observation enters an explicit, owned, measurable and time-bound monitoring state before active response governance is considered complete.

## Core Principle
Closure ends the active response case; it does not necessarily end control. Where residual risk, sustainability, recurrence potential, mandatory assurance or other conditions require continued observation, post-closure monitoring shall be explicitly activated, owned, configured, verified and traceable.

```text
CASE CLOSED
        ↓
POST-CLOSURE MONITORING REQUIRED?
├── NO → CONTROLLED CLOSED STATE
└── YES
     ↓
DEFINE MONITORING OBJECTIVE
     ↓
DEFINE SIGNALS / METRICS / THRESHOLDS
     ↓
ASSIGN OWNER + AUTHORITY
     ↓
CONFIGURE FREQUENCY + DURATION
     ↓
ESTABLISH ESCALATION + REOPENING PATH
     ↓
ACTIVATE MONITORING
     ↓
VERIFY MONITORING IS OPERATING
     ↓
ENTER POST-CLOSURE MONITORING STATE
```

## Activation Quality Test
```text
VALID CLOSURE
+
MONITORING REQUIREMENT
+
DEFINED OBJECTIVE
+
VALID SIGNALS / METRICS
+
THRESHOLDS
+
OWNER + AUTHORITY
+
FREQUENCY + DURATION
+
ESCALATION / REOPENING
+
WORKING MONITORING MECHANISM
+
TRACEABLE ACTIVATION EVIDENCE
=
VALID GOVERNED POST-CLOSURE MONITORING ACTIVATION
```

## Closure vs Monitoring Activation vs Monitoring Execution
```text
CLOSURE
→ ACTIVE RESPONSE CASE FORMALLY ENDS

MONITORING ACTIVATION
→ POST-CLOSURE OBSERVATION CONTROL IS ESTABLISHED AND STARTED

MONITORING EXECUTION
→ OBSERVATIONS / MEASUREMENTS ARE BEING PERFORMED

REGRESSION DETECTION
→ MONITORING IDENTIFIES A GOVERNED DEVIATION / REGRESSION CONDITION
```

## Activation States
```text
M0 — MONITORING NOT REQUIRED
M1 — MONITORING REQUIRED / PENDING CONFIGURATION
M2 — CONFIGURATION IN PROGRESS
M3 — READY FOR ACTIVATION
M4 — ACTIVATION AUTHORIZED
M5 — MONITORING ACTIVE
M6 — ACTIVATION VERIFIED
MX — UNKNOWN / INVALID ACTIVATION
MF — ACTIVATION FAILED
MR — MONITORING SUSPENDED / REQUIRES REACTIVATION
```

## Activation Dimensions
| Dimension | Required determination |
|---|---|
| Objective | What monitoring must establish |
| Scope | What remains under observation |
| Signals | Observable indicators |
| Metrics | Measurement definitions |
| Thresholds | Trigger boundaries |
| Owner | Monitoring responsibility |
| Authority | Decision / escalation authority |
| Frequency | Observation cadence |
| Duration | Required monitoring period |
| Evidence | Monitoring records |
| Escalation | Triggered response path |
| Reopening | Conditions for reactivation |

## Activation Invariants

```text
POST-CLOSURE MONITORING SHALL BE EXPLICITLY DETERMINED WHERE REQUIRED
```

```text
MONITORING ACTIVATION SHALL OCCUR BEFORE THE REQUIRED POST-CLOSURE OBSERVATION WINDOW BEGINS
```

```text
MONITORING SHALL HAVE A DEFINED OBJECTIVE
```

```text
MONITORING SIGNALS AND METRICS SHALL BE SUFFICIENT FOR THE INTENDED OBJECTIVE
```

```text
THRESHOLDS SHALL BE EXPLICIT WHERE TRIGGERED ACTION IS REQUIRED
```

```text
MONITORING SHALL HAVE AN IDENTIFIABLE OWNER AND AUTHORITY
```

```text
FREQUENCY AND DURATION SHALL MATCH CONSEQUENCE AND REGRESSION RISK
```

```text
ESCALATION AND REOPENING PATHS SHALL BE DEFINED BEFORE ACTIVATION WHERE MATERIAL
```

```text
FAILED OR UNVERIFIED MONITORING SHALL NOT BE TREATED AS ACTIVE MONITORING
```

```text
MONITORING GAPS SHALL BE VISIBLE AND GOVERNED
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE MONITORING SHALL USE DOMAIN-APPROPRIATE CONTROLS
```

```text
AI AND AGENT MONITORING SHALL INCLUDE RELEVANT BEHAVIOR, AUTHORITY, TOOL, DATA AND OVERSIGHT SIGNALS
```

```text
MONITORING ACTIVATION SHALL PRESERVE TRACEABILITY TO THE CLOSED CASE AND RESOLUTION
```

```text
MONITORING SHALL NOT BE CONFIGURED TO EXCLUDE KNOWN RISK MERELY TO AVOID REOPENING
```

```text
POST-CLOSURE MONITORING SHALL HAVE A DEFINED END, REVIEW OR CONTINUATION CONDITION WHERE APPLICABLE
```

```text
ACTIVATION CONTROLS SHALL BE REVIEWED AFTER MISSED SIGNALS, GAPS OR FALSE REOPENING EVENTS
```

## 1. Activation Domain — Post-Closure Monitoring Activation Governance

**Control family:** `PCMA-001`

The Post-Closure Monitoring Activation Governance domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-001-01` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-001-02` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-001-03` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-001-04` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-001-05` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-001-06` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-001-07` — Establish and maintain the post-closure monitoring activation governance control.
- `PCMA-001-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 2. Activation Domain — Post-Closure Monitoring Activation Objective

**Control family:** `PCMA-002`

The Post-Closure Monitoring Activation Objective domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-002-01` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-002-02` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-002-03` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-002-04` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-002-05` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-002-06` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-002-07` — Establish and maintain the post-closure monitoring activation objective control.
- `PCMA-002-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 3. Activation Domain — Post-Closure Monitoring Activation Definition

**Control family:** `PCMA-003`

The Post-Closure Monitoring Activation Definition domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-003-01` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-003-02` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-003-03` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-003-04` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-003-05` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-003-06` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-003-07` — Establish and maintain the post-closure monitoring activation definition control.
- `PCMA-003-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 4. Activation Domain — Post-Closure Monitoring Activation Scope

**Control family:** `PCMA-004`

The Post-Closure Monitoring Activation Scope domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-004-01` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-004-02` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-004-03` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-004-04` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-004-05` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-004-06` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-004-07` — Establish and maintain the post-closure monitoring activation scope control.
- `PCMA-004-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 5. Activation Domain — Post-Closure Monitoring Activation Authority

**Control family:** `PCMA-005`

The Post-Closure Monitoring Activation Authority domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-005-01` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-005-02` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-005-03` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-005-04` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-005-05` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-005-06` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-005-07` — Establish and maintain the post-closure monitoring activation authority control.
- `PCMA-005-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 6. Activation Domain — Post-Closure Monitoring Activation Criteria

**Control family:** `PCMA-006`

The Post-Closure Monitoring Activation Criteria domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-006-01` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-006-02` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-006-03` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-006-04` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-006-05` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-006-06` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-006-07` — Establish and maintain the post-closure monitoring activation criteria control.
- `PCMA-006-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 7. Activation Domain — Post-Closure Monitoring Activation Preconditions

**Control family:** `PCMA-007`

The Post-Closure Monitoring Activation Preconditions domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-007-01` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-007-02` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-007-03` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-007-04` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-007-05` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-007-06` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-007-07` — Establish and maintain the post-closure monitoring activation preconditions control.
- `PCMA-007-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 8. Activation Domain — Post-Closure Monitoring Activation Evidence

**Control family:** `PCMA-008`

The Post-Closure Monitoring Activation Evidence domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-008-01` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-008-02` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-008-03` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-008-04` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-008-05` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-008-06` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-008-07` — Establish and maintain the post-closure monitoring activation evidence control.
- `PCMA-008-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 9. Activation Domain — Post-Closure Monitoring Activation Method

**Control family:** `PCMA-009`

The Post-Closure Monitoring Activation Method domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-009-01` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-009-02` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-009-03` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-009-04` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-009-05` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-009-06` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-009-07` — Establish and maintain the post-closure monitoring activation method control.
- `PCMA-009-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 10. Activation Domain — Post-Closure Monitoring Activation Decision

**Control family:** `PCMA-010`

The Post-Closure Monitoring Activation Decision domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-010-01` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-010-02` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-010-03` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-010-04` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-010-05` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-010-06` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-010-07` — Establish and maintain the post-closure monitoring activation decision control.
- `PCMA-010-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 11. Activation Domain — Post-Closure Monitoring Activation Accountability

**Control family:** `PCMA-011`

The Post-Closure Monitoring Activation Accountability domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-011-01` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-011-02` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-011-03` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-011-04` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-011-05` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-011-06` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-011-07` — Establish and maintain the post-closure monitoring activation accountability control.
- `PCMA-011-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 12. Activation Domain — Post-Closure Monitoring Activation Timing

**Control family:** `PCMA-012`

The Post-Closure Monitoring Activation Timing domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-012-01` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-012-02` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-012-03` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-012-04` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-012-05` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-012-06` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-012-07` — Establish and maintain the post-closure monitoring activation timing control.
- `PCMA-012-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 13. Activation Domain — Security Post-Closure Monitoring Activation

**Control family:** `PCMA-013`

The Security Post-Closure Monitoring Activation domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-013-01` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-013-02` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-013-03` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-013-04` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-013-05` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-013-06` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-013-07` — Establish and maintain the security post-closure monitoring activation control.
- `PCMA-013-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 14. Activation Domain — Resilience Post-Closure Monitoring Activation

**Control family:** `PCMA-014`

The Resilience Post-Closure Monitoring Activation domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-014-01` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-014-02` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-014-03` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-014-04` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-014-05` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-014-06` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-014-07` — Establish and maintain the resilience post-closure monitoring activation control.
- `PCMA-014-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 15. Activation Domain — Compliance Post-Closure Monitoring Activation

**Control family:** `PCMA-015`

The Compliance Post-Closure Monitoring Activation domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-015-01` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-015-02` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-015-03` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-015-04` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-015-05` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-015-06` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-015-07` — Establish and maintain the compliance post-closure monitoring activation control.
- `PCMA-015-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 16. Activation Domain — Data Post-Closure Monitoring Activation

**Control family:** `PCMA-016`

The Data Post-Closure Monitoring Activation domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-016-01` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-016-02` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-016-03` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-016-04` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-016-05` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-016-06` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-016-07` — Establish and maintain the data post-closure monitoring activation control.
- `PCMA-016-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 17. Activation Domain — AI and Agent Post-Closure Monitoring Activation

**Control family:** `PCMA-017`

The AI and Agent Post-Closure Monitoring Activation domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-017-01` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-017-02` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-017-03` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-017-04` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-017-05` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-017-06` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-017-07` — Establish and maintain the ai and agent post-closure monitoring activation control.
- `PCMA-017-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 18. Activation Domain — Post-Closure Monitoring Activation Failure

**Control family:** `PCMA-018`

The Post-Closure Monitoring Activation Failure domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-018-01` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-018-02` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-018-03` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-018-04` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-018-05` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-018-06` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-018-07` — Establish and maintain the post-closure monitoring activation failure control.
- `PCMA-018-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 19. Activation Domain — Post-Closure Monitoring Activation Independence

**Control family:** `PCMA-019`

The Post-Closure Monitoring Activation Independence domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-019-01` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-019-02` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-019-03` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-019-04` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-019-05` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-019-06` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-019-07` — Establish and maintain the post-closure monitoring activation independence control.
- `PCMA-019-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## 20. Activation Domain — Post-Closure Monitoring Activation Review and Learning

**Control family:** `PCMA-020`

The Post-Closure Monitoring Activation Review and Learning domain establishes governed mandatory post-closure monitoring activation requirements.

### Required controls
- `PCMA-020-01` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-01-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-020-02` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-02-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-020-03` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-03-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-020-04` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-04-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-020-05` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-05-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-020-06` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-06-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.
- `PCMA-020-07` — Establish and maintain the post-closure monitoring activation review and learning control.
- `PCMA-020-07-E` — Preserve closure, objective, scope, signals, metrics, thresholds, owner, authority, frequency, duration, escalation and activation evidence.

```text
DEFINE → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → MONITOR
```

## Post-Closure Monitoring Activation Structure

| Element | Required definition |
|---|---|
| Objective | Monitoring purpose |
| Scope | Observed condition / controls |
| Signals | Indicators |
| Metrics | Measurement definitions |
| Thresholds | Trigger boundaries |
| Owner | Monitoring owner |
| Authority | Decision authority |
| Frequency | Observation cadence |
| Duration | Monitoring period |
| Escalation | Trigger path |
| Reopening | Reactivation conditions |

## Post-Closure Monitoring Activation Objective

Ensure required post-closure observation begins as an explicit controlled state with sufficient signals, thresholds, ownership and escalation to detect renewed regression before consequence becomes uncontrolled.

## Post-Closure Monitoring Activation Definition

Monitoring activation is the governed establishment and commencement of an approved post-closure observation control, including its objective, signals, metrics, thresholds, ownership, timing and escalation path.

## Post-Closure Monitoring Activation Scope

Scope includes residual risks, restored controls, key outcome conditions, known regression precursors, mandatory assurance conditions and other indicators requiring continued observation.

## Post-Closure Monitoring Activation Authority

Authority shall define who approves activation, changes monitoring parameters, accepts monitoring gaps, suspends monitoring and authorizes completion or continuation.

## Post-Closure Monitoring Activation Criteria

Criteria shall define when monitoring is required, what must be observed, acceptable thresholds, frequency, duration, owner, escalation and reopening.
```text
CLOSED CASE
↓
MONITOR REQUIRED?
├── NO → CONTROLLED CLOSED
└── YES
     ↓
OBJECTIVE
↓
SIGNALS / METRICS
↓
THRESHOLDS
↓
OWNER / AUTHORITY
↓
FREQUENCY / DURATION
↓
ESCALATION / REOPENING
↓
ACTIVATE
```

## Post-Closure Monitoring Activation Preconditions

Preconditions include valid closure, defined monitoring requirement, sufficient instrumentation or observation capability, owner, authority, thresholds and escalation path.

## Post-Closure Monitoring Activation Evidence

Evidence shall preserve closure reference, objective, scope, configuration, signals, metrics, thresholds, owner, authority, activation timestamp, verification and monitoring schedule.

## Post-Closure Monitoring Activation Method

Methods may include automated monitoring, scheduled human review, control testing, telemetry, sampling, audits, inspections and hybrid observation.
```text
CONFIGURE
↓
TEST SIGNALS
↓
AUTHORIZE
↓
ACTIVATE
↓
VERIFY
↓
OBSERVE
```

## Post-Closure Monitoring Activation Decision

Decision shall determine M0, M1, M2, M3, M4, M5, M6, MX, MF or MR and the associated action.

## Post-Closure Monitoring Activation Accountability

Accountability shall remain explicit for configuration quality, activation, monitoring continuity, threshold governance and escalation readiness.

## Post-Closure Monitoring Activation Timing

Activation shall occur before the required observation window and shall account for the time needed to detect recurrence before consequence becomes material.

## Security Post-Closure Monitoring Activation

Security monitoring shall include relevant exposure, access, control and attack-path indicators and shall connect material thresholds to the approved response path.

## Resilience Post-Closure Monitoring Activation

Resilience monitoring shall include relevant capacity, availability, redundancy, recovery and fallback indicators.

## Compliance Post-Closure Monitoring Activation

Compliance monitoring shall include continuing obligations, reporting conditions, control effectiveness and evidence requirements where applicable.

## Data Post-Closure Monitoring Activation

Data monitoring shall include relevant integrity, quality, lineage, availability, confidentiality and downstream reliance indicators.

## AI and Agent Post-Closure Monitoring Activation

AI/agent monitoring shall include relevant behavior, authority boundaries, tool use, data handling, autonomy and human-oversight signals.
```text
AI / AGENT CLOSED CASE
↓
BEHAVIOR SIGNALS
+
AUTHORITY SIGNALS
+
TOOL SIGNALS
+
DATA SIGNALS
+
OVERSIGHT SIGNALS
↓
MONITORING ACTIVE
```

## Post-Closure Monitoring Activation Failure

Failure includes missing monitoring configuration, broken signals, invalid thresholds, unavailable owner, failed activation, unverified monitoring or an observation gap.
```text
ACTIVATION FAILURE
↓
REGRESSION RISK MATERIAL?
├── YES → ESCALATE / REOPEN / ALTERNATE MONITORING
└── NO → CORRECT / VERIFY
```

## Post-Closure Monitoring Activation Independence

Independent validation may be required where monitoring is critical, contested, safety-significant or susceptible to configuration bias.

## Post-Closure Monitoring Activation Review and Learning

Reviews shall examine activation delays, blind spots, poor thresholds, monitoring gaps, false positives, false negatives and cases where monitoring failed to detect recurrence.

## Activation Determination Model
```text
CASE CLOSED
↓
MONITORING REQUIRED?
├── NO → CONTROLLED CLOSED STATE
└── YES
     ↓
DEFINE OBJECTIVE
     ↓
DEFINE SCOPE
     ↓
DEFINE SIGNALS / METRICS
     ↓
DEFINE THRESHOLDS
     ↓
ASSIGN OWNER + AUTHORITY
     ↓
SET FREQUENCY + DURATION
     ↓
ESTABLISH ESCALATION + REOPENING
     ↓
CONFIGURE
     ↓
TEST / VERIFY
     ↓
ACTIVATE
     ↓
MONITORING ACTIVE
```

## Activation Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| M0 | Monitoring not required | Controlled closed state |
| M1 | Required / pending configuration | Configure |
| M2 | Configuration in progress | Complete / test |
| M3 | Ready for activation | Obtain authorization |
| M4 | Activation authorized | Start |
| M5 | Monitoring active | Observe / measure |
| M6 | Activation verified | Continue governed monitoring |
| MX | Unknown / invalid | Treat as inactive |
| MF | Activation failed | Correct / escalate |
| MR | Suspended / reactivation required | Restore monitoring |

## Monitoring Activation Record
| Field | Required |
|---|---|
| Monitoring ID | Yes |
| Closure ID | Yes |
| Objective | Yes |
| Scope | Yes |
| Signals | Yes |
| Metrics | Yes |
| Thresholds | Yes where applicable |
| Owner | Yes |
| Authority | Yes |
| Frequency | Yes |
| Duration | Yes where applicable |
| Escalation | Yes |
| Reopening Criteria | Yes where applicable |
| Activation Timestamp | Yes |
| Verification | Yes |
| Evidence | Yes |

## Monitoring Activation Is Not Monitoring Execution
Activation establishes the monitoring control. Subsequent observation and measurement constitute monitoring execution.
```text
ACTIVATED
≠
OBSERVED
```

## Monitoring Gaps
A monitoring mechanism that is configured but not functioning shall be treated as a monitoring gap, not as active monitoring.
```text
CONFIGURED
≠
FUNCTIONING
```

## Threshold Governance
Thresholds shall be linked to consequence and response pathways. Thresholds shall not be set merely to minimize alerts.

## Frequency and Duration
Frequency shall be sufficient to detect relevant regression within the required tolerance. Duration shall reflect persistence and recurrence risk.

## Owner and Authority
The monitoring owner performs or coordinates observation. The authority determines escalation, parameter changes, suspension and continuation where applicable.

## Monitoring Suspension
Suspension shall require explicit authority, documented reason, risk assessment and defined reactivation condition where material.

## Monitoring Blind Spots
Known blind spots shall be documented. They shall not be silently treated as evidence of absence of regression.

## AI and Agent Monitoring
AI/agent monitoring shall not rely solely on self-reported status. Independent or external signals shall be used where required.

## Relationship to Regression Detection
RG-122 establishes the active monitoring state from which later monitoring and regression-detection layers operate.
```text
CLOSURE
↓
MONITORING ACTIVATION
↓
MONITORING EXECUTION
↓
REGRESSION DETECTION
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure monitoring activation layer beneath closure and above monitoring execution, regression detection and subsequent post-closure governance. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, consequence, alerting, notification, acknowledgement, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Monitoring Activation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MANDATORY POST-CLOSURE MONITORING ACTIVATION → MONITORING EXECUTION → REGRESSION DETECTION → REGRESSION CLASSIFICATION → CONSEQUENCE DETERMINATION → ALERT DETERMINATION → NOTIFICATION DETERMINATION → ACKNOWLEDGEMENT DETERMINATION → RESPONSE INITIATION DETERMINATION → AUTHORITY TRANSFER DETERMINATION → RESPONSE EXECUTION DETERMINATION → EFFECTIVENESS DETERMINATION → RESOLUTION DETERMINATION → CLOSURE DETERMINATION → REOPENING
```

## Complete Post-Closure Monitoring Activation Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → QUALIFY → COMPARE → DETERMINE DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → DETERMINE ALERT → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLVE → CLOSE → ACTIVATE POST-CLOSURE MONITORING → OBSERVE → MEASURE → DETECT REGRESSION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING AS REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-123` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Monitoring Execution Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY CLOSED REGRESSION CASE WITH A CONTINUING OBSERVATION REQUIREMENT TO ENTER AN EXPLICIT, OWNED, MEASURABLE, THRESHOLD-BASED AND VERIFIED POST-CLOSURE MONITORING STATE BEFORE THE ACTIVE RESPONSE GOVERNANCE IS CONSIDERED COMPLETE, SO THAT CLOSURE NEVER CREATES A LOSS OF OBSERVABILITY OR AN UNCONTROLLED GAP IN REGRESSION DETECTION.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-MONITORING-ACTIVATION-DETERMINATION-01

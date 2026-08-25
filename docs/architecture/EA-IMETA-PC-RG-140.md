# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-MONITORING-ACTIVATION-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-140`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-140` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-MONITORING-ACTIVATION-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Monitoring Activation Determination |
| Parent | EA-IMETA-PC-RG-139 — Mandatory Post-Closure Regression Closure Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory monitoring-activation layer that determines whether a closed post-closure regression case requires controlled monitoring, defines the monitoring objective and scope, assigns ownership and authority, establishes duration, frequency, thresholds, evidence requirements and escalation rules, and verifies that monitoring has actually become operational before the case is treated as actively monitored.

## Core Principle
Post-closure monitoring is a governed control state, not a passive intention to observe. Where monitoring is required, it shall be explicitly activated with a defined objective, owner, authority, scope, cadence, duration, thresholds, evidence model, escalation path and termination or transition conditions. Monitoring shall not be considered active merely because a plan exists or a responsible party has been informed.

```text
VERIFIED CLOSURE
        ↓
MONITORING REQUIRED?
├── NO → MAINTAIN CLOSED STATE / REOPENING CONDITIONS
└── YES
     ↓
ACTIVATION CRITERIA MET?
├── NO → PREPARE / CORRECT / ESCALATE
└── YES
     ↓
DEFINE
├── OBJECTIVE
├── SCOPE
├── OWNER
├── AUTHORITY
├── CADENCE
├── DURATION
├── SIGNALS / METRICS
├── THRESHOLDS
├── EVIDENCE
├── ESCALATION
└── EXIT / REVALIDATION CONDITIONS
     ↓
ACTIVATE
     ↓
VERIFY ACTIVE MONITORING
     ↓
HAND OVER TO MONITORING EXECUTION
```
## Monitoring Activation Quality Test
```text
VALID CLOSED CASE
+
MONITORING REQUIREMENT
+
DEFINED OBJECTIVE
+
DEFINED SCOPE
+
ASSIGNED OWNER / AUTHORITY
+
DEFINED CADENCE / DURATION
+
DEFINED SIGNALS / THRESHOLDS
+
DEFINED EVIDENCE
+
DEFINED ESCALATION
+
VERIFIED ACTIVATION
=
VALID GOVERNED POST-CLOSURE MONITORING
```
## Closure vs Monitoring Activation vs Monitoring Execution
```text
CLOSURE
→ CASE LEAVES ACTIVE RESPONSE / RESOLUTION

MONITORING ACTIVATION
→ GOVERNED MONITORING CONTROL IS ESTABLISHED AND MADE ACTIVE

MONITORING EXECUTION
→ OBSERVATIONS / MEASUREMENTS ARE ACTUALLY PERFORMED

REVALIDATION
→ MONITORING EVIDENCE IS USED TO CONFIRM THE CLOSED / RELIED-UPON STATE

REOPENING
→ NEW EVIDENCE REQUIRES RETURN TO ACTIVE GOVERNANCE
```
## Monitoring Activation States
```text
MA0 — MONITORING NOT REQUIRED
MA1 — MONITORING ASSESSMENT PENDING
MA2 — MONITORING REQUIREMENT CONFIRMED
MA3 — ACTIVATION PREPARATION IN PROGRESS
MA4 — MONITORING OWNER IDENTIFIED
MA5 — MONITORING SCOPE DEFINED
MA6 — MONITORING CONFIGURATION READY
MA7 — MONITORING ACTIVATION AUTHORIZED
MA8 — MONITORING ACTIVATED
MA9 — ACTIVATION VERIFIED
MA10 — MONITORING ACTIVE / EXECUTION HANDOVER
MA11 — ACTIVATION BLOCKED
MA12 — ACTIVATION DELAYED
MA13 — ACTIVATION ESCALATED
MA14 — ACTIVATION REJECTED / REASSESSMENT
MA15 — ACTIVATION COMPLETED / BASELINE ESTABLISHED
MAX — UNKNOWN / INSUFFICIENT BASIS
MAS — ACTIVATION SUSPENDED

## Monitoring Activation Dimensions
| Dimension | Required determination |
|---|---|
| Monitoring Requirement | Why monitoring is required |
| Objective | What monitoring must establish |
| Scope | What is monitored |
| Owner | Accountable monitoring owner |
| Authority | Decision / escalation authority |
| Signals | Observable indicators |
| Metrics | Measurement requirements |
| Cadence | Observation frequency |
| Duration | Monitoring period |
| Thresholds | Trigger conditions |
| Evidence | Required records |
| Escalation | Response path |
| Exit | Monitoring termination criteria |
| Revalidation | Future validation conditions |
| Reopening | Reopening triggers |
| Verification | Activation confirmation |

## Monitoring Activation Invariants

```text
MONITORING SHALL NOT BE CONSIDERED ACTIVE WITHOUT VERIFIED ACTIVATION
```

```text
MONITORING SHALL HAVE A DEFINED OBJECTIVE
```

```text
MONITORING SCOPE SHALL BE EXPLICIT
```

```text
MONITORING OWNER AND AUTHORITY SHALL BE EXPLICIT
```

```text
MONITORING CADENCE AND DURATION SHALL BE DEFINED WHERE APPLICABLE
```

```text
SIGNALS, METRICS AND THRESHOLDS SHALL BE DEFINED TO THE EXTENT REQUIRED BY RISK
```

```text
MONITORING EVIDENCE SHALL BE SUFFICIENT TO SUPPORT LATER REVALIDATION AND REOPENING DECISIONS
```

```text
MONITORING ESCALATION SHALL BE DEFINED BEFORE ACTIVATION WHERE A MATERIAL THRESHOLD CAN BE CROSSED
```

```text
ACTIVATION FAILURE SHALL NOT SILENTLY CREATE A FALSE MONITORING STATE
```

```text
MONITORING REQUIREMENTS SHALL BE PROPORTIONAL TO CONSEQUENCE, RECURRENCE RISK AND GOVERNANCE REQUIREMENTS
```

```text
SECURITY, RESILIENCE, SAFETY, COMPLIANCE AND DATA MONITORING SHALL USE DOMAIN-APPROPRIATE SIGNALS AND THRESHOLDS
```

```text
AI AND AGENT MONITORING SHALL INCLUDE CONTROL, POLICY, TOOL, DATA, BEHAVIOR AND RECURRENCE SIGNALS WHERE RELEVANT
```

```text
MONITORING ACTIVATION SHALL REMAIN DISTINCT FROM MONITORING EXECUTION
```

```text
MONITORING ACTIVATION SHALL REMAIN DISTINCT FROM REVALIDATION
```

```text
MONITORING SHALL NOT BE TERMINATED SOLELY TO AVOID ESCALATION OR REOPENING
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

```text
ACTIVATION SHALL PRESERVE THE CLOSED CASE RECORD AND ITS GOVERNED REOPENING CONDITIONS
```

## 1. Activation Domain — Post-Closure Regression Monitoring Activation Governance

**Control family:** `PCMA-001`

The Post-Closure Regression Monitoring Activation Governance domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-001-01` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-001-02` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-001-03` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-001-04` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-001-05` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-001-06` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-001-07` — Establish and maintain the post-closure regression monitoring activation governance control.
- `PCMA-001-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 2. Activation Domain — Post-Closure Regression Monitoring Activation Objective

**Control family:** `PCMA-002`

The Post-Closure Regression Monitoring Activation Objective domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-002-01` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-002-02` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-002-03` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-002-04` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-002-05` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-002-06` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-002-07` — Establish and maintain the post-closure regression monitoring activation objective control.
- `PCMA-002-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 3. Activation Domain — Post-Closure Regression Monitoring Activation Definition

**Control family:** `PCMA-003`

The Post-Closure Regression Monitoring Activation Definition domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-003-01` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-003-02` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-003-03` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-003-04` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-003-05` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-003-06` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-003-07` — Establish and maintain the post-closure regression monitoring activation definition control.
- `PCMA-003-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 4. Activation Domain — Post-Closure Regression Monitoring Activation Scope

**Control family:** `PCMA-004`

The Post-Closure Regression Monitoring Activation Scope domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-004-01` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-004-02` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-004-03` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-004-04` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-004-05` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-004-06` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-004-07` — Establish and maintain the post-closure regression monitoring activation scope control.
- `PCMA-004-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 5. Activation Domain — Post-Closure Regression Monitoring Activation Authority

**Control family:** `PCMA-005`

The Post-Closure Regression Monitoring Activation Authority domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-005-01` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-005-02` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-005-03` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-005-04` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-005-05` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-005-06` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-005-07` — Establish and maintain the post-closure regression monitoring activation authority control.
- `PCMA-005-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 6. Activation Domain — Post-Closure Regression Monitoring Activation Criteria

**Control family:** `PCMA-006`

The Post-Closure Regression Monitoring Activation Criteria domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-006-01` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-006-02` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-006-03` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-006-04` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-006-05` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-006-06` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-006-07` — Establish and maintain the post-closure regression monitoring activation criteria control.
- `PCMA-006-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 7. Activation Domain — Post-Closure Regression Monitoring Activation Preconditions

**Control family:** `PCMA-007`

The Post-Closure Regression Monitoring Activation Preconditions domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-007-01` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-007-02` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-007-03` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-007-04` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-007-05` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-007-06` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-007-07` — Establish and maintain the post-closure regression monitoring activation preconditions control.
- `PCMA-007-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 8. Activation Domain — Post-Closure Regression Monitoring Activation Evidence

**Control family:** `PCMA-008`

The Post-Closure Regression Monitoring Activation Evidence domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-008-01` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-008-02` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-008-03` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-008-04` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-008-05` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-008-06` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-008-07` — Establish and maintain the post-closure regression monitoring activation evidence control.
- `PCMA-008-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 9. Activation Domain — Post-Closure Regression Monitoring Activation Method

**Control family:** `PCMA-009`

The Post-Closure Regression Monitoring Activation Method domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-009-01` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-009-02` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-009-03` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-009-04` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-009-05` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-009-06` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-009-07` — Establish and maintain the post-closure regression monitoring activation method control.
- `PCMA-009-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 10. Activation Domain — Post-Closure Regression Monitoring Activation Decision

**Control family:** `PCMA-010`

The Post-Closure Regression Monitoring Activation Decision domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-010-01` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-010-02` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-010-03` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-010-04` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-010-05` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-010-06` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-010-07` — Establish and maintain the post-closure regression monitoring activation decision control.
- `PCMA-010-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 11. Activation Domain — Post-Closure Regression Monitoring Activation Accountability

**Control family:** `PCMA-011`

The Post-Closure Regression Monitoring Activation Accountability domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-011-01` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-011-02` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-011-03` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-011-04` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-011-05` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-011-06` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-011-07` — Establish and maintain the post-closure regression monitoring activation accountability control.
- `PCMA-011-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 12. Activation Domain — Post-Closure Regression Monitoring Activation Timing

**Control family:** `PCMA-012`

The Post-Closure Regression Monitoring Activation Timing domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-012-01` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-012-02` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-012-03` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-012-04` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-012-05` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-012-06` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-012-07` — Establish and maintain the post-closure regression monitoring activation timing control.
- `PCMA-012-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 13. Activation Domain — Security Post-Closure Regression Monitoring Activation

**Control family:** `PCMA-013`

The Security Post-Closure Regression Monitoring Activation domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-013-01` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-013-02` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-013-03` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-013-04` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-013-05` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-013-06` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-013-07` — Establish and maintain the security post-closure regression monitoring activation control.
- `PCMA-013-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 14. Activation Domain — Resilience Post-Closure Regression Monitoring Activation

**Control family:** `PCMA-014`

The Resilience Post-Closure Regression Monitoring Activation domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-014-01` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-014-02` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-014-03` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-014-04` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-014-05` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-014-06` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-014-07` — Establish and maintain the resilience post-closure regression monitoring activation control.
- `PCMA-014-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 15. Activation Domain — Compliance Post-Closure Regression Monitoring Activation

**Control family:** `PCMA-015`

The Compliance Post-Closure Regression Monitoring Activation domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-015-01` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-015-02` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-015-03` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-015-04` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-015-05` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-015-06` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-015-07` — Establish and maintain the compliance post-closure regression monitoring activation control.
- `PCMA-015-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 16. Activation Domain — Data Post-Closure Regression Monitoring Activation

**Control family:** `PCMA-016`

The Data Post-Closure Regression Monitoring Activation domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-016-01` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-016-02` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-016-03` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-016-04` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-016-05` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-016-06` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-016-07` — Establish and maintain the data post-closure regression monitoring activation control.
- `PCMA-016-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 17. Activation Domain — AI and Agent Post-Closure Regression Monitoring Activation

**Control family:** `PCMA-017`

The AI and Agent Post-Closure Regression Monitoring Activation domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-017-01` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-017-02` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-017-03` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-017-04` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-017-05` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-017-06` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-017-07` — Establish and maintain the ai and agent post-closure regression monitoring activation control.
- `PCMA-017-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 18. Activation Domain — Post-Closure Regression Monitoring Activation Failure

**Control family:** `PCMA-018`

The Post-Closure Regression Monitoring Activation Failure domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-018-01` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-018-02` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-018-03` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-018-04` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-018-05` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-018-06` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-018-07` — Establish and maintain the post-closure regression monitoring activation failure control.
- `PCMA-018-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 19. Activation Domain — Post-Closure Regression Monitoring Activation Independence

**Control family:** `PCMA-019`

The Post-Closure Regression Monitoring Activation Independence domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-019-01` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-019-02` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-019-03` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-019-04` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-019-05` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-019-06` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-019-07` — Establish and maintain the post-closure regression monitoring activation independence control.
- `PCMA-019-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## 20. Activation Domain — Post-Closure Regression Monitoring Activation Review and Learning

**Control family:** `PCMA-020`

The Post-Closure Regression Monitoring Activation Review and Learning domain establishes governed mandatory monitoring-activation requirements.

### Required controls
- `PCMA-020-01` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-01-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-020-02` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-02-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-020-03` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-03-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-020-04` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-04-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-020-05` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-05-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-020-06` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-06-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.
- `PCMA-020-07` — Establish and maintain the post-closure regression monitoring activation review and learning control.
- `PCMA-020-07-E` — Preserve requirement, objective, scope, owner, authority, signals, metrics, cadence, duration, thresholds, evidence, escalation, exit, revalidation, reopening and verification traceability.

```text
CLOSED CASE → MONITORING REQUIREMENT → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → EXECUTION HANDOVER
```

## Post-Closure Regression Monitoring Activation Structure

| Element | Required definition |
|---|---|
| Requirement | Reason monitoring is needed |
| Objective | Monitoring purpose |
| Scope | Monitored condition / population |
| Owner | Accountable owner |
| Authority | Decision / escalation authority |
| Signals | Observable indicators |
| Metrics | Measurement model |
| Cadence | Frequency |
| Duration | Monitoring period |
| Thresholds | Trigger conditions |
| Evidence | Required record |
| Escalation | Response path |
| Exit | Termination conditions |
| Revalidation | Future validation |
| Reopening | Trigger conditions |

## Post-Closure Regression Monitoring Activation Objective

Establish an operational and verifiable monitoring control that can detect recurrence, degradation, changed assumptions, threshold breaches or other conditions that challenge the closed state.

## Post-Closure Regression Monitoring Activation Definition

Monitoring activation is the governed transition from a defined monitoring requirement and configuration to a verified active monitoring control.

## Post-Closure Regression Monitoring Activation Scope

Scope includes monitoring requirements, objectives, signals, metrics, cadence, duration, ownership, authority, thresholds, evidence, escalation, exit, revalidation and reopening conditions.

## Post-Closure Regression Monitoring Activation Authority

Authority shall define who may approve, activate, modify, suspend, terminate, escalate or independently verify post-closure monitoring.

## Post-Closure Regression Monitoring Activation Criteria

Criteria shall define when monitoring is required and what must exist before activation.
```text
CLOSED CASE
↓
MONITORING REQUIRED?
├── NO → NO ACTIVATION
└── YES
     ↓
OBJECTIVE / SCOPE / OWNER / AUTHORITY DEFINED?
├── NO → PREPARE / CORRECT
└── YES
     ↓
SIGNALS / THRESHOLDS / CADENCE / EVIDENCE DEFINED?
├── NO → CONFIGURE
└── YES
     ↓
AUTHORIZED?
├── NO → ESCALATE / HOLD
└── YES
     ↓
ACTIVATE → VERIFY
```

## Post-Closure Regression Monitoring Activation Preconditions

Preconditions include verified closure, a confirmed monitoring requirement, defined objective and scope, assigned owner and authority, monitoring configuration, evidence requirements and escalation conditions.

## Post-Closure Regression Monitoring Activation Evidence

Evidence shall preserve the monitoring requirement, rationale, configuration, owner, authority, signals, thresholds, cadence, duration, activation timestamp, verification and handover.

## Post-Closure Regression Monitoring Activation Method

Methods may include manual monitoring setup, automated monitoring configuration, scheduled observation, event-driven monitoring, threshold monitoring, control monitoring and hybrid monitoring.
```text
REQUIREMENT → DESIGN → CONFIGURE → AUTHORIZE → ACTIVATE → VERIFY → HANDOVER
```

## Post-Closure Regression Monitoring Activation Decision

Decision shall determine MA0, MA1, MA2, MA3, MA4, MA5, MA6, MA7, MA8, MA9, MA10, MA11, MA12, MA13, MA14, MA15, MAX or MAS.

## Post-Closure Regression Monitoring Activation Accountability

Accountability shall remain explicit for monitoring design, activation, verification, ongoing ownership and escalation.

## Post-Closure Regression Monitoring Activation Timing

Monitoring shall be activated before the required observation window begins. Activation delays that materially increase risk shall trigger escalation.

## Security Post-Closure Regression Monitoring Activation

Security monitoring activation shall define relevant security signals, alert thresholds, evidence retention, escalation authority and access controls.

## Resilience Post-Closure Regression Monitoring Activation

Resilience monitoring activation shall define service-health indicators, dependency signals, continuity thresholds and escalation paths.

## Compliance Post-Closure Regression Monitoring Activation

Compliance monitoring activation shall define applicable obligations, evidence, review cadence, threshold conditions and reporting escalation.

## Data Post-Closure Regression Monitoring Activation

Data monitoring activation shall define integrity, lineage, access, availability, consistency and anomaly signals appropriate to the closed condition.

## AI and Agent Post-Closure Regression Monitoring Activation

AI/agent monitoring activation shall define signals for policy adherence, authority boundaries, tool usage, data access, behavioral drift, unsafe outcomes and recurrence where applicable.
```text
AI / AGENT CLOSED STATE
↓
DEFINE CONTROL / POLICY / TOOL / DATA SIGNALS
↓
DEFINE THRESHOLDS
↓
AUTHORIZE
↓
ACTIVATE
↓
VERIFY
```

## Post-Closure Regression Monitoring Activation Failure

Failure includes missing owner, invalid configuration, missing threshold, unavailable telemetry, failed activation, delayed activation or inability to verify active monitoring.
```text
ACTIVATION FAILURE
↓
MONITORING CONTROL AT RISK?
├── YES → ESCALATE / FALLBACK / MANUAL CONTROL
└── NO → CORRECT / RETRY / RECORD
```

## Post-Closure Regression Monitoring Activation Independence

Independent activation verification shall be used where monitoring failure or configuration bias could materially compromise safety, security, compliance or other high-consequence controls.

## Post-Closure Regression Monitoring Activation Review and Learning

Reviews shall examine activation gaps, missing signals, ineffective thresholds, delayed activation, false confidence, telemetry failures and monitoring-triggered reopenings.

## Monitoring Activation Decision Model
```text
VERIFIED CLOSURE
↓
MONITORING REQUIRED?
├── NO → MA0 / MAINTAIN CLOSED STATE
└── YES
     ↓
DEFINE OBJECTIVE + SCOPE
     ↓
ASSIGN OWNER + AUTHORITY
     ↓
DEFINE SIGNALS + METRICS + THRESHOLDS
     ↓
DEFINE CADENCE + DURATION
     ↓
DEFINE EVIDENCE + ESCALATION + EXIT
     ↓
CONFIGURATION READY?
├── NO → CORRECT
└── YES
     ↓
AUTHORIZE ACTIVATION
     ↓
ACTIVATE
     ↓
ACTIVATION VERIFIED?
├── NO → BLOCK / FALLBACK / ESCALATE
└── YES
     ↓
HANDOVER TO MONITORING EXECUTION
```

## Monitoring Activation Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| MA0 | Not required | Maintain closed state |
| MA1 | Assessment pending | Determine requirement |
| MA2 | Requirement confirmed | Prepare activation |
| MA3 | Preparation in progress | Configure |
| MA4 | Owner identified | Complete governance assignment |
| MA5 | Scope defined | Complete configuration |
| MA6 | Configuration ready | Seek authorization |
| MA7 | Authorized | Activate |
| MA8 | Activated | Verify |
| MA9 | Activation verified | Make operational |
| MA10 | Active / handover | Begin monitoring execution |
| MA11 | Blocked | Correct / escalate / fallback |
| MA12 | Delayed | Escalate where material |
| MA13 | Escalated | Higher authority engaged |
| MA14 | Rejected / reassessment | Reassess requirement |
| MA15 | Completed / baseline established | Continue execution |
| MAX | Unknown | Do not assume active monitoring |
| MAS | Suspended | Restore activation |

## Monitoring Activation Record
| Field | Required |
|---|---|
| Monitoring Activation ID | Yes |
| Closure ID | Yes |
| Regression ID | Yes |
| Monitoring Requirement | Yes |
| Objective | Yes |
| Scope | Yes |
| Owner | Yes |
| Authority | Yes |
| Signals | Yes |
| Metrics | Where applicable |
| Cadence | Yes |
| Duration | Where applicable |
| Thresholds | Yes where applicable |
| Evidence Model | Yes |
| Escalation | Yes where applicable |
| Exit Criteria | Yes |
| Revalidation Conditions | Where applicable |
| Reopening Conditions | Yes |
| Activation Authorization | Yes |
| Activation Timestamp | Yes |
| Verification | Yes |
| Handover | Yes |
| Audit Trail | Yes |

## Monitoring Activation Is Not Monitoring Execution
Activation establishes the monitoring control. Execution performs observations and measurements.
```text
ACTIVATED
≠
OBSERVATION PERFORMED
```

## Monitoring Activation Is Not Revalidation
Activation creates the capability to observe. Revalidation uses monitoring evidence to confirm a condition or reliance state.
```text
MONITORING ACTIVE
≠
REVALIDATED
```

## Monitoring Activation Is Not Reopening
Activation does not imply that a case is reopened. Reopening occurs only when defined reopening conditions are met.

## Monitoring Objective
Every required monitoring arrangement shall have a clear objective describing what the monitoring is expected to detect, confirm or protect.

## Monitoring Scope
Scope shall define the systems, services, controls, data, behaviors, populations, dependencies or conditions subject to observation.

## Signals and Thresholds
Signals and thresholds shall be sufficient to detect material deterioration or recurrence. Thresholds shall not be defined so broadly that meaningful changes are hidden.

## Monitoring Cadence
Cadence shall be proportionate to consequence, recurrence risk, rate of change and the time available to respond to a threshold breach.

## Monitoring Duration
Where monitoring is time-bound, duration shall be explicit. Where monitoring is condition-bound, the exit condition shall be explicit.

## Evidence
Monitoring activation evidence shall be sufficient to prove that the monitoring control exists and was operationally verified before execution is relied upon.

## Fallback Control
Where automated monitoring cannot be activated, an approved fallback or manual control shall be used where required to preserve the intended protection.

## AI and Agent Monitoring
AI/agent monitoring shall cover relevant model behavior, policy compliance, tool calls, authority boundaries, data access, drift and consequential outcomes.

## Relationship to Monitoring Execution
RG-140 supplies the verified monitoring activation state to the subsequent monitoring-execution layer.
```text
CLOSURE → MONITORING ACTIVATION → MONITORING EXECUTION
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression monitoring activation layer beneath closure determination and above monitoring execution. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, qualification, validation, deviation, regression determination, regression classification, consequence determination, alert determination, notification determination, acknowledgement determination, response initiation, authority transfer, response execution, effectiveness, resolution, closure, monitoring execution, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Monitoring Activation Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → MANDATORY MONITORING ACTIVATION → MONITORING EXECUTION → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REOPENING
```

## Complete Monitoring Activation Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ISSUE ALERT → DETERMINE NOTIFICATION → ISSUE NOTIFICATION → DELIVER → DETERMINE ACKNOWLEDGEMENT → VALIDATE ACTOR / TIMING / COMPLETENESS → ACKNOWLEDGE → ACCEPT / ASSIGN → DETERMINE RESPONSE INITIATION → AUTHORIZE → ASSIGN → ACTIVATE → VERIFY → DETERMINE AUTHORITY TRANSFER → IDENTIFY RECEIVER → PACKAGE STATE → ACCEPT → VERIFY → ACTIVATE RECEIVING AUTHORITY → DETERMINE EXECUTION → AUTHORIZE ACTION → EXECUTE → OBSERVE → VERIFY → ADJUST / ESCALATE / ROLLBACK / STOP → COMPLETE → DETERMINE EFFECTIVENESS → VERIFY → DETERMINE RESOLUTION → RESTORE / CONTROL CONDITION → VERIFY → DETERMINE CLOSURE → COMPLETE OBLIGATIONS → CONFIRM EVIDENCE / RISK / HANDOVER → AUTHORIZE → VERIFY → CLOSE → DETERMINE MONITORING REQUIREMENT → DEFINE OBJECTIVE / SCOPE / OWNER / AUTHORITY / SIGNALS / THRESHOLDS / CADENCE / DURATION / EVIDENCE / ESCALATION → AUTHORIZE → ACTIVATE → VERIFY → HANDOVER → EXECUTE MONITORING → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-141` — Mandatory Post-Closure Regression Monitoring Execution Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY POST-CLOSURE REGRESSION CASE FOR WHICH MONITORING IS REQUIRED TO HAVE AN EXPLICITLY DEFINED AND AUTHORIZED MONITORING OBJECTIVE, SCOPE, OWNER, AUTHORITY, SIGNALS, METRICS, CADENCE, DURATION, THRESHOLDS, EVIDENCE, ESCALATION AND EXIT CONDITIONS, WITH ACTIVATION VERIFIED BEFORE MONITORING IS TREATED AS OPERATIONAL, ACTIVATION KEPT DISTINCT FROM MONITORING EXECUTION AND REVALIDATION, AND ANY ACTIVATION FAILURE OR MATERIAL DELAY GOVERNED THROUGH FALLBACK, ESCALATION, CORRECTION OR REASSESSMENT.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-MONITORING-ACTIVATION-DETERMINATION-01

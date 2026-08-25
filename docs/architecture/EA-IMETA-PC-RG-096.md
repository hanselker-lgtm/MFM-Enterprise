# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-MONITORING-ACTIVATION-AND-BASELINE-CONTROL-01

## Physical File ID
`EA-IMETA-PC-RG-096`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-096` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-MONITORING-ACTIVATION-AND-BASELINE-CONTROL-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Monitoring Activation and Baseline Control |
| Parent | EA-IMETA-PC-RG-095 — Mandatory Post-Closure Transition Control |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory post-closure monitoring activation and baseline-control layer that makes the transitioned post-closure state observable, comparable and governable, with an explicit baseline from which future deviation and regression can be determined.

## Core Principle
Monitoring cannot reliably detect change without a defined observation model and baseline. RG-096 therefore establishes the required monitoring controls, baseline state, observation parameters, ownership, timing, evidence and activation confirmation before post-closure monitoring is considered operational.

```text
POST-CLOSURE STATE ACCEPTED
      ↓
MONITORING REQUIREMENTS DEFINED?
├── NO → DEFINE / HOLD
└── YES
     ↓
BASELINE VALID?
├── NO → ESTABLISH / RECONSTRUCT / ESCALATE
└── YES
     ↓
MONITORING CONTROLS CONFIGURED?
├── NO → CONFIGURE
└── YES
     ↓
DATA / SIGNALS AVAILABLE?
├── NO → CORRECT / COMPENSATE
└── YES
     ↓
ACTIVATION VERIFIED?
├── NO → CORRECT / ESCALATE
└── YES
     ↓
POST-CLOSURE MONITORING ACTIVE
     ↓
OBSERVE → COMPARE → DETECT DEVIATION
```

## Monitoring Activation Quality Test
```text
VALID POST-CLOSURE STATE
+
DEFINED MONITORING OBJECTIVES
+
VALID BASELINE
+
DEFINED OBSERVATION PARAMETERS
+
ACTIVE DATA / SIGNAL PATH
+
IDENTIFIED OWNER
+
DEFINED ALERT / ESCALATION PATH
+
ACTIVATION VERIFIED
=
VALID GOVERNED POST-CLOSURE MONITORING
```

## Monitoring vs Baseline vs Comparison
```text
MONITORING
→ OBSERVE THE CURRENT POST-CLOSURE STATE

BASELINE
→ DEFINE THE VALID REFERENCE STATE

COMPARISON
→ DETERMINE WHETHER CURRENT OBSERVATION DEVIATES FROM THE REFERENCE
```

## Monitoring Activation State Model
```text
NOT DEFINED
PLANNED
CONFIGURING
PENDING BASELINE
PENDING DATA
PENDING VERIFICATION
ACTIVE
DEGRADED
SUSPENDED
FAILED
REACTIVATING
RETIRED
```

## Monitoring Activation and Baseline Invariants

```text
POST-CLOSURE MONITORING SHALL HAVE AN EXPLICIT OBJECTIVE
```

```text
THE MONITORED CONDITION SHALL BE IDENTIFIABLE
```

```text
THE BASELINE SHALL BE VALID, VERSIONED AND TRACEABLE
```

```text
BASELINE ASSUMPTIONS SHALL BE DOCUMENTED
```

```text
OBSERVATION PARAMETERS SHALL BE DEFINED
```

```text
MONITORING DATA OR SIGNALS SHALL HAVE IDENTIFIABLE PROVENANCE WHERE MATERIAL
```

```text
MONITORING OWNERSHIP SHALL BE EXPLICIT
```

```text
ACTIVATION SHALL BE VERIFIED BEFORE MONITORING IS CONSIDERED OPERATIONAL
```

```text
MONITORING FAILURE SHALL NOT BE TREATED AS EVIDENCE OF STABILITY
```

```text
BASELINE CHANGE SHALL BE GOVERNED AND SHALL NOT SILENTLY ERASE HISTORICAL REFERENCE
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE MONITORING SHALL HAVE APPROPRIATE COVERAGE
```

```text
AI AND AGENT MONITORING SHALL COVER RELEVANT OUTCOME, CONTROL, AUTHORITY AND BEHAVIOURAL CONDITIONS
```

```text
DATA GAPS SHALL BE VISIBLE AND SHALL HAVE APPROPRIATE COMPENSATING CONTROLS
```

```text
MONITORING THRESHOLDS SHALL REMAIN TRACEABLE TO APPLICABLE CRITERIA
```

```text
BASELINE RECONSTRUCTION SHALL BE EXPLICIT WHEN ORIGINAL BASELINE EVIDENCE IS INCOMPLETE
```

```text
MONITORING ACTIVATION SHALL PRESERVE THE POST-CLOSURE HANDOVER HISTORY
```

## 1. Monitoring Domain — Post-Closure Monitoring Activation Baseline Governance

**Control family:** `PCMA-001`

The Post-Closure Monitoring Activation Baseline Governance domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-001-01` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-001-02` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-001-03` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-001-04` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-001-05` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-001-06` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-001-07` — Establish and maintain the post-closure monitoring activation baseline governance control.
- `PCMA-001-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 2. Monitoring Domain — Post-Closure Monitoring Activation Baseline Objective

**Control family:** `PCMA-002`

The Post-Closure Monitoring Activation Baseline Objective domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-002-01` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-002-02` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-002-03` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-002-04` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-002-05` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-002-06` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-002-07` — Establish and maintain the post-closure monitoring activation baseline objective control.
- `PCMA-002-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 3. Monitoring Domain — Post-Closure Monitoring Activation Baseline Definition

**Control family:** `PCMA-003`

The Post-Closure Monitoring Activation Baseline Definition domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-003-01` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-003-02` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-003-03` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-003-04` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-003-05` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-003-06` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-003-07` — Establish and maintain the post-closure monitoring activation baseline definition control.
- `PCMA-003-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 4. Monitoring Domain — Post-Closure Monitoring Activation Baseline Scope

**Control family:** `PCMA-004`

The Post-Closure Monitoring Activation Baseline Scope domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-004-01` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-004-02` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-004-03` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-004-04` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-004-05` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-004-06` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-004-07` — Establish and maintain the post-closure monitoring activation baseline scope control.
- `PCMA-004-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 5. Monitoring Domain — Post-Closure Monitoring Activation Baseline Authority

**Control family:** `PCMA-005`

The Post-Closure Monitoring Activation Baseline Authority domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-005-01` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-005-02` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-005-03` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-005-04` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-005-05` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-005-06` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-005-07` — Establish and maintain the post-closure monitoring activation baseline authority control.
- `PCMA-005-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 6. Monitoring Domain — Post-Closure Monitoring Activation Baseline Criteria

**Control family:** `PCMA-006`

The Post-Closure Monitoring Activation Baseline Criteria domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-006-01` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-006-02` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-006-03` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-006-04` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-006-05` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-006-06` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-006-07` — Establish and maintain the post-closure monitoring activation baseline criteria control.
- `PCMA-006-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 7. Monitoring Domain — Post-Closure Monitoring Activation Baseline Preconditions

**Control family:** `PCMA-007`

The Post-Closure Monitoring Activation Baseline Preconditions domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-007-01` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-007-02` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-007-03` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-007-04` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-007-05` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-007-06` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-007-07` — Establish and maintain the post-closure monitoring activation baseline preconditions control.
- `PCMA-007-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 8. Monitoring Domain — Post-Closure Monitoring Activation Baseline Evidence

**Control family:** `PCMA-008`

The Post-Closure Monitoring Activation Baseline Evidence domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-008-01` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-008-02` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-008-03` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-008-04` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-008-05` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-008-06` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-008-07` — Establish and maintain the post-closure monitoring activation baseline evidence control.
- `PCMA-008-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 9. Monitoring Domain — Post-Closure Monitoring Activation Baseline Method

**Control family:** `PCMA-009`

The Post-Closure Monitoring Activation Baseline Method domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-009-01` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-009-02` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-009-03` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-009-04` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-009-05` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-009-06` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-009-07` — Establish and maintain the post-closure monitoring activation baseline method control.
- `PCMA-009-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 10. Monitoring Domain — Post-Closure Monitoring Activation Baseline Decision

**Control family:** `PCMA-010`

The Post-Closure Monitoring Activation Baseline Decision domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-010-01` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-010-02` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-010-03` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-010-04` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-010-05` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-010-06` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-010-07` — Establish and maintain the post-closure monitoring activation baseline decision control.
- `PCMA-010-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 11. Monitoring Domain — Post-Closure Monitoring Activation Baseline Accountability

**Control family:** `PCMA-011`

The Post-Closure Monitoring Activation Baseline Accountability domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-011-01` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-011-02` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-011-03` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-011-04` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-011-05` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-011-06` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-011-07` — Establish and maintain the post-closure monitoring activation baseline accountability control.
- `PCMA-011-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 12. Monitoring Domain — Post-Closure Monitoring Activation Baseline Timing

**Control family:** `PCMA-012`

The Post-Closure Monitoring Activation Baseline Timing domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-012-01` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-012-02` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-012-03` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-012-04` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-012-05` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-012-06` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-012-07` — Establish and maintain the post-closure monitoring activation baseline timing control.
- `PCMA-012-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 13. Monitoring Domain — Security Post-Closure Monitoring Activation Baseline

**Control family:** `PCMA-013`

The Security Post-Closure Monitoring Activation Baseline domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-013-01` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-013-02` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-013-03` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-013-04` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-013-05` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-013-06` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-013-07` — Establish and maintain the security post-closure monitoring activation baseline control.
- `PCMA-013-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 14. Monitoring Domain — Resilience Post-Closure Monitoring Activation Baseline

**Control family:** `PCMA-014`

The Resilience Post-Closure Monitoring Activation Baseline domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-014-01` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-014-02` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-014-03` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-014-04` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-014-05` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-014-06` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-014-07` — Establish and maintain the resilience post-closure monitoring activation baseline control.
- `PCMA-014-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 15. Monitoring Domain — Compliance Post-Closure Monitoring Activation Baseline

**Control family:** `PCMA-015`

The Compliance Post-Closure Monitoring Activation Baseline domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-015-01` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-015-02` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-015-03` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-015-04` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-015-05` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-015-06` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-015-07` — Establish and maintain the compliance post-closure monitoring activation baseline control.
- `PCMA-015-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 16. Monitoring Domain — Data Post-Closure Monitoring Activation Baseline

**Control family:** `PCMA-016`

The Data Post-Closure Monitoring Activation Baseline domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-016-01` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-016-02` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-016-03` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-016-04` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-016-05` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-016-06` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-016-07` — Establish and maintain the data post-closure monitoring activation baseline control.
- `PCMA-016-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 17. Monitoring Domain — AI and Agent Post-Closure Monitoring Activation Baseline

**Control family:** `PCMA-017`

The AI and Agent Post-Closure Monitoring Activation Baseline domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-017-01` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-017-02` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-017-03` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-017-04` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-017-05` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-017-06` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-017-07` — Establish and maintain the ai and agent post-closure monitoring activation baseline control.
- `PCMA-017-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 18. Monitoring Domain — Post-Closure Monitoring Activation Baseline Failure

**Control family:** `PCMA-018`

The Post-Closure Monitoring Activation Baseline Failure domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-018-01` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-018-02` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-018-03` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-018-04` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-018-05` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-018-06` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-018-07` — Establish and maintain the post-closure monitoring activation baseline failure control.
- `PCMA-018-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 19. Monitoring Domain — Post-Closure Monitoring Activation Baseline Independence

**Control family:** `PCMA-019`

The Post-Closure Monitoring Activation Baseline Independence domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-019-01` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-019-02` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-019-03` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-019-04` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-019-05` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-019-06` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-019-07` — Establish and maintain the post-closure monitoring activation baseline independence control.
- `PCMA-019-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## 20. Monitoring Domain — Post-Closure Monitoring Activation Baseline Review and Learning

**Control family:** `PCMA-020`

The Post-Closure Monitoring Activation Baseline Review and Learning domain establishes governed mandatory post-closure monitoring activation and baseline requirements.

### Required controls
- `PCMA-020-01` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-01-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-020-02` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-02-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-020-03` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-03-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-020-04` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-04-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-020-05` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-05-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-020-06` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-06-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.
- `PCMA-020-07` — Establish and maintain the post-closure monitoring activation baseline review and learning control.
- `PCMA-020-07-E` — Preserve monitoring objective, baseline, observation parameters, data source, owner, activation state, timing and verification traceability.

```text
DEFINE → BASELINE → CONFIGURE → VERIFY → ACTIVATE → OBSERVE
```

## Post-Closure Monitoring Activation Baseline Structure

| Element | Required definition |
|---|---|
| Monitoring Objective | What must be observed |
| Condition | Governed post-closure condition |
| Baseline | Valid reference state |
| Observation Parameters | What / how / when to observe |
| Data Source | Source of evidence |
| Owner | Monitoring responsibility |
| Thresholds | Trigger criteria |
| Escalation | Response path |
| Activation Evidence | Proof monitoring is operational |

## Post-Closure Monitoring Activation Baseline Objective

Make the post-closure state continuously or periodically observable at the level required to detect meaningful deviation, renewed failure or regression.

## Post-Closure Monitoring Activation Baseline Definition

Monitoring activation is the verified transition into an operational observation state. Baseline control is the governed establishment and maintenance of the reference state used for subsequent comparison.

## Post-Closure Monitoring Activation Baseline Scope

Scope shall identify conditions, systems, services, data, controls, dependencies, metrics, observations, time windows and environments included in monitoring.

## Post-Closure Monitoring Activation Baseline Authority

Authority shall define who establishes or approves the baseline, activates monitoring, changes parameters, accepts monitoring gaps and authorizes suspension or retirement.

## Post-Closure Monitoring Activation Baseline Criteria

Criteria shall define monitoring coverage, baseline validity, observation frequency, data quality, activation verification, threshold configuration and escalation readiness.

```text
POST-CLOSURE STATE
↓
BASELINE VALID?
├── NO → ESTABLISH / RECONSTRUCT
└── YES
     ↓
MONITORING CONFIGURED?
├── NO → CONFIGURE
└── YES
     ↓
DATA AVAILABLE + VALID?
├── NO → CORRECT / COMPENSATE
└── YES
     ↓
ACTIVATION VERIFIED?
├── NO → CORRECT / ESCALATE
└── YES → ACTIVE
```

## Post-Closure Monitoring Activation Baseline Preconditions

Preconditions include accepted post-closure transition, defined monitoring objective, baseline, observation parameters, data sources, owner, thresholds and escalation path.

## Post-Closure Monitoring Activation Baseline Evidence

Evidence shall preserve baseline state, baseline source, criteria version, monitoring configuration, activation tests, data-source validation, owner acceptance and effective activation time.

## Post-Closure Monitoring Activation Baseline Method

Methods may include baseline registration, sensor or telemetry activation, scheduled observation, automated control checks, manual verification, sampling and threshold validation.

```text
BASELINE
↓
CONFIGURE OBSERVATION
↓
VALIDATE SIGNAL
↓
TEST THRESHOLDS
↓
VERIFY ACTIVATION
↓
MONITOR
```

## Post-Closure Monitoring Activation Baseline Decision

Decision shall explicitly determine active, pending, degraded, suspended, failed or reactivation status and the effect on reliance and regression detection.

```text
MONITORING
├── ACTIVE → OBSERVE / COMPARE
├── DEGRADED → COMPENSATE / CORRECT
├── FAILED → ESCALATE / RESTORE
└── SUSPENDED → GOVERN / REACTIVATE
```

## Post-Closure Monitoring Activation Baseline Accountability

Accountability shall remain explicit for baseline validity, monitoring availability, data quality, activation status and response to monitoring degradation.

## Post-Closure Monitoring Activation Baseline Timing

Monitoring frequency shall reflect consequence, expected change rate, time-to-impact and the likelihood that a meaningful regression could occur between observations.

## Security Post-Closure Monitoring Activation Baseline

Security monitoring shall maintain valid reference conditions for access, exposure, control integrity, anomalous activity and relevant threat indicators.

## Resilience Post-Closure Monitoring Activation Baseline

Resilience monitoring shall maintain reference conditions for availability, recovery capability, capacity, dependencies, continuity and degradation indicators.

## Compliance Post-Closure Monitoring Activation Baseline

Compliance monitoring shall maintain reference conditions for required controls, obligations, evidence and reporting states.

## Data Post-Closure Monitoring Activation Baseline

Data monitoring shall maintain reference conditions for integrity, quality, lineage, access, confidentiality, retention and authorized-use controls.

## AI and Agent Post-Closure Monitoring Activation Baseline

AI/agent monitoring shall establish relevant baselines for outcome quality, policy compliance, authority use, tool use, data use, autonomy and behavioural conditions.

```text
AI / AGENT BASELINE
↓
OUTCOME + CONTROL + AUTHORITY + TOOL + DATA + BEHAVIOUR
↓
MONITOR
```

## Post-Closure Monitoring Activation Baseline Failure

Failure includes missing baseline, invalid baseline, inactive data path, stale observations, broken monitoring logic, false healthy state or inability to determine current state.

```text
MONITORING FAILURE
↓
CURRENT STATE KNOWN?
├── YES → DEGRADED / COMPENSATE
└── NO → ESCALATE / REOPEN AS REQUIRED
```

## Post-Closure Monitoring Activation Baseline Independence

Independent verification may be required for high-consequence monitoring, critical baselines, disputed activation evidence or situations where the monitoring owner controls the condition being measured.

## Post-Closure Monitoring Activation Baseline Review and Learning

Reviews shall identify blind spots, stale baselines, false negatives, activation failures, excessive data gaps, inappropriate observation frequency and recurring monitoring degradation.

## Monitoring Activation Determination Model
```text
POST-CLOSURE STATE ACCEPTED
↓
MONITORING OBJECTIVE DEFINED?
├── NO → DEFINE / HOLD
└── YES
     ↓
BASELINE VALID?
├── NO → ESTABLISH / RECONSTRUCT / ESCALATE
└── YES
     ↓
OBSERVATION PARAMETERS DEFINED?
├── NO → DEFINE
└── YES
     ↓
DATA / SIGNAL PATH AVAILABLE?
├── NO → CORRECT / COMPENSATE
└── YES
     ↓
THRESHOLDS / ESCALATION READY?
├── NO → CONFIGURE
└── YES
     ↓
ACTIVATION VERIFIED?
├── NO → CORRECT / ESCALATE
└── YES
     ↓
MONITORING ACTIVE
```

## Monitoring Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Not Defined | Monitoring model absent | Define |
| Planned | Requirements defined | Configure |
| Configuring | Controls being established | Complete |
| Pending Baseline | Reference state unavailable | Establish / reconstruct |
| Pending Data | Observation source unavailable | Restore / compensate |
| Pending Verification | Activation not proven | Verify |
| Active | Monitoring operational | Observe / compare |
| Degraded | Monitoring partially impaired | Compensate / correct |
| Suspended | Monitoring intentionally inactive | Govern / reactivate |
| Failed | Monitoring cannot reliably operate | Escalate / restore |
| Reactivating | Controls being restored | Verify |
| Retired | Monitoring formally ended | Preserve rationale |

## Monitoring Activation Record
| Field | Required |
|---|---|
| Monitoring ID | Yes |
| Condition ID | Yes |
| Transition ID | Yes |
| Monitoring Objective | Yes |
| Baseline ID | Yes |
| Baseline Version | Yes |
| Observation Parameters | Yes |
| Data Source | Yes |
| Thresholds | Where applicable |
| Escalation Path | Yes |
| Owner | Yes |
| Activation Evidence | Yes |
| Effective Time | Yes |
| Verification | Yes |
| Exceptions / Gaps | Where applicable |

## Baseline Integrity
The baseline is a governed reference state. It shall not be silently changed to make a current deviation appear normal.

```text
CURRENT STATE
vs
ORIGINAL / APPROVED BASELINE
≠
BASELINE SILENTLY MOVED TO CURRENT STATE
```

## Baseline Change
Material baseline changes shall be explicitly proposed, justified, approved, versioned and linked to the prior baseline.

## Baseline Reconstruction
If the original baseline is incomplete, reconstruction shall be explicit and evidence-backed. Reconstructed baselines shall carry an uncertainty or confidence indication where appropriate.

## Observation Parameters
Monitoring shall define, as applicable:
- what is observed
- measurement method
- observation frequency
- observation window
- data quality requirements
- threshold logic
- ownership
- escalation

## Monitoring Coverage
Coverage shall be proportional to consequence. A low-frequency observation model shall not be used where the condition can materially regress between observations without compensating controls.

## Data Gaps
A missing observation is not proof of a healthy condition.

```text
NO DATA
≠
NO DEVIATION
```

Data gaps shall be visible and handled through correction, compensation, escalation or other governed treatment.

## Monitoring Degradation
If monitoring becomes degraded, the post-closure state shall be marked accordingly. It shall not remain represented as fully monitored.

## False Healthy State
Monitoring systems shall avoid interpreting stale, frozen or default values as evidence of a healthy state.

## Activation Verification
Activation verification shall demonstrate that the configured monitoring actually produces expected observations and that thresholds or control paths operate as intended.

## AI and Agent Monitoring
AI/agent post-closure monitoring should cover not only output outcomes but relevant control dimensions, including authority, policy, tool use, data access, autonomy and behaviour.

## Monitoring Anti-Gaming
Monitoring shall not be configured or tuned merely to reduce alerts, improve apparent stability or avoid reopening unless the change is justified by valid criteria and governance.

## Relationship to Comparison
RG-096 establishes the operational observation and reference foundation. The next layers use the observations and baseline to determine meaningful change.

```text
MONITORING ACTIVE
↓
OBSERVE
↓
BASELINE COMPARISON
↓
DEVIATION DETECTION
↓
CLASSIFICATION / CONSEQUENCE
```

## Relationship to Existing Architecture
This document specializes the mandatory post-closure monitoring activation and baseline-control layer beneath transition control and above observation, comparison, deviation detection, revalidation, reacceptance, reliance restoration and regression determination. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, deviation detection, classification, alerting, acknowledgement, response initiation, escalation, authority transfer, response execution, effectiveness, resolution, closure, transition, revalidation, reacceptance, reliance restoration, regression determination or reopening layers.

## Governance-to-Monitoring Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERTING → NOTIFICATION → ACKNOWLEDGEMENT → ASSESSMENT → RESPONSE INITIATION → ESCALATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → CLOSURE → TRANSITION → MANDATORY MONITORING ACTIVATION → BASELINE CONTROL → COMPARISON → DEVIATION DETECTION → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REGRESSION → REOPENING
```

## Complete Monitoring Chain
```text
BASELINE → ACTIVATE MONITORING → OBSERVE → VALIDATE DATA → COMPARE → DETECT DEVIATION → CLASSIFY → DETERMINE CONSEQUENCE → ALERT → NOTIFY → ACKNOWLEDGE → ASSESS → RESPOND → ESCALATE → EXECUTE → DETERMINE EFFECTIVENESS → RESOLVE → CLOSE → TRANSITION → MONITOR → REVALIDATE → REACCEPT → RESTORE RELIANCE → DETECT REGRESSION → REOPEN IF REQUIRED
```

## Next Document
`EA-IMETA-PC-RG-097` — Mandatory Regression Reliance Restoration Monitoring Post-Closure Observation and Measurement Control

## Final Principle
EA-IMETA SHALL REQUIRE POST-CLOSURE MONITORING TO BE EXPLICITLY DEFINED, BASELINED, CONFIGURED, DATA-VALIDATED AND ACTIVATION-VERIFIED BEFORE IT IS CONSIDERED OPERATIONAL, WITH MONITORING GAPS, BASELINE CHANGES AND DEGRADED OBSERVABILITY GOVERNED SO THAT ABSENCE OF OBSERVATION CANNOT BE MISTAKEN FOR EVIDENCE OF STABILITY OR REGRESSION ABSENCE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-MONITORING-ACTIVATION-AND-BASELINE-CONTROL-01

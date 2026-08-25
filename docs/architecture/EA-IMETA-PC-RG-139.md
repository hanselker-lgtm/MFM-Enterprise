# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CLOSURE-DETERMINATION-01

## Physical File ID
`EA-IMETA-PC-RG-139`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-139` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CLOSURE-DETERMINATION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Post-Closure Regression Closure Determination |
| Parent | EA-IMETA-PC-RG-138 — Mandatory Post-Closure Regression Response Resolution Determination |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory closure-determination layer that decides whether a post-closure regression case has satisfied every applicable closure condition, whether all required evidence, accountability, residual-risk treatment, documentation, approvals and follow-up arrangements are complete, and whether the governed response may formally transition from active resolution into controlled post-closure monitoring or another explicitly authorized state.

## Core Principle
Closure is a governed state transition, not an administrative deletion of the case. A regression case shall be closed only when resolution has been verified, all mandatory closure criteria are satisfied, outstanding obligations are dispositioned, residual risk is explicitly accepted or otherwise governed, evidence is complete, accountability is transferred where required, and the conditions for reopening remain defined.

```text
VERIFIED RESOLUTION
        ↓
CLOSURE CRITERIA MET?
├── NO → CONTINUE RESOLUTION / MONITOR / REASSESS
└── YES
     ↓
ALL OBLIGATIONS COMPLETE?
├── NO → COMPLETE / ESCALATE / DISPOSITION
└── YES
     ↓
RESIDUAL RISK GOVERNED?
├── NO → ACCEPT / MITIGATE / ESCALATE
└── YES
     ↓
EVIDENCE / RECORD COMPLETE?
├── NO → COMPLETE RECORD
└── YES
     ↓
ACCOUNTABILITY / HANDOVER COMPLETE?
├── NO → ASSIGN / TRANSFER
└── YES
     ↓
CLOSURE AUTHORIZED
     ↓
CLOSURE VERIFIED
     ↓
POST-CLOSURE MONITORING / REVALIDATION / REOPENING CONDITIONS
```
## Closure Quality Test
```text
VERIFIED RESOLUTION
+
ALL MANDATORY CLOSURE CRITERIA
+
OUTSTANDING OBLIGATIONS DISPOSITIONED
+
RESIDUAL RISK EXPLICITLY GOVERNED
+
EVIDENCE COMPLETE
+
ACCOUNTABILITY / HANDOVER COMPLETE
+
CLOSURE AUTHORIZED
+
CLOSURE VERIFIED
+
REOPENING CONDITIONS DEFINED
=
VALID GOVERNED CLOSURE
```
## Resolution vs Closure vs Post-Closure Monitoring
```text
RESOLUTION
→ UNDERLYING CONDITION IS SUFFICIENTLY RESTORED / CONTROLLED

CLOSURE
→ GOVERNED CASE TRANSITIONS OUT OF ACTIVE RESPONSE / RESOLUTION

POST-CLOSURE MONITORING
→ CLOSED CONDITION REMAINS SUBJECT TO DEFINED OBSERVATION

REOPENING
→ NEW EVIDENCE INVALIDATES OR CHALLENGES THE CLOSED STATE
```
## Closure States
```text
CL0 — CLOSURE NOT REQUIRED
CL1 — CLOSURE ASSESSMENT PENDING
CL2 — CLOSURE ASSESSMENT IN PROGRESS
CL3 — CLOSURE CRITERIA NOT SATISFIED
CL4 — CLOSURE BLOCKED
CL5 — CLOSURE READY
CL6 — CLOSURE AUTHORIZED
CL7 — CLOSURE VERIFIED
CL8 — CLOSURE COMPLETED
CL9 — CLOSURE WITH CONTROLLED RESIDUAL RISK
CL10 — CLOSURE WITH MANDATORY POST-CLOSURE MONITORING
CL11 — CLOSURE WITH REVALIDATION CONDITION
CL12 — CLOSURE WITH REACCEPTANCE CONDITION
CL13 — CLOSURE REJECTED / REASSESSMENT
CL14 — CLOSURE REOPENED
CL15 — CLOSURE SUPERSEDED
CLX — UNKNOWN / INSUFFICIENT BASIS
CLS — CLOSURE ASSESSMENT SUSPENDED
```
## Closure Dimensions
| Dimension | Required determination |
|---|---|
| Regression | Case being closed |
| Resolution | Verified resolution |
| Criteria | Closure requirements |
| Obligations | Outstanding duties |
| Evidence | Complete record |
| Residual Risk | Remaining exposure |
| Acceptance | Required approvals / acceptance |
| Accountability | Current owner |
| Handover | Post-closure owner |
| Monitoring | Required follow-up |
| Revalidation | Future validation |
| Reacceptance | Future acceptance |
| Reopening | Trigger conditions |
| Verification | Closure confirmation |
| Audit Trail | Traceability |

## Closure Invariants

```text
CLOSURE SHALL BE A FORMAL GOVERNED STATE TRANSITION
```

```text
CLOSURE SHALL REQUIRE VERIFIED RESOLUTION OR AN EXPLICITLY GOVERNED ALTERNATIVE CLOSURE BASIS
```

```text
ALL MANDATORY CLOSURE CRITERIA SHALL BE SATISFIED BEFORE NORMAL CLOSURE
```

```text
OUTSTANDING OBLIGATIONS SHALL BE COMPLETED, TRANSFERRED OR EXPLICITLY DISPOSITIONED
```

```text
RESIDUAL MATERIAL RISK SHALL NOT BE HIDDEN BY CLOSURE
```

```text
CLOSURE SHALL PRESERVE COMPLETE EVIDENCE AND AUDITABILITY
```

```text
ACCOUNTABILITY SHALL REMAIN EXPLICIT THROUGH THE CLOSURE TRANSITION
```

```text
POST-CLOSURE MONITORING SHALL BE REQUIRED WHERE DEFINED BY RISK, GOVERNANCE OR STABILITY CONDITIONS
```

```text
REVALIDATION AND REACCEPTANCE CONDITIONS SHALL BE PRESERVED WHERE REQUIRED
```

```text
REOPENING CONDITIONS SHALL BE DEFINED BEFORE CLOSURE
```

```text
CLOSURE SHALL NOT PREVENT REOPENING WHEN NEW EVIDENCE INVALIDATES THE CLOSED STATE
```

```text
SECURITY, RESILIENCE, SAFETY, COMPLIANCE AND DATA CLOSURE SHALL USE DOMAIN-APPROPRIATE CRITERIA
```

```text
AI AND AGENT CLOSURE SHALL INCLUDE CONTROL-BOUNDARY, POLICY, TOOL, DATA AND RECURRENCE CONSIDERATIONS
```

```text
ADMINISTRATIVE COMPLETION SHALL NOT SUBSTITUTE FOR GOVERNED CLOSURE
```

```text
UNVERIFIED CLOSURE SHALL NOT BE RECORDED AS VERIFIED CLOSURE
```

```text
OVERRIDES SHALL BE AUTHORIZED, JUSTIFIED AND TRACEABLE
```

```text
CLOSURE REVIEW SHALL CAPTURE LESSONS FROM FAILED, DELAYED OR REOPENED CASES
```

## 1. Closure Domain — Post-Closure Regression Closure Governance

**Control family:** `PCRC-001`

The Post-Closure Regression Closure Governance domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-001-01` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-001-02` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-001-03` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-001-04` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-001-05` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-001-06` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-001-07` — Establish and maintain the post-closure regression closure governance control.
- `PCRC-001-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 2. Closure Domain — Post-Closure Regression Closure Objective

**Control family:** `PCRC-002`

The Post-Closure Regression Closure Objective domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-002-01` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-002-02` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-002-03` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-002-04` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-002-05` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-002-06` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-002-07` — Establish and maintain the post-closure regression closure objective control.
- `PCRC-002-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 3. Closure Domain — Post-Closure Regression Closure Definition

**Control family:** `PCRC-003`

The Post-Closure Regression Closure Definition domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-003-01` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-003-02` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-003-03` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-003-04` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-003-05` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-003-06` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-003-07` — Establish and maintain the post-closure regression closure definition control.
- `PCRC-003-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 4. Closure Domain — Post-Closure Regression Closure Scope

**Control family:** `PCRC-004`

The Post-Closure Regression Closure Scope domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-004-01` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-004-02` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-004-03` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-004-04` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-004-05` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-004-06` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-004-07` — Establish and maintain the post-closure regression closure scope control.
- `PCRC-004-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 5. Closure Domain — Post-Closure Regression Closure Authority

**Control family:** `PCRC-005`

The Post-Closure Regression Closure Authority domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-005-01` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-005-02` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-005-03` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-005-04` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-005-05` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-005-06` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-005-07` — Establish and maintain the post-closure regression closure authority control.
- `PCRC-005-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 6. Closure Domain — Post-Closure Regression Closure Criteria

**Control family:** `PCRC-006`

The Post-Closure Regression Closure Criteria domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-006-01` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-006-02` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-006-03` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-006-04` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-006-05` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-006-06` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-006-07` — Establish and maintain the post-closure regression closure criteria control.
- `PCRC-006-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 7. Closure Domain — Post-Closure Regression Closure Preconditions

**Control family:** `PCRC-007`

The Post-Closure Regression Closure Preconditions domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-007-01` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-007-02` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-007-03` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-007-04` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-007-05` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-007-06` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-007-07` — Establish and maintain the post-closure regression closure preconditions control.
- `PCRC-007-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 8. Closure Domain — Post-Closure Regression Closure Evidence

**Control family:** `PCRC-008`

The Post-Closure Regression Closure Evidence domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-008-01` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-008-02` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-008-03` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-008-04` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-008-05` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-008-06` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-008-07` — Establish and maintain the post-closure regression closure evidence control.
- `PCRC-008-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 9. Closure Domain — Post-Closure Regression Closure Method

**Control family:** `PCRC-009`

The Post-Closure Regression Closure Method domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-009-01` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-009-02` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-009-03` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-009-04` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-009-05` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-009-06` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-009-07` — Establish and maintain the post-closure regression closure method control.
- `PCRC-009-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 10. Closure Domain — Post-Closure Regression Closure Decision

**Control family:** `PCRC-010`

The Post-Closure Regression Closure Decision domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-010-01` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-010-02` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-010-03` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-010-04` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-010-05` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-010-06` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-010-07` — Establish and maintain the post-closure regression closure decision control.
- `PCRC-010-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 11. Closure Domain — Post-Closure Regression Closure Accountability

**Control family:** `PCRC-011`

The Post-Closure Regression Closure Accountability domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-011-01` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-011-02` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-011-03` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-011-04` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-011-05` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-011-06` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-011-07` — Establish and maintain the post-closure regression closure accountability control.
- `PCRC-011-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 12. Closure Domain — Post-Closure Regression Closure Timing

**Control family:** `PCRC-012`

The Post-Closure Regression Closure Timing domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-012-01` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-012-02` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-012-03` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-012-04` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-012-05` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-012-06` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-012-07` — Establish and maintain the post-closure regression closure timing control.
- `PCRC-012-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 13. Closure Domain — Security Post-Closure Regression Closure

**Control family:** `PCRC-013`

The Security Post-Closure Regression Closure domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-013-01` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-013-02` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-013-03` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-013-04` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-013-05` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-013-06` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-013-07` — Establish and maintain the security post-closure regression closure control.
- `PCRC-013-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 14. Closure Domain — Resilience Post-Closure Regression Closure

**Control family:** `PCRC-014`

The Resilience Post-Closure Regression Closure domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-014-01` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-014-02` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-014-03` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-014-04` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-014-05` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-014-06` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-014-07` — Establish and maintain the resilience post-closure regression closure control.
- `PCRC-014-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 15. Closure Domain — Compliance Post-Closure Regression Closure

**Control family:** `PCRC-015`

The Compliance Post-Closure Regression Closure domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-015-01` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-015-02` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-015-03` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-015-04` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-015-05` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-015-06` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-015-07` — Establish and maintain the compliance post-closure regression closure control.
- `PCRC-015-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 16. Closure Domain — Data Post-Closure Regression Closure

**Control family:** `PCRC-016`

The Data Post-Closure Regression Closure domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-016-01` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-016-02` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-016-03` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-016-04` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-016-05` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-016-06` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-016-07` — Establish and maintain the data post-closure regression closure control.
- `PCRC-016-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 17. Closure Domain — AI and Agent Post-Closure Regression Closure

**Control family:** `PCRC-017`

The AI and Agent Post-Closure Regression Closure domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-017-01` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-017-02` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-017-03` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-017-04` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-017-05` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-017-06` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-017-07` — Establish and maintain the ai and agent post-closure regression closure control.
- `PCRC-017-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 18. Closure Domain — Post-Closure Regression Closure Failure

**Control family:** `PCRC-018`

The Post-Closure Regression Closure Failure domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-018-01` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-018-02` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-018-03` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-018-04` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-018-05` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-018-06` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-018-07` — Establish and maintain the post-closure regression closure failure control.
- `PCRC-018-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 19. Closure Domain — Post-Closure Regression Closure Independence

**Control family:** `PCRC-019`

The Post-Closure Regression Closure Independence domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-019-01` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-019-02` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-019-03` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-019-04` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-019-05` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-019-06` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-019-07` — Establish and maintain the post-closure regression closure independence control.
- `PCRC-019-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## 20. Closure Domain — Post-Closure Regression Closure Review and Learning

**Control family:** `PCRC-020`

The Post-Closure Regression Closure Review and Learning domain establishes governed mandatory closure requirements.

### Required controls
- `PCRC-020-01` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-01-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-020-02` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-02-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-020-03` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-03-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-020-04` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-04-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-020-05` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-05-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-020-06` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-06-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.
- `PCRC-020-07` — Establish and maintain the post-closure regression closure review and learning control.
- `PCRC-020-07-E` — Preserve regression, resolution, criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and verification traceability.

```text
RESOLUTION → CLOSURE CRITERIA → AUTHORIZE → VERIFY → CLOSE → MONITOR / REVALIDATE / REOPEN
```

## Post-Closure Regression Closure Structure

| Element | Required definition |
|---|---|
| Regression | Case being closed |
| Resolution | Verified resolution |
| Closure Criteria | Mandatory requirements |
| Obligations | Remaining duties |
| Evidence | Complete record |
| Residual Risk | Remaining exposure |
| Acceptance | Required acceptance |
| Accountability | Owner |
| Handover | Post-closure responsibility |
| Monitoring | Follow-up |
| Revalidation | Future validation |
| Reacceptance | Future acceptance |
| Reopening | Trigger conditions |
| Verification | Closure confirmation |

## Post-Closure Regression Closure Objective

Formally transition a sufficiently resolved regression case from active governance into the next authorized state while preserving evidence, accountability, residual-risk controls, monitoring and reopening capability.

## Post-Closure Regression Closure Definition

Closure determination is the governed decision that the case satisfies its applicable closure criteria and may leave the active resolution state without loss of required control or traceability.

## Post-Closure Regression Closure Scope

Scope includes closure criteria, obligations, evidence, residual risk, acceptance, accountability, handover, monitoring, revalidation, reacceptance, reopening and closure verification.

## Post-Closure Regression Closure Authority

Authority shall define who may authorize, verify, reject, override, reopen or independently confirm closure.

## Post-Closure Regression Closure Criteria

Criteria shall cover verified resolution, mandatory obligations, evidence completeness, residual risk, acceptance, ownership, monitoring and reopening conditions.
```text
VERIFIED RESOLUTION
↓
CLOSURE CRITERIA
↓
ALL OBLIGATIONS DISPOSITIONED?
├── NO → COMPLETE / TRANSFER / ESCALATE
└── YES
     ↓
RESIDUAL RISK GOVERNED?
├── NO → MITIGATE / ACCEPT / ESCALATE
└── YES
     ↓
EVIDENCE COMPLETE?
├── NO → COMPLETE RECORD
└── YES
     ↓
AUTHORIZE → VERIFY → CLOSE
```

## Post-Closure Regression Closure Preconditions

Preconditions include verified resolution, defined closure criteria, complete evidence, dispositioned obligations and authorized closure authority.

## Post-Closure Regression Closure Evidence

Evidence shall preserve the complete case history, decisions, actions, outcomes, resolution, residual risk, approvals, handover, monitoring and reopening conditions.

## Post-Closure Regression Closure Method

Methods may include formal closure review, checklist validation, evidence reconciliation, residual-risk review, acceptance confirmation and independent assurance.
```text
CASE RECORD
↓
CRITERIA CHECK
↓
OBLIGATION CHECK
↓
RISK CHECK
↓
EVIDENCE CHECK
↓
AUTHORIZATION
↓
VERIFICATION
↓
CLOSURE
```

## Post-Closure Regression Closure Decision

Decision shall determine CL0, CL1, CL2, CL3, CL4, CL5, CL6, CL7, CL8, CL9, CL10, CL11, CL12, CL13, CL14, CL15, CLX or CLS.

## Post-Closure Regression Closure Accountability

Accountability shall remain explicit through authorization, verification, handover and post-closure ownership.

## Post-Closure Regression Closure Timing

Closure shall occur only after applicable criteria are satisfied and shall not be accelerated solely to meet administrative deadlines or reporting targets.

## Security Post-Closure Regression Closure

Security closure shall preserve evidence, access-control decisions, residual exposure, monitoring requirements and reopening triggers.

## Resilience Post-Closure Regression Closure

Resilience closure shall preserve recovery evidence, service stability, dependencies, continuity controls and monitoring requirements.

## Compliance Post-Closure Regression Closure

Compliance closure shall preserve required records, approvals, reporting, evidence retention and residual obligations.

## Data Post-Closure Regression Closure

Data closure shall preserve lineage, integrity, access, retention, evidence and downstream dependency conditions.

## AI and Agent Post-Closure Regression Closure

AI/agent closure shall confirm restored control boundaries, approved policy state, tool permissions, data access, oversight and recurrence controls.
```text
AI / AGENT CASE
↓
RESOLUTION VERIFIED
↓
CONTROL / POLICY / TOOL / DATA STATE VERIFIED
↓
REOPENING CONDITIONS DEFINED
↓
CLOSE
```

## Post-Closure Regression Closure Failure

Failure includes incomplete criteria, missing evidence, unresolved obligations, uncontrolled residual risk, missing acceptance, ambiguous ownership or failed verification.
```text
CLOSURE FAILURE
↓
BLOCK CLOSURE
↓
CORRECT / COMPLETE / ESCALATE
↓
REASSESS
```

## Post-Closure Regression Closure Independence

Independent closure verification shall be required where consequence, governance, safety, security, compliance, public interest or conflict of interest warrants independent assurance.

## Post-Closure Regression Closure Review and Learning

Reviews shall examine premature closure, missing evidence, residual-risk concealment, ownership gaps, weak reopening criteria and reopened cases.

## Closure Decision Model
```text
VERIFIED RESOLUTION
↓
CONFIRM ALL CLOSURE CRITERIA
↓
OUTSTANDING OBLIGATIONS?
├── YES → COMPLETE / TRANSFER / DISPOSITION
└── NO
     ↓
RESIDUAL RISK GOVERNED?
├── NO → MITIGATE / ACCEPT / ESCALATE
└── YES
     ↓
EVIDENCE COMPLETE?
├── NO → COMPLETE RECORD
└── YES
     ↓
ACCOUNTABILITY / HANDOVER COMPLETE?
├── NO → ASSIGN / TRANSFER
└── YES
     ↓
POST-CLOSURE MONITORING REQUIRED?
├── YES → DEFINE MONITORING
└── NO
     ↓
REVALIDATION / REACCEPTANCE REQUIRED?
├── YES → DEFINE CONDITIONS
└── NO
     ↓
DEFINE REOPENING CONDITIONS
↓
AUTHORIZE CLOSURE
↓
VERIFY CLOSURE
↓
CLOSURE ACTIVE
```

## Closure Outcome Matrix
| State | Meaning | Typical treatment |
|---|---|---|
| CL0 | Not required | Record basis |
| CL1 | Assessment pending | Gather evidence |
| CL2 | Assessment in progress | Validate criteria |
| CL3 | Criteria not satisfied | Continue resolution |
| CL4 | Blocked | Correct blocker |
| CL5 | Ready | Prepare authorization |
| CL6 | Authorized | Verify |
| CL7 | Verified | Activate closure |
| CL8 | Completed | Maintain post-closure state |
| CL9 | Controlled residual risk | Maintain controls |
| CL10 | Monitoring required | Activate monitoring |
| CL11 | Revalidation required | Define trigger |
| CL12 | Reacceptance required | Obtain acceptance |
| CL13 | Rejected / reassessment | Correct / review |
| CL14 | Reopened | Return to active governance |
| CL15 | Superseded | Preserve record |
| CLX | Unknown | Do not assume closure |
| CLS | Suspended | Restore assessment |

## Closure Record
| Field | Required |
|---|---|
| Closure ID | Yes |
| Regression ID | Yes |
| Resolution ID | Yes |
| Closure Criteria | Yes |
| Obligations | Yes |
| Evidence | Yes |
| Residual Risk | Yes |
| Acceptance | Yes where required |
| Accountable Owner | Yes |
| Handover Owner | Where applicable |
| Monitoring Requirement | Yes |
| Revalidation Condition | Where applicable |
| Reacceptance Condition | Where applicable |
| Reopening Condition | Yes |
| Authorization | Yes |
| Verification | Yes |
| Closure State | Yes |
| Audit Trail | Yes |

## Closure Is Not Deletion
Closure does not delete the case, evidence or audit history.
```text
CLOSED
≠
DELETED
```

## Closure Is Not Reliance Restoration
A closed case may still require revalidation, reacceptance or controlled restoration of normal reliance.
```text
CLOSED
≠
RELIANCE RESTORED
```

## Closure Is Not Permanent Immunity
A closed case can be reopened if new evidence, recurrence, changed conditions or failed post-closure controls invalidate the closure basis.
```text
CLOSED
↓
NEW EVIDENCE
↓
REASSESS
↓
REOPEN IF CRITERIA MET
```

## Outstanding Obligations
Any remaining obligation must be completed, transferred or explicitly dispositioned before closure. Unowned obligations shall block closure.

## Residual Risk
Residual risk must be explicit, owned and governed. Material uncontrolled residual risk blocks normal closure.

## Post-Closure Monitoring
Where monitoring is required, its objective, owner, duration, triggers and escalation path shall be defined before closure.

## Revalidation
Where the closure basis depends on assumptions or conditions that may change, revalidation triggers shall be defined before closure.

## Reacceptance
Where renewed acceptance is required, the responsible authority and acceptance conditions shall be recorded before closure.

## Reopening
Reopening conditions shall include relevant recurrence, material new evidence, failed monitoring, changed assumptions, material residual-risk change or invalidated closure criteria.

## AI and Agent Closure
AI/agent cases shall retain explicit boundaries for policy, authority, tools, data and human oversight after closure.

## Relationship to Post-Closure Monitoring
RG-139 supplies the verified closure state to the subsequent post-closure monitoring activation layer.
```text
RESOLUTION → CLOSURE → POST-CLOSURE MONITORING
```

## Relationship to Existing Architecture
This document establishes the mandatory post-closure regression closure layer beneath resolution determination and above post-closure monitoring activation. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, verification, evidence, measurement, baseline, comparison, qualification, validation, deviation, regression determination, regression classification, consequence determination, alert determination, notification determination, acknowledgement determination, response initiation, authority transfer, response execution, effectiveness, resolution, monitoring activation, revalidation, reacceptance, reliance restoration or reopening layers.

## Governance-to-Closure Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → ALERT → NOTIFICATION → ACKNOWLEDGEMENT → RESPONSE INITIATION → AUTHORITY TRANSFER → RESPONSE EXECUTION → EFFECTIVENESS → RESOLUTION → MANDATORY CLOSURE DETERMINATION → POST-CLOSURE MONITORING → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → REOPENING
```

## Complete Closure Chain
```text
BASELINE → MONITOR → OBSERVE → MEASURE → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DIFFERENCE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → ISSUE ALERT → DETERMINE NOTIFICATION → ISSUE NOTIFICATION → DELIVER → DETERMINE ACKNOWLEDGEMENT → VALIDATE ACTOR / TIMING / COMPLETENESS → ACKNOWLEDGE → ACCEPT / ASSIGN → DETERMINE RESPONSE INITIATION → AUTHORIZE → ASSIGN → ACTIVATE → VERIFY → DETERMINE AUTHORITY TRANSFER → IDENTIFY RECEIVER → PACKAGE STATE → ACCEPT → VERIFY → ACTIVATE RECEIVING AUTHORITY → DETERMINE EXECUTION → AUTHORIZE ACTION → EXECUTE → OBSERVE → VERIFY → ADJUST / ESCALATE / ROLLBACK / STOP → COMPLETE → DETERMINE EFFECTIVENESS → VERIFY → DETERMINE RESOLUTION → RESTORE / CONTROL CONDITION → VERIFY → DETERMINE CLOSURE → COMPLETE OBLIGATIONS → CONFIRM EVIDENCE / RISK / HANDOVER → AUTHORIZE → VERIFY → CLOSE → ACTIVATE POST-CLOSURE MONITORING → EXECUTE → VALIDATE → QUALIFY → COMPARE → DETERMINE DEVIATION → DETERMINE REGRESSION → CLASSIFY REGRESSION → DETERMINE CONSEQUENCE → DETERMINE ALERT → NOTIFY → ACKNOWLEDGE → INITIATE RESPONSE → TRANSFER AUTHORITY → EXECUTE → VERIFY → EFFECTIVENESS → RESOLUTION → CLOSURE / CONTINUE MONITORING
```

## Next Document
`EA-IMETA-PC-RG-140` — Mandatory Post-Closure Regression Monitoring Activation Determination

## Final Principle
EA-IMETA SHALL REQUIRE EVERY MATERIAL POST-CLOSURE REGRESSION CASE TO REMAIN GOVERNED UNTIL CLOSURE IS EXPLICITLY AUTHORIZED AND VERIFIED AGAINST ALL APPLICABLE CRITERIA, WITH OUTSTANDING OBLIGATIONS DISPOSITIONED, RESIDUAL RISK OWNED AND CONTROLLED, EVIDENCE COMPLETE, ACCOUNTABILITY AND HANDOVER EXPLICIT, AND POST-CLOSURE MONITORING, REVALIDATION, REACCEPTANCE AND REOPENING CONDITIONS DEFINED WHERE REQUIRED, WHILE PRESERVING THE DISTINCTION BETWEEN RESOLUTION, CLOSURE AND RESTORATION OF NORMAL RELIANCE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-POST-CLOSURE-REGRESSION-RESPONSE-POST-CLOSURE-REGRESSION-CLOSURE-DETERMINATION-01

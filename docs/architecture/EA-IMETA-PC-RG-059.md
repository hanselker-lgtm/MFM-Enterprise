# EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-01

## Physical File ID
`EA-IMETA-PC-RG-059`

## Document Registry Entry
| Field | Value |
|---|---|
| Short File ID | `EA-IMETA-PC-RG-059` |
| Full Document ID | `EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-01` |
| Domain | Post-Closure Monitoring / Regression Governance |
| Layer | Mandatory Escalation Resolution |
| Parent | EA-IMETA-PC-RG-058 — Mandatory Alerting Escalation |
| Version | 1.0 |
| Status | Active Architecture Baseline |
| Governing Architecture | EA-IMETA-MASTER-01 |

## Purpose
Establish the authoritative mandatory resolution layer defining how an escalated condition is brought to a controlled and demonstrably acceptable state, how resolution authority is exercised, and how unresolved or failed conditions remain under governed control.

## Core Principle
Escalation establishes that a condition requires broader or stronger authority; resolution establishes that the condition has been controlled, remediated, accepted under explicit conditions, or otherwise brought to a governed end state. Escalation is therefore not resolution.

```text
ESCALATED CONDITION
      ↓
DEFINE RESOLUTION OBJECTIVE
      ↓
CONTAIN / CONTROL / REMEDIATE
      ↓
VERIFY CURRENT STATE
      ↓
RESOLUTION CRITERIA MET?
├── NO → CONTINUE / RE-ESCALATE
├── CONDITIONAL → CONTROL WITH CONDITIONS
└── YES → FORMAL RESOLUTION
             ↓
          VERIFY → REVALIDATE
```

## Resolution Quality Test
```text
ESCALATED CONDITION
+
CURRENT RESOLUTION CRITERIA
+
AUTHORIZED RESOLUTION AUTHORITY
+
SUFFICIENT EVIDENCE
+
CONTROL / REMEDIATION
+
CURRENT-STATE VERIFICATION
+
RESIDUAL-RISK DISPOSITION
=
VALID GOVERNED RESOLUTION
```

## Resolution Status Model
```text
OPEN
CONTAINED
IN REMEDIATION
READY FOR RESOLUTION
RESOLVED
CONDITIONALLY RESOLVED
REJECTED
FAILED
REOPENED
SUPERSEDED
```

## Resolution Invariants

```text
RESOLUTION SHALL BE BASED ON GOVERNED CURRENT CRITERIA
```

```text
CONTAINMENT SHALL NOT BE PRESENTED AS FULL RESOLUTION
```

```text
RESOLUTION AUTHORITY SHALL BE EXPLICIT
```

```text
RESOLUTION SCOPE SHALL REMAIN WITHIN THE ESCALATED CONDITION
```

```text
EVIDENCE SHALL BE SUFFICIENT TO SUPPORT THE DETERMINATION
```

```text
CURRENT STATE SHALL BE VERIFIED WHERE REQUIRED
```

```text
CONDITIONAL RESOLUTION SHALL HAVE EXPLICIT CONDITIONS, OWNERS AND REVIEW POINTS
```

```text
FAILED RESOLUTION SHALL NOT BE TREATED AS RESOLVED
```

```text
UNRESOLVED CONDITIONS SHALL REMAIN UNDER ACTIVE CONTROL OR ESCALATION
```

```text
RESOLUTION SHALL NOT SILENTLY REMOVE RESTRICTIONS OR RISK CONTROLS
```

```text
SECURITY, RESILIENCE, SAFETY AND COMPLIANCE RESOLUTION SHALL RECEIVE APPROPRIATE RIGOR
```

```text
AI AND AGENT RESOLUTION SHALL ADDRESS AUTHORITY, POLICY, TOOLS, DATA, AUTONOMY AND BEHAVIOURAL CONDITIONS
```

```text
RESOLUTION SHALL REMAIN TRACEABLE TO THE ORIGINAL ALERT AND ESCALATION
```

```text
RESOLUTION SHALL FEED VERIFICATION, REVALIDATION AND REACCEPTANCE AS REQUIRED
```

```text
REPEATED RESOLUTION FAILURE SHALL TRIGGER GOVERNANCE REVIEW
```

## 1. Resolution Domain — Escalation Resolution Governance

**Control family:** `PCRS-001`

The Escalation Resolution Governance domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-001-01` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-001-02` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-001-03` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-001-04` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-001-05` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-001-06` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-001-07` — Establish and maintain the escalation resolution governance control.
- `PCRS-001-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 2. Resolution Domain — Escalation Resolution Objective

**Control family:** `PCRS-002`

The Escalation Resolution Objective domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-002-01` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-002-02` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-002-03` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-002-04` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-002-05` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-002-06` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-002-07` — Establish and maintain the escalation resolution objective control.
- `PCRS-002-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 3. Resolution Domain — Escalation Resolution Definition

**Control family:** `PCRS-003`

The Escalation Resolution Definition domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-003-01` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-003-02` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-003-03` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-003-04` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-003-05` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-003-06` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-003-07` — Establish and maintain the escalation resolution definition control.
- `PCRS-003-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 4. Resolution Domain — Escalation Resolution Scope

**Control family:** `PCRS-004`

The Escalation Resolution Scope domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-004-01` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-004-02` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-004-03` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-004-04` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-004-05` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-004-06` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-004-07` — Establish and maintain the escalation resolution scope control.
- `PCRS-004-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 5. Resolution Domain — Escalation Resolution Authority

**Control family:** `PCRS-005`

The Escalation Resolution Authority domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-005-01` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-005-02` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-005-03` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-005-04` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-005-05` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-005-06` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-005-07` — Establish and maintain the escalation resolution authority control.
- `PCRS-005-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 6. Resolution Domain — Escalation Resolution Criteria

**Control family:** `PCRS-006`

The Escalation Resolution Criteria domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-006-01` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-006-02` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-006-03` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-006-04` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-006-05` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-006-06` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-006-07` — Establish and maintain the escalation resolution criteria control.
- `PCRS-006-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 7. Resolution Domain — Escalation Resolution Preconditions

**Control family:** `PCRS-007`

The Escalation Resolution Preconditions domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-007-01` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-007-02` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-007-03` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-007-04` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-007-05` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-007-06` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-007-07` — Establish and maintain the escalation resolution preconditions control.
- `PCRS-007-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 8. Resolution Domain — Escalation Resolution Evidence

**Control family:** `PCRS-008`

The Escalation Resolution Evidence domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-008-01` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-008-02` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-008-03` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-008-04` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-008-05` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-008-06` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-008-07` — Establish and maintain the escalation resolution evidence control.
- `PCRS-008-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 9. Resolution Domain — Escalation Resolution Method

**Control family:** `PCRS-009`

The Escalation Resolution Method domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-009-01` — Establish and maintain the escalation resolution method control.
- `PCRS-009-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-009-02` — Establish and maintain the escalation resolution method control.
- `PCRS-009-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-009-03` — Establish and maintain the escalation resolution method control.
- `PCRS-009-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-009-04` — Establish and maintain the escalation resolution method control.
- `PCRS-009-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-009-05` — Establish and maintain the escalation resolution method control.
- `PCRS-009-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-009-06` — Establish and maintain the escalation resolution method control.
- `PCRS-009-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-009-07` — Establish and maintain the escalation resolution method control.
- `PCRS-009-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 10. Resolution Domain — Escalation Resolution Decision

**Control family:** `PCRS-010`

The Escalation Resolution Decision domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-010-01` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-010-02` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-010-03` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-010-04` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-010-05` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-010-06` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-010-07` — Establish and maintain the escalation resolution decision control.
- `PCRS-010-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 11. Resolution Domain — Escalation Resolution Accountability

**Control family:** `PCRS-011`

The Escalation Resolution Accountability domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-011-01` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-011-02` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-011-03` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-011-04` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-011-05` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-011-06` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-011-07` — Establish and maintain the escalation resolution accountability control.
- `PCRS-011-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 12. Resolution Domain — Escalation Resolution Timing

**Control family:** `PCRS-012`

The Escalation Resolution Timing domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-012-01` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-012-02` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-012-03` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-012-04` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-012-05` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-012-06` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-012-07` — Establish and maintain the escalation resolution timing control.
- `PCRS-012-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 13. Resolution Domain — Security Escalation Resolution

**Control family:** `PCRS-013`

The Security Escalation Resolution domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-013-01` — Establish and maintain the security escalation resolution control.
- `PCRS-013-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-013-02` — Establish and maintain the security escalation resolution control.
- `PCRS-013-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-013-03` — Establish and maintain the security escalation resolution control.
- `PCRS-013-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-013-04` — Establish and maintain the security escalation resolution control.
- `PCRS-013-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-013-05` — Establish and maintain the security escalation resolution control.
- `PCRS-013-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-013-06` — Establish and maintain the security escalation resolution control.
- `PCRS-013-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-013-07` — Establish and maintain the security escalation resolution control.
- `PCRS-013-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 14. Resolution Domain — Resilience Escalation Resolution

**Control family:** `PCRS-014`

The Resilience Escalation Resolution domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-014-01` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-014-02` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-014-03` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-014-04` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-014-05` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-014-06` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-014-07` — Establish and maintain the resilience escalation resolution control.
- `PCRS-014-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 15. Resolution Domain — Compliance Escalation Resolution

**Control family:** `PCRS-015`

The Compliance Escalation Resolution domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-015-01` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-015-02` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-015-03` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-015-04` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-015-05` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-015-06` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-015-07` — Establish and maintain the compliance escalation resolution control.
- `PCRS-015-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 16. Resolution Domain — Data Escalation Resolution

**Control family:** `PCRS-016`

The Data Escalation Resolution domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-016-01` — Establish and maintain the data escalation resolution control.
- `PCRS-016-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-016-02` — Establish and maintain the data escalation resolution control.
- `PCRS-016-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-016-03` — Establish and maintain the data escalation resolution control.
- `PCRS-016-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-016-04` — Establish and maintain the data escalation resolution control.
- `PCRS-016-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-016-05` — Establish and maintain the data escalation resolution control.
- `PCRS-016-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-016-06` — Establish and maintain the data escalation resolution control.
- `PCRS-016-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-016-07` — Establish and maintain the data escalation resolution control.
- `PCRS-016-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 17. Resolution Domain — AI and Agent Escalation Resolution

**Control family:** `PCRS-017`

The AI and Agent Escalation Resolution domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-017-01` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-017-02` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-017-03` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-017-04` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-017-05` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-017-06` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-017-07` — Establish and maintain the ai and agent escalation resolution control.
- `PCRS-017-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 18. Resolution Domain — Escalation Resolution Failure

**Control family:** `PCRS-018`

The Escalation Resolution Failure domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-018-01` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-018-02` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-018-03` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-018-04` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-018-05` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-018-06` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-018-07` — Establish and maintain the escalation resolution failure control.
- `PCRS-018-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 19. Resolution Domain — Escalation Resolution Independence

**Control family:** `PCRS-019`

The Escalation Resolution Independence domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-019-01` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-019-02` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-019-03` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-019-04` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-019-05` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-019-06` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-019-07` — Establish and maintain the escalation resolution independence control.
- `PCRS-019-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## 20. Resolution Domain — Escalation Resolution Review and Learning

**Control family:** `PCRS-020`

The Escalation Resolution Review and Learning domain establishes governed mandatory resolution requirements.

### Required controls
- `PCRS-020-01` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-01-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-020-02` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-02-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-020-03` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-03-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-020-04` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-04-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-020-05` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-05-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-020-06` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-06-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.
- `PCRS-020-07` — Establish and maintain the escalation resolution review and learning control.
- `PCRS-020-07-E` — Preserve escalation basis, resolution objective, criteria, authority, evidence, determination and follow-on traceability.

```text
ESCALATE → RESOLVE → VERIFY
```

## Escalation Resolution Structure

| Element | Required definition |
|---|---|
| Escalated Condition | Material condition under escalation |
| Resolution Objective | Required controlled end state |
| Criteria | Current resolution requirements |
| Authority | Authorized resolution decision-maker |
| Evidence | Basis for determination |
| Determination | Resolution outcome |
| Follow-on | Verification / revalidation / reacceptance |

## Escalation Resolution Objective

Bring the escalated condition to a controlled end state that satisfies current criteria and has sufficient evidence for progression.

## Escalation Resolution Definition

Resolution is the governed determination that an escalated condition has reached the required controlled state, either fully or under explicit authorized conditions.

## Escalation Resolution Scope

Scope shall identify affected systems, services, users, data, decisions, dependencies, environments and boundaries covered by the resolution.

## Escalation Resolution Authority

Authority shall define who may approve resolution, who may reject it, who may impose conditions and who may require renewed escalation.

## Escalation Resolution Criteria

Criteria shall distinguish contained, resolved, conditionally resolved, failed and reopened states.

```text
ESCALATED
↓
OBJECTIVE + CRITERIA DEFINED?
├── NO → GOVERNANCE GAP
└── YES
     ↓
CONTROL / REMEDIATION COMPLETE?
├── NO → CONTINUE
└── YES
     ↓
CURRENT STATE VERIFIED?
├── NO → VERIFY
└── YES
     ↓
RESIDUAL RISK ACCEPTABLE?
├── NO → RESTRICT / ESCALATE
└── YES → RESOLVE
```

## Escalation Resolution Preconditions

Preconditions include defined objective, current criteria, authority, scope, remediation status, evidence and required verification method.

## Escalation Resolution Evidence

Evidence shall preserve the original condition, actions taken, current state, criteria, tests, observations, residual risk and resolution decision.

## Escalation Resolution Method

Methods may include containment, remediation, corrective action, compensating control, controlled exception and formal decision.

```text
ESCALATED CONDITION
↓
CONTAIN
↓
REMEDIATE / CONTROL
↓
VERIFY
↓
FORMAL RESOLUTION
```

## Escalation Resolution Decision

Decisions shall distinguish unresolved, contained, resolved, conditional, failed and reopened states.

```text
CONTAINED → CONTINUE CONTROL
RESOLVED → VERIFY / REVALIDATE
CONDITIONAL → MONITOR CONDITIONS
FAILED → REOPEN / ESCALATE
REOPENED → NEW CONTROL CYCLE
```

## Escalation Resolution Accountability

Accountability shall remain explicit for remediation, evidence, decision, conditions, residual risk and follow-on verification.

## Escalation Resolution Timing

Resolution timing shall reflect materiality, time-to-impact, containment needs and dependencies. Delay shall not imply resolution.

## Security Escalation Resolution

Resolve security conditions through validated containment, remediation, control restoration and residual-risk disposition.

## Resilience Escalation Resolution

Resolve resilience conditions through restoration of service capability, recovery readiness, continuity and dependency stability.

## Compliance Escalation Resolution

Resolve compliance conditions through corrective action, evidence completion, obligation satisfaction and authorized disposition.

## Data Escalation Resolution

Resolve data conditions through integrity restoration, access correction, quality remediation, lineage confirmation and authorized-use controls.

## AI and Agent Escalation Resolution

Resolve AI/agent conditions through control of authority, policy, tools, data, autonomy, behaviour and affected outcomes.

```text
AI / AGENT ESCALATION
↓
LIMIT / CONTAIN
↓
CORRECT POLICY / AUTHORITY / TOOLS / DATA / BEHAVIOUR
↓
VERIFY
↓
RESOLVE OR RESTRICT
```

## Escalation Resolution Failure

Failure includes unmet criteria, insufficient evidence, recurring condition, ineffective remediation or inability to establish a controlled state.

```text
RESOLUTION FAILURE
↓
NO FALSE CLOSURE
↓
CONTINUE CONTROL
↓
REMEDIATE / RE-ESCALATE
↓
VERIFY AGAIN
```

## Escalation Resolution Independence

Where materiality requires it, resolution shall receive independent challenge or verification separate from the remediation role.

## Escalation Resolution Review and Learning

Reviews shall identify recurring resolution failure, weak remediation, insufficient criteria, authority gaps and opportunities to improve escalation governance.

## Resolution Determination Model
```text
ESCALATED CONDITION
↓
OBJECTIVE + CRITERIA CURRENT?
├── NO → GOVERNANCE GAP
└── YES
     ↓
CONTAINED / CONTROLLED?
├── NO → CONTINUE / PROTECT
└── YES
     ↓
EVIDENCE SUFFICIENT?
├── NO → COMPLETE EVIDENCE
└── YES
     ↓
CURRENT STATE VERIFIED?
├── NO → VERIFY
└── YES
     ↓
RESIDUAL RISK ACCEPTABLE?
├── NO → RESTRICT / ESCALATE
└── YES → RESOLVED
```

## Resolution Outcome Matrix
| Outcome | Meaning | Required treatment |
|---|---|---|
| Open | Condition remains active | Continue control |
| Contained | Impact limited but condition remains | Continue remediation |
| Resolved | Required controlled state established | Verify / revalidate |
| Conditionally Resolved | Controlled under explicit conditions | Monitor conditions |
| Failed | Resolution criteria not met | Reopen / remediate |
| Reopened | Prior resolution invalidated | New control cycle |

## Resolution Record
| Field | Required |
|---|---|
| Resolution ID | Yes |
| Escalation ID | Yes |
| Objective | Yes |
| Scope | Yes |
| Criteria Version | Yes |
| Authority | Yes |
| Evidence | Yes |
| Current-State Verification | Where required |
| Residual Risk | Yes |
| Conditions | Where applicable |
| Decision | Yes |
| Follow-on | Yes |

## Containment vs Resolution
```text
CONTAINMENT = LIMIT IMPACT
RESOLUTION   = ESTABLISH REQUIRED CONTROLLED STATE
```
Containment may remain active while remediation and verification continue. It shall not be represented as full resolution unless current criteria explicitly define containment as the accepted end state.

## Conditional Resolution
Conditional resolution shall define condition, owner, monitoring method, review point, expiry or renewal rule and consequence of breach.

```text
CONDITIONAL RESOLUTION
↓
DEFINE CONDITION
↓
ASSIGN OWNER
↓
MONITOR
↓
REVIEW
↓
BREACH?
├── NO → CONTINUE
└── YES → REOPEN / ESCALATE
```

## Resolution Reopening
A resolved condition shall be reopened when material invalidating evidence, recurrence, boundary breach or failure of a resolution condition demonstrates that the required state no longer exists.

```text
RESOLVED
↓
INVALIDATING EVIDENCE?
├── NO → CONTINUE
└── YES → REOPEN → RE-ESCALATE / REMEDIATE
```

## Root Cause and Recurrence
Where recurrence risk is material, resolution shall address root cause or establish an explicit governed compensating control with documented residual risk.

## Resolution Change Control
Changes to criteria, authority, scope, conditions, methods or evidence requirements shall be governed, approved, versioned and effective-dated.

```text
CURRENT RESOLUTION MODEL
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

## Resolution Anti-Gaming Control
Resolution shall not be granted merely to close a ticket, remove an escalation, restore metrics or reduce visible governance activity. The actual controlled state remains the governing basis.

Historical resolution records, remediation evidence, conditions, failures, reopenings, residual-risk decisions and follow-on verification shall remain preserved according to applicable retention and governance requirements.

## Relationship to Existing Architecture
This document specializes the mandatory escalation-resolution layer beneath escalation and above verification. It does not replace governance, authority, mandate, role, responsibility, accountability, outcome, criteria, success, success conditions, mandatory conditions, non-negotiable requirements, applicability, state, evidence, measurement, threshold, classification, consequence, response, effectiveness, reassessment, revalidation, reacceptance, reliance restoration, monitoring, alerting, closure, post-closure monitoring or regression detection layers.

## Governance-to-Resolution Chain
```text
GOVERNANCE → AUTHORITY → MANDATE → ROLE → RESPONSIBILITY → ACCOUNTABILITY → OUTCOME → CRITERIA → SUCCESS → SUCCESS CONDITIONS → MANDATORY CONDITIONS → NON-NEGOTIABLE REQUIREMENTS → APPLICABILITY → MANDATORY STATE → VERIFICATION → EVIDENCE → MEASUREMENT → THRESHOLD → CLASSIFICATION → CONSEQUENCE → RESPONSE → EFFECTIVENESS → REASSESSMENT → REVALIDATION → REACCEPTANCE → RELIANCE RESTORATION → MONITORING → ALERTING → ESCALATION → MANDATORY RESOLUTION
```

## Complete Resolution Chain
```text
RESTORE RELIANCE → MONITOR → ALERT → ESCALATE → CONTROL / REMEDIATE → RESOLVE → VERIFY → REVALIDATE → REACCEPT IF REQUIRED → MONITOR
```

## Next Document
`EA-IMETA-PC-RG-060` — Mandatory Regression Reliance Monitoring Alerting Escalation Resolution Verification

## Final Principle
EA-IMETA SHALL REQUIRE ESCALATED CONDITIONS TO REACH A GOVERNED AND EVIDENCE-SUPPORTED CONTROLLED STATE BEFORE THEY ARE TREATED AS RESOLVED, WITH EXPLICIT OBJECTIVES, CURRENT CRITERIA, AUTHORIZED DECISION RIGHTS, CONTINUOUS ACCOUNTABILITY, RESIDUAL-RISK DISPOSITION, CONDITIONAL CONTROLS, REOPENING CAPABILITY AND TRACEABLE FOLLOW-ON VERIFICATION SO THAT ESCALATION NEVER BECOMES FALSE CLOSURE.
# END OF EA-IMETA-POST-CLOSURE-MONITORING-REGRESSION-GOVERNANCE-AUTHORITY-MANDATE-ROLE-RESPONSIBILITY-ACCOUNTABILITY-OUTCOME-CRITERIA-SUCCESS-CONDITIONS-MANDATORY-APPLICABILITY-MANDATORY-STATE-MANDATORY-VERIFICATION-MANDATORY-EVIDENCE-MANDATORY-MEASUREMENT-MANDATORY-THRESHOLDS-MANDATORY-CLASSIFICATION-MANDATORY-CONSEQUENCE-MANDATORY-RESPONSE-MANDATORY-EFFECTIVENESS-MANDATORY-REASSESSMENT-MANDATORY-REVALIDATION-MANDATORY-REACCEPTANCE-MANDATORY-RELIANCE-RESTORATION-MANDATORY-MONITORING-MANDATORY-ALERTING-MANDATORY-ESCALATION-MANDATORY-RESOLUTION-01

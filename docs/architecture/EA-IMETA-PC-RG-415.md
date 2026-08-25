# EA-IMETA-PC-RG-415

## RISK, MATERIALITY & ESCALATION MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-415 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Risk, Materiality & Escalation Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-414 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how risk, impact, materiality, tolerance and escalation determine proportional PC-RG responses |
| Architectural Boundary | Hazard → Risk → Impact → Materiality → Response → Escalation → Decision |

---

# 2. Purpose

EA-IMETA-PC-RG-415 defines the risk and materiality model used by PC-RG.

RG-414 established policy and decision logic.

RG-415 determines **how significant a deviation is and what response it requires**.

The governing distinction is:

```text
RISK
= POSSIBILITY OF HARM / LOSS / FAILURE

IMPACT
= CONSEQUENCE IF IT OCCURS

MATERIALITY
= WHETHER THE EFFECT IS SIGNIFICANT ENOUGH TO CHANGE GOVERNANCE RESPONSE

TOLERANCE
= ACCEPTABLE LIMIT

ESCALATION
= REQUIRED CHANGE IN GOVERNANCE RESPONSE
```

---

# 3. Core Principle

> **Not every deviation is a regression, and not every regression requires the same response.**

The architecture SHALL therefore distinguish:

```text
OBSERVATION
   ↓
DEVIATION
   ↓
IMPACT ASSESSMENT
   ↓
MATERIALITY
   ↓
RISK
   ↓
RESPONSE
```

---

# 4. Risk Object

Every material risk SHALL be represented as a controlled object.

Minimum attributes:

```text
Risk ID
Case ID
Description
Source
Cause
Event
Consequence
Likelihood
Impact
Existing Controls
Residual Risk
Owner
Status
Review Date
Version
```

---

# 5. Risk Categories

Initial catalogue:

```text
OPERATIONAL
TECHNICAL
SECURITY
COMPLIANCE
FINANCIAL
DATA
REPUTATIONAL
SAFETY
AVAILABILITY
INTEGRITY
CONFIDENTIALITY
AUTHORITY
GOVERNANCE
AI / AGENT
SUPPLIER / DEPENDENCY
```

Additional categories may be introduced through controlled governance.

---

# 6. Risk Chain

A risk SHALL be understandable as:

```text
SOURCE / HAZARD
      ↓
THREAT / EVENT
      ↓
VULNERABILITY
      ↓
CONSEQUENCE
      ↓
IMPACT
      ↓
RISK
```

Controls may interrupt the chain.

---

# 7. Inherent Risk

Inherent risk represents risk before considering existing controls.

```text
INHERENT RISK
=
LIKELIHOOD × IMPACT
```

The exact methodology SHALL be defined by the applicable risk policy.

---

# 8. Residual Risk

Residual risk represents risk after controls.

```text
INHERENT RISK
      ↓
CONTROLS
      ↓
RESIDUAL RISK
```

Residual risk SHALL be the principal risk value used for acceptance decisions unless policy states otherwise.

---

# 9. Likelihood

Likelihood SHALL use a controlled scale.

Illustrative:

| Level | Description |
|---|---|
| 1 | Rare |
| 2 | Unlikely |
| 3 | Possible |
| 4 | Likely |
| 5 | Almost Certain |

The definitions SHALL be measurable enough to support consistent use.

---

# 10. Impact

Impact SHALL consider applicable consequence dimensions.

Examples:

```text
Safety
Financial
Operational
Security
Compliance
Data
Reputation
Service Availability
Decision Integrity
```

A single composite score SHALL not hide critical dimensions where policy requires separate treatment.

---

# 11. Impact Scale

Illustrative:

| Level | Description |
|---|---|
| 1 | Negligible |
| 2 | Minor |
| 3 | Moderate |
| 4 | Major |
| 5 | Severe / Critical |

Actual thresholds SHALL be approved through policy governance.

---

# 12. Risk Rating

A basic model MAY be:

```text
RISK SCORE = LIKELIHOOD × IMPACT
```

Example:

```text
Likelihood = 4
Impact = 5

Risk Score = 20
```

The score SHALL be interpreted through an approved risk matrix rather than treated as self-explanatory.

---

# 13. Risk Matrix

Illustrative:

```text
              IMPACT
          1    2    3    4    5

L 1       1    2    3    4    5
I 2       2    4    6    8   10
K 3       3    6    9   12   15
E 4       4    8   12   16   20
L 5       5   10   15   20   25
```

The matrix is an illustrative baseline only.

---

# 14. Risk Bands

A controlled risk model MAY classify results as:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Each band SHALL have defined governance consequences.

---

# 15. Risk Tolerance

Risk tolerance defines the maximum acceptable residual risk under a policy.

```text
RESIDUAL RISK
      ↓
COMPARE TOLERANCE
      ↓
ACCEPTABLE / NOT ACCEPTABLE
```

Tolerance may differ by:

```text
Risk Type
Case Type
Business Function
Decision Type
Regulatory Context
```

---

# 16. Risk Appetite vs Tolerance

The architecture SHALL distinguish:

```text
RISK APPETITE
= strategic willingness to accept risk

RISK TOLERANCE
= operational boundary for a specific condition
```

A general appetite statement SHALL not override a mandatory tolerance.

---

# 17. Materiality

Materiality determines whether a deviation requires a change in lifecycle treatment.

A deviation MAY be material because of:

```text
Magnitude
Duration
Frequency
Scope
Risk
Compliance
Security
Control Failure
Decision Impact
Evidence Invalidation
Authority Loss
Cumulative Effect
```

---

# 18. Materiality Dimensions

Materiality SHOULD consider:

```text
QUANTITATIVE
QUALITATIVE
TEMPORAL
SCOPE
RISK
DEPENDENCY
GOVERNANCE
```

A small numerical change may still be materially significant if it affects a critical control.

---

# 19. Quantitative Materiality

Where measurable:

```text
ABSOLUTE DEVIATION
PERCENTAGE DEVIATION
TREND
RATE
DURATION
FREQUENCY
```

shall be considered.

The selected metric SHALL be documented.

---

# 20. Qualitative Materiality

A deviation may be material even without a large numerical difference.

Examples:

```text
Loss of required approval
Security control disabled
Critical evidence invalid
Mandatory criterion breached
Segregation of duties broken
Regulatory obligation affected
Decision authority compromised
```

---

# 21. Cumulative Materiality

Repeated small deviations MAY become material.

```text
Deviation 1
   +
Deviation 2
   +
Deviation 3
   ↓
CUMULATIVE IMPACT
   ↓
MATERIAL
```

Monitoring SHALL support aggregation where required.

---

# 22. Duration Materiality

A deviation that persists may become material.

Example:

```text
SHORT INTERRUPTION
→ monitor

PROLONGED INTERRUPTION
→ escalation

CRITICAL DURATION
→ suspension / regression
```

Duration thresholds SHALL be policy-controlled.

---

# 23. Scope Materiality

The same deviation may have different significance depending on scope.

```text
ONE NON-CRITICAL CASE
```

may differ from:

```text
SYSTEM-WIDE CONDITION
```

Materiality rules SHALL consider affected population.

---

# 24. Dependency Materiality

A failure of a dependency may become material even if the local system appears operational.

Examples:

```text
Identity Provider Failure
Evidence Repository Failure
External Data Feed Failure
Critical Service Failure
Authority Service Failure
Audit Service Failure
```

---

# 25. Control Failure Materiality

A control failure SHALL be assessed independently from the observed business result.

A control that currently appears not to have caused harm may still require escalation if it compromises future assurance.

---

# 26. Evidence Materiality

Evidence may be materially affected by:

```text
Invalid Source
Expired Evidence
Integrity Failure
Missing Chain of Custody
Conflicting Evidence
Unknown Origin
Unauthorised Modification
```

Material evidence failure may invalidate a previously supported decision.

---

# 27. Decision Materiality

A deviation is material if it could reasonably alter a governed decision.

Examples:

```text
Acceptance Outcome
Closure Outcome
Reliance
Risk Classification
Compliance Status
Security Status
```

---

# 28. Materiality Decision

Conceptual logic:

```text
DEVIATION
   ↓
QUANTITATIVE CHECK
   +
QUALITATIVE CHECK
   +
RISK CHECK
   +
CONTROL CHECK
   +
SCOPE CHECK
   +
DURATION CHECK
   ↓
MATERIALITY RESULT
```

Possible results:

```text
NOT MATERIAL
POTENTIALLY MATERIAL
MATERIAL
CRITICAL
INCONCLUSIVE
```

---

# 29. Materiality Review

Potentially material findings SHALL receive appropriate review.

```text
POTENTIALLY MATERIAL
        ↓
QUALIFIED REVIEW
        ↓
MATERIALITY DECISION
```

The reviewer and authority SHALL be defined by policy.

---

# 30. Escalation

Escalation is a controlled increase in governance response.

It may change:

```text
Priority
Owner
Authority
Review Level
Frequency
Controls
State
Reporting
Decision Rights
```

---

# 31. Escalation Levels

Illustrative:

```text
LEVEL 0 — NORMAL
LEVEL 1 — WATCH
LEVEL 2 — MANAGEMENT ACTION
LEVEL 3 — FORMAL GOVERNANCE REVIEW
LEVEL 4 — CRITICAL / EXECUTIVE ESCALATION
LEVEL 5 — SUSPENSION / REVOCATION
```

The exact levels SHALL be configured by applicable governance policy.

---

# 32. Escalation Triggers

Triggers MAY include:

```text
Risk Above Tolerance
Critical Control Failure
Material Regression
Repeated SLA Breach
Evidence Invalidity
Security Incident
Compliance Breach
Authority Failure
Unresolved Conflict
Critical Dependency Failure
Repeated Remediation Failure
```

---

# 33. Escalation Routing

Every escalation rule SHALL identify:

```text
Trigger
Recipient
Authority
Time Limit
Required Action
Evidence
Outcome
```

---

# 34. Escalation Timing

Escalation SHALL be time-aware.

Example:

```text
Finding Raised
   ↓
T+0 Owner Assigned
   ↓
T+24 Warning
   ↓
T+48 Management Escalation
   ↓
T+72 Critical Review
```

Actual timings SHALL be policy-defined.

---

# 35. Automatic Escalation

Automatic escalation MAY be used for deterministic conditions.

Examples:

```text
Critical threshold breached
Required evidence expired
Remediation overdue
Authority expired
Security control disabled
```

Automation SHALL create an auditable event.

---

# 36. Human Escalation

Some situations require human judgement.

Examples:

```text
Conflicting Evidence
Ambiguous Materiality
Novel Risk
Policy Conflict
Unclear Authority
Unexpected AI Behaviour
```

The system SHALL route such cases to the defined decision authority.

---

# 37. Escalation and State

Escalation may cause a state transition.

Example:

```text
MONITORED
   ↓
CRITICAL REGRESSION
   ↓
SUSPENDED
```

However:

```text
ESCALATION
```

does not automatically equal:

```text
STATE TRANSITION
```

unless the state policy explicitly defines it.

---

# 38. Risk-Based State Control

The state machine SHOULD consume risk outcomes where appropriate.

Example:

```text
Residual Risk > Acceptance Tolerance
        ↓
ACCEPTANCE BLOCKED
```

and:

```text
Material Risk Increase
        ↓
REGRESSION / SUSPENSION
```

---

# 39. Risk Treatment

Risk responses SHALL include:

```text
ACCEPT
REDUCE
TRANSFER
AVOID
MONITOR
ESCALATE
SUSPEND
REVOKE
```

The selected treatment SHALL be authorised.

---

# 40. Risk Acceptance

Risk acceptance SHALL be explicit.

It SHALL record:

```text
Risk
Residual Rating
Tolerance
Decision
Authority
Conditions
Expiry
Evidence
Rationale
```

Acceptance of risk SHALL not automatically equal acceptance of the governed case.

---

# 41. Residual Risk Conditions

Conditional risk acceptance SHALL define:

```text
Condition
Owner
Due Date
Monitoring
Evidence
Consequence
Review
```

Expired conditions SHALL trigger reassessment.

---

# 42. Risk Concentration

The system SHOULD detect concentrations such as:

```text
Many cases affected by one dependency
Many findings owned by one control
Multiple regressions from one source
Repeated failures in one workflow
```

Concentration may increase materiality.

---

# 43. Risk Correlation

Independent-looking risks may share a common cause.

Example:

```text
Risk A
Risk B
Risk C
   ↓
COMMON DEPENDENCY
```

The architecture SHOULD support correlation analysis.

---

# 44. Systemic Risk

Systemic risk exists when a condition can affect a broad population or critical architecture component.

Examples:

```text
Common Identity Service
Common Evidence Store
Common Rule Engine
Common AI Model
Common Integration
```

Systemic risk SHALL receive enhanced escalation.

---

# 45. Third-Party Risk

Third-party dependencies SHALL be evaluated for:

```text
Availability
Security
Integrity
Compliance
Continuity
Change Management
Concentration
```

Material third-party failures SHALL trigger defined response.

---

# 46. AI / Agent Risk

AI/agent risks SHALL include:

```text
Incorrect Output
Hallucination
Bias / Inconsistent Classification
Tool Misuse
Permission Escalation
Data Leakage
Model Drift
Prompt Manipulation
Uncontrolled Automation
Non-Reproducibility
```

AI risk SHALL be evaluated according to actual use and impact.

---

# 47. Model Change Risk

A model/version change may be material even if application code has not changed.

```text
MODEL v1
   ↓
MODEL v2
   ↓
BEHAVIOUR CHANGE?
   ↓
IMPACT ASSESSMENT
```

Material changes SHALL trigger applicable regression or revalidation.

---

# 48. Risk Scoring Governance

Risk scores SHALL not be treated as objective facts.

They are governed assessments.

The system SHALL retain:

```text
Method
Inputs
Scale
Version
Assessor
Timestamp
Rationale
```

---

# 49. Uncertainty

Where risk cannot be reliably quantified:

```text
UNKNOWN
```

shall remain distinct from:

```text
LOW
```

Uncertainty may itself increase escalation requirements.

---

# 50. Worst-Case Consideration

For critical risks, the assessment SHOULD consider credible worst-case outcomes.

This prevents average-case assumptions from masking severe consequences.

---

# 51. Risk Overrides

Risk ratings MAY be overridden only under controlled authority.

An override SHALL record:

```text
Calculated Rating
Override Rating
Reason
Authority
Evidence
Expiry / Review
```

---

# 52. Materiality Overrides

Materiality overrides SHALL be exceptional.

An override SHALL not modify the underlying observation.

It changes the governed interpretation and must be auditable.

---

# 53. Risk / Rule Engine Relationship

RG-414 policy/rule logic SHALL consume risk outputs.

```text
RISK ENGINE
    ↓
RISK RESULT
    ↓
POLICY / RULE ENGINE
    ↓
DECISION
    ↓
STATE MACHINE
```

The risk engine SHALL not independently change lifecycle state.

---

# 54. Evidence Requirements

Risk and materiality assessments SHALL link evidence for:

```text
Observation
Likelihood
Impact
Controls
Residual Risk
Materiality
Decision
```

---

# 55. Audit Requirements

Every material risk decision SHALL be auditable.

Required:

```text
Risk ID
Assessment
Inputs
Method
Policy Version
Risk Version
Authority
Decision
Timestamp
Evidence
```

---

# 56. Risk Review Cycle

Risk SHALL be reviewed:

```text
On Schedule
On Material Change
On Regression
On Control Failure
On Incident
On Evidence Invalidation
On Authority Change
On Dependency Change
```

---

# 57. Reassessment

Risk reassessment SHALL preserve history.

```text
Risk v1
   ↓
Risk v2
   ↓
Risk v3
```

Previous assessments SHALL remain recoverable.

---

# 58. Escalation Closure

An escalation is closed only when:

```text
Trigger Resolved
+
Required Action Complete
+
Evidence Present
+
Risk Reassessed
+
Authority Confirms Closure
```

Closing an escalation SHALL not erase the escalation history.

---

# 59. MFM Data Model

Core entities:

```text
Risk
RiskAssessment
RiskFactor
ImpactAssessment
LikelihoodAssessment
MaterialityAssessment
Tolerance
Escalation
RiskTreatment
RiskAcceptance
RiskReview
```

Relationships:

```text
Case
 ↓
Risk
 ↓
Assessment
 ↓
Materiality
 ↓
Treatment
 ↓
Escalation
 ↓
Decision
```

---

# 60. MFM Service Boundary

The conceptual implementation should include:

```text
Risk Service
Risk Assessment Service
Materiality Service
Tolerance Service
Escalation Service
Risk Treatment Service
Risk Reporting Service
```

These SHALL integrate with:

```text
Policy
Rule
Authority
Evidence
Workflow
State
Audit
```

services.

---

# 61. API Concepts

Illustrative operations:

```text
createRisk()
assessLikelihood()
assessImpact()
calculateRisk()
assessMateriality()
compareTolerance()
createEscalation()
escalateRisk()
treatRisk()
acceptRisk()
reassessRisk()
closeEscalation()
```

These are architectural concepts rather than implementation-specific commitments.

---

# 62. Risk Dashboard

The MFM implementation SHOULD provide:

```text
Risk by Category
Risk by Severity
Risk Above Tolerance
Open Material Findings
Critical Escalations
Overdue Risk Actions
Risk Concentrations
Systemic Risks
AI Risks
Third-Party Risks
```

---

# 63. Key Risk Indicators

The system SHOULD support KRIs such as:

```text
Critical Findings
Control Failure Rate
Regression Rate
Evidence Expiry Rate
SLA Breach Rate
Unresolved High Risks
Repeated Findings
Dependency Failure Rate
Authority Violations
```

Each KRI SHALL have an explicit definition and threshold.

---

# 64. Key Control Indicators

KCIs MAY include:

```text
Control Test Pass Rate
Control Coverage
Evidence Coverage
SoD Compliance
Audit Completeness
Remediation Effectiveness
```

KCI breaches MAY trigger escalation.

---

# 65. Threshold Governance

Thresholds SHALL be:

```text
Defined
Owned
Versioned
Approved
Tested
Reviewed
Audited
```

Changing a threshold may itself be a material change.

---

# 66. Threshold Change Impact

A threshold change SHALL identify affected:

```text
Open Risks
Existing Decisions
Controls
Tests
Monitoring
Regression Rules
Cases
Reports
```

Historical decisions SHALL retain the threshold version used.

---

# 67. Testing

Risk/materiality logic SHALL be tested for:

```text
Low Risk
Boundary Risk
High Risk
Critical Risk
Unknown
Missing Inputs
Conflicting Inputs
Threshold Boundary
Cumulative Effects
Duration Effects
Scope Effects
Override
Expiry
```

---

# 68. Negative Testing

The architecture SHALL verify that:

```text
Missing risk data
≠
Low risk

Unknown impact
≠
Acceptable impact

Expired tolerance
≠
Valid tolerance

Unauthorised override
≠
Valid override
```

---

# 69. Scenario Testing

Representative scenarios SHALL include:

```text
Minor operational deviation
Critical security failure
Evidence invalidation
Repeated small deviations
Systemic dependency failure
AI model change
Authority expiry
Critical remediation overdue
Risk above tolerance
Conflicting risk assessments
```

---

# 70. Acceptance Criteria

EA-IMETA-PC-RG-415 is accepted when:

- risk and materiality are distinct concepts;
- inherent and residual risk are distinguishable;
- likelihood and impact are defined;
- tolerance is explicit;
- quantitative and qualitative materiality are supported;
- cumulative, duration and scope effects are considered;
- escalation levels and triggers are defined;
- risk acceptance is explicit and authorised;
- systemic and dependency risks are supported;
- AI/agent risks are addressed;
- overrides are controlled;
- historical assessments are retained;
- threshold changes support impact analysis;
- risk logic is testable;
- uncertainty cannot silently become low risk.

---

# 71. Next Step

The next logical artifact is the **PC-RG monitoring and observability model**, because RG-415 establishes what constitutes risk/materiality and when escalation is required, while the architecture now needs to define how those conditions are continuously detected and measured.

Provisional next artifact:

> **EA-IMETA-PC-RG-416 — MONITORING, OBSERVABILITY & EARLY-WARNING MODEL**

This will connect operational signals to the risk, materiality, regression and escalation mechanisms already defined.

---

# 72. Governing Principle

> **Risk determines potential consequence, materiality determines governance significance, tolerance determines acceptability, and escalation determines the required response.**

The PC-RG architecture SHALL therefore treat risk as a controlled decision input rather than as a decorative score attached to a case.

# END OF EA-IMETA-PC-RG-415

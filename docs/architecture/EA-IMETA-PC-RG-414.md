# EA-IMETA-PC-RG-414

## POLICY, RULES & DECISION LOGIC MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-414 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Policy, Rules & Decision Logic Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-413 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how requirements, policies, criteria, thresholds, conditions and authority are converted into consistent decision logic |
| Architectural Boundary | Requirement → Policy → Rule → Evaluation → Decision → State |

---

# 2. Purpose

EA-IMETA-PC-RG-414 defines the policy and decision-logic architecture for PC-RG.

RG-413 establishes who may make a decision.

RG-414 establishes how the decision is evaluated.

The governing distinction is:

```text
POLICY
= WHAT MUST BE ACHIEVED

RULE
= HOW A CONDITION IS EVALUATED

CRITERION
= WHAT IS ACCEPTABLE

THRESHOLD
= WHEN A CONDITION BECOMES MATERIAL

DECISION LOGIC
= HOW RESULTS ARE COMBINED

AUTHORITY
= WHO MAY DECIDE

STATE MACHINE
= WHAT STATE MAY FOLLOW
```

No one of these concepts SHALL silently replace another.

---

# 3. Policy Hierarchy

Policies SHALL be organised into levels.

```text
GOVERNING POLICY
      ↓
DOMAIN POLICY
      ↓
CONTROL POLICY
      ↓
OPERATIONAL RULE
      ↓
CASE-SPECIFIC CONDITION
```

Lower-level rules SHALL not contradict higher-level mandatory requirements.

---

# 4. Policy Object

A policy SHALL be represented as a controlled object.

Minimum attributes:

| Attribute | Required |
|---|---|
| Policy ID | Yes |
| Title | Yes |
| Purpose | Yes |
| Scope | Yes |
| Owner | Yes |
| Authority | Yes |
| Version | Yes |
| Effective From | Yes |
| Effective Until | Where applicable |
| Normative Strength | Yes |
| Source | Yes |
| Dependencies | Where applicable |
| Approval | Yes |
| Status | Yes |

---

# 5. Policy Status

```text
DRAFT
UNDER REVIEW
APPROVED
ACTIVE
SUSPENDED
SUPERSEDED
EXPIRED
RETIRED
```

Only an approved/active policy SHALL be used for new material decisions unless an explicitly controlled historical or transitional rule applies.

---

# 6. Rule Object

A rule defines a deterministic or controlled evaluation.

Conceptually:

```text
IF
    CONDITION
THEN
    RESULT
ELSE
    RESULT
```

Example:

```text
IF required_evidence_count = 0
THEN acceptance = BLOCKED
```

Rules SHALL identify their scope and version.

---

# 7. Rule Attributes

Every material rule SHALL contain:

```text
Rule ID
Policy ID
Name
Purpose
Inputs
Conditions
Operator
Expected Values
Outcome
Severity
Applicability
Exceptions
Effective Period
Owner
Version
Test Reference
```

---

# 8. Rule Types

Initial rule catalogue:

```text
VALIDATION RULE
VERIFICATION RULE
ACCEPTANCE RULE
CLOSURE RULE
MONITORING RULE
REGRESSION RULE
REMEDIATION RULE
REVALIDATION RULE
REVERIFICATION RULE
REACCEPTANCE RULE
AUTHORITY RULE
SECURITY RULE
COMPLIANCE RULE
RISK RULE
DATA QUALITY RULE
TIME / EXPIRY RULE
```

---

# 9. Criteria

A criterion defines an acceptable condition.

Examples:

```text
Required evidence is present.

Control test result is PASS.

Risk is within approved tolerance.

Acceptance authority is valid.

Mandatory condition is satisfied.
```

Criteria SHALL be measurable or otherwise objectively assessable where practicable.

---

# 10. Criterion Object

```text
Criterion ID
Description
Measurement
Source
Applicable Scope
Minimum / Maximum
Comparison Operator
Evidence Requirement
Owner
Version
Effective Period
```

---

# 11. Thresholds

Thresholds determine when an observed value requires action.

Examples:

```text
Warning Threshold
Action Threshold
Critical Threshold
Expiry Threshold
Tolerance Threshold
```

Thresholds SHALL have explicit units and context.

A threshold of:

```text
10
```

without defining what 10 represents SHALL be considered incomplete.

---

# 12. Materiality

A materiality rule determines whether a deviation requires a lifecycle response.

Conceptually:

```text
OBSERVED CHANGE
      ↓
COMPARE BASELINE
      ↓
ASSESS MATERIALITY
      ↓
NO MATERIAL IMPACT
        OR
MATERIAL IMPACT
```

Materiality SHALL consider applicable risk and policy context.

---

# 13. Rule Evaluation

The evaluation engine SHALL receive:

```text
INPUT DATA
+
CRITERIA
+
POLICIES
+
RULES
+
CONTEXT
+
AUTHORITY
```

and produce:

```text
EVALUATION RESULT
+
RATIONALE
+
EVIDENCE REFERENCES
+
RULE VERSION
```

---

# 14. Decision Logic

Decision logic combines evaluation results.

Example:

```text
VALIDATION = PASS
VERIFICATION = PASS
AUTHORITY = VALID
RISK = ACCEPTABLE
BLOCKERS = 0
        ↓
ACCEPTANCE = PERMITTED
```

A decision SHALL not be derived from one isolated Boolean when multiple mandatory conditions exist.

---

# 15. Boolean Logic

The rule engine SHALL support explicit operators:

```text
AND
OR
NOT
XOR
IF / THEN / ELSE
IN
NOT IN
GREATER THAN
LESS THAN
EQUAL
BETWEEN
EXISTS
NOT EXISTS
```

Complex logic SHALL remain readable and testable.

---

# 16. Rule Precedence

Where multiple rules apply, precedence SHALL be explicit.

Recommended hierarchy:

```text
LEGAL / MANDATORY
      ↓
GOVERNING POLICY
      ↓
DOMAIN POLICY
      ↓
RISK RULE
      ↓
CONTROL RULE
      ↓
OPERATIONAL RULE
```

A lower-level rule SHALL not override a higher-level mandatory rule.

---

# 17. Conflict Detection

Conflicting rules SHALL be detected.

Example:

```text
RULE A:
Acceptance permitted.

RULE B:
Acceptance prohibited.
```

If both apply to the same context:

```text
RULE CONFLICT
```

The engine SHALL not arbitrarily choose one.

---

# 18. Rule Conflict Resolution

Resolution SHALL consider:

```text
Authority
Policy Level
Normative Strength
Scope
Effective Date
Risk
Explicit Precedence
```

The final resolution SHALL be recorded.

---

# 19. Rule Exceptions

Exceptions SHALL be explicit.

```text
RULE
 ↓
EXCEPTION CONDITION
 ↓
ALTERNATIVE OUTCOME
```

Every exception SHALL define:

```text
Scope
Authority
Duration
Reason
Evidence
Review
```

---

# 20. Temporary Rules

Temporary rules SHALL have an expiry.

```text
ACTIVE
  ↓
EXPIRING
  ↓
EXPIRED
```

The system SHALL prevent expired temporary rules from being silently applied.

---

# 21. Policy Versioning

Policies and rules SHALL be versioned.

Example:

```text
Acceptance Policy v1.4
Acceptance Policy v1.5
```

Historical decisions SHALL retain the versions used when the decision was made.

---

# 22. Effective Dating

A policy/rule SHALL support:

```text
Effective From
Effective Until
```

Evaluation SHALL use the version applicable to the decision time unless a defined transition rule states otherwise.

---

# 23. Temporal Decision Logic

The engine SHOULD support:

```text
"What rule was active on date X?"
```

This is required for retrospective audit.

---

# 24. Rule Inputs

Inputs SHALL identify:

```text
Source
Value
Type
Timestamp
Validity
Evidence
Confidence where applicable
```

An input without a trustworthy source SHALL be treated according to the applicable evidence policy.

---

# 25. Input Validation

Before rule evaluation:

```text
INPUT
 ↓
TYPE CHECK
 ↓
RANGE CHECK
 ↓
REQUIRED CHECK
 ↓
SOURCE CHECK
 ↓
VALIDITY CHECK
 ↓
EVALUATE
```

Invalid inputs SHALL not silently produce normal decisions.

---

# 26. Missing Inputs

A mandatory missing input SHALL produce:

```text
INPUT INCOMPLETE
```

and may result in:

```text
BLOCKED
INCONCLUSIVE
ESCALATED
```

according to policy.

It SHALL not default to PASS.

---

# 27. Unknown Values

The engine SHALL distinguish:

```text
TRUE
FALSE
UNKNOWN
NOT APPLICABLE
NOT AVAILABLE
```

Unknown SHALL not automatically equal FALSE or TRUE.

---

# 28. Confidence

Where decision inputs contain confidence measures, confidence SHALL not automatically replace evidence quality.

Example:

```text
AI confidence = 98%
```

does not by itself mean:

```text
Evidence validity = 98%
```

Confidence models SHALL be explicitly governed.

---

# 29. Decision Outcome Types

Rules and decision logic SHALL support:

```text
PASS
FAIL
CONDITIONAL
BLOCKED
INCONCLUSIVE
NOT APPLICABLE
REQUIRES REVIEW
REQUIRES APPROVAL
ESCALATE
```

---

# 30. Decision Gate

A decision gate combines the required inputs.

Example:

```text
ACCEPTANCE GATE

Validation = PASS
AND
Verification = PASS
AND
Authority = VALID
AND
Required Evidence = COMPLETE
AND
Critical Findings = 0
AND
Risk <= Tolerance
```

Only when all mandatory conditions are satisfied may the gate return:

```text
ACCEPTANCE PERMITTED
```

---

# 31. Validation Logic

Validation rules SHALL evaluate:

```text
Current State
Criteria
Evidence
Measurements
Applicable Requirements
```

Output:

```text
VALID
INVALID
CONDITIONAL
INCONCLUSIVE
```

---

# 32. Verification Logic

Verification rules SHALL evaluate:

```text
Validation Method
Validation Result
Evidence
Independence
Required Test Coverage
```

Output:

```text
VERIFIED
NOT VERIFIED
CONDITIONAL
INCONCLUSIVE
```

---

# 33. Acceptance Logic

Acceptance logic SHALL evaluate:

```text
Verified State
Authority
Risk
Conditions
Evidence
Blocking Findings
Expiry
```

Output:

```text
ACCEPT
REJECT
CONDITIONAL
SUSPEND
```

---

# 34. Closure Logic

Closure SHALL evaluate:

```text
Required Tasks = COMPLETE
Mandatory Evidence = PRESENT
Open Critical Findings = 0
Required Decisions = COMPLETE
Monitoring Plan = ACTIVE
Conditions = RECORDED
```

Only then may closure be permitted.

---

# 35. Monitoring Logic

Monitoring rules SHALL evaluate:

```text
Current Observation
Baseline
Thresholds
Trend
Context
```

Output:

```text
NORMAL
WARNING
ACTION REQUIRED
REGRESSION ASSESSMENT
CRITICAL
```

---

# 36. Regression Logic

Regression logic SHALL distinguish:

```text
OBSERVED CHANGE
```

from:

```text
MATERIAL REGRESSION
```

Example:

```text
IF deviation <= tolerance
THEN no regression

IF deviation > tolerance
AND risk impact = material
THEN regression confirmed
```

---

# 37. Remediation Logic

Remediation rules SHALL determine:

```text
Severity
Priority
Owner
Target Date
Required Action
Verification Requirement
Escalation
```

A remediation may not be closed solely because a task is marked complete.

---

# 38. Revalidation Logic

Revalidation SHALL evaluate:

```text
Remediation Evidence
Current Criteria
Current State
Residual Risk
Outstanding Conditions
```

Output:

```text
VALID
INVALID
CONDITIONAL
INCONCLUSIVE
```

---

# 39. Reverification Logic

Reverification SHALL evaluate:

```text
Revalidation Result
Method
Evidence
Independence
Criteria Version
Authority
```

Output:

```text
VERIFIED
NOT VERIFIED
CONDITIONAL
INCONCLUSIVE
```

---

# 40. Reacceptance Logic

Reacceptance SHALL evaluate:

```text
Revalidation = VALID
AND
Reverification = VERIFIED
AND
Authority = VALID
AND
Risk = ACCEPTABLE
AND
Conditions = ACCEPTED
```

Only then may reliance be restored.

---

# 41. Authority Rules

Policy logic SHALL not grant authority.

It may evaluate whether authority requirements are satisfied.

```text
Authority Service
       ↓
Authority Valid?
       ↓
Policy Engine
```

This preserves the separation defined in RG-413.

---

# 42. State Rules

The policy engine SHALL not independently invent lifecycle states.

It SHALL return an outcome to the state machine.

```text
RULE ENGINE
   ↓
DECISION RESULT
   ↓
STATE MACHINE
   ↓
AUTHORISED TRANSITION
```

---

# 43. Risk Rules

Risk rules MAY influence decision outcomes.

Examples:

```text
Risk > tolerance
→ acceptance blocked

Critical risk
→ suspension required

Risk decreasing after remediation
→ revalidation permitted
```

Risk calculations SHALL identify their methodology and version.

---

# 44. Compliance Rules

Compliance rules SHALL identify:

```text
Obligation
Source
Applicability
Requirement
Evidence
Evaluation
Result
```

Compliance logic SHALL not be reduced to a generic "compliant / non-compliant" label without traceability.

---

# 45. Security Rules

Security rules MAY govern:

```text
Access
Data Classification
Authentication
Authorisation
SoD
Audit
Evidence Integrity
Agent Permissions
```

Security failures affecting material decisions SHALL produce the defined outcome.

---

# 46. Data Quality Rules

Data quality rules SHALL detect:

```text
Missing
Invalid
Duplicate
Stale
Contradictory
Out-of-range
Untrusted
Unlinked
```

Data quality failures SHALL have defined consequences.

---

# 47. Time Rules

Time rules SHALL support:

```text
Deadline
Expiry
Grace Period
Review Interval
Monitoring Frequency
SLA
Retention
```

Time-based decisions SHALL use an authoritative time source.

---

# 48. Rule Engine Architecture

Conceptually:

```text
             ┌──────────────┐
             │    INPUTS    │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ VALIDATION   │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ POLICY LOAD  │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ RULE ENGINE  │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ EVALUATION   │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ DECISION     │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │ STATE MACHINE│
             └──────────────┘
```

---

# 49. Rule Execution Record

Every material evaluation SHALL record:

```text
Evaluation ID
Rule Set Version
Policy Versions
Input References
Evidence References
Evaluation Time
Result
Decision
Actor / Service
Correlation ID
```

This makes the evaluation reproducible.

---

# 50. Determinism

Where deterministic rules are used, the same:

```text
Inputs
+
Policy Versions
+
Rule Versions
+
Context
```

SHALL produce the same evaluation result.

If nondeterminism is intentional, it SHALL be documented and controlled.

---

# 51. Rule Testing

Every material rule SHALL have tests for:

```text
Positive
Negative
Boundary
Missing Input
Invalid Input
Exception
Conflict
Expiry
Version Change
```

---

# 52. Boundary Testing

Threshold rules SHALL test:

```text
Below Threshold
Exactly at Threshold
Above Threshold
```

Example:

```text
Tolerance = 5

4.99 → normal
5.00 → defined boundary outcome
5.01 → action
```

The boundary behaviour SHALL be explicit.

---

# 53. Rule Regression Testing

When a rule changes:

```text
RULE v1
   ↓
RULE v2
```

the system SHOULD execute affected regression tests.

Impact SHALL identify:

```text
Decisions
Controls
Workflows
States
Reports
Cases
```

---

# 54. Policy Conflict

Policy conflicts SHALL be handled as architectural issues.

The engine SHALL report:

```text
CONFLICTING POLICY
```

rather than selecting an arbitrary outcome.

---

# 55. Override

Overrides SHALL be exceptional.

An override SHALL record:

```text
Original Rule
Override Reason
Authority
Scope
Duration
Decision
Evidence
Post-Review
```

Overrides SHALL not modify the underlying rule.

---

# 56. Rule Simulation

The MFM implementation SHOULD support simulation:

```text
CURRENT CASE
+
ALTERNATIVE POLICY / RULE VERSION
        ↓
SIMULATED RESULT
```

Simulation SHALL not change production state.

---

# 57. Explainability

Material evaluations SHALL be explainable.

The system SHOULD show:

```text
Rule Applied
Inputs
Criteria
Comparisons
Outcome
Blocked Conditions
Evidence
Policy Version
```

A generic "rule failed" message is insufficient for governance review.

---

# 58. Decision Rationale

The engine SHALL generate structured rationale data:

```text
Satisfied Conditions
Unsatisfied Conditions
Exceptions
Threshold Results
Applicable Policies
Final Outcome
```

Human decision-makers may add narrative rationale.

---

# 59. AI and Agent Decision Logic

AI may assist with:

```text
Classification
Pattern Detection
Candidate Rule Selection
Anomaly Detection
Draft Rationale
```

AI SHALL not silently modify authoritative rule definitions.

Where AI proposes a decision:

```text
AI PROPOSAL
   ↓
POLICY / RULE VALIDATION
   ↓
AUTHORITY CHECK
   ↓
HUMAN OR AUTHORISED AUTOMATED DECISION
```

---

# 60. AI Rule Safety

Agents SHALL not:

- invent policy;
- invent thresholds;
- alter rule precedence;
- bypass mandatory criteria;
- infer approval authority;
- suppress conflicting evidence;
- convert UNKNOWN to PASS without a defined rule.

---

# 61. Policy Governance

Policy owners SHALL be responsible for:

```text
Definition
Review
Approval
Versioning
Expiry
Impact Assessment
Retirement
```

Rule owners SHALL be identifiable.

---

# 62. Policy Change Workflow

```text
CHANGE REQUEST
    ↓
IMPACT ASSESSMENT
    ↓
DRAFT
    ↓
REVIEW
    ↓
TEST
    ↓
APPROVAL
    ↓
ACTIVATION
    ↓
MONITOR
```

Material changes SHALL trigger regression analysis.

---

# 63. Policy Impact Analysis

Changes SHALL identify affected:

```text
Requirements
Controls
Rules
Decisions
States
Workflows
Tests
Reports
Open Cases
```

---

# 64. MFM Service Boundary

The conceptual implementation should include:

```text
Policy Service
Rule Service
Criteria Service
Decision Logic Service
Evaluation Service
Threshold Service
Policy Version Service
Simulation Service
```

These SHALL integrate with:

```text
Authority
Evidence
State
Workflow
Audit
```

services.

---

# 65. API Concepts

Illustrative operations:

```text
getApplicablePolicies()
getApplicableRules()
evaluateRule()
evaluateDecision()
validateInputs()
simulateDecision()
explainEvaluation()
createPolicyVersion()
createRuleVersion()
activatePolicy()
retirePolicy()
```

These operations are architectural concepts, not implementation-specific commitments.

---

# 66. Decision Cache

Caching of evaluations MAY be used for performance.

Cached decisions SHALL respect:

```text
Policy Version
Rule Version
Input Version
Evidence Validity
Authority
Time
Case State
```

Stale cached evaluations SHALL not be used for material decisions.

---

# 67. Failure Handling

If the policy/rule engine cannot produce a trustworthy result:

```text
ENGINE FAILURE
   ↓
DECISION BLOCKED
   OR
CONTROLLED FALLBACK
   ↓
AUDIT
   ↓
ESCALATION
```

Technical failure SHALL not silently become PASS.

---

# 68. Security

The policy/rule engine SHALL protect:

```text
Policy Definitions
Rule Definitions
Thresholds
Decision Logic
Versions
Overrides
```

Unauthorised rule changes SHALL be prevented and audited.

---

# 69. Rule Administration

Administrative access SHALL be separated from decision authority where appropriate.

A person able to configure rules SHALL not automatically be allowed to approve decisions based on those rules.

---

# 70. Metrics

The system SHOULD report:

```text
Rule Evaluations
PASS
FAIL
BLOCKED
INCONCLUSIVE
REQUIRES REVIEW
Rule Conflicts
Overrides
Expired Rules
Failed Evaluations
Policy Changes
Decision Reversals
```

---

# 71. Acceptance Criteria

EA-IMETA-PC-RG-414 is accepted when:

- policy and rule concepts are distinct;
- criteria and thresholds are explicit;
- rule versions are controlled;
- temporal applicability is supported;
- conflicts are detected;
- missing inputs cannot silently produce PASS;
- authority remains separate from decision logic;
- state transitions remain controlled by RG-410;
- material evaluations are reproducible;
- explanations are available;
- overrides are controlled;
- AI cannot invent or alter authoritative policy;
- rule changes have impact analysis and regression tests.

---

# 72. Next Step

The next logical artifact is the **PC-RG risk and materiality model**, because policy/rule evaluation now requires a consistent way to classify impact, severity, tolerance, residual risk and escalation.

Provisional next artifact:

> **EA-IMETA-PC-RG-415 — RISK, MATERIALITY & ESCALATION MODEL**

This will connect policy evaluation to proportional control response without introducing another abstract document layer.

---

# 73. Governing Principle

> **Policies define obligations, rules evaluate conditions, criteria define acceptability, thresholds define materiality, authority defines who may decide, and the state machine defines what state may follow.**

The PC-RG decision engine SHALL preserve these boundaries so that decisions remain explainable, reproducible, versioned and auditable.

# END OF EA-IMETA-PC-RG-414

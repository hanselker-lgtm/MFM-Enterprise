# EA-IMETA-PC-RG-434

## GOVERNANCE INTELLIGENCE, PRIORITISATION & INTERVENTION-SELECTION MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-434 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Governance Intelligence, Prioritisation & Intervention-Selection Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-433 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Convert validated governance intelligence into transparent, risk-based prioritisation and accountable decisions concerning remediation, assurance, intervention, monitoring and resource allocation |
| Architectural Boundary | Intelligence → Prioritisation → Options → Decision → Authority → Resource Allocation → Intervention Selection → Execution → Outcome Feedback |

---

# 2. Purpose

EA-IMETA-PC-RG-434 establishes the decision layer above finding intelligence and remediation analytics.

RG-433 identifies recurrence, patterns, systemic signals, governance debt and remediation performance.

RG-434 establishes **how those signals are prioritised and converted into explicit, evidence-based governance decisions about what should happen next**.

The architecture SHALL distinguish:

```text
INTELLIGENCE
= STRUCTURED EVIDENCE AND ANALYSIS

PRIORITISATION
= ORDERING GOVERNANCE DEMANDS ACCORDING TO DEFINED CRITERIA

DECISION
= AUTHORISED SELECTION AMONG GOVERNED OPTIONS

INTERVENTION SELECTION
= CHOOSING THE APPROPRIATE TREATMENT FOR A CONDITION

RESOURCE ALLOCATION
= ASSIGNING LIMITED CAPACITY TO APPROVED ACTIONS

URGENCY
= TIME PRESSURE CREATED BY RISK OR CONSEQUENCE

IMPORTANCE
= RELATIVE SIGNIFICANCE TO GOVERNED OBJECTIVES

MATERIALITY
= SIGNIFICANCE SUFFICIENT TO AFFECT GOVERNANCE, DECISION OR RELIANCE

RISK
= EFFECT OF UNCERTAINTY ON OBJECTIVES

PRIORITY
= GOVERNED RELATIVE POSITION IN THE ACTION QUEUE

DECISION QUALITY
= DEGREE TO WHICH A DECISION IS SUPPORTED, AUTHORISED, TRACEABLE AND PROPORTIONATE
```

---

# 3. Core Principle

> **Prioritisation is not merely ranking what is important; it is an accountable decision process that balances risk, evidence, urgency, impact, dependencies, capacity, effectiveness and residual uncertainty.**

The governing chain is:

```text
VALIDATED INTELLIGENCE
      ↓
CONTEXT
      ↓
RISK / IMPACT
      ↓
PRIORITISATION CRITERIA
      ↓
OPTIONS
      ↓
TRADE-OFF ANALYSIS
      ↓
DECISION
      ↓
AUTHORITY
      ↓
RESOURCE ALLOCATION
      ↓
INTERVENTION SELECTION
      ↓
EXECUTION
      ↓
OUTCOME
      ↓
FEEDBACK
```

---

# 4. Decision Object

Every material governance decision SHALL be represented as a controlled object.

Minimum attributes:

```text
Decision ID
Subject
Problem
Evidence
Risk
Options
Criteria
Recommendation
Decision
Authority
Conditions
Resources
Dependencies
Expected Outcome
Residual Risk
Review Date
Status
```

---

# 5. Prioritisation Object

Minimum attributes:

```text
Priority ID
Subject
Population
Criteria
Weights
Risk
Urgency
Impact
Dependencies
Capacity
Score
Rank
Confidence
Decision
```

---

# 6. Intervention Selection Object

Minimum attributes:

```text
Selection ID
Condition
Options
Evaluation Criteria
Selected Option
Rejected Options
Rationale
Authority
Expected Outcome
Residual Risk
Dependencies
```

---

# 7. Decision Lifecycle

```text
SIGNAL
   ↓
ASSESS
   ↓
PRIORITISE
   ↓
OPTIONS
   ↓
EVALUATE
   ↓
DECIDE
   ↓
AUTHORISE
   ↓
ALLOCATE
   ↓
EXECUTE
   ↓
MEASURE
   ↓
REVIEW
```

Alternative states:

```text
DEFERRED
ESCALATED
BLOCKED
REJECTED
SUPERSEDED
REOPENED
```

---

# 8. Decision Trigger

Decision triggers MAY include:

```text
Systemic Signal
Critical Finding
High Governance Debt
Recurrence
Regression
Benefit Erosion
Risk Threshold
Capacity Constraint
Assurance Finding
Policy Change
Dependency Failure
```

---

# 9. Trigger Validation

A trigger SHALL be assessed before being treated as a material decision requirement unless immediate action is required.

---

# 10. Decision Context

The decision record SHALL describe:

```text
Problem
Current State
Desired State
Risk
Evidence
Constraints
Dependencies
```

---

# 11. Decision Scope

Scope SHALL define:

```text
Population
Systems
Processes
Controls
Time
Organisational Boundary
```

---

# 12. Decision Boundary

The decision SHALL identify:

```text
Included
Excluded
Assumptions
Limitations
```

---

# 13. Decision Criteria

Criteria MAY include:

```text
Risk
Impact
Urgency
Effectiveness
Cost
Time
Feasibility
Dependency
Reversibility
Strategic Alignment
Compliance
Sustainability
```

---

# 14. Criteria Governance

Criteria SHALL be:

```text
Defined
Versioned
Applicable
Traceable
```

---

# 15. Weighting

Weighted criteria MAY be used.

Weights SHALL be explicit and governed.

---

# 16. Scoring

Composite scoring MAY be used for prioritisation.

Scoring logic SHALL be:

```text
Documented
Versioned
Reproducible
Auditable
```

---

# 17. Score Limitation

A composite score SHALL not conceal a critical risk.

---

# 18. Hard Constraints

Some conditions SHALL override scoring.

Examples:

```text
LEGAL REQUIREMENT
CRITICAL SAFETY RISK
MANDATORY CONTROL
SECURITY CRITICALITY
NON-NEGOTIABLE DEADLINE
```

---

# 19. Hard Constraint Override

Overrides SHALL be documented with:

```text
Reason
Authority
Evidence
Impact
```

---

# 20. Risk Priority

Priority SHOULD consider:

```text
Likelihood
Impact
Exposure
Velocity
Persistence
Detectability
Residual Risk
```

---

# 21. Risk Velocity

Rapidly increasing risk MAY justify priority above a slower but larger static risk.

---

# 22. Risk Persistence

Persistent risk SHALL be visible even when no immediate incident occurs.

---

# 23. Impact Dimensions

Impact MAY include:

```text
Operational
Financial
Security
Compliance
Safety
Reputation
Customer
Strategic
Systemic
```

---

# 24. Impact Concentration

Concentrated impact MAY increase priority.

---

# 25. Population Impact

Priority SHALL consider affected population where relevant.

---

# 26. Urgency

Urgency SHALL reflect:

```text
Time to Consequence
Exposure Duration
Deadline
Regulatory Timing
Dependency Timing
```

---

# 27. Urgency vs Importance

```text
URGENT
≠
IMPORTANT
```

A decision framework SHALL retain both dimensions.

---

# 28. Priority Quadrant

Conceptual:

```text
                 HIGH IMPORTANCE
                       ↑
                       │
          STRATEGIC    │    CRITICAL
                       │
LOW URGENCY ───────────┼────────── HIGH URGENCY
                       │
          MONITOR      │    RESPOND
                       │
                       ↓
                 LOW IMPORTANCE
```

---

# 29. Capacity

Prioritisation SHALL consider available:

```text
People
Budget
Technology
Time
Assurance Capacity
Change Capacity
```

---

# 30. Capacity Constraint

Capacity constraints SHALL not silently downgrade risk.

They SHALL create an explicit decision:

```text
DEFER
ADD CAPACITY
REDUCE SCOPE
ACCEPT RISK
CHANGE APPROACH
```

---

# 31. Resource Allocation

Resource allocation SHALL be traceable to approved decisions.

---

# 32. Resource Competition

Competing interventions SHALL be evaluated together where they consume shared capacity.

---

# 33. Portfolio Prioritisation

Portfolio prioritisation MAY consider:

```text
Risk Reduction
Strategic Value
Dependency
Cost
Time
Capacity
Outcome
```

---

# 34. Portfolio Balance

The portfolio SHOULD avoid:

```text
ALL HIGH-URGENCY WORK
```

when doing so creates long-term strategic or systemic exposure.

---

# 35. Intervention Options

Possible options:

```text
DO NOTHING / ACCEPT
MONITOR
CONTAIN
CORRECT
REMEDIATE
INTERVENE
REDESIGN
TRANSFER
AVOID
DEFER
```

---

# 36. Do-Nothing Option

The decision SHALL consider the consequences of taking no action where appropriate.

---

# 37. Option Definition

Each option SHOULD define:

```text
Objective
Scope
Cost
Time
Risk
Dependencies
Expected Outcome
Residual Risk
Reversibility
```

---

# 38. Option Comparison

Options SHALL be compared against common criteria where practicable.

---

# 39. Trade-Off Analysis

Trade-offs MAY include:

```text
Speed vs Quality
Cost vs Risk
Scope vs Time
Centralisation vs Flexibility
Automation vs Control
Immediate vs Long-Term Benefit
```

---

# 40. Trade-Off Transparency

Material trade-offs SHALL be documented.

---

# 41. Reversibility

Options SHOULD identify whether they are:

```text
REVERSIBLE
PARTIALLY REVERSIBLE
IRREVERSIBLE
```

---

# 42. Irreversible Decision

Irreversible decisions SHOULD require higher evidence and authority proportionate to impact.

---

# 43. Decision Confidence

Possible levels:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

---

# 44. Evidence Quality

Decision confidence SHALL reflect:

```text
Evidence Quality
Evidence Completeness
Evidence Independence
Measurement Reliability
Uncertainty
```

---

# 45. Uncertainty

Uncertainty SHALL be visible.

```text
UNKNOWN
≠
LOW RISK
```

---

# 46. Decision Assumptions

Material assumptions SHALL be documented.

---

# 47. Assumption Validation

Assumptions SHOULD have:

```text
Owner
Evidence
Validation Method
Review Date
```

---

# 48. Assumption Failure

If a material assumption fails:

```text
DECISION REVIEW
```

shall be triggered.

---

# 49. Dependency Analysis

Decision options SHALL identify:

```text
Internal Dependencies
External Dependencies
Technical Dependencies
Policy Dependencies
Resource Dependencies
```

---

# 50. Dependency Criticality

Critical dependencies SHALL influence priority and option selection.

---

# 51. Dependency Concentration

High concentration MAY justify:

```text
REDUNDANCY
DIVERSIFICATION
SEQUENCING
```

---

# 52. Scenario Analysis

Decisions MAY evaluate:

```text
BASE CASE
BEST CASE
WORST CASE
LIKELY CASE
```

---

# 53. Scenario Confidence

Scenario assumptions SHALL be explicit.

---

# 54. Sensitivity Analysis

Where quantitative scoring is used, sensitivity SHOULD assess whether small changes in assumptions materially change the decision.

---

# 55. Ranking Stability

If minor weighting changes cause major ranking changes:

```text
PRIORITY SENSITIVE
```

shall be reported.

---

# 56. Priority Tie

Where priorities are materially equal, the system SHOULD identify the tie rather than fabricate precision.

---

# 57. Decision Precision

Scores SHALL not imply more certainty than the evidence supports.

---

# 58. Human Judgment

Human judgement MAY override analytical ranking where justified.

Override SHALL document:

```text
Reason
Evidence
Authority
Impact
```

---

# 59. Override Governance

Overrides SHALL be auditable.

---

# 60. Bias

Prioritisation SHOULD assess potential bias from:

```text
Reporting
Visibility
Data Quality
Historical Decisions
Organisational Influence
Metric Design
```

---

# 61. Reporting Bias

Highly visible problems may receive higher priority than poorly detected problems.

---

# 62. Detection Bias

Low detection SHALL not be interpreted as low risk.

---

# 63. Data Bias

Missing data SHALL reduce confidence.

---

# 64. Strategic Bias

Strategic importance SHALL be explicit rather than hidden inside a score.

---

# 65. Political / Organisational Pressure

Material prioritisation SHALL distinguish evidence-based priority from organisational preference.

---

# 66. Decision Rights

Every material decision SHALL identify the decision authority.

---

# 67. Authority Levels

Authority SHALL reflect:

```text
Risk
Materiality
Scope
Financial Impact
Strategic Impact
Reversibility
```

---

# 68. Delegation

Delegated authority SHALL be:

```text
Explicit
Current
Traceable
Bounded
```

---

# 69. Separation of Duties

Where appropriate:

```text
RECOMMEND
≠
APPROVE
≠
IMPLEMENT
≠
ASSURE
```

---

# 70. Decision Record

Decision record SHALL preserve:

```text
Options
Evidence
Recommendation
Decision
Authority
Conditions
Dissent
```

---

# 71. Dissent

Material dissent MAY be recorded.

Dissent SHALL not be erased from the historical record.

---

# 72. Decision Rationale

Rationale SHALL explain:

```text
WHY THIS OPTION
WHY NOW
WHY NOT ALTERNATIVES
```

---

# 73. Decision Conditions

Conditions MAY include:

```text
Evidence
Milestones
Risk Controls
Review Date
Dependencies
```

---

# 74. Conditional Decision

Conditional decisions SHALL define:

```text
Condition
Owner
Deadline
Consequence
```

---

# 75. Deferred Decision

Deferral SHALL record:

```text
Reason
Risk
Next Review
Owner
Interim Control
```

---

# 76. Deferred Risk

Deferral SHALL not eliminate the underlying risk.

---

# 77. Risk Acceptance Decision

Risk acceptance SHALL follow appropriate authority and remain subject to monitoring.

---

# 78. Intervention Selection

Selection SHALL determine the appropriate treatment:

```text
MONITOR
CONTAIN
REMEDIATE
INTERVENE
ACCEPT
AVOID
TRANSFER
```

---

# 79. Selection Principle

> **The selected intervention SHALL be proportionate to the condition, evidence, risk, population, dependencies and expected outcome.**

---

# 80. Intervention Level

Possible levels:

```text
LOCAL
FUNCTIONAL
CROSS-FUNCTIONAL
ENTERPRISE
SYSTEMIC
```

---

# 81. Local vs Systemic

A systemic condition SHALL not be treated solely as a local issue without explicit justification.

---

# 82. Intervention Escalation

Escalation MAY occur when:

```text
Local Remediation Failed
Recurrence Persists
Cross-Domain Pattern
Shared Dependency
High Population Impact
```

---

# 83. Intervention De-escalation

De-escalation MAY occur when evidence demonstrates reduced scope or risk.

---

# 84. Intervention Scope

Scope SHALL align with the validated pattern and risk.

---

# 85. Over-Intervention

The architecture SHALL guard against interventions broader than evidence supports.

---

# 86. Under-Intervention

The architecture SHALL identify when a local treatment is inadequate for a systemic condition.

---

# 87. Intervention Portfolio

Selected interventions SHALL be managed as a portfolio where they compete for shared capacity.

---

# 88. Portfolio Dependencies

Dependencies SHALL be visible.

---

# 89. Portfolio Conflicts

Conflicting decisions SHALL be identified.

---

# 90. Portfolio Sequencing

Sequence SHALL consider:

```text
Risk
Dependency
Capacity
Time
Outcome
```

---

# 91. Change Saturation

The portfolio SHALL consider operational change saturation.

---

# 92. Resource Concentration

Concentration of resources on one intervention MAY create:

```text
Single Point of Failure
Capacity Risk
Delayed Other Risk
```

---

# 93. Decision Debt

Decision debt represents unresolved decisions required to govern material conditions.

---

# 94. Decision Debt Metrics

Possible measures:

```text
Open Decisions
Overdue Decisions
High-Risk Decisions
Average Decision Age
```

---

# 95. Decision Bottleneck

Bottlenecks MAY occur at:

```text
Evidence
Analysis
Recommendation
Authority
Funding
Implementation
```

---

# 96. Decision Latency

Measure:

```text
Decision Trigger
   ↓
Decision
```

---

# 97. Decision-to-Action Latency

Measure:

```text
Decision
   ↓
Action Start
```

---

# 98. Priority-to-Outcome Latency

Measure:

```text
Priority Assignment
   ↓
Measured Outcome
```

---

# 99. Decision Effectiveness

Decision effectiveness MAY consider:

```text
Outcome
Risk Reduction
Timeliness
Residual Risk
Recurrence
```

---

# 100. Decision Reversal

A decision MAY be reversed due to:

```text
New Evidence
Assumption Failure
Risk Change
Outcome Failure
Dependency Change
```

---

# 101. Reversal Governance

Reversal SHALL preserve the original decision.

---

# 102. Decision Reopening

A closed decision MAY reopen when material assumptions or conditions change.

---

# 103. Decision Sustainability

Material decisions SHOULD be reviewed against outcomes.

---

# 104. Decision Learning

Decision outcomes SHALL feed RG-433 intelligence.

---

# 105. Decision-to-Finding

Poor decision outcomes MAY create new findings.

---

# 106. Decision-to-Pattern

Repeated poor decisions MAY indicate governance patterns.

---

# 107. Decision Assurance

Material decisions MAY require RG-431 independent assurance.

---

# 108. Decision Corrective Action

Decision weaknesses MAY trigger RG-432 corrective action.

---

# 109. Decision Sustainability

RG-430 SHALL monitor outcomes of material interventions selected through this model.

---

# 110. Risk Integration

RG-415 SHALL provide risk assessment.

---

# 111. Policy Integration

RG-414 SHALL provide policy criteria.

---

# 112. Authority Integration

RG-413 SHALL govern decision rights.

---

# 113. Evidence Integration

RG-412 SHALL provide evidence traceability.

---

# 114. Workflow Integration

RG-411 SHALL govern lifecycle transitions.

---

# 115. Change Integration

RG-423 SHALL govern implementation changes.

---

# 116. Baseline Integration

RG-424 SHALL govern approved target states.

---

# 117. Monitoring Integration

RG-425 SHALL provide monitoring.

---

# 118. Exception Integration

RG-426 SHALL govern deviations.

---

# 119. Remediation Integration

RG-427 SHALL govern remediation.

---

# 120. Pattern Integration

RG-428 SHALL provide systemic pattern intelligence.

---

# 121. Intervention Integration

RG-429 SHALL govern selected systemic interventions.

---

# 122. Sustainability Integration

RG-430 SHALL monitor intervention outcomes.

---

# 123. Assurance Integration

RG-431 SHALL independently challenge material decisions.

---

# 124. Follow-Up Integration

RG-432 SHALL govern corrective actions resulting from decision review.

---

# 125. Intelligence Integration

RG-433 SHALL receive decision outcomes and performance data.

---

# 126. Governance Decision Dashboard

The dashboard SHOULD display:

```text
Decision Queue
Priority
Risk
Urgency
Authority
Dependencies
Capacity
Decision Age
Decision Status
```

---

# 127. Intervention Selection Dashboard

The dashboard SHOULD display:

```text
Systemic Signals
Recommended Treatments
Selected Interventions
Rejected Options
Residual Risk
Expected Outcomes
```

---

# 128. Portfolio Dashboard

The portfolio SHOULD display:

```text
Risk
Priority
Resource Allocation
Dependencies
Change Saturation
Expected Outcomes
Actual Outcomes
```

---

# 129. Decision Heatmap

Conceptual:

```text
                     LOW       MEDIUM       HIGH
RISK                  [ ]        [ ]         [ ]
URGENCY               [ ]        [ ]         [ ]
IMPACT                [ ]        [ ]         [ ]
UNCERTAINTY           [ ]        [ ]         [ ]
CAPACITY CONSTRAINT   [ ]        [ ]         [ ]
```

---

# 130. Prioritisation Matrix

A governed matrix MAY combine:

```text
Risk
Urgency
Impact
Feasibility
```

The matrix SHALL be versioned.

---

# 131. Risk-Based Queue

The system MAY maintain:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Queues.

Priority rules SHALL be explicit.

---

# 132. Queue Override

Manual queue overrides SHALL be auditable.

---

# 133. Starvation Risk

Low-priority items SHALL not remain indefinitely unaddressed without review.

---

# 134. Aging Review

Long-aged low-priority items SHALL be reassessed.

---

# 135. Priority Decay

Priority MAY change over time.

Changes SHALL be traceable.

---

# 136. Priority Escalation

Priority MAY increase due to:

```text
Risk Increase
Recurrence
Deadline
Population Growth
Dependency Change
```

---

# 137. Priority Reduction

Priority MAY decrease due to:

```text
Risk Reduction
Scope Reduction
Mitigation
Superseding Action
```

---

# 138. Priority Freeze

Critical decisions MAY require temporary priority freeze during execution.

---

# 139. Priority Rebalancing

Portfolio priorities SHALL be periodically reassessed.

---

# 140. Decision Frequency

Frequency SHALL be proportionate to:

```text
Risk
Volatility
Decision Volume
Change
```

---

# 141. Decision Review

Material decisions SHOULD have defined review dates.

---

# 142. Decision Expiry

Some decisions MAY expire automatically when:

```text
Time Limit
Condition
Policy
Dependency
```

changes.

---

# 143. Expired Decision

Expired decisions SHALL not silently remain authoritative.

---

# 144. Decision Preconditions

Preconditions SHALL be explicit.

---

# 145. Preconditions Failure

Failure SHALL trigger:

```text
REVIEW
```

---

# 146. Decision Dependencies

Decisions MAY depend on other decisions.

Dependency graph SHALL be maintained.

---

# 147. Decision Collision

Conflicting decisions SHALL be detected.

---

# 148. Decision Supersession

New decisions MAY supersede older decisions.

Historical traceability SHALL remain.

---

# 149. Decision Consistency

The system SHOULD detect contradictory decisions affecting the same scope.

---

# 150. Governance Consistency

Material contradictions SHALL trigger governance review.

---

# 151. Decision Quality Metrics

Possible measures:

```text
Decision Timeliness
Decision Reversal
Outcome Achievement
Risk Reduction
Unsupported Decision Rate
Decision Debt
```

---

# 152. Prioritisation Metrics

Possible measures:

```text
Priority Accuracy
Priority Changes
Priority Stability
Queue Age
Critical Response Time
```

---

# 153. Intervention Metrics

Possible measures:

```text
Selection-to-Action Time
Outcome Achievement
Residual Risk
Rework
Recurrence
```

---

# 154. Resource Metrics

Possible measures:

```text
Capacity Utilisation
Resource Concentration
Change Saturation
Deferred Risk
```

---

# 155. Decision Learning

Possible measures:

```text
Correct Decisions
Reversed Decisions
Unexpected Outcomes
Assumption Failures
```

---

# 156. AI-Assisted Prioritisation

AI MAY assist with:

```text
Risk Ranking
Pattern Summarisation
Scenario Analysis
Option Comparison
Capacity Forecasting
Decision Support
```

---

# 157. AI Restrictions

AI SHALL not silently:

```text
Set Material Priority
Accept Risk
Approve Intervention
Override Authority
Hide Uncertainty
```

---

# 158. AI Explainability

Material AI-assisted recommendations SHALL retain:

```text
Model
Version
Input
Criteria
Output
Confidence
Human Decision
```

---

# 159. AI Recommendation vs Decision

```text
AI RECOMMENDATION
≠
GOVERNANCE DECISION
```

---

# 160. Automation

Automation MAY perform:

```text
Priority Recalculation
Threshold Detection
Queue Updates
Dependency Checks
Decision Reminders
```

---

# 161. Automated Escalation

Deterministic thresholds MAY create escalation candidates.

---

# 162. Automated Decision

Fully automated material decisions SHALL be restricted to explicitly authorised bounded cases.

---

# 163. Human Oversight

Material governance decisions SHALL retain accountable human authority.

---

# 164. Data Quality

Decision inputs SHALL be assessed for:

```text
Completeness
Accuracy
Timeliness
Lineage
Consistency
```

---

# 165. Missing Data

Missing material information SHALL reduce decision confidence.

---

# 166. Stale Data

Stale intelligence SHALL be visible.

---

# 167. Data Freshness

Decision dashboards SHALL show:

```text
Last Refresh
Data Period
Known Gaps
```

---

# 168. Security

Decision data SHALL be protected against:

```text
Priority Manipulation
Evidence Manipulation
Authority Bypass
Resource Manipulation
Decision Suppression
```

---

# 169. Audit Trail

Decision events MAY include:

```text
Trigger Created
Assessment Completed
Priority Assigned
Options Created
Recommendation Submitted
Decision Made
Authority Confirmed
Resources Allocated
Decision Changed
Decision Reversed
```

---

# 170. Historical Integrity

Decision history SHALL remain immutable except through controlled correction.

---

# 171. Rationale Integrity

Decision rationale SHALL remain linked to the evidence and criteria used at decision time.

---

# 172. Decision Reconstruction

A historical decision SHOULD be reconstructable from:

```text
Evidence
Criteria
Options
Recommendation
Authority
Decision
Conditions
```

---

# 173. Confidentiality

Decision records MAY contain sensitive information.

Access SHALL follow:

```text
Need to Know
Least Privilege
Role
Purpose
```

---

# 174. MFM Data Model

Core entities:

```text
GovernanceDecision
DecisionTrigger
DecisionContext
DecisionCriteria
PriorityModel
PriorityAssessment
DecisionOption
OptionEvaluation
DecisionRecommendation
DecisionAuthority
DecisionCondition
ResourceAllocation
InterventionSelection
DecisionDependency
DecisionReview
DecisionOutcome
DecisionReversal
```

Relationships:

```text
Intelligence
   ↓
Priority
   ↓
Options
   ↓
Decision
   ↓
Authority
   ↓
Resources
   ↓
Intervention
   ↓
Outcome
   ↓
Learning
```

---

# 175. MFM Service Boundary

The conceptual implementation should include:

```text
Governance Decision Service
Prioritisation Service
Option Evaluation Service
Decision Authority Service
Resource Allocation Service
Intervention Selection Service
Decision Review Service
Decision Learning Service
```

These integrate with:

```text
Finding Intelligence
Recurrence
Pattern
Systemic Risk
Intervention
Assurance
Corrective Action
Follow-Up
Sustainability
Outcome
Benefit
Exception
Remediation
Change
Baseline
Monitoring
Dependency
Impact
Risk
Policy
Authority
Evidence
Reliance
Audit
```

---

# 176. API Concepts

Illustrative operations:

```text
createDecisionTrigger()
assessDecisionContext()
calculatePriority()
createOptions()
evaluateOptions()
submitRecommendation()
makeDecision()
approveDecision()
allocateResources()
selectIntervention()
reviewDecision()
reverseDecision()
supersedeDecision()
recordOutcome()
```

These are architectural concepts, not implementation-specific commitments.

---

# 177. Decision Data Pipeline

Conceptual flow:

```text
INTELLIGENCE
      ↓
CONTEXT
      ↓
RISK
      ↓
PRIORITY
      ↓
OPTIONS
      ↓
EVALUATION
      ↓
DECISION
      ↓
RESOURCE
      ↓
INTERVENTION
      ↓
OUTCOME
```

---

# 178. Analytical Reproducibility

Priority calculations SHALL be reproducible where practical.

---

# 179. Model Versioning

Priority models SHALL retain:

```text
Version
Criteria
Weights
Thresholds
Effective Date
Owner
```

---

# 180. Historical Recalculation

Changes to prioritisation models SHALL not silently rewrite historical decisions.

---

# 181. Model Drift

AI or analytical prioritisation models SHALL be monitored for:

```text
Performance Drift
Data Drift
Bias
Ranking Drift
```

---

# 182. Sensitivity Testing

Material priority models SHOULD be sensitivity tested.

---

# 183. Scenario Testing

Decision scenarios SHOULD test:

```text
Capacity Reduction
Risk Increase
Dependency Failure
Urgency Increase
Outcome Failure
```

---

# 184. Failure Handling

If prioritisation services fail:

```text
PRIORITY STATUS = DEGRADED
```

Manual governance SHALL remain available.

---

# 185. Manual Fallback

Manual prioritisation SHALL preserve:

```text
Criteria
Evidence
Rationale
Authority
Decision
```

---

# 186. Recovery

After service recovery:

```text
GAP
   ↓
RECALCULATE
   ↓
RECONCILE
   ↓
REVIEW
```

---

# 187. Negative Testing

The system SHALL verify:

```text
No decision authority → BLOCK
No decision scope → BLOCK
No material criteria → BLOCK
Missing critical evidence → LOW CONFIDENCE / REVIEW
Composite score hides critical risk → BLOCK
Hard constraint ignored → BLOCK
AI recommendation treated as final decision → BLOCK
Manual override without rationale → BLOCK
Resource allocation without approved decision → BLOCK
Intervention selected outside authorised scope → BLOCK
Decision dependency unresolved → REVIEW
Stale intelligence → FLAG
Missing data treated as zero → BLOCK
Priority starvation → REVIEW
Contradictory decisions → ESCALATION
Historical decision overwritten → BLOCK
```

---

# 188. Scenario Testing

Representative scenarios:

```text
Critical risk with low capacity
High urgency / low importance
Low urgency / high systemic impact
Competing interventions
Shared dependency
Resource conflict
Priority override
Hard constraint
Decision deferral
Risk acceptance
Decision reversal
New evidence
Assumption failure
Systemic intervention selection
AI-assisted ranking
Model drift
Population change
Stale intelligence
Decision collision
```

---

# 189. Acceptance Criteria

EA-IMETA-PC-RG-434 is accepted when:

- validated intelligence can be converted into governed priorities;
- priority criteria, weights and hard constraints are explicit;
- risk, urgency, impact and importance remain distinguishable;
- capacity constraints create explicit governance decisions rather than hidden risk reduction;
- options include appropriate treatment alternatives;
- trade-offs and rejected options remain visible;
- decision confidence reflects evidence and uncertainty;
- assumptions and dependencies are governed;
- material decisions have explicit authority;
- recommendation, approval, implementation and assurance can be separated;
- resource allocation is traceable to approved decisions;
- intervention level can be local, cross-functional, enterprise or systemic;
- over-intervention and under-intervention can be identified;
- portfolio conflicts, change saturation and resource concentration are visible;
- decision debt and decision latency are measurable;
- decision reversal and supersession preserve historical integrity;
- AI-assisted prioritisation remains explainable and non-authoritative unless explicitly bounded;
- historical priority calculations remain reproducible;
- decision outcomes feed back into intelligence;
- negative tests prevent unauthorised, unsupported or misleading prioritisation and intervention selection.

---

# 190. Next Step

The next logical artifact is the **PC-RG decision execution, resource mobilisation and intervention-governance model**, because RG-434 establishes which interventions should be selected, while the architecture now needs to govern how approved decisions are translated into funded, staffed, sequenced and controlled execution without losing traceability back to the original intelligence and decision.

Provisional next artifact:

> **EA-IMETA-PC-RG-435 — DECISION EXECUTION, RESOURCE MOBILISATION & INTERVENTION-GOVERNANCE MODEL**

This will establish the execution layer beneath governance decision and intervention selection.

---

# 191. Governing Principle

> **A priority is not a decision, a decision is not an intervention, and an intervention is not an outcome; each transition requires explicit criteria, authority, resources, evidence and traceability.**

The PC-RG architecture SHALL therefore ensure that governance intelligence leads to deliberate decisions, that decisions are proportionate to risk and uncertainty, that resource constraints remain visible, and that intervention selection can always be reconstructed from the evidence and authority that produced it.

# END OF EA-IMETA-PC-RG-434

# EA-IMETA-PC-RG-444

## ADAPTIVE PORTFOLIO OPTIMISATION, DYNAMIC PRIORITISATION & STRATEGIC REBALANCING MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-444 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Adaptive Portfolio Optimisation, Dynamic Prioritisation & Strategic Rebalancing Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-443 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Establish a controlled adaptive mechanism for continuously reassessing, reprioritising, resequencing, resizing and rebalancing the enterprise intervention portfolio as strategy, evidence, risk, benefits, capacity, dependencies and external conditions change |
| Architectural Boundary | Portfolio Assurance → Change Signal → Portfolio Reassessment → Dynamic Prioritisation → Optimisation → Rebalancing Decision → Controlled Portfolio Change → Verification → Continuous Adaptation |

---

# 2. Purpose

EA-IMETA-PC-RG-444 establishes the adaptive portfolio layer above portfolio assurance.

RG-443 establishes whether the portfolio remains strategically aligned, beneficial, sufficiently assured and sustainably resourced.

RG-444 establishes **how the portfolio dynamically changes when evidence changes**.

The architecture SHALL distinguish:

```text
ADAPTIVE PORTFOLIO GOVERNANCE
= GOVERNED CAPABILITY TO CHANGE PORTFOLIO PRIORITIES, SCOPE, SEQUENCE, CAPACITY AND INVESTMENT IN RESPONSE TO MATERIAL NEW EVIDENCE

DYNAMIC PRIORITISATION
= REASSESSMENT OF RELATIVE INTERVENTION PRIORITY USING CURRENT AUTHORISED CRITERIA AND EVIDENCE

PORTFOLIO OPTIMISATION
= SEARCH FOR A BETTER COMBINATION OF INTERVENTIONS, RESOURCES, SEQUENCE, RISK AND BENEFITS WITHIN AUTHORISED CONSTRAINTS

STRATEGIC REBALANCING
= DELIBERATE ADJUSTMENT OF PORTFOLIO COMPOSITION TO RESTORE OR IMPROVE STRATEGIC ALIGNMENT, VALUE, RESILIENCE OR CAPACITY SUSTAINABILITY

CHANGE SIGNAL
= MATERIAL NEW INFORMATION THAT MAY REQUIRE PORTFOLIO REASSESSMENT

REBALANCING TRIGGER
= DEFINED CONDITION THAT REQUIRES OR PERMITS A PORTFOLIO REVIEW

ADAPTATION THRESHOLD
= DEFINED LEVEL OF CHANGE AT WHICH THE CURRENT PORTFOLIO STATE SHALL BE REASSESSED

PORTFOLIO ELASTICITY
= ABILITY OF THE PORTFOLIO TO ADAPT WITHOUT UNACCEPTABLE LOSS OF CONTROL, VALUE OR RESILIENCE

PRIORITY VOLATILITY
= FREQUENCY AND MAGNITUDE OF MATERIAL PRIORITY CHANGES

OPTIMISATION CONSTRAINT
= CONDITION THAT LIMITS PERMITTED PORTFOLIO OPTIONS

REBALANCING DECISION
= AUTHORISED DECISION TO CHANGE PORTFOLIO COMPOSITION, PRIORITY, CAPACITY OR SEQUENCE

ADAPTIVE BASELINE
= CURRENT AUTHORISED PORTFOLIO STATE AGAINST WHICH CHANGE IS MEASURED

PORTFOLIO STABILITY
= DEGREE TO WHICH THE PORTFOLIO REMAINS COHERENT AND CONTROLLED THROUGH CHANGE

CHANGE FATIGUE
= LOSS OF EFFECTIVENESS CAUSED BY EXCESSIVE OR POORLY SEQUENCED CHANGE

PORTFOLIO CHURN
= UNCONTROLLED OR EXCESSIVE ADDITION, REMOVAL, PAUSING OR reprioritisation of interventions

STRATEGIC REBALANCE
= PORTFOLIO CHANGE REQUIRED TO MAINTAIN ALIGNMENT WITH CURRENT STRATEGIC CONDITIONS

OPTIMISATION FAILURE
= CONDITION WHERE APPARENT PORTFOLIO IMPROVEMENT CREATES UNACCEPTABLE HIDDEN RISK, CAPACITY STRAIN OR OUTCOME LOSS

LOCAL OPTIMUM
= PORTFOLIO STATE THAT APPEARS BEST UNDER LIMITED CRITERIA BUT IS NOT BEST FOR THE ENTERPRISE SYSTEM

GLOBAL ENTERPRISE OPTIMUM
= BEST AUTHORISED PORTFOLIO STATE UNDER THE DEFINED ENTERPRISE OBJECTIVE, CONSTRAINTS AND RISK APPETITE

ADAPTIVE REVALIDATION
= RECONFIRMATION THAT A CHANGED PORTFOLIO REMAINS JUSTIFIED, CONTROLLED AND SUSTAINABLE
```

---

# 3. Core Principle

> **A portfolio SHALL adapt to material evidence without becoming unstable; every significant change in strategy, risk, benefit, capacity or external conditions SHALL be capable of triggering reassessment, while every resulting portfolio change SHALL remain authorised, traceable, proportionate and verifiable.**

The governing chain is:

```text
CURRENT PORTFOLIO
      ↓
NEW EVIDENCE
      ↓
CHANGE SIGNAL
      ↓
MATERIALITY ASSESSMENT
      ↓
REASSESSMENT
      ↓
DYNAMIC PRIORITISATION
      ↓
OPTIMISATION OPTIONS
      ↓
TRADE-OFF ANALYSIS
      ↓
REBALANCING DECISION
      ↓
CONTROLLED CHANGE
      ↓
VERIFICATION
      ↓
ADAPTIVE BASELINE
```

---

# 4. Adaptive Portfolio Object

Minimum attributes:

```text
Adaptive Portfolio ID
Current Baseline
Strategic Objective
Interventions
Priorities
Constraints
Capacity
Risk
Benefits
Change Signals
Status
```

---

# 5. Change Signal Object

Minimum attributes:

```text
Signal ID
Source
Condition
Evidence
Materiality
Affected Areas
Urgency
Confidence
Trigger
Status
```

---

# 6. Reassessment Object

Minimum attributes:

```text
Reassessment ID
Trigger
Portfolio State
Evidence
Assumptions
Options
Impact
Decision
Authority
Status
```

---

# 7. Optimisation Option Object

Minimum attributes:

```text
Option ID
Portfolio
Objective
Changes
Benefits
Costs
Risk
Capacity
Dependencies
Trade-Offs
Confidence
Status
```

---

# 8. Rebalancing Decision Object

Minimum attributes:

```text
Decision ID
Current State
Target State
Change
Rationale
Evidence
Risk
Capacity
Authority
Effective Date
Status
```

---

# 9. Adaptive Baseline Object

Minimum attributes:

```text
Baseline ID
Portfolio State
Scope
Priorities
Capacity
Risk
Benefits
Assumptions
Authority
Version
Date
Status
```

---

# 10. Adaptation Event Object

Minimum attributes:

```text
Event ID
Trigger
Affected Interventions
Change
Decision
Execution
Verification
Outcome
Status
```

---

# 11. Lifecycle

```text
PORTFOLIO
   ↓
MONITOR
   ↓
SIGNAL
   ↓
ASSESS
   ↓
REASSESS
   ↓
OPTIMISE
   ↓
REBALANCE
   ↓
EXECUTE
   ↓
VERIFY
   ↓
LEARN
   ↓
NEW BASELINE
```

Alternative states:

```text
STABLE
WATCH
SIGNAL DETECTED
REASSESSMENT
OPTIMISATION
REBALANCING
EXECUTION
VERIFYING
ADAPTED
DEGRADED
UNSTABLE
UNKNOWN
```

---

# 12. Adaptive Governance Boundary

The adaptive mechanism SHALL define:

```text
What Can Change
What Cannot Change Without Escalation
Who Can Change It
Under Which Conditions
How Change Is Verified
```

---

# 13. Stable Core

Certain portfolio conditions MAY be treated as stable core requirements.

Examples:

```text
Legal Obligations
Safety Requirements
Critical Controls
Mandatory Regulatory Commitments
Approved Risk Boundaries
```

---

# 14. Adaptive Layer

Other elements MAY adapt:

```text
Priority
Sequence
Scope
Resource Allocation
Timing
Delivery Method
Intervention Mix
```

---

# 15. Stability vs Adaptability

The architecture SHALL balance:

```text
STABILITY
+
ADAPTABILITY
=
CONTROLLED EVOLUTION
```

---

# 16. Change Signal Sources

Signals MAY arise from:

```text
Strategy
Risk
Benefits
Capacity
Dependencies
Assurance
Performance
Incidents
Technology
Regulation
Market
Stakeholders
Operations
```

---

# 17. Signal Detection

Material signals SHALL be detectable.

---

# 18. Signal Registration

Material signals SHALL be recorded.

---

# 19. Signal Evidence

Signals SHOULD include evidence and source.

---

# 20. Signal Confidence

Possible:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

---

# 21. Signal Materiality

Materiality SHALL consider:

```text
Impact
Scope
Persistence
Urgency
Confidence
```

---

# 22. Signal False Positive

Weak signals SHALL not automatically cause major portfolio changes.

---

# 23. Signal False Negative

Failure to detect material change SHALL be subject to monitoring effectiveness review.

---

# 24. Signal Correlation

Multiple related signals MAY indicate systemic change.

---

# 25. Signal Aggregation

Signals SHOULD be aggregated without losing source traceability.

---

# 26. Signal Escalation

Escalation SHALL reflect:

```text
Materiality
Urgency
Risk
Scope
```

---

# 27. Trigger Types

Possible:

```text
MANDATORY
THRESHOLD
EVENT
FORECAST
TREND
STRATEGIC
ASSURANCE
BENEFIT
CAPACITY
RISK
```

---

# 28. Threshold Trigger

A threshold trigger SHALL have:

```text
Metric
Threshold
Direction
Timeframe
Response
```

---

# 29. Event Trigger

Material events MAY trigger immediate reassessment.

---

# 30. Trend Trigger

Persistent trends MAY trigger reassessment even before a hard threshold is breached.

---

# 31. Forecast Trigger

Forecast deterioration MAY trigger early review.

---

# 32. Strategic Trigger

Material strategy change SHALL trigger portfolio reassessment.

---

# 33. Benefit Trigger

Material benefit underperformance SHALL trigger reassessment.

---

# 34. Capacity Trigger

Material capacity deterioration SHALL trigger reassessment.

---

# 35. Risk Trigger

Material risk change SHALL trigger reassessment.

---

# 36. Assurance Trigger

Critical assurance findings SHALL trigger portfolio reassessment where relevant.

---

# 37. Trigger Suppression

Triggers SHALL not be suppressed merely to preserve portfolio stability.

---

# 38. Trigger Override

Override SHALL require:

```text
Reason
Authority
Evidence
Expiry
```

---

# 39. Reassessment Initiation

A reassessment SHALL identify:

```text
Trigger
Current State
Affected Scope
Required Decision
```

---

# 40. Reassessment Boundary

Reassessment SHALL define what is and is not being reconsidered.

---

# 41. Current State

The current state SHALL remain visible during reassessment.

---

# 42. Historical Baseline

Previous authorised baselines SHALL remain preserved.

---

# 43. Evidence Refresh

Material reassessments SHALL use current evidence.

---

# 44. Assumption Refresh

Material assumptions SHALL be reassessed.

---

# 45. Dependency Refresh

Critical dependencies SHALL be reassessed.

---

# 46. Capacity Refresh

Current and forecast capacity SHALL be reassessed.

---

# 47. Risk Refresh

Material risks SHALL be reassessed.

---

# 48. Benefit Refresh

Expected and realised benefits SHALL be reassessed.

---

# 49. Strategic Refresh

Strategic relevance SHALL be reassessed.

---

# 50. Reassessment Outcome

Possible:

```text
NO CHANGE
MINOR ADJUSTMENT
RESEQUENCE
REPRIORITISE
REDUCE
PAUSE
ACCELERATE
STOP
REPLACE
REBUILD
```

---

# 51. Dynamic Prioritisation

Priorities SHALL be recalculated when material criteria change.

---

# 52. Priority Criteria

Possible:

```text
Strategic Alignment
Mandatory Requirement
Risk Reduction
Benefit
Urgency
Dependency
Capacity
Resilience
Cost
Opportunity Cost
```

---

# 53. Priority Formula

Where a formula is used:

```text
CRITERIA
+
WEIGHTS
+
DATA
+
LIMITATIONS
=
PRIORITY RESULT
```

---

# 54. Priority Transparency

Priority changes SHALL preserve the reason for change.

---

# 55. Priority Stability

Unnecessary priority changes SHOULD be avoided.

---

# 56. Priority Volatility

Priority volatility SHALL be monitored.

---

# 57. Priority Volatility Threshold

High volatility SHALL trigger analysis of:

```text
Strategy Stability
Decision Quality
Signal Quality
Governance Stability
```

---

# 58. Priority Override

Mandatory or critical requirements MAY override normal prioritisation.

---

# 59. Override Governance

Overrides SHALL retain:

```text
Authority
Reason
Impact
Duration
```

---

# 60. Priority Gaming

Priority criteria SHALL be protected from manipulation.

---

# 61. Goodhart Risk

```text
A PRIORITY METRIC USED AS A TARGET
MAY CEASE TO REPRESENT TRUE ENTERPRISE VALUE.
```

---

# 62. Portfolio Optimisation

Optimisation SHALL seek improved enterprise outcome subject to constraints.

---

# 63. Optimisation Objective

Possible objectives:

```text
MAXIMISE BENEFIT
MINIMISE RISK
MINIMISE COST
PROTECT CAPACITY
MAXIMISE RESILIENCE
MAXIMISE STRATEGIC ALIGNMENT
```

---

# 64. Multi-Objective Optimisation

Where multiple objectives exist, trade-offs SHALL be explicit.

---

# 65. Optimisation Constraints

Constraints MAY include:

```text
Budget
Capacity
Risk Appetite
Regulation
Dependency
Technology
Time
Safety
```

---

# 66. Hard Constraint

A hard constraint SHALL not be violated without authorised exception.

---

# 67. Soft Constraint

Soft constraints MAY be traded off where explicitly authorised.

---

# 68. Constraint Hierarchy

Conflicting constraints SHALL have defined precedence.

---

# 69. Optimisation Options

The system SHOULD generate multiple feasible options where material.

---

# 70. Option Comparison

Options SHALL compare:

```text
Benefit
Cost
Risk
Capacity
Time
Dependencies
Resilience
```

---

# 71. Option Uncertainty

Uncertainty SHALL remain visible.

---

# 72. Scenario Optimisation

Options MAY be evaluated against:

```text
BASE
UPSIDE
DOWNSIDE
STRESS
CRISIS
```

---

# 73. Sensitivity

Material optimisation SHOULD support sensitivity analysis.

---

# 74. Local Optimum

Local optimisation SHALL not be treated as enterprise optimum without broader analysis.

---

# 75. Enterprise Optimum

Enterprise optimisation SHALL consider cross-domain effects.

---

# 76. Optimisation Bias

Possible biases SHALL be considered:

```text
Sunk Cost
Availability
Recency
Confirmation
Status Quo
Political
Metric
```

---

# 77. Sunk Cost Control

Past expenditure SHALL not determine future priority by itself.

---

# 78. Status Quo Control

Maintaining the current portfolio SHALL be treated as an option requiring justification.

---

# 79. Confirmation Bias Control

Evidence supporting continuation SHALL be balanced against contradictory evidence.

---

# 80. Rebalancing

Rebalancing MAY change:

```text
Intervention Mix
Priority
Sequence
Scope
Resources
Timing
```

---

# 81. Rebalancing Objective

Rebalancing SHALL state the intended improvement.

---

# 82. Rebalancing Trigger

Rebalancing SHALL identify the trigger.

---

# 83. Rebalancing Decision

Decision SHALL include:

```text
Current State
Target State
Change
Reason
Evidence
Risk
Authority
```

---

# 84. Rebalancing Impact

Impact assessment SHALL cover:

```text
Interventions
Benefits
Dependencies
Capacity
Risk
Stakeholders
```

---

# 85. Rebalancing Transition

Material rebalancing SHALL have a controlled transition plan.

---

# 86. Rebalancing Rollback

Where feasible, rollback criteria SHOULD be defined.

---

# 87. Rebalancing Verification

Post-change verification SHALL confirm intended effect.

---

# 88. Adaptive Baseline

After approved change, a new baseline SHALL be established.

---

# 89. Baseline Preservation

Previous baselines SHALL remain immutable.

---

# 90. Baseline Delta

The system SHALL identify:

```text
OLD STATE
→
CHANGE
→
NEW STATE
```

---

# 91. Change Ledger

A portfolio change ledger SHALL preserve material adaptations.

---

# 92. Change Entry

Minimum:

```text
Date
Trigger
Old State
New State
Authority
Rationale
Evidence
```

---

# 93. Change Frequency

Excessive change frequency SHALL be monitored.

---

# 94. Portfolio Churn

Portfolio churn SHALL be assessed.

---

# 95. Churn Threshold

Material churn SHALL trigger governance review.

---

# 96. Change Fatigue

Change fatigue MAY reduce:

```text
Adoption
Quality
Capacity
Assurance
Control
```

---

# 97. Change Saturation

Change saturation SHALL be monitored.

---

# 98. Adaptive Capacity

The enterprise SHALL assess its capacity to absorb portfolio changes.

---

# 99. Change Absorption

Possible indicators:

```text
Training Load
Implementation Load
Leadership Load
Technology Load
Operational Load
Assurance Load
```

---

# 100. Change Queue

Pending portfolio changes SHALL remain visible.

---

# 101. Change Queue Prioritisation

Change queue priority SHALL use authorised criteria.

---

# 102. Change Queue Aging

Long-pending changes SHALL be reassessed.

---

# 103. Change Collision

Conflicting changes SHALL be identified.

---

# 104. Change Dependency

Changes MAY depend on:

```text
Technology
Capability
Policy
Resource
Decision
Other Change
```

---

# 105. Change Critical Path

Critical change dependencies SHALL be monitored.

---

# 106. Strategic Rebalancing

Strategic rebalancing SHALL occur when the portfolio no longer reflects authorised strategic priorities.

---

# 107. Strategic Rebalancing Trigger

Possible:

```text
STRATEGY CHANGE
EXTERNAL SHOCK
BENEFIT EROSION
RISK CHANGE
CAPACITY CHANGE
```

---

# 108. Strategic Rebalancing Options

Possible:

```text
ACCELERATE STRATEGIC
REDUCE NON-STRATEGIC
STOP OBSOLETE
CREATE NEW
RESEQUENCE
```

---

# 109. Strategic Rebalancing Test

The portfolio SHOULD answer:

```text
Does the current portfolio still represent the best authorised strategic allocation?
```

---

# 110. Opportunity Cost Reassessment

Rebalancing SHALL reassess opportunity cost.

---

# 111. Capacity Rebalancing

Capacity SHALL be reallocated where justified.

---

# 112. Capacity Protection

Critical operational capacity SHALL not be consumed without appropriate authority.

---

# 113. Risk Rebalancing

Portfolio risk concentration SHALL be reassessed.

---

# 114. Benefit Rebalancing

Resources MAY be shifted toward higher-confidence benefit opportunities.

---

# 115. Resilience Rebalancing

Critical resilience gaps MAY justify reprioritisation even where immediate financial benefit is low.

---

# 116. Mandatory Rebalancing

Mandatory requirements SHALL be protected from discretionary displacement.

---

# 117. Portfolio Composition

Portfolio composition SHALL remain visible.

---

# 118. Composition Dimensions

Possible:

```text
Mandatory
Strategic
Risk
Benefit
Resilience
Capability
Transformation
Maintenance
```

---

# 119. Composition Balance

The portfolio SHOULD maintain an appropriate balance.

---

# 120. Concentration Risk

Excessive concentration SHALL be assessed.

---

# 121. Diversification

Diversification MAY improve resilience but SHALL not become an objective by itself.

---

# 122. Portfolio Elasticity

Portfolio elasticity SHALL consider:

```text
Decision Speed
Resource Flexibility
Dependency Flexibility
Change Capacity
Governance Capacity
```

---

# 123. Low Elasticity

Low elasticity MAY indicate:

```text
Rigid Contracts
Capacity Lock-In
Technology Lock-In
Governance Delay
Dependency Concentration
```

---

# 124. Elasticity Improvement

Possible:

```text
Modularisation
Cross-Skilling
Flexible Capacity
Alternative Suppliers
Simplified Governance
```

---

# 125. Adaptive Resilience

Resilience SHALL include ability to adapt, not only ability to recover.

---

# 126. Adaptation Stress Test

Scenarios MAY include:

```text
20% BUDGET REDUCTION
20% CAPACITY REDUCTION
MAJOR STRATEGY CHANGE
CRITICAL DEPENDENCY LOSS
BENEFIT REDUCTION
REGULATORY CHANGE
```

---

# 127. Adaptation Stress Result

Possible:

```text
ROBUST
CONDITIONAL
FRAGILE
FAIL
NOT TESTED
```

---

# 128. Not Tested

```text
NOT TESTED
≠
ADAPTIVE
```

---

# 129. Adaptive Failure

Adaptive failure MAY occur where the portfolio cannot respond within required time or constraints.

---

# 130. Adaptive Recovery

Recovery SHALL restore controlled adaptation capability.

---

# 131. Decision Velocity

Decision velocity SHALL be measured where rapid adaptation is material.

---

# 132. Decision Quality vs Speed

Fast decisions SHALL not automatically be considered good decisions.

---

# 133. Decision Trade-Off

The architecture SHALL balance:

```text
SPEED
+
QUALITY
+
CONTROL
```

---

# 134. Escalation Speed

Material change signals SHALL have appropriate escalation speed.

---

# 135. Decision Latency

Decision latency MAY create portfolio risk.

---

# 136. Decision Latency Threshold

Thresholds SHALL reflect urgency and impact.

---

# 137. Emergency Rebalancing

Emergency rebalancing MAY be permitted for critical conditions.

---

# 138. Emergency Authority

Emergency authority SHALL be explicit.

---

# 139. Emergency Scope

Emergency decisions SHALL remain limited to necessary scope.

---

# 140. Emergency Review

Emergency changes SHALL receive retrospective governance review.

---

# 141. Temporary Rebalancing

Temporary changes SHALL define:

```text
Start
End
Owner
Exit Criteria
```

---

# 142. Temporary State

Temporary portfolio states SHALL not become permanent by neglect.

---

# 143. Rebalancing Expiry

Temporary changes SHOULD have automatic review or expiry.

---

# 144. Portfolio Pause

The portfolio MAY enter controlled pause where evidence is insufficient for continued execution.

---

# 145. Pause Criteria

Possible:

```text
UNKNOWN MATERIAL CONDITION
CAPACITY CRISIS
STRATEGIC UNCERTAINTY
CRITICAL ASSURANCE FAILURE
```

---

# 146. Pause Risk

Pause itself SHALL be assessed for risk and opportunity cost.

---

# 147. Portfolio Stop

Stopping the portfolio or material components SHALL preserve:

```text
Residual Risk
Benefits Lost
Costs Avoided
Dependencies
Knowledge
```

---

# 148. Portfolio Restart

Restart SHALL use current evidence rather than historical assumptions alone.

---

# 149. Portfolio Replacement

Replacement SHALL compare alternatives.

---

# 150. Replacement Transition

Transition risk SHALL be assessed.

---

# 151. Rebalancing Governance

Material rebalancing SHALL require:

```text
Evidence
Option Analysis
Impact Assessment
Authority
Decision
Verification
```

---

# 152. Rebalancing Gate

Possible gates:

```text
SIGNAL
ASSESSMENT
OPTION
DECISION
IMPLEMENTATION
VERIFICATION
```

---

# 153. Gate Failure

Gate failure SHALL result in:

```text
HOLD
REWORK
ESCALATE
ABANDON
```

---

# 154. Adaptive Assurance

Adaptive changes SHALL be assured proportionately.

---

# 155. Change Assurance

Assurance SHALL consider:

```text
Trigger
Decision
Impact
Execution
Outcome
```

---

# 156. Assurance Independence

Material adaptive decisions SHOULD receive independent challenge.

---

# 157. Adaptive Finding

Findings SHALL identify whether adaptation was:

```text
TIMELY
APPROPRIATE
AUTHORISED
EFFECTIVE
```

---

# 158. Adaptation Effectiveness

Effectiveness SHALL assess whether the change improved the intended condition.

---

# 159. Adaptation False Positive

Unnecessary rebalancing SHALL be analysed.

---

# 160. Adaptation False Negative

Missed adaptation opportunities SHALL be analysed.

---

# 161. Portfolio Learning

Every material adaptation SHOULD generate learning.

---

# 162. Adaptation Learning

Learning SHOULD identify:

```text
Trigger Quality
Decision Quality
Timing
Outcome
Unintended Effects
```

---

# 163. Unintended Consequences

Rebalancing SHALL assess unintended consequences.

---

# 164. Second-Order Effects

Material changes SHOULD consider second-order effects.

---

# 165. Third-Order Effects

High-impact changes MAY require third-order analysis.

---

# 166. Change Cascade

Conceptual:

```text
PORTFOLIO CHANGE
      ↓
DEPENDENCY CHANGE
      ↓
RESOURCE CHANGE
      ↓
INTERVENTION CHANGE
      ↓
OUTCOME CHANGE
```

---

# 167. Change Containment

Material adverse effects SHALL be contained where feasible.

---

# 168. Change Rollback

Rollback SHALL be used where appropriate and safe.

---

# 169. Rollback Verification

Rollback SHALL be verified.

---

# 170. Post-Change Review

Material changes SHALL receive post-change review.

---

# 171. Adaptive Metrics

Possible:

```text
Time to Detect
Time to Decide
Time to Rebalance
Change Success
Change Failure
Portfolio Churn
Priority Volatility
Benefit Protection
Capacity Stability
```

---

# 172. Rebalancing Metrics

Possible:

```text
Rebalancing Frequency
Rebalancing Effectiveness
Strategic Alignment Improvement
Risk Reduction
Benefit Improvement
```

---

# 173. Adaptation Metrics

Possible:

```text
Adaptation Lead Time
Signal Detection Rate
False Positive Rate
False Negative Rate
```

---

# 174. Stability Metrics

Possible:

```text
Portfolio Stability
Priority Stability
Capacity Stability
Dependency Stability
```

---

# 175. Churn Metrics

Possible:

```text
Interventions Added
Interventions Removed
Interventions Paused
Priority Changes
Sequence Changes
```

---

# 176. Change Fatigue Metrics

Possible:

```text
Change Load
Adoption Decline
Rework
Error Rate
Absence
Turnover
```

---

# 177. Adaptive Health

Possible:

```text
ADAPTIVE
WATCH
DEGRADED
RIGID
CHAOTIC
UNKNOWN
```

---

# 178. Rigid Portfolio

A portfolio that fails to adapt to material evidence SHALL be treated as governance risk.

---

# 179. Chaotic Portfolio

A portfolio with uncontrolled frequent change SHALL be treated as governance risk.

---

# 180. Balanced Adaptive State

Desired state:

```text
RESPONSIVE
+
CONTROLLED
+
EVIDENCE-BASED
+
STABLE ENOUGH TO EXECUTE
```

---

# 181. Adaptive Debt

Adaptive debt MAY include:

```text
Decision Debt
Signal Debt
Reassessment Debt
Capacity Debt
Dependency Debt
Strategic Debt
```

---

# 182. Signal Debt

Signal debt represents known change signals not yet assessed.

---

# 183. Reassessment Debt

Reassessment debt represents required reviews not yet completed.

---

# 184. Adaptive Debt Aging

Debt SHALL be monitored by:

```text
Age
Materiality
Risk
Impact
```

---

# 185. Adaptive Debt Reduction

Debt reduction SHALL be integrated into portfolio governance.

---

# 186. Adaptive Dashboard

Should display:

```text
Signals
Triggers
Reassessments
Priorities
Rebalancing
Capacity
Risk
Benefits
```

---

# 187. Change Signal Dashboard

Should display:

```text
Open Signals
Age
Materiality
Confidence
Owner
Status
```

---

# 188. Rebalancing Dashboard

Should display:

```text
Pending Changes
Approved Changes
Active Changes
Verification
Outcome
```

---

# 189. Priority Dashboard

Should display:

```text
Current Priority
Previous Priority
Change
Reason
Impact
```

---

# 190. Adaptive Capacity Dashboard

Should display:

```text
Change Demand
Available Capacity
Saturation
Buffer
Bottleneck
```

---

# 191. Adaptive Risk Dashboard

Should display:

```text
New Risks
Changed Risks
Risk Concentration
Risk Reduction
```

---

# 192. Adaptive Benefit Dashboard

Should display:

```text
Benefit Change
Benefit Protection
Benefit Improvement
Benefit Erosion
```

---

# 193. Adaptive Heatmap

Conceptual:

```text
                    LOW       MEDIUM       HIGH       CRITICAL
STRATEGY              [ ]        [ ]         [ ]         [ ]
RISK                  [ ]        [ ]         [ ]         [ ]
BENEFIT               [ ]        [ ]         [ ]         [ ]
CAPACITY              [ ]        [ ]         [ ]         [ ]
DEPENDENCY            [ ]        [ ]         [ ]         [ ]
CHANGE LOAD           [ ]        [ ]         [ ]         [ ]
DECISION LATENCY      [ ]        [ ]         [ ]         [ ]
```

---

# 194. Adaptive Control Loop

Conceptual:

```text
        ┌──────────────────────┐
        │                      │
        ↓                      │
MONITOR → SIGNAL → ASSESS → DECIDE
                         ↓
                    REBALANCE
                         ↓
                     EXECUTE
                         ↓
                     VERIFY
                         ↓
                     LEARN
                         │
                         └──────────→ MONITOR
```

---

# 195. Portfolio Rebalancing Loop

Conceptual:

```text
CURRENT STATE
      ↓
NEW EVIDENCE
      ↓
OPTION SET
      ↓
TRADE-OFF
      ↓
AUTHORISED DECISION
      ↓
NEW PORTFOLIO STATE
      ↓
VERIFY
```

---

# 196. Strategic Rebalancing Loop

Conceptual:

```text
STRATEGY
   ↓
PORTFOLIO
   ↓
EVIDENCE
   ↓
ALIGNMENT TEST
   ↓
REBALANCE
   ↓
NEW PORTFOLIO
   ↓
STRATEGY
```

---

# 197. Optimisation Failure Chain

Conceptual:

```text
NARROW METRIC
   ↓
LOCAL OPTIMISATION
   ↓
HIDDEN TRADE-OFF
   ↓
CAPACITY / RISK IMPACT
   ↓
ENTERPRISE VALUE LOSS
```

---

# 198. Adaptation Failure Chain

Conceptual:

```text
CHANGE SIGNAL
   ↓
SIGNAL IGNORED
   ↓
REASSESSMENT DELAY
   ↓
PORTFOLIO DRIFT
   ↓
BENEFIT / RISK DETERIORATION
   ↓
LARGER CORRECTIVE CHANGE
```

---

# 199. Churn Failure Chain

Conceptual:

```text
FREQUENT CHANGE
   ↓
CHANGE FATIGUE
   ↓
ADOPTION LOSS
   ↓
REWORK
   ↓
CAPACITY LOSS
   ↓
PORTFOLIO PERFORMANCE LOSS
```

---

# 200. Adaptive Review

Review SHALL consider:

```text
Signals
Triggers
Priorities
Capacity
Risk
Benefits
Strategic Alignment
Change Load
```

---

# 201. Review Frequency

Frequency SHALL reflect:

```text
Volatility
Risk
Change Rate
Portfolio Criticality
```

---

# 202. Event-Driven Review

Events MAY include:

```text
Major Strategy Change
Critical Incident
Benefit Collapse
Capacity Shock
Regulatory Change
Major Dependency Failure
Critical Assurance Finding
```

---

# 203. Review Output

Output SHOULD include:

```text
Current State
Change Signals
Options
Trade-Offs
Decision
Actions
Verification
```

---

# 204. Adaptive Decision Forum

A formal decision forum SHOULD govern material portfolio rebalancing.

---

# 205. Decision Authority

Authority SHALL reflect:

```text
Materiality
Scope
Risk
Strategic Impact
```

---

# 206. Decision Transparency

Material rebalancing decisions SHALL remain traceable.

---

# 207. Reporting Integrity

Reports SHALL show:

```text
Positive
Negative
Unknown
Unintended
```

conditions.

---

# 208. Evidence Integrity

Adaptive decisions SHALL use evidence that is:

```text
Current
Traceable
Relevant
Sufficient
```

---

# 209. Evidence Conflict

Conflicting evidence SHALL be reconciled or explicitly presented.

---

# 210. Evidence Uncertainty

Uncertainty SHALL remain visible.

---

# 211. Historical Integrity

Adaptation SHALL not rewrite history.

---

# 212. Baseline Integrity

Old baselines SHALL remain reconstructable.

---

# 213. Method Versioning

Optimisation and prioritisation methods SHALL retain versions.

---

# 214. Historical Score Integrity

Method changes SHALL not silently rewrite prior priority results.

---

# 215. Comparability

Comparisons across time SHALL identify methodology changes.

---

# 216. AI-Assisted Adaptive Governance

AI MAY assist with:

```text
Signal Detection
Trend Detection
Priority Analysis
Scenario Generation
Optimisation Analysis
Capacity Forecasting
Dependency Analysis
Change Impact Analysis
```

---

# 217. AI Restrictions

AI SHALL not silently:

```text
Change Portfolio Priority
Approve Rebalancing
Allocate Material Capacity
Accept Material Risk
Stop Mandatory Work
Declare Optimal Portfolio
Override Strategic Authority
```

---

# 218. AI Explainability

Material AI outputs SHALL preserve:

```text
Model
Version
Input
Method
Output
Confidence
Human Review
```

---

# 219. AI Optimisation

AI-generated optimisation options SHALL be treated as decision support.

---

# 220. AI Signal Detection

AI-generated signals SHALL be validated before material action.

---

# 221. AI Forecasting

Forecasts SHALL retain assumptions and uncertainty.

---

# 222. Automation

Automation MAY support:

```text
Threshold Monitoring
Signal Registration
Priority Calculation
Dashboarding
Scenario Analysis
Change Notifications
```

---

# 223. Human Governance

Material adaptive decisions SHALL retain accountable human authority.

---

# 224. Security

Adaptive governance data SHALL be protected against:

```text
Signal Suppression
Priority Manipulation
Decision Manipulation
Historical Rewriting
Evidence Manipulation
```

---

# 225. Access Control

Access SHALL follow:

```text
Least Privilege
Need to Know
Role
Purpose
```

---

# 226. Audit Trail

Events MAY include:

```text
Signal Registered
Trigger Fired
Reassessment Started
Priority Changed
Option Created
Rebalancing Approved
Portfolio Changed
Baseline Created
Verification Completed
```

---

# 227. Failure Handling

If adaptive portfolio services fail:

```text
ADAPTIVE GOVERNANCE STATUS = DEGRADED
```

Manual reassessment SHALL remain available.

---

# 228. Manual Fallback

Manual fallback SHALL preserve:

```text
Signal
Evidence
Current State
Options
Decision
Authority
Change
Verification
```

---

# 229. Recovery

After service recovery:

```text
GAP
   ↓
RECONSTRUCT
   ↓
RECONCILE
   ↓
REASSESS
   ↓
RESTORE
```

---

# 230. Negative Testing

The system SHALL verify:

```text
Material signal without owner → BLOCK
Material signal without evidence → REVIEW
Mandatory trigger suppressed → BLOCK
Threshold trigger without response definition → BLOCK
Strategic change without reassessment → BLOCK
Benefit collapse without reassessment → BLOCK
Capacity shock without reassessment → BLOCK
Risk escalation without portfolio review → REVIEW
Priority change without criteria → BLOCK
Priority change without authority → BLOCK
Priority volatility hidden → BLOCK
Optimisation without constraints → BLOCK
Local optimum declared enterprise optimum → REVIEW / BLOCK
Hard constraint violated without exception → BLOCK
Sunk cost used as sole priority justification → BLOCK
Rebalancing without impact assessment → BLOCK
Rebalancing without authority → BLOCK
Rebalancing without verification → BLOCK
Temporary change without expiry → BLOCK
Emergency change without retrospective review → BLOCK
Portfolio churn above threshold without governance review → REVIEW
Unknown treated as stable → BLOCK
Not tested adaptation treated as adaptive → BLOCK
AI-generated priority treated as authorised → BLOCK
AI-generated optimisation treated as final decision → BLOCK
AI material capacity allocation treated as approved → BLOCK
Historical baseline overwritten → BLOCK
Method change silently rewriting historical scores → BLOCK
Manual fallback without audit trail → BLOCK
```

---

# 231. Scenario Testing

Representative scenarios:

```text
Stable portfolio
Major strategic change
Sudden capacity reduction
Critical dependency failure
Benefit collapse
Regulatory change
Major risk increase
Strong positive opportunity
Priority volatility
Portfolio churn
Change fatigue
Emergency rebalancing
Temporary rebalancing
Portfolio pause
Portfolio restart
Portfolio replacement
Local optimisation trap
Multi-objective conflict
Budget reduction
Technology disruption
AI signal detection
AI optimisation recommendation
Manual fallback
Post-rebalancing regression
```

---

# 232. Acceptance Criteria

EA-IMETA-PC-RG-444 is accepted when:

- material change signals can be detected, registered and assessed;
- trigger types and thresholds are explicit;
- signal confidence and uncertainty remain visible;
- strategic, risk, benefit, capacity and assurance changes can trigger reassessment;
- reassessment preserves the current state and historical baseline;
- current evidence, assumptions, dependencies, capacity and benefits are refreshed;
- dynamic prioritisation uses explicit and auditable criteria;
- priority volatility and priority gaming are detectable;
- optimisation considers multiple objectives and explicit constraints;
- local optimisation cannot silently be treated as enterprise optimisation;
- trade-offs and uncertainty remain visible;
- rebalancing decisions include evidence, impact, authority and rationale;
- material rebalancing is verified after execution;
- adaptive baselines preserve historical states;
- change ledgers provide complete traceability;
- portfolio churn and change fatigue are monitored;
- adaptive capacity is assessed;
- strategic rebalancing is triggered by material strategic change;
- emergency and temporary rebalancing are governed;
- adaptive assurance evaluates whether changes were timely, appropriate, authorised and effective;
- unintended and second-order effects are assessed;
- adaptation debt and reassessment debt are visible;
- portfolio learning feeds future adaptation;
- dashboards expose signals, triggers, priorities, capacity, risk, benefits and rebalancing;
- AI-assisted adaptation remains explainable and non-authoritative;
- manual fallback exists;
- historical methodologies and scores remain reconstructable;
- negative tests prevent unsupported claims of optimisation, stability, adaptability and enterprise optimum.

---

# 233. Next Step

The next logical artifact is the **PC-RG enterprise adaptive governance, predictive portfolio intelligence and anticipatory decision model**, because RG-444 establishes controlled reaction and rebalancing, while the next layer should extend the architecture from reactive adaptation toward evidence-based anticipation of future portfolio conditions.

Provisional next artifact:

> **EA-IMETA-PC-RG-445 — PREDICTIVE PORTFOLIO INTELLIGENCE, ANTICIPATORY GOVERNANCE & FORWARD-LOOKING DECISION MODEL**

This will establish the anticipatory governance layer above adaptive portfolio rebalancing.

---

# 234. Governing Principle

> **Adaptation is successful only when the portfolio changes neither too late nor too often: it must respond to material evidence early enough to protect enterprise value, but remain stable enough to execute, learn and sustain outcomes.**

The PC-RG architecture SHALL therefore treat adaptive portfolio governance as a controlled feedback system in which signals, evidence, prioritisation, optimisation, capacity, risk, strategy and benefits continuously inform the next authorised portfolio state without allowing either rigidity or uncontrolled churn to undermine enterprise outcomes.

# END OF EA-IMETA-PC-RG-444

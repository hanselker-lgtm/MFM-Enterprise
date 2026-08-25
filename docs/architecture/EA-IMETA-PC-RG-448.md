# EA-IMETA-PC-RG-448

## ENTERPRISE CRISIS DECISION, ADAPTIVE CONTINUITY & CONTROLLED DEGRADATION MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-448 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Enterprise Crisis Decision, Adaptive Continuity & Controlled Degradation Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-447 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Establish a controlled enterprise capability for crisis decision-making, continuity, graceful degradation, emergency authority, recovery prioritisation and transition back to stable operations when resilience thresholds are exceeded |
| Architectural Boundary | Resilience Intelligence → Crisis Trigger → Situational Assessment → Crisis Classification → Decision Authority → Controlled Degradation → Continuity → Containment → Recovery → Stabilisation → Verification → Learning |

---

# 2. Purpose

EA-IMETA-PC-RG-448 establishes the crisis decision and adaptive continuity layer above systemic resilience intelligence.

RG-447 establishes systemic exposure, dependency concentration, cascade paths, resilience thresholds and recovery capability.

RG-448 establishes how the enterprise governs itself when disruption becomes sufficiently material that normal operating arrangements are no longer adequate.

The architecture SHALL distinguish:

```text
CRISIS
= CONDITION WHERE NORMAL GOVERNANCE OR OPERATING CAPABILITY IS INSUFFICIENT TO CONTROL MATERIAL IMPACT WITHIN ACCEPTABLE LIMITS

CRISIS DECISION
= AUTHORISED DECISION TAKEN UNDER MATERIAL TIME, INFORMATION OR RESOURCE CONSTRAINT

ADAPTIVE CONTINUITY
= CAPABILITY TO MAINTAIN CRITICAL OUTCOMES THROUGH CONTROLLED CHANGES TO NORMAL OPERATING MODES

CONTROLLED DEGRADATION
= DELIBERATE REDUCTION OF NON-CRITICAL SERVICE OR CAPABILITY TO PROTECT CRITICAL FUNCTIONS

CRISIS MODE
= DEFINED OPERATING STATE WITH ALTERED GOVERNANCE, PRIORITIES, AUTHORITY OR RESOURCE ALLOCATION

NORMAL MODE
= STANDARD AUTHORISED OPERATING STATE

DEGRADED MODE
= CONTROLLED OPERATING STATE BELOW NORMAL CAPABILITY BUT ABOVE CRITICAL FAILURE

SURVIVAL MODE
= MINIMUM CONTROLLED STATE REQUIRED TO PRESERVE ESSENTIAL OUTCOMES

CRISIS THRESHOLD
= DEFINED CONDITION THAT REQUIRES TRANSITION TO CRISIS GOVERNANCE

CRISIS ACTIVATION
= AUTHORISED ENTRY INTO CRISIS MODE

CRISIS DEACTIVATION
= AUTHORISED EXIT FROM CRISIS MODE

EMERGENCY AUTHORITY
= TEMPORARY AUTHORITY TO MAKE DECISIONS FASTER OR DIFFERENTLY THAN NORMAL GOVERNANCE ALLOWS

DELEGATED AUTHORITY
= FORMAL TRANSFER OF SPECIFIED DECISION RIGHTS

DECISION LATENCY
= TIME BETWEEN REQUIRED DECISION POINT AND ACTUAL DECISION

CRISIS INFORMATION
= INFORMATION USED TO SUPPORT DECISION-MAKING DURING DISRUPTION

CRISIS UNCERTAINTY
= DEGREE TO WHICH THE CURRENT CONDITION, IMPACT OR FUTURE STATE IS UNKNOWN

DECISION WINDOW
= PERIOD DURING WHICH A DECISION CAN BE MADE WITHOUT UNACCEPTABLE LOSS OF OPTIONS

CONTAINMENT
= ACTION INTENDED TO LIMIT PROPAGATION OR ESCALATION OF IMPACT

CONTINUITY
= ABILITY TO MAINTAIN REQUIRED FUNCTIONS AT AN ACCEPTABLE LEVEL

RECOVERY
= RESTORATION OF REQUIRED FUNCTION AFTER DISRUPTION

STABILISATION
= RETURN TO A CONTROLLED OPERATING STATE BEFORE FULL NORMALISATION

RETURN TO NORMAL
= CONTROLLED TRANSITION FROM CRISIS OR DEGRADED MODE TO NORMAL OPERATIONS

CRISIS FATIGUE
= LOSS OF DECISION AND EXECUTION EFFECTIVENESS CAUSED BY PROLONGED CRISIS CONDITIONS

CRISIS OVERRIDE
= TEMPORARY DEPARTURE FROM NORMAL CONTROL ARRANGEMENTS UNDER DEFINED EMERGENCY AUTHORITY

OVERRIDE EXPIRY
= DEFINED POINT OR CONDITION AT WHICH AN EMERGENCY OVERRIDE ENDS OR MUST BE REAUTHORISED

CRISIS LEARNING
= CAPTURE AND APPLICATION OF LESSONS FROM CRISIS, CONTINUITY, DEGRADATION AND RECOVERY

CONTINUITY DEBT
= KNOWN CONTINUITY GAP NOT YET REMEDIATED

CRISIS GOVERNANCE DEBT
= KNOWN DEFICIENCY IN CRISIS AUTHORITY, PROCESS, INFORMATION OR DECISION CAPABILITY
```

---

# 3. Core Principle

> **During crisis, the enterprise SHALL prioritise protection of critical outcomes, containment of cascading impact, preservation of decision options and restoration of control, while ensuring that emergency authority remains bounded, traceable and temporary.**

The governing chain is:

```text
TRIGGER
  ↓
ACTIVATE
  ↓
ASSESS
  ↓
CLASSIFY
  ↓
PRIORITISE
  ↓
DECIDE
  ↓
DEGRADE / CONTINUE
  ↓
CONTAIN
  ↓
RECOVER
  ↓
STABILISE
  ↓
VERIFY
  ↓
RETURN TO NORMAL
  ↓
LEARN
```

---

# 4. Crisis Object

Minimum attributes:

```text
Crisis ID
Trigger
Classification
Scope
Impact
Current State
Critical Functions
Authority
Decisions
Actions
Recovery State
Status
```

---

# 5. Crisis Trigger Object

Minimum attributes:

```text
Trigger ID
Condition
Threshold
Evidence
Source
Time
Authority
Status
```

---

# 6. Crisis Decision Object

Minimum attributes:

```text
Decision ID
Situation
Options
Information
Uncertainty
Decision
Authority
Time
Expected Effect
Status
```

---

# 7. Continuity Object

Minimum attributes:

```text
Continuity ID
Critical Function
Normal State
Degraded State
Minimum State
Dependencies
Resources
Recovery
Owner
Status
```

---

# 8. Degradation Object

Minimum attributes:

```text
Degradation ID
Function
Trigger
Reduced Capability
Protected Capability
Duration
Authority
Exit Criteria
Status
```

---

# 9. Recovery Object

Minimum attributes:

```text
Recovery ID
Disruption
Target
Sequence
Dependencies
Resources
Verification
Residual Risk
Status
```

---

# 10. Crisis Authority Object

Minimum attributes:

```text
Authority ID
Role
Decision Rights
Scope
Conditions
Start
Expiry
Delegation
Status
```

---

# 11. Lifecycle

```text
PREPARE
   ↓
DETECT
   ↓
ACTIVATE
   ↓
ASSESS
   ↓
PRIORITISE
   ↓
DECIDE
   ↓
CONTAIN
   ↓
CONTINUE / DEGRADE
   ↓
RECOVER
   ↓
STABILISE
   ↓
VERIFY
   ↓
NORMALISE
   ↓
LEARN
```

Alternative states:

```text
NORMAL
WATCH
CRISIS CANDIDATE
ACTIVATED
DEGRADED
CONTAINED
RECOVERING
STABILISING
NORMALISING
CLOSED
UNKNOWN
```

---

# 12. Crisis Governance Boundary

The crisis architecture SHALL define:

```text
Activation
Authority
Scope
Priorities
Decision Rights
Communication
Continuity
Recovery
Exit
```

---

# 13. Crisis Classification

Classification SHOULD consider:

```text
Impact
Breadth
Velocity
Duration
Uncertainty
Recovery Difficulty
```

---

# 14. Crisis Levels

Example:

```text
LEVEL 0 = NORMAL
LEVEL 1 = ELEVATED
LEVEL 2 = SIGNIFICANT
LEVEL 3 = MAJOR
LEVEL 4 = ENTERPRISE CRISIS
```

Definitions SHALL be explicit.

---

# 15. Activation Threshold

Each crisis level SHALL have activation criteria.

---

# 16. Activation Authority

Activation authority SHALL be explicit.

---

# 17. Automatic Activation

Automatic activation MAY be used for predefined critical conditions.

---

# 18. Automatic Activation Controls

Automatic activation SHALL have:

```text
Trigger
Scope
Authority
Fallback
Review
```

---

# 19. Activation Logging

Every crisis activation SHALL be logged.

---

# 20. Activation Challenge

Where practical, activation SHALL be validated without delaying necessary response.

---

# 21. Crisis Escalation

Escalation SHALL reflect:

```text
Impact
Velocity
Breadth
Uncertainty
Irreversibility
```

---

# 22. Crisis De-Escalation

De-escalation SHALL require evidence that conditions have improved sufficiently.

---

# 23. Crisis Deactivation

Deactivation SHALL be authorised.

---

# 24. Deactivation Criteria

Possible:

```text
Critical Functions Stable
Propagation Controlled
Recovery Established
Residual Risk Acceptable
Governance Restored
```

---

# 25. Decision Authority

Crisis authority SHALL remain accountable.

---

# 26. Emergency Authority

Emergency authority SHALL be:

```text
Defined
Bounded
Temporary
Traceable
Reviewable
```

---

# 27. Delegated Authority

Delegation SHALL specify:

```text
Who
What
Scope
Conditions
Duration
```

---

# 28. Authority Expiry

Emergency authority SHALL have expiry or review conditions.

---

# 29. Authority Extension

Extension SHALL require explicit reauthorisation.

---

# 30. Authority Conflict

Conflicting authorities SHALL have precedence rules.

---

# 31. Crisis Override

Overrides SHALL be used only where necessary.

---

# 32. Override Logging

Every material override SHALL record:

```text
Reason
Authority
Scope
Time
Impact
```

---

# 33. Override Review

Overrides SHALL receive retrospective review.

---

# 34. Override Abuse

Repeated or unjustified overrides SHALL trigger governance review.

---

# 35. Crisis Information

Crisis information SHALL distinguish:

```text
KNOWN
ESTIMATED
FORECAST
UNKNOWN
CONTRADICTORY
```

---

# 36. Information Freshness

Critical crisis information SHALL be refreshed at appropriate intervals.

---

# 37. Information Confidence

Confidence SHALL remain visible.

---

# 38. Information Conflict

Conflicting information SHALL be retained until resolved.

---

# 39. Crisis Common Picture

A common operating picture SHOULD provide:

```text
Current State
Critical Functions
Impacts
Dependencies
Actions
Decisions
Unknowns
```

---

# 40. Crisis Information Minimum

At minimum:

```text
WHAT HAPPENED
WHAT IS AFFECTED
WHAT IS CRITICAL
WHAT IS UNKNOWN
WHAT IS BEING DONE
WHO DECIDES
WHAT HAPPENS NEXT
```

---

# 41. Situational Assessment

Initial assessment SHALL establish:

```text
Scope
Impact
Velocity
Critical Functions
Dependencies
Immediate Threats
Available Options
```

---

# 42. Rapid Assessment

Rapid assessment SHOULD occur before full information is available.

---

# 43. Assessment Update

Assessments SHALL be updated as evidence changes.

---

# 44. Assessment Versioning

Material assessment changes SHALL be traceable.

---

# 45. Crisis Uncertainty

Uncertainty SHALL not automatically prevent action where delay creates material harm.

---

# 46. Decision Under Uncertainty

Decision-making SHALL balance:

```text
Speed
Evidence
Risk
Reversibility
```

---

# 47. Last Responsible Moment

The decision process SHOULD identify the latest safe decision point.

---

# 48. Option Preservation

Decisions SHOULD preserve future options where uncertainty remains high.

---

# 49. Reversible Decision

Reversible actions MAY be preferred under uncertainty.

---

# 50. Irreversible Decision

Irreversible actions SHOULD require stronger evidence or higher authority.

---

# 51. Decision Latency

Decision latency SHALL be monitored for critical decisions.

---

# 52. Decision Escalation

Unresolved decisions SHALL escalate according to defined rules.

---

# 53. Decision Logging

Material crisis decisions SHALL be logged.

---

# 54. Decision Rationale

Decision records SHOULD capture:

```text
Situation
Evidence
Uncertainty
Options
Rationale
Authority
Expected Outcome
```

---

# 55. Crisis Priorities

Priority hierarchy SHOULD begin with:

```text
SAFETY / LIFE
      ↓
CRITICAL FUNCTIONS
      ↓
CONTAINMENT
      ↓
INFORMATION INTEGRITY
      ↓
RECOVERY OPTIONS
      ↓
SERVICE RESTORATION
      ↓
NORMALISATION
```

The enterprise SHALL adapt the hierarchy to its legal and operational context.

---

# 56. Critical Function Protection

Critical functions SHALL receive priority over non-critical functions during constrained capacity.

---

# 57. Resource Allocation

Crisis resource allocation SHALL be explicit.

---

# 58. Resource Reallocation

Resources MAY be moved from lower-priority activities to critical functions.

---

# 59. Resource Trade-Off

Trade-offs SHALL remain visible.

---

# 60. Resource Reserve

Protected reserves MAY be activated under defined conditions.

---

# 61. Reserve Authority

Reserve activation SHALL have explicit authority.

---

# 62. Controlled Degradation

Controlled degradation SHALL protect critical outcomes by reducing non-critical capability.

---

# 63. Degradation Principle

```text
PROTECT CRITICAL
REDUCE NON-CRITICAL
CONTAIN PROPAGATION
PRESERVE RECOVERY
```

---

# 64. Degradation Levels

Possible:

```text
NORMAL
REDUCED
MINIMUM
SURVIVAL
```

---

# 65. Degradation Criteria

Each level SHALL define:

```text
Entry
Capabilities
Restrictions
Owner
Exit
```

---

# 66. Graceful Degradation

Where possible, services SHOULD degrade progressively rather than fail abruptly.

---

# 67. Degradation Ordering

Non-critical capability SHOULD be reduced before critical capability.

---

# 68. Degradation Dependencies

Degradation SHALL consider dependent functions.

---

# 69. Degradation Communication

Affected stakeholders SHALL receive appropriate information.

---

# 70. Degradation Duration

Material degradation SHALL have expected or reviewable duration.

---

# 71. Degradation Expiry

Temporary degradation SHALL be reviewed and exited when conditions permit.

---

# 72. Survival Mode

Survival mode SHALL represent the minimum controlled operating state.

---

# 73. Survival Mode Authority

Entry into survival mode SHALL have explicit authority.

---

# 74. Survival Mode Controls

Essential controls SHALL remain active.

---

# 75. Continuity

Continuity SHALL preserve critical outcomes rather than merely preserve normal processes.

---

# 76. Continuity Objective

Each critical function SHOULD define:

```text
Normal
Degraded
Minimum
Recovery
```

---

# 77. Continuity Dependencies

Critical continuity plans SHALL identify dependencies.

---

# 78. Continuity Alternatives

Alternatives MAY include:

```text
Manual
Remote
Secondary Site
Alternative Supplier
Alternative Process
Reduced Service
```

---

# 79. Continuity Capacity

Continuity plans SHALL be supported by realistic capacity.

---

# 80. Continuity Testing

Material continuity arrangements SHOULD be tested.

---

# 81. Continuity Evidence

Continuity claims SHALL be supported by evidence.

---

# 82. Continuity Debt

Known continuity gaps SHALL be recorded.

---

# 83. Crisis Containment

Containment SHALL focus on limiting:

```text
Spread
Cascade
Resource Drain
Information Loss
Decision Loss
```

---

# 84. Containment Point

Critical containment points SHALL be identified.

---

# 85. Containment Failure

Containment failure SHALL trigger escalation.

---

# 86. Containment Verification

Containment SHALL be verified.

---

# 87. Crisis Communication

Communication SHALL be:

```text
Timely
Accurate
Relevant
Consistent
Uncertainty-Aware
```

---

# 88. Communication Authority

Crisis communication authority SHALL be explicit.

---

# 89. Communication Fallback

Critical communication channels SHALL have alternatives.

---

# 90. Communication Integrity

Material information SHALL not be intentionally distorted.

---

# 91. Crisis Decision Forum

A crisis decision forum SHOULD be established for material events.

---

# 92. Forum Composition

Composition SHALL reflect the crisis, not organisational hierarchy alone.

---

# 93. Decision Rhythm

Crisis decision cadence SHALL reflect:

```text
Velocity
Impact
Decision Latency
```

---

# 94. Decision Rhythm Overload

Excessive meeting cadence SHALL not replace actual decision-making.

---

# 95. Crisis Fatigue

Crisis fatigue SHALL be monitored.

---

# 96. Human Capacity

Crisis staffing SHALL consider:

```text
Hours
Skills
Fatigue
Redundancy
Succession
```

---

# 97. Shift Rotation

Prolonged crisis operations SHOULD use controlled rotation where feasible.

---

# 98. Key Person Risk

Critical decisions SHALL not depend indefinitely on one individual.

---

# 99. Crisis Succession

Critical crisis roles SHOULD have alternates.

---

# 100. Crisis Knowledge

Decision knowledge SHALL be captured during prolonged events.

---

# 101. Crisis Decision Record

Material decisions SHALL preserve:

```text
Time
Decision
Authority
Evidence
Rationale
Outcome
```

---

# 102. Crisis Action Register

Actions SHALL be tracked with:

```text
Owner
Priority
Deadline
Dependency
Status
```

---

# 103. Action Escalation

Overdue critical actions SHALL escalate.

---

# 104. Action Verification

Critical actions SHALL be verified.

---

# 105. Recovery

Recovery SHALL be planned from the beginning of crisis where practical.

---

# 106. Recovery Objective

Recovery objectives SHALL define target state.

---

# 107. Recovery Sequence

Recovery sequence SHALL reflect:

```text
Dependencies
Criticality
Safety
Capacity
```

---

# 108. Recovery Critical Path

Critical recovery dependencies SHALL remain visible.

---

# 109. Recovery Bottleneck

Bottlenecks SHALL be actively managed.

---

# 110. Recovery Resource Allocation

Critical recovery SHALL receive appropriate resources.

---

# 111. Recovery Verification

Restoration SHALL be verified before full normalisation.

---

# 112. Recovery Quality

Recovery SHALL restore required capability, not simply system availability.

---

# 113. Residual Risk

Residual risk SHALL be assessed before return to normal.

---

# 114. Stabilisation

Stabilisation SHALL establish a controlled state between crisis and normal operations.

---

# 115. Stabilisation Criteria

Possible:

```text
Critical Functions Stable
Dependencies Stable
Recovery Controlled
Decision Load Reduced
Residual Risk Known
```

---

# 116. Stabilisation Duration

Stabilisation SHALL continue until evidence supports normalisation.

---

# 117. Return to Normal

Normalisation SHALL be controlled.

---

# 118. Normalisation Criteria

Possible:

```text
Critical Functions Normal
Controls Restored
Emergency Authority Ended
Residual Risk Accepted
Continuity Mode Closed
```

---

# 119. Normalisation Verification

Return to normal SHALL be verified.

---

# 120. Emergency Authority Closure

Emergency authority SHALL end when no longer necessary.

---

# 121. Override Closure

Temporary overrides SHALL be closed or formally extended.

---

# 122. Residual Crisis State

Residual issues SHALL transfer into normal governance.

---

# 123. Post-Crisis Review

Material crises SHALL receive structured post-crisis review.

---

# 124. Review Timing

Review SHALL occur after sufficient stabilisation to support meaningful analysis.

---

# 125. Review Scope

Review SHOULD cover:

```text
Trigger
Decisions
Authority
Continuity
Degradation
Containment
Recovery
Communication
Outcomes
```

---

# 126. Hindsight Protection

Historical decision review SHALL use information available at the decision time.

---

# 127. Outcome Bias Protection

Good or bad outcomes SHALL not alone determine decision quality.

---

# 128. Crisis Learning

Learning SHALL identify:

```text
What Worked
What Failed
What Was Unknown
What Was Late
What Was Missing
```

---

# 129. Corrective Actions

Learning SHALL produce accountable actions.

---

# 130. Resilience Feedback

Crisis lessons SHALL feed RG-447 resilience intelligence.

---

# 131. Early-Warning Feedback

Crisis lessons SHALL feed RG-446 early-warning capability.

---

# 132. Predictive Feedback

Crisis lessons SHALL feed RG-445 predictive models and assumptions.

---

# 133. Adaptive Feedback

Crisis lessons SHALL feed RG-444 portfolio adaptation.

---

# 134. Assurance Feedback

Crisis lessons SHALL feed RG-443 assurance.

---

# 135. Orchestration Feedback

Crisis lessons SHALL feed RG-442 orchestration.

---

# 136. Systemic Feedback

Crisis lessons SHALL feed RG-441 systemic integration.

---

# 137. Crisis Governance Debt

Known crisis governance gaps SHALL be recorded.

---

# 138. Crisis Debt Aging

Debt SHALL be monitored by:

```text
Age
Criticality
Impact
Likelihood
```

---

# 139. Crisis Exercise

Material crisis arrangements SHOULD be exercised.

---

# 140. Exercise Types

Possible:

```text
TABLETOP
SIMULATION
WALKTHROUGH
TECHNICAL TEST
FULL EXERCISE
```

---

# 141. Exercise Objectives

Exercises SHALL have defined objectives.

---

# 142. Exercise Evidence

Exercise results SHALL be recorded.

---

# 143. Exercise Failure

Exercise failure SHALL trigger remediation.

---

# 144. Exercise Repetition

Repeated exercise without remediation SHALL be treated as governance failure.

---

# 145. Crisis Readiness

Readiness SHALL be assessed using evidence, not documentation alone.

---

# 146. Crisis Readiness Levels

Possible:

```text
READY
CONDITIONAL
DEGRADED
NOT READY
UNKNOWN
```

---

# 147. Readiness Dashboard

Should display:

```text
Critical Functions
Authority
Continuity
Degradation
Recovery
Exercises
Open Gaps
```

---

# 148. Crisis Dashboard

Should display:

```text
Current State
Impact
Critical Functions
Decisions
Actions
Unknowns
Recovery
```

---

# 149. Degradation Dashboard

Should display:

```text
Function
Normal State
Current State
Protected Capability
Restrictions
Exit Criteria
```

---

# 150. Recovery Dashboard

Should display:

```text
Target
Current
Critical Path
Bottleneck
Progress
Residual Risk
```

---

# 151. Crisis Heatmap

Conceptual:

```text
                     LOW        MEDIUM        HIGH       CRITICAL
IMPACT                 [ ]         [ ]          [ ]         [ ]
VELOCITY               [ ]         [ ]          [ ]         [ ]
UNCERTAINTY             [ ]         [ ]          [ ]         [ ]
CASCADE                 [ ]         [ ]          [ ]         [ ]
CAPACITY                [ ]         [ ]          [ ]         [ ]
RECOVERY                [ ]         [ ]          [ ]         [ ]
DECISION LATENCY        [ ]         [ ]          [ ]         [ ]
```

---

# 152. Crisis Control Loop

Conceptual:

```text
TRIGGER
   ↓
ACTIVATE
   ↓
ASSESS
   ↓
PRIORITISE
   ↓
DECIDE
   ↓
CONTAIN
   ↓
DEGRADE / CONTINUE
   ↓
RECOVER
   ↓
STABILISE
   ↓
VERIFY
   ↓
NORMALISE
   ↓
LEARN
```

---

# 153. Controlled Degradation Loop

```text
NORMAL
  ↓
THRESHOLD
  ↓
REDUCE NON-CRITICAL
  ↓
PROTECT CRITICAL
  ↓
MONITOR
  ↓
RECOVER
  ↓
RESTORE
```

---

# 154. Crisis Decision Loop

```text
SITUATION
   ↓
INFORMATION
   ↓
UNCERTAINTY
   ↓
OPTIONS
   ↓
AUTHORITY
   ↓
DECISION
   ↓
ACTION
   ↓
OUTCOME
```

---

# 155. Crisis Escalation Chain

```text
WATCH
 ↓
ELEVATED
 ↓
SIGNIFICANT
 ↓
MAJOR
 ↓
ENTERPRISE CRISIS
```

---

# 156. Crisis Failure Chain

```text
EARLY SIGNAL
   ↓
DELAYED ACTIVATION
   ↓
DECISION LATENCY
   ↓
CASCADE
   ↓
CAPACITY LOSS
   ↓
RECOVERY DELAY
```

---

# 157. Degradation Failure Chain

```text
NO DEGRADATION PLAN
   ↓
NON-CRITICAL LOAD REMAINS
   ↓
CRITICAL CAPACITY CONSUMED
   ↓
CRITICAL FUNCTION FAILURE
```

---

# 158. Authority Failure Chain

```text
UNCLEAR AUTHORITY
   ↓
DECISION DELAY
   ↓
CONFLICT
   ↓
ESCALATION DELAY
   ↓
IMPACT AMPLIFICATION
```

---

# 159. Recovery Failure Chain

```text
RECOVERY START
   ↓
WRONG SEQUENCE
   ↓
DEPENDENCY FAILURE
   ↓
REWORK
   ↓
RECOVERY DELAY
```

---

# 160. Crisis Review

Review SHALL consider:

```text
Activation
Authority
Information
Decisions
Degradation
Continuity
Containment
Recovery
Normalisation
Learning
```

---

# 161. Review Frequency

Frequency SHALL reflect:

```text
Crisis Duration
Decision Velocity
Impact
Uncertainty
```

---

# 162. Event-Driven Review

Triggers MAY include:

```text
Major Escalation
Critical Decision
Containment Failure
Recovery Failure
Authority Override
Return to Normal
```

---

# 163. Decision Authority

Authority SHALL reflect:

```text
Impact
Urgency
Scope
Reversibility
```

---

# 164. Reporting Integrity

Crisis reporting SHALL distinguish:

```text
CONFIRMED
ESTIMATED
FORECAST
UNKNOWN
CONTRADICTORY
```

---

# 165. Crisis Communication Integrity

Material uncertainty SHALL not be intentionally hidden.

---

# 166. Security

Crisis information SHALL be protected while remaining accessible to authorised decision makers.

---

# 167. Crisis Information Classification

Sensitive crisis information SHOULD be classified appropriately.

---

# 168. Access Control

Access SHALL follow:

```text
Least Privilege
Need to Know
Role
Purpose
```

---

# 169. Crisis Audit Trail

All material crisis decisions and overrides SHALL be auditable.

---

# 170. AI-Assisted Crisis Support

AI MAY assist with:

```text
Situational Summarisation
Dependency Analysis
Option Generation
Resource Analysis
Recovery Sequencing
Scenario Analysis
Information Correlation
```

---

# 171. AI Restrictions

AI SHALL not silently:

```text
Declare Crisis Activation
Assume Emergency Authority
Override Human Decisions
Deprioritise Critical Functions
Approve Irreversible Crisis Actions
Declare Recovery Complete
Declare Crisis Resolved
```

---

# 172. AI Explainability

Material AI-supported crisis outputs SHALL preserve:

```text
Inputs
Method
Model
Version
Output
Confidence
Uncertainty
Human Review
```

---

# 173. AI Crisis Hallucination Control

Unverified AI-generated information SHALL not be treated as operational fact.

---

# 174. AI Fallback

Critical AI-supported crisis functions SHALL have non-AI fallback.

---

# 175. Automation

Automation MAY support:

```text
Threshold Detection
Activation Notification
Action Tracking
Recovery Tracking
Dashboarding
Communication Routing
```

---

# 176. Human Governance

Material crisis decisions SHALL retain accountable human authority.

---

# 177. Failure Handling

If crisis governance technology fails:

```text
CRISIS GOVERNANCE STATUS = DEGRADED
```

Manual crisis procedures SHALL remain available.

---

# 178. Manual Fallback

Manual fallback SHALL preserve:

```text
Authority
Situation
Decision
Action
Communication
Recovery
Audit
```

---

# 179. Recovery of Governance Services

After technology recovery:

```text
GAP
   ↓
RECONSTRUCT
   ↓
RECONCILE
   ↓
VALIDATE
   ↓
RESTORE
```

---

# 180. Negative Testing

The system SHALL verify:

```text
Crisis trigger without criteria → BLOCK
Crisis activation without authority → BLOCK
Crisis level without definition → BLOCK
Emergency authority without scope → BLOCK
Emergency authority without expiry → BLOCK
Override without rationale → BLOCK
Override without logging → BLOCK
Conflicting authorities without precedence → BLOCK
Critical decision without owner → BLOCK
Critical decision without decision record → BLOCK
Unknown treated as confirmed → BLOCK
Unverified information treated as fact → BLOCK
Critical function without continuity state → BLOCK
Degradation without exit criteria → BLOCK
Degradation of critical function without authority → BLOCK
Non-critical load not reduced during constrained capacity → REVIEW
Recovery without critical path → BLOCK
Recovery without verification → BLOCK
Return to normal without residual risk assessment → BLOCK
Emergency authority not closed after crisis → BLOCK
Crisis exercise without objectives → REVIEW
Repeated exercise failure without remediation → BLOCK
AI-generated crisis activation treated as authorised → BLOCK
AI-generated recovery completion treated as fact → BLOCK
Manual fallback without audit trail → BLOCK
Historical crisis decision overwritten → BLOCK
```

---

# 181. Scenario Testing

Representative scenarios:

```text
Rapid operational crisis
Slow-building crisis
Multiple simultaneous failures
Common-mode failure
Critical supplier loss
Technology outage
Communication outage
Capacity shock
Cyber-related disruption
Regulatory emergency
Financial shock
Geographic disruption
Critical person loss
Compound crisis
Crisis during planned transformation
Crisis during recovery
Prolonged crisis
Decision under severe uncertainty
Authority conflict
Emergency override
Controlled degradation
Survival mode
Recovery bottleneck
Return-to-normal failure
AI support failure
Manual fallback
Post-crisis learning
```

---

# 182. Acceptance Criteria

EA-IMETA-PC-RG-448 is accepted when:

- crisis activation thresholds and authority are explicit;
- crisis levels are defined;
- emergency authority is bounded, temporary and traceable;
- delegated authority includes scope, conditions and expiry;
- crisis information distinguishes known, estimated, forecast and unknown;
- a common operating picture can be maintained;
- decision latency and decision windows are visible;
- critical functions receive explicit priority;
- controlled degradation can protect critical outcomes;
- degraded and survival modes are defined;
- continuity arrangements identify normal, degraded, minimum and recovery states;
- containment points are identified;
- crisis communication is governed;
- recovery starts from defined objectives and critical paths;
- recovery is verified before normalisation;
- residual risk is assessed before return to normal;
- emergency overrides are closed or reauthorised;
- crisis exercises test real decision and continuity capability;
- repeated exercise failures create remediation obligations;
- crisis governance debt and continuity debt are visible;
- post-crisis learning feeds RG-441 through RG-447;
- AI-assisted crisis support remains non-authoritative and explainable;
- manual fallback exists;
- historical crisis decisions remain reconstructable;
- negative tests prevent unsupported claims of authority, continuity, recovery and crisis resolution.

---

# 183. Next Step

The next logical artifact is the **PC-RG enterprise recovery orchestration, restoration sequencing and post-crisis stabilisation model**.

Provisional next artifact:

> **EA-IMETA-PC-RG-449 — ENTERPRISE RECOVERY ORCHESTRATION, RESTORATION SEQUENCING & POST-CRISIS STABILISATION MODEL**

This will establish the coordinated recovery layer above crisis continuity and degradation.

---

# 184. Governing Principle

> **Crisis governance is successful when the enterprise protects critical outcomes, contains propagation, makes timely and accountable decisions under uncertainty, deliberately degrades non-critical capability when necessary, preserves recovery options and returns to stable operations through verified rather than assumed recovery.**

The PC-RG architecture SHALL therefore treat crisis mode as a controlled temporary state—not an alternative permanent operating model—and SHALL require explicit activation, bounded authority, controlled degradation, continuity, recovery, stabilisation, verification and learning.

# END OF EA-IMETA-PC-RG-448

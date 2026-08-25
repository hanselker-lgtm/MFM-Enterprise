# EA-IMETA-PC-RG-428

## RECURRENCE, SYSTEMIC-RISK & CROSS-CASE PATTERN MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-428 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Recurrence, Systemic-Risk & Cross-Case Pattern Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-427 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Detect, correlate and govern recurring conditions, systemic weaknesses and cross-case patterns across exceptions, findings, incidents, remediations and closed decisions |
| Architectural Boundary | Case → Recurrence → Correlation → Pattern → Systemic Risk → Enterprise Assessment → Improvement → Verification |

---

# 2. Purpose

EA-IMETA-PC-RG-428 defines the cross-case intelligence and systemic-risk layer above individual exception, remediation and closure records.

RG-427 establishes how an individual exception is remediated, closed and converted into learning.

RG-428 establishes **how multiple cases are compared to determine whether they represent recurrence, common cause, systemic weakness or enterprise-level risk**.

The architecture SHALL distinguish:

```text
RECURRENCE
= REAPPEARANCE OF A MATERIAL CONDITION OR RELATED CONDITION

PATTERN
= REPEATED OR CORRELATED CHARACTERISTICS ACROSS CASES

COMMON CAUSE
= A SHARED FACTOR CONTRIBUTING TO MULTIPLE CASES

SYSTEMIC WEAKNESS
= A STRUCTURAL CONDITION THAT CAN PRODUCE OR AMPLIFY MULTIPLE FAILURES

SYSTEMIC RISK
= RISK ARISING FROM A CONDITION THAT MAY AFFECT MULTIPLE OBJECTS, CONTROLS OR DECISIONS

CROSS-CASE CORRELATION
= GOVERNED ASSOCIATION OF INFORMATION FROM MULTIPLE CASES

ENTERPRISE IMPROVEMENT
= ACTION DESIGNED TO REDUCE A PATTERN OR SYSTEMIC RISK ACROSS A DEFINED POPULATION
```

---

# 3. Core Principle

> **A repeated local failure may be evidence of a systemic condition; governance must therefore learn across cases rather than treating every recurrence as an isolated event.**

The governing chain is:

```text
CASE
   ↓
CROSS-CASE CORRELATION
   ↓
RECURRENCE
   ↓
PATTERN
   ↓
COMMON CAUSE
   ↓
SYSTEMIC RISK
   ↓
ASSESSMENT
   ↓
ENTERPRISE ACTION
   ↓
VERIFICATION
   ↓
PATTERN REDUCTION
```

---

# 4. Cross-Case Object

Every material cross-case relationship SHALL be represented as a controlled object.

Minimum attributes:

```text
Pattern ID
Cases
Population
Relationship
Pattern Type
Evidence
Confidence
Risk
Materiality
Common Cause
Systemic Assessment
Owner
Decision
Actions
Status
Review Date
```

---

# 5. Recurrence Object

A recurrence object SHALL identify:

```text
Original Case
Subsequent Case
Common Condition
Time Relationship
Similarity
Materiality
Cause Relationship
Evidence
```

Recurrence SHALL not be inferred solely from similar titles or keywords.

---

# 6. Recurrence Lifecycle

```text
IDENTIFIED
   ↓
CORRELATED
   ↓
ASSESSED
   ↓
CONFIRMED / REJECTED
   ↓
SYSTEMIC REVIEW
   ↓
ACTION
   ↓
VERIFIED
   ↓
CLOSED
```

Alternative states:

```text
SUSPECTED
UNCONFIRMED
MONITORED
ESCALATED
REOPENED
```

---

# 7. Recurrence Types

Recurrence MAY be:

```text
EXACT
FUNCTIONAL
CAUSAL
CONTROL
CONFIGURATION
PROCESS
POLICY
DEPENDENCY
TEMPORAL
BEHAVIOURAL
MODEL
```

---

# 8. Exact Recurrence

The same condition reappears materially unchanged.

Example:

```text
SAME FAILURE
+
SAME CONTROL
+
SAME CONDITION
```

---

# 9. Functional Recurrence

Different technical symptoms produce the same material outcome.

```text
FAILURE A
FAILURE B
FAILURE C
   ↓
SAME OUTCOME
```

---

# 10. Causal Recurrence

Different cases share a common underlying cause.

```text
CASE A ─┐
CASE B ─┼→ COMMON CAUSE
CASE C ─┘
```

---

# 11. Control Recurrence

Multiple cases reveal weakness in the same control.

---

# 12. Configuration Recurrence

Multiple cases reveal repeated configuration drift or configuration error.

---

# 13. Process Recurrence

Multiple cases reveal repeated process failure.

---

# 14. Policy Recurrence

Multiple cases reveal repeated exceptions or deviations caused by the same policy condition.

---

# 15. Dependency Recurrence

Multiple cases are linked to the same dependency.

---

# 16. Temporal Recurrence

A condition repeatedly occurs within a particular period, cycle or operating phase.

---

# 17. Behavioural Recurrence

Repeated behaviour by users, systems or processes contributes to similar outcomes.

---

# 18. Model Recurrence

AI/ML systems may exhibit repeated failure modes across:

```text
Model Versions
Datasets
Prompts
Tools
Tasks
Environments
```

---

# 19. Pattern Object

A pattern SHALL describe:

```text
Population
Observed Similarities
Differences
Relationship
Evidence
Confidence
Materiality
Risk
```

---

# 20. Pattern Confidence

Pattern confidence MAY be:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

Confidence SHALL be evidence-based.

---

# 21. Pattern vs Coincidence

Similarity does not prove common cause.

```text
SIMILAR
≠
CAUSALLY RELATED
```

The architecture SHALL preserve this distinction.

---

# 22. Pattern Evidence

Evidence MAY include:

```text
Cases
Timelines
Configurations
Controls
Dependencies
Decisions
Logs
Metrics
Remediation
Lessons
```

---

# 23. Pattern Scope

Pattern scope SHALL define:

```text
Population
Environment
Systems
Processes
Controls
Time Period
```

---

# 24. Pattern Detection

Patterns MAY be detected through:

```text
Rule-Based Analysis
Statistical Analysis
Graph Analysis
Historical Comparison
Manual Review
AI-Assisted Analysis
```

---

# 25. Pattern Detection Governance

Detection methods SHALL preserve:

```text
Method
Version
Inputs
Criteria
Result
Confidence
```

---

# 26. Similarity Model

Similarity MAY compare:

```text
Root Cause
Control
Requirement
Configuration
Dependency
Outcome
Impact
Timeline
```

---

# 27. Keyword Similarity

Keyword similarity MAY be used for discovery.

It SHALL not alone establish recurrence or systemic risk.

---

# 28. Semantic Similarity

Semantic analysis MAY identify conceptually similar cases.

Material conclusions SHALL retain human-governed assessment where required.

---

# 29. Graph Correlation

A graph MAY represent:

```text
CASE
 ↓
CAUSE
 ↓
CONTROL
 ↓
SYSTEM
 ↓
DEPENDENCY
 ↓
OUTCOME
```

Cross-case graph intersections MAY reveal systemic patterns.

---

# 30. Pattern Threshold

A policy MAY define thresholds such as:

```text
COUNT
FREQUENCY
IMPACT
RISK
RECURRENCE RATE
```

Thresholds SHALL not replace professional judgment.

---

# 31. Recurrence Frequency

Frequency SHOULD consider:

```text
Occurrences
Population Size
Time
Exposure
Criticality
```

Ten occurrences in a population of ten million may differ materially from ten occurrences in a population of fifty.

---

# 32. Recurrence Severity

Severity SHALL consider:

```text
Impact
Risk
Duration
Scope
Reliance
Control Failure
```

---

# 33. Recurrence Velocity

Velocity MAY measure how quickly recurrence appears after remediation or closure.

High recurrence velocity MAY indicate ineffective remediation.

---

# 34. Recurrence Density

Density MAY measure cases per:

```text
Time
Population
System
Control
Transaction
Decision
```

---

# 35. Recurrence After Closure

A recurrence after closure SHALL be linked to the original case.

```text
CLOSED CASE
   ↓
RECURRENCE
   ↓
NEW CASE / REOPEN REVIEW
```

Historical closure SHALL not be rewritten.

---

# 36. Recurrence After Remediation

If recurrence occurs after remediation:

```text
REMEDIATION
   ↓
RECURRENCE
   ↓
EFFECTIVENESS REVIEW
```

---

# 37. Remediation Effectiveness

Repeated recurrence MAY indicate:

```text
Wrong Root Cause
Weak Action
Incomplete Scope
Control Failure
External Dependency
```

---

# 38. Systemic Assessment

A systemic assessment SHALL determine whether:

```text
LOCAL ISSUE
OR
COMMON PATTERN
OR
SYSTEMIC WEAKNESS
```

---

# 39. Systemic Risk Object

Minimum attributes:

```text
Systemic Risk ID
Pattern
Population
Risk
Drivers
Dependencies
Controls
Exposure
Owner
Mitigations
Decision
Status
```

---

# 40. Systemic Risk Drivers

Drivers MAY include:

```text
Architecture
Technology
Process
Policy
People
Dependency
Data
Control
Governance
Culture
```

---

# 41. Systemic Risk Scope

Scope MAY be:

```text
SERVICE
DOMAIN
BUSINESS UNIT
ENTERPRISE
ECOSYSTEM
```

---

# 42. Systemic Exposure

Exposure SHALL consider:

```text
Number of Affected Objects
Criticality
Duration
Concentration
Interdependency
Propagation
```

---

# 43. Systemic Concentration

A large number of cases associated with one dependency or control may represent concentration risk.

---

# 44. Systemic Propagation

Systemic risk MAY propagate through:

```text
Dependency
Shared Configuration
Shared Control
Shared Policy
Shared Data
Shared Infrastructure
```

---

# 45. Cascading Risk

A systemic condition MAY create cascading failures.

```text
COMMON FAILURE
      ↓
DEPENDENCY
      ↓
MULTIPLE SYSTEMS
      ↓
MULTIPLE DECISIONS
```

Cascading potential SHALL be assessed.

---

# 46. Systemic vs Local Risk

```text
LOCAL RISK
= LIMITED SCOPE

SYSTEMIC RISK
= MULTI-OBJECT / STRUCTURAL EXPOSURE
```

The distinction SHALL be explicit.

---

# 47. Systemic Risk Materiality

Materiality SHALL consider:

```text
Breadth
Depth
Criticality
Propagation
Likelihood
Impact
Reliance
Regulatory Exposure
```

---

# 48. Systemic Risk Escalation

Material systemic risk SHALL be escalated according to authority and risk policy.

---

# 49. Systemic Risk Owner

Every material systemic risk SHALL have an accountable owner.

---

# 50. Systemic Risk Treatment

Possible responses:

```text
MONITOR
MITIGATE
REMEDIATE
REDESIGN
CHANGE POLICY
CHANGE CONTROL
CHANGE ARCHITECTURE
TRANSFER
ACCEPT
AVOID
```

---

# 51. Systemic Remediation

Systemic remediation SHALL address the population rather than only individual cases.

```text
CASE A
CASE B
CASE C
   ↓
SYSTEMIC ACTION
```

---

# 52. Population Remediation

Population remediation MAY include:

```text
Bulk Configuration Change
Control Redesign
Policy Update
Training
Architecture Change
Automation
Dependency Replacement
```

---

# 53. Systemic Change

Systemic action requiring governed change SHALL follow RG-423.

---

# 54. Systemic Baseline

Target systemic state SHALL be governed through RG-424.

---

# 55. Systemic Monitoring

RG-425 SHALL monitor whether systemic risk decreases after intervention.

---

# 56. Systemic Exception

Where immediate systemic remediation is impossible, RG-426 MAY govern controlled temporary exceptions.

---

# 57. Systemic Closure

Systemic risk SHALL not close merely because individual cases are closed.

```text
ALL CASES CLOSED
   ≠
SYSTEMIC RISK RESOLVED
```

---

# 58. Systemic Effectiveness

Effectiveness SHALL demonstrate reduction in:

```text
Frequency
Severity
Exposure
Recurrence
Propagation
```

where applicable.

---

# 59. Pattern Closure

A pattern may be closed when:

```text
Pattern No Longer Relevant
OR
Systemic Cause Removed
OR
Risk Formally Accepted
```

Evidence SHALL support the conclusion.

---

# 60. Pattern Monitoring

Closed patterns MAY remain under observation where recurrence risk remains material.

---

# 61. Pattern Reopening

A closed pattern MAY reopen when:

```text
Recurrence
New Evidence
Changed Dependency
Changed Risk
New Population Exposure
```

---

# 62. Cross-Case Evidence

Cross-case analysis SHALL preserve links to source cases.

---

# 63. Case Independence

Cases SHALL remain independently governed even when correlated.

Correlation SHALL not merge their lifecycle records without explicit authority.

---

# 64. Cross-Case Privacy

Cross-case analytics SHALL apply appropriate access controls.

---

# 65. Cross-Case Data Quality

Pattern quality depends on:

```text
Case Completeness
Classification Quality
Root-Cause Quality
Timestamp Accuracy
Dependency Accuracy
```

Poor source data SHALL reduce pattern confidence.

---

# 66. Missing Data

Missing case information SHALL be visible.

```text
UNKNOWN
≠
NO PATTERN
```

---

# 67. False Pattern

The system SHALL support rejection of patterns caused by:

```text
Coincidence
Biased Sampling
Duplicate Records
Classification Error
Common Naming
```

---

# 68. False Systemic Risk

A suspected systemic risk SHALL be validated before major action unless immediate containment is necessary.

---

# 69. Systemic Risk Confidence

Assessment MAY be:

```text
CONFIRMED
PROBABLE
POSSIBLE
UNCONFIRMED
REJECTED
```

---

# 70. AI Pattern Detection

AI MAY assist with:

```text
Case Clustering
Semantic Similarity
Common-Cause Suggestions
Graph Analysis
Trend Detection
Recurrence Prediction
```

AI output SHALL be treated as analytical evidence, not automatic governance truth.

---

# 71. AI Pattern Explainability

Material AI-assisted pattern findings SHALL preserve:

```text
Model
Version
Input Population
Method
Output
Confidence
Human Assessment
```

---

# 72. AI Systemic-Risk Recommendation

AI MAY recommend systemic review.

It SHALL not silently declare a material systemic risk without required governance.

---

# 73. Cross-Case Decision

Material systemic conclusions SHALL identify:

```text
Decision
Authority
Evidence
Alternatives
Risk
Conditions
```

---

# 74. Cross-Case Governance

The system SHOULD support a review board or designated authority for material systemic patterns.

---

# 75. Escalation Trigger

Escalation MAY occur based on:

```text
Recurrence Count
Risk
Impact
Velocity
Breadth
Control Failure
Dependency Concentration
```

---

# 76. Early Warning

Patterns MAY be classified as early warnings before they become material systemic risks.

```text
SIGNAL
   ↓
EMERGING PATTERN
   ↓
SYSTEMIC RISK
```

---

# 77. Emerging Pattern

An emerging pattern SHALL be monitored without automatically being treated as confirmed systemic risk.

---

# 78. Pattern Threshold Breach

When a governed threshold is exceeded:

```text
PATTERN
   ↓
ESCALATE
   ↓
SYSTEMIC ASSESSMENT
```

---

# 79. Recurrence Suppression

Duplicate or irrelevant recurrences MAY be suppressed from operational alerting.

Source evidence SHALL remain available.

---

# 80. Pattern Suppression

Pattern suppression SHALL require authority and reason.

Silent suppression SHALL be prohibited.

---

# 81. Cross-Case Correlation Rules

Rules SHALL be:

```text
Versioned
Tested
Approved
Auditable
```

---

# 82. Correlation False Positives

False correlations SHALL be tracked to improve analytical quality.

---

# 83. Correlation False Negatives

Missed systemic relationships MAY represent significant governance risk.

Material misses SHALL trigger review.

---

# 84. Pattern Quality

Pattern quality SHOULD consider:

```text
Precision
Recall
Confidence
Completeness
Timeliness
Actionability
```

---

# 85. Recurrence Metrics

Possible metrics:

```text
Recurrence Rate
Recurrence Velocity
Recurrence Density
Repeat Root Causes
Repeat Controls
Repeat Dependencies
```

---

# 86. Systemic Metrics

Possible metrics:

```text
Systemic Risk Count
Open Systemic Risks
Affected Population
Concentration
Propagation
Residual Risk
```

---

# 87. Pattern Metrics

Possible measures:

```text
Patterns Detected
Patterns Confirmed
False Patterns
Pattern Closure Rate
Pattern Recurrence
Pattern Age
```

---

# 88. Remediation Metrics

Cross-case remediation SHOULD track:

```text
Cases Remediated
Population Remediated
Recurrence After Remediation
Effectiveness
```

---

# 89. Trend Analysis

Trend analysis SHOULD identify:

```text
Increasing Recurrence
Increasing Severity
New Common Causes
Emerging Dependencies
Control Degradation
```

---

# 90. Heatmap

The architecture SHOULD support conceptual views such as:

```text
                 LOW      MEDIUM      HIGH
RECURRENCE       [ ]        [ ]        [ ]
IMPACT           [ ]        [ ]        [ ]
PROPAGATION      [ ]        [ ]        [ ]
CONCENTRATION    [ ]        [ ]        [ ]
```

---

# 91. Systemic Risk Graph

A conceptual graph:

```text
          POLICY
             │
             ▼
CONTROL ─→ CASE A
   │          │
   │          ▼
   ├──────→ CASE B
   │          │
   ▼          ▼
DEPENDENCY → CASE C
      │
      ▼
SYSTEMIC RISK
```

---

# 92. Dependency Concentration

Shared dependencies SHALL be assessed for systemic exposure.

---

# 93. Control Concentration

A single control supporting many critical decisions MAY represent systemic control risk.

---

# 94. Authority Concentration

Excessive dependency on one approval authority MAY represent governance concentration risk.

---

# 95. Data Concentration

A single data source supporting many critical controls MAY represent systemic data risk.

---

# 96. Monitoring Concentration

A single monitoring source supporting many controls MAY represent systemic observability risk.

---

# 97. Common Cause Library

The system SHOULD maintain a controlled taxonomy of recurring causes.

Examples:

```text
CONFIGURATION ERROR
CONTROL DESIGN
PROCESS GAP
DEPENDENCY FAILURE
POLICY AMBIGUITY
INSUFFICIENT MONITORING
AUTHORITY GAP
DATA QUALITY
HUMAN FACTOR
```

---

# 98. Taxonomy Governance

Cause taxonomy changes SHALL be versioned.

---

# 99. Cross-Case Lessons

RG-427 lessons SHOULD feed pattern analysis.

```text
LESSON A
LESSON B
LESSON C
   ↓
COMMON LEARNING
```

---

# 100. Pattern-to-Lesson

Confirmed systemic patterns SHALL generate lessons where appropriate.

---

# 101. Pattern-to-Improvement

Material patterns SHALL feed improvement portfolios.

---

# 102. Pattern-to-Policy

Repeated policy-related patterns MAY trigger policy review.

---

# 103. Pattern-to-Control

Repeated control failures MAY trigger control redesign.

---

# 104. Pattern-to-Architecture

Repeated structural failures MAY trigger architecture review.

---

# 105. Pattern-to-Training

Repeated human-process failures MAY trigger training or competency review.

---

# 106. Pattern-to-Automation

Repeated deterministic errors MAY justify automation.

Automation SHALL follow change and assurance governance.

---

# 107. Pattern-to-Dependency

Repeated dependency-related cases MAY justify:

```text
Fallback
Redundancy
Replacement
Contract Change
Architecture Change
```

---

# 108. Systemic Risk Acceptance

Systemic risk MAY be formally accepted only by appropriate authority.

Acceptance SHALL identify:

```text
Population
Risk
Duration
Conditions
Monitoring
Review
```

---

# 109. Systemic Risk Review

Material systemic risks SHALL have periodic review.

---

# 110. Systemic Risk Expiry

Temporary systemic risk acceptance SHALL expire unless renewed.

---

# 111. Systemic Risk Closure

Closure SHALL require evidence that:

```text
Risk Removed
OR
Risk Reduced
OR
Risk Formally Accepted
```

---

# 112. Systemic Risk Reopening

New recurrence MAY reopen a systemic risk assessment.

---

# 113. Historical Integrity

Historical pattern conclusions SHALL not be rewritten without preserving the original decision and reason for revision.

---

# 114. Audit

Material cross-case actions SHALL generate audit events:

```text
Correlation Created
Pattern Detected
Pattern Confirmed
Systemic Risk Created
Systemic Risk Escalated
Systemic Action Approved
Pattern Closed
Pattern Reopened
```

---

# 115. Security

Cross-case analytics SHALL be protected against:

```text
Data Manipulation
Pattern Suppression
Selective Correlation
Evidence Deletion
Unauthorised Exposure
```

---

# 116. Failure Handling

If cross-case analytics are unavailable:

```text
INDIVIDUAL CASE GOVERNANCE
   ↓
CONTINUES
```

but:

```text
SYSTEMIC VISIBILITY
   ↓
DEGRADED
```

This degradation SHALL be visible.

---

# 117. Manual Systemic Review

Manual systemic review MAY be initiated when analytics are unavailable or when material circumstances require independent judgement.

---

# 118. Recovery

After analytical service recovery:

```text
MISSED PERIOD
   ↓
REPROCESS
   ↓
CORRELATE
   ↓
ASSESS
```

---

# 119. MFM Data Model

Core entities:

```text
Recurrence
CrossCasePattern
PatternEvidence
PatternCorrelation
CommonCause
SystemicRisk
SystemicAssessment
SystemicAction
PatternReview
PatternClosure
PatternReopening
```

Relationships:

```text
Case
  ↓
Recurrence
  ↓
Pattern
  ↓
Common Cause
  ↓
Systemic Risk
  ↓
Action
  ↓
Verification
```

---

# 120. MFM Service Boundary

The conceptual implementation should include:

```text
Recurrence Service
Cross-Case Correlation Service
Pattern Detection Service
Common Cause Service
Systemic Risk Service
Pattern Assessment Service
Pattern Review Service
Systemic Action Service
Pattern Analytics Service
```

These integrate with:

```text
Exception
Deviation
Remediation
Closure
Finding
Incident
Change
Baseline
Monitoring
Dependency
Impact
Risk
Policy
Authority
Evidence
Assurance
Decision
Reliance
Audit
```

---

# 121. API Concepts

Illustrative operations:

```text
createRecurrence()
correlateCases()
assessPattern()
confirmPattern()
rejectPattern()
createSystemicRisk()
assessSystemicRisk()
escalateSystemicRisk()
createSystemicAction()
verifySystemicAction()
closePattern()
reopenPattern()
calculateRecurrenceMetrics()
```

These are architectural concepts, not implementation-specific commitments.

---

# 122. Automation

Automation MAY perform:

```text
Case Clustering
Threshold Detection
Trend Analysis
Dependency Matching
Recurrence Alerts
Pattern Candidate Creation
```

Automated results SHALL remain auditable.

---

# 123. Automated Systemic Escalation

High-confidence, high-materiality conditions MAY trigger automatic escalation.

Automatic escalation SHALL not necessarily equal automatic systemic-risk declaration.

---

# 124. Human Review

Human review SHALL be proportionate to:

```text
Materiality
Confidence
Impact
Scope
Automation
```

---

# 125. Privacy and Access

Cross-case analysis MAY expose information across teams or domains.

Access SHALL be governed by:

```text
Purpose
Role
Need to Know
Sensitivity
```

---

# 126. Testing

The architecture SHALL test:

```text
Recurrence Detection
Cross-Case Correlation
False Positives
False Negatives
Pattern Confirmation
Pattern Rejection
Systemic Risk Assessment
Systemic Escalation
Systemic Action
Closure
Reopening
```

---

# 127. Negative Testing

The system SHALL verify:

```text
Duplicate case → NO FALSE RECURRENCE
Keyword similarity only → NOT CONFIRMED
Insufficient evidence → UNCONFIRMED
Missing data → CONFIDENCE REDUCED
Suppressed pattern without authority → BLOCK
Systemic risk without owner → BLOCK
Systemic closure without effectiveness → BLOCK
Individual closure → DOES NOT CLOSE SYSTEMIC RISK
AI suggestion → DOES NOT EQUAL GOVERNANCE DECISION
Analytics outage → VISIBILITY DEGRADED, NOT ZERO RISK
```

---

# 128. Scenario Testing

Representative scenarios:

```text
Repeated configuration error
Repeated security exception
Same dependency causing multiple cases
Common control failure
Common policy ambiguity
Post-remediation recurrence
False pattern from duplicate cases
Emerging pattern below threshold
Pattern crossing threshold
Systemic risk affecting multiple domains
Systemic risk acceptance
Systemic remediation
Pattern closure
Pattern reopening
AI-detected pattern
Analytics failure
Historical backfill
```

---

# 129. Acceptance Criteria

EA-IMETA-PC-RG-428 is accepted when:

- recurrence and pattern are explicitly distinguished;
- exact, functional and causal recurrence are supported;
- cross-case correlation is governed;
- pattern confidence is represented;
- similarity does not automatically establish causation;
- systemic risk has a distinct object and lifecycle;
- systemic scope, exposure and propagation are measurable;
- local and systemic risk are distinguished;
- systemic remediation addresses populations rather than only individual cases;
- closed individual cases do not automatically close systemic risk;
- recurrence after remediation triggers effectiveness review;
- AI-assisted pattern analysis is governed;
- false positives and false negatives are measurable;
- cross-case privacy and access are controlled;
- analytical outages create visible systemic-visibility degradation;
- historical conclusions remain auditable;
- systemic patterns feed lessons, policy, control and architecture improvement;
- negative tests prevent unsupported systemic conclusions and silent pattern suppression.

---

# 130. Next Step

The next logical artifact is the **PC-RG systemic remediation, enterprise intervention and outcome-verification model**, because RG-428 identifies systemic patterns and risks, while the architecture now needs to define how enterprise-level interventions are selected, implemented, measured and verified across the affected population.

Provisional next artifact:

> **EA-IMETA-PC-RG-429 — SYSTEMIC REMEDIATION, ENTERPRISE INTERVENTION & OUTCOME VERIFICATION MODEL**

This will establish the action and outcome layer above recurrence and systemic-risk detection.

---

# 131. Governing Principle

> **A pattern becomes governance-relevant when evidence shows that treating cases independently is no longer sufficient; systemic risk therefore requires population-level assessment, accountable intervention and measurable proof that the underlying condition has changed.**

The PC-RG architecture SHALL ensure that recurrence becomes learning, learning becomes systemic action where necessary, and systemic action is not considered effective until measurable evidence demonstrates reduced exposure or formally accepted residual risk.

# END OF EA-IMETA-PC-RG-428

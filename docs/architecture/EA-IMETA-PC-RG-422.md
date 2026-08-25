# EA-IMETA-PC-RG-422

## DEPENDENCY, CHANGE-IMPACT & PROPAGATION MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-422 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Dependency, Change-Impact & Propagation Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-421 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define how changes are identified, analysed, traced and propagated across dependencies, controls, decisions, reliance relationships and closed cases |
| Architectural Boundary | Change → Dependency Graph → Impact Analysis → Propagation → Reassessment → Decision / Control Response |

---

# 2. Purpose

EA-IMETA-PC-RG-422 defines the architecture for understanding how a change in one object can affect other objects that depend upon it.

RG-421 establishes continuing surveillance and reliance.

RG-422 establishes **how material change is traced from origin to consequence and how affected governance objects are identified**.

The architecture SHALL distinguish:

```text
CHANGE
= A MODIFICATION TO AN EXISTING CONDITION, OBJECT, RULE, DEPENDENCY OR ENVIRONMENT

DEPENDENCY
= A RELATIONSHIP WHERE ONE OBJECT REQUIRES OR RELIES UPON ANOTHER

IMPACT
= THE POTENTIAL OR ACTUAL EFFECT OF A CHANGE

PROPAGATION
= THE TRANSMISSION OF IMPACT THROUGH DEPENDENCY RELATIONSHIPS

REASSESSMENT
= CONTROLLED REVIEW OF AFFECTED OBJECTS

CONTAINMENT
= ACTION TO LIMIT CHANGE IMPACT
```

---

# 3. Core Principle

> **A change is not isolated merely because it is implemented in one component; governance SHALL evaluate the dependency graph through which its effects may propagate.**

The governing chain is:

```text
CHANGE SOURCE
      ↓
DEPENDENCY IDENTIFICATION
      ↓
IMPACT ANALYSIS
      ↓
PROPAGATION ANALYSIS
      ↓
AFFECTED OBJECTS
      ↓
RISK / MATERIALITY
      ↓
REASSESSMENT
      ↓
DECISION
      ↓
MONITORING
```

---

# 4. Change Object

Every material change SHALL be represented as a controlled object.

Minimum attributes:

```text
Change ID
Change Type
Origin
Subject
Reason
Current Version
Target Version
Effective Time
Scope
Dependencies
Risk
Materiality
Authority
Impact Assessment
Affected Objects
Implementation Status
Verification
Decision
Rollback
Audit Reference
```

---

# 5. Change Types

Initial catalogue:

```text
CODE CHANGE
CONFIGURATION CHANGE
POLICY CHANGE
RULE CHANGE
THRESHOLD CHANGE
CONTROL CHANGE
PROCESS CHANGE
DATA CHANGE
MODEL CHANGE
DEPENDENCY CHANGE
AUTHORITY CHANGE
EVIDENCE CHANGE
ENVIRONMENT CHANGE
ORGANISATIONAL CHANGE
REGULATORY CHANGE
```

The catalogue SHALL remain extensible.

---

# 6. Change Lifecycle

```text
IDENTIFIED
   ↓
CLASSIFIED
   ↓
IMPACT ASSESSED
   ↓
AUTHORISED
   ↓
PLANNED
   ↓
IMPLEMENTED
   ↓
VERIFIED
   ↓
PROPAGATION OBSERVED
   ↓
ACCEPTED / REJECTED
   ↓
CLOSED
```

Alternative states:

```text
BLOCKED
DEFERRED
ROLLED BACK
SUSPENDED
FAILED
REOPENED
```

---

# 7. Dependency Object

A dependency SHALL identify a relationship between objects.

Minimum attributes:

```text
Dependency ID
Source
Target
Relationship Type
Direction
Criticality
Strength
Owner
Validity
Version
Evidence
Change Sensitivity
Impact Rules
```

---

# 8. Dependency Types

Examples:

```text
REQUIRES
DEPENDS ON
DERIVES FROM
CONTROLS
VALIDATES
AUTHORIZES
MONITORS
CONSUMES
PRODUCES
SUPPORTS
INFLUENCES
INHERITS
CONSTRAINS
```

Relationships SHALL be typed rather than represented as generic links.

---

# 9. Dependency Direction

Dependencies SHALL preserve direction.

```text
A
 ↓
DEPENDS ON
 ↓
B
```

A change to B may affect A.

A change to A does not necessarily affect B.

---

# 10. Direct Dependency

A direct dependency exists where an explicit relationship connects two objects.

Example:

```text
Decision A
   ↓ DEPENDS ON
Assurance B
```

---

# 11. Indirect Dependency

An indirect dependency exists through intermediate objects.

```text
Decision A
   ↓
Control B
   ↓
System C
   ↓
Dependency D
```

A change to D may propagate to A.

---

# 12. Dependency Depth

Impact analysis SHALL support multiple dependency levels:

```text
LEVEL 0 = CHANGE SOURCE
LEVEL 1 = DIRECT DEPENDENCY
LEVEL 2 = INDIRECT DEPENDENCY
LEVEL 3+ = DOWNSTREAM PROPAGATION
```

Depth alone SHALL not determine materiality.

---

# 13. Dependency Criticality

Dependencies MAY be classified:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Critical dependencies SHALL receive enhanced change-impact treatment.

---

# 14. Dependency Strength

The relationship MAY be:

```text
MANDATORY
STRONG
MODERATE
WEAK
OPTIONAL
```

A mandatory dependency generally creates greater propagation potential.

---

# 15. Dependency Validity

Dependencies SHALL have validity conditions.

Examples:

```text
Version
Effective Period
Scope
Environment
Contract
Authority
Policy
```

Expired dependencies SHALL not silently remain active.

---

# 16. Dependency Graph

The architecture SHALL support a directed graph:

```text
          ┌→ CONTROL B ─→ DECISION C
CHANGE A ─┤
          └→ SYSTEM D ─→ RELIANCE E
```

The graph SHALL be queryable.

---

# 17. Dependency Graph Integrity

The system SHOULD detect:

```text
Missing Target
Orphan Dependency
Circular Dependency
Contradictory Relationship
Expired Relationship
Unknown Owner
Stale Dependency
```

---

# 18. Circular Dependency

Circular relationships MAY be valid, but they SHALL be explicitly identified.

Example:

```text
A → B
↑   ↓
└── C
```

Circularity SHALL not be treated as automatically erroneous.

---

# 19. Change Impact

Impact analysis SHALL determine:

```text
WHAT CHANGED?
WHAT DEPENDS ON IT?
WHAT COULD BE AFFECTED?
WHAT IS ACTUALLY AFFECTED?
WHAT GOVERNANCE OBJECTS MAY BE INVALIDATED?
```

---

# 20. Impact Categories

Initial catalogue:

```text
FUNCTIONAL
TECHNICAL
SECURITY
COMPLIANCE
OPERATIONAL
FINANCIAL
DATA
RISK
CONTROL
AUTHORITY
EVIDENCE
ASSURANCE
DECISION
RELIANCE
REGRESSION
```

---

# 21. Impact Scope

Impact analysis SHALL identify:

```text
Direct Scope
Indirect Scope
Potential Scope
Confirmed Scope
Out of Scope
```

Potential impact SHALL not be represented as confirmed impact.

---

# 22. Impact Severity

Impact severity MAY consider:

```text
Magnitude
Likelihood
Duration
Scope
Criticality
Materiality
Risk
Dependency Strength
```

---

# 23. Change Materiality

A change SHALL be assessed for materiality.

Material changes MAY require:

```text
Enhanced Testing
Independent Assurance
Decision Review
Reacceptance
Stakeholder Notification
```

---

# 24. Change Risk

Change risk SHALL consider:

```text
Inherent Change Risk
Dependency Criticality
Propagation Potential
Control Strength
Rollback Capability
Uncertainty
```

---

# 25. Impact Analysis Workflow

```text
CHANGE
  ↓
CLASSIFY
  ↓
MAP DEPENDENCIES
  ↓
IDENTIFY AFFECTED OBJECTS
  ↓
ASSESS MATERIALITY
  ↓
ASSESS RISK
  ↓
DEFINE RESPONSE
```

---

# 26. Static Impact Analysis

Static analysis uses known relationships before implementation.

Examples:

```text
Dependency Graph
Configuration Map
Requirement Traceability
Architecture Map
Data Lineage
```

---

# 27. Dynamic Impact Analysis

Dynamic analysis uses observed runtime effects.

Examples:

```text
Monitoring
Logs
Events
Telemetry
Incidents
Performance
Usage
```

Static and dynamic analysis SHOULD complement each other.

---

# 28. Predictive Impact

Where appropriate, the system MAY estimate likely downstream impact.

Predictive results SHALL be clearly identified as:

```text
PREDICTED
```

rather than:

```text
CONFIRMED
```

---

# 29. Change Propagation

Propagation is the movement of impact through dependencies.

```text
CHANGE A
   ↓
DEPENDENCY B
   ↓
CONTROL C
   ↓
DECISION D
   ↓
RELIANCE E
```

Each propagation step SHALL be traceable.

---

# 30. Propagation Rules

Rules MAY specify:

```text
IF B CHANGES
THEN REASSESS A

IF CONTROL C FAILS
THEN REVIEW DECISION D

IF DECISION D IS REVOKED
THEN REVIEW RELIANCE E
```

Rules SHALL be versioned.

---

# 31. Propagation Status

Each propagation relationship MAY be:

```text
NOT AFFECTED
POTENTIALLY AFFECTED
AFFECTED
MATERIALLY AFFECTED
REASSESSED
RESOLVED
```

---

# 32. Impact Propagation Event

Every material propagation SHALL be recorded.

Minimum attributes:

```text
Propagation ID
Change ID
Source
Target
Relationship
Impact Type
Impact Level
Evidence
Assessment
Timestamp
Disposition
```

---

# 33. Change-to-Decision Traceability

The system SHALL support:

```text
CHANGE
 ↓
DEPENDENCY
 ↓
CONTROL
 ↓
ASSURANCE
 ↓
DECISION
```

This allows affected decisions to be identified.

---

# 34. Change-to-Reliance Traceability

The system SHALL support:

```text
CHANGE
 ↓
DECISION
 ↓
RELIANCE
 ↓
DOWNSTREAM CONSUMER
```

A material change may therefore require downstream reassessment.

---

# 35. Change-to-Closure Traceability

Closed cases SHALL remain linked to their governing dependencies.

```text
CLOSED CASE
   ↓
DEPENDENCY
   ↓
CHANGE
   ↓
REASSESSMENT
```

Closure SHALL not sever dependency traceability.

---

# 36. Change-to-Finding Traceability

A change MAY generate a finding:

```text
CHANGE
   ↓
REGRESSION
   ↓
FINDING
```

The finding SHALL retain the originating change reference.

---

# 37. Change-to-Incident Traceability

A change MAY generate an incident:

```text
CHANGE
   ↓
IMPACT
   ↓
INCIDENT
```

The incident SHALL preserve change correlation.

---

# 38. Change-to-Exception Traceability

A change MAY create a temporary condition requiring an exception.

```text
CHANGE
   ↓
TEMPORARY GAP
   ↓
EXCEPTION
```

The exception SHALL remain time-bound.

---

# 39. Change-to-Remediation Traceability

A change may be the remediation itself.

```text
FINDING
   ↓
REMEDIATION
   ↓
CHANGE
   ↓
VERIFICATION
```

The architecture SHALL preserve the relationship.

---

# 40. Change-to-Assurance

Material changes MAY require renewed assurance.

```text
CHANGE
   ↓
IMPACT ANALYSIS
   ↓
ASSURANCE REQUIREMENT
   ↓
VALIDATION / VERIFICATION
```

---

# 41. Change-to-Decision Reassessment

Where a material dependency changes:

```text
CHANGE
   ↓
AFFECTED DECISION
   ↓
REASSESSMENT
   ↓
CONTINUE / SUSPEND / REVOKE / REOPEN
```

---

# 42. Dependency Change

A dependency itself may change:

```text
VERSION
OWNER
PROVIDER
INTERFACE
SERVICE LEVEL
SECURITY
ARCHITECTURE
```

Such changes SHALL be impact-assessed.

---

# 43. Interface Change

Interface changes MAY affect:

```text
Consumers
Contracts
Validation
Monitoring
Data
Security
Performance
```

Impact analysis SHALL identify downstream consumers.

---

# 44. Data Dependency

Data dependencies SHALL support lineage:

```text
SOURCE
 ↓
TRANSFORMATION
 ↓
DATASET
 ↓
MODEL / PROCESS
 ↓
DECISION
```

A source-data change may propagate to decisions.

---

# 45. Data Lineage

Material data dependencies SHALL identify:

```text
Source
Transformation
Owner
Version
Consumers
Quality
Validity
```

---

# 46. Policy Change Propagation

Policy changes SHALL identify affected:

```text
Rules
Controls
Processes
Decisions
Exceptions
Assurance
Monitoring
```

---

# 47. Rule Change Propagation

Rule changes MAY affect:

```text
Evaluation
Thresholds
Classification
State Transitions
Acceptance
Closure
```

Historical decisions SHALL preserve their original rule version.

---

# 48. Threshold Change Propagation

Threshold changes MAY alter:

```text
Alerting
Risk
Monitoring
Findings
Reliance
Assurance
```

Threshold changes SHALL not silently rewrite historical outcomes.

---

# 49. Control Change Propagation

Control changes MAY affect:

```text
Evidence
Risk
Assurance
Acceptance
Reliance
Monitoring
```

---

# 50. Authority Change Propagation

Authority changes MAY affect:

```text
Approvals
Delegations
Decisions
Reliance
Closure
Exceptions
```

Invalid authority SHALL trigger reassessment of affected decisions.

---

# 51. Model Change Propagation

AI/model changes MAY affect:

```text
Outputs
Risk
Controls
Evidence
Decisions
Reliance
Monitoring
Assurance
```

Model version SHALL be traceable.

---

# 52. Environment Change

Environment changes MAY include:

```text
Infrastructure
Operating System
Cloud Provider
Network
Hardware
External Service
Security Environment
```

Impact analysis SHALL identify affected assumptions.

---

# 53. Organisational Change

Organisational changes MAY affect:

```text
Ownership
Authority
Separation of Duties
Competence
Escalation
Control Operation
```

---

# 54. Regulatory Change

Regulatory changes MAY require:

```text
Policy Update
Rule Update
Control Change
Reassessment
Reacceptance
Evidence Refresh
```

The architecture SHALL support identifying affected closed cases.

---

# 55. Change Windows

Material changes SHOULD have defined:

```text
Start
Expected Duration
End
Observation Period
Rollback Window
```

---

# 56. Change Freeze

A governance-controlled freeze MAY prevent changes during critical periods.

The freeze SHALL identify:

```text
Scope
Start
End
Exceptions
Authority
```

---

# 57. Emergency Change

Emergency changes MAY bypass normal sequencing only under explicit emergency authority.

They SHALL still require:

```text
Impact Assessment
Authority
Evidence
Post-Change Verification
Post-Change Impact Review
```

---

# 58. Rollback Impact

Rollback is itself a change.

```text
CHANGE
 ↓
ROLLBACK
 ↓
NEW STATE
 ↓
IMPACT ASSESSMENT
```

Rollback SHALL not assume that all downstream effects automatically disappear.

---

# 59. Partial Rollback

Partial rollback SHALL identify:

```text
Reverted Components
Remaining Changes
Affected Dependencies
Residual Risk
```

---

# 60. Failed Change

A failed change SHALL generate:

```text
Change Failure
Risk Reassessment
Impact Analysis
Potential Finding / Incident
```

---

# 61. Change Collision

The system SHOULD detect concurrent changes affecting the same object.

```text
CHANGE A
      ↘
       SAME OBJECT
      ↗
CHANGE B
```

Collision SHALL trigger coordination.

---

# 62. Change Sequencing

Dependencies MAY impose:

```text
A BEFORE B
B BEFORE C
```

The workflow SHALL enforce required sequence.

---

# 63. Change Compatibility

Changes SHALL be assessed for compatibility with:

```text
Current Baseline
Policy
Controls
Interfaces
Dependencies
Monitoring
Assurance
Reliance
```

---

# 64. Change Blast Radius

The system SHOULD calculate or estimate a change blast radius.

Factors:

```text
Dependency Count
Criticality
Depth
Propagation Paths
Reliance Consumers
Risk
Materiality
```

Blast radius SHALL be treated as an analytical indicator, not an absolute truth.

---

# 65. Change Concentration

Multiple changes affecting one critical dependency may create compound risk.

The system SHOULD identify:

```text
Change Density
Concurrent Changes
Shared Dependency
Shared Owner
Shared Control
```

---

# 66. Compound Change

Several individually low-risk changes may collectively become material.

```text
A + B + C
   ↓
COMBINED IMPACT
```

The architecture SHALL support aggregate impact analysis.

---

# 67. Change Correlation

Changes SHOULD be correlated with:

```text
Findings
Incidents
Exceptions
Remediations
Assurance
Decisions
Monitoring Events
```

---

# 68. Change Evidence

Material changes SHALL retain:

```text
Request
Approval
Implementation
Configuration
Test
Verification
Impact Assessment
Rollback
Outcome
```

---

# 69. Change Verification

Verification SHALL confirm:

```text
Intended Change Applied
No Unauthorised Change
Required Controls Present
Expected Interfaces Operate
Monitoring Active
```

---

# 70. Post-Change Observation

Material changes SHOULD have an observation period.

```text
IMPLEMENT
   ↓
STABILISE
   ↓
OBSERVE
   ↓
ASSESS
```

---

# 71. Change Effectiveness

Effectiveness SHALL assess:

```text
Did the change achieve its objective?
Did it introduce unintended effects?
Did dependencies remain valid?
Did risk remain acceptable?
```

---

# 72. Change Regression

A change may cause regression:

```text
CHANGE
 ↓
REGRESSION
 ↓
FINDING / INCIDENT
 ↓
REMEDIATION
```

The change SHALL remain traceable throughout the chain.

---

# 73. Dependency Health

Dependency health SHOULD consider:

```text
Availability
Performance
Security
Version
Integrity
Ownership
Change Frequency
Failure History
```

---

# 74. Dependency Risk

Dependency risk MAY be calculated from:

```text
Criticality
Failure Likelihood
Propagation Potential
Substitutability
Recovery Time
Observability
```

---

# 75. Single Point of Failure

The graph SHOULD identify dependencies where:

```text
ONE NODE
   ↓
MANY CRITICAL RELATIONSHIPS
```

Such nodes may represent systemic risk.

---

# 76. Redundancy

Dependency analysis SHOULD identify whether alternate paths exist.

```text
A
├→ B
└→ C
```

Redundancy may reduce propagation risk.

---

# 77. Dependency Resilience

Resilience MAY consider:

```text
Redundancy
Failover
Substitution
Isolation
Recovery
Monitoring
```

---

# 78. Dependency Isolation

Where feasible, critical dependencies SHOULD be isolated to limit propagation.

Isolation itself SHALL be evaluated for trade-offs.

---

# 79. Propagation Containment

If a change begins propagating unexpectedly:

```text
DETECT
 ↓
ISOLATE
 ↓
CONTAIN
 ↓
ASSESS
 ↓
REMEDIATE
```

Containment SHALL preserve evidence.

---

# 80. Propagation Stop Conditions

Propagation MAY stop when:

```text
No Dependency
Relationship Invalid
Impact Proven Immaterial
Control Boundary Stops Effect
Isolation Applied
```

The reason SHALL be recorded.

---

# 81. Propagation Uncertainty

Where propagation cannot be determined:

```text
PROPAGATION = UNKNOWN
```

Unknown SHALL not be treated as no impact.

---

# 82. Impact Confidence

Impact analysis MAY assign:

```text
HIGH CONFIDENCE
MEDIUM CONFIDENCE
LOW CONFIDENCE
UNKNOWN
```

Confidence SHALL be supported by evidence.

---

# 83. Impact Evidence

Evidence MAY include:

```text
Dependency Graph
Testing
Simulation
Monitoring
Historical Incidents
Architecture Review
Data Lineage
Expert Assessment
```

---

# 84. Simulation

Where feasible, material change impact MAY be simulated before implementation.

Simulation results SHALL be labelled:

```text
SIMULATED
```

and not confused with observed production impact.

---

# 85. Dry Run

Dry-run execution MAY validate:

```text
Dependency Resolution
Rule Evaluation
Configuration
Data Transformation
Workflow
```

---

# 86. Change Approval

Approval SHALL consider:

```text
Impact
Risk
Dependencies
Rollback
Testing
Assurance
Authority
```

---

# 87. Change Authority

RG-413 SHALL determine who may approve changes based on:

```text
Scope
Risk
Materiality
Environment
Emergency Status
```

---

# 88. Change Decision

RG-420 decision logic SHALL govern:

```text
Accept Change
Reject Change
Conditionally Accept
Defer
Suspend
Rollback
```

---

# 89. Change Monitoring

RG-416 SHALL monitor:

```text
Implementation
Signals
Errors
Performance
Dependencies
Regression
```

---

# 90. Change Findings

RG-417 SHALL receive material change findings.

---

# 91. Change Remediation

RG-418 SHALL govern corrective actions resulting from failed or harmful changes.

---

# 92. Change Assurance

RG-419 SHALL provide independent assurance where required.

---

# 93. Post-Closure Reliance

RG-421 SHALL identify closed decisions affected by changes.

```text
CHANGE
   ↓
DEPENDENCY GRAPH
   ↓
CLOSED DECISION
   ↓
CONTINUING RELIANCE REVIEW
```

---

# 94. Decision Reassessment

Affected decisions SHALL be reassessed according to RG-420.

---

# 95. Historical Integrity

A change SHALL not rewrite:

```text
Original Decision
Original Evidence
Original Closure
Historical State
```

Historical records SHALL remain valid for their original period.

---

# 96. Temporal Impact

Impact analysis SHALL consider when the change became effective.

```text
CHANGE EFFECTIVE T1
DECISION VALID T0–T2
```

The system SHALL determine the actual overlap.

---

# 97. Retroactive Impact

Retroactive impact analysis SHALL be exceptional.

It SHALL record:

```text
Effective Period
Reason
Authority
Affected Decisions
Risk
Corrective Action
```

---

# 98. Change and Legal / Regulatory Records

Where regulatory obligations apply, historical decisions SHALL remain reconstructable under the applicable rules.

---

# 99. Dependency Versioning

Dependency relationships SHALL be versioned where material.

Example:

```text
Dependency D v1
   ↓
Dependency D v2
```

Impact analysis SHALL identify the transition.

---

# 100. Graph Versioning

The dependency graph itself SHALL support historical versions.

This enables:

```text
WHAT DID THE GRAPH LOOK LIKE
WHEN THE DECISION WAS MADE?
```

---

# 101. Graph Comparison

The system SHOULD support:

```text
GRAPH BEFORE
      ↓
CHANGE
      ↓
GRAPH AFTER
```

Differences SHALL be identifiable.

---

# 102. Orphan Detection

After change, the system SHOULD detect:

```text
Orphan Decision
Orphan Control
Orphan Monitor
Orphan Evidence
Orphan Reliance
```

---

# 103. Stale Dependency Detection

A dependency may remain recorded but no longer reflect reality.

Stale dependencies SHOULD be identified through:

```text
Version Drift
Observed Behaviour
Ownership Changes
Failed Validation
Inactive Systems
```

---

# 104. Dependency Reconciliation

Critical dependency maps SHOULD periodically be reconciled with actual architecture.

---

# 105. Change Inventory

A controlled change inventory SHOULD provide:

```text
Active Changes
Planned Changes
Completed Changes
Failed Changes
Rolled Back Changes
Emergency Changes
High-Impact Changes
```

---

# 106. Impact Register

An impact register SHOULD provide:

```text
Change
Affected Object
Impact
Severity
Confidence
Decision
Status
```

---

# 107. Propagation Register

A propagation register MAY provide:

```text
Source
Target
Relationship
Impact
Evidence
Assessment
Disposition
```

---

# 108. MFM Data Model

Core entities:

```text
Change
Dependency
DependencyVersion
ImpactAssessment
PropagationEvent
ChangeEffectiveness
ChangeDecision
ChangeEvidence
DependencyRisk
ImpactScope
```

Relationships:

```text
Change
 ↓
Dependency Graph
 ↓
Impact Assessment
 ↓
Propagation
 ↓
Affected Governance Objects
 ↓
Reassessment
 ↓
Decision
```

---

# 109. MFM Service Boundary

The conceptual implementation should include:

```text
Change Service
Dependency Service
Dependency Graph Service
Impact Analysis Service
Propagation Service
Change Risk Service
Change Verification Service
Change Effectiveness Service
Change Decision Service
```

These integrate with:

```text
Monitoring
Finding
Incident
Exception
Remediation
Assurance
Acceptance
Reliance
Risk
Authority
Evidence
Workflow
State
Audit
```

---

# 110. API Concepts

Illustrative operations:

```text
createChange()
registerDependency()
updateDependency()
analyseImpact()
tracePropagation()
findAffectedDecisions()
findAffectedReliance()
assessChangeRisk()
approveChange()
verifyChange()
observePostChange()
rollbackChange()
closeChange()
```

These are architectural concepts, not implementation-specific commitments.

---

# 111. Reporting

The system SHOULD support:

```text
Show all critical dependencies.

Show decisions affected by change X.

Show reliance relationships downstream of dependency Y.

Show all changes affecting control Z.

Show changes with unknown impact.

Show changes with high propagation potential.

Show stale dependencies.

Show orphan governance objects.

Show changes that caused findings.

Show changes followed by incidents.

Show high-risk concurrent changes.
```

---

# 112. Dashboard

The dashboard SHOULD expose:

```text
Open Changes
High-Risk Changes
Critical Dependencies
Unknown Impact
Active Propagation
Affected Decisions
Affected Reliance
Failed Changes
Rolled Back Changes
Stale Dependencies
```

---

# 113. Security

Dependency and change maps SHALL be protected against:

```text
Unauthorised Modification
Graph Manipulation
Impact Concealment
Unauthorised Disclosure
Change Spoofing
```

---

# 114. Integrity

Historical dependency graphs and impact assessments SHALL be immutable or tamper-evident.

---

# 115. Privacy

Dependency information may reveal sensitive architecture or organisational information.

Access SHALL follow:

```text
Least Privilege
Purpose Limitation
Need to Know
Audit
```

---

# 116. Continuity

Critical dependency and change-impact functions SHALL have continuity arrangements.

---

# 117. Failure Handling

If dependency graph services are unavailable:

```text
IMPACT ANALYSIS INCOMPLETE
   ↓
CHANGE BLOCKED / RISK ESCALATED
```

depending on criticality.

---

# 118. Unknown Impact

If impact cannot be determined for a material change:

```text
UNKNOWN IMPACT
```

SHALL trigger risk-based review.

Unknown SHALL not automatically equal low risk.

---

# 119. Testing

The architecture SHALL test:

```text
Direct Dependency
Indirect Dependency
Circular Dependency
Dependency Expiry
Impact Analysis
Propagation
Change Collision
Compound Change
Rollback
Partial Rollback
Policy Change
Rule Change
Model Change
Authority Change
Evidence Change
Regulatory Change
```

---

# 120. Negative Testing

The system SHALL verify:

```text
Unknown dependency → REVIEW
Unknown impact → NOT LOW RISK
Invalid authority → BLOCK
Expired dependency → BLOCK / REVIEW
Missing graph node → FLAG
Stale relationship → FLAG
Unauthorised change → BLOCK
Historical record overwrite → BLOCK
Silent threshold change → BLOCK
Untracked downstream reliance → FLAG
```

---

# 121. Scenario Testing

Representative scenarios:

```text
Low-risk isolated change
Critical dependency change
Shared service change
Policy revision
Rule threshold change
Model upgrade
Data-source replacement
Authority restructuring
Emergency change
Failed change
Rollback
Partial rollback
Concurrent changes
Compound low-risk changes
Closed decision affected by change
Downstream reliance propagation
Unknown impact
```

---

# 122. Acceptance Criteria

EA-IMETA-PC-RG-422 is accepted when:

- changes are controlled objects;
- dependencies are typed and directional;
- direct and indirect dependencies are supported;
- dependency graphs are versioned;
- impact analysis distinguishes potential and confirmed impact;
- propagation is traceable;
- change materiality and risk are assessed;
- policy, rule, threshold, control, data, authority and model changes are covered;
- downstream decisions and reliance can be identified;
- rollback is treated as a new change;
- compound and concurrent changes are supported;
- unknown impact is visible;
- stale and orphan dependencies can be detected;
- historical graph and decision integrity are preserved;
- change monitoring integrates with RG-416;
- findings/incidents/exceptions integrate with RG-417;
- remediation integrates with RG-418;
- assurance integrates with RG-419;
- decisions integrate with RG-420;
- post-closure reliance integrates with RG-421;
- negative tests prevent silent propagation and unauthorised change.

---

# 123. Next Step

The next logical artifact is the **PC-RG change-control, release and deployment governance model**, because RG-422 establishes what may be affected by a change, while the architecture now needs to define how material changes are controlled from request through approval, implementation, release, observation, rollback and final closure.

Provisional next artifact:

> **EA-IMETA-PC-RG-423 — CHANGE CONTROL, RELEASE & DEPLOYMENT GOVERNANCE MODEL**

This will establish the execution-control boundary for the change-impact architecture.

---

# 124. Governing Principle

> **Every material change has a dependency context; every dependency creates potential propagation; every material propagation requires controlled impact assessment; and no closed decision is exempt from reassessment when the conditions supporting its validity materially change.**

The PC-RG architecture SHALL therefore maintain traceability from the original change through every affected dependency, governance object, decision and reliance relationship.

# END OF EA-IMETA-PC-RG-422

# MFM Post-Steady-State Phase Control

## N8-B — Architecture Roadmap & Transition Portfolio Governance

**Control ID:** MFM-Post-Steady-State-Phase-Control-N8-B-Architecture-Roadmap-and-Transition-Portfolio-Governance-001  
**Version:** 1.0  
**Status:** ACTIVE — N8-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N8 — Post-N7 Controlled Continuation  
**Predecessor:** N8-A — Strategy, Outcome & Capability Alignment  
**Authorization:** AUTHORIZED — N8 ACTIVE WITH CONDITIONS  
**Next Work Package:** N8-C — Investment, Prioritization & Portfolio Traceability  

---

# 1. Purpose

N8-B establishes controlled governance for the relationship between:

```text
Current Architecture
    ↓
Transition Architecture
    ↓
Architecture Roadmap
    ↓
Transition Portfolio
    ↓
Target Architecture
```

The purpose is to transform the strategic, outcome and capability alignment established in N8-A into a controlled architecture evolution and transition roadmap.

N8-B does not establish that roadmap items, initiatives or investments are approved, funded or implemented.

---

# 2. N8-A Dependency

N8-B uses the controlled outputs from N8-A:

```text
Strategy Model
Strategic Objectives
Business Outcomes
Capability Alignment
Capability Gaps
Strategic Dependencies
Strategic Assumptions
Capability-to-Architecture Traceability
```

N8-B also reuses:

```text
N7 Current-State Architecture
N7 Target-State Architecture
N7 Transition-State Model
N7 Architecture Principles
N7 Architecture Decisions
N7 Architecture Dependencies
N7 Architecture Drift
```

---

# 3. Core Roadmap Chain

The primary N8-B model is:

```text
CURRENT STATE
      ↓
TRANSITION STATE
      ↓
ROADMAP
      ↓
TRANSITION PORTFOLIO
      ↓
TARGET STATE
```

Where appropriate:

```text
Architecture Need
      ↓
Roadmap Item
      ↓
Transition Initiative
      ↓
Portfolio
      ↓
Execution
      ↓
Validation
```

---

# 4. Architecture Roadmap

A roadmap item should contain:

```text
Roadmap ID
Architecture Objective
Source Capability
Current State
Target State
Transition State
Dependencies
Milestone
Owner
Priority
Status
Decision
Evidence
```

Possible states:

```text
PROPOSED
PLANNED
PRIORITIZED
APPROVED
ACTIVE
DEFERRED
SUPERSEDED
COMPLETED
CANCELLED
UNVERIFIED
```

---

# 5. Roadmap Objective

Each material roadmap item shall identify:

```text
What architecture condition must change?
Why must it change?
Which capability requires the change?
Which outcome does it support?
Which target-state element is affected?
What dependency exists?
What evidence will demonstrate completion?
```

---

# 6. Current-State Baseline

N8-B shall reuse the N7 current-state architecture baseline.

Current-state information may include:

```text
Architecture Components
Capabilities
Services
Applications
Data
Technology
Interfaces
Dependencies
Constraints
Risks
Known Gaps
Architecture Drift
```

The current-state baseline shall not be silently modified.

---

# 7. Transition-State Model

Transition states shall identify controlled intermediate conditions:

```text
CURRENT
   ↓
T1
   ↓
T2
   ↓
T3
   ↓
TARGET
```

Each material transition state should define:

```text
Purpose
Entry Conditions
Architecture State
Dependencies
Risks
Exit Conditions
Evidence
Owner
```

---

# 8. Target-State Relationship

Each material roadmap item should trace to:

```text
Target-State Architecture
Target Capability State
Target Outcome
Strategic Objective
```

Relationship:

```text
Roadmap Item
    ↓
ENABLES
    ↓
Target State
```

---

# 9. Architecture Roadmap Governance

Roadmap changes shall be controlled through:

```text
Change Identification
Impact Assessment
Architecture Review
Decision
Authority
Dependency Assessment
Risk Assessment
Approval
Validation
Evidence
```

N7 change governance shall be reused.

---

# 10. Transition Portfolio

A transition portfolio groups related roadmap items and initiatives required to move from current to target state.

Portfolio grouping may be by:

```text
Capability
Architecture Domain
Strategic Objective
Outcome
Business Area
Technology Domain
Service
Transformation Theme
```

Portfolio grouping shall not alter the underlying traceability relationships.

---

# 11. Transition Initiative

A transition initiative should identify:

```text
Initiative ID
Roadmap ID
Capability
Architecture Objective
Outcome
Dependencies
Risk
Priority
Owner
Status
Decision
Evidence
```

Potential states:

```text
PROPOSED
PRIORITIZED
APPROVED
FUNDED
ACTIVE
DEFERRED
COMPLETED
CANCELLED
UNVERIFIED
```

---

# 12. Roadmap-to-Initiative Relationship

The controlled relationship is:

```text
Roadmap Item
    ↓
REALIZED_BY
    ↓
Transition Initiative
```

This does not mean the initiative has been funded.

---

# 13. Initiative-to-Architecture Relationship

The relationship is:

```text
Transition Initiative
    ↓
CHANGES / ENABLES
    ↓
Architecture
```

Material architecture changes remain subject to N7 change governance.

---

# 14. Initiative-to-Capability Relationship

The relationship is:

```text
Transition Initiative
    ↓
ENABLES
    ↓
Capability Change
```

Capability change does not automatically establish capability effectiveness.

---

# 15. Roadmap Dependencies

Material roadmap dependencies may include:

```text
Architecture
Capability
Technology
Data
Security
Identity
Integration
Service
Supplier
Investment
Regulatory
Organizational
Decision
```

Dependencies shall retain:

```text
Dependency ID
Source
Target
Criticality
Owner
Risk
Required Date
Status
Evidence
```

---

# 16. Roadmap Sequencing

Sequencing may be driven by:

```text
Dependency
Risk
Strategic Priority
Capability Need
Architecture Constraint
Regulatory Requirement
Technology Lifecycle
Operational Readiness
Resource Constraint
```

Sequencing does not constitute funding approval.

---

# 17. Milestone Governance

Material roadmap milestones should contain:

```text
Milestone ID
Roadmap ID
Description
Entry Criteria
Exit Criteria
Owner
Target Date
Dependency
Evidence
Status
```

Possible states:

```text
PLANNED
READY
ACTIVE
ACHIEVED
MISSED
DEFERRED
CANCELLED
UNVERIFIED
```

---

# 18. Transition Gate

A material transition may require:

```text
Entry Conditions Met
AND
Dependencies Assessed
AND
Risk Assessed
AND
Required Decision Recorded
AND
Authority Confirmed
AND
Validation Criteria Defined
```

---

# 19. Target-State Readiness

Target-state readiness may consider:

```text
Architecture Completeness
Capability Readiness
Dependency Resolution
Risk
Security
Compliance
Operational Readiness
Evidence
Validation
```

Readiness does not prove implementation.

---

# 20. Architecture Roadmap Materiality

Roadmap items may be classified:

```text
MINOR
MATERIAL
MAJOR
TRANSFORMATIONAL
```

Factors:

```text
Architecture Impact
Capability Impact
Strategic Impact
Business Impact
Risk
Security
Compliance
Dependency
Cost
Reversibility
Time
```

---

# 21. Portfolio Prioritization Input

N8-B shall provide structured input to N8-C:

```text
Architecture Priority
Capability Priority
Dependency Priority
Risk Priority
Strategic Priority
Target-State Urgency
Transition Criticality
```

N8-B does not itself establish final investment prioritization.

---

# 22. Portfolio Decision Boundary

The following distinctions are mandatory:

```text
ROADMAP ITEM
≠
INITIATIVE

INITIATIVE
≠
PRIORITIZED INVESTMENT

PRIORITIZED INVESTMENT
≠
APPROVED INVESTMENT

APPROVED INVESTMENT
≠
FUNDED INITIATIVE

FUNDED INITIATIVE
≠
IMPLEMENTED CHANGE

IMPLEMENTED CHANGE
≠
TARGET-STATE EFFECTIVENESS
```

---

# 23. Roadmap-to-Strategy Traceability

Each material roadmap item should be traceable to:

```text
Strategic Objective
Business Outcome
Capability
Architecture
Target State
```

The chain is:

```text
Strategy
    ↓
Outcome
    ↓
Capability
    ↓
Architecture Need
    ↓
Roadmap
```

---

# 24. Roadmap-to-Evidence Traceability

Each material roadmap item should identify:

```text
Expected Result
Validation Method
Evidence Source
Evidence Owner
Evidence Class
Completion Criteria
```

Evidence classes:

```text
E0 — Conceptual
E1 — Architectural
E2 — Governance / Implementation Model
E3 — Actual Implementation
```

---

# 25. Architecture Drift and Roadmap

Roadmap governance shall consider:

```text
Approved Architecture
        ≠
Observed Architecture
```

Potential drift:

```text
Scope Drift
Sequence Drift
Architecture Drift
Dependency Drift
Target-State Drift
Priority Drift
Milestone Drift
```

Material drift requires controlled assessment.

---

# 26. Roadmap Conflict Detection

Potential conflicts:

```text
Roadmap vs Architecture Principle
Roadmap vs Target State
Roadmap vs Capability Need
Roadmap vs Dependency
Roadmap vs Existing Change
Roadmap vs Risk
Roadmap vs Compliance
Roadmap vs Strategic Objective
```

Conflicts shall not be silently resolved.

---

# 27. Roadmap Orphan Detection

Potential orphans:

```text
Roadmap Item Without Objective
Roadmap Item Without Capability
Roadmap Item Without Architecture Target
Roadmap Item Without Owner
Roadmap Item Without Dependency Assessment
Roadmap Item Without Completion Criteria
Target-State Element Without Roadmap
Material Architecture Gap Without Roadmap Treatment
```

These are detection conditions and require assessment.

---

# 28. Transition Portfolio Register

| Portfolio | Objective | Capability | Architecture | Roadmap Items | Status |
|---|---|---|---|---|---|
| PRT-* | TBD | CAP-* | ARC-* | RM-* | TBD |

---

# 29. Architecture Roadmap Register

| Roadmap | Objective | Current State | Target State | Priority | Status |
|---|---|---|---|---|---|
| RM-* | TBD | TBD | TBD | TBD | TBD |

---

# 30. Transition Initiative Register

| Initiative | Roadmap | Capability | Architecture | Owner | Status |
|---|---|---|---|---|---|
| INIT-* | RM-* | CAP-* | ARC-* | TBD | TBD |

---

# 31. Transition Dependency Register

| Dependency | Source | Target | Criticality | Owner | Status |
|---|---|---|---|---|---|
| DEP-* | RM-* | INIT-* | TBD | TBD | TBD |

---

# 32. Milestone Register

| Milestone | Roadmap | Entry Criteria | Exit Criteria | Owner | Status |
|---|---|---|---|---|---|
| MILE-* | RM-* | TBD | TBD | TBD | TBD |

---

# 33. Target-State Readiness Register

| Target Element | Readiness Area | Status | Evidence | Owner |
|---|---|---|---|---|
| ARC-* | TBD | TBD | EVD-* | TBD |

---

# 34. N8 Authorization Conditions

N8-B remains bound by:

```text
AUTH-N8-01
N8 shall remain within the approved work-package scope.

AUTH-N8-02
N5, N6 and N7 carry-forward conditions remain active.

AUTH-N8-03
N7 closure shall not be reopened without a separate controlled decision.

AUTH-N8-04
N8 shall not silently redefine N5, N6 or N7 baselines.

AUTH-N8-05
Material scope expansion requires explicit authorization.

AUTH-N8-06
Investment, funding and implementation claims shall remain distinct.

AUTH-N8-07
Value and outcome claims shall remain evidence-dependent.

AUTH-N8-08
Material portfolio changes shall receive impact assessment.

AUTH-N8-09
N8 work packages shall maintain independent completion criteria.

AUTH-N8-10
N8 closure requires a separate completion authority decision.
```

---

# 35. N8-B Deliverables

N8-B shall produce:

```text
D-B01
Architecture Roadmap Model

D-B02
Current-to-Target Transition Model

D-B03
Transition State Register

D-B04
Architecture Roadmap Register

D-B05
Transition Portfolio Register

D-B06
Transition Initiative Register

D-B07
Roadmap Dependency Register

D-B08
Roadmap Milestone Register

D-B09
Target-State Readiness Register

D-B10
Roadmap-to-Strategy Traceability Matrix

D-B11
Roadmap-to-Capability Traceability Matrix

D-B12
Roadmap-to-Architecture Traceability Matrix

D-B13
Roadmap-to-Evidence Traceability Matrix

D-B14
Roadmap Conflict Register

D-B15
Roadmap Orphan Register

D-B16
Architecture / Roadmap Drift Register

D-B17
N8-B Findings Register

D-B18
N8-B Completion Recommendation
```

---

# 36. N8-B Completion Criteria

N8-B may be considered complete when:

```text
Architecture Roadmap Established
AND
Current-to-Target Transition Model Established
AND
Transition States Established
AND
Transition Portfolio Established
AND
Transition Initiatives Established
AND
Roadmap Dependencies Assessed
AND
Roadmap Milestones Established
AND
Target-State Readiness Assessed
AND
Strategy Traceability Established
AND
Capability Traceability Established
AND
Architecture Traceability Established
AND
Evidence Traceability Established
AND
Roadmap Conflicts Assessed
AND
Roadmap Orphans Assessed
AND
Architecture / Roadmap Drift Assessed
AND
Material Findings Consolidated
AND
Evidence Boundaries Preserved
AND
N8-C Input Prepared
```

---

# 37. Current N8-B State

```text
N8-B
=
ACTIVE
```

N8-B is the current authorized work package.

---

# 38. Next Work Package

Upon N8-B completion:

```text
N8-C
Investment, Prioritization & Portfolio Traceability
```

N8-C shall use the controlled roadmap and transition portfolio outputs from N8-B.

---

# 39. Current Program State

```text
N2
= CLOSED / N2C-2

N3
= CLOSED / N3C-2

N4
= CLOSED / N4C-2

N5
= CLOSED / N5C-2
  COMPLETE WITH CONDITIONS

N6
= CLOSED / N6C-2
  COMPLETE WITH CONDITIONS

N7
= CLOSED / N7C-2
  COMPLETE WITH CONDITIONS

N8-00
= COMPLETED

N8-01
= COMPLETED

N8
= AUTHORIZED / ACTIVE
  WITH CONDITIONS

N8-A
= COMPLETED

N8-B
= ACTIVE
```

---

# 40. Final N8-B Statement

> **N8-B establishes the Architecture Roadmap & Transition Portfolio Governance layer of the authorized N8 workstream. It converts the strategy, outcome and capability alignment from N8-A into controlled current-state, transition-state, roadmap, transition-portfolio and target-state relationships. It establishes roadmap dependencies, milestones, target-state readiness, traceability, conflict detection, orphan detection and drift governance while preserving the distinction between roadmap, initiative, prioritization, approval, funding, implementation and effectiveness.**

---

# 41. Document Control

**Document:** MFM Post-Steady-State Phase Control — N8-B Architecture Roadmap & Transition Portfolio Governance  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N8-B-Architecture-Roadmap-and-Transition-Portfolio-Governance-001  
**Version:** 1.0  
**Status:** ACTIVE — N8-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N8 — Post-N7 Controlled Continuation  
**Predecessor:** N8-A — Strategy, Outcome & Capability Alignment  
**Authorization:** AUTHORIZED — N8 ACTIVE WITH CONDITIONS  
**Current Work Package:** N8-B  
**Next Work Package:** N8-C — Investment, Prioritization & Portfolio Traceability  
**Automatic Scope Expansion:** PROHIBITED  
**Automatic Completion:** PROHIBITED  

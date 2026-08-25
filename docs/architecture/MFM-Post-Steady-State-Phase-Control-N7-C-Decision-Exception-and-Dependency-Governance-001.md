# MFM Post-Steady-State Phase Control

## N7-C — Decision, Exception & Dependency Governance

**Control ID:** MFM-Post-Steady-State-Phase-Control-N7-C-Decision-Exception-and-Dependency-Governance-001  
**Version:** 1.0  
**Status:** ACTIVE — N7-C WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N7 — Post-N6 Controlled Continuation  
**Predecessor:** N7-B — Change Impact & Transition Governance  
**Authorization:** AUTHORIZED — N7 ACTIVE WITH CONDITIONS  
**Next Work Package:** N7-D — Operationalization & Continuous Architecture Governance  

---

# 1. Purpose

N7-C establishes controlled governance for:

```text
Architecture Decisions
Exceptions
Dependencies
Assumptions
Constraints
Escalations
Decision Rights
```

The core governance chain is:

```text
Issue / Need
    ↓
Assessment
    ↓
Decision
    ↓
Authority
    ↓
Rationale
    ↓
Affected Objects
    ↓
Evidence
```

N7-C does not itself authorize unrestricted implementation or scope expansion.

---

# 2. N7-B Dependency

N7-C builds on the outputs of N7-B:

```text
Change Register
Change Impact Assessments
Transition Governance
Change Decisions
Change Dependencies
Change Risks
Change Approvals
Change Validation
Change Conflicts
```

N7-C shall preserve the N7-A architecture evolution baseline and the N6 traceability baseline.

---

# 3. Scope

N7-C covers:

```text
Architecture Decision Governance
Decision Rights
Decision Records
Decision Rationale
Exception Governance
Dependency Governance
Assumption Governance
Constraint Governance
Escalation Governance
Decision Conflicts
Exception Conflicts
Dependency Conflicts
Decision Traceability
Authority Traceability
Evidence Traceability
```

---

# 4. Decision Object

A material decision should contain:

```text
Decision ID
Decision Statement
Decision Type
Context
Problem / Need
Options
Assessment
Risk
Dependencies
Constraints
Authority
Rationale
Conditions
Affected Objects
Evidence
Effective Date
Review Date
Status
```

---

# 5. Decision Types

Possible decision types:

```text
Architecture
Business
Technology
Security
Data
Application
Integration
Service
Operational
Risk
Compliance
Governance
Exception
Transition
Change
AI / Agent
Lifecycle
Strategic
```

Classification shall be evidence-based.

---

# 6. Decision Lifecycle

The controlled lifecycle is:

```text
IDENTIFIED
    ↓
ASSESSED
    ↓
PROPOSED
    ↓
REVIEWED
    ↓
DECIDED
    ↓
APPROVED
    ↓
EFFECTIVE
    ↓
REVIEWED
    ↓
SUPERSEDED / RETIRED
```

Alternative states:

```text
REJECTED
DEFERRED
CANCELLED
WITHDRAWN
```

A decision shall not be treated as effective solely because it exists in a register.

---

# 7. Decision Authority

N7-C shall distinguish:

```text
Decision Requestor
Decision Owner
Decision Maker
Architecture Authority
Business Authority
Risk Authority
Security Authority
Compliance Authority
Operational Authority
Approval Authority
```

Authority shall be supported by evidence.

---

# 8. Decision Rights

Decision rights shall identify:

```text
Who May Propose
Who May Assess
Who May Recommend
Who May Decide
Who May Approve
Who May Reject
Who May Escalate
Who May Review
Who May Close
```

No decision right shall be inferred solely from job title or system access.

---

# 9. Decision Rationale

A material decision should preserve:

```text
Problem
Context
Options Considered
Criteria
Trade-offs
Risk
Dependencies
Constraints
Chosen Option
Rejected Options
Rationale
```

The rationale shall remain traceable to the decision.

---

# 10. Decision Traceability

The standard chain is:

```text
Requirement / Need
        ↓
Assessment
        ↓
Options
        ↓
Decision
        ↓
Authority
        ↓
Affected Architecture
        ↓
Change / Transition
        ↓
Implementation
        ↓
Evidence
```

Not every decision will contain every relationship.

---

# 11. Architecture Decision Records

Material architecture decisions shall identify:

```text
Architecture Context
Decision
Rationale
Consequences
Dependencies
Risks
Affected Architecture
Affected Services
Affected Controls
Evidence
Review Date
```

An architecture decision does not constitute proof that the chosen architecture has been implemented.

---

# 12. Exception Governance

An exception is a controlled deviation from an established:

```text
Principle
Policy
Standard
Requirement
Architecture Rule
Control
Process
Target-State Constraint
```

An exception shall identify:

```text
Exception ID
Requirement / Rule
Reason
Scope
Risk
Compensating Control
Owner
Authority
Approval
Start Date
Expiry Date
Review Date
Evidence
Status
```

---

# 13. Exception Lifecycle

The exception lifecycle is:

```text
IDENTIFIED
    ↓
ASSESSED
    ↓
PROPOSED
    ↓
RISK REVIEWED
    ↓
APPROVED
    ↓
ACTIVE
    ↓
REVIEWED
    ↓
EXPIRED / CLOSED
```

Alternative states:

```text
REJECTED
WITHDRAWN
SUPERSEDED
```

---

# 14. Exception Boundary

The following distinctions are mandatory:

```text
Exception Request
≠
Approved Exception

Approved Exception
≠
Risk Acceptance

Risk Acceptance
≠
Compliance Approval

Compliance Approval
≠
Control Effectiveness
```

Each claim requires appropriate authority and evidence.

---

# 15. Exception Materiality

Exceptions shall be classified:

```text
LOW
MEDIUM
HIGH
CRITICAL
UNKNOWN
```

Factors:

```text
Security
Compliance
Operational Impact
Business Impact
Risk
Architecture Impact
Service Impact
Duration
Scope
Reversibility
```

---

# 16. Exception Authority

A material exception shall identify:

```text
Exception Owner
Risk Owner
Decision Authority
Approval Authority
Control Owner
Compliance Authority
Security Authority
```

Only materially applicable authorities need to be populated.

---

# 17. Dependency Governance

A dependency is a relationship in which one object, activity, decision or transition relies materially upon another.

Controlled relationship:

```text
Object A
    ↓
DEPENDS_ON
    ↓
Object B
```

Dependencies may be:

```text
Business
Capability
Architecture
Application
Data
Technology
Security
Identity
Integration
Infrastructure
Service
Operational
Supplier
Regulatory
Decision
Change
Transition
```

---

# 18. Dependency Record

Material dependencies should contain:

```text
Dependency ID
Source Object
Target Object
Dependency Type
Description
Owner
Criticality
Risk
Required Date
Status
Evidence
Resolution
```

---

# 19. Dependency Lifecycle

```text
IDENTIFIED
    ↓
ASSESSED
    ↓
ACCEPTED
    ↓
MANAGED
    ↓
RESOLVED / RETIRED
```

Alternative states:

```text
BLOCKED
ESCALATED
UNVERIFIED
CANCELLED
```

---

# 20. Dependency Criticality

Dependencies may be:

```text
CRITICAL
HIGH
MEDIUM
LOW
UNKNOWN
```

Criticality factors:

```text
Blocking Effect
Time Sensitivity
Risk
Security
Compliance
Service Impact
Architecture Impact
Reversibility
External Dependency
```

---

# 21. Assumption Governance

Material assumptions shall be recorded where they influence:

```text
Architecture
Decision
Transition
Risk
Implementation
Service
Compliance
Target State
```

An assumption record should contain:

```text
Assumption ID
Statement
Source
Owner
Impact
Confidence
Validation Requirement
Review Date
Status
Evidence
```

Possible states:

```text
PROPOSED
ACCEPTED
VALIDATED
INVALIDATED
SUPERSEDED
UNKNOWN
```

---

# 22. Constraint Governance

Material constraints may include:

```text
Technical
Architectural
Financial
Operational
Regulatory
Security
Data
Supplier
Resource
Time
Organizational
```

Constraints shall be distinguished from assumptions.

```text
CONSTRAINT
≠
ASSUMPTION
```

---

# 23. Escalation Governance

Escalation may be required when:

```text
Decision Authority Is Unclear
Risk Exceeds Delegated Authority
Dependency Becomes Blocking
Exception Becomes Material
Change Exceeds Scope
Architecture Principle Is Violated
Compliance Impact Is Material
Security Impact Is Material
Conflicting Decisions Exist
```

Escalation shall preserve:

```text
Issue
Reason
Authority
Decision
Evidence
Date
Outcome
```

---

# 24. Decision Conflict

Potential decision conflicts include:

```text
Decision vs Requirement
Decision vs Architecture Principle
Decision vs Policy
Decision vs Risk
Decision vs Compliance
Decision vs Existing Decision
Decision vs Target State
Decision vs Active Exception
```

Conflicts shall not be silently resolved.

---

# 25. Exception Conflict

Potential conflicts:

```text
Exception vs Policy
Exception vs Standard
Exception vs Control
Exception vs Compliance Obligation
Exception vs Security Requirement
Exception vs Target State
Exception vs Risk Appetite
```

Material conflicts require authority review.

---

# 26. Dependency Conflict

Potential dependency conflicts:

```text
Circular Dependency
Conflicting Dependency
Unowned Dependency
Unmanaged Critical Dependency
Expired Dependency
Unverified Dependency
Dependency Without Target
Dependency Without Source
```

A detected dependency issue is not automatically a material finding.

---

# 27. Decision-to-Change Relationship

The relationship is:

```text
Decision
    ↓
AUTHORIZES / DIRECTS
    ↓
Change
```

Where applicable:

```text
Decision
    ↓
CONSTRAINS
    ↓
Change
```

The exact authorized relationship vocabulary shall follow the N6 model.

---

# 28. Decision-to-Architecture Relationship

Material decisions shall be traceable to affected architecture:

```text
Decision
    ↓
AFFECTS
    ↓
Architecture Element
```

This supports:

```text
Architecture Evolution
Target-State Control
Change Impact
Drift Detection
Decision History
```

---

# 29. Decision-to-Risk Relationship

Material decisions may:

```text
CREATE RISK
CHANGE RISK
REDUCE RISK
ACCEPT RISK
TRANSFER RISK
AVOID RISK
```

Risk acceptance shall not be inferred from decision existence.

---

# 30. Decision-to-Compliance Relationship

Where applicable:

```text
Decision
    ↓
AFFECTS
    ↓
Compliance Obligation
```

or:

```text
Decision
    ↓
REQUIRES
    ↓
Compliance Assessment
```

A decision does not establish compliance.

---

# 31. Decision Evidence

Evidence may include:

```text
Approved Decision Record
Meeting Record
Authority Delegation
Risk Assessment
Architecture Assessment
Impact Assessment
Exception Approval
Compliance Assessment
Security Assessment
Implementation Evidence
```

Evidence shall support the specific claim being made.

---

# 32. Governance Orphans

Potential orphan objects:

```text
Decision Without Authority
Decision Without Rationale
Exception Without Authority
Exception Without Risk Assessment
Dependency Without Owner
Dependency Without Target
Assumption Without Owner
Constraint Without Source
Escalation Without Outcome
```

Each requires assessment.

---

# 33. Governance Traceability Matrix

| Source | Relationship | Target | Authority | Evidence | Status |
|---|---|---|---|---|---|
| DEC-* | AFFECTS | ARC-* | TBD | EVD-* | TBD |
| DEC-* | DIRECTS | CHG-* | TBD | EVD-* | TBD |
| EXC-* | DEVIATES_FROM | STD-* | TBD | EVD-* | TBD |
| RSK-* | CONTROLLED_BY | CTL-* | TBD | EVD-* | TBD |
| OBJ-* | DEPENDS_ON | OBJ-* | TBD | EVD-* | TBD |

---

# 34. Decision Register

| Decision | Type | Authority | Affected Object | Status | Evidence |
|---|---|---|---|---|---|
| DEC-* | TBD | TBD | TBD | TBD | EVD-* |

---

# 35. Exception Register

| Exception | Rule | Risk | Authority | Expiry | Status |
|---|---|---|---|---|---|
| EXC-* | TBD | RSK-* | TBD | TBD | TBD |

---

# 36. Dependency Register

| Dependency | Source | Target | Criticality | Owner | Status |
|---|---|---|---|---|---|
| DEP-* | OBJ-* | OBJ-* | TBD | TBD | TBD |

---

# 37. Assumption Register

| Assumption | Statement | Owner | Validation | Status |
|---|---|---|---|---|
| ASM-* | TBD | TBD | TBD | TBD |

---

# 38. Constraint Register

| Constraint | Type | Source | Impact | Owner | Status |
|---|---|---|---|---|---|
| CST-* | TBD | TBD | TBD | TBD | TBD |

---

# 39. Escalation Register

| Escalation | Reason | Authority | Decision | Outcome | Status |
|---|---|---|---|---|---|
| ESC-* | TBD | TBD | TBD | TBD | TBD |

---

# 40. N7 Authorization Conditions

N7-C remains bound by:

```text
AUTH-N7-01
N7 shall remain within approved work-package scope.

AUTH-N7-02
N5 and N6 conditions remain active.

AUTH-N7-03
N6 closure shall not be reopened without controlled decision.

AUTH-N7-04
N6 objects and relationships shall not be silently redefined.

AUTH-N7-05
Material scope expansion requires authorization.

AUTH-N7-06
Implementation claims remain evidence-dependent.

AUTH-N7-07
Compliance and effectiveness claims remain evidence-dependent.

AUTH-N7-08
Material changes require impact assessment.

AUTH-N7-09
Work packages maintain independent completion criteria.

AUTH-N7-10
N7 closure requires separate authority decision.
```

---

# 41. N5 / N6 Carry-Forward

N7-C preserves:

```text
COND-N5-01 through COND-N5-06
```

and:

```text
COND-N6-01 through COND-N6-10
```

No carry-forward condition is silently removed.

---

# 42. N7-C Deliverables

N7-C shall produce:

```text
D-C01
Decision Governance Model

D-C02
Decision Rights Register

D-C03
Architecture Decision Register

D-C04
Decision Traceability Matrix

D-C05
Exception Governance Model

D-C06
Exception Register

D-C07
Dependency Governance Model

D-C08
Dependency Register

D-C09
Assumption Register

D-C10
Constraint Register

D-C11
Escalation Register

D-C12
Decision / Exception / Dependency Conflict Register

D-C13
N7-C Findings Register

D-C14
N7-C Completion Recommendation
```

---

# 43. N7-C Completion Criteria

N7-C may be considered complete when:

```text
Decision Governance Established
AND
Decision Rights Established
AND
Decision Traceability Established
AND
Architecture Decision Governance Established
AND
Exception Governance Established
AND
Exception Lifecycle Established
AND
Dependency Governance Established
AND
Dependency Lifecycle Established
AND
Assumption Governance Established
AND
Constraint Governance Established
AND
Escalation Governance Established
AND
Decision Conflicts Assessed
AND
Exception Conflicts Assessed
AND
Dependency Conflicts Assessed
AND
Governance Orphans Assessed
AND
Evidence Boundaries Preserved
AND
Material Findings Consolidated
AND
N7-D Input Prepared
```

---

# 44. Current N7-C State

```text
N7-C
=
ACTIVE
```

N7-C is the current authorized work package.

---

# 45. Next Work Package

Upon N7-C completion:

```text
N7-D
Operationalization & Continuous Architecture Governance
```

N7-D will build on:

```text
Architecture Decisions
Decision Rights
Exceptions
Dependencies
Assumptions
Constraints
Escalations
Change Governance
```

---

# 46. Current Program State

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
= AUTHORIZED / ACTIVE
  WITH CONDITIONS

N7-A
= COMPLETED

N7-B
= COMPLETED

N7-C
= ACTIVE

N7-D
= AUTHORIZED / SCHEDULED

N7-E
= AUTHORIZED / SCHEDULED
```

---

# 47. Final N7-C Statement

> **N7-C establishes the controlled Decision, Exception & Dependency Governance framework for the authorized N7 workstream. It provides governance for material decisions, decision rights, architecture decisions, exceptions, dependencies, assumptions, constraints and escalations, while maintaining traceability to authority, rationale, affected objects and evidence. N7-C preserves the N5 and N6 carry-forward conditions and does not treat a decision, exception or approval as proof of implementation, compliance or effectiveness.**

---

# 48. Document Control

**Document:** MFM Post-Steady-State Phase Control — N7-C Decision, Exception & Dependency Governance  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N7-C-Decision-Exception-and-Dependency-Governance-001  
**Version:** 1.0  
**Status:** ACTIVE — N7-C WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N7 — Post-N6 Controlled Continuation  
**Predecessor:** N7-B — Change Impact & Transition Governance  
**Authorization:** AUTHORIZED — N7 ACTIVE WITH CONDITIONS  
**Current Work Package:** N7-C  
**Next Work Package:** N7-D — Operationalization & Continuous Architecture Governance  
**Automatic Implementation:** PROHIBITED  
**Automatic Scope Expansion:** PROHIBITED  

# MFM Post-Steady-State Phase Control

## N5-B — Authority, Accountability & Decision Rights Model

**Control ID:** MFM-Post-Steady-State-Phase-Control-N5-B-Authority-Accountability-and-Decision-Rights-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N5-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N5 — Governance & Control Architecture  
**Parent Control:** N5.00 — Governance & Control Architecture Scope, Charter and Work Package Control  
**Predecessor:** N5-A — Governance Scope & Evidence Baseline  
**Upstream Workstream:** N4 — Operational Architecture  
**N4 Closure:** N4-SC-90 — CLOSED  
**N4 Completion:** N4C-2 — COMPLETE WITH CONDITIONS  
**N5 Authorization:** EXPLICITLY APPROVED  

---

# 1. Purpose

N5-B establishes the controlled model for:

```text
Authority
Accountability
Responsibility
Delegation
Decision Rights
Decision Classes
Approval
Escalation
Governance Evidence
```

The purpose is to define how governance authority is represented and assessed without inventing organizational structures, named individuals or decision rights that are not supported by controlled evidence.

N5-B builds on the governance scope established in N5-A.

---

# 2. Governing Principle

The source governance model establishes that governance requires:

```text
CLEAR AUTHORITY
DEFINED ACCOUNTABILITY
DELEGATED RESPONSIBILITY
CONTROLLED DECISION-MAKING
TRANSPARENT EVIDENCE
CONTINUOUS ASSURANCE
```

N5-B therefore treats authority and accountability as explicit governance relationships rather than inferred organizational assumptions.

---

# 3. Source Governance Baseline

The existing EA-IMETA governance material establishes an Architecture Authority responsible for:

```text
Architecture Principles
Architecture Standards
Architecture Decisions
Architecture Exceptions
Architecture Conformance
Architecture Evolution
```

It also establishes the concept of domain authorities and delegated decision rights.

N5-B preserves these source concepts without assuming that a specific person or organization currently occupies each role.

---

# 4. Authority Model

The controlled authority hierarchy is:

```text
Enterprise Authority
        ↓
Architecture / Master Governance Authority
        ↓
Domain Authority
        ↓
Solution Authority
        ↓
Implementation Authority
        ↓
Operational Authority
```

Cross-cutting authorities may operate across the hierarchy:

```text
Security
Data
Identity
Risk
Compliance
Assurance
Change
Service
```

The hierarchy is a governance model, not proof of current organizational implementation.

---

# 5. Authority Object

A material authority object should establish:

```text
Authority ID
Authority Name / Role
Scope
Decision Rights
Accountability
Delegation
Escalation
Approval Rights
Evidence
Lifecycle
```

Where an authority instance is not evidenced:

```text
AUTHORITY INSTANCE
= NOT ESTABLISHED
```

No named individual shall be invented.

---

# 6. Accountability Model

N5-B distinguishes:

```text
ACCOUNTABLE
RESPONSIBLE
CONSULTED
INFORMED
```

A material decision should establish at least:

```text
Accountable Authority
Responsible Owner
Required Consultation
Required Notification
```

The exact RACI-style structure shall be used only where supported by the actual governance model.

---

# 7. Accountability Relationship

The controlled relationship is:

```text
Governance Object
        ↓
Accountable Authority
```

Examples:

```text
Architecture Decision
        ↓
Architecture Authority

Security Decision
        ↓
Security Authority

Data Decision
        ↓
Data Authority

Service Decision
        ↓
Service Authority
```

These are relationship patterns, not claims that each authority exists.

---

# 8. Responsibility vs Authority

N5-B shall preserve:

```text
RESPONSIBILITY
≠
AUTHORITY
```

A person or role may be responsible for executing a decision without possessing the authority to approve that decision.

Likewise:

```text
AUTHORITY
≠
EXECUTION
```

Decision rights and execution responsibility shall remain separate where the governance model requires separation.

---

# 9. Delegated Authority

The controlled delegation model considers:

```text
Risk
Impact
Materiality
Complexity
Reversibility
Strategic Importance
Regulatory Impact
```

The baseline model is:

```text
LOW IMPACT
    ↓
LOCAL DECISION

MEDIUM IMPACT
    ↓
DOMAIN DECISION

HIGH IMPACT
    ↓
MASTER ARCHITECTURE DECISION

ENTERPRISE-CRITICAL
    ↓
EXECUTIVE / ENTERPRISE AUTHORITY
```

This is a governance pattern and shall not be treated as evidence of actual delegation until verified.

---

# 10. Delegation Object

A material delegation should establish:

```text
Delegation ID
Delegating Authority
Delegated Authority
Scope
Decision Rights
Limitations
Duration
Conditions
Escalation
Evidence
Status
```

Delegation states:

```text
PROPOSED
APPROVED
ACTIVE
SUSPENDED
EXPIRED
REVOKED
UNKNOWN
```

---

# 11. Decision Rights

N5-B shall establish decision-right relationships covering:

```text
Decision Type
Decision Scope
Authority
Accountability
Responsibility
Consultation
Approval
Escalation
Evidence
```

The decision-right model is the principal governance mechanism for determining who may make which decision.

---

# 12. Decision Classes

The source governance model establishes:

```text
Class A — Strategic
Class B — Enterprise
Class C — Domain
Class D — Solution
Class E — Operational
```

The classification is used to determine expected governance depth.

---

# 13. Class A — Strategic Decisions

Examples:

```text
Enterprise Platform Strategy
Major Cloud Strategy
Enterprise Architecture Direction
Major Strategic Architecture Principles
```

Expected governance:

```text
Executive / Enterprise Authority
+
Architecture Review
+
Material Risk / Compliance Review
```

Exact authority remains evidence-dependent.

---

# 14. Class B — Enterprise Decisions

Examples:

```text
Enterprise Data Platform
Enterprise Identity Architecture
Enterprise Integration Direction
Major Shared Services
```

Expected governance:

```text
Architecture Board / Master Authority
+
Relevant Domain Review
```

The actual governance body must be evidenced.

---

# 15. Class C — Domain Decisions

Examples:

```text
Domain Application Architecture
Domain Data Architecture
Domain Process Architecture
Domain Integration
```

Expected governance:

```text
Domain Authority
+
Enterprise Review where material
```

---

# 16. Class D — Solution Decisions

Examples:

```text
Application Component
Integration Design
Solution Architecture
Deployment Pattern
```

Expected governance:

```text
Solution Authority
+
Domain Architecture Review where required
```

---

# 17. Class E — Operational Decisions

Examples:

```text
Configuration
Minor Version Change
Operational Optimization
Routine Technical Adjustment
```

Expected governance:

```text
Operational Authority
+
Architecture Review where material
```

---

# 18. Decision Authority Matrix

The baseline matrix is:

| Decision Class | Primary Authority | Required Review |
|---|---|---|
| Strategic | Executive Architecture Authority | Enterprise Architecture |
| Enterprise | Architecture Board / Master Authority | Relevant Domains |
| Domain | Domain Architecture Authority | Enterprise where required |
| Solution | Solution Architecture Authority | Domain Architecture |
| Operational | Operational Authority | Architecture where material |

This is the controlled baseline model.

Actual authority assignments require evidence.

---

# 19. Decision Lifecycle

Material governance decisions shall use:

```text
REQUESTED
↓
CLASSIFIED
↓
ASSESSED
↓
CONSULTED
↓
RECOMMENDED
↓
APPROVED / REJECTED
↓
IMPLEMENTED
↓
VALIDATED
↓
CLOSED
```

Where applicable:

```text
ESCALATED
RETURNED
REOPENED
SUPERSEDED
```

Lifecycle state shall be evidence-controlled.

---

# 20. Decision Record

A material decision should establish:

```text
Decision ID
Decision Class
Decision Subject
Requestor
Responsible Owner
Accountable Authority
Consulted Parties
Decision
Rationale
Risk
Evidence
Approval
Implementation
Validation
Status
```

A decision definition does not establish that the decision has occurred.

---

# 21. Approval Model

N5-B distinguishes:

```text
RECOMMENDATION
≠
APPROVAL
```

and:

```text
APPROVAL
≠
IMPLEMENTATION
```

A recommendation may be prepared without being approved.

An approved decision may require separate implementation evidence.

---

# 22. Escalation Model

Escalation may be triggered by:

```text
Risk
Impact
Authority Boundary
Policy Conflict
Architecture Conflict
Security Concern
Compliance Concern
Material Exception
Decision Deadlock
```

Escalation path:

```text
Local
 ↓
Domain
 ↓
Master / Enterprise
 ↓
Executive
```

The applicable path must be supported by governance evidence.

---

# 23. Decision Exceptions

A decision may require exception handling where:

```text
Standard Cannot Be Met
Policy Cannot Be Met
Architecture Principle Conflict
Risk Accepted
Technical Constraint
Regulatory Constraint
Operational Constraint
```

The exception relationship shall identify:

```text
Decision
↓
Exception
↓
Authority
↓
Risk
↓
Approval
↓
Compensating Control
↓
Review / Expiry
```

---

# 24. Architecture Exception Authority

The source governance model assigns Architecture Authority responsibility for architecture exceptions.

N5-B shall assess:

```text
Exception Authority
Approval Rights
Risk Acceptance
Compensating Controls
Review
Expiry
Evidence
```

No exception approval shall be inferred.

---

# 25. Accountability Matrix

N5-B shall use the following logical structure:

| Governance Object | Accountable | Responsible | Consulted | Informed | Evidence |
|---|---|---|---|---|---|
| Architecture Principle | TBD | TBD | TBD | TBD | Required |
| Architecture Standard | TBD | TBD | TBD | TBD | Required |
| Architecture Decision | TBD | TBD | TBD | TBD | Required |
| Architecture Exception | TBD | TBD | TBD | TBD | Required |
| Security Decision | TBD | TBD | TBD | TBD | Required |
| Data Decision | TBD | TBD | TBD | TBD | Required |
| Service Decision | TBD | TBD | TBD | TBD | Required |
| Change Decision | TBD | TBD | TBD | TBD | Required |

TBD means:

```text
NOT YET ESTABLISHED
```

It is not permission to invent an organizational assignment.

---

# 26. Governance Role Types

N5-B may recognize:

```text
Executive Authority
Architecture Authority
Domain Authority
Solution Authority
Operational Authority
Security Authority
Data Authority
Identity Authority
Risk Authority
Compliance Authority
Assurance Authority
Change Authority
Service Authority
```

These are governance role categories.

They are not evidence of named organizations or people.

---

# 27. Decision Rights Boundary

N5-B shall distinguish:

```text
CAN RECOMMEND
CAN REVIEW
CAN APPROVE
CAN REJECT
CAN ESCALATE
CAN IMPLEMENT
CAN VALIDATE
```

A role possessing one right does not automatically possess all others.

---

# 28. Separation of Duties

Where material, N5-B shall assess separation between:

```text
Request
Recommendation
Approval
Implementation
Validation
Assurance
```

This is particularly relevant to:

```text
Security
Risk
Compliance
Financially Material Decisions
High-Risk Architecture
Production Change
Exception Approval
```

Actual segregation requirements remain evidence-dependent.

---

# 29. Governance Evidence

Authority and accountability claims require appropriate evidence.

Examples:

```text
Approved Governance Charter
Delegation Record
Decision-right Matrix
Policy
Appointment Record
Committee Terms of Reference
Approved Decision
Meeting Record
Architecture Decision Record
Exception Approval
Control Record
Assurance Evidence
```

Evidence shall be evaluated for:

```text
Authority
Currency
Integrity
Traceability
Completeness
Relevance
```

---

# 30. Authority Evidence States

Controlled states:

```text
ESTABLISHED
PARTIALLY ESTABLISHED
DEFINED / NOT VERIFIED
NOT ESTABLISHED
UNVERIFIED
CONFLICTING
SUPERSEDED
RETIRED
```

No authority shall be upgraded to:

```text
ACTIVE
```

without appropriate evidence.

---

# 31. Decision Evidence States

Controlled states:

```text
DRAFT
RECOMMENDED
APPROVED
REJECTED
IMPLEMENTED
VALIDATED
CLOSED
SUPERSEDED
UNKNOWN
```

These states are mutually meaningful only where the relevant lifecycle is applicable.

---

# 32. Governance Finding Classes

N5-B may identify:

```text
AB-01 Missing Authority
AB-02 Missing Accountability
AB-03 Missing Responsibility
AB-04 Missing Decision Right
AB-05 Missing Delegation
AB-06 Unclear Approval Authority
AB-07 Unclear Escalation
AB-08 Separation-of-Duties Concern
AB-09 Conflicting Authority
AB-10 Conflicting Decision Right
AB-11 Missing Decision Evidence
AB-12 Missing Delegation Evidence
AB-13 Unverified Authority
AB-14 Governance Lifecycle Deficiency
AB-15 Decision Traceability Deficiency
AB-16 Authority Effectiveness Not Established
```

These are controlled finding classes.

---

# 33. False-Gap Control

The following conclusions are prohibited without additional evidence:

```text
No Named Person
≠
No Authority

No Committee Record
≠
No Governance

No Decision Record
≠
No Decision

No Delegation Record
≠
No Delegation

No Approval Evidence
≠
Decision Was Rejected

No RACI Matrix
≠
No Accountability
```

N5-B shall classify such conditions as:

```text
UNVERIFIED
```

or:

```text
NOT ESTABLISHED
```

until evidence supports a stronger conclusion.

---

# 34. Governance Contradiction Control

Where multiple sources establish different authority relationships:

```text
SOURCE A
    vs
SOURCE B
```

N5-B shall record:

```text
CONFLICTING
```

until:

```text
Resolution
OR
Controlled Acceptance
```

is established.

The model shall not silently select one source.

---

# 35. Materiality and Decision Depth

Decision governance depth shall be based on:

```text
Strategic Impact
Enterprise Impact
Risk
Security
Compliance
Financial Impact
Operational Impact
Reversibility
Dependency
Change Magnitude
```

Higher materiality requires deeper authority, evidence and review.

---

# 36. Relationship to N4

N4 established operational governance relationships around:

```text
Service
Process
Owner
KPI / KRI
Monitoring
Incident
Problem
Change
Improvement
```

N5-B adds:

```text
Authority
Accountability
Decision Rights
Approval
Escalation
Assurance
```

N5-B shall not redefine N4 objects.

---

# 37. Relationship to N5-A

N5-A established:

```text
Governance Domains
Governance Layers
Authority Scope
Accountability Scope
Decision Scope
Policy / Standard / Control Scope
Risk / Compliance / Assurance Scope
Evidence Scope
Materiality
False-Gap Controls
```

N5-B operationalizes the:

```text
Authority
Accountability
Decision Rights
```

portion of that baseline.

---

# 38. Relationship to N5-C

N5-B provides the governance decision-right foundation required for:

```text
N5-C
Policy, Standards & Control Architecture Assessment
```

N5-C shall use N5-B to determine:

```text
Who approves
Who owns
Who controls
Who reviews
Who accepts exceptions
Who assures
```

---

# 39. Decision Rights Assessment Register

N5-B shall use:

| Assessment ID | Subject | Decision Class | Authority | Evidence | Status | Finding |
|---|---|---|---|---|---|---|
| N5-B-001 | Strategic Architecture | A | TBD | TBD | OPEN | TBD |
| N5-B-002 | Enterprise Architecture | B | TBD | TBD | OPEN | TBD |
| N5-B-003 | Domain Architecture | C | TBD | TBD | OPEN | TBD |
| N5-B-004 | Solution Architecture | D | TBD | TBD | OPEN | TBD |
| N5-B-005 | Operational Architecture | E | TBD | TBD | OPEN | TBD |
| N5-B-006 | Architecture Exception | Applicable | TBD | TBD | OPEN | TBD |
| N5-B-007 | Security Decision | Applicable | TBD | TBD | OPEN | TBD |
| N5-B-008 | Data Decision | Applicable | TBD | TBD | OPEN | TBD |
| N5-B-009 | Change Decision | Applicable | TBD | TBD | OPEN | TBD |

This is a controlled assessment structure, not evidence that the listed authority assignments exist.

---

# 40. N5-B Completion Criteria

N5-B may be considered complete when:

```text
Authority Model Established
AND
Accountability Model Established
AND
Responsibility Model Established
AND
Delegation Model Established
AND
Decision Classes Established
AND
Decision Rights Assessed
AND
Approval Model Assessed
AND
Escalation Model Assessed
AND
Exception Authority Assessed
AND
Governance Evidence Assessed
AND
False-Gap Control Applied
AND
N5-C Inputs Prepared
```

---

# 41. N5-B Completion State

At this stage:

```text
N5-B
=
ACTIVE
```

No completion recommendation shall be issued until the completion criteria have been assessed.

---

# 42. Current State

```text
N2
= CLOSED
N2C-2 — COMPLETE WITH CONDITIONS

N3
= CLOSED
N3C-2 — COMPLETE WITH CONDITIONS

N4
= CLOSED
N4C-2 — COMPLETE WITH CONDITIONS

N5
= ACTIVE / AUTHORIZED

N5.00
= COMPLETED / SCOPE ESTABLISHED

N5-A
= COMPLETED / GOVERNANCE SCOPE & EVIDENCE BASELINE

N5-B
= ACTIVE / AUTHORITY, ACCOUNTABILITY & DECISION RIGHTS MODEL

N5-C
= NEXT CONTROLLED WORK PACKAGE

N5-D
= NOT STARTED

N5-E
= NOT STARTED

N6
= NOT AUTHORIZED
```

---

# 43. Authority Boundary

N5-B does not authorize:

```text
Appointment of Named Authorities
Final Organizational Design
Final Policy Approval
Final Control Certification
Operational Effectiveness Certification
N5 Closure
N6 Generation
```

These require appropriate authority and evidence.

---

# 44. Final N5-B Statement

> **N5-B establishes the controlled Authority, Accountability & Decision Rights Model for the MFM Governance & Control Architecture workstream. It distinguishes authority from responsibility, recommendation from approval, approval from implementation, and governance models from actual organizational assignments. Decision classes, delegated authority, escalation, exception authority and governance evidence are controlled through explicit relationships. No named authority or decision right is invented where evidence is absent.**

---

# 45. Document Control

**Document:** MFM Post-Steady-State Phase Control — N5-B Authority, Accountability & Decision Rights Model  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N5-B-Authority-Accountability-and-Decision-Rights-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N5-B WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N5 — Governance & Control Architecture  
**Parent:** N5.00 — Governance & Control Architecture Scope, Charter and Work Package Control  
**Predecessor:** N5-A — Governance Scope & Evidence Baseline  
**N4 Closure:** N4-SC-90 — CLOSED  
**N4 Completion:** N4C-2 — COMPLETE WITH CONDITIONS  
**N5 Authorization:** EXPLICITLY APPROVED  
**Current Work Package:** N5-B  
**Next Work Package:** N5-C — Policy, Standards & Control Architecture Assessment  
**Automatic Successor Generation:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
**Automatic N6 Generation:** PROHIBITED  

# MFM Post-Steady-State Phase Control

## N5-A — Governance Scope & Evidence Baseline

**Control ID:** MFM-Post-Steady-State-Phase-Control-N5-A-Governance-Scope-and-Evidence-Baseline-001  
**Version:** 1.0  
**Status:** ACTIVE — N5-A WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N5 — Governance & Control Architecture  
**Parent Control:** N5.00 — Governance & Control Architecture Scope, Charter and Work Package Control  
**Predecessor:** N5.00  
**Upstream Workstream:** N4 — Operational Architecture  
**N4 Closure:** N4-SC-90 — CLOSED  
**N4 Completion:** N4C-2 — COMPLETE WITH CONDITIONS  
**N5 Authorization:** EXPLICITLY APPROVED  

---

# 1. Purpose

N5-A establishes the controlled governance scope and evidence baseline for N5.

Its purpose is to determine:

```text
WHAT
governance relationships are material

WHO
must hold authority or accountability

WHAT
governance artifacts must exist or be assessed

WHICH
evidence is required

WHERE
governance boundaries begin and end

HOW
governance claims shall be classified
```

N5-A does not attempt to complete the governance architecture.

It establishes the evidence-controlled foundation upon which N5-B through N5-E may operate.

---

# 2. Governing Principle

The N1 Phase Charter defines N5 as:

```text
N5 — Governance & Control Architecture
```

with potential governance domains:

```text
Architecture Governance
Security Governance
Data Governance
Application Governance
Infrastructure Governance
Identity Governance
Service Governance
Risk
Compliance
Assurance
Change
```

The Charter explicitly requires the final N5 boundaries to be derived from the actual governance model rather than assumed in advance.

N5-A therefore establishes the boundary-discovery mechanism rather than declaring every potential domain to be active.

---

# 3. Scope Objective

N5-A shall establish a controlled baseline covering:

```text
SB-01 Governance Domain Scope
SB-02 Governance Layer Scope
SB-03 Authority Scope
SB-04 Accountability Scope
SB-05 Decision Scope
SB-06 Policy / Standard / Control Scope
SB-07 Risk / Compliance / Assurance Scope
SB-08 Change Governance Scope
SB-09 Evidence Scope
SB-10 Governance Boundary Scope
SB-11 Dependency Scope
SB-12 Finding Classification Scope
```

---

# 4. Scope Boundary

N5-A includes:

```text
Governance identification
Governance classification
Governance boundary definition
Governance evidence requirements
Governance relationship identification
Governance ownership identification
Governance dependency identification
Governance evidence-quality assessment
```

N5-A does not include:

```text
Final authority assignment
Final decision-right approval
Final policy approval
Final control approval
Operational implementation
Governance effectiveness certification
N5 closure
N6 traceability matrix
```

Those activities require later controlled work packages or explicit authority decisions.

---

# 5. Governance Domain Baseline

The initial controlled candidate set is:

```text
GD-01 — Architecture Governance
GD-02 — Security Governance
GD-03 — Data Governance
GD-04 — Application Governance
GD-05 — Infrastructure Governance
GD-06 — Identity Governance
GD-07 — Service Governance
GD-08 — Risk Governance
GD-09 — Compliance Governance
GD-10 — Assurance Governance
GD-11 — Change Governance
```

Status at N5-A initiation:

```text
DEFINED AS CANDIDATE DOMAINS
≠
CONFIRMED ACTIVE GOVERNANCE
```

No candidate domain shall be treated as an implemented governance capability without appropriate evidence.

---

# 6. Governance Domain Assessment

Each candidate governance domain shall be assessed against:

```text
Purpose
Scope
Authority
Accountability
Decision Rights
Policies
Standards
Controls
Evidence
Assurance
Exceptions
Lifecycle
Dependencies
Operational Relationship
Architecture Relationship
```

The assessment result shall be recorded using controlled states.

---

# 7. Governance State Model

N5-A shall use:

```text
GS-01 — ESTABLISHED
GS-02 — PARTIALLY ESTABLISHED
GS-03 — DEFINED / IMPLEMENTATION NOT ESTABLISHED
GS-04 — NOT ESTABLISHED
GS-05 — NOT REQUIRED
GS-06 — UNVERIFIED
GS-07 — CONFLICTING
GS-08 — SUPERSEDED
GS-09 — RETIRED
```

The distinction between:

```text
DEFINED
IMPLEMENTED
ACTIVE
EFFECTIVE
```

shall be preserved.

---

# 8. Governance Layer Baseline

The governance architecture shall be assessed across:

```text
GL-01 — Strategic Intent
GL-02 — Governance Principles
GL-03 — Authority
GL-04 — Control
GL-05 — Execution
GL-06 — Observation
GL-07 — Assurance
GL-08 — Evolution
```

The controlled relationship is:

```text
Intent
  ↓
Principles
  ↓
Authority
  ↓
Control
  ↓
Execution
  ↓
Observation
  ↓
Assurance
  ↓
Evolution
```

N5-A uses this as a structural assessment model, not as proof that each layer is currently implemented.

---

# 9. Governance Hierarchy Baseline

The baseline hierarchy is:

```text
ENTERPRISE GOVERNANCE
        |
        v
EA-IMETA MASTER GOVERNANCE
        |
        +-----------------------------+
        |                             |
        v                             v
DOMAIN GOVERNANCE               CROSS-CUTTING GOVERNANCE
        |                             |
        +--------------+--------------+
                       |
                       v
              SOLUTION GOVERNANCE
                       |
                       v
             IMPLEMENTATION GOVERNANCE
                       |
                       v
              OPERATIONAL GOVERNANCE
```

N5-A shall determine whether material governance relationships can be traced through this hierarchy.

---

# 10. Governance Relationship Baseline

N5-A shall identify relationships among:

```text
Objective
Capability
Policy
Authority
Decision
Information
System
Agent
Control
Risk
Evidence
Outcome
```

The target relationship chain is:

```text
Objective
    ↓
Policy
    ↓
Authority
    ↓
Capability
    ↓
Decision
    ↓
Action
    ↓
Outcome
    ↓
Evidence
```

A missing relationship shall be classified as:

```text
NOT ESTABLISHED
```

unless evidence demonstrates that the relationship does not apply.

---

# 11. Authority Scope

N5-A shall identify the categories of authority that require governance assessment:

```text
Enterprise Authority
Architecture Authority
Domain Authority
Solution Authority
Implementation Authority
Operational Authority
Security Authority
Data Authority
Identity Authority
Service Authority
Risk Authority
Compliance Authority
Assurance Authority
Change Authority
```

The list is a controlled assessment baseline.

It is not an assertion that each authority exists as a separately named organizational body.

---

# 12. Accountability Scope

Material governance objects shall be assessed for:

```text
Accountable Owner
Responsible Owner
Decision Authority
Approval Authority
Escalation Authority
Implementation Owner
Control Owner
Evidence Owner
Assurance Owner
```

Where a role is not established, N5-A shall record:

```text
OWNER NOT ESTABLISHED
```

rather than inventing an owner.

---

# 13. Decision Scope

N5-A shall recognize the decision classes:

```text
Class A — Strategic
Class B — Enterprise
Class C — Domain
Class D — Solution
Class E — Operational
```

The decision class shall determine the expected governance depth.

The existence of a decision class does not itself establish an approved decision-right matrix.

---

# 14. Policy Scope

N5-A shall identify material policy categories:

```text
Architecture Policy
Security Policy
Data Policy
Identity Policy
Application Policy
Infrastructure Policy
Service Policy
Risk Policy
Compliance Policy
Change Policy
Assurance Policy
```

For each material policy relationship, N5-A shall assess:

```text
Owner
Authority
Scope
Requirement
Approval
Version
Effective State
Exception Mechanism
Review Cycle
Evidence
```

---

# 15. Standards Scope

N5-A shall identify standards where governance depends on repeatable requirements.

Potential categories include:

```text
Architecture Standards
API Standards
Data Standards
Identity Standards
Cloud Standards
AI Standards
Agent Standards
Logging Standards
Security Standards
Integration Standards
```

N5-A shall distinguish:

```text
STANDARD DEFINED
from
STANDARD APPROVED
from
STANDARD IMPLEMENTED
from
STANDARD EFFECTIVE
```

---

# 16. Control Scope

N5-A shall identify material control categories:

```text
Preventive Controls
Detective Controls
Corrective Controls
Technical Controls
Process Controls
Governance Controls
Security Controls
Compliance Controls
Operational Controls
```

For each material control, the evidence baseline shall seek:

```text
Control Objective
Control Owner
Control Requirement
Control Frequency
Control Method
Control Evidence
Control Validation
Control Exception
Control Status
```

---

# 17. Risk Scope

N5-A shall identify governance relationships for:

```text
Risk Appetite
Risk Classification
Risk Thresholds
Risk Ownership
Control Requirements
Risk Treatment
Escalation
Risk Acceptance
Continuous Risk Monitoring
```

N5-A shall not infer risk acceptance merely because a risk has been identified.

---

# 18. Compliance Scope

N5-A shall identify:

```text
Regulatory Obligations
Policy Obligations
Compliance Ownership
Compliance Requirements
Compliance Monitoring
Compliance Evidence
Compliance Exceptions
Compliance Escalation
Compliance Assurance
```

No compliance state shall be declared without appropriate evidence.

---

# 19. Assurance Scope

N5-A shall identify assurance mechanisms covering:

```text
Control Validation
Compliance
Audit
Risk Assessment
Governance Review
Independent Review
Evidence Review
Architecture Conformance
Operational Assurance
```

Assurance activity shall remain distinct from the governance authority that is being assured.

---

# 20. Change Governance Scope

N5-A shall identify governance relationships for:

```text
Business Change
Architecture Change
Technology Change
Security Change
Regulatory Change
Operational Change
Policy Change
Control Change
Exception Change
```

The controlled distinction is:

```text
CHANGE
≠
AUTOMATIC APPROVAL
```

and:

```text
CHANGE REQUEST
≠
AUTHORIZED CHANGE
```

---

# 21. Exception Scope

N5-A shall identify material exception mechanisms for:

```text
Architecture Exceptions
Policy Exceptions
Standard Exceptions
Control Exceptions
Risk Acceptance
Temporary Deviations
```

Each material exception should be capable of being traced to:

```text
Reason
Risk
Owner
Authority
Approval
Expiry / Review
Compensating Control
Evidence
Status
```

---

# 22. Evidence Principle

N5-A shall apply the principle:

```text
GOVERNANCE CLAIM
        ↓
EVIDENCE REQUIREMENT
        ↓
EVIDENCE
        ↓
EVIDENCE QUALITY
        ↓
CONTROLLED STATUS
```

Evidence shall be evaluated rather than assumed.

---

# 23. Evidence Classes

N5-A shall use:

```text
E0 — Conceptual Evidence
E1 — Architectural Evidence
E2 — Governance / Implementation Model Evidence
E3 — Actual Implementation Evidence
```

Examples:

```text
E0:
Governance concept described

E1:
Governance architecture defined

E2:
Approved governance mechanism / role / process documented

E3:
Actual operation demonstrated by evidence
```

No E0 or E1 evidence shall silently be treated as E3 evidence.

---

# 24. Evidence Quality

Governance evidence shall be assessed for:

```text
Authenticity
Traceability
Currency
Completeness
Authority
Integrity
Retention
Accessibility
Relevance
```

The baseline governance requirement is that evidence be:

```text
AUTHENTIC
TRACEABLE
CURRENT
PROTECTED
RETAINED
```

---

# 25. Evidence Boundary

N5-A shall preserve the distinction:

```text
NO EVIDENCE FOUND
≠
CAPABILITY ABSENT
```

and:

```text
NOT ESTABLISHED
≠
DOES NOT EXIST
```

and:

```text
NOT VERIFIED
≠
FAILED
```

This is mandatory false-gap protection.

---

# 26. Governance Evidence Register

N5-A shall establish the following logical register:

| Field | Purpose |
|---|---|
| Evidence ID | Unique evidence reference |
| Governance Domain | Domain relationship |
| Governance Object | Object being evidenced |
| Claim | Governance claim |
| Evidence Class | E0–E3 |
| Source | Evidence source |
| Authority | Source authority |
| Date | Evidence date |
| Status | Current evidence state |
| Owner | Evidence owner |
| Validation | Validation status |
| Finding | Related finding if any |
| Condition | Related condition if any |

This is a logical baseline. A physical register requires separate artifact authorization if needed.

---

# 27. Governance Object Types

N5-A shall recognize:

```text
GOV-DOMAIN
GOV-AUTHORITY
GOV-ROLE
GOV-ACCOUNTABILITY
GOV-DECISION
GOV-POLICY
GOV-STANDARD
GOV-CONTROL
GOV-EXCEPTION
GOV-RISK
GOV-COMPLIANCE
GOV-ASSURANCE
GOV-CHANGE
GOV-EVIDENCE
GOV-OUTCOME
```

---

# 28. Governance Object Lifecycle

Where applicable, governance objects shall use:

```text
PROPOSED
DEFINED
REVIEWED
APPROVED
IMPLEMENTED
ACTIVE
SUSPENDED
SUPERSEDED
RETIRED
UNKNOWN
```

The lifecycle state must be supported by appropriate evidence.

---

# 29. Governance Boundary Rules

N5-A shall apply:

```text
IF GOVERNANCE RELATIONSHIP IS MATERIAL
    THEN ASSESS

IF GOVERNANCE RELATIONSHIP IS IMMATERIAL
    THEN RECORD AS OUT OF SCOPE

IF APPLICABILITY IS UNKNOWN
    THEN RECORD UNVERIFIED

IF EVIDENCE IS INSUFFICIENT
    THEN DO NOT UPGRADE STATUS

IF GOVERNANCE CLAIM CONFLICTS WITH EVIDENCE
    THEN CLASSIFY CONFLICT
```

---

# 30. Materiality

N5-A shall use:

```text
CRITICAL
HIGH
MEDIUM
LOW
UNKNOWN
```

Materiality shall consider:

```text
Enterprise Impact
Risk
Security
Compliance
Financial Impact
Operational Impact
Strategic Importance
Regulatory Impact
Reversibility
Dependency
```

---

# 31. Dependency Scope

N5-A shall identify dependencies between governance domains.

Examples:

```text
Architecture ↔ Security
Architecture ↔ Data
Architecture ↔ Identity
Architecture ↔ Risk
Architecture ↔ Compliance
Architecture ↔ Service
Security ↔ Identity
Data ↔ Privacy
Risk ↔ Compliance
Change ↔ Assurance
Service ↔ Operational Governance
```

Dependencies shall be assessed for materiality and authority.

---

# 32. Governance Conflict Baseline

Potential conflicts include:

```text
Authority Conflict
Accountability Conflict
Decision-right Conflict
Policy Conflict
Standard Conflict
Control Ownership Conflict
Risk Acceptance Conflict
Approval Conflict
Escalation Conflict
Exception Conflict
```

N5-A shall identify conflicts but shall not resolve them unless explicitly authorized by the relevant work package.

---

# 33. Relationship to Existing EA-IMETA Governance

The existing EA-IMETA governance material establishes:

```text
Architecture Authority
Domain Authorities
Decision Rights
Delegated Authority
Governance Hierarchy
Decision Classes
Decision Authority Matrix
Architecture Principles
Policy Model
Architecture Standards
```

These existing definitions form source material for N5-A.

N5-A shall therefore preserve established terminology and shall not redefine the Master Governance model without explicit justification.

---

# 34. Relationship to N4

N4 is closed as:

```text
N4C-2 — COMPLETE WITH CONDITIONS
```

with:

```text
COND-N4-E.01-01
=
OPEN / CONTROLLED CARRY-FORWARD
```

N5-A shall not convert this condition into an unsupported governance finding.

Where the condition affects governance evidence, N5-A may reference it as an inherited condition.

---

# 35. Relationship to N6

N5-A shall prepare governance relationships for later consumption by N6.

N6's target traceability model is:

```text
Requirement
    ↓
Capability
    ↓
Architecture Document
    ↓
Architecture Element
    ↓
Implementation Element
    ↓
Service
    ↓
Control
    ↓
Evidence
```

N5-A does not create the N6 matrix.

---

# 36. Initial Governance Scope Matrix

| Domain | Initial Scope | Evidence Required | Current State |
|---|---|---|---|
| Architecture | Authority, principles, decisions, exceptions | Governance evidence | To assess |
| Security | Security authority, policy, controls | Security governance evidence | To assess |
| Data | Ownership, stewardship, policy, quality | Data governance evidence | To assess |
| Application | Ownership, lifecycle, standards | Application governance evidence | To assess |
| Infrastructure | Standards, lifecycle, ownership | Infrastructure governance evidence | To assess |
| Identity | Authority, access decisions, reviews | Identity governance evidence | To assess |
| Service | Service ownership, governance, performance | Service governance evidence | To assess |
| Risk | Appetite, ownership, treatment | Risk governance evidence | To assess |
| Compliance | Obligations, monitoring, evidence | Compliance evidence | To assess |
| Assurance | Audit, validation, review | Assurance evidence | To assess |
| Change | Change authority and approval | Change governance evidence | To assess |

This table is a scope baseline, not an assessment result.

---

# 37. Initial Governance Evidence Questions

For each material governance domain N5-A shall ask:

```text
1. Does the governance relationship need to exist?
2. Why is it material?
3. Who is accountable?
4. Who has authority?
5. What decisions are governed?
6. Which policy applies?
7. Which standard applies?
8. Which controls apply?
9. What evidence is required?
10. How is assurance performed?
11. How are exceptions handled?
12. How is change governed?
13. How is escalation performed?
14. How is the relationship retired or superseded?
```

---

# 38. Initial Finding Classes

N5-A may classify findings as:

```text
GF-01 Missing Governance Authority
GF-02 Missing Accountability
GF-03 Missing Decision Right
GF-04 Missing Delegation
GF-05 Missing Policy
GF-06 Missing Standard
GF-07 Missing Control
GF-08 Missing Exception Mechanism
GF-09 Missing Evidence
GF-10 Missing Assurance
GF-11 Conflicting Authority
GF-12 Conflicting Decision Right
GF-13 Unverified Governance Relationship
GF-14 Governance Lifecycle Deficiency
GF-15 Governance Traceability Deficiency
GF-16 Governance Effectiveness Not Established
```

These are classification mechanisms, not pre-existing findings.

---

# 39. False-Gap Controls

N5-A shall not classify the following automatically:

```text
No named authority
→
No authority exists

No policy found
→
No policy exists

No decision record
→
No decision was made

No evidence found
→
Control failed

No governance board identified
→
Governance absent

No implementation evidence
→
Architecture invalid
```

Additional evidence shall be required.

---

# 40. Governance Evidence Decision Logic

The controlled interpretation is:

```text
CLAIM
 ↓
APPLICABILITY
 ↓
MATERIALITY
 ↓
REQUIRED EVIDENCE
 ↓
AVAILABLE EVIDENCE
 ↓
EVIDENCE QUALITY
 ↓
STATUS
```

This prevents premature findings.

---

# 41. N5-A Deliverables

N5-A shall produce, as part of the work package:

```text
1. Governance Scope Baseline
2. Governance Domain Classification
3. Governance Layer Classification
4. Authority / Accountability Scope
5. Decision Scope
6. Policy / Standard / Control Scope
7. Risk / Compliance / Assurance Scope
8. Change Governance Scope
9. Evidence Classification Model
10. Governance Boundary Register
11. Initial Finding Classification Model
12. N5-B Readiness Assessment
```

These deliverables remain logical outputs until separately authorized as physical documents or registers where required.

---

# 42. N5-A Completion Criteria

N5-A may be considered complete when:

```text
Governance Domains Identified
AND
Governance Layers Defined
AND
Authority Scope Defined
AND
Accountability Scope Defined
AND
Decision Scope Defined
AND
Policy / Standard / Control Scope Defined
AND
Risk / Compliance / Assurance Scope Defined
AND
Change Scope Defined
AND
Evidence Model Defined
AND
False-Gap Controls Established
AND
Governance Boundaries Established
AND
N5-B Readiness Determined
```

---

# 43. N5-A Completion Recommendation

At initiation:

```text
N5-A
=
ACTIVE
```

No completion recommendation shall be issued until the completion criteria have been assessed.

---

# 44. Current State

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
= ACTIVE / GOVERNANCE SCOPE & EVIDENCE BASELINE

N5-B
= NOT STARTED

N5-C
= NOT STARTED

N5-D
= NOT STARTED

N5-E
= NOT STARTED

N6
= NOT AUTHORIZED
```

---

# 45. Authority Boundary

N5-A does not authorize:

```text
Final Governance Approval
Final Organizational Appointment
Policy Approval
Control Certification
Operational Effectiveness Certification
N5 Closure
N6 Generation
New Capability Creation
```

Any such action requires its own appropriate authority.

---

# 46. Final N5-A Statement

> **N5-A establishes the controlled Governance Scope & Evidence Baseline for the MFM Post-Steady-State N5 workstream. It defines the governance domains, governance layers, authority and accountability scope, decision scope, policy/standard/control scope, risk/compliance/assurance scope, change governance scope, evidence classes, materiality and false-gap controls required for subsequent N5 work. N5-A does not assume that candidate governance structures exist merely because they are architecturally defined. Governance claims shall be supported by appropriate evidence, and the final N5 boundaries shall remain derived from the actual governance model.**

---

# 47. Document Control

**Document:** MFM Post-Steady-State Phase Control — N5-A Governance Scope & Evidence Baseline  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N5-A-Governance-Scope-and-Evidence-Baseline-001  
**Version:** 1.0  
**Status:** ACTIVE — N5-A WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N5 — Governance & Control Architecture  
**Parent:** N5.00 — Governance & Control Architecture Scope, Charter and Work Package Control  
**Predecessor:** N5.00  
**N4 Closure:** N4-SC-90 — CLOSED  
**N4 Completion:** N4C-2 — COMPLETE WITH CONDITIONS  
**N5 Authorization:** EXPLICITLY APPROVED  
**Current Work Package:** N5-A  
**Next Work Package:** N5-B — Authority, Accountability & Decision Rights Model  
**Automatic Successor Generation:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  
**Automatic N6 Generation:** PROHIBITED  

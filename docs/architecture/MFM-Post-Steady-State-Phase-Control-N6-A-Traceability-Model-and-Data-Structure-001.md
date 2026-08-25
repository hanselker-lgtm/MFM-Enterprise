# MFM Post-Steady-State Phase Control

## N6-A — Traceability Model & Data Structure

**Control ID:** MFM-Post-Steady-State-Phase-Control-N6-A-Traceability-Model-and-Data-Structure-001  
**Version:** 1.0  
**Status:** ACTIVE — N6-A WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N6 — Architecture Traceability Matrix  
**Parent:** N6-00 — Architecture Traceability Matrix Scope, Readiness & Authorization Control  
**Authorization:** N6-A AUTHORIZED  
**Predecessor:** N6-AUTH-DEC — Formal N6 Authorization Decision  
**Next Work Package:** N6-B — Requirement-to-Architecture Traceability  

---

# 1. Purpose

N6-A establishes the controlled traceability model and data structure that shall be used by the N6 Architecture Traceability Matrix.

The objective is to define:

```text
Traceability Objects
Identifiers
Relationship Types
Relationship Semantics
Cardinality
Lifecycle States
Evidence Classes
Validation States
Ownership Fields
Source References
Change References
```

N6-A establishes the model.

It does not populate the complete enterprise traceability matrix.

---

# 2. Authorization

N6 was formally authorized.

N6-A is therefore:

```text
AUTHORIZED / ACTIVE
```

The approved N6 sequence remains:

```text
N6-A
    ↓
N6-B
    ↓
N6-C
    ↓
N6-D
    ↓
N6-E
```

N6-A shall remain within the authorized N6 scope.

---

# 3. Primary Traceability Model

The primary chain is:

```text
Requirement
    ↓
Capability
    ↓
Architecture
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

Cross-cutting relationships are:

```text
Risk
Compliance
Governance
Assurance
Decision
Owner
Lifecycle
Change
```

---

# 4. Traceability Object Model

The controlled N6 object classes are:

```text
T01 Requirement
T02 Capability
T03 Architecture Domain
T04 Architecture Principle
T05 Architecture Element
T06 Solution Element
T07 Implementation Element
T08 Service
T09 Policy
T10 Standard
T11 Control
T12 Risk
T13 Compliance Obligation
T14 Assurance Activity
T15 Evidence
T16 Decision
T17 Exception
T18 Owner / Role
T19 Change
T20 Lifecycle Record
```

These are traceability object classes.

Their existence in the model does not imply that every object exists in the actual enterprise.

---

# 5. T01 — Requirement

Minimum structure:

```text
Requirement ID
Requirement Name
Requirement Statement
Requirement Type
Source
Priority
Owner
Applicability
Status
Lifecycle
Evidence Reference
```

Requirement types may include:

```text
Business
Strategic
Regulatory
Contractual
Security
Data
Operational
Architecture
Technology
Risk
Compliance
Service
```

---

# 6. T02 — Capability

Minimum structure:

```text
Capability ID
Capability Name
Business Outcome
Description
Owner
Source Requirement
Status
Lifecycle
Evidence Reference
```

A capability shall not be inferred solely from the existence of a system, service or organizational unit.

---

# 7. T03 — Architecture Domain

Minimum structure:

```text
Domain ID
Domain Name
Domain Type
Description
Owner
Lifecycle
Status
```

Possible domains:

```text
Business
Information
Application
Technology
Security
Data
Integration
AI / Agent
Infrastructure
Service
Operational
```

Only materially applicable domains shall be populated.

---

# 8. T04 — Architecture Principle

Minimum structure:

```text
Principle ID
Principle Name
Principle Statement
Rationale
Authority
Applicability
Status
Lifecycle
Source
```

The principle may govern:

```text
Policy
Standard
Architecture Decision
Control
Design
Implementation
```

---

# 9. T05 — Architecture Element

Minimum structure:

```text
Element ID
Element Name
Element Type
Architecture Domain
Description
Owner
Lifecycle
Status
Source
Evidence
```

Element types may include:

```text
Process
Information Object
Data Object
Application
Service
API
Integration
Technology Component
Infrastructure Component
Security Component
Identity Component
AI Model
Agent
Control
```

---

# 10. T06 — Solution Element

Minimum structure:

```text
Solution ID
Solution Element ID
Element Type
Description
Architecture Parent
Owner
Status
Lifecycle
Evidence
```

The solution layer shall remain distinguishable from both architecture and implementation.

---

# 11. T07 — Implementation Element

Minimum structure:

```text
Implementation ID
Implementation Type
Name
Architecture Parent
Solution Parent
Owner
Environment
Status
Lifecycle
Evidence
```

Possible implementation types:

```text
System
Component
Configuration
Deployment
Infrastructure
Service Instance
Data Store
Interface
Agent Instance
Operational Component
```

Architecture existence does not prove implementation existence.

---

# 12. T08 — Service

Minimum structure:

```text
Service ID
Service Name
Capability
Architecture Element
Implementation Element
Owner
Service Status
Lifecycle
Control
Risk
Evidence
```

---

# 13. T09 — Policy

Minimum structure:

```text
Policy ID
Policy Name
Authority
Owner
Scope
Status
Lifecycle
Effective Date
Review Date
Source
```

Policy remains distinct from:

```text
Standard
Procedure
Control
```

---

# 14. T10 — Standard

Minimum structure:

```text
Standard ID
Standard Name
Parent Policy
Owner
Scope
Status
Lifecycle
Effective Date
Review Date
Source
```

---

# 15. T11 — Control

Minimum structure:

```text
Control ID
Control Name
Control Type
Requirement
Policy
Standard
Risk
Owner
Evidence
Status
Lifecycle
Assurance
```

Control types may include:

```text
Preventive
Detective
Corrective
Directive
Compensating
Automated
Manual
```

A control definition does not prove that the control operates effectively.

---

# 16. T12 — Risk

Minimum structure:

```text
Risk ID
Risk Statement
Risk Category
Owner
Likelihood
Impact
Risk Rating
Treatment
Residual Risk
Acceptance Authority
Status
Lifecycle
Evidence
```

Possible categories:

```text
Strategic
Enterprise
Architecture
Operational
Security
Compliance
Financial
Data
AI
Agent
Supplier
Resilience
Reputational
```

---

# 17. T13 — Compliance Obligation

Minimum structure:

```text
Obligation ID
Source
Requirement
Applicability
Jurisdiction
Owner
Effective Date
Review Date
Status
Control
Evidence
Assurance
```

N6 shall not infer compliance solely because an obligation is linked to a control.

---

# 18. T14 — Assurance Activity

Minimum structure:

```text
Assurance ID
Assurance Type
Scope
Criteria
Authority
Performer
Independence
Date
Result
Finding
Evidence
Status
```

Possible types:

```text
Control Validation
Compliance Assurance
Risk Assessment
Architecture Conformance
Operational Assurance
Independent Review
Audit
Certification / Attestation
Governance Review
```

---

# 19. T15 — Evidence

Minimum structure:

```text
Evidence ID
Evidence Type
Evidence Class
Source
Claim
Requirement
Architecture Element
Control
Date
Owner
Validity
Status
Retention
```

Evidence classes:

```text
E0 — Conceptual Evidence
E1 — Architectural Evidence
E2 — Governance / Implementation Model Evidence
E3 — Actual Implementation Evidence
```

The established boundary remains:

```text
E0 / E1
≠
E3
```

---

# 20. T16 — Decision

Minimum structure:

```text
Decision ID
Decision Statement
Decision Class
Authority
Decision Date
Rationale
Affected Object
Risk
Conditions
Evidence
Status
```

Decision classes may include:

```text
Architecture
Governance
Risk
Compliance
Exception
Change
Security
Service
```

---

# 21. T17 — Exception

Minimum structure:

```text
Exception ID
Requirement
Exception Statement
Reason
Risk
Owner
Authority
Compensating Control
Approval
Expiry
Review
Evidence
Status
```

An exception is not automatically equivalent to approval of non-compliance.

---

# 22. T18 — Owner / Role

Minimum structure:

```text
Owner ID
Role
Accountability
Responsibility
Authority
Scope
Status
Source
```

Where an actual owner is not evidenced:

```text
OWNER NOT ESTABLISHED
```

shall be recorded rather than inventing an assignment.

---

# 23. T19 — Change

Minimum structure:

```text
Change ID
Change Type
Requestor
Owner
Affected Object
Impact
Risk
Authority
Approval
Implementation
Validation
Evidence
Status
Lifecycle
```

Change types may include:

```text
Business
Architecture
Technology
Security
Regulatory
Operational
Policy
Control
Exception
AI / Agent
```

---

# 24. T20 — Lifecycle Record

Minimum structure:

```text
Lifecycle ID
Object ID
Previous State
New State
Effective Date
Authority
Evidence
Reason
Change Reference
```

Lifecycle history shall be preserved where material.

---

# 25. Relationship Model

N6-A defines the following controlled relationship types:

```text
SATISFIES
IMPLEMENTS
SUPPORTS
GOVERNS
DEPENDS_ON
OWNED_BY
OPERATED_BY
CONTROLLED_BY
EVIDENCED_BY
ASSESSED_BY
APPROVED_BY
DERIVED_FROM
IMPACTS
CONSTRAINS
SUPERSEDES
```

---

# 26. SATISFIES

```text
Requirement
    ↓
SATISFIES
    ↓
Capability / Architecture Element / Control
```

The relationship means that the target is intended to satisfy the source requirement.

It does not alone prove effectiveness.

---

# 27. IMPLEMENTS

```text
Architecture Element
    ↓
IMPLEMENTS
    ↓
Solution / Implementation Element
```

This relationship indicates realization.

It does not alone prove that the implementation is operational.

---

# 28. SUPPORTS

```text
Capability
    ↓
SUPPORTS
    ↓
Service / Architecture Element
```

The relationship indicates contribution to the source outcome.

---

# 29. GOVERNS

```text
Policy
    ↓
GOVERNS
    ↓
Standard / Control / Architecture Element
```

The relationship indicates governance scope.

---

# 30. DEPENDS_ON

```text
Object A
    ↓
DEPENDS_ON
    ↓
Object B
```

Dependency may be:

```text
Business
Technical
Data
Security
Operational
Regulatory
Service
```

---

# 31. OWNED_BY

```text
Object
    ↓
OWNED_BY
    ↓
Owner / Role
```

This relationship requires evidence where actual ownership is claimed.

---

# 32. OPERATED_BY

```text
Service / Implementation
    ↓
OPERATED_BY
    ↓
Role / Organization
```

Operational responsibility is distinct from accountability.

---

# 33. CONTROLLED_BY

```text
Requirement / Risk / Service / Element
    ↓
CONTROLLED_BY
    ↓
Control
```

This relationship identifies the relevant control.

It does not prove control effectiveness.

---

# 34. EVIDENCED_BY

```text
Claim / Relationship / Control
    ↓
EVIDENCED_BY
    ↓
Evidence
```

Evidence shall support the claim it is associated with.

---

# 35. ASSESSED_BY

```text
Object
    ↓
ASSESSED_BY
    ↓
Assurance Activity
```

This relationship identifies the assessment mechanism.

It does not establish the result.

---

# 36. APPROVED_BY

```text
Decision / Policy / Change / Exception
    ↓
APPROVED_BY
    ↓
Authority
```

Approval shall remain evidence-dependent.

---

# 37. DERIVED_FROM

```text
Architecture / Requirement / Policy / Standard
    ↓
DERIVED_FROM
    ↓
Source
```

The relationship identifies origin or derivation.

---

# 38. IMPACTS

```text
Change / Risk / Requirement
    ↓
IMPACTS
    ↓
Affected Object
```

This relationship supports change-impact analysis.

---

# 39. CONSTRAINS

```text
Policy / Standard / Requirement
    ↓
CONSTRAINS
    ↓
Architecture / Solution / Implementation
```

This relationship identifies an imposed boundary.

---

# 40. SUPERSEDES

```text
New Object
    ↓
SUPERSEDES
    ↓
Previous Object
```

The previous object shall not be silently deleted.

---

# 41. Relationship Record Structure

Each material relationship shall be capable of carrying:

```text
Relationship ID
Source Object ID
Source Type
Relationship Type
Target Object ID
Target Type
Source Reference
Evidence Reference
Owner
Status
Lifecycle
Effective Date
Review Date
Confidence / Validation State
Change Reference
```

---

# 42. Relationship Validation States

Each relationship may be:

```text
PROPOSED
ESTABLISHED
VALIDATED
CONDITIONAL
UNVERIFIED
CONFLICTING
SUPERSEDED
RETIRED
```

Definitions:

```text
PROPOSED
Relationship suggested but not yet established.

ESTABLISHED
Relationship supported by source material.

VALIDATED
Relationship independently checked within the authorized N6 process.

CONDITIONAL
Relationship valid subject to a documented condition.

UNVERIFIED
Insufficient evidence to validate.

CONFLICTING
Conflicting source relationships exist.

SUPERSEDED
Relationship replaced by a later relationship.

RETIRED
Relationship no longer active.
```

---

# 43. Cardinality Model

N6-A supports:

```text
ONE-TO-ONE
ONE-TO-MANY
MANY-TO-ONE
MANY-TO-MANY
```

Examples:

```text
Requirement
→
Many Architecture Elements

Capability
→
Many Services

Control
→
Many Requirements

Evidence
→
Many Claims
```

Cardinality shall not be interpreted as completeness.

---

# 44. Identifier Model

Every material traceability object shall have a stable identifier.

Recommended format:

```text
<DOMAIN>-<TYPE>-<SEQUENCE>
```

Examples:

```text
REQ-001
CAP-001
ARC-001
IMP-001
SRV-001
POL-001
STD-001
CTL-001
RSK-001
CMP-001
ASM-001
EVD-001
DEC-001
EXC-001
CHG-001
```

Identifiers shall remain stable through lifecycle changes unless formally superseded.

---

# 45. Source Reference

Each material object should retain:

```text
Source Document
Source Section
Source Location
Source Date
Source Version
```

This ensures traceability back to the originating artifact.

---

# 46. Evidence Reference

Where evidence exists:

```text
Evidence ID
Evidence Class
Evidence Source
Evidence Date
Validation State
```

shall be retained.

No evidence shall be invented to complete a matrix field.

---

# 47. Lifecycle Model

The baseline lifecycle is:

```text
PROPOSED
    ↓
DEFINED
    ↓
APPROVED
    ↓
IMPLEMENTED
    ↓
ACTIVE
    ↓
VALIDATED
    ↓
SUPERSEDED / RETIRED
```

Objects may legitimately skip states where the lifecycle model permits it.

Unknown state shall remain:

```text
UNKNOWN
```

rather than being inferred.

---

# 48. Ownership Model

N6-A distinguishes:

```text
ACCOUNTABLE
RESPONSIBLE
AUTHORIZED
OWNER
OPERATOR
EVIDENCE OWNER
ASSURANCE OWNER
```

These roles are not automatically interchangeable.

---

# 49. Evidence Classes and Claims

N6-A shall associate claims with the minimum evidence class required.

Example:

```text
Concept Exists
→ E0 may be sufficient

Architecture Defined
→ E1 may be sufficient

Governance / Implementation Model Defined
→ E2 may be sufficient

Actual Implementation
→ E3 required

Operational Effectiveness
→ appropriate operational evidence required
```

This prevents architectural claims from being silently promoted into operational claims.

---

# 50. Traceability Matrix Core Schema

The conceptual matrix row is:

| Field | Description |
|---|---|
| Trace ID | Unique relationship identifier |
| Source ID | Source object |
| Source Type | Source object class |
| Relationship | Semantic relationship |
| Target ID | Target object |
| Target Type | Target object class |
| Status | Relationship status |
| Lifecycle | Relationship lifecycle |
| Source Reference | Originating artifact |
| Evidence | Supporting evidence |
| Owner | Responsible traceability owner |
| Effective Date | Relationship validity |
| Review Date | Review point |
| Change Reference | Related change |

---

# 51. Traceability Matrix Example

Example only:

| Source | Relationship | Target | Evidence State |
|---|---|---|---|
| REQ-001 | SATISFIES | CAP-001 | ESTABLISHED |
| CAP-001 | SUPPORTS | SRV-001 | ESTABLISHED |
| SRV-001 | IMPLEMENTS | ARC-001 | UNVERIFIED |
| ARC-001 | CONTROLLED_BY | CTL-001 | ESTABLISHED |
| CTL-001 | EVIDENCED_BY | EVD-001 | VALIDATED |

These are structural examples, not claims about actual MFM implementation.

---

# 52. Orphan Model

N6-A defines potential orphan states:

```text
ORPHAN-REQ
Requirement without downstream relationship

ORPHAN-CAP
Capability without architecture relationship

ORPHAN-ARC
Architecture without upstream rationale

ORPHAN-IMP
Implementation without architecture relationship

ORPHAN-SRV
Service without capability relationship

ORPHAN-CTL
Control without requirement/risk relationship

ORPHAN-EVD
Evidence without supported claim

ORPHAN-DEC
Decision without authority relationship
```

These are detection classes, not findings by themselves.

---

# 53. Broken Chain Model

Potential broken chains include:

```text
Requirement
 ↓
[NO CAPABILITY]

Capability
 ↓
[NO ARCHITECTURE]

Architecture
 ↓
[NO IMPLEMENTATION]

Implementation
 ↓
[NO SERVICE]

Control
 ↓
[NO EVIDENCE]
```

Each condition shall be assessed for:

```text
Applicability
Materiality
Evidence
Intent
```

---

# 54. Change Impact Structure

N6-A supports:

```text
Change
 ↓
Affected Requirement
 ↓
Affected Capability
 ↓
Affected Architecture
 ↓
Affected Implementation
 ↓
Affected Service
 ↓
Affected Control
 ↓
Affected Evidence
```

This structure shall support later N6-C traceability.

---

# 55. Governance Traceability Structure

The N5 governance chain is represented as:

```text
Principle
 ↓
Policy
 ↓
Standard
 ↓
Procedure
 ↓
Control
 ↓
Evidence
 ↓
Assurance
```

N6-A defines the structure.

N6-D will perform the controlled governance/risk/compliance population.

---

# 56. Risk Traceability Structure

The risk relationship is:

```text
Risk
 ↓
Affected Capability
 ↓
Affected Architecture
 ↓
Affected Service
 ↓
Control
 ↓
Evidence
 ↓
Treatment
 ↓
Acceptance / Escalation
```

N6-A defines the relationship types.

N6-D will perform the controlled population.

---

# 57. Compliance Traceability Structure

The compliance relationship is:

```text
Compliance Obligation
 ↓
Requirement
 ↓
Policy
 ↓
Standard
 ↓
Control
 ↓
Evidence
 ↓
Assurance
```

Traceability does not itself certify compliance.

---

# 58. Decision Traceability Structure

The decision chain is:

```text
Requirement / Risk / Change
        ↓
Decision
        ↓
Authority
        ↓
Rationale
        ↓
Affected Object
        ↓
Evidence
```

---

# 59. Validation Rules

N6-A establishes the following validation rules:

```text
VR-01
Source object must exist or be explicitly marked unresolved.

VR-02
Target object must exist or be explicitly marked unresolved.

VR-03
Relationship type must be from the authorized relationship vocabulary.

VR-04
Relationship semantics must match the source and target types.

VR-05
Material ownership claims require evidence.

VR-06
Approval claims require evidence.

VR-07
Effectiveness claims require appropriate operational evidence.

VR-08
Lifecycle transitions require a valid source or decision.

VR-09
Superseded relationships shall not be silently deleted.

VR-10
Unknown information shall remain explicitly unknown.

VR-11
No relationship shall be invented to eliminate an apparent gap.

VR-12
N5 conditions shall remain traceable.
```

---

# 60. False-Gap Rules

The following are prohibited:

```text
Blank field
→
Invented value

Missing relationship
→
Assumed relationship

Missing owner
→
Assumed owner

Missing evidence
→
Synthetic evidence

Architecture object
→
Assumed implementation

Traceability
→
Assumed compliance

Control relationship
→
Assumed effectiveness
```

---

# 61. N6-A Deliverables

N6-A shall produce:

```text
D-A01
Traceability Object Catalogue

D-A02
Relationship Vocabulary

D-A03
Relationship Semantics

D-A04
Identifier Model

D-A05
Lifecycle Model

D-A06
Evidence Classification Model

D-A07
Traceability Matrix Core Schema

D-A08
Validation Rules

D-A09
Orphan / Broken Chain Detection Model

D-A10
N6-A Completion Recommendation
```

---

# 62. N6-A Completion Criteria

N6-A may be considered complete when:

```text
Traceability Objects Defined
AND
Identifiers Defined
AND
Relationship Vocabulary Defined
AND
Relationship Semantics Defined
AND
Cardinality Defined
AND
Lifecycle Defined
AND
Evidence Classes Defined
AND
Validation States Defined
AND
Core Matrix Schema Defined
AND
False-Gap Rules Defined
AND
Orphan Detection Defined
AND
Broken Chain Detection Defined
AND
N6-B Input Prepared
```

---

# 63. Current N6-A State

```text
N6-A
=
ACTIVE
```

The model is established in this work package.

Population of enterprise traceability data begins only within the authorized subsequent work packages.

---

# 64. Next Work Package

Upon N6-A completion, the next controlled work package is:

```text
N6-B
Requirement-to-Architecture Traceability
```

N6-B shall use the N6-A model without silently changing its semantics.

Any material change to the model shall be documented and controlled.

---

# 65. Current Program State

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

N5 CONDITIONS
= ACTIVE CARRY-FORWARD

N6
= AUTHORIZED / ACTIVE

N6.00
= COMPLETED

N6-A
= ACTIVE

N6-B
= AUTHORIZED / SCHEDULED

N6-C
= AUTHORIZED / SCHEDULED

N6-D
= AUTHORIZED / SCHEDULED

N6-E
= AUTHORIZED / SCHEDULED
```

---

# 66. Final N6-A Statement

> **N6-A establishes the controlled Traceability Model & Data Structure for the authorized N6 Architecture Traceability Matrix workstream. It defines the traceability object catalogue, identifier model, relationship vocabulary and semantics, cardinality, lifecycle, evidence classes, validation states, matrix schema, ownership model, orphan detection and broken-chain controls. N6-A does not claim that the modeled objects or relationships exist in the actual enterprise; population and validation of actual traceability data are controlled by subsequent N6 work packages.**

---

# 67. Document Control

**Document:** MFM Post-Steady-State Phase Control — N6-A Traceability Model & Data Structure  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N6-A-Traceability-Model-and-Data-Structure-001  
**Version:** 1.0  
**Status:** ACTIVE — N6-A WORK PACKAGE  
**Date:** 18 August 2026  
**Phase:** MFM Post-Steady-State  
**Workstream:** N6 — Architecture Traceability Matrix  
**Parent:** N6-00 — Architecture Traceability Matrix Scope, Readiness & Authorization Control  
**Authorization:** N6-A AUTHORIZED  
**Predecessor:** N6-AUTH-DEC — Formal N6 Authorization Decision  
**Current Work Package:** N6-A  
**Next Work Package:** N6-B — Requirement-to-Architecture Traceability  
**Automatic Scope Expansion:** PROHIBITED  
**Automatic Capability Expansion:** PROHIBITED  

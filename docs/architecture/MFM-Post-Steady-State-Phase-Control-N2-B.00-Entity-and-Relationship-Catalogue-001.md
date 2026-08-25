# MFM Post-Steady-State Phase Control
## N2-B.00 — Entity & Relationship Catalogue

**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-B.00-Entity-and-Relationship-Catalogue-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-B WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-A.00 — Traceability Model & Meta-Model  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-B — Entity & Relationship Catalogue  
**State:** N2-B.00 — CATALOGUE ESTABLISHMENT

---

# 1. Purpose

N2-B.00 converts the abstract traceability meta-model established by N2-A.00 into a controlled catalogue of entity classes and relationship types.

N2-A.00 established that the traceability model requires:

```text
Entities
Relationships
Ownership
Evidence
Status
Lifecycle
Materiality
Traceability Depth
Validation
```

N2-B.00 defines the controlled vocabulary needed to represent those objects consistently.

This document is a catalogue and semantic control.

It does not perform the actual MFM traceability mapping.

It does not create new architecture.

It does not authorize a new Steady-State document sequence.

---

# 2. Governing Chain

The controlled sequence is:

```text
MFM v1.2-Steady-State
        ↓
SC-90 — SERIES CLOSED
        ↓
N1.00 — POST-STEADY-STATE PHASE CHARTER
        ↓
N2.00 — TRACEABILITY CONTROL & SCOPE
        ↓
N2-A.00 — TRACEABILITY MODEL
        ↓
N2-B.00 — ENTITY & RELATIONSHIP CATALOGUE
```

N2-B therefore implements the semantic layer required by N2-A.

---

# 3. Catalogue Objectives

The catalogue shall provide:

```text
1. Stable terminology
2. Controlled entity classes
3. Controlled relationship types
4. Clear semantic boundaries
5. Ownership expectations
6. Lifecycle expectations
7. Evidence expectations
8. Validation expectations
9. Compatibility with the existing EA-IMETA model
10. Prevention of duplicate concepts
```

---

# 4. Catalogue Principles

## 4.1 Existing-First

Existing authoritative concepts shall be reused before introducing new ones.

## 4.2 Semantic Stability

A term shall have one controlled meaning within the traceability model.

## 4.3 Minimum Necessary Vocabulary

The catalogue shall contain the minimum coherent set of concepts required for material traceability.

## 4.4 No Artificial Expansion

A new entity class shall not be created merely because another label could be useful.

## 4.5 Relationship Before Document

A traceability need should first be represented as a relationship before considering creation of another document.

---

# 5. Entity Classification

N2-B groups entity classes into nine families:

```text
E1  Strategic
E2  Business / Outcome
E3  Capability
E4  Requirement / Governance
E5  Architecture
E6  Implementation
E7  Operation
E8  Control / Evidence
E9  Measurement / Value
```

---

# 6. E1 — Strategic Entities

The strategic family contains:

```text
Enterprise
Purpose
Stakeholder
Strategy
Objective
```

### Enterprise

Represents the organizational or enterprise context within which the architecture exists.

### Purpose

Represents the fundamental reason the enterprise or architecture exists.

### Stakeholder

Represents a party with an interest, concern, requirement or accountability relationship.

### Strategy

Represents strategic direction or deliberate strategic choice.

### Objective

Represents a defined strategic or business result to be achieved.

---

# 7. E2 — Business / Outcome Entities

The business/outcome family contains:

```text
Outcome
Value Stream
Business Service
Process
Organization
Role
```

### Outcome

Represents an intended or achieved result.

### Value Stream

Represents the sequence of activities through which value is created or delivered.

### Business Service

Represents a service provided to a business consumer or stakeholder.

### Process

Represents repeatable activities used to produce an outcome.

### Organization

Represents an organizational unit.

### Role

Represents an accountable or responsible function.

---

# 8. E3 — Capability Entities

The capability family is centered on:

```text
Capability
```

A capability represents what the enterprise is able to do.

The inherited canonical MFM capability baseline is:

```text
CAN-01 Enterprise Integration
CAN-02 Enterprise Application
CAN-03 Enterprise Infrastructure
CAN-04 Enterprise Network
CAN-05 Enterprise Cybersecurity
CAN-06 Security Operations
CAN-07 Data Platform & Analytics
CAN-08 Identity & Access Management
```

These are inherited from the closed Steady-State baseline and are not redefined by N2-B.

---

# 9. E4 — Requirement / Governance Entities

This family contains:

```text
Requirement
Decision
Policy
Standard
```

### Requirement

Represents a stated need or constraint that must be satisfied.

### Decision

Represents an approved architectural or governance choice and its rationale.

### Policy

Represents a governing rule or mandatory direction.

### Standard

Represents a defined technical, architectural or operational standard.

---

# 10. E5 — Architecture Entities

The architecture family includes:

```text
Information
Architecture Element
Dependency
Risk
```

Where more specific architecture classes are required, they may be represented through controlled types of Architecture Element rather than creating duplicate top-level concepts.

An architecture element should retain:

```text
Identity
Type
Purpose
Context
Owner
Relationships
Dependencies
Constraints
Lifecycle
Value
Risk
Status
Evidence
```

This preserves the existing EA-IMETA architecture-element principle.

---

# 11. E6 — Implementation Entities

The implementation family contains:

```text
Application
Application Service
Data Asset
Data Product
Technology Component
Platform
Infrastructure Component
Network Component
Security Component
AI Model
AI Service
Agent
Tool
Interface
Integration
```

These represent realization of architecture.

The presence of an implementation class does not imply that the corresponding technology exists in the current MFM environment.

---

# 12. E7 — Operational Entities

The operational family contains:

```text
Service
Process
Operational Event
Change
Incident
Problem
```

Where an operational class is required but not yet represented by the current MFM source material, it shall remain a model class rather than being asserted as an existing MFM object.

---

# 13. E8 — Control / Evidence Entities

This family contains:

```text
Control
Evidence
```

### Control

Represents a mechanism used to manage, protect, assure or constrain an entity or relationship.

### Evidence

Represents information supporting an architectural or operational claim.

Evidence is not automatically proof of correctness.

Its confidence and validation status must be recorded separately.

---

# 14. E9 — Measurement / Value Entities

This family contains:

```text
Measurement
Value
```

### Measurement

Represents a KPI, KRI, performance measure, maturity measure, outcome measure or similar metric.

### Value

Represents the business, operational, strategic, financial, security, compliance or other value associated with an architecture or outcome.

---

# 15. Entity Catalogue

| ID | Entity Class | Family | Primary Meaning |
|---|---|---|---|
| ENT-01 | Enterprise | E1 | Enterprise context |
| ENT-02 | Purpose | E1 | Fundamental reason for existence |
| ENT-03 | Stakeholder | E1 | Interested or accountable party |
| ENT-04 | Strategy | E1 | Strategic direction |
| ENT-05 | Objective | E1 | Intended result |
| ENT-06 | Outcome | E2 | Result achieved/intended |
| ENT-07 | Value Stream | E2 | Value creation sequence |
| ENT-08 | Business Service | E2 | Business-facing service |
| ENT-09 | Process | E2 | Repeatable activity sequence |
| ENT-10 | Organization | E2 | Organizational unit |
| ENT-11 | Role | E2 | Responsibility/function |
| ENT-12 | Capability | E3 | Enterprise ability |
| ENT-13 | Requirement | E4 | Need or constraint |
| ENT-14 | Decision | E4 | Approved choice |
| ENT-15 | Policy | E4 | Governing rule |
| ENT-16 | Standard | E4 | Defined standard |
| ENT-17 | Architecture Element | E5 | Architectural object |
| ENT-18 | Information | E5 | Information concept |
| ENT-19 | Dependency | E5 | Material dependency |
| ENT-20 | Risk | E5 | Risk affecting architecture |
| ENT-21 | Application | E6 | Application realization |
| ENT-22 | Application Service | E6 | Application-provided service |
| ENT-23 | Data Asset | E6 | Implemented data asset |
| ENT-24 | Data Product | E6 | Managed data product |
| ENT-25 | Technology Component | E6 | Technology realization |
| ENT-26 | Platform | E6 | Technology platform |
| ENT-27 | Infrastructure Component | E6 | Infrastructure realization |
| ENT-28 | Network Component | E6 | Network realization |
| ENT-29 | Security Component | E6 | Security realization |
| ENT-30 | AI Model | E6 | AI model |
| ENT-31 | AI Service | E6 | AI-provided service |
| ENT-32 | Agent | E6 | Autonomous/agentic component |
| ENT-33 | Tool | E6 | Agent/tool capability |
| ENT-34 | Interface | E6 | Technical interface |
| ENT-35 | Integration | E6 | Integration realization |
| ENT-36 | Service | E7 | Operational service |
| ENT-37 | Operational Event | E7 | Operational occurrence |
| ENT-38 | Change | E7 | Controlled operational change |
| ENT-39 | Incident | E7 | Service disruption/event |
| ENT-40 | Problem | E7 | Underlying recurring cause |
| ENT-41 | Control | E8 | Control mechanism |
| ENT-42 | Evidence | E8 | Supporting evidence |
| ENT-43 | Measurement | E9 | Metric or measurement |
| ENT-44 | Value | E9 | Resulting value |

---

# 16. Canonical Relationship Families

Relationships are grouped into:

```text
R1  Strategic
R2  Business
R3  Capability
R4  Requirement
R5  Architecture
R6  Implementation
R7  Operational
R8  Governance / Control
R9  Evidence
R10 Measurement / Value
R11 Dependency
```

---

# 17. R1 — Strategic Relationships

Controlled relationships:

```text
SUPPORTS
DERIVES_FROM
ALIGNS_WITH
```

Examples:

```text
Strategy ──SUPPORTS──► Objective
Objective ──DERIVES_FROM──► Strategy
Architecture ──ALIGNS_WITH──► Strategy
```

---

# 18. R2 — Business Relationships

Controlled relationships:

```text
ENABLES
PROVIDES
CONSUMES
PARTICIPATES_IN
REALIZES
```

Examples:

```text
Capability ──ENABLES──► Outcome
Organization ──PROVIDES──► Business Service
Process ──REALIZES──► Outcome
```

---

# 19. R3 — Capability Relationships

Controlled relationships:

```text
REALIZES
ENABLES
SUPPORTS
DEPENDS_ON
```

Examples:

```text
Architecture ──REALIZES──► Capability
Capability ──ENABLES──► Outcome
Capability ──DEPENDS_ON──► Capability
```

---

# 20. R4 — Requirement Relationships

Controlled relationships:

```text
SATISFIES
DERIVES_FROM
CONSTRAINS
VALIDATES
```

Examples:

```text
Architecture ──SATISFIES──► Requirement
Requirement ──DERIVES_FROM──► Stakeholder Need
Policy ──CONSTRAINS──► Requirement
```

---

# 21. R5 — Architecture Relationships

Controlled relationships:

```text
DEPENDS_ON
ENABLES
CONSTRAINS
AFFECTS
USES
PROVIDES
```

Examples:

```text
Architecture Element ──DEPENDS_ON──► Architecture Element
Architecture Element ──AFFECTS──► Capability
Architecture Element ──USES──► Information
```

---

# 22. R6 — Implementation Relationships

Controlled relationships:

```text
IMPLEMENTS
REALIZES
PROVIDES
CONSUMES
USES
INTEGRATES_WITH
```

Examples:

```text
Application ──IMPLEMENTS──► Architecture Element
Application ──PROVIDES──► Application Service
Integration ──INTEGRATES_WITH──► Application
```

---

# 23. R7 — Operational Relationships

Controlled relationships:

```text
OPERATES
SUPPORTS
PROVIDES
CONSUMES
AFFECTS
CHANGES
RECOVERS
```

Examples:

```text
Service ──SUPPORTS──► Capability
Change ──AFFECTS──► Service
Operational Process ──OPERATES──► Service
```

---

# 24. R8 — Governance / Control Relationships

Controlled relationships:

```text
GOVERNS
PROTECTS
CONSTRAINS
OWNS
VALIDATES
```

Examples:

```text
Policy ──GOVERNS──► Architecture Element
Control ──PROTECTS──► Asset
Role ──OWNS──► Capability
Authority ──VALIDATES──► Decision
```

---

# 25. R9 — Evidence Relationships

Controlled relationships:

```text
EVIDENCES
SUPPORTS
VALIDATES
```

Examples:

```text
Evidence ──EVIDENCES──► Control
Evidence ──SUPPORTS──► Relationship
Evidence ──VALIDATES──► Architecture Claim
```

The direction of evidence relationships shall be kept consistent in implementation.

---

# 26. R10 — Measurement / Value Relationships

Controlled relationships:

```text
MEASURES
GENERATES
PROTECTS
CONTRIBUTES_TO
```

Examples:

```text
Measurement ──MEASURES──► Service
Architecture ──CONTRIBUTES_TO──► Value
Control ──PROTECTS──► Value
```

---

# 27. R11 — Dependency Relationships

The primary dependency relationship is:

```text
DEPENDS_ON
```

It may be used between:

```text
Capability
Application
Data
Infrastructure
Network
Service
Control
Organization
Supplier
```

Dependency criticality shall be represented as an attribute rather than creating multiple relationship names for every criticality level.

---

# 28. Relationship Catalogue

| ID | Relationship | Family | Meaning |
|---|---|---|---|
| REL-01 | SUPPORTS | R1/R2/R3/R9 | Provides support |
| REL-02 | DERIVES_FROM | R1/R4 | Originates from |
| REL-03 | ALIGNS_WITH | R1 | Strategic alignment |
| REL-04 | ENABLES | R2/R3/R5 | Makes possible |
| REL-05 | PROVIDES | R2/R6/R7 | Provides service/capability |
| REL-06 | CONSUMES | R2/R6/R7 | Consumes service/resource |
| REL-07 | REALIZES | R2/R3/R6 | Realizes outcome/capability |
| REL-08 | SATISFIES | R4 | Satisfies requirement |
| REL-09 | CONSTRAINS | R4/R5/R8 | Imposes constraint |
| REL-10 | VALIDATES | R4/R8/R9 | Validates claim/decision |
| REL-11 | DEPENDS_ON | R3/R5/R11 | Material dependency |
| REL-12 | AFFECTS | R5/R7 | Has material impact |
| REL-13 | USES | R5/R6 | Uses entity |
| REL-14 | IMPLEMENTS | R6 | Implements architecture |
| REL-15 | INTEGRATES_WITH | R6 | Integration relationship |
| REL-16 | OPERATES | R7 | Operational relationship |
| REL-17 | CHANGES | R7 | Change affects target |
| REL-18 | RECOVERS | R7 | Recovery relationship |
| REL-19 | GOVERNS | R8 | Governance relationship |
| REL-20 | PROTECTS | R8/R10 | Protection relationship |
| REL-21 | OWNS | R8 | Accountability |
| REL-22 | EVIDENCES | R9 | Evidence supports claim |
| REL-23 | MEASURES | R10 | Measurement relationship |
| REL-24 | GENERATES | R10 | Generates value/outcome |
| REL-25 | CONTRIBUTES_TO | R10 | Contributes to value |

---

# 29. Semantic Boundary Rules

The following distinctions are mandatory.

## Capability vs Service

```text
Capability = what the enterprise can do
Service = what is provided to a consumer
```

## Requirement vs Architecture

```text
Requirement = what must be satisfied
Architecture = how the required structure is defined
```

## Architecture vs Implementation

```text
Architecture = intended/approved structure
Implementation = actual realization
```

## Control vs Evidence

```text
Control = mechanism
Evidence = information demonstrating operation/existence/effectiveness
```

## Measurement vs Value

```text
Measurement = observed metric
Value = resulting benefit/outcome
```

---

# 30. Duplicate Concept Prevention

Before adding an entity class, ask:

```text
Does an existing class already represent this concept?
```

If yes:

```text
Reuse existing class.
```

If no:

```text
Demonstrate material need.
Define semantic boundary.
Define owner.
Define lifecycle.
Define relationships.
Seek authorization.
```

---

# 31. Relationship Duplication Prevention

Before adding a relationship type, ask:

```text
Can an existing relationship express the required semantics?
```

If yes:

```text
Reuse existing relationship.
```

If no:

```text
Define semantic difference.
Define direction.
Define valid source classes.
Define valid target classes.
Define evidence requirements.
Seek authorization.
```

---

# 32. Validity Constraints

A relationship is valid only if:

```text
Source Class permits relationship
AND
Target Class permits relationship
AND
Relationship direction is valid
AND
Semantic meaning is unambiguous
```

The catalogue therefore becomes the first validation layer for the traceability repository.

---

# 33. Ownership Constraints

Ownership shall not be inferred merely from relationship existence.

Example:

```text
Application ──IMPLEMENTS──► Architecture
```

does not prove:

```text
Application Owner = Architecture Owner
```

Ownership must be separately represented and evidenced where material.

---

# 34. Evidence Constraints

Evidence may support:

```text
Entity existence
Relationship existence
Ownership
Implementation
Operation
Compliance
Performance
```

but evidence shall not automatically establish all of these simultaneously.

Each claim requires appropriate evidence.

---

# 35. Lifecycle Constraints

A retired entity may remain traceable historically.

An archived relationship may remain queryable.

However:

```text
RETIRED ≠ ACTIVE
ARCHIVED ≠ CURRENT
```

The catalogue shall preserve this distinction.

---

# 36. Canonical Capability Mapping

The eight canonical capabilities are entity instances of:

```text
Entity Class = Capability
```

They are not new entity classes.

Therefore:

```text
CAN-01 → Capability
CAN-02 → Capability
...
CAN-08 → Capability
```

The catalogue governs their semantic representation but does not redefine their scope.

---

# 37. Historical MFM Documents

Historical MFM documents are not automatically entity classes.

Where useful, a document may be represented as:

```text
Evidence
```

or as a controlled architecture artifact through the relevant repository model.

The catalogue must not turn every historical file into a new architectural entity type.

---

# 38. Traceability Repository Readiness

The catalogue provides the semantic prerequisites for a future repository.

A repository should be able to store:

```text
Entity
Relationship
Owner
Evidence
Status
Confidence
Lifecycle
Materiality
Depth
Effective Date
```

N2-B does not specify the technical database implementation.

---

# 39. Pilot Readiness

The catalogue is ready for pilot use when:

```text
Entity classes are understood
Relationship semantics are understood
Allowed source/target combinations can be validated
Evidence can be attached
Ownership can be represented
Status can be assigned
Lifecycle can be assigned
Materiality can be assigned
```

The pilot remains subject to N2 validation.

---

# 40. N2-B Validation

The catalogue shall be tested against the N2-A recommended pilot.

Preferred pilot:

```text
CAN-01 — Enterprise Integration
```

The pilot shall determine whether:

```text
Existing entity classes are sufficient
Existing relationship types are sufficient
New semantic classes are actually required
Any relationship is ambiguous
Any class is redundant
```

---

# 41. N2-B Completion Criteria

N2-B may close when:

```text
Entity catalogue established
AND
Relationship catalogue established
AND
Semantic boundaries established
AND
Duplicate prevention rules established
AND
Validity constraints established
AND
Ownership constraints established
AND
Evidence constraints established
AND
Pilot readiness established
AND
No material semantic ambiguity remains
AND
N2 Workstream Authority approves closure
```

---

# 42. N2-B Closure State

The formal closure state is:

```text
N2-B-SC-90 — ENTITY & RELATIONSHIP CATALOGUE CLOSED
```

Closure means the vocabulary is controlled.

It does not mean that every possible MFM entity has already been mapped.

---

# 43. Change Control

Catalogue changes require:

```text
Change Request
 ↓
Semantic Assessment
 ↓
Existing Concept Review
 ↓
Impact Assessment
 ↓
Architecture Authority
 ↓
Approval
 ↓
Catalogue Version
```

Minor clarifications may be handled as minor version changes.

Material semantic changes require major version control.

---

# 44. Anti-Runaway Control

N2-B shall not create:

```text
N2-B.01
N2-B.02
N2-B.03
...
```

merely to add more terminology.

The catalogue shall remain intentionally compact.

New concepts must demonstrate material semantic value.

---

# 45. Final N2-B.00 Finding

> **N2-B.00 establishes the controlled entity and relationship vocabulary for the MFM Post-Steady-State traceability system. It converts the N2-A meta-model into a stable semantic catalogue while preserving the inherited EA-IMETA concepts and preventing duplicate or unnecessarily granular terminology. The catalogue is intended to provide the semantic foundation for pilot traceability and subsequent repository or matrix implementation.**

---

# 46. Final N2-B Principle

> **A controlled traceability system requires a controlled vocabulary. Every entity and relationship shall have one clear semantic meaning, and new concepts shall be introduced only where an existing concept cannot represent a materially different requirement.**

---

# 47. Final N2-B Anti-Runaway Principle

> **Vocabulary expansion is not progress by itself. The catalogue shall grow only when evidence demonstrates a genuine semantic requirement that cannot be represented by the existing controlled vocabulary.**

---

# 48. Document Control

**Document:** MFM Post-Steady-State Phase Control — N2-B.00 Entity & Relationship Catalogue  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-B.00-Entity-and-Relationship-Catalogue-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-B WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2-A.00 — Traceability Model & Meta-Model  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-B — Entity & Relationship Catalogue  
**Inherited Baseline:** MFM v1.2-Steady-State SC-90 Closure Baseline  
**Canonical Capabilities:** 8  
**Entity Classes:** 44  
**Relationship Classes:** 25  
**Catalogue Status:** ESTABLISHED  
**Pilot:** CAN-01 Enterprise Integration — RECOMMENDED / PENDING VALIDATION  
**N2-B Completion Gate:** REQUIRED  
**Automatic Successor Generation:** PROHIBITED  
**Closure State:** N2-B-SC-90 — ENTITY & RELATIONSHIP CATALOGUE CLOSED

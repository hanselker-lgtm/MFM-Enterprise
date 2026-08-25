# MFM Post-Steady-State Phase Control
## N2.00 — Architecture-to-Implementation Traceability Control & Scope

**Control ID:** MFM-Post-Steady-State-Phase-Control-N2.00-Architecture-to-Implementation-Traceability-Control-and-Scope-001  
**Version:** 1.0  
**Status:** ACTIVE — N2 WORKSTREAM ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N1.00 — Transition, Baseline & Phase Charter  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Workstream State:** N2.00 — SCOPE / CONTROL ESTABLISHMENT

---

# 1. Purpose

N2.00 formally establishes the scope, control model and evidence requirements for the first substantive Post-Steady-State workstream:

```text
N2 — Architecture-to-Implementation Traceability
```

N1.00 explicitly identifies N2 as the first substantive workstream and requires N2 to establish its own scope and evidence requirements before downstream N2 artifacts are generated. fileciteturn46file3

N2.00 therefore does **not** begin by producing a large collection of traceability documents.

Its purpose is first to establish:

```text
Traceability Objective
Traceability Scope
Traceability Model
Traceability Levels
Traceability Entities
Traceability Relationships
Evidence Rules
Ownership
Status Model
Gap Model
Validation Rules
Completion Criteria
Authorization Boundary
```

This is a control document.

---

# 2. Starting Condition

The Post-Steady-State phase begins from the closed MFM v1.2-Steady-State baseline.

N1.00 establishes:

```text
MFM v1.2-Steady-State
        ↓
SC-90 — SERIES CLOSED
        ↓
POST-STEADY-STATE BASELINE
        ↓
N1.00 — PHASE CHARTER
        ↓
N2 — TRACEABILITY
```

The closed Steady-State architecture remains authoritative until changed through controlled governance. fileciteturn46file1

The canonical capability baseline inherited by N2 is:

```text
CAN-01  Enterprise Integration
CAN-02  Enterprise Application
CAN-03  Enterprise Infrastructure
CAN-04  Enterprise Network
CAN-05  Enterprise Cybersecurity
CAN-06  Security Operations
CAN-07  Data Platform & Analytics
CAN-08  Identity & Access Management
```

These capabilities are inherited rather than regenerated. fileciteturn46file5

---

# 3. N2 Objective

The objective of N2 is:

> **To establish a controlled traceability system that connects strategic intent, business purpose, capabilities, requirements, architecture, implementation, operation, controls, evidence and value at the depth required by the MFM programme.**

The objective is therefore not merely to create a matrix.

It is to establish a traceability capability.

---

# 4. Fundamental Traceability Principle

The existing EA-IMETA material establishes:

> **Every material architectural element shall be traceable to its context, purpose, owner, relationships, decisions, implementation and outcome.**

The same material defines traceability as a fundamental architecture capability. fileciteturn46file6

N2 adopts this principle as its governing rule.

---

# 5. Canonical Traceability Chain

The existing EA-IMETA traceability model provides the following canonical chain:

```text
PURPOSE
    ↓
STRATEGY
    ↓
OBJECTIVE
    ↓
OUTCOME
    ↓
CAPABILITY
    ↓
REQUIREMENT
    ↓
ARCHITECTURE
    ↓
IMPLEMENTATION
    ↓
OPERATION
    ↓
MEASUREMENT
    ↓
VALUE
```

This chain is established in the existing EA-IMETA material. fileciteturn46file6

N2 adopts this chain as the **strategic-to-value traceability spine**.

---

# 6. Operational Traceability Chain

For the Post-Steady-State implementation focus, N2 establishes a more operationally explicit chain:

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

This is consistent with the N1.00 traceability requirement. fileciteturn47file0

The two chains are complementary:

```text
STRATEGIC TRACEABILITY

Purpose
  ↓
Strategy
  ↓
Objective
  ↓
Outcome
  ↓
Capability
  ↓
Requirement


IMPLEMENTATION TRACEABILITY

Requirement
  ↓
Architecture
  ↓
Implementation
  ↓
Operation
  ↓
Control
  ↓
Evidence
  ↓
Measurement
  ↓
Value
```

---

# 7. Traceability Is Not Documentation Cross-Referencing

N2 explicitly distinguishes:

```text
DOCUMENT CROSS-REFERENCE
```

from:

```text
ARCHITECTURAL TRACEABILITY
```

A document reference such as:

```text
"See MFM-149"
```

is not sufficient evidence of traceability.

True traceability requires that the relationship between entities is explicitly represented.

For example:

```text
Requirement R-001
    ↓
Capability CAN-04
    ↓
Architecture Element NET-SEG-001
    ↓
Implementation Element FW-SEG-001
    ↓
Service Network Segmentation
    ↓
Control SEC-NET-004
    ↓
Evidence EV-2026-001
```

The example is illustrative and does not assert that these identifiers currently exist.

---

# 8. Traceability Dimensions

The existing EA-IMETA material identifies multiple traceability dimensions:

```text
Strategic Traceability
Business Traceability
Capability Traceability
Requirement Traceability
Architecture Traceability
Technology Traceability
Data Traceability
AI Traceability
Agent Traceability
Security Traceability
Risk Traceability
Investment Traceability
Implementation Traceability
Operational Traceability
Value Traceability
```

fileciteturn46file6

N2 adopts these as the candidate traceability dimensions.

N2.00 does not yet claim that every dimension must be implemented to identical depth.

Depth shall be determined by materiality and phase requirements.

---

# 9. N2 Traceability Layers

N2 establishes nine controlled layers:

```text
L1  Strategic Context
L2  Business / Outcome
L3  Capability
L4  Requirement
L5  Architecture
L6  Implementation
L7  Operation
L8  Control / Evidence
L9  Measurement / Value
```

Each layer shall have:

```text
Identity
Owner
Status
Relationships
Evidence
Lifecycle
```

where materially applicable.

---

# 10. Layer L1 — Strategic Context

L1 connects architecture to:

```text
Enterprise Purpose
Strategic Direction
Strategic Objectives
Strategic Priorities
```

The existing EA-IMETA material states that Strategic Traceability connects architecture to enterprise strategy. fileciteturn46file6

Every material architecture initiative should be able to answer:

```text
Which strategic objective does this support?
```

If no meaningful relationship exists, the initiative should be reassessed.

---

# 11. Layer L2 — Business / Outcome

L2 connects:

```text
Business Objective
    ↓
Capability
    ↓
Value Stream
    ↓
Process
    ↓
Business Service
```

This follows the existing Business Traceability model. fileciteturn46file6

The purpose is to ensure that technology and architecture remain connected to actual enterprise outcomes.

---

# 12. Layer L3 — Capability

Capabilities are the central anchor of the MFM Post-Steady-State model.

The inherited canonical capability set is:

```text
CAN-01 Integration
CAN-02 Application
CAN-03 Infrastructure
CAN-04 Network
CAN-05 Cybersecurity
CAN-06 Security Operations
CAN-07 Data Platform & Analytics
CAN-08 Identity & Access
```

A capability shall be traceable, where materially applicable, to:

```text
Strategy
Objectives
Outcomes
Value Streams
Processes
Organization
Applications
Data
Technology
AI
Agents
Investment
Risk
```

This follows the established EA-IMETA Capability Traceability model. fileciteturn46file6

---

# 13. Layer L4 — Requirement

Requirements shall be traceable from origin through architecture and implementation.

The existing model establishes:

```text
Stakeholder Need
      ↓
Business Requirement
      ↓
Architecture Requirement
      ↓
Solution Requirement
      ↓
Implementation
      ↓
Validation
```

fileciteturn46file6

Important requirements should contain, where applicable:

```text
Requirement ID
Source
Description
Purpose
Priority
Owner
Affected Architecture
Acceptance Criteria
Validation Method
Status
```

fileciteturn46file6

---

# 14. Layer L5 — Architecture

Architecture elements shall be traceable to:

```text
Purpose
Strategy
Requirements
Architecture Principles
Architecture Decisions
Dependencies
Standards
Implementation
Operations
```

This follows the existing Architecture Traceability model. fileciteturn46file6

N2 therefore requires every material architecture element to have sufficient context to answer:

```text
Why does it exist?
What requirement does it address?
Who owns it?
What does it depend on?
What depends on it?
How is it implemented?
How is it operated?
What evidence supports it?
```

---

# 15. Layer L6 — Implementation

Implementation traceability connects architecture to actual realization.

Potential implementation entities include:

```text
Application
Application Component
Data Asset
Data Product
Technology Component
Platform
Infrastructure Component
Network Component
Security Component
Identity Component
Integration
Interface
AI Model
AI Service
Agent
Tool
```

The existing EA-IMETA Meta-Model identifies many of these as canonical architecture classes. fileciteturn47file1

N2 does not assume that every class exists in the current MFM implementation.

It establishes the model that future implementation evidence shall use where applicable.

---

# 16. Layer L7 — Operation

Operational traceability connects implementation to:

```text
Service
Process
Owner
Monitoring
Incident
Problem
Change
Recovery
Improvement
```

N1.00 establishes the intended operational chain:

```text
Architecture
    ↓
Service
    ↓
Process
    ↓
Owner
    ↓
KPI / KRI
    ↓
Monitoring
    ↓
Incident
    ↓
Problem
    ↓
Change
    ↓
Improvement
```

N2 shall provide the upstream traceability required to support this later operational model. fileciteturn46file3

---

# 17. Layer L8 — Control & Evidence

The traceability system must connect architecture and implementation to controls and evidence.

Potential relationships include:

```text
Architecture Element
    ↓
Control
    ↓
Control Owner
    ↓
Control Objective
    ↓
Evidence
    ↓
Validation
```

Evidence must be classified.

Minimum evidence states:

```text
VERIFIED
SUPPORTED
INFERRED
UNVERIFIED
NOT APPLICABLE
```

N2 shall not convert an unverified relationship into a verified relationship without evidence.

---

# 18. Layer L9 — Measurement & Value

The final layer connects operation to:

```text
Measurement
KPI
KRI
Performance
Maturity
Outcome
Value
```

The established EA-IMETA traceability chain explicitly terminates in:

```text
MEASUREMENT
    ↓
VALUE
```

fileciteturn46file6

N2 therefore treats value traceability as part of the model, even though detailed KPI and maturity implementation belongs partly to later workstreams.

---

# 19. Core Traceability Object

N2 establishes the conceptual traceability relationship:

```text
TRACEABILITY RELATIONSHIP

Source Entity
    ↓
Relationship Type
    ↓
Target Entity
    ↓
Relationship Owner
    ↓
Evidence
    ↓
Status
    ↓
Effective Date
    ↓
Lifecycle
```

The relationship itself is an architecture object.

---

# 20. Traceability Relationship Types

Initial relationship types shall include:

```text
SUPPORTS
DERIVES_FROM
SATISFIES
IMPLEMENTS
REALIZES
DEPENDS_ON
ENABLES
CONSTRAINS
GOVERNS
PROTECTS
OPERATES
MEASURES
VALIDATES
EVIDENCES
OWNS
USES
PROVIDES
CONSUMES
AFFECTS
```

These are initial controlled relationship classes.

Additional relationship types require explicit governance.

---

# 21. Traceability Status Model

Each material relationship shall have one of the following states:

```text
T0 — Not Assessed
T1 — Candidate
T2 — Supported
T3 — Verified
T4 — Validated
T5 — Retired
```

Definitions:

```text
T0
No assessment performed.

T1
Relationship proposed but not evidenced.

T2
Relationship supported by available evidence.

T3
Relationship directly verified.

T4
Relationship verified and validated against the relevant owner / acceptance method.

T5
Relationship no longer current but retained for historical traceability.
```

---

# 22. Evidence Confidence

Traceability status and evidence confidence are separate.

Example:

```text
Relationship Status = T3 VERIFIED
Evidence Confidence = HIGH
```

or:

```text
Relationship Status = T2 SUPPORTED
Evidence Confidence = MEDIUM
```

The system must not use one field to represent both concepts.

---

# 23. Ownership Model

Each material traceability relationship should identify:

```text
Source Owner
Target Owner
Relationship Owner
Validation Authority
```

Where these are the same person or organizational function, that fact may be explicitly recorded.

---

# 24. Lifecycle Model

Traceability relationships have lifecycle states:

```text
Proposed
Active
Suspended
Superseded
Retired
Archived
```

Historical relationships shall remain recoverable where required for auditability.

---

# 25. Traceability Completeness

N2 introduces the concept:

```text
TRACEABILITY COMPLETENESS
```

A relationship is complete only when the required fields for its materiality class are present.

For example:

```text
Requirement
    ↓
Capability
```

may require:

```text
Requirement ID
Capability ID
Relationship
Owner
Evidence
Status
```

A relationship missing mandatory fields is incomplete.

---

# 26. Traceability Depth

Not every entity requires the same traceability depth.

N2 establishes:

```text
D1 — Identity Only
D2 — Context
D3 — Relationship
D4 — Ownership
D5 — Evidence
D6 — Implementation
D7 — Operational
D8 — Measurement / Value
```

Materiality determines the minimum required depth.

---

# 27. Materiality Rules

High-materiality elements should normally achieve:

```text
D6 or greater
```

where implementation exists.

Critical operational elements should normally achieve:

```text
D7
```

and where value measurement is required:

```text
D8
```

Low-materiality elements may remain at a lower depth if formally accepted.

This prevents excessive documentation of low-value relationships.

---

# 28. Traceability Gap Types

N2 establishes:

```text
TG-01 Missing Source
TG-02 Missing Target
TG-03 Missing Relationship
TG-04 Missing Owner
TG-05 Missing Evidence
TG-06 Missing Implementation
TG-07 Missing Operational Mapping
TG-08 Missing Measurement
TG-09 Conflicting Relationship
TG-10 Stale Relationship
TG-11 Unverified Relationship
TG-12 Orphaned Element
```

These are traceability gaps.

They are not automatically architecture gaps.

---

# 29. Orphan Detection

N2 shall specifically identify orphaned entities.

Examples:

```text
Requirement with no architecture mapping
Capability with no requirement mapping
Architecture element with no requirement
Implementation component with no architecture
Service with no implementation owner
Control with no governed element
Evidence with no controlled relationship
```

An orphan is a signal for investigation.

It does not automatically justify a new architecture document.

---

# 30. Contradiction Detection

N2 shall also identify contradictory relationships.

Examples:

```text
Two different owners for the same controlled element
Two incompatible implementation mappings
A requirement marked satisfied by conflicting architectures
An element marked active and retired simultaneously
A dependency recorded in one direction only where bidirectional impact exists
```

Contradictions require resolution or explicit acceptance.

---

# 31. Traceability Evidence Sources

Potential evidence sources include:

```text
Architecture Documents
Requirements
Policies
Standards
Architecture Decisions
Design Records
Configuration Records
Application Inventories
Data Catalogues
CMDB / Asset Records
Service Catalogues
Security Controls
Operational Procedures
Monitoring Records
Test Results
Audit Evidence
Change Records
Incident / Problem Records
Performance Records
```

The availability of a source must not be assumed.

N2 shall distinguish:

```text
Available
Unavailable
Not Applicable
Unknown
```

---

# 32. Traceability Authority

N2 is governed by the Post-Steady-State Phase Control.

The architecture baseline remains authoritative.

N2 may identify:

```text
Missing Evidence
Missing Relationships
Contradictions
Implementation Gaps
Operational Gaps
Traceability Gaps
```

N2 may not silently alter the canonical architecture.

Any material architecture change must enter controlled change management.

---

# 33. Relationship to N3

N2 precedes N3.

N2 shall provide the evidence required to determine the actual scope of Implementation Architecture.

Therefore:

```text
N2
    ↓
Traceability Findings
    ↓
Implementation Requirements
    ↓
N3 Scope
```

N3 must not be fully predetermined before N2 findings are known.

N1.00 explicitly states that N3's final scope must be determined from N2 findings. fileciteturn46file3

---

# 34. Relationship to N4

N2 provides upstream traceability for:

```text
Architecture
→ Implementation
→ Service
→ Operation
```

N4 will later establish the operational architecture.

N2 does not replace N4.

---

# 35. Relationship to N6

N2 establishes the traceability control model.

N6 is planned as the Architecture Traceability Matrix workstream.

Therefore:

```text
N2
= Traceability Architecture / Control

N6
= Traceability Matrix / Operationalization
```

N2 should establish the semantics that N6 later implements.

---

# 36. No Automatic N2 Document Chain

N2.00 explicitly prohibits:

```text
N2.00
 ↓
N2.01
 ↓
N2.02
 ↓
N2.03
 ↓
...
```

unless each artifact is independently justified.

A subsequent N2 artifact requires:

```text
Defined requirement
Defined scope
Material value
Defined boundary
Evidence need
Owner
Completion impact
Authorization
```

---

# 37. N2 Work Package Structure

N2 is divided into controlled activities:

```text
N2-A  Traceability Model
N2-B  Entity Catalogue
N2-C  Relationship Catalogue
N2-D  Evidence Model
N2-E  Traceability Status
N2-F  Materiality / Depth Model
N2-G  Gap & Orphan Model
N2-H  Pilot Traceability
N2-I  Validation
N2-J  N2 Completion Assessment
```

These are work packages, not automatic documents.

---

# 38. N2 Pilot Principle

Before large-scale traceability is attempted, N2 shall use a controlled pilot.

The pilot should test:

```text
One or more canonical capabilities
One representative requirement chain
One implementation chain
One operational chain
One control/evidence chain
```

The pilot must validate the model before broad rollout.

---

# 39. Recommended Pilot Boundary

The preferred initial pilot is:

```text
CAN-01 — Enterprise Integration
```

because Integration has established historical architecture material and clear relationships across:

```text
Application
Data
Network
Infrastructure
Identity
Security
Operations
```

This is a recommended pilot, not a final production assignment.

The pilot scope shall be confirmed before execution.

---

# 40. Pilot Traceability Chain

The pilot should attempt:

```text
Purpose
  ↓
Strategic Objective
  ↓
Integration Capability
  ↓
Requirement
  ↓
Integration Architecture
  ↓
Integration Element
  ↓
Implementation
  ↓
Integration Service
  ↓
Control
  ↓
Operational Evidence
  ↓
Measurement
  ↓
Value
```

The objective is to test the complete chain.

---

# 41. Traceability Quality Gates

Each pilot relationship should pass:

```text
QG1 Identity
QG2 Context
QG3 Relationship
QG4 Ownership
QG5 Evidence
QG6 Lifecycle
QG7 Implementation
QG8 Operation
QG9 Measurement
```

Not every relationship must pass every gate if its materiality does not require that depth.

---

# 42. N2 Completion Criteria

N2 may close when:

```text
Traceability model defined
AND
Entity model defined
AND
Relationship model defined
AND
Evidence model defined
AND
Status model defined
AND
Materiality model defined
AND
Gap model defined
AND
Pilot successfully validated
AND
Required ownership established
AND
N6 input requirements defined
AND
No unresolved material traceability control defect remains
AND
N2 Completion Authority approves closure
```

---

# 43. N2 Completion State

The N2 closure state shall be:

```text
N2-SC-90 — TRACEABILITY WORKSTREAM CLOSED
```

After closure:

```text
No automatic N2.01
No automatic N2.02
No automatic N3
```

unless separately authorized by the phase control.

---

# 44. N2 Reopening

N2 may be reopened if:

```text
Major traceability requirement changes
New architecture domain introduced
Major implementation model changes
Major regulatory traceability requirement
Major audit requirement
Material evidence model change
Major EA-IMETA meta-model change
```

Minor traceability changes should be managed through controlled revision.

---

# 45. Initial N2 Deliverables

The first controlled deliverables should be:

```text
D-N2-01 Traceability Model
D-N2-02 Entity / Relationship Catalogue
D-N2-03 Evidence & Status Model
D-N2-04 Materiality / Traceability Depth Model
D-N2-05 Pilot Traceability
D-N2-06 N2 Validation & Completion Assessment
```

These are deliverable classes.

They do not automatically authorize six separate files.

The minimum coherent artifact set should be preferred.

---

# 46. Initial N2 Decision

N2.00 authorizes:

```text
N2 WORKSTREAM
STATUS = ESTABLISHED
```

and authorizes planning of:

```text
N2-A — Traceability Model
```

before any broad implementation traceability rollout.

N2.00 does not authorize automatic production of N2-B through N2-J.

---

# 47. Anti-Runaway Control

The following rule is permanent for N2:

> **N2 may define traceability work, but no N2 artifact may create automatic authority for its own successor. Every additional artifact must pass the N2 authorization test.**

---

# 48. Final N2.00 Finding

> **The N2 Architecture-to-Implementation Traceability workstream is hereby established as a controlled capability within the MFM Post-Steady-State phase. It adopts the existing EA-IMETA traceability chain from Purpose through Strategy, Objective, Outcome, Capability, Requirement, Architecture, Implementation, Operation, Measurement and Value, while adding explicit evidence, ownership, status, materiality and lifecycle controls. N2 shall establish the traceability model before large-scale implementation mapping and shall not become another sequential document-generation chain.**

---

# 49. Final N2.00 Principle

> **Traceability is not the act of linking documents; it is the controlled representation of relationships between architectural entities, their purpose, ownership, implementation, operation, evidence and value.**

---

# 50. Final N2 Anti-Runaway Principle

> **No traceability requirement, gap or relationship shall by itself authorize creation of a new document. The preferred resolution is to improve the traceability model or existing controlled artifact before creating additional documentation.**

---

# 51. Document Control

**Document:** MFM Post-Steady-State Phase Control — N2.00 Architecture-to-Implementation Traceability Control & Scope  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N2.00-Architecture-to-Implementation-Traceability-Control-and-Scope-001  
**Version:** 1.0  
**Status:** ACTIVE — N2 WORKSTREAM ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N1.00 — Transition, Baseline & Phase Charter  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Inherited Baseline:** MFM v1.2-Steady-State SC-90 Closure Baseline  
**Canonical Capabilities:** 8  
**Traceability Spine:** Purpose → Strategy → Objective → Outcome → Capability → Requirement → Architecture → Implementation → Operation → Measurement → Value  
**Implementation Traceability Spine:** Requirement → Capability → Architecture → Implementation → Operation → Control → Evidence  
**N2 Status:** ESTABLISHED  
**Next Controlled Work Package:** N2-A — Traceability Model  
**Automatic Successor Generation:** PROHIBITED  
**N2 Completion Gate:** REQUIRED  
**N2 Closure State:** N2-SC-90 — TRACEABILITY WORKSTREAM CLOSED

# MFM Post-Steady-State Phase Control
## N2-A.00 — Traceability Model & Meta-Model

**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-A.00-Traceability-Model-and-Meta-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-A WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2.00 — Architecture-to-Implementation Traceability Control & Scope  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-A — Traceability Model  
**State:** N2-A.00 — MODEL ESTABLISHMENT

---

# 1. Purpose

N2-A.00 establishes the controlled traceability model required by N2.00.

N2.00 established that the first substantive Post-Steady-State workstream is Architecture-to-Implementation Traceability and that the traceability model must be defined before broad implementation mapping is undertaken.

This document therefore defines the structural model for representing:

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

It does not perform the full MFM traceability mapping.

It establishes the model by which that mapping shall subsequently be performed.

---

# 2. Governing Baseline

The governing baseline remains:

```text
MFM v1.2-Steady-State
        ↓
SC-90 — SERIES CLOSED
        ↓
POST-STEADY-STATE ARCHITECTURAL BASELINE
        ↓
N1.00 — PHASE CHARTER
        ↓
N2.00 — TRACEABILITY CONTROL & SCOPE
        ↓
N2-A.00 — TRACEABILITY MODEL
```

N1.00 establishes that the closed Steady-State architecture remains authoritative and that canonical capabilities are inherited rather than regenerated.

The canonical capability baseline is:

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

---

# 3. Model Objective

The N2-A model shall answer five fundamental questions:

```text
WHAT exists?
WHY does it exist?
HOW is it related?
WHO owns it?
WHAT evidence demonstrates the relationship?
```

For implementation traceability it shall additionally answer:

```text
HOW is it realized?
HOW is it operated?
HOW is it controlled?
HOW is it measured?
WHAT value does it produce?
```

---

# 4. Fundamental Traceability Model

The canonical model is:

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

The implementation-oriented model is:

```text
REQUIREMENT
    ↓
CAPABILITY
    ↓
ARCHITECTURE
    ↓
ARCHITECTURE ELEMENT
    ↓
IMPLEMENTATION ELEMENT
    ↓
SERVICE
    ↓
CONTROL
    ↓
EVIDENCE
```

The two views form one connected traceability system.

---

# 5. Traceability Meta-Model

N2-A establishes the following conceptual classes:

```text
ENTITY
RELATIONSHIP
EVIDENCE
OWNER
DECISION
CONTROL
STATUS
LIFECYCLE
MEASUREMENT
VALUE
```

The central structure is:

```text
ENTITY
   │
   ├── Identity
   ├── Type
   ├── Purpose
   ├── Context
   ├── Owner
   ├── Lifecycle
   ├── Status
   └── Evidence
   │
   └──── RELATIONSHIP ────► ENTITY
                 │
                 ├── Type
                 ├── Owner
                 ├── Evidence
                 ├── Status
                 ├── Confidence
                 └── Lifecycle
```

The relationship itself is therefore a controlled object.

---

# 6. Entity Principle

Every material entity shall have:

```text
Unique Identity
Defined Type
Context
Purpose
Owner
Lifecycle
Status
```

Where materially applicable it shall additionally have:

```text
Relationships
Dependencies
Constraints
Evidence
Risk
Value
```

This preserves the existing EA-IMETA architecture-element principle.

---

# 7. Core Entity Classes

The initial N2-A entity classes are:

```text
Enterprise
Purpose
Stakeholder
Strategy
Objective
Outcome
Capability
Value Stream
Business Service
Process
Organization
Role
Decision
Policy
Requirement
Information
Data Asset
Data Product
Application
Application Service
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
Service
Control
Evidence
Measurement
Value
Risk
Dependency
Standard
```

Not every class is required in every MFM traceability chain.

---

# 8. Entity Identity

Each controlled entity shall have a stable identifier.

Conceptual examples:

```text
CAP-001
REQ-001
ARC-001
IMP-001
SRV-001
CTL-001
EVD-001
```

These examples are illustrative.

N2-A does not assign production identifiers to existing MFM architecture.

Existing authoritative identifiers shall be preserved.

---

# 9. Entity Context and Purpose

Each material entity shall identify:

```text
Context
Purpose
Owner
Lifecycle
Status
```

Context may include:

```text
Enterprise
Domain
Capability
Architecture Layer
Business Area
Service
Technology Domain
Security Domain
Operational Domain
```

Purpose answers:

```text
Why does this entity exist?
```

A purpose statement shall not merely repeat the entity name.

---

# 10. Ownership Model

Each material entity should identify, where applicable:

```text
Accountable Owner
Operational Owner
Architecture Owner
```

Each material relationship should identify:

```text
Relationship Owner
Validation Authority
```

Where one authority performs multiple roles, that shall be explicitly recorded.

---

# 11. Relationship Meta-Model

N2-A defines a relationship as:

```text
SOURCE
    ↓
RELATIONSHIP TYPE
    ↓
TARGET
```

with:

```text
Relationship ID
Owner
Evidence
Status
Confidence
Effective Date
Lifecycle
```

A relationship is not fully controlled merely because source and target are known.

---

# 12. Core Relationship Types

The initial controlled vocabulary is:

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

Additional relationship types require controlled review.

---

# 13. Directionality

Relationships shall be directional unless explicitly defined as symmetric.

For example:

```text
Requirement
    ──SATISFIES──►
Architecture Element
```

is not identical to:

```text
Architecture Element
    ──SATISFIES──►
Requirement
```

The model shall preserve relationship direction.

---

# 14. Evidence Meta-Model

N2-A defines:

```text
EVIDENCE
   │
   ├── Evidence ID
   ├── Evidence Type
   ├── Source
   ├── Owner
   ├── Date
   ├── Validity
   ├── Confidence
   ├── Related Entity
   └── Related Relationship
```

Evidence may be:

```text
Documentary
Technical
Operational
Test-based
Audit-based
Observational
```

Evidence may establish:

```text
Existence
Ownership
Purpose
Implementation
Operation
Compliance
Performance
Outcome
```

---

# 15. Evidence Status

Evidence shall use:

```text
VERIFIED
SUPPORTED
INFERRED
UNVERIFIED
NOT APPLICABLE
```

These states distinguish evidence from the formal status of the relationship.

---

# 16. Traceability Status

Relationship status shall use:

```text
T0 — NOT ASSESSED
T1 — CANDIDATE
T2 — SUPPORTED
T3 — VERIFIED
T4 — VALIDATED
T5 — RETIRED
```

The distinction is:

```text
Evidence Confidence
        ≠
Relationship Status
```

---

# 17. Confidence Model

Evidence confidence shall use:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

Confidence reflects the quality and reliability of the evidence.

It does not replace relationship status.

---

# 18. Lifecycle Model

Entities and relationships shall use:

```text
PROPOSED
ACTIVE
SUSPENDED
SUPERSEDED
RETIRED
ARCHIVED
```

Lifecycle and status are separate dimensions.

Example:

```text
Lifecycle = ACTIVE
Status = T2 SUPPORTED
```

---

# 19. Materiality Model

N2-A establishes four materiality levels:

```text
M1 — LOW
M2 — MODERATE
M3 — HIGH
M4 — CRITICAL
```

Materiality considers:

```text
Business Impact
Security Impact
Operational Impact
Regulatory Impact
Financial Impact
Dependency Impact
Change Impact
Risk
```

The purpose is to prevent excessive traceability overhead for low-value relationships.

---

# 20. Traceability Depth Model

The N2-A depth model is:

```text
D1 — IDENTITY
D2 — CONTEXT
D3 — RELATIONSHIP
D4 — OWNERSHIP
D5 — EVIDENCE
D6 — IMPLEMENTATION
D7 — OPERATION
D8 — MEASUREMENT / VALUE
```

Minimum depth shall be determined from materiality.

---

# 21. Minimum Depth by Materiality

Initial control guidance:

```text
M1 LOW
Minimum D3

M2 MODERATE
Minimum D4

M3 HIGH
Minimum D6

M4 CRITICAL
Minimum D7
and D8 where measurement/value is materially required
```

This is a control baseline and may be refined during the N2 pilot.

---

# 22. Requirement Model

A requirement shall be represented by:

```text
Requirement ID
Source
Description
Purpose
Priority
Owner
Affected Capability
Affected Architecture
Acceptance Criteria
Validation Method
Status
Evidence
```

The requirement chain is:

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

---

# 23. Capability Model

A capability is the principal architectural anchor.

A capability may connect to:

```text
Strategy
Objective
Outcome
Value Stream
Process
Organization
Application
Data
Technology
AI
Agent
Investment
Risk
Requirement
Architecture
Implementation
Operation
Value
```

The eight inherited canonical capabilities remain authoritative.

---

# 24. Architecture Element Model

An architecture element shall include, where applicable:

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

This preserves the existing EA-IMETA meta-model.

---

# 25. Implementation Element Model

Implementation elements may represent:

```text
Application
Application Component
Platform
Technology Component
Infrastructure
Network
Integration
Data Asset
Security Component
Identity Component
AI Model
AI Service
Agent
Tool
```

The implementation model must remain traceable to its originating architecture element.

---

# 26. Service Model

A service provides the bridge between implementation and operation.

A service may be represented through:

```text
Service ID
Service Name
Owner
Consumers
Supporting Capability
Supporting Architecture
Implementation
Process
KPI / KRI
Controls
Evidence
Lifecycle
```

---

# 27. Control Model

A control shall identify:

```text
Control ID
Control Objective
Controlled Entity
Owner
Frequency
Method
Evidence
Status
Exception
Remediation
```

The control model provides the bridge between architecture and assurance.

---

# 28. Measurement and Value Model

Measurement may include:

```text
KPI
KRI
Performance Metric
Availability
Capacity
Quality
Security Metric
Maturity Measure
Outcome Measure
Value Measure
```

Value may include:

```text
Business Value
Operational Value
Financial Value
Risk Reduction
Security Value
Compliance Value
Customer Value
Strategic Value
```

Not every architecture element requires a direct financial value.

---

# 29. Dependency Model

A material dependency shall identify:

```text
Source
Dependency Type
Target
Criticality
Owner
Impact
Evidence
Status
```

Dependencies may exist between:

```text
Capabilities
Applications
Data
Infrastructure
Networks
Services
Controls
Suppliers
Organizations
```

---

# 30. Decision, Policy and Standard Traceability

Architecture decisions shall be traceable through:

```text
Decision
   ↓
Reason
   ↓
Affected Requirement
   ↓
Affected Architecture
   ↓
Affected Implementation
   ↓
Affected Operation
```

Policies and standards may constrain architecture:

```text
Policy / Standard
        ↓
Requirement
        ↓
Architecture
        ↓
Implementation
        ↓
Control
        ↓
Evidence
```

---

# 31. Risk and Security Traceability

Risk shall be traceable through:

```text
Risk
 ↓
Affected Capability
 ↓
Affected Architecture
 ↓
Affected Implementation
 ↓
Control
 ↓
Evidence
 ↓
Residual Risk
```

Security traceability shall support:

```text
Requirement
 ↓
Security Architecture
 ↓
Security Control
 ↓
Implementation
 ↓
Monitoring
 ↓
Evidence
```

---

# 32. Data, AI and Agent Traceability

Data relationships may be represented as:

```text
Business Need
 ↓
Information
 ↓
Data Asset
 ↓
Data Product
 ↓
Application
 ↓
Integration
 ↓
Platform
 ↓
Control
 ↓
Evidence
```

Where AI or agents are materially present:

```text
AI Requirement
 ↓
AI Capability
 ↓
AI Architecture
 ↓
AI Model / Service
 ↓
Agent
 ↓
Tool
 ↓
Operation
 ↓
Control
 ↓
Evidence
```

The model does not assume that AI or agents are present in every capability.

---

# 33. Canonical Traceability Graph

The preferred conceptual representation is:

```text
                 STRATEGY
                    |
                    v
                 OBJECTIVE
                    |
                    v
                  OUTCOME
                    |
                    v
                CAPABILITY
              /     |                   v      v       v
       REQUIREMENT ARCH  RISK
             |       |
             v       v
       IMPLEMENTATION
             |
             v
           SERVICE
             |
             v
          OPERATION
             |
       +-----+-----+
       v           v
    CONTROL     MEASURE
       |           |
       v           v
    EVIDENCE      VALUE
```

This graph is the conceptual basis for future repository, matrix and knowledge-graph implementations.

---

# 34. Traceability Completeness

A relationship is complete when the required fields for its materiality class are present.

Conceptually:

```text
Completeness =
Required Attributes Present
/
Required Attributes Expected
```

The numerical result is not itself the final quality judgement.

A formally required missing field remains material even when overall completeness is high.

---

# 35. Orphan Model

An orphan is an entity that lacks a required relationship.

Examples:

```text
Requirement with no architecture
Capability with no requirement
Architecture with no purpose
Implementation with no architecture
Service with no implementation
Control with no controlled object
Evidence with no relationship
Measurement with no measured object
```

Orphans shall be assessed.

They do not automatically require new documentation.

---

# 36. Contradiction Model

Contradictions include:

```text
Conflicting Owners
Conflicting Status
Conflicting Lifecycle
Conflicting Architecture Mapping
Conflicting Implementation Mapping
Conflicting Dependency Direction
Conflicting Control Assignment
```

Contradictions require:

```text
Resolution
Acceptance
or
Retirement
```

---

# 37. Historical Traceability

Historical relationships shall be preserved where they provide useful evidence.

Historical state may use:

```text
Lifecycle = ARCHIVED
Status = T5 RETIRED
```

Historical uncertainty does not automatically reopen the closed Steady-State baseline.

---

# 38. Existing-First Rule

Before introducing a new entity, relationship or artifact, N2-A shall determine whether an existing controlled object can satisfy the requirement.

Priority:

```text
Existing Entity
        ↓
Existing Relationship
        ↓
Existing Section
        ↓
Existing Document
        ↓
Existing Control
        ↓
New Entity / Relationship
        ↓
New Artifact
```

New documentation is therefore the last, not first, response.

---

# 39. Traceability Evidence Rule

No relationship shall be upgraded from:

```text
T1 CANDIDATE
```

to:

```text
T3 VERIFIED
```

without appropriate evidence.

Likewise:

```text
T3 VERIFIED
```

shall not become:

```text
T4 VALIDATED
```

without the required validation authority.

---

# 40. Model Governance

Changes to the N2-A model require:

```text
Change Request
 ↓
Reason
 ↓
Impact Assessment
 ↓
Owner Review
 ↓
Architecture Authority
 ↓
Approval
 ↓
Version Update
```

The model itself is controlled architecture.

---

# 41. Model Versioning

N2-A model versions use:

```text
Major.Minor
```

Examples:

```text
1.0
1.1
1.2
2.0
```

Minor versions may clarify or extend the model.

Major versions represent material structural change.

---

# 42. N2-A Validation

Before the model is considered complete, it shall be tested against at least:

```text
One capability
One requirement
One architecture element
One implementation element
One service
One control
One evidence relationship
```

The preferred pilot remains:

```text
CAN-01 — Enterprise Integration
```

subject to confirmation under N2.

---

# 43. Validation Questions

The pilot shall answer:

```text
Can the entity be uniquely identified?
Can its purpose be understood?
Can its owner be identified?
Can its relationships be represented?
Can the relationship be evidenced?
Can implementation be traced?
Can operation be traced?
Can controls be traced?
Can evidence be traced?
Can measurement/value be represented where required?
Can gaps and contradictions be detected?
```

---

# 44. N2-A Completion Criteria

N2-A may close when:

```text
Meta-model established
AND
Entity classes established
AND
Relationship classes established
AND
Evidence model established
AND
Status model established
AND
Lifecycle model established
AND
Materiality model established
AND
Depth model established
AND
Orphan model established
AND
Contradiction model established
AND
Pilot requirements defined
AND
Validation criteria established
AND
No material model defect remains
AND
N2 Workstream Authority approves closure
```

---

# 45. N2-A Closure State

The formal closure state shall be:

```text
N2-A-SC-90 — TRACEABILITY MODEL CLOSED
```

Closure does not automatically create another N2 artifact.

The next work package must be separately authorized.

---

# 46. Anti-Runaway Rule

N2-A shall not generate:

```text
N2-A.01
N2-A.02
N2-A.03
...
```

merely because additional model detail could be imagined.

A new model artifact requires demonstrated material need.

The preferred method is controlled revision of N2-A where the existing model can safely accommodate the requirement.

---

# 47. Final N2-A.00 Finding

> **N2-A.00 establishes the controlled traceability meta-model for the MFM Post-Steady-State phase. The model integrates strategic, business, capability, requirement, architecture, implementation, operational, control, evidence, measurement and value traceability into one governed relationship system. It preserves the existing EA-IMETA terminology and structural principles while adding explicit status, confidence, materiality, depth, lifecycle, orphan and contradiction controls required for implementation-oriented traceability.**

---

# 48. Final N2-A Principle

> **A traceability model is complete when it can represent the materially required relationships between architectural entities, their ownership, evidence, implementation, operation and value without requiring uncontrolled document proliferation.**

---

# 49. Final N2-A Anti-Runaway Principle

> **Model completeness shall be determined by required traceability capability, not by the number of model sections, entities or documents produced.**

---

# 50. Document Control

**Document:** MFM Post-Steady-State Phase Control — N2-A.00 Traceability Model & Meta-Model  
**Control ID:** MFM-Post-Steady-State-Phase-Control-N2-A.00-Traceability-Model-and-Meta-Model-001  
**Version:** 1.0  
**Status:** ACTIVE — N2-A WORK PACKAGE ESTABLISHMENT  
**Date:** 18 August 2026  
**Previous Controlled Artifact:** N2.00 — Architecture-to-Implementation Traceability Control & Scope  
**Phase:** MFM Post-Steady-State  
**Workstream:** N2 — Architecture-to-Implementation Traceability  
**Work Package:** N2-A — Traceability Model  
**Inherited Baseline:** MFM v1.2-Steady-State SC-90 Closure Baseline  
**Canonical Capabilities:** 8  
**Model Status:** ESTABLISHED  
**Pilot:** CAN-01 Enterprise Integration — RECOMMENDED / PENDING CONFIRMATION  
**N2-A Completion Gate:** REQUIRED  
**Automatic Successor Generation:** PROHIBITED  
**Closure State:** N2-A-SC-90 — TRACEABILITY MODEL CLOSED

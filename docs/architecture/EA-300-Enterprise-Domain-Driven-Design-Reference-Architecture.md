# EA-300 Enterprise Domain-Driven Design Reference Architecture

| Property | Value |
|----------|-------|
| Document ID | EA-300 |
| Document Type | Enterprise Architecture Reference Standard |
| Title | Enterprise Domain-Driven Design Reference Architecture |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | Entire Enterprise Domain Model |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Domain Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise DDD Reference Architecture aligned with EA-020 and EA-111 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-301 | Enterprise Domain Architecture Standard |
| EA-302 | Enterprise Aggregate Architecture Standard |
| EA-303 | Enterprise Entity Architecture Standard |
| EA-304 | Enterprise Value Object Architecture Standard |
| EA-305 | Enterprise Domain Service Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-307 | Enterprise Specification Architecture Standard |
| EA-308 | Enterprise Factory Architecture Standard |
| EA-309 | Enterprise Domain Event Architecture Standard |

---

# Architecture Compliance

This Reference Architecture defines the common architectural principles governing Domain-Driven Design throughout the MFM Enterprise Platform.

All Domain Architecture standards shall inherit the architectural principles defined in this document.

Common enterprise requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this Reference Architecture is to establish a unified Domain-Driven Design architecture for the MFM Enterprise Platform.

The architecture defines the common principles, responsibilities, dependencies and interaction rules governing all domain components.

It provides a consistent foundation for business modelling, domain behaviour and business rule implementation across the enterprise.

---

# 2. Scope

This Reference Architecture applies to every business domain within the MFM Enterprise Platform.

It governs

- Domains
- Bounded Contexts
- Aggregates
- Entities
- Value Objects
- Domain Services
- Repositories
- Specifications
- Factories
- Domain Events

This Reference Architecture does not define implementation details for individual architectural building blocks.

Those are defined by the corresponding Enterprise Architecture Standards.

---

# 3. Architectural Position

Within the Enterprise Architecture, the Domain Layer represents the authoritative implementation of enterprise business knowledge.

The Domain Layer contains

- business rules
- business behaviour
- business invariants
- domain terminology
- business policies

The Domain Layer shall remain independent of

- Presentation
- Reporting
- Workflow
- Integration
- Infrastructure
- Persistence technologies

---

# 4. Core Principles

The Enterprise Domain Model shall follow the principles of Domain-Driven Design.

Core principles include

- ubiquitous language
- explicit business modelling
- behaviour before data
- encapsulation
- aggregate consistency
- immutable value objects
- persistence ignorance
- separation of concerns
- dependency inversion

Every Domain component shall support these principles.

---

# 5. Enterprise Domain Responsibilities

The Enterprise Domain Layer is responsible for

- implementing business rules
- protecting business invariants
- modelling enterprise concepts
- enforcing aggregate consistency
- expressing business behaviour
- publishing Domain Events
- preserving business integrity

The Domain Layer shall never

- contain user interface logic
- contain infrastructure logic
- execute SQL
- call external systems directly
- depend upon framework-specific behaviour

---

# End of Part 1

---

# 6. Domain-Driven Design Reference Model

The Enterprise Domain Model is composed of cooperating architectural building blocks.

```text
Enterprise Domain
        │
        ▼
Bounded Context
        │
        ▼
Aggregate
        │
 ┌──────┴───────────┐
 ▼                  ▼
Entity        Value Object
 │                  │
 └──────────┬───────┘
            ▼
     Domain Service
            │
     ┌──────┴───────────┐
     ▼                  ▼
 Repository       Specification
            │
            ▼
         Factory
            │
            ▼
       Domain Event
```

Each building block has a single architectural responsibility.

Responsibilities shall not overlap.

---

# 7. Bounded Contexts

Every Enterprise Domain shall be partitioned into one or more Bounded Contexts.

A Bounded Context defines

- a business boundary
- a ubiquitous language
- a consistency boundary
- ownership
- architectural autonomy

Business concepts shall not have conflicting meanings within the same Bounded Context.

Communication between Bounded Contexts shall occur only through approved architectural interfaces.

---

# 8. Layered Domain Architecture

The Enterprise Domain Layer shall be positioned independently from other architectural layers.

```text
Presentation
       │
Application
       │
═══════════════════════
Domain
═══════════════════════
       │
Infrastructure
       │
Persistence
```

The Domain Layer shall never depend upon higher architectural layers.

Dependencies shall always point towards the Domain Layer.

---

# 9. Enterprise Building Blocks

The Domain Layer consists of the following architectural building blocks.

| Building Block | Responsibility |
|----------------|----------------|
| Domain | Business capability |
| Bounded Context | Business boundary |
| Aggregate | Consistency boundary |
| Entity | Business identity |
| Value Object | Immutable business value |
| Domain Service | Business behaviour outside Aggregates |
| Repository | Aggregate persistence abstraction |
| Specification | Business rule evaluation |
| Factory | Aggregate creation |
| Domain Event | Business state change notification |

Each building block shall have exactly one primary responsibility.

---

# 10. Domain Dependencies

The following dependency rules apply throughout the Enterprise Domain.

| Component | May Depend On |
|------------|---------------|
| Aggregate | Entity, Value Object, Domain Event |
| Entity | Value Object |
| Value Object | Nothing |
| Domain Service | Aggregate, Specification |
| Repository | Aggregate |
| Specification | Aggregate, Entity, Value Object |
| Factory | Aggregate, Entity, Value Object |
| Domain Event | Value Object |

Business dependencies shall always remain acyclic.

Circular dependencies are prohibited.

---

# 11. Domain Isolation

The Domain Layer shall remain isolated from technical implementation details.

The Domain Layer shall never directly depend upon

- SQL
- databases
- REST APIs
- messaging infrastructure
- graphical user interfaces
- dependency injection frameworks
- ORM implementations
- cloud SDKs

Technical implementations belong to Infrastructure.

---

# 12. Interaction with Enterprise Architecture

The Domain Layer interacts with the remaining Enterprise Architecture through well-defined architectural boundaries.

| Layer | Interaction |
|--------|-------------|
| Presentation | Invokes Application Layer only |
| Workflow | Coordinates application behaviour |
| Application | Invokes Domain behaviour |
| Domain | Executes business logic |
| Infrastructure | Implements technical services |
| Persistence | Stores Aggregate state |

The Domain Layer shall never directly invoke Presentation, Workflow or Infrastructure components.

---

# End of Part 2

---

# 13. Domain Lifecycle

Every Enterprise Domain shall follow a defined architectural lifecycle.

```text
Business Need
      │
      ▼
Domain Discovery
      │
      ▼
Domain Modelling
      │
      ▼
Architecture Review
      │
      ▼
Implementation
      │
      ▼
Operation
      │
      ▼
Evolution
```

Each lifecycle stage shall produce documented architectural artefacts.

Changes to the Domain Model shall preserve business integrity and maintain backward compatibility where required.

Evolution of the Domain Model shall be governed through Enterprise Architecture governance.

---

# 14. Architectural Constraints

The Enterprise Domain shall comply with the following architectural constraints.

Business behaviour shall reside exclusively within the Domain Layer.

The Domain Layer shall

- enforce business invariants
- protect aggregate consistency
- encapsulate business state
- expose explicit business behaviour
- remain persistence ignorant
- remain framework independent

The Domain Layer shall never

- expose mutable internal state
- depend on infrastructure implementations
- contain presentation concerns
- implement workflow orchestration
- perform technical integration

---

# 15. Dependency Rules

The following dependency rules are mandatory throughout the Enterprise Domain.

Dependencies shall always point toward more stable business concepts.

Allowed dependencies

- Aggregate → Entity
- Aggregate → Value Object
- Aggregate → Domain Event
- Domain Service → Aggregate
- Repository → Aggregate
- Factory → Aggregate
- Specification → Aggregate
- Specification → Entity
- Specification → Value Object

Prohibited dependencies

- Entity → Repository
- Entity → Infrastructure
- Aggregate → SQL
- Aggregate → Presentation
- Aggregate → Workflow
- Aggregate → Messaging Infrastructure
- Value Object → Aggregate
- Domain Event → Repository

Circular dependencies shall never exist.

---

# 16. Enterprise Governance

Enterprise Domain governance shall ensure

- architectural consistency
- ubiquitous language consistency
- bounded context ownership
- aggregate consistency
- business rule ownership
- dependency compliance
- documentation quality
- architectural review

Every Enterprise Domain shall have an assigned business owner and an assigned architectural owner.

Architectural reviews shall be completed before significant structural changes are approved.

---

# 17. Domain Anti-Patterns

The following architectural anti-patterns are prohibited.

## Anemic Domain Model

Business logic shall not be moved into Application Services while Domain objects become passive data structures.

Business behaviour belongs in the Domain Layer.

---

## Transaction Script

Business workflows shall not replace Domain behaviour.

Business processes coordinate work.

The Domain performs the work.

---

## Shared Database as Integration

Bounded Contexts shall never integrate by directly sharing internal database structures.

Integration shall occur through approved architectural interfaces.

---

## Infrastructure Leakage

Infrastructure concerns shall never appear inside Domain objects.

Examples include

- SQL
- ORM annotations that influence business behaviour
- HTTP clients
- file systems
- messaging APIs
- cloud SDKs

---

## God Aggregate

Aggregates shall remain cohesive.

Aggregates shall not accumulate unrelated responsibilities.

Aggregate boundaries shall reflect true business consistency boundaries.

---

# 18. Domain Quality Attributes

The Enterprise Domain shall be designed to achieve

- correctness
- maintainability
- testability
- evolvability
- consistency
- scalability
- readability
- business traceability

Architectural decisions shall prioritize business correctness over technical convenience.

---

# End of Part 3

---

# 19. Architecture Compliance

Enterprise Domain implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- this Enterprise Domain-Driven Design Reference Architecture

All Domain Standards (EA-301 through EA-309) shall inherit the architectural principles defined in this Reference Architecture.

Architecture reviews shall verify

- architectural placement
- dependency compliance
- bounded context integrity
- aggregate consistency
- business rule ownership
- dependency inversion
- documentation completeness
- architectural consistency

---

# 20. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| Bounded Contexts identified | ☐ |
| Aggregate boundaries documented | ☐ |
| Business invariants identified | ☐ |
| Dependency rules verified | ☐ |
| Domain ownership assigned | ☐ |
| Anti-pattern review completed | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Enterprise Domain implementations shall not be approved until all mandatory compliance requirements have been satisfied or an approved architectural exception exists.

---

# 21. Relationship to Domain Standards

This Reference Architecture establishes the common architectural principles inherited by all Domain Architecture Standards.

| Standard | Responsibility |
|----------|----------------|
| EA-301 | Enterprise Domain Architecture |
| EA-302 | Enterprise Aggregate Architecture |
| EA-303 | Enterprise Entity Architecture |
| EA-304 | Enterprise Value Object Architecture |
| EA-305 | Enterprise Domain Service Architecture |
| EA-306 | Enterprise Repository Architecture |
| EA-307 | Enterprise Specification Architecture |
| EA-308 | Enterprise Factory Architecture |
| EA-309 | Enterprise Domain Event Architecture |

Each standard defines one architectural building block in detail while inheriting the principles defined in this document.

---

# 22. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-307 Enterprise Specification Architecture Standard
- EA-308 Enterprise Factory Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard

---

# 23. Reference Architecture Summary

The Enterprise Domain-Driven Design Reference Architecture establishes the common architectural foundation for all Domain-Driven Design components within the MFM Enterprise Platform.

It defines

- common architectural principles
- domain responsibilities
- dependency rules
- bounded context principles
- aggregate consistency rules
- governance model
- architectural constraints
- quality attributes
- compliance requirements

Individual Domain Architecture Standards shall extend this Reference Architecture without redefining its common principles.

---

# 24. Summary

This Reference Architecture defines the authoritative Domain-Driven Design architecture for the MFM Enterprise Platform.

The Domain Layer is the exclusive location for enterprise business knowledge, business behaviour and business rules.

It provides the common architectural foundation for Domains, Aggregates, Entities, Value Objects, Domain Services, Repositories, Specifications, Factories and Domain Events.

Common Enterprise Architecture requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This document shall be regarded as the authoritative Domain-Driven Design Reference Architecture for the MFM Enterprise Platform.

---

# End of Document
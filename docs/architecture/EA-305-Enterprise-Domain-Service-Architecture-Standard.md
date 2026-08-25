# EA-305 Enterprise Domain Service Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-305 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Domain Service Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Domain Services |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Domain Service Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Domain Service Architecture aligned with EA-020, EA-111, EA-300, EA-301, EA-302, EA-303 and EA-304 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-301 | Enterprise Domain Architecture Standard |
| EA-302 | Enterprise Aggregate Architecture Standard |
| EA-303 | Enterprise Entity Architecture Standard |
| EA-304 | Enterprise Value Object Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-309 | Enterprise Domain Event Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Domain Services.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Domain Services shall be designed, implemented and governed within the MFM Enterprise Platform.

A Domain Service encapsulates business behaviour that does not naturally belong within a single Aggregate, Entity or Value Object, while remaining part of the Domain Layer.

---

# 2. Scope

This standard applies to every Domain Service within every Enterprise Domain.

It governs

- Domain Service responsibilities
- Domain Service boundaries
- Aggregate collaboration
- business operations
- dependencies
- lifecycle
- governance
- evolution

Application Services and Infrastructure Services are outside the scope of this standard.

---

# 3. Definition of a Domain Service

A Domain Service represents business behaviour that cannot be naturally assigned to an Aggregate, Entity or Value Object.

A Domain Service shall

- represent a business capability
- encapsulate business rules
- remain technology independent
- belong to one Enterprise Domain
- expose meaningful business operations

A Domain Service shall never become a container for unrelated business logic.

---

# 4. Domain Service Objectives

Every Domain Service shall

- encapsulate shared business behaviour
- support Aggregate collaboration
- preserve Domain purity
- minimise duplication
- remain cohesive
- expose meaningful business operations

Business behaviour shall remain within the Domain Layer.

---

# 5. Domain Service Responsibilities

A Domain Service is responsible for

- business calculations
- business decisions
- coordination between Aggregates within the same Domain
- business policies
- business algorithms

A Domain Service shall never

- contain presentation logic
- implement infrastructure behaviour
- orchestrate application workflows
- access user interfaces

---

# End of Part 1

---

# 6. Stateless Design

Enterprise Domain Services shall be stateless.

A Domain Service shall not maintain mutable business state between invocations.

Business state belongs exclusively within

- Aggregates
- Entities
- Value Objects

A Domain Service shall derive all required information from its input parameters and collaborating Domain objects.

Stateless design improves

- predictability
- testability
- scalability
- maintainability

---

# 7. Aggregate Collaboration

A Domain Service may coordinate business behaviour involving multiple Aggregates within the same Enterprise Domain.

Aggregate collaboration shall

- preserve Aggregate autonomy
- preserve Aggregate consistency
- avoid direct Aggregate coupling
- execute meaningful business operations

A Domain Service shall never bypass Aggregate business rules.

Each Aggregate shall remain responsible for protecting its own invariants.

---

# 8. Dependencies

Domain Services shall depend only upon Domain abstractions.

Permitted dependencies include

- Aggregates
- Entities
- Value Objects
- Specifications
- Domain Events
- Repository interfaces

Prohibited dependencies include

- SQL
- ORM frameworks
- HTTP clients
- GUI components
- Infrastructure implementations
- Messaging infrastructure

Dependencies shall always point toward Domain abstractions.

---

# 9. Domain Purity

Domain Services shall remain pure business components.

A Domain Service shall

- express business terminology
- implement business policies
- execute business algorithms
- preserve business meaning

Technical implementation details shall remain outside the Domain Layer.

The Domain Layer shall remain independent of frameworks and infrastructure technologies.

---

# 10. Business Operations

Domain Services expose business operations that cannot naturally be assigned to a single Aggregate.

Business operations shall

- represent meaningful business actions
- enforce business rules
- preserve Domain consistency
- return meaningful business results

Operations shall avoid technical terminology.

Operation names shall reflect the ubiquitous language of the Domain.

---

# 11. Domain Services versus Application Services

Domain Services and Application Services have different responsibilities.

| Domain Service | Application Service |
|----------------|---------------------|
| Executes business behaviour | Orchestrates use cases |
| Uses ubiquitous language | Coordinates application flow |
| Contains business rules | Contains no business rules |
| Belongs to the Domain Layer | Belongs to the Application Layer |
| Technology independent | Coordinates infrastructure interaction |

Application Services coordinate work.

Domain Services perform business work.

---

# 12. Business Algorithms

Business algorithms that cannot naturally belong to an Aggregate, Entity or Value Object shall be implemented as Domain Services.

Examples include

- complex business calculations
- pricing policies
- allocation algorithms
- scheduling algorithms
- optimisation rules
- eligibility evaluation

Algorithms shall remain deterministic whenever business requirements permit.

Business algorithms shall remain independent of technical implementation details.

---

# End of Part 2

---

# 13. Domain Service Lifecycle

Every Domain Service shall follow a controlled architectural lifecycle.

```text
Business Requirement
         │
         ▼
Service Design
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
Continuous Evolution
```

Domain Services shall evolve together with the Enterprise Domain they belong to.

Changes shall preserve business semantics and remain compatible with the ubiquitous language.

Major structural changes shall undergo Enterprise Architecture review.

---

# 14. Business Rule Enforcement

Domain Services shall enforce only those business rules that cannot naturally be assigned to a single Aggregate, Entity or Value Object.

Business rule enforcement shall

- preserve Domain consistency
- respect Aggregate boundaries
- support business decision making
- remain deterministic whenever possible

Rules belonging to a specific Aggregate shall remain inside that Aggregate.

Domain Services shall never bypass Aggregate validation.

---

# 15. Architectural Constraints

Enterprise Domain Services shall comply with the following architectural constraints.

Domain Services shall

- remain stateless
- remain technology independent
- belong to exactly one Enterprise Domain
- expose meaningful business operations
- use ubiquitous language
- preserve Domain purity

Domain Services shall never

- own business state
- replace Aggregate behaviour
- contain presentation logic
- implement infrastructure concerns
- orchestrate application workflows
- expose technical implementation details

These constraints preserve clear separation of responsibilities throughout the Domain Layer.

---

# 16. Domain Service Quality Attributes

Enterprise Domain Services shall be designed to achieve

- correctness
- cohesion
- readability
- maintainability
- reusability
- testability
- determinism
- business traceability

Business correctness shall always take precedence over implementation convenience.

Domain Services shall remain focused on one cohesive business responsibility.

---

# 17. Domain Service Anti-Patterns

The following architectural anti-patterns are prohibited.

## God Service

A Domain Service shall not accumulate unrelated business responsibilities.

Business behaviour shall remain cohesive and aligned with one business capability.

---

## Application Logic in Domain Services

Domain Services shall not orchestrate application workflows, user interactions or infrastructure operations.

These responsibilities belong to the Application Layer.

---

## Infrastructure Leakage

Domain Services shall never contain

- SQL
- ORM-specific behaviour
- HTTP clients
- messaging APIs
- dependency injection
- file system access
- framework-specific logic

Infrastructure responsibilities belong exclusively to the Infrastructure Layer.

---

## Stateful Domain Service

Domain Services shall never maintain mutable internal state between invocations.

Business state belongs exclusively within Aggregates, Entities and Value Objects.

---

## Duplicate Business Logic

Business rules shall not be duplicated across multiple Domain Services.

Shared business behaviour shall have a single authoritative implementation.

---

# 18. Service Evolution

Enterprise Domain Services shall evolve together with the business domain.

Evolution shall

- preserve business meaning
- maintain compatibility with the ubiquitous language
- minimise breaking changes
- improve business expressiveness

Architectural reviews shall ensure that Domain Services continue to represent genuine business capabilities rather than becoming technical utility classes.

---

# End of Part 3

---

# 19. Implementation Guidelines

Enterprise Domain Services shall be implemented according to the architectural principles defined in EA-300, EA-301, EA-302, EA-303 and EA-304.

Implementation shall ensure

- stateless behaviour
- technology independence
- business cohesion
- deterministic business operations
- clear Aggregate collaboration
- separation of responsibilities
- Domain purity

Domain Services shall expose meaningful business operations using the ubiquitous language of the Domain.

Implementation details shall never influence business behaviour.

---

# 20. Architecture Compliance

Enterprise Domain Service implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- this Enterprise Domain Service Architecture Standard

Architecture reviews shall verify

- stateless implementation
- business cohesion
- Aggregate collaboration
- dependency compliance
- Domain purity
- technology independence
- documentation completeness

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 21. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-300 compliance verified | ☐ |
| EA-301 compliance verified | ☐ |
| EA-302 compliance verified | ☐ |
| EA-303 compliance verified | ☐ |
| EA-304 compliance verified | ☐ |
| Stateless implementation verified | ☐ |
| Domain purity verified | ☐ |
| Business cohesion verified | ☐ |
| No infrastructure dependencies | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Domain Service shall satisfy all mandatory compliance requirements before being released into production.

---

# 22. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard

---

# 23. Summary

This standard defines how Enterprise Domain Services shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Domain Services encapsulate business behaviour that cannot naturally be assigned to an Aggregate, Entity or Value Object while preserving the integrity of the Domain Layer.

This standard establishes

- stateless design
- business cohesion
- Aggregate collaboration
- business algorithms
- dependency rules
- Domain purity
- architectural constraints
- implementation guidance
- compliance requirements

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Entity responsibilities are inherited from EA-303.

Value Object principles are inherited from EA-304.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This standard shall be regarded as the authoritative Enterprise Domain Service Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
# EA-308 Enterprise Factory Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-308 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Factory Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Factories |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Factory Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Factory Architecture aligned with EA-020, EA-111, EA-300, EA-301, EA-302, EA-303, EA-304, EA-305, EA-306 and EA-307 | Chief Enterprise Architect |

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
| EA-305 | Enterprise Domain Service Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-307 | Enterprise Specification Architecture Standard |
| EA-309 | Enterprise Domain Event Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Factories.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Factories shall be designed, implemented and governed within the MFM Enterprise Platform.

Factories provide the authorised mechanism for creating complex Domain objects while ensuring that business invariants are satisfied from the moment an object is created.

Factories shall encapsulate construction complexity without exposing implementation details.

---

# 2. Scope

This standard applies to every Factory within every Enterprise Domain.

It governs

- object creation
- Aggregate creation
- Entity creation
- Value Object creation
- construction logic
- dependency rules
- lifecycle
- governance

Object persistence and infrastructure-specific instantiation mechanisms are outside the scope of this standard.

---

# 3. Definition of a Factory

A Factory is responsible for creating fully valid Domain objects.

A Factory shall

- encapsulate complex construction
- enforce business invariants during creation
- return valid Domain objects
- remain technology independent
- expose meaningful creation operations

Factories shall hide construction complexity from client code.

---

# 4. Factory Objectives

Every Factory shall

- simplify object creation
- preserve Domain consistency
- enforce business invariants
- minimise construction duplication
- improve readability
- support maintainability

Factories exist to create valid Domain objects—not to implement business behaviour.

---

# 5. Factory Responsibilities

Factories are responsible for

- constructing Aggregate Roots
- constructing complex Entities
- constructing complex Value Objects
- coordinating construction dependencies
- ensuring valid initial state

Factories shall never

- persist Domain objects
- execute business workflows
- contain presentation logic
- implement infrastructure concerns

Business behaviour remains the responsibility of Aggregates and Domain Services.

---

# End of Part 1

---

# 6. Aggregate Creation

Factories shall create Aggregate Roots in a fully valid initial state.

Aggregate creation shall

- satisfy all Aggregate invariants
- initialise mandatory business data
- establish required Value Objects
- create required internal Entities
- produce a complete Aggregate Root

An Aggregate shall never exist in a partially constructed state.

---

# 7. Construction Rules

Factory construction logic shall

- encapsulate complex object creation
- validate mandatory construction parameters
- enforce business constraints
- prevent invalid object creation
- minimise construction duplication

Construction shall always result in either

- a fully valid Domain object, or
- a construction failure.

Factories shall never create partially valid objects.

---

# 8. Invariant Enforcement

Factories are responsible for enforcing all invariants required at object creation.

Construction shall verify

- mandatory business values
- required relationships
- business constraints
- identifier validity
- initial consistency

After creation, responsibility for maintaining invariants transfers to the Aggregate Root.

---

# 9. Factory Interfaces

Every Factory shall expose a Domain-defined interface.

Factory interfaces shall

- use business terminology
- expose meaningful creation operations
- remain technology independent
- avoid implementation details

Factory method names shall reflect the ubiquitous language of the Domain.

Examples include

- CreateMember()
- RegisterVessel()
- CreateVoyage()
- CreateMaintenancePlan()

Generic method names such as

- Build()
- Make()
- NewObject()

should be avoided unless they accurately express the business concept.

---

# 10. Dependency Rules

Factories may depend upon

- Aggregates
- Entities
- Value Objects
- Specifications
- Domain Services
- Domain identifiers

Factories shall never depend upon

- SQL
- ORM frameworks
- messaging infrastructure
- presentation components
- external APIs
- infrastructure libraries

Construction shall remain entirely within the Domain Layer.

---

# 11. Factory Collaboration

Factories may collaborate with

- Specifications
- Domain Services
- other Factories
- Value Objects

Factories shall never collaborate directly with

- Repositories
- user interfaces
- application workflows
- infrastructure services

Object creation shall remain independent of persistence and presentation concerns.

---

# 12. Construction Complexity

Factories should be introduced when object creation becomes sufficiently complex that constructors alone no longer express the business intent clearly.

Indicators include

- multiple mandatory Value Objects
- complex validation logic
- multiple dependent Entities
- conditional construction rules
- complex business invariants

Simple Domain objects may be created directly without introducing unnecessary Factory abstractions.

---

# End of Part 2

---

# 13. Factory Lifecycle

Every Factory shall follow a controlled architectural lifecycle.

```text
Business Requirement
         │
         ▼
Factory Design
         │
         ▼
Architecture Review
         │
         ▼
Object Construction
         │
         ▼
Business Validation
         │
         ▼
Return Valid Domain Object
```

Factories shall evolve together with the Enterprise Domain.

Construction behaviour shall preserve business meaning while adapting to changing business requirements.

---

# 14. Creation Strategies

Factories shall select construction strategies that best preserve Domain integrity.

Supported strategies include

- direct Aggregate creation
- staged construction
- composition of Value Objects
- delegation to subordinate Factories
- collaboration with Domain Services

The chosen strategy shall maximise readability while preserving business correctness.

Construction strategies shall remain invisible to client code.

---

# 15. Architectural Constraints

Enterprise Factories shall comply with the following architectural constraints.

Factories shall

- create fully valid Domain objects
- remain technology independent
- preserve Domain purity
- encapsulate construction complexity
- expose business-oriented creation operations

Factories shall never

- persist Domain objects
- modify existing Aggregates
- execute business workflows
- contain presentation logic
- expose infrastructure dependencies

These constraints preserve clear separation between object construction and object behaviour.

---

# 16. Factory Quality Attributes

Enterprise Factories shall be designed to achieve

- correctness
- consistency
- readability
- maintainability
- reusability
- testability
- business traceability
- simplicity

Construction logic shall always favour business clarity over technical optimisation.

Factories shall remain focused on one cohesive construction responsibility.

---

# 17. Factory Anti-Patterns

The following architectural anti-patterns are prohibited.

## God Factory

A Factory shall never become responsible for constructing unrelated Domain objects.

Each Factory shall support one cohesive business capability.

---

## Partial Construction

Factories shall never return partially initialised Domain objects.

Object creation shall either

- succeed completely, or
- fail completely.

---

## Infrastructure Leakage

Factories shall never contain

- SQL
- ORM-specific APIs
- HTTP clients
- messaging APIs
- dependency injection
- file system access
- framework-specific logic

Infrastructure concerns belong exclusively to the Infrastructure Layer.

---

## Business Workflow Factory

Factories shall never orchestrate business processes.

Their responsibility ends when a valid Domain object has been created.

Subsequent business behaviour belongs to Aggregates and Domain Services.

---

## Duplicate Construction Logic

Construction logic shall not be duplicated across multiple Factories.

Reusable construction behaviour shall have one authoritative implementation whenever practical.

---

# 18. Factory Evolution

Enterprise Factories shall evolve together with the Enterprise Domain.

Evolution shall

- preserve business semantics
- minimise breaking interface changes
- improve construction clarity
- support evolving business requirements

Architecture reviews shall ensure that Factories continue to encapsulate construction complexity rather than accumulating unrelated responsibilities.

---

# End of Part 3

---

# 19. Implementation Guidelines

Enterprise Factory implementations shall be developed according to the architectural principles defined in EA-300, EA-301, EA-302, EA-303, EA-304, EA-305, EA-306 and EA-307.

Implementation shall ensure

- complete object construction
- business invariant enforcement
- technology independence
- cohesive construction logic
- clear Factory interfaces
- Domain purity
- maintainable implementation

Factories shall expose business-oriented creation methods that reflect the ubiquitous language of the Domain.

Construction details shall remain hidden from client code.

---

# 20. Architecture Compliance

Enterprise Factory implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-307 Enterprise Specification Architecture Standard
- this Enterprise Factory Architecture Standard

Architecture reviews shall verify

- invariant enforcement
- construction correctness
- dependency compliance
- Domain purity
- technology independence
- Factory cohesion
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
| EA-305 compliance verified | ☐ |
| EA-306 compliance verified | ☐ |
| EA-307 compliance verified | ☐ |
| Invariants enforced during construction | ☐ |
| No partial object creation | ☐ |
| Technology-independent implementation | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Factory shall satisfy all mandatory compliance requirements before being released into production.

---

# 22. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-307 Enterprise Specification Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard

---

# 23. Summary

This standard defines how Enterprise Factories shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Factories encapsulate the creation of complex Domain objects while ensuring that business invariants are satisfied from the moment an object is created.

This standard establishes

- object creation responsibilities
- Aggregate construction
- Entity construction
- Value Object construction
- invariant enforcement
- construction strategies
- dependency rules
- architectural constraints
- implementation guidance
- governance requirements
- compliance requirements

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Entity responsibilities are inherited from EA-303.

Value Object principles are inherited from EA-304.

Domain Service responsibilities are inherited from EA-305.

Repository responsibilities are inherited from EA-306.

Specification responsibilities are inherited from EA-307.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This standard shall be regarded as the authoritative Enterprise Factory Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
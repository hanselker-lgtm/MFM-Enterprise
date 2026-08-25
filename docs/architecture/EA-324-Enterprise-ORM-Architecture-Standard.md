# EA-324 Enterprise ORM Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-324 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise ORM Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | Entire MFM Enterprise Platform |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy ORM Guidance | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise ORM Architecture aligned with EA-020, EA-111, EA-112, EA-300, EA-310, EA-320, EA-321, EA-322 and EA-323 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-302 | Enterprise Aggregate Architecture Standard |
| EA-303 | Enterprise Entity Architecture Standard |
| EA-304 | Enterprise Value Object Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-320 | Enterprise Infrastructure Layer Reference Architecture |
| EA-321 | Enterprise Persistence Architecture Standard |
| EA-323 | Enterprise Database Architecture Standard |

---

# Architecture Compliance

This standard defines the Enterprise ORM Architecture.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Domain-Driven Design principles are inherited from EA-300.

Infrastructure Layer principles are inherited from EA-320.

Persistence Architecture principles are inherited from EA-321.

Database Architecture principles are inherited from EA-323.

All Enterprise ORM implementations shall conform to this standard.

---

# 1. Purpose

The purpose of this standard is to define how Object-Relational Mapping shall be implemented throughout the MFM Enterprise Platform.

The ORM Architecture shall

- isolate persistence technology
- preserve Domain integrity
- simplify persistence implementation
- support maintainability
- support technology independence
- enable efficient object persistence
- minimise infrastructure coupling

ORM implementations shall remain Infrastructure Layer components.

---

# 2. Scope

This standard applies to every ORM implementation throughout the Enterprise Platform.

It governs

- object mapping
- Aggregate mapping
- Entity mapping
- Value Object mapping
- relationship mapping
- inheritance mapping
- change tracking
- loading strategies
- persistence integration

The standard applies regardless of ORM framework.

---

# 3. ORM Definition

Object-Relational Mapping (ORM) is the technical mechanism that maps Domain objects to persistent storage structures.

ORM responsibilities include

- object persistence
- object retrieval
- object mapping
- relationship mapping
- change tracking
- persistence synchronization

ORM implementations shall never contain Enterprise business behaviour.

---

# 4. ORM Objectives

Enterprise ORM Architecture shall

- preserve Domain Models
- isolate persistence technology
- simplify Repository implementations
- support efficient persistence
- support maintainability
- support scalability
- remain replaceable

ORM behaviour shall remain transparent to the Domain Layer.

---

# 5. ORM Responsibilities

The ORM Architecture is responsible for

- object mapping
- relationship mapping
- persistence synchronization
- identity tracking
- change tracking
- loading strategies
- persistence integration

The ORM Architecture shall never

- implement business rules
- enforce business policies
- perform Domain decision making
- expose ORM technology to higher architectural layers

Business behaviour remains exclusively within the Domain Layer.

---

# End of Part 1

---

# 6. ORM Architecture

The Enterprise ORM Architecture provides the technical bridge between the Domain Model and persistent storage.

The ORM Architecture consists of

- object mappings
- persistence mappings
- identity management
- relationship mappings
- inheritance mappings
- loading strategies
- change tracking
- persistence synchronization

The ORM shall remain entirely within the Infrastructure Layer.

Domain objects shall remain unaware of ORM implementation details.

---

# 7. Aggregate Mapping

Aggregates shall be persisted as complete consistency boundaries.

Aggregate mapping shall

- preserve Aggregate integrity
- maintain transactional consistency
- support Repository operations
- respect Aggregate Root ownership
- prevent external persistence of internal Aggregate members

Only Aggregate Roots shall be directly loaded or persisted through Repositories.

Internal Aggregate objects shall be managed exclusively through Aggregate mappings.

---

# 8. Entity Mapping

Entities shall be mapped according to their identity.

Entity mappings shall

- preserve Entity identity
- maintain object lifecycle
- support persistence transparency
- map technical identifiers appropriately
- preserve Domain behaviour

Entity mappings shall never introduce business behaviour.

Persistence identifiers shall remain technical concerns.

---

# 9. Value Object Mapping

Value Objects shall be mapped according to their immutable nature.

Value Object mappings shall

- preserve immutability
- avoid independent identity
- support embedded persistence where appropriate
- maintain value semantics
- simplify persistence representation

Value Objects shall never be persisted independently unless explicitly required by architectural constraints.

---

# 10. Relationship Mapping

Relationships between Domain objects shall reflect Aggregate boundaries.

Relationship mappings shall

- preserve ownership
- maintain consistency
- minimise unnecessary coupling
- avoid circular dependencies
- support efficient persistence

Relationships crossing Aggregate boundaries shall reference Aggregate Roots rather than internal objects.

Relationship mappings shall remain aligned with Domain-Driven Design principles.

---

# 11. Inheritance Mapping

Inheritance shall be used only when it accurately represents Domain concepts.

Supported inheritance strategies may include

- Table per Hierarchy (TPH)
- Table per Type (TPT)
- Table per Concrete Type (TPC)

Selection of inheritance strategy shall consider

- performance
- maintainability
- scalability
- storage efficiency
- simplicity

Inheritance shall never be introduced solely to satisfy ORM limitations.

---

# 12. Change Tracking

ORM implementations shall track changes to persisted objects efficiently.

Change tracking shall

- detect modifications
- identify inserts
- identify updates
- identify deletions
- minimise unnecessary database operations

Automatic change tracking should be preferred where practical.

Manual tracking shall be limited to exceptional scenarios requiring explicit optimisation.

---

# 13. Dependency Rules

The ORM Architecture shall comply with Enterprise dependency inversion principles.

ORM implementations may depend upon

- database providers
- persistence frameworks
- Infrastructure services
- mapping libraries

Higher architectural layers shall never depend directly upon

- ORM-specific APIs
- ORM configuration classes
- provider-specific features
- persistence implementation details

All dependencies shall flow toward abstractions defined by the Domain and Application Layers.

---

# End of Part 2

---

# 14. ORM Lifecycle

Every ORM-managed object shall follow a well-defined lifecycle.

```text
Object Created
        │
        ▼
Transient
        │
        ▼
Attached
        │
        ▼
Tracked
        │
        ▼
Persisted
        │
        ▼
Detached
        │
        ▼
Archived or Removed
```

The ORM lifecycle shall

- preserve object identity
- support transactional consistency
- ensure predictable persistence behaviour
- minimise unnecessary database interaction
- maintain Domain integrity

Lifecycle transitions shall remain under Repository and Unit of Work control.

---

# 15. Loading Strategies

ORM implementations shall support appropriate loading strategies based on application requirements.

Supported loading strategies include

- Lazy Loading
- Eager Loading
- Explicit Loading

Selection of loading strategy shall consider

- performance
- memory consumption
- query complexity
- Aggregate consistency
- expected usage patterns

Loading strategies shall remain transparent to the Domain Layer.

---

## Lazy Loading

Lazy Loading postpones retrieval of related data until it is required.

Lazy Loading may improve performance for large object graphs but shall be used cautiously to avoid excessive database round trips.

Lazy Loading shall never introduce unpredictable application behaviour.

---

## Eager Loading

Eager Loading retrieves all required related objects as part of the initial query.

Eager Loading shall be preferred when

- Aggregate consistency requires complete object graphs
- related data is always required
- database round trips should be minimised

---

## Explicit Loading

Explicit Loading retrieves related data through clearly defined Repository operations.

Explicit Loading shall be preferred whenever application behaviour requires precise control over persistence operations.

---

# 16. Performance Optimisation

ORM implementations shall support efficient persistence operations.

Performance optimisation may include

- batching database operations
- compiled queries
- efficient mapping configurations
- projection queries
- selective loading
- connection pooling
- query optimisation
- cache utilisation where appropriate

Performance optimisation shall never compromise

- Domain integrity
- transactional consistency
- data correctness
- architectural compliance

---

# 17. Concurrency

ORM implementations shall support reliable concurrent data access.

Concurrency mechanisms may include

- optimistic concurrency
- pessimistic concurrency where justified
- version columns
- row versioning
- conflict detection

Concurrency conflicts shall

- be detected
- be reported
- be resolved according to Enterprise application policies

The ORM shall not silently overwrite concurrent changes.

---

# 18. Error Handling

ORM failures shall be handled consistently throughout the Enterprise Platform.

Error handling shall distinguish between

- mapping errors
- validation failures
- database connectivity failures
- concurrency conflicts
- transaction failures
- configuration errors

Technical exceptions shall remain Infrastructure concerns.

Business exceptions shall remain Domain concerns.

ORM implementations shall provide sufficient diagnostic information for operational support while avoiding exposure of sensitive implementation details.

---

# 19. Security

ORM implementations shall comply with Enterprise security requirements.

Security responsibilities include

- secure database communication
- parameterised queries
- prevention of injection attacks
- secure credential handling
- encryption support
- audit integration

ORM implementations shall never

- construct SQL through string concatenation
- expose credentials
- bypass Enterprise authorization
- weaken Infrastructure security controls

Security shall remain consistent across all supported ORM technologies.

---

# 20. ORM Anti-Patterns

The following architectural anti-patterns are prohibited.

## Business Logic in ORM Classes

ORM configuration shall never contain Domain behaviour or business rules.

---

## Domain Objects Depending on ORM Frameworks

Domain Models shall never inherit from, reference or depend upon ORM-specific base classes or APIs.

---

## Leaking ORM Types

ORM-specific objects shall never be exposed beyond the Infrastructure Layer.

Repositories shall return Domain objects only.

---

## Excessive Lazy Loading

Uncontrolled Lazy Loading resulting in excessive database queries (N+1 query problems) shall be avoided.

Loading behaviour shall be explicitly designed and reviewed.

---

## Persistence-Driven Domain Design

The Domain Model shall never be modified solely to accommodate ORM limitations.

The persistence technology shall adapt to the Domain Model—not the reverse.

---

## Overly Complex Mapping Configurations

Mapping configurations shall remain simple, maintainable and aligned with Enterprise architectural principles.

---

# End of Part 3

---

# 21. Implementation Guidelines

Enterprise ORM implementations shall follow the architectural principles defined in EA-020, EA-111, EA-112, EA-300, EA-302, EA-303, EA-304, EA-306, EA-320, EA-321 and EA-323.

Implementation shall ensure

- transparent persistence
- Domain independence
- Aggregate consistency
- maintainable mapping configurations
- efficient object tracking
- controlled loading strategies
- secure persistence operations
- reliable transaction participation
- technology independence
- operational observability

ORM implementations shall remain replaceable without requiring modifications to the Domain Layer.

Persistence technology shall never dictate Domain Model design.

---

# 22. Architecture Compliance

Enterprise ORM implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-321 Enterprise Persistence Architecture Standard
- EA-323 Enterprise Database Architecture Standard
- this Enterprise ORM Architecture Standard

Architecture reviews shall verify

- Aggregate mappings
- Entity mappings
- Value Object mappings
- relationship mappings
- inheritance mappings
- loading strategies
- change tracking
- performance optimisation
- security compliance
- dependency inversion
- documentation completeness

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 23. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-300 compliance verified | ☐ |
| EA-302 compliance verified | ☐ |
| EA-303 compliance verified | ☐ |
| EA-304 compliance verified | ☐ |
| EA-306 compliance verified | ☐ |
| EA-320 compliance verified | ☐ |
| EA-321 compliance verified | ☐ |
| EA-323 compliance verified | ☐ |
| Mapping strategy verified | ☐ |
| Loading strategy verified | ☐ |
| Change tracking verified | ☐ |
| Performance verified | ☐ |
| Security compliance verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise ORM implementation shall satisfy all mandatory compliance requirements before being released into production.

---

# 24. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-321 Enterprise Persistence Architecture Standard
- EA-323 Enterprise Database Architecture Standard
- EA-325 Enterprise File Storage Architecture Standard

---

# 25. Summary

This standard defines the Enterprise ORM Architecture for the MFM Enterprise Platform.

The ORM Architecture provides the technical bridge between the Domain Layer and persistent storage while preserving Domain integrity, technology independence and architectural consistency.

This standard establishes

- ORM principles
- ORM architecture
- Aggregate mapping
- Entity mapping
- Value Object mapping
- relationship mapping
- inheritance mapping
- loading strategies
- change tracking
- dependency rules
- lifecycle management
- performance optimisation
- concurrency handling
- error handling
- security requirements
- implementation guidance
- governance requirements
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Domain-Driven Design principles are inherited from EA-300.

Infrastructure Layer principles are inherited from EA-320.

Persistence Architecture principles are inherited from EA-321.

Database Architecture principles are inherited from EA-323.

This standard shall be regarded as the authoritative Enterprise ORM Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
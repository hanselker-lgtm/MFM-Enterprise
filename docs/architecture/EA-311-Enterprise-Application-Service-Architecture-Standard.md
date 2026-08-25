# EA-311 Enterprise Application Service Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-311 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Application Service Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Application Services |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Application Service Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Application Service Architecture aligned with EA-020, EA-111, EA-112, EA-300–EA-310 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-301 | Enterprise Domain Architecture Standard |
| EA-305 | Enterprise Domain Service Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-309 | Enterprise Domain Event Architecture Standard |
| EA-310 | Enterprise Application Layer Reference Architecture |
| EA-312 | Enterprise Command Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Application Services.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Enterprise Domain architecture is inherited from EA-300 through EA-309.

Application Layer principles are inherited from EA-310.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Application Services shall be designed, implemented and governed within the MFM Enterprise Platform.

Application Services coordinate business use cases by orchestrating Domain operations while preserving the integrity and independence of the Domain Layer.

---

# 2. Scope

This standard applies to every Application Service within every Enterprise Domain.

It governs

- use case orchestration
- Domain interaction
- Repository coordination
- transaction coordination
- validation coordination
- security coordination
- dependency rules
- governance

Business rule implementation is outside the scope of this standard.

---

# 3. Definition of an Application Service

An Application Service coordinates the execution of a business use case.

An Application Service shall

- orchestrate Domain behaviour
- coordinate Repository interaction
- manage transaction boundaries
- coordinate external interactions
- return application results

An Application Service shall never own business rules.

---

# 4. Application Service Objectives

Every Application Service shall

- expose one or more business use cases
- remain orchestration focused
- preserve Domain purity
- coordinate technical concerns
- minimise application complexity

Application Services exist to coordinate business execution—not to implement business behaviour.

---

# 5. Application Service Responsibilities

Application Services are responsible for

- receiving application requests
- validating application input
- loading Aggregates
- invoking Domain behaviour
- coordinating persistence
- publishing Application Events
- returning application responses

Application Services shall never

- implement business rules
- manipulate Aggregate internals
- bypass Aggregate invariants
- contain persistence implementation

Their responsibility is orchestration only.

---

# End of Part 1

---

# 6. Use Case Coordination

Application Services shall coordinate the complete execution of a business use case.

Use case coordination may include

- validating application requests
- retrieving Aggregate Roots
- invoking Domain behaviour
- coordinating Repository operations
- publishing Application Events
- preparing application responses

Each Application Service operation shall represent one clearly defined business use case.

---

# 7. Repository Interaction

Application Services shall access persistent Domain objects exclusively through Repository interfaces.

Repository interaction shall

- retrieve Aggregate Roots
- persist Aggregate changes
- coordinate transactional consistency
- remain independent of persistence technology

Application Services shall never access database implementations directly.

All persistence interaction shall occur through Repository abstractions.

---

# 8. Transaction Management

Application Services are responsible for coordinating transactional execution.

Transaction management shall

- establish transaction boundaries
- coordinate Unit of Work
- ensure atomic execution
- commit successful operations
- rollback failed operations

Business behaviour shall remain independent of transaction management.

Transaction coordination belongs to the Application Layer.

---

# 9. Validation Coordination

Application Services shall coordinate application-level validation before invoking Domain behaviour.

Validation may include

- request completeness
- mandatory input verification
- data format validation
- authorization prerequisites
- application-level consistency checks

Business validation shall remain within the Domain Layer.

Application validation shall never duplicate Domain validation.

---

# 10. Security Coordination

Application Services shall coordinate application security.

Security coordination may include

- authentication verification
- authorization evaluation
- permission checks
- tenant resolution
- audit initiation

Security mechanisms shall remain independent of Domain behaviour.

Business authorization rules shall remain within the Domain Model.

---

# 11. Dependency Rules

Application Services may depend upon

- Aggregates
- Domain Services
- Repository interfaces
- Specifications
- Factories
- Application contracts
- infrastructure abstractions

Application Services shall never depend directly upon

- database implementations
- ORM implementations
- presentation frameworks
- user interface components

Dependency direction shall always point toward abstractions.

---

# 12. Application Service Collaboration

Application Services may collaborate with

- Domain Services
- Repository interfaces
- Factories
- Application Events
- external service abstractions

Application Services shall never collaborate directly with

- database engines
- ORM sessions
- presentation components
- infrastructure implementations

Collaboration shall preserve architectural layering and Domain independence.

---

# End of Part 2

---

# 13. Application Service Lifecycle

Every Application Service shall follow a controlled architectural lifecycle.

```text
Application Request
         │
         ▼
Request Validation
         │
         ▼
Transaction Started
         │
         ▼
Repository Interaction
         │
         ▼
Domain Execution
         │
         ▼
Persistence Coordination
         │
         ▼
Application Event Publication
         │
         ▼
Application Response
```

The lifecycle shall coordinate execution without introducing business behaviour into the Application Layer.

Application Services shall evolve together with the business use cases they support.

---

# 14. Error Handling

Application Services shall coordinate application-level error handling.

Error handling shall

- preserve transactional consistency
- distinguish business exceptions from technical exceptions
- propagate meaningful error information
- support diagnostics and auditing
- avoid exposing internal implementation details

Business exceptions originating in the Domain Layer shall retain their business meaning.

Technical failures shall be translated into appropriate application-level responses.

---

# 15. Architectural Constraints

Enterprise Application Services shall comply with the following architectural constraints.

Application Services shall

- remain orchestration focused
- coordinate Domain behaviour
- coordinate transaction boundaries
- preserve Domain purity
- expose meaningful use cases
- remain technology independent where practical

Application Services shall never

- implement business rules
- manipulate Aggregate internals
- expose persistence implementations
- bypass Repository abstractions
- maintain Domain state

These constraints preserve the separation between application orchestration and Domain execution.

---

# 16. Application Service Quality Attributes

Enterprise Application Services shall be designed to achieve

- simplicity
- readability
- maintainability
- reliability
- scalability
- traceability
- testability
- clear separation of concerns

Application Services shall remain thin orchestration components.

Business complexity shall remain within the Domain Layer.

---

# 17. Performance Considerations

Application Services shall coordinate business execution efficiently while preserving architectural integrity.

Performance optimisation shall

- minimise unnecessary Repository access
- reduce redundant Domain operations
- coordinate efficient transaction scope
- support scalable execution

Performance improvements shall never compromise

- Domain correctness
- business consistency
- Aggregate invariants
- architectural layering

Correctness shall always take precedence over optimisation.

---

# 18. Application Service Anti-Patterns

The following architectural anti-patterns are prohibited.

## Fat Application Service

Application Services shall never accumulate business logic.

Business decisions belong exclusively within Aggregates and Domain Services.

---

## Aggregate Bypass

Application Services shall never manipulate internal Entity state directly.

All business state changes shall occur through Aggregate operations.

---

## Infrastructure Leakage

Application Services shall never expose

- SQL statements
- ORM entities
- database sessions
- messaging APIs
- framework-specific persistence objects

Infrastructure concerns shall remain isolated behind architectural abstractions.

---

## Duplicate Domain Logic

Business rules shall never be duplicated between the Application Layer and the Domain Layer.

The Domain Model shall remain the single authoritative source of business behaviour.

---

## Workflow-Centric Business Logic

Application workflows shall never replace proper Domain modelling.

Application Services coordinate business execution.

They do not define business behaviour.

---

# End of Part 3

---

# 13. Application Service Lifecycle

Every Application Service shall follow a controlled architectural lifecycle.

```text
Application Request
         │
         ▼
Request Validation
         │
         ▼
Transaction Started
         │
         ▼
Repository Interaction
         │
         ▼
Domain Execution
         │
         ▼
Persistence Coordination
         │
         ▼
Application Event Publication
         │
         ▼
Application Response
```

The lifecycle shall coordinate execution without introducing business behaviour into the Application Layer.

Application Services shall evolve together with the business use cases they support.

---

# 14. Error Handling

Application Services shall coordinate application-level error handling.

Error handling shall

- preserve transactional consistency
- distinguish business exceptions from technical exceptions
- propagate meaningful error information
- support diagnostics and auditing
- avoid exposing internal implementation details

Business exceptions originating in the Domain Layer shall retain their business meaning.

Technical failures shall be translated into appropriate application-level responses.

---

# 15. Architectural Constraints

Enterprise Application Services shall comply with the following architectural constraints.

Application Services shall

- remain orchestration focused
- coordinate Domain behaviour
- coordinate transaction boundaries
- preserve Domain purity
- expose meaningful use cases
- remain technology independent where practical

Application Services shall never

- implement business rules
- manipulate Aggregate internals
- expose persistence implementations
- bypass Repository abstractions
- maintain Domain state

These constraints preserve the separation between application orchestration and Domain execution.

---

# 16. Application Service Quality Attributes

Enterprise Application Services shall be designed to achieve

- simplicity
- readability
- maintainability
- reliability
- scalability
- traceability
- testability
- clear separation of concerns

Application Services shall remain thin orchestration components.

Business complexity shall remain within the Domain Layer.

---

# 17. Performance Considerations

Application Services shall coordinate business execution efficiently while preserving architectural integrity.

Performance optimisation shall

- minimise unnecessary Repository access
- reduce redundant Domain operations
- coordinate efficient transaction scope
- support scalable execution

Performance improvements shall never compromise

- Domain correctness
- business consistency
- Aggregate invariants
- architectural layering

Correctness shall always take precedence over optimisation.

---

# 18. Application Service Anti-Patterns

The following architectural anti-patterns are prohibited.

## Fat Application Service

Application Services shall never accumulate business logic.

Business decisions belong exclusively within Aggregates and Domain Services.

---

## Aggregate Bypass

Application Services shall never manipulate internal Entity state directly.

All business state changes shall occur through Aggregate operations.

---

## Infrastructure Leakage

Application Services shall never expose

- SQL statements
- ORM entities
- database sessions
- messaging APIs
- framework-specific persistence objects

Infrastructure concerns shall remain isolated behind architectural abstractions.

---

## Duplicate Domain Logic

Business rules shall never be duplicated between the Application Layer and the Domain Layer.

The Domain Model shall remain the single authoritative source of business behaviour.

---

## Workflow-Centric Business Logic

Application workflows shall never replace proper Domain modelling.

Application Services coordinate business execution.

They do not define business behaviour.

---

# End of Part 3

---

# 19. Implementation Guidelines

Enterprise Application Service implementations shall be developed according to the architectural principles defined in EA-020, EA-111, EA-112, EA-300 through EA-310.

Implementation shall ensure

- thin orchestration components
- clear use case boundaries
- technology-independent business coordination
- transaction coordination
- Repository abstraction
- Domain purity
- maintainable implementation

Application Services shall expose business-oriented operations using the ubiquitous language of the Enterprise Domain.

Technical implementation details shall remain hidden behind architectural abstractions.

---

# 20. Architecture Compliance

Enterprise Application Service implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-307 Enterprise Specification Architecture Standard
- EA-308 Enterprise Factory Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard
- EA-310 Enterprise Application Layer Reference Architecture
- this Enterprise Application Service Architecture Standard

Architecture reviews shall verify

- orchestration-only responsibility
- Domain purity
- Repository abstraction
- transaction coordination
- dependency compliance
- technology independence
- documentation completeness

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 21. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-300 compliance verified | ☐ |
| EA-301 compliance verified | ☐ |
| EA-302 compliance verified | ☐ |
| EA-303 compliance verified | ☐ |
| EA-304 compliance verified | ☐ |
| EA-305 compliance verified | ☐ |
| EA-306 compliance verified | ☐ |
| EA-307 compliance verified | ☐ |
| EA-308 compliance verified | ☐ |
| EA-309 compliance verified | ☐ |
| EA-310 compliance verified | ☐ |
| Orchestration-only implementation verified | ☐ |
| Repository abstraction verified | ☐ |
| Domain purity verified | ☐ |
| Transaction coordination verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Application Service shall satisfy all mandatory compliance requirements before being released into production.

---

# 22. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-307 Enterprise Specification Architecture Standard
- EA-308 Enterprise Factory Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard
- EA-310 Enterprise Application Layer Reference Architecture
- EA-312 Enterprise Command Architecture Standard

---

# 23. Summary

This standard defines how Enterprise Application Services shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Application Services coordinate business use cases by orchestrating Domain operations while preserving the independence, integrity and purity of the Domain Layer.

This standard establishes

- use case orchestration
- Repository coordination
- transaction coordination
- validation coordination
- security coordination
- dependency rules
- architectural constraints
- implementation guidance
- governance requirements
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Enterprise Domain architecture is inherited from EA-300 through EA-309.

Application Layer principles are inherited from EA-310.

This standard shall be regarded as the authoritative Enterprise Application Service Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
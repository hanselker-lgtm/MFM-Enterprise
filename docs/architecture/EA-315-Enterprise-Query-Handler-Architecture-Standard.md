# EA-315 Enterprise Query Handler Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-315 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Query Handler Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Query Handlers |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Query Handler Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Query Handler Architecture aligned with EA-020, EA-111, EA-112 and EA-300–EA-314 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-310 | Enterprise Application Layer Reference Architecture |
| EA-311 | Enterprise Application Service Architecture Standard |
| EA-314 | Enterprise Query Architecture Standard |
| EA-316 | Enterprise CQRS Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Query Handlers.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Application Layer principles are inherited from EA-310 through EA-314.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Query Handlers shall be designed, implemented and governed within the MFM Enterprise Platform.

Query Handlers coordinate information retrieval.

They execute Queries.

They never modify Domain state.

---

# 2. Scope

This standard applies to every Query Handler within every Enterprise Domain.

It governs

- responsibilities
- orchestration
- read operations
- dependency rules
- mapping
- lifecycle
- governance

Business execution and state modification are outside the scope of this standard.

---

# 3. Definition of a Query Handler

A Query Handler is an Application Layer component responsible for executing exactly one Query.

A Query Handler shall

- receive one Query
- coordinate information retrieval
- invoke read infrastructure
- map retrieved information
- return a result

A Query Handler shall never modify Domain state.

---

# 4. Query Handler Objectives

Every Query Handler shall

- execute one Query
- retrieve requested information
- remain deterministic
- coordinate read operations
- return application results

Query Handlers orchestrate information retrieval while remaining free of business behaviour.

---

# 5. Query Handler Responsibilities

Query Handlers are responsible for

- validating execution prerequisites
- coordinating read operations
- invoking Read Repositories
- invoking Read Models
- mapping retrieved data
- returning application responses

Query Handlers shall never

- execute business rules
- modify Aggregates
- publish Domain Events
- invoke Command Handlers
- perform write operations

Business execution belongs exclusively to the write side of CQRS.

---

# End of Part 1

---

# 6. Query Handler Structure

Every Enterprise Query Handler shall follow a consistent architectural structure.

A Query Handler shall contain

- one Query input
- orchestration logic
- read coordination
- result mapping
- application response generation

A Query Handler shall not contain

- business rules
- Aggregate behaviour
- persistence logic
- infrastructure implementation
- presentation logic

The Query Handler shall remain an orchestration component within the Application Layer.

---

# 7. Read Model Collaboration

Query Handlers retrieve information through Read Models.

Read Models may

- represent denormalised data
- aggregate multiple data sources
- optimise read performance
- expose application-specific views

Query Handlers shall never modify Read Models.

Read Models exist solely to support efficient information retrieval.

---

# 8. Repository Collaboration

Query Handlers may collaborate with Read Repositories.

Read Repositories are responsible for

- retrieving data
- executing queries
- optimising data access
- hiding persistence implementation

Query Handlers shall never

- execute SQL directly
- access databases directly
- depend upon ORM implementations
- expose persistence technology

Repository abstractions preserve infrastructure independence.

---

# 9. Read-only Execution

Query Handler execution shall always remain read-only.

Execution may

- retrieve information
- aggregate information
- transform information
- map information
- return information

Execution shall never

- create entities
- update entities
- delete entities
- invoke Commands
- modify Aggregates
- publish Domain Events

Read-side execution shall remain completely free of side effects.

---

# 10. Mapping Responsibilities

Query Handlers are responsible for mapping retrieved information into application responses.

Mapping may include

- Data Transfer Objects
- View Models
- response contracts
- projection models
- immutable response objects

Mapping shall

- remain deterministic
- preserve business meaning
- avoid infrastructure leakage

Mapping logic shall remain lightweight.

Complex business calculations belong outside the Query Handler.

---

# 11. Dependency Rules

Query Handlers shall depend only upon stable Application Layer abstractions.

Permitted dependencies include

- Query definitions
- Read Repository interfaces
- Read Model interfaces
- Value Objects
- DTOs
- response contracts

Query Handlers shall never depend directly upon

- database implementations
- ORM entities
- infrastructure frameworks
- presentation frameworks
- Aggregate implementations
- Domain Event publishers

Dependency direction shall always point toward stable abstractions.

---

# 12. Query Handler Collaboration

Query Handlers collaborate only through the Application Layer.

A Query Handler may collaborate with

- Read Repositories
- Read Models
- mapping components
- response factories

A Query Handler shall never collaborate directly with

- Command Handlers
- Commands
- Aggregates
- Domain Services performing business execution
- infrastructure implementations

Each Query Handler shall execute one Query independently.

---

# End of Part 2

---

# 13. Query Handler Lifecycle

Every Enterprise Query Handler shall follow a well-defined architectural lifecycle.

```text
Query Received
       │
       ▼
Application Validation
       │
       ▼
Read Repository / Read Model
       │
       ▼
Data Retrieval
       │
       ▼
Result Mapping
       │
       ▼
Application Response
```

Each Query Handler executes exactly one Query.

Execution shall remain deterministic, stateless and free of side effects.

No Domain state shall be modified during execution.

---

# 14. Error Handling

Query Handlers shall handle errors consistently.

Recoverable errors may include

- missing data
- invalid query parameters
- unavailable read resources
- timeout conditions
- temporary infrastructure failures

Query Handlers shall

- return consistent error responses
- avoid exposing infrastructure details
- preserve diagnostic information for logging
- support application-level error handling

Unexpected exceptions shall be propagated through the Enterprise exception handling framework.

---

# 15. Caching

Query Handlers may support caching where appropriate.

Caching may be applied to

- frequently requested reference data
- read-only lookup data
- static configuration data
- projection results
- expensive read operations

Caching shall never compromise

- correctness
- security
- data consistency
- authorization
- auditability

Caching policies shall be defined outside individual Query Handlers.

---

# 16. Performance Optimisation

Query Handlers shall be designed for efficient information retrieval.

Optimisation techniques may include

- projection queries
- pagination
- filtering
- asynchronous execution
- batching
- caching
- optimized read models

Performance optimisation shall never violate Enterprise Architecture principles.

Correctness shall always take precedence over performance.

---

# 17. Quality Attributes

Enterprise Query Handlers shall achieve

- simplicity
- readability
- maintainability
- predictability
- scalability
- testability
- traceability
- performance

Query Handlers shall remain lightweight orchestration components.

Business behaviour shall remain outside the Application Layer.

---

# 18. Architectural Constraints

Enterprise Query Handlers shall comply with the following constraints.

A Query Handler shall

- execute exactly one Query
- remain stateless
- coordinate read operations
- retrieve information only
- return application responses

A Query Handler shall never

- execute Commands
- modify Domain state
- update Aggregates
- publish Domain Events
- perform write operations
- contain business rules

These constraints preserve the separation between the read and write sides of CQRS.

---

# 19. Query Handler Anti-Patterns

The following architectural anti-patterns are prohibited.

## Fat Query Handler

Query Handlers shall never implement business logic.

They shall orchestrate information retrieval only.

---

## Multi-Query Handler

A Query Handler shall never execute multiple unrelated Queries.

One Query Handler shall execute exactly one Query.

---

## Stateful Query Handler

Query Handlers shall never retain mutable execution state between requests.

Each execution shall be independent.

---

## Infrastructure Leakage

Query Handlers shall never expose

- SQL statements
- ORM entities
- persistence models
- infrastructure services
- database-specific implementations

Infrastructure details shall remain hidden behind Enterprise abstractions.

---

## Write-side Behaviour

Query Handlers shall never

- create entities
- modify entities
- delete entities
- invoke Command Handlers
- publish Domain Events

Read-side and write-side responsibilities shall remain completely separated.

---

# End of Part 3

---

# 20. Implementation Guidelines

Enterprise Query Handler implementations shall follow the architectural principles defined in EA-020, EA-111, EA-112 and EA-310 through EA-314.

Implementation shall ensure

- one Query Handler per Query
- lightweight orchestration
- read-only execution
- repository abstraction
- technology independence
- deterministic execution
- efficient information retrieval

Query Handlers shall coordinate information retrieval.

Business behaviour shall remain within the Domain Layer or dedicated read infrastructure where appropriate.

---

# 21. Architecture Compliance

Enterprise Query Handler implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-310 Enterprise Application Layer Reference Architecture
- EA-311 Enterprise Application Service Architecture Standard
- EA-312 Enterprise Command Architecture Standard
- EA-313 Enterprise Command Handler Architecture Standard
- EA-314 Enterprise Query Architecture Standard
- this Enterprise Query Handler Architecture Standard

Architecture reviews shall verify

- one Query Handler per Query
- read-only execution
- repository abstraction
- dependency compliance
- technology independence
- mapping responsibilities
- documentation completeness

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 22. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-310 compliance verified | ☐ |
| EA-311 compliance verified | ☐ |
| EA-312 compliance verified | ☐ |
| EA-313 compliance verified | ☐ |
| EA-314 compliance verified | ☐ |
| One Query per Handler verified | ☐ |
| Read-only execution verified | ☐ |
| Repository abstraction verified | ☐ |
| Dependency compliance verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Query Handler shall satisfy all mandatory compliance requirements before being released into production.

---

# 23. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-310 Enterprise Application Layer Reference Architecture
- EA-311 Enterprise Application Service Architecture Standard
- EA-312 Enterprise Command Architecture Standard
- EA-313 Enterprise Command Handler Architecture Standard
- EA-314 Enterprise Query Architecture Standard
- EA-316 Enterprise CQRS Architecture Standard

---

# 24. Summary

This standard defines how Enterprise Query Handlers shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Query Handlers coordinate the execution of immutable Queries and retrieve information through Read Repositories and Read Models. They remain stateless orchestration components and shall never modify Domain state.

This standard establishes

- Query Handler responsibilities
- read-only execution
- orchestration principles
- Read Repository collaboration
- Read Model collaboration
- mapping responsibilities
- dependency rules
- lifecycle
- error handling
- caching principles
- performance optimisation
- architectural constraints
- implementation guidance
- governance requirements
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Application Layer principles are inherited from EA-310 through EA-314.

This standard shall be regarded as the authoritative Enterprise Query Handler Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
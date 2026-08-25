# EA-306 Enterprise Repository Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-306 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Repository Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Repository Interfaces and Implementations |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Repository Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Repository Architecture aligned with EA-020, EA-111, EA-300, EA-301, EA-302, EA-303, EA-304 and EA-305 | Chief Enterprise Architect |

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
| EA-309 | Enterprise Domain Event Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Repository design and implementation.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Repositories shall be designed, implemented and governed within the MFM Enterprise Platform.

Repositories provide the architectural abstraction between the Domain Layer and the Infrastructure Layer while preserving persistence ignorance.

Repositories shall provide access to Aggregate Roots without exposing persistence technology.

---

# 2. Scope

This standard applies to every Repository interface and every Repository implementation throughout the Enterprise Platform.

It governs

- Repository responsibilities
- Aggregate persistence
- Repository interfaces
- dependency rules
- transaction boundaries
- infrastructure implementations
- lifecycle
- governance

Database technology, ORM frameworks and storage engines are outside the scope of this standard.

---

# 3. Definition of a Repository

A Repository is the architectural abstraction responsible for loading and persisting Aggregate Roots.

Repositories represent collections of Aggregates from the perspective of the Domain Layer.

A Repository shall

- expose Aggregate access
- preserve Domain abstraction
- remain technology independent at the interface level
- hide persistence implementation
- support business operations

A Repository shall never expose database structures.

---

# 4. Repository Objectives

Every Repository shall

- isolate persistence concerns
- preserve Domain purity
- support Aggregate consistency
- minimise infrastructure leakage
- expose meaningful business operations

Repositories exist to support the Domain Model rather than the database model.

---

# 5. Repository Responsibilities

Repositories are responsible for

- loading Aggregate Roots
- storing Aggregate Roots
- removing Aggregate Roots
- locating Aggregates using business criteria
- supporting transactional consistency

Repositories shall never

- implement business rules
- contain presentation logic
- execute application workflows
- expose database schema

Business behaviour belongs exclusively within the Domain Layer.

---

# End of Part 1

---

# 6. Repository Interfaces

Every Repository shall expose its functionality through a Domain-defined interface.

Repository interfaces belong exclusively to the Domain Layer.

Repository implementations belong exclusively to the Infrastructure Layer.

Repository interfaces shall

- define business-oriented operations
- remain technology independent
- expose Aggregate access
- avoid persistence terminology

Method names shall reflect the ubiquitous language of the Domain.

---

# 7. Aggregate Persistence

Repositories shall persist Aggregate Roots as complete consistency boundaries.

Repositories shall never persist individual internal Entities independently of their Aggregate Root.

Aggregate persistence shall

- preserve Aggregate invariants
- preserve transactional consistency
- preserve business integrity
- support Aggregate lifecycle management

Only Aggregate Roots shall be directly accessible through Repository interfaces.

---

# 8. Query Responsibilities

Repositories shall support business-oriented retrieval of Aggregate Roots.

Repository queries shall

- use business terminology
- express Domain intent
- return Aggregate Roots
- remain independent of database technology

Repositories shall avoid exposing database-specific query mechanisms.

Complex reporting queries that do not return Aggregate Roots should be implemented outside the Domain Repository abstraction.

---

# 9. Dependency Rules

Repository interfaces may depend upon

- Aggregate Roots
- Value Objects
- Domain identifiers
- Specifications
- Domain abstractions

Repository interfaces shall never depend upon

- SQL
- ORM frameworks
- database drivers
- infrastructure libraries
- messaging frameworks
- presentation components

Infrastructure implementations may depend upon persistence technologies while preserving the Domain interface contract.

---

# 10. Unit of Work Interaction

Repositories shall cooperate with the Unit of Work to ensure transactional consistency.

The Unit of Work is responsible for

- transaction boundaries
- change tracking
- commit coordination
- rollback handling

Repositories shall not manage transactions directly unless explicitly defined by the architectural infrastructure.

Transaction management belongs outside the Domain Layer.

---

# 11. Repository Collaboration

Repositories may collaborate with

- Domain Services
- Application Services
- Specifications
- Domain Events
- Unit of Work

Repositories shall never collaborate directly with

- user interfaces
- presentation components
- external APIs
- messaging infrastructure

All collaboration shall preserve Domain isolation and architectural layering.

---

# 12. Repository Operations

Repository operations shall represent meaningful Domain activities.

Typical operations include

- retrieve Aggregate by identifier
- retrieve Aggregate using business criteria
- store Aggregate
- remove Aggregate
- determine Aggregate existence

Repository interfaces shall avoid exposing generic CRUD terminology whenever a business-oriented alternative exists.

Business language shall always take precedence over technical persistence language.

---

# End of Part 2

---

# 13. Repository Lifecycle

Every Repository shall follow a well-defined architectural lifecycle.

```text
Repository Interface
         │
         ▼
Infrastructure Implementation
         │
         ▼
Aggregate Retrieval
         │
         ▼
Aggregate Persistence
         │
         ▼
Transaction Completion
         │
         ▼
Repository Reuse
```

Repository implementations shall remain reusable throughout the lifetime of the Enterprise Platform.

Repository interfaces shall remain stable even when persistence technologies evolve.

---

# 14. Transaction Boundaries

Repositories participate in transactions but do not define transaction scope.

Transaction boundaries shall be managed by the Application Layer through the Unit of Work or an equivalent transactional mechanism.

Repositories shall

- participate in active transactions
- preserve Aggregate consistency
- support atomic persistence
- cooperate with transaction management

Repositories shall never

- open transactions autonomously
- commit transactions independently
- rollback transactions independently
- coordinate distributed transactions

Transaction orchestration belongs outside the Repository abstraction.

---

# 15. Architectural Constraints

Enterprise Repositories shall comply with the following architectural constraints.

Repository interfaces shall

- remain technology independent
- expose Aggregate-oriented operations
- preserve Domain abstraction
- remain persistence ignorant

Repository implementations shall

- encapsulate persistence technology
- implement Repository interfaces
- remain isolated within the Infrastructure Layer
- preserve Domain contracts

Repositories shall never

- expose database tables
- expose SQL statements
- expose ORM entities
- contain business rules
- bypass Aggregate invariants

These constraints preserve the separation between Domain and Infrastructure.

---

# 16. Repository Quality Attributes

Enterprise Repositories shall be designed to achieve

- consistency
- reliability
- maintainability
- scalability
- performance
- testability
- technology independence
- architectural stability

Repository implementations shall optimise persistence without changing Domain behaviour.

Performance improvements shall never compromise Domain integrity.

---

# 17. Repository Anti-Patterns

The following architectural anti-patterns are prohibited.

## Database-Centric Repository

Repositories shall not expose database schema, table structures or persistence-specific concepts.

The Domain shall remain independent of storage design.

---

## Generic CRUD Repository

Repositories shall not be designed as generic CRUD wrappers.

Repository operations shall express meaningful Domain behaviour rather than technical database operations.

---

## Business Logic in Repository

Repositories shall never contain

- business decisions
- business policies
- validation rules
- calculations

Business logic belongs exclusively within the Domain Layer.

---

## Infrastructure Leakage

Repository interfaces shall never expose

- SQL
- ORM APIs
- persistence annotations
- database sessions
- storage-specific identifiers

Persistence technology shall remain completely hidden from the Domain Layer.

---

## Aggregate Bypass

Repositories shall never allow direct persistence of internal Entities or Value Objects outside their Aggregate Root.

Aggregate consistency boundaries shall always be preserved.

---

# 18. Repository Evolution

Enterprise Repositories shall evolve together with the Domain Model.

Evolution shall

- preserve Domain contracts
- minimise breaking interface changes
- support new persistence technologies
- maintain architectural consistency

Repository interfaces shall remain stable over time even when infrastructure implementations are replaced.

---

# End of Part 3

---

# 19. Implementation Guidelines

Enterprise Repository implementations shall be developed in accordance with the architectural principles defined in EA-300, EA-301, EA-302, EA-303, EA-304 and EA-305.

Implementation shall ensure

- complete separation between Domain and Infrastructure
- persistence ignorance
- Aggregate-oriented persistence
- technology-independent interfaces
- transactional consistency
- business-oriented operations
- stable Repository contracts

Repository implementations shall encapsulate all persistence-specific concerns.

Changes to persistence technology shall not require modifications to the Domain Layer.

---

# 20. Architecture Compliance

Enterprise Repository implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- this Enterprise Repository Architecture Standard

Architecture reviews shall verify

- Domain abstraction
- technology-independent Repository interfaces
- Aggregate persistence
- dependency compliance
- transaction handling
- persistence isolation
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
| Repository interface technology independent | ☐ |
| Aggregate-only persistence verified | ☐ |
| No infrastructure leakage into Domain | ☐ |
| Transaction handling verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Repository shall satisfy all mandatory compliance requirements before being released into production.

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
- EA-307 Enterprise Specification Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard

---

# 23. Summary

This standard defines how Enterprise Repositories shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Repositories provide the architectural abstraction between the Domain Layer and the Infrastructure Layer by encapsulating persistence concerns while preserving Domain purity and Aggregate consistency.

This standard establishes

- Repository abstraction
- Aggregate-oriented persistence
- technology-independent interfaces
- transaction participation
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

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This standard shall be regarded as the authoritative Enterprise Repository Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
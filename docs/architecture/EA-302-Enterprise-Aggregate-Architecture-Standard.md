# EA-302 Enterprise Aggregate Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-302 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Aggregate Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Aggregates |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Aggregate Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Aggregate Architecture aligned with EA-020, EA-111, EA-300 and EA-301 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-301 | Enterprise Domain Architecture Standard |
| EA-303 | Enterprise Entity Architecture Standard |
| EA-304 | Enterprise Value Object Architecture Standard |
| EA-305 | Enterprise Domain Service Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-309 | Enterprise Domain Event Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Aggregates.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Aggregates shall be designed, implemented and governed within the MFM Enterprise Platform.

An Aggregate represents the authoritative consistency boundary for a group of related business objects.

It protects business invariants while ensuring transactional consistency.

---

# 2. Scope

This standard applies to every Aggregate within every Enterprise Domain.

It governs

- Aggregate structure
- Aggregate Root
- consistency boundaries
- transactional boundaries
- Aggregate behaviour
- Aggregate lifecycle
- Aggregate references
- Aggregate persistence
- Aggregate evolution

Implementation details of Entities and Value Objects are defined in their respective standards.

---

# 3. Definition of an Aggregate

An Aggregate is a cluster of business objects treated as a single consistency boundary.

Every Aggregate shall

- have exactly one Aggregate Root
- protect business invariants
- encapsulate internal state
- expose business behaviour
- define transactional consistency
- control access to internal objects

The Aggregate Root is the only externally accessible object.

---

# 4. Aggregate Objectives

Every Aggregate shall

- maintain business consistency
- enforce invariants
- encapsulate business rules
- expose meaningful business operations
- prevent invalid state
- remain cohesive
- minimise external dependencies

Business correctness shall always take precedence over implementation convenience.

---

# 5. Aggregate Root

Every Aggregate shall contain one Aggregate Root.

The Aggregate Root

- owns the Aggregate
- validates business operations
- enforces invariants
- coordinates Entities
- coordinates Value Objects
- publishes Domain Events
- protects Aggregate integrity

External components shall communicate only with the Aggregate Root.

---

# End of Part 1

---

# 6. Consistency Boundary

An Aggregate defines the smallest business consistency boundary within the Enterprise Domain.

All business invariants contained within an Aggregate shall always be valid before and after every business operation.

Consistency shall be maintained

- during object creation
- during state transitions
- during updates
- during deletion
- during event publication

Business consistency shall never depend upon multiple Aggregates participating in the same transaction.

---

# 7. Transaction Boundary

An Aggregate represents one transactional boundary.

Every business transaction shall modify at most one Aggregate.

Transactions shall

- begin at the Aggregate Root
- complete within the Aggregate
- preserve all invariants
- either succeed completely or fail completely

Distributed transactions between Aggregates are prohibited.

Business workflows requiring multiple Aggregates shall be coordinated by the Application Layer or Enterprise Workflow Layer.

---

# 8. Aggregate Composition

An Aggregate consists of one Aggregate Root and zero or more internal business objects.

An Aggregate may contain

- Entities
- Value Objects
- Collections of Entities
- Collections of Value Objects

Internal objects belong exclusively to their Aggregate.

Internal objects shall never be shared between Aggregates.

Ownership shall remain explicit throughout the Aggregate lifecycle.

---

# 9. Aggregate References

Aggregates shall remain independent.

References between Aggregates shall be implemented using business identifiers only.

An Aggregate shall never directly reference another Aggregate instance.

Allowed

- Aggregate ID
- Business Identifier
- Reference Number

Prohibited

- Object references
- Shared Entity instances
- Shared Value Object instances
- Shared collections

This prevents hidden dependencies and preserves Aggregate autonomy.

---

# 10. Aggregate Size

Aggregates shall remain small and cohesive.

An Aggregate shall contain only business objects required to enforce its own invariants.

Large Aggregates increase

- transaction duration
- locking
- coupling
- memory usage
- implementation complexity

If an Aggregate grows beyond its business responsibility, it shall be decomposed into multiple Aggregates.

Aggregate size shall be determined by business consistency rather than database relationships.

---

# 11. Business Invariants

Business invariants define conditions that shall always remain true within an Aggregate.

Examples include

- required business state
- ownership rules
- financial balances
- uniqueness constraints
- lifecycle restrictions
- business authorisations

Every business operation shall validate all affected invariants before committing state changes.

Violation of an invariant shall prevent completion of the transaction.

Business invariants shall be implemented exclusively within the Aggregate.

---

# 12. Aggregate Behaviour

Aggregates encapsulate business behaviour rather than exposing mutable data.

Business operations shall

- validate intent
- enforce invariants
- modify internal state
- produce Domain Events where appropriate
- preserve consistency

Consumers shall invoke explicit business operations.

Consumers shall never manipulate Aggregate state directly.

---

# End of Part 2

---

# 13. Aggregate Lifecycle

Every Aggregate shall follow a well-defined lifecycle.

```text
Create
   │
   ▼
Initialize
   │
   ▼
Active
   │
   ├───────────────┐
   ▼               ▼
Modify         Publish Events
   │               │
   └───────┬───────┘
           ▼
      Persist State
           │
           ▼
      Archive/Delete
```

Each lifecycle transition shall preserve Aggregate consistency.

Lifecycle transitions shall occur only through explicit business operations exposed by the Aggregate Root.

Aggregate state transitions shall never bypass business validation.

---

# 14. Concurrency Control

Enterprise Aggregates shall support concurrent access without compromising business integrity.

Concurrency management shall ensure

- consistency
- repeatable business outcomes
- protection against conflicting updates
- deterministic state transitions

Concurrency mechanisms shall remain transparent to business logic.

Business rules shall never depend upon infrastructure-specific locking implementations.

---

# 15. Aggregate Versioning

Every Aggregate shall maintain an explicit version.

Versioning supports

- optimistic concurrency control
- change tracking
- event sequencing
- auditability

Version numbers shall increase only after successful completion of a business transaction.

Failed transactions shall not modify Aggregate versions.

---

# 16. Optimistic Locking

Enterprise Aggregates shall use optimistic locking unless an approved architectural exception exists.

Optimistic locking shall

- detect concurrent modifications
- prevent lost updates
- preserve Aggregate consistency
- avoid unnecessary database locking

Concurrency conflicts shall result in transaction failure rather than automatic overwrite.

Conflict resolution belongs to the Application Layer.

---

# 17. Persistence Rules

Persistence shall preserve Aggregate boundaries.

Repositories shall

- load complete Aggregates
- persist complete Aggregates
- never expose partial Aggregate state
- preserve Aggregate consistency

Persistence technologies shall never influence Aggregate design.

Aggregates shall remain persistence ignorant.

Database schemas shall adapt to the Aggregate model, not the reverse.

---

# 18. Aggregate Collaboration

Aggregates collaborate through business processes rather than direct object relationships.

Collaboration shall occur using

- business identifiers
- Domain Events
- Application Services
- Enterprise Workflows

Aggregates shall never invoke business behaviour on other Aggregates directly.

Business processes spanning multiple Aggregates shall be coordinated outside the Domain Layer.

---

# 19. Aggregate Anti-Patterns

The following Aggregate anti-patterns are prohibited.

## Large Aggregate

Aggregates shall not accumulate unrelated responsibilities.

Oversized Aggregates reduce maintainability and scalability.

---

## Shared Entity

Entities shall belong to exactly one Aggregate.

Sharing Entity instances between Aggregates is prohibited.

---

## Cross-Aggregate Transaction

Business transactions shall not modify multiple Aggregates within a single transaction boundary.

Distributed consistency shall be achieved through Domain Events and Workflow coordination.

---

## Infrastructure Leakage

Aggregates shall never contain

- SQL statements
- ORM-specific behaviour
- HTTP clients
- messaging infrastructure
- dependency injection logic
- file system access

Infrastructure belongs exclusively to the Infrastructure Layer.

---

## Public Mutable State

Aggregates shall never expose mutable internal collections or mutable internal state.

All state changes shall occur through explicit business operations.

---

# End of Part 3

---

# 20. Implementation Guidelines

Enterprise Aggregates shall be implemented according to the architectural principles defined in EA-300 and EA-301.

Implementation shall ensure

- one clearly defined Aggregate Root
- explicit business behaviour
- protected business invariants
- transactional consistency
- high cohesion
- low coupling
- persistence ignorance
- technology independence

Business operations shall be expressed as meaningful domain methods.

Aggregate implementations shall never expose internal implementation details.

Changes to Aggregate structure shall preserve business semantics and maintain backward compatibility where appropriate.

---

# 21. Architecture Compliance

Enterprise Aggregate implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- this Enterprise Aggregate Architecture Standard

Architecture reviews shall verify

- Aggregate boundaries
- Aggregate Root responsibilities
- invariant enforcement
- transaction boundaries
- dependency compliance
- Aggregate size
- persistence independence
- Domain Event publication
- documentation completeness

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 22. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-300 compliance verified | ☐ |
| EA-301 compliance verified | ☐ |
| Aggregate Root identified | ☐ |
| Aggregate boundary documented | ☐ |
| Business invariants documented | ☐ |
| Transaction boundary verified | ☐ |
| Aggregate references use business identifiers only | ☐ |
| Aggregate remains persistence ignorant | ☐ |
| Domain Events identified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Aggregate shall satisfy all mandatory compliance requirements before being released into production.

---

# 23. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-303 Enterprise Entity Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard

---

# 24. Summary

This standard defines how Enterprise Aggregates shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Aggregates are the authoritative consistency and transactional boundaries within the Domain Layer.

This standard establishes

- Aggregate Root responsibilities
- consistency boundaries
- transaction boundaries
- business invariant protection
- Aggregate lifecycle
- concurrency management
- persistence rules
- collaboration principles
- implementation guidance
- compliance requirements

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This standard shall be regarded as the authoritative Enterprise Aggregate Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
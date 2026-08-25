# EA-303 Enterprise Entity Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-303 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Entity Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Entities |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Entity Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Entity Architecture aligned with EA-020, EA-111, EA-300, EA-301 and EA-302 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-301 | Enterprise Domain Architecture Standard |
| EA-302 | Enterprise Aggregate Architecture Standard |
| EA-304 | Enterprise Value Object Architecture Standard |
| EA-305 | Enterprise Domain Service Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-309 | Enterprise Domain Event Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Entities.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Entities shall be designed, implemented and governed within the MFM Enterprise Platform.

An Entity represents a business object whose identity remains constant throughout its lifecycle, even when its attributes change.

Entities encapsulate business behaviour while preserving a stable business identity.

---

# 2. Scope

This standard applies to every Entity within every Enterprise Aggregate.

It governs

- Entity identity
- Entity lifecycle
- Entity state
- Entity behaviour
- Entity ownership
- Entity relationships
- Entity validation
- Entity evolution

Persistence implementation details are outside the scope of this standard.

---

# 3. Definition of an Entity

An Entity is a business object distinguished by its identity rather than by the values of its attributes.

Every Entity shall

- possess a stable identity
- belong to exactly one Aggregate
- encapsulate business behaviour
- maintain valid business state
- participate in Aggregate consistency

Entities shall never exist independently of an Aggregate unless explicitly approved by Enterprise Architecture.

---

# 4. Entity Objectives

Every Entity shall

- represent a meaningful business concept
- preserve business identity
- encapsulate business behaviour
- maintain valid state
- support Aggregate consistency
- remain cohesive
- minimise unnecessary dependencies

Business meaning shall always take precedence over technical implementation.

---

# 5. Entity Identity

Identity is the defining characteristic of an Entity.

Entity identity

- is immutable
- uniquely identifies the Entity
- survives attribute changes
- survives state transitions
- distinguishes one Entity from another

Identity shall never be derived from mutable business attributes.

Entity identity shall remain stable throughout the complete lifecycle of the Entity.

---

# End of Part 1

---

# 6. Entity State

Every Entity maintains business state throughout its lifecycle.

Entity state

- represents current business information
- evolves through business operations
- remains internally consistent
- supports business decision making

State changes shall occur only through explicit business behaviour.

Direct modification of internal state from outside the Entity is prohibited.

Every state transition shall preserve Aggregate consistency.

---

# 7. Identity versus Equality

Entity identity and Entity equality are distinct concepts.

Identity determines whether two references represent the same business object.

Equality compares identity rather than attribute values.

Two Entity instances with identical attributes shall not be considered equal unless they represent the same business identity.

Examples

- Two members with identical names remain different Entities.
- Two invoices with identical amounts remain different Entities.
- Two vessels with identical specifications remain different Entities.

Identity is authoritative.

Business attributes are descriptive.

---

# 8. Entity Behaviour

Entities shall encapsulate business behaviour related to their own responsibilities.

Business behaviour shall

- validate business rules
- modify Entity state
- protect business integrity
- collaborate with other objects inside the Aggregate
- preserve Aggregate invariants

Entities shall never expose setters that bypass business validation.

Business behaviour shall be expressed through meaningful domain operations.

---

# 9. Entity Ownership

Every Entity shall belong to exactly one Aggregate.

Ownership is exclusive.

The Aggregate Root

- creates Entities
- removes Entities
- coordinates Entity collaboration
- protects Entity integrity
- controls Entity visibility

Entities shall never be shared between Aggregates.

Entity ownership shall remain stable throughout the Entity lifecycle.

---

# 10. Entity Relationships

Relationships between Entities shall be explicit and meaningful.

Allowed relationships include

- parent-child relationships
- ownership relationships
- composition
- collaboration within the same Aggregate

Relationships shall never violate Aggregate boundaries.

References to Entities in other Aggregates are prohibited.

Cross-Aggregate communication shall occur through Aggregate Roots.

---

# 11. Entity Validation

Entities are responsible for validating their own business rules.

Validation shall ensure

- valid business state
- legal state transitions
- business rule compliance
- consistency with Aggregate invariants

Technical validation

- database constraints
- serialization
- framework validation
- transport validation

shall remain outside the Entity.

Business validation belongs exclusively within the Domain Layer.

---

# 12. Entity Collaboration

Entities may collaborate only within the Aggregate that owns them.

Collaboration shall

- support Aggregate behaviour
- preserve Aggregate consistency
- remain coordinated by the Aggregate Root
- avoid hidden dependencies

Entities shall never coordinate business processes across multiple Aggregates.

Cross-Aggregate collaboration belongs to Application Services, Domain Events or Enterprise Workflows.

---

# End of Part 2

---

# 13. Entity Lifecycle

Every Entity shall follow a controlled business lifecycle.

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
Modify        Business Validation
   │               │
   └───────┬───────┘
           ▼
      Persist State
           │
           ▼
      Archive/Delete
```

Entity lifecycle transitions shall occur only through explicit business behaviour.

Every transition shall preserve both Entity validity and Aggregate consistency.

An Entity shall never enter an invalid business state.

---

# 14. Mutable State

Unlike Value Objects, Entities maintain mutable business state.

Mutable state shall

- represent legitimate business evolution
- remain internally consistent
- preserve Entity identity
- comply with business rules

Mutability shall be controlled through business operations.

Public modification of Entity attributes is prohibited.

All mutations shall be validated before becoming effective.

---

# 15. Concurrency

Concurrent modification of Entities shall be governed by the owning Aggregate.

Entities shall not implement independent concurrency mechanisms.

Concurrency control shall

- preserve Aggregate consistency
- prevent conflicting business updates
- maintain deterministic outcomes

Concurrency responsibilities belong to the Aggregate Root and Repository implementation.

Business behaviour shall remain independent of persistence technology.

---

# 16. Business Rules

Entities shall enforce business rules that are specific to their own responsibilities.

Business rules may include

- state transitions
- attribute constraints
- ownership validation
- lifecycle validation
- business permissions
- consistency requirements

Business rules affecting the entire Aggregate shall be enforced by the Aggregate Root.

Business rules spanning multiple Aggregates belong outside the Entity.

---

# 17. Architectural Constraints

Enterprise Entities shall comply with the following architectural constraints.

Entities shall

- maintain stable identity
- encapsulate business behaviour
- protect valid business state
- remain persistence ignorant
- belong to one Aggregate only

Entities shall never

- access repositories
- execute SQL
- invoke external services
- perform workflow orchestration
- contain presentation logic
- communicate directly with other Aggregates

These constraints preserve Domain integrity and maintain clear architectural responsibilities.

---

# 18. Entity Quality Attributes

Enterprise Entities shall be designed to achieve

- correctness
- maintainability
- readability
- cohesion
- traceability
- testability
- business integrity
- long-term evolvability

Architectural decisions shall always prioritise business correctness over technical optimisation.

---

# 19. Entity Anti-Patterns

The following Entity anti-patterns are prohibited.

## Anemic Entity

Entities shall not become passive data containers.

Business behaviour belongs inside the Entity whenever it concerns the Entity's own responsibilities.

---

## Mutable Identity

Entity identity shall never change after creation.

Changing identity invalidates business traceability.

---

## Shared Entity

Entities shall never be shared between multiple Aggregates.

Exclusive ownership is mandatory.

---

## Infrastructure Leakage

Entities shall never contain

- SQL
- ORM-specific behaviour
- HTTP clients
- messaging APIs
- dependency injection
- file system access

Infrastructure responsibilities belong exclusively to the Infrastructure Layer.

---

## Public State Mutation

Entities shall never expose public mutable state.

Business state shall only change through explicit business operations that enforce business rules.

---

# End of Part 3

---

# 20. Implementation Guidelines

Enterprise Entities shall be implemented according to the architectural principles defined in EA-300, EA-301 and EA-302.

Implementation shall ensure

- immutable business identity
- explicit business behaviour
- controlled state transitions
- protection of business rules
- Aggregate ownership
- persistence ignorance
- technology independence

Entities shall expose business operations instead of attribute manipulation.

All business state changes shall occur through methods that preserve Entity validity and Aggregate consistency.

Entity implementations shall remain focused on business responsibilities.

---

# 21. Architecture Compliance

Enterprise Entity implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- this Enterprise Entity Architecture Standard

Architecture reviews shall verify

- Entity identity
- Aggregate ownership
- business behaviour
- business rule enforcement
- dependency compliance
- persistence independence
- architectural consistency
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
| EA-302 compliance verified | ☐ |
| Stable Entity identity defined | ☐ |
| Aggregate ownership documented | ☐ |
| Business behaviour implemented | ☐ |
| Business rules validated | ☐ |
| No infrastructure dependencies | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Entity shall satisfy all mandatory compliance requirements before being released into production.

---

# 23. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-301 Enterprise Domain Architecture Standard
- EA-302 Enterprise Aggregate Architecture Standard
- EA-304 Enterprise Value Object Architecture Standard
- EA-305 Enterprise Domain Service Architecture Standard
- EA-306 Enterprise Repository Architecture Standard
- EA-309 Enterprise Domain Event Architecture Standard

---

# 24. Summary

This standard defines how Enterprise Entities shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Entities represent business objects whose identity remains constant throughout their lifecycle while their business state evolves through controlled behaviour.

This standard establishes

- Entity identity
- Entity ownership
- business behaviour
- state management
- lifecycle rules
- validation responsibilities
- architectural constraints
- implementation guidance
- compliance requirements

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This standard shall be regarded as the authoritative Enterprise Entity Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
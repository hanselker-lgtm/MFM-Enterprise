# EA-309 Enterprise Domain Event Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-309 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Domain Event Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Domain Events |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Domain Event Architecture | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Domain Event Architecture aligned with EA-020, EA-111, EA-112, EA-300, EA-301, EA-302, EA-303, EA-304, EA-305, EA-306, EA-307 and EA-308 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-301 | Enterprise Domain Architecture Standard |
| EA-302 | Enterprise Aggregate Architecture Standard |
| EA-303 | Enterprise Entity Architecture Standard |
| EA-304 | Enterprise Value Object Architecture Standard |
| EA-305 | Enterprise Domain Service Architecture Standard |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-307 | Enterprise Specification Architecture Standard |
| EA-308 | Enterprise Factory Architecture Standard |

---

# Architecture Compliance

This standard defines the architectural requirements governing Enterprise Domain Events.

General Enterprise Event Architecture principles are inherited from EA-112.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise Domain Events shall be designed, implemented and governed within the MFM Enterprise Platform.

Domain Events represent business facts describing something that has already occurred within the Domain.

Domain Events enable loose coupling between Aggregates, Domain Services and other Domain components while preserving business meaning.

---

# 2. Scope

This standard applies to every Domain Event within every Enterprise Domain.

It governs

- Domain Event definition
- event structure
- event publication
- event immutability
- naming
- versioning
- lifecycle
- governance

Infrastructure messaging mechanisms are outside the scope of this standard.

---

# 3. Definition of a Domain Event

A Domain Event represents a completed business occurrence that is significant to the Enterprise Domain.

A Domain Event shall

- represent a past business fact
- be immutable
- express business meaning
- belong to one Enterprise Domain
- support business traceability

A Domain Event shall never represent a future intention or a technical notification.

---

# 4. Domain Event Objectives

Every Domain Event shall

- communicate completed business facts
- preserve business intent
- improve Domain decoupling
- support business traceability
- enable event-driven collaboration

Domain Events describe what happened—not what should happen.

---

# 5. Domain Event Responsibilities

Domain Events are responsible for

- describing completed business occurrences
- carrying relevant business information
- enabling Domain collaboration
- supporting auditability
- preserving historical accuracy

Domain Events shall never

- execute business behaviour
- contain business logic
- invoke infrastructure services
- modify Domain state

Domain Events communicate business facts.

They do not perform business actions.

---

# End of Part 1

---

# 6. Event Structure

Every Domain Event shall expose a well-defined business-oriented structure.

A Domain Event shall contain

- event identifier
- event name
- event occurrence timestamp
- Aggregate identifier
- business payload
- event version

Optional metadata may include

- correlation identifier
- causation identifier
- tenant identifier
- business context

Technical implementation details shall remain outside the Domain Event definition.

---

# 7. Event Immutability

Enterprise Domain Events shall be immutable.

Once created, a Domain Event shall never be modified.

Immutability preserves

- historical accuracy
- auditability
- consistency
- traceability
- replayability

If business information changes, a new Domain Event shall be published rather than modifying an existing event.

---

# 8. Event Naming

Domain Event names shall represent completed business occurrences.

Event names shall

- use past tense
- express business meaning
- use ubiquitous language
- remain stable over time

Examples include

- MemberRegistered
- MembershipRenewed
- VesselRegistered
- MaintenanceCompleted
- InvoicePaid
- VoyageCompleted

Technical names such as

- SaveCompleted
- DatabaseUpdated
- InsertExecuted
- ProcessFinished

shall never be used as Domain Event names.

---

# 9. Aggregate Integration

Aggregate Roots are responsible for producing Domain Events whenever significant business state changes occur.

Domain Events shall

- originate from Aggregate behaviour
- preserve Aggregate consistency
- represent completed business facts
- be published only after successful business execution

Aggregates shall never publish events describing unsuccessful business operations.

---

# 10. Event Publication

Domain Events shall be published only after the successful completion of the business operation they describe.

Publication shall

- preserve business consistency
- maintain ordering within the Aggregate
- support reliable delivery
- preserve historical correctness

Publication mechanisms belong outside the Domain Layer.

The Domain Layer defines the event.

The Infrastructure Layer delivers the event.

---

# 11. Event Payload Design

Event payloads shall contain only information required to describe the completed business occurrence.

Payloads shall

- contain business data
- avoid unnecessary duplication
- remain technology independent
- preserve business meaning

Payloads shall never include

- ORM entities
- database sessions
- infrastructure objects
- presentation models

Business data shall remain independent of implementation technology.

---

# 12. Dependency Rules

Domain Events may depend upon

- Domain identifiers
- Value Objects
- immutable business data

Domain Events shall never depend upon

- SQL
- ORM frameworks
- messaging infrastructure
- dependency injection
- user interfaces
- external APIs

Dependencies shall always preserve Domain purity and technology independence.

---

# End of Part 2

---

# 13. Event Lifecycle

Every Domain Event shall follow a well-defined architectural lifecycle.

```text
Business Operation
         │
         ▼
Business State Changes
         │
         ▼
Domain Event Created
         │
         ▼
Event Published
         │
         ▼
Event Processed
         │
         ▼
Event Archived
```

The lifecycle shall preserve the historical integrity of the business occurrence.

A published Domain Event shall never be altered or withdrawn.

---

# 14. Event Versioning

Enterprise Domain Events shall support explicit versioning.

Versioning shall

- preserve backward compatibility whenever practical
- support event evolution
- minimise breaking changes
- maintain historical interpretation

New optional payload attributes may be introduced without changing the event identity.

Breaking changes shall require a new event version or a new event type.

Event consumers shall explicitly handle supported event versions.

---

# 15. Event Ordering

Events originating from the same Aggregate shall preserve chronological order.

Ordering shall

- reflect the sequence of completed business operations
- preserve business consistency
- support deterministic event processing
- maintain historical correctness

Ordering across different Aggregates is not guaranteed unless explicitly defined by the surrounding business process.

Consumers shall not assume global ordering of all Domain Events.

---

# 16. Architectural Constraints

Enterprise Domain Events shall comply with the following architectural constraints.

Domain Events shall

- be immutable
- represent completed business facts
- use ubiquitous language
- remain technology independent
- preserve business meaning
- contain only relevant business information

Domain Events shall never

- contain business logic
- modify Domain state
- invoke external services
- expose infrastructure dependencies
- represent technical implementation details

These constraints preserve the separation between business facts and business behaviour.

---

# 17. Domain Event Quality Attributes

Enterprise Domain Events shall be designed to achieve

- correctness
- immutability
- traceability
- readability
- auditability
- maintainability
- technology independence
- business clarity

Business meaning shall always take precedence over technical optimisation.

Domain Events shall remain stable representations of completed business facts.

---

# 18. Domain Event Anti-Patterns

The following architectural anti-patterns are prohibited.

## Command as Event

A Domain Event shall never express an intention or request.

Examples include

- RegisterMember
- CreateInvoice
- StartMaintenance

These represent commands rather than completed business facts.

---

## Mutable Event

Published Domain Events shall never be modified.

Corrections shall be represented by publishing new Domain Events.

---

## Technical Event

Technical infrastructure notifications shall never be modelled as Domain Events.

Examples include

- DatabaseSaved
- CacheUpdated
- MessageQueued
- TransactionCommitted

Domain Events shall represent business occurrences only.

---

## Infrastructure Leakage

Domain Events shall never contain

- ORM entities
- SQL statements
- database connections
- HTTP clients
- messaging APIs
- dependency injection
- framework-specific logic

Infrastructure concerns belong exclusively to the Infrastructure Layer.

---

## Excessive Payload

Domain Events shall not contain unnecessary or redundant information.

Payloads shall include only the business information required to understand the completed business occurrence.

---

# End of Part 3

---

# 19. Implementation Guidelines

Enterprise Domain Event implementations shall be developed according to the architectural principles defined in EA-112, EA-300, EA-301, EA-302, EA-303, EA-304, EA-305, EA-306, EA-307 and EA-308.

Implementation shall ensure

- immutable event instances
- business-oriented event names
- complete business traceability
- technology-independent event definitions
- stable event contracts
- clear Aggregate integration
- Domain purity

Domain Events shall expose only the information necessary to describe the completed business occurrence.

Implementation details shall never influence business semantics.

---

# 20. Architecture Compliance

Enterprise Domain Event implementations shall comply with

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
- this Enterprise Domain Event Architecture Standard

Architecture reviews shall verify

- immutable implementation
- business-oriented naming
- event payload correctness
- dependency compliance
- Aggregate integration
- Domain purity
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
| Immutable implementation verified | ☐ |
| Business-oriented event naming verified | ☐ |
| Event payload validated | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Domain Event shall satisfy all mandatory compliance requirements before being released into production.

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

---

# 23. Summary

This standard defines how Enterprise Domain Events shall be designed, implemented and governed throughout the MFM Enterprise Platform.

Enterprise Domain Events represent immutable business facts describing completed business occurrences while enabling loose coupling, traceability and event-driven collaboration across the Enterprise Domain.

This standard establishes

- Domain Event definition
- immutable event design
- business-oriented event naming
- event payload design
- Aggregate integration
- publication principles
- versioning
- ordering
- architectural constraints
- implementation guidance
- governance requirements
- compliance requirements

General Enterprise Event Architecture principles are inherited from EA-112.

General Domain-Driven Design principles are inherited from EA-300.

Enterprise Domain architecture is inherited from EA-301.

Aggregate ownership principles are inherited from EA-302.

Entity responsibilities are inherited from EA-303.

Value Object principles are inherited from EA-304.

Domain Service responsibilities are inherited from EA-305.

Repository responsibilities are inherited from EA-306.

Specification responsibilities are inherited from EA-307.

Factory responsibilities are inherited from EA-308.

Enterprise-wide architectural requirements are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

This standard shall be regarded as the authoritative Enterprise Domain Event Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
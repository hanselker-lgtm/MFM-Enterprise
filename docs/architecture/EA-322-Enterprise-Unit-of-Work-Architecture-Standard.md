# EA-322 Enterprise Unit of Work Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-322 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Unit of Work Architecture Standard |
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
| 1.x | Previous | Legacy Unit of Work Guidance | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete Enterprise Unit of Work Architecture aligned with EA-020, EA-111, EA-112, EA-300, EA-310, EA-320 and EA-321 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-300 | Enterprise Domain-Driven Design Reference Architecture |
| EA-306 | Enterprise Repository Architecture Standard |
| EA-310 | Enterprise Application Layer Reference Architecture |
| EA-320 | Enterprise Infrastructure Layer Reference Architecture |
| EA-321 | Enterprise Persistence Architecture Standard |
| EA-323 | Enterprise Database Architecture Standard |

---

# Architecture Compliance

This standard defines the Enterprise Unit of Work Architecture.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Domain-Driven Design principles are inherited from EA-300.

Application Layer principles are inherited from EA-310.

Infrastructure Layer principles are inherited from EA-320.

Persistence Architecture principles are inherited from EA-321.

All Enterprise Unit of Work implementations shall conform to this standard.

---

# 1. Purpose

The purpose of this standard is to define how Enterprise transactions shall be coordinated throughout the MFM Enterprise Platform.

The Unit of Work Architecture shall

- coordinate persistence operations
- preserve Aggregate consistency
- ensure transactional integrity
- support atomic execution
- provide reliable commit and rollback behaviour
- isolate transaction management from business logic

Unit of Work shall remain an Infrastructure Layer responsibility.

---

# 2. Scope

This standard applies to every Unit of Work implementation throughout the Enterprise Platform.

It governs

- transaction coordination
- Repository coordination
- persistence context integration
- commit processing
- rollback processing
- transaction lifecycle
- concurrency coordination
- dependency rules

The standard applies regardless of database or persistence technology.

---

# 3. Unit of Work Definition

A Unit of Work coordinates all persistence operations performed during a single business transaction.

A Unit of Work is responsible for

- tracking persistence operations
- coordinating Repository activity
- managing transaction boundaries
- committing changes
- rolling back failed operations

A Unit of Work shall represent exactly one transactional boundary.

---

# 4. Unit of Work Objectives

Enterprise Unit of Work implementations shall

- preserve transactional consistency
- coordinate multiple Repository operations
- support reliable commit processing
- support reliable rollback processing
- minimise transaction duration
- ensure deterministic transaction behaviour
- support technology independence

Transaction coordination shall remain transparent to the Domain Layer.

---

# 5. Unit of Work Responsibilities

The Unit of Work is responsible for

- transaction coordination
- Repository coordination
- persistence context coordination
- commit processing
- rollback processing
- concurrency participation
- resource coordination

The Unit of Work shall never

- implement business rules
- enforce business policies
- perform Domain decision making
- expose persistence technology to higher architectural layers

Business behaviour remains exclusively within the Domain Layer.

---

# End of Part 1

---

# 6. Unit of Work Structure

The Enterprise Unit of Work coordinates all persistence activities within a single business transaction.

A Unit of Work consists of

- transaction coordination
- Repository coordination
- persistence context management
- change tracking
- commit processing
- rollback processing
- resource coordination

Each Unit of Work shall represent one complete transactional boundary.

The Unit of Work shall remain an Infrastructure Layer component.

---

# 7. Repository Coordination

A Unit of Work coordinates all Repository operations participating in the same business transaction.

Repository coordination shall ensure

- consistent Aggregate persistence
- ordered persistence operations
- transaction participation
- coordinated commit
- coordinated rollback

Repositories shall never coordinate transactions independently.

Transaction coordination shall remain the responsibility of the Unit of Work.

---

# 8. Persistence Context Integration

The Unit of Work shall integrate with the Enterprise Persistence Context.

The Persistence Context shall

- track Aggregate instances
- monitor state changes
- manage object identity
- coordinate persistence operations
- participate in transaction processing

The Unit of Work shall coordinate the Persistence Context without exposing implementation details to higher architectural layers.

---

# 9. Transaction Coordination

Every Unit of Work shall coordinate exactly one business transaction.

Transaction coordination includes

- transaction creation
- transaction participation
- transaction completion
- transaction rollback
- transaction disposal

Nested business transactions shall be avoided unless explicitly supported by the underlying persistence technology and approved through Enterprise Architecture governance.

---

# 10. Commit Processing

Commit processing shall persist all approved changes as a single atomic operation.

Commit processing shall

- validate transaction state
- coordinate Repository operations
- flush pending persistence operations
- commit the transaction
- release allocated resources

A successful commit shall guarantee that all participating persistence operations have been completed consistently.

Partial commits are prohibited.

---

# 11. Rollback Processing

Rollback processing shall restore the persistence environment to its original consistent state following a failed transaction.

Rollback processing shall

- cancel pending persistence operations
- roll back the transaction
- discard uncommitted changes
- release allocated resources
- preserve diagnostic information

Rollback operations shall execute automatically whenever transactional consistency cannot be guaranteed.

---

# 12. Aggregate Consistency

The Unit of Work shall preserve Aggregate consistency throughout transaction execution.

The Unit of Work shall ensure

- Aggregate invariants remain protected
- Aggregate boundaries are respected
- persistence occurs atomically
- transactional consistency is maintained

Multiple Aggregates may participate in the same Unit of Work where required by the business transaction.

Aggregate consistency shall never be compromised by transaction management.

---

# 13. Dependency Rules

The Unit of Work shall comply with Enterprise dependency inversion principles.

The Unit of Work may depend upon

- Repository implementations
- persistence providers
- transaction managers
- Persistence Context implementations
- Infrastructure services

Higher architectural layers shall never depend directly upon

- transaction implementations
- persistence providers
- ORM frameworks
- database transaction mechanisms

Dependency direction shall always point toward abstractions defined by higher architectural layers.

---

# End of Part 2

---

# 14. Unit of Work Lifecycle

Every Enterprise Unit of Work shall follow a well-defined lifecycle.

```text
Unit of Work Created
          │
          ▼
Persistence Context Established
          │
          ▼
Repositories Participate
          │
          ▼
Changes Tracked
          │
          ▼
Commit or Rollback
          │
          ▼
Resources Released
```

The Unit of Work lifecycle shall

- establish transaction boundaries
- coordinate Repository participation
- track persistence operations
- complete commit or rollback
- dispose allocated resources

Each Unit of Work shall exist only for the duration of a single business transaction.

---

# 15. Concurrency Coordination

The Unit of Work shall coordinate concurrent persistence operations safely.

Concurrency management may include

- optimistic concurrency
- concurrency tokens
- version identifiers
- transaction isolation levels
- conflict detection

The Unit of Work shall

- detect conflicting updates
- prevent lost updates
- preserve Aggregate consistency
- support deterministic transaction outcomes

Concurrency mechanisms shall remain transparent to higher architectural layers.

---

# 16. Error Handling

The Unit of Work shall handle transaction failures consistently.

Typical failures include

- transaction failures
- Repository failures
- persistence failures
- concurrency conflicts
- timeout conditions
- infrastructure failures
- connection failures

The Unit of Work shall

- preserve diagnostic information
- initiate rollback where required
- release allocated resources
- propagate technical exceptions through Enterprise exception handling mechanisms

Business decisions shall never be made during transaction error handling.

---

# 17. Performance Optimisation

Unit of Work implementations shall support efficient transaction processing.

Performance optimisation may include

- efficient change tracking
- batched persistence operations
- connection reuse
- transaction optimisation
- asynchronous persistence where appropriate
- efficient resource allocation

Performance optimisation shall never compromise

- transactional integrity
- Aggregate consistency
- correctness
- auditability
- architectural compliance

Transactions should remain as short-lived as practical.

---

# 18. Security

Unit of Work implementations shall enforce Enterprise security requirements.

Security responsibilities include

- secure transaction handling
- credential protection
- secure persistence communication
- protected transaction context
- audit integration
- secure resource management

Sensitive transaction information shall never

- be exposed through exception messages
- be written to logs without appropriate protection
- be transmitted insecurely
- be stored outside approved persistence mechanisms

Unit of Work security shall align with Enterprise security policies.

---

# 19. Quality Attributes

Enterprise Unit of Work implementations shall achieve

- reliability
- consistency
- durability
- maintainability
- scalability
- recoverability
- observability
- resilience
- technology independence

The Unit of Work shall remain transparent to Domain and Application logic.

---

# 20. Architectural Constraints

Unit of Work implementations shall comply with the following constraints.

The Unit of Work shall

- coordinate one business transaction
- preserve Aggregate consistency
- coordinate Repository operations
- manage commit and rollback
- isolate transaction management

The Unit of Work shall never

- implement business rules
- expose transaction technology
- enforce business policies
- bypass Repository abstractions
- introduce dependencies into higher architectural layers

These constraints preserve long-term architectural integrity.

---

# 21. Unit of Work Anti-Patterns

The following architectural anti-patterns are prohibited.

## Business Logic in Unit of Work

The Unit of Work shall never implement business behaviour.

Business logic belongs exclusively within the Domain Layer.

---

## Repository-managed Transactions

Repositories shall never manage transactions independently.

Transaction coordination belongs exclusively to the Unit of Work.

---

## Long-running Transactions

Business transactions shall remain as short-lived as practical.

Long-running transactions increase the risk of contention, resource exhaustion and inconsistent behaviour.

---

## Partial Commit

A Unit of Work shall never commit only part of a business transaction.

Commit operations shall remain atomic.

---

## Transaction Leakage

Transaction implementation details shall never be exposed outside the Infrastructure Layer.

Dependency inversion shall always be preserved.

---

## Infrastructure-driven Business Decisions

Transaction failures shall never determine business behaviour.

Business decisions remain the responsibility of the Domain Layer.

---

# End of Part 3

---

# 22. Implementation Guidelines

Enterprise Unit of Work implementations shall follow the architectural principles defined in EA-020, EA-111, EA-112, EA-300, EA-310, EA-320 and EA-321.

Implementation shall ensure

- one Unit of Work per business transaction
- Repository coordination through a single transaction boundary
- deterministic commit processing
- deterministic rollback processing
- Aggregate consistency
- technology independence
- dependency inversion
- secure transaction management
- efficient resource utilisation
- operational observability

Unit of Work implementations shall remain transparent to the Domain Layer and Application Layer.

Transaction management shall never influence Enterprise business behaviour.

---

# 23. Architecture Compliance

Enterprise Unit of Work implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-306 Enterprise Repository Architecture Standard
- EA-310 Enterprise Application Layer Reference Architecture
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-321 Enterprise Persistence Architecture Standard
- this Enterprise Unit of Work Architecture Standard

Architecture reviews shall verify

- transaction coordination
- Repository coordination
- commit processing
- rollback processing
- Aggregate consistency
- Persistence Context integration
- dependency inversion
- technology independence
- security compliance
- documentation completeness

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 24. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-300 compliance verified | ☐ |
| EA-306 compliance verified | ☐ |
| EA-310 compliance verified | ☐ |
| EA-320 compliance verified | ☐ |
| EA-321 compliance verified | ☐ |
| Transaction coordination verified | ☐ |
| Repository coordination verified | ☐ |
| Commit processing verified | ☐ |
| Rollback processing verified | ☐ |
| Aggregate consistency verified | ☐ |
| Dependency inversion verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Unit of Work implementation shall satisfy all mandatory compliance requirements before being released into production.

---

# 25. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-300 Enterprise Domain-Driven Design Reference Architecture
- EA-306 Enterprise Repository Architecture Standard
- EA-310 Enterprise Application Layer Reference Architecture
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-321 Enterprise Persistence Architecture Standard
- EA-323 Enterprise Database Architecture Standard
- EA-324 Enterprise ORM Architecture Standard

---

# 26. Summary

This standard defines the Enterprise Unit of Work Architecture for the MFM Enterprise Platform.

The Unit of Work Architecture coordinates all persistence operations performed within a single business transaction while preserving Aggregate consistency, transactional integrity and technology independence.

This standard establishes

- Unit of Work principles
- transaction coordination
- Repository coordination
- Persistence Context integration
- commit processing
- rollback processing
- Aggregate consistency
- dependency rules
- lifecycle management
- concurrency coordination
- error handling
- performance optimisation
- security requirements
- quality attributes
- architectural constraints
- implementation guidance
- governance requirements
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Domain-Driven Design principles are inherited from EA-300.

Application Layer principles are inherited from EA-310.

Infrastructure Layer principles are inherited from EA-320.

Persistence Architecture principles are inherited from EA-321.

This standard shall be regarded as the authoritative Enterprise Unit of Work Architecture Standard for the MFM Enterprise Platform.

---

# End of Document
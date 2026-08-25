# EA-285 Enterprise Event Messaging Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-285 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Event Messaging Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Messaging Components |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Messaging Standard | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete consolidation aligned with EA-020, EA-112 and EA-293 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-293 | Enterprise Event Distribution Architecture Standard |
| EA-286 | Enterprise Message Broker Architecture Standard |
| EA-287 | Enterprise Event Bus Architecture Standard |
| EA-288 | Enterprise Queue Architecture Standard |
| EA-289 | Enterprise Event Stream Architecture Standard |
| EA-290 | Enterprise Topic Architecture Standard |
| EA-291 | Enterprise Channel Architecture Standard |
| EA-292 | Enterprise Subscription Architecture Standard |

---

# Architecture Compliance

This standard shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture
- EA-293 Enterprise Event Distribution Architecture Standard

This document defines only the responsibilities specific to Enterprise Event Messaging Architecture.

Common architectural requirements are inherited from EA-020.

Common Enterprise Event Architecture is inherited from EA-112.

Distribution responsibilities are inherited from EA-293.

---

# 1. Purpose

The purpose of this standard is to define the architectural principles, responsibilities, constraints and interfaces governing the Enterprise Messaging Layer within the MFM Enterprise Platform.

The Messaging Layer provides reliable, scalable and technology-independent message transportation between enterprise components.

Messaging is responsible for transporting messages.

Messaging is not responsible for business orchestration, technical processing, routing decisions or business logic.

---

# 2. Scope

This standard applies to all enterprise messaging implementations.

Examples include

- message brokers
- event buses
- queues
- event streams
- topics
- channels
- subscriptions

This standard does not apply to

- business workflows
- pipeline coordination
- technical processing
- routing decisions
- message distribution
- business capabilities

Those responsibilities are defined in their respective Enterprise Architecture Standards.

---

# 3. Architectural Position

This standard defines the architecture of the Enterprise Messaging Layer.

Within the Enterprise Architecture the Messaging Layer begins where Distribution ends.

The Messaging Layer provides the transport mechanisms required for reliable communication between enterprise components.

---

# 4. Out of Scope

The following responsibilities are outside the scope of this standard

- business orchestration
- business rules
- technical processing
- routing decisions
- message distribution
- domain modelling
- persistence

---

# 5. Responsibilities

The Messaging Layer is responsible for

- transporting enterprise messages
- providing reliable message delivery
- supporting asynchronous communication
- supporting scalable message transport
- supporting decoupled communication
- providing delivery guarantees

The Messaging Layer shall never

- execute business logic
- perform technical processing
- determine routing decisions
- orchestrate business workflows
- implement domain behaviour

---

# End of Part 1

---

# 6. Messaging Architecture

The Enterprise Messaging Layer provides the common transport infrastructure for asynchronous communication throughout the MFM Enterprise Platform.

The Messaging Layer is responsible for transporting messages between enterprise components while remaining independent of business processes and business logic.

Messaging components shall provide reliable, scalable and loosely coupled communication.

---

# 7. Messaging Components

An Enterprise Messaging implementation may consist of the following logical components.

## Message Broker

Provides centralized message management.

Responsibilities

- broker connections
- message acceptance
- message forwarding
- delivery coordination
- broker configuration

---

## Event Bus

Provides event propagation across enterprise components.

Responsibilities

- event publication
- event propagation
- event consumption
- event registration

---

## Queue

Provides reliable sequential message storage.

Responsibilities

- message buffering
- ordered delivery
- acknowledgement handling
- retry support

---

## Event Stream

Provides continuous event transportation.

Responsibilities

- ordered event streaming
- event replay
- stream management
- stream consumption

---

## Topic

Provides publish-subscribe communication.

Responsibilities

- topic management
- publication endpoints
- subscriber registration
- event categorization

---

## Channel

Provides logical communication paths.

Responsibilities

- communication separation
- endpoint abstraction
- channel configuration
- transport isolation

---

## Subscription

Represents consumer interest in one or more event sources.

Responsibilities

- subscription registration
- filtering configuration
- delivery preferences
- subscription lifecycle

---

# 8. Interfaces

The Messaging Layer communicates exclusively through approved architectural interfaces.

The Messaging Layer may receive

- Distribution Requests
- Routed Events
- Delivery Metadata
- Technical Configuration

The Messaging Layer may expose

- Message Publication
- Event Publication
- Queue Submission
- Stream Publication
- Subscription Registration

The Messaging Layer shall never communicate directly with

- Workflow
- Pipeline
- Processing
- Domain Aggregates
- User Interfaces
- Repositories

Communication shall occur exclusively through the Distribution layer.

---

# 9. Messaging Operation

The Messaging Layer performs the technical transportation of enterprise messages.

Typical messaging operations include

- accepting delivery requests
- validating messaging configuration
- selecting messaging components
- transporting messages
- confirming delivery
- reporting messaging status

The Messaging Layer shall not evaluate routing policies.

The Messaging Layer shall not determine message destinations.

---

# 10. Interaction with Other Standards

| Standard | Relationship |
|----------|--------------|
| EA-293 Distribution | Supplies delivery requests to the Messaging Layer |
| EA-286 Message Broker | Defines broker architecture |
| EA-287 Event Bus | Defines enterprise event bus architecture |
| EA-288 Queue | Defines queue architecture |
| EA-289 Event Stream | Defines stream architecture |
| EA-290 Topic | Defines topic architecture |
| EA-291 Channel | Defines channel architecture |
| EA-292 Subscription | Defines subscription architecture |
| EA-020 | Common architectural requirements |
| EA-112 | Enterprise Event Reference Architecture |

---

# End of Part 2

---

# 11. Messaging Lifecycle

Every Messaging component shall follow a defined operational lifecycle.

```text
Created
    │
    ▼
Configured
    │
    ▼
Available
    │
    ▼
Processing
    │
    ▼
Completed
```

Alternative operational states include

- Paused
- Failed
- Stopped

Each lifecycle transition shall be validated.

Invalid lifecycle transitions shall be rejected.

---

# 12. Messaging Execution Model

The standard messaging execution sequence is illustrated below.

```text
Distribution
      │
      ▼
Messaging Layer
      │
      ▼
Select Messaging Component
      │
      ▼
Transport Message
      │
      ▼
Receive Delivery Confirmation
      │
      ▼
Return Messaging Result
```

The Messaging Layer is responsible exclusively for transporting enterprise messages.

The Messaging Layer shall never determine routing decisions.

The Messaging Layer shall never perform business processing.

---

# 13. Design Constraints

Messaging implementations shall

- support reliable message transport
- support configurable delivery guarantees
- support asynchronous communication
- support horizontal scalability
- preserve message integrity
- preserve message ordering where required
- maintain correlation identifiers
- remain technology independent

Messaging components shall be independently deployable and replaceable.

---

# 14. Dependency Matrix

| Messaging May Use | Messaging Shall Not Use |
|-------------------|-------------------------|
| Distribution Requests | Workflow |
| Delivery Metadata | Pipeline Coordination |
| Messaging Configuration | Processing Logic |
| Infrastructure Abstractions | Routing Decisions |
| Correlation Services | Business Rules |
| Transport Adapters | Domain Aggregates |
| Messaging Protocol Adapters | Repositories |
| Monitoring Services | User Interfaces |

The Messaging Layer shall communicate only through approved architectural interfaces.

---

# 15. Sequence Responsibilities

The responsibilities of the Messaging Layer relative to neighbouring architectural components are defined below.

| Component | Responsibility |
|-----------|----------------|
| Workflow | Defines business orchestration |
| Pipeline | Coordinates technical execution |
| Processing | Executes technical operations |
| Routing | Determines event destinations |
| Distribution | Delivers events to the Messaging Layer |
| Messaging Layer | Transports enterprise messages |
| Messaging Components | Implement transport mechanisms |

The Messaging Layer shall never perform Workflow responsibilities.

The Messaging Layer shall never coordinate Pipeline execution.

The Messaging Layer shall never execute Processing logic.

The Messaging Layer shall never determine Routing decisions.

The Messaging Layer shall never perform Distribution responsibilities.

---

# End of Part 3

---

# 16. Implementation Guidelines

Messaging implementations should

- remain focused exclusively on message transportation
- support configurable messaging technologies
- isolate transport mechanisms from enterprise components
- expose stable messaging interfaces
- support configurable delivery guarantees
- provide comprehensive operational diagnostics
- minimize coupling to specific messaging products

Messaging components should be reusable across multiple enterprise solutions.

---

# 17. Architecture Anti-Patterns

The following practices are prohibited.

## Business Logic inside Messaging

The Messaging Layer shall not implement

- business calculations
- business validation
- pricing logic
- authorization decisions
- domain rules
- business decisions

These responsibilities belong to Domain Capabilities.

---

## Routing inside Messaging

The Messaging Layer shall never

- determine message destinations
- evaluate routing policies
- modify routing decisions
- select business recipients

These responsibilities belong to Routing.

---

## Distribution inside Messaging

The Messaging Layer shall never

- prepare delivery requests
- determine delivery policies
- perform delivery coordination
- execute distribution responsibilities

These responsibilities belong to Distribution.

---

## Direct Domain Access

The Messaging Layer shall never access

- Domain Aggregates
- Domain Services
- repositories
- databases
- SQL
- user interfaces

The Messaging Layer shall remain isolated from business and persistence concerns.

---

## Technology-Coupled Messaging

Messaging implementations shall remain independent of

- broker vendors
- cloud providers
- transport protocol implementations
- infrastructure vendors
- database products

Messaging behaviour shall remain portable across supported messaging technologies.

---

# 18. Architecture Compliance

Messaging implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture
- EA-293 Enterprise Event Distribution Architecture Standard

Architecture reviews shall verify

- correct architectural placement
- dependency compliance
- messaging responsibilities
- transport model compliance
- interface compliance
- lifecycle compliance
- documentation completeness

---

# 19. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-293 compliance verified | ☐ |
| Messaging responsibilities respected | ☐ |
| Transport mechanisms documented | ☐ |
| No routing implemented | ☐ |
| No business processing implemented | ☐ |
| Lifecycle documented | ☐ |
| Dependencies verified | ☐ |
| Architecture review completed | ☐ |

Messaging implementations shall not be approved until mandatory compliance requirements have been satisfied or an approved architectural exception exists.

---

# 20. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-293 Enterprise Event Distribution Architecture Standard
- EA-286 Enterprise Message Broker Architecture Standard
- EA-287 Enterprise Event Bus Architecture Standard
- EA-288 Enterprise Queue Architecture Standard
- EA-289 Enterprise Event Stream Architecture Standard
- EA-290 Enterprise Topic Architecture Standard
- EA-291 Enterprise Channel Architecture Standard
- EA-292 Enterprise Subscription Architecture Standard

---

# 21. Summary

This standard defines the architectural principles, responsibilities, constraints and interfaces governing the Enterprise Messaging Layer within the MFM Enterprise Platform.

The Messaging Layer is responsible exclusively for transporting enterprise messages between enterprise components using approved messaging technologies.

The Messaging Layer neither performs business orchestration, technical processing, routing decisions nor message distribution.

Common Enterprise Architecture requirements are inherited from EA-020.

Common Enterprise Event Architecture requirements are inherited from EA-112.

Distribution responsibilities are inherited from EA-293.

This standard shall be regarded as the authoritative specification for Enterprise Event Messaging Architecture within the MFM Enterprise Platform.

---

# End of Document
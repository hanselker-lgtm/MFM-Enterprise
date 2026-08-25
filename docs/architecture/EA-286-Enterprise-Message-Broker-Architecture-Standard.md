# EA-286 Enterprise Message Broker Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-286 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Message Broker Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Message Broker Components |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Message Broker Standard | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete consolidation aligned with EA-020, EA-112 and EA-285 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-285 | Enterprise Event Messaging Architecture Standard |
| EA-287 | Enterprise Event Bus Architecture Standard |
| EA-288 | Enterprise Queue Architecture Standard |
| EA-289 | Enterprise Event Stream Architecture Standard |
| EA-290 | Enterprise Topic Architecture Standard |
| EA-291 | Enterprise Channel Architecture Standard |
| EA-292 | Enterprise Subscription Architecture Standard |
| EA-293 | Enterprise Event Distribution Architecture Standard |

---

# Architecture Compliance

This standard shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture
- EA-285 Enterprise Event Messaging Architecture Standard

This document defines only the responsibilities specific to Enterprise Message Broker Architecture.

Common architectural requirements are inherited from EA-020.

Common Enterprise Event Architecture is inherited from EA-112.

Common Messaging Architecture is inherited from EA-285.

---

# 1. Purpose

The purpose of this standard is to define the architectural responsibilities, constraints and interfaces governing Enterprise Message Broker components within the MFM Enterprise Platform.

A Message Broker is responsible for receiving, managing and forwarding messages between messaging endpoints.

The Message Broker provides reliable message mediation.

The Message Broker is not responsible for business logic, business orchestration, routing decisions or message distribution.

---

# 2. Scope

This standard applies to every Enterprise Message Broker implementation.

Examples include

- broker services
- broker clusters
- broker nodes
- broker endpoints
- message mediation
- protocol mediation

This standard does not apply to

- business workflows
- event processing
- routing decisions
- message distribution
- application business logic

Those responsibilities are defined in their respective Enterprise Architecture Standards.

---

# 3. Architectural Position

This standard defines the architecture of the Enterprise Message Broker component.

Within the Enterprise Messaging Layer, the Message Broker provides centralized message mediation services.

The Message Broker receives messages from the Distribution layer and forwards them to the appropriate messaging mechanisms.

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

The Message Broker is responsible for

- accepting incoming messages
- validating messaging protocols
- mediating message transport
- forwarding messages
- managing broker connections
- reporting broker status

The Message Broker shall never

- execute business logic
- determine routing decisions
- coordinate workflows
- process business data

---

# End of Part 1

---

# 6. Message Broker Architecture

An Enterprise Message Broker provides centralized message mediation services within the Enterprise Messaging Layer.

The Message Broker accepts messages from the Distribution layer, validates messaging requests, manages broker connections and forwards messages to the appropriate messaging mechanisms.

The Message Broker shall remain independent of business processes, business rules and application logic.

The Message Broker shall not determine routing decisions.

---

# 7. Message Broker Components

A Message Broker implementation may consist of the following logical components.

## Broker Definition

Defines the broker configuration.

Responsibilities

- broker configuration
- supported protocols
- endpoint configuration
- security configuration
- version management

---

## Broker Instance

Represents one operational broker.

Responsibilities

- broker status
- active connections
- broker metrics
- execution history
- operational state

---

## Broker Context

Contains technical information required during broker execution.

Typical information includes

- Broker ID
- Correlation ID
- Connection ID
- Protocol Type
- Endpoint Information
- Delivery Metadata
- Execution Timestamp

Broker Context shall contain only technical messaging information.

---

## Broker Result

Represents the outcome of a broker operation.

Typical information includes

- Broker Status
- Delivery Status
- Transport Status
- Acknowledgement Information
- Error Information

Broker Results shall be immutable once produced.

---

# 8. Interfaces

The Message Broker communicates exclusively through approved architectural interfaces.

The Message Broker may receive

- Distribution Requests
- Messaging Requests
- Delivery Metadata
- Technical Configuration

The Message Broker may invoke

- Queue Components
- Event Bus Components
- Event Stream Components
- Topic Components
- Channel Components

The Message Broker may return

- Broker Result
- Delivery Confirmation
- Technical Status
- Error Information

The Message Broker shall never invoke

- Workflow
- Pipeline
- Processing
- Routing
- Domain Aggregates
- User Interfaces
- Repositories

Broker communication shall remain technology independent.

---

# 9. Broker Operation

Each broker operation shall perform one message mediation operation.

Typical broker activities include

- accepting messaging requests
- validating broker configuration
- establishing broker connections
- forwarding messages
- receiving acknowledgements
- reporting broker status

Broker operations shall not evaluate routing policies.

Broker operations shall not execute business logic.

---

# 10. Interaction with Other Standards

| Standard | Relationship |
|----------|--------------|
| EA-293 Distribution | Supplies delivery requests to the Message Broker |
| EA-285 Messaging | Defines the Enterprise Messaging Layer |
| EA-287 Event Bus | May be invoked for event propagation |
| EA-288 Queue | May be invoked for queued delivery |
| EA-289 Event Stream | May be invoked for stream delivery |
| EA-290 Topic | May be invoked for publish-subscribe communication |
| EA-291 Channel | May be invoked for logical communication paths |
| EA-292 Subscription | Supports subscriber delivery |
| EA-020 | Common architectural requirements |
| EA-112 | Enterprise Event Reference Architecture |

---

# End of Part 2

---

# 11. Broker Lifecycle

Every Message Broker shall follow a defined operational lifecycle.

```text
Created
    │
    ▼
Configured
    │
    ▼
Started
    │
    ▼
Operational
    │
    ▼
Stopping
    │
    ▼
Stopped
```

Alternative operational states include

- Paused
- Failed
- Recovering

Each lifecycle transition shall be validated.

Invalid lifecycle transitions shall be rejected.

---

# 12. Broker Execution Model

The standard Message Broker execution sequence is illustrated below.

```text
Distribution
      │
      ▼
Message Broker
      │
      ▼
Validate Broker Configuration
      │
      ▼
Select Messaging Component
      │
      ▼
Forward Message
      │
      ▼
Receive Delivery Acknowledgement
      │
      ▼
Return Broker Result
```

The Message Broker is responsible exclusively for mediating message transport.

The Message Broker shall never determine routing decisions.

The Message Broker shall never execute business processing.

---

# 13. Design Constraints

Message Broker implementations shall

- support high availability
- support horizontal scalability
- support configurable messaging protocols
- preserve message integrity
- preserve message ordering where required
- support reliable delivery guarantees
- maintain correlation identifiers
- remain technology independent

Message Broker implementations shall support graceful startup and shutdown procedures.

Broker components shall be independently deployable and replaceable.

---

# 14. Dependency Matrix

| Message Broker May Use | Message Broker Shall Not Use |
|------------------------|------------------------------|
| Distribution Requests | Workflow |
| Messaging Configuration | Pipeline Coordination |
| Infrastructure Abstractions | Processing Logic |
| Queue Components | Routing Decisions |
| Event Bus Components | Business Rules |
| Event Stream Components | Domain Aggregates |
| Topic Components | Repositories |
| Channel Components | User Interfaces |
| Subscription Components | SQL Statements |
| Monitoring Services | Application Services |

The Message Broker shall communicate only through approved architectural interfaces.

---

# 15. Sequence Responsibilities

The responsibilities of the Message Broker relative to neighbouring architectural components are defined below.

| Component | Responsibility |
|-----------|----------------|
| Distribution | Delivers messaging requests |
| Message Broker | Mediates message transport |
| Event Bus | Propagates enterprise events |
| Queue | Buffers messages |
| Event Stream | Streams ordered events |
| Topic | Supports publish-subscribe communication |
| Channel | Provides logical communication paths |
| Subscription | Delivers messages to registered consumers |

The Message Broker shall never perform Distribution responsibilities.

The Message Broker shall never implement business workflows.

The Message Broker shall never execute Processing logic.

The Message Broker shall never determine Routing decisions.

The Message Broker shall never implement consumer business behaviour.

---

# End of Part 3

---

# 16. Implementation Guidelines

Message Broker implementations should

- remain focused exclusively on message mediation
- support configurable messaging protocols
- isolate transport mechanisms from enterprise components
- expose stable broker interfaces
- support configurable reliability guarantees
- provide comprehensive operational diagnostics
- minimize coupling to specific broker products

Message Broker implementations should support high availability and horizontal scalability.

---

# 17. Architecture Anti-Patterns

The following practices are prohibited.

## Business Logic inside the Message Broker

The Message Broker shall not implement

- business calculations
- business validation
- pricing logic
- authorization decisions
- domain rules
- business decisions

These responsibilities belong to Domain Capabilities.

---

## Routing Decisions inside the Message Broker

The Message Broker shall never

- determine message destinations
- evaluate routing policies
- modify routing decisions
- select business recipients

These responsibilities belong to the Routing component.

---

## Distribution Responsibilities inside the Message Broker

The Message Broker shall never

- prepare delivery requests
- determine delivery policies
- coordinate message distribution
- perform Distribution responsibilities

These responsibilities belong to the Distribution component.

---

## Direct Domain Access

The Message Broker shall never access

- Domain Aggregates
- Domain Services
- repositories
- databases
- SQL
- user interfaces

The Message Broker shall remain isolated from business and persistence concerns.

---

## Technology-Coupled Broker Implementations

Message Broker implementations shall remain independent of

- broker vendors
- cloud providers
- proprietary infrastructure
- database products
- application frameworks

Broker behaviour shall remain portable across approved messaging technologies.

---

# 18. Architecture Compliance

Message Broker implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture
- EA-285 Enterprise Event Messaging Architecture Standard

Architecture reviews shall verify

- correct architectural placement
- dependency compliance
- broker responsibilities
- mediation model compliance
- interface compliance
- lifecycle compliance
- documentation completeness

---

# 19. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-285 compliance verified | ☐ |
| Broker responsibilities respected | ☐ |
| Broker interfaces documented | ☐ |
| No routing decisions implemented | ☐ |
| No business processing implemented | ☐ |
| Lifecycle documented | ☐ |
| Dependencies verified | ☐ |
| Architecture review completed | ☐ |

Message Broker implementations shall not be approved until all mandatory compliance requirements have been satisfied or an approved architectural exception exists.

---

# 20. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-285 Enterprise Event Messaging Architecture Standard
- EA-287 Enterprise Event Bus Architecture Standard
- EA-288 Enterprise Queue Architecture Standard
- EA-289 Enterprise Event Stream Architecture Standard
- EA-290 Enterprise Topic Architecture Standard
- EA-291 Enterprise Channel Architecture Standard
- EA-292 Enterprise Subscription Architecture Standard
- EA-293 Enterprise Event Distribution Architecture Standard

---

# 21. Summary

This standard defines the architectural responsibilities, constraints and interfaces governing Enterprise Message Broker components within the MFM Enterprise Platform.

The Message Broker is responsible exclusively for receiving, mediating and forwarding enterprise messages between approved messaging components.

The Message Broker neither performs business orchestration, technical processing, routing decisions nor message distribution.

Common Enterprise Architecture requirements are inherited from EA-020.

Common Enterprise Event Architecture requirements are inherited from EA-112.

Common Messaging Architecture requirements are inherited from EA-285.

This standard shall be regarded as the authoritative specification for Enterprise Message Broker Architecture within the MFM Enterprise Platform.

---

# End of Document
# EA-284 Enterprise Event Routing Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-284 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Event Routing Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Event Routing Components |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Routing Standard | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete consolidation aligned with EA-020 and EA-112 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-281 | Enterprise Workflow Architecture Standard |
| EA-282 | Enterprise Event Pipeline Architecture Standard |
| EA-283 | Enterprise Event Processing Architecture Standard |

---

# Architecture Compliance

This standard shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture

This document defines only the responsibilities specific to Event Routing Architecture.

Common architectural requirements are inherited from EA-020.

Common Enterprise Event Architecture is inherited from EA-112.

---

# 1. Purpose

The purpose of this standard is to define the architectural responsibilities, constraints and interfaces governing Event Routing components within the MFM Enterprise Platform.

Routing is responsible for determining the destination of processed events based on technical routing rules.

Routing neither performs business orchestration, technical processing nor event distribution.

---

# 2. Scope

This standard applies to every Event Routing implementation.

Examples include

- destination selection
- endpoint resolution
- channel selection
- routing policy evaluation
- recipient determination
- route selection

This standard does not apply to

- business workflows
- pipeline coordination
- event processing
- event distribution
- messaging infrastructure

Those responsibilities are defined in their respective Enterprise Architecture Standards.

---

# 3. Architectural Position

This standard defines the architecture of the Routing component.

Within the Enterprise Event Reference Architecture this component belongs to the Event Orchestration Layer.

Its responsibility begins where Processing ends and ends where Distribution begins.

---

# 4. Out of Scope

The following responsibilities are outside the scope of this standard

- business orchestration
- business rules
- technical processing
- message delivery
- runtime infrastructure
- persistence
- user interface behaviour

---

# 5. Responsibilities

Routing is responsible for

- determining event destinations
- selecting delivery channels
- evaluating routing policies
- resolving recipients
- producing routing decisions
- forwarding routing results to Distribution

Routing shall never

- execute business rules
- perform technical processing
- deliver messages
- coordinate workflow execution

---

# End of Part 1

---

# 6. Routing Architecture

An Event Routing component determines the appropriate destination for processed events.

Routing evaluates technical routing policies and produces one or more routing decisions.

Routing shall remain independent of business processes and technical event distribution.

Routing components shall not perform message delivery.

---

# 7. Routing Components

A Routing implementation may consist of the following logical components.

## Routing Definition

Defines the routing model.

Responsibilities

- routing policies
- destination definitions
- channel configuration
- routing priorities
- version management

---

## Routing Instance

Represents one routing execution.

Responsibilities

- routing status
- evaluated destinations
- routing history
- execution result
- correlation identifiers

---

## Routing Context

Contains execution information received from Processing.

Typical information includes

- Correlation ID
- Event ID
- Event Type
- Processing Result
- Routing Policy Version
- Execution Timestamp

Routing Context shall contain only technical routing information.

---

## Routing Result

Represents the outcome of routing evaluation.

Typical information includes

- Selected Destinations
- Selected Delivery Channels
- Routing Status
- Routing Metadata
- Error Information

Routing Results shall be immutable once produced.

---

# 8. Interfaces

Routing communicates exclusively through approved architectural interfaces.

Routing may receive

- Routing Context
- Processed Event
- Routing Policies
- Technical Metadata

Routing may return

- Routing Result
- Destination List
- Delivery Instructions
- Routing Status

Routing shall never invoke

- Workflow
- Pipeline
- Processing
- User Interfaces
- Domain Aggregates
- Repositories

Routing components shall remain reusable across multiple Event Pipelines.

---

# 9. Routing Execution

Each Routing execution shall evaluate one routing decision.

Typical routing activities include

- destination selection
- channel selection
- endpoint resolution
- recipient determination
- policy evaluation
- priority evaluation

Routing execution shall not perform message delivery.

Message delivery belongs to the Distribution layer.

---

# 10. Interaction with Other Standards

| Standard | Relationship |
|----------|--------------|
| EA-281 Workflow | Indirectly initiates Routing through Pipeline and Processing |
| EA-282 Pipeline | Coordinates technical execution |
| EA-283 Processing | Supplies processed events |
| EA-020 | Common architectural requirements |
| EA-112 | Enterprise Event Reference Architecture |

---

# End of Part 2

---

# 11. Routing Lifecycle

Every Routing component shall follow a defined execution lifecycle.

```text
Created
    │
    ▼
Initialized
    │
    ▼
Evaluating
    │
    ▼
Completed
```

Alternative terminal states include

- Failed
- Cancelled

Each lifecycle transition shall be validated.

Invalid transitions shall be rejected.

---

# 12. Routing Execution Model

The standard Routing execution sequence is illustrated below.

```text
Processing
      │
      ▼
Routing Component
      │
      ▼
Evaluate Routing Policies
      │
      ▼
Determine Destinations
      │
      ▼
Produce Routing Result
      │
      ▼
Forward Result to Distribution
```

Routing is responsible exclusively for determining where an event shall be delivered.

Routing shall never perform message delivery.

Routing shall never coordinate Processing execution.

---

# 13. Design Constraints

Routing implementations shall

- evaluate routing policies consistently
- produce deterministic routing decisions
- support configurable routing rules
- remain stateless where practical
- support concurrent execution
- preserve routing integrity
- support correlation identifiers
- remain technology independent

Routing components shall be independently deployable and replaceable.

---

# 14. Dependency Matrix

| Routing May Use | Routing Shall Not Use |
|-----------------|-----------------------|
| Routing Context | Workflow |
| Routing Policies | Pipeline Coordination |
| Processed Events | Processing Logic |
| Technical Metadata | Business Rules |
| Infrastructure Abstractions | Domain Aggregates |
| Correlation Services | Repositories |
| Policy Evaluation Services | SQL Statements |
| Destination Configuration | User Interfaces |

Routing shall communicate only through approved architectural interfaces.

---

# 15. Sequence Responsibilities

The responsibilities of Routing relative to neighbouring architectural components are defined below.

| Component | Responsibility |
|-----------|----------------|
| Workflow | Defines business orchestration |
| Pipeline | Coordinates technical execution |
| Processing | Executes technical operations |
| Routing | Determines event destinations |
| Distribution | Delivers routed events |

Routing shall never perform Workflow responsibilities.

Routing shall never perform Pipeline coordination.

Routing shall never execute Processing logic.

Routing shall never perform message delivery.

---

# End of Part 3

---

# 16. Implementation Guidelines

Routing implementations should

- evaluate routing policies consistently
- remain stateless whenever practical
- support configurable routing rules
- produce deterministic routing decisions
- be independently testable
- expose stable interfaces
- minimize coupling to infrastructure

Routing components should be reusable across multiple Event Pipelines.

---

# 17. Architecture Anti-Patterns

The following practices are prohibited.

## Business Logic inside Routing

Routing shall not implement

- business calculations
- business validation
- pricing logic
- authorization decisions
- domain rules
- business decisions

These responsibilities belong to Domain Capabilities.

---

## Processing inside Routing

Routing shall never

- validate event payloads
- transform event data
- enrich event payloads
- execute technical processing operations

These responsibilities belong to Processing.

---

## Message Delivery inside Routing

Routing shall never

- publish messages
- transmit events
- communicate directly with message brokers
- manage queues
- perform event distribution

These responsibilities belong to the Distribution layer.

---

## Direct Infrastructure Access

Routing shall never access

- repositories
- databases
- SQL
- ORM frameworks
- user interfaces

Infrastructure shall only be accessed through approved architectural abstractions.

---

## Technology-Coupled Routing

Routing implementations shall remain independent of

- messaging platforms
- cloud providers
- queue implementations
- broker implementations
- database products

Routing behaviour shall remain portable across supported platforms.

---

# 18. Architecture Compliance

Routing implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture

Architecture reviews shall verify

- correct architectural placement
- dependency compliance
- routing responsibilities
- routing policy compliance
- interface compliance
- lifecycle compliance
- documentation completeness

---

# 19. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| Routing responsibilities respected | ☐ |
| Routing policies documented | ☐ |
| No processing implemented | ☐ |
| No message delivery implemented | ☐ |
| Lifecycle documented | ☐ |
| Dependencies verified | ☐ |
| Architecture review completed | ☐ |

Routing implementations shall not be approved until mandatory compliance requirements have been satisfied or an approved architectural exception exists.

---

# 20. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-281 Enterprise Workflow Architecture Standard
- EA-282 Enterprise Event Pipeline Architecture Standard
- EA-283 Enterprise Event Processing Architecture Standard

---

# 21. Summary

This standard defines the architectural responsibilities, constraints and interfaces governing Event Routing components within the MFM Enterprise Platform.

Routing is responsible exclusively for determining the destination of processed events based on technical routing policies.

Routing neither performs business orchestration, technical processing nor message distribution.

Common Enterprise Architecture requirements are inherited from EA-020.

Common Enterprise Event Architecture requirements are inherited from EA-112.

This standard shall be regarded as the authoritative specification for Enterprise Event Routing Architecture within the MFM Enterprise Platform.

---

# End of Document
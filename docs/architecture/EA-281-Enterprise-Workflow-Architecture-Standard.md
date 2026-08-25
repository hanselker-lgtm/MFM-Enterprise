# EA-281 Enterprise Workflow Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-281 |
| Title | Enterprise Workflow Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Workflow Components |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Workflow Standard | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete consolidation aligned with EA-020 and EA-112 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-282 | Enterprise Event Pipeline Architecture Standard |
| EA-283 | Enterprise Event Processing Architecture Standard |
| EA-284 | Enterprise Event Routing Architecture Standard |

---

# Architecture Compliance

This standard shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture

This document defines only the responsibilities specific to Workflow Architecture.

Common architectural requirements are inherited from EA-020.

Common Event Architecture is inherited from EA-112.

---

# 1. Purpose

The purpose of this standard is to define the architectural responsibilities, constraints and interfaces of Workflow components within the MFM Enterprise Platform.

Workflow is responsible for orchestrating business processes.

Workflow is not responsible for technical event processing.

---

# 2. Scope

This standard applies to all Workflow implementations.

Examples include

- business process orchestration
- approval workflows
- long-running business processes
- cross-capability coordination
- process state management

This standard does not apply to

- event pipelines
- event processing
- routing
- messaging
- runtime infrastructure

Those responsibilities are defined in their respective Enterprise Architecture Standards.

---

# 3. Position within Enterprise Event Architecture

Within the Enterprise Event Reference Architecture, Workflow is positioned immediately after the creation of Application Events.

```text
Business Action
      │
      ▼
Domain Event
      │
      ▼
Application Event
      │
      ▼
Workflow
      │
      ▼
Pipeline
```

Workflow coordinates business execution before technical event processing begins.

---

# 4. Responsibilities

Workflow is responsible for

- orchestrating business processes
- coordinating multiple capabilities
- invoking Feature APIs
- maintaining workflow state
- sequencing business activities
- coordinating long-running business operations
- compensating failed business activities where appropriate

Workflow shall never execute business rules directly.

Workflow shall never perform event routing.

Workflow shall never perform event processing.

Workflow shall never perform messaging.

---

# End of Part 1

---

# 5. Workflow Architecture

A Workflow is an orchestration component responsible for coordinating business activities across one or more capabilities.

A Workflow defines

- the sequence of business activities
- decision points
- synchronization points
- waiting states
- completion criteria

A Workflow shall coordinate business operations without embedding business rules.

Business decisions shall remain inside the participating capabilities.

---

# 6. Workflow Components

A Workflow implementation may consist of the following logical components.

## Workflow Definition

Defines the workflow model.

Responsibilities

- process definition
- workflow metadata
- workflow version
- process ownership

---

## Workflow Instance

Represents one executing workflow.

Responsibilities

- execution state
- progress tracking
- correlation identifiers
- execution history

---

## Workflow Coordinator

Coordinates execution.

Responsibilities

- invoke Feature APIs
- maintain execution order
- manage waiting states
- handle completion

---

## Workflow Context

Contains shared execution information.

Examples

- Correlation ID
- Workflow ID
- Initiating User
- Initiating Capability
- Business Reference
- Start Time

Workflow Context shall not contain business logic.

---

# 7. Interfaces

Workflow interacts only through approved architectural interfaces.

Workflow may invoke

- Feature APIs
- Workflow Services
- Domain Application Services

Workflow shall never invoke

- Repositories
- Databases
- Infrastructure Components
- Message Brokers
- Event Buses

Workflow shall communicate through stable interfaces only.

---

# 8. Workflow State Management

Workflow state represents the progress of a business process.

Typical states include

- Created
- Running
- Waiting
- Suspended
- Completed
- Cancelled
- Failed
- Compensated

Workflow engines shall preserve execution state independently from business state.

---

# 9. Dependencies

Workflow depends upon

- Application Events
- Feature APIs
- Domain Capabilities

Workflow is followed by

- Pipeline

Workflow shall never bypass Pipeline to invoke Processing directly.

Workflow shall remain independent of runtime infrastructure.

---

# 10. Interaction with Other Standards

| Standard | Relationship |
|----------|--------------|
| EA-282 Pipeline | Receives execution from Workflow |
| EA-283 Processing | Executes processing defined by Pipeline |
| EA-284 Routing | Determines event destinations after processing |
| EA-020 | Common architectural requirements |
| EA-112 | Enterprise Event reference model |

---

# End of Part 2

---

# 11. Workflow Lifecycle

Every Workflow shall follow a well-defined lifecycle.

```text
Created
    │
    ▼
Initialized
    │
    ▼
Running
    │
    ▼
Waiting
    │
    ▼
Running
    │
    ▼
Completed
```

Alternative terminal states include

- Cancelled
- Failed
- Compensated

Workflow implementations shall support lifecycle tracking and state transitions.

Invalid state transitions shall be rejected.

---

# 12. Workflow Execution Model

Workflow execution follows the sequence below.

```text
Application Event
        │
        ▼
Workflow
        │
        ▼
Feature API
        │
        ▼
Capability
        │
        ▼
Application Event
        │
        ▼
Pipeline
```

Workflow coordinates execution but does not execute business operations itself.

Each business operation shall remain inside the owning Capability.

---

# 13. Design Constraints

Workflow implementations shall

- remain deterministic
- support idempotent execution where applicable
- maintain execution history
- support correlation identifiers
- support timeout handling
- support compensation for failed business activities
- remain independent of messaging technology

Workflow definitions shall be version controlled.

Workflow engines shall support multiple concurrent workflow instances.

---

# 14. Dependency Matrix

| Workflow May Use | Workflow Shall Not Use |
|------------------|------------------------|
| Feature APIs | Repositories |
| Domain Application Services | Database Connections |
| Application Events | SQL Statements |
| Workflow Context | Message Brokers |
| Correlation Services | Event Bus |
| Domain DTOs | Queue Infrastructure |
| Workflow Services | Stream Infrastructure |

Workflow shall only depend upon stable architectural interfaces.

---

# 15. Sequence Responsibilities

The responsibilities of Workflow relative to neighbouring architectural components are defined below.

| Component | Responsibility |
|-----------|----------------|
| Application Event | Initiates Workflow |
| Workflow | Coordinates business execution |
| Feature API | Provides application boundary |
| Capability | Executes business logic |
| Pipeline | Begins technical processing |
| Processing | Executes technical processing |
| Routing | Determines event destination |

Workflow shall never bypass the Feature API layer.

Workflow shall never invoke Processing directly.

Workflow shall never perform Routing.

---

# End of Part 3

---

# 16. Implementation Guidelines

Workflow implementations should

- remain focused on business orchestration
- be composed of small, well-defined workflow steps
- use explicit workflow state transitions
- support resumable execution
- support compensation where business transactions cannot be rolled back
- minimize coupling between participating capabilities

Workflow definitions should remain readable and business-oriented.

---

# 17. Architecture Anti-Patterns

The following practices are prohibited.

## Business Logic inside Workflow

Workflow shall not implement

- business calculations
- business validation
- pricing logic
- authorization decisions
- domain rules

These responsibilities belong to Domain Capabilities.

---

## Direct Infrastructure Access

Workflow shall never access

- repositories
- SQL
- ORM
- databases
- message brokers
- event buses

Infrastructure shall only be accessed through approved architectural layers.

---

## Workflow-to-Workflow Coupling

A Workflow shall not directly invoke another Workflow.

Cross-workflow coordination shall occur through

- Application Events
- Feature APIs
- Approved orchestration mechanisms

---

## Technology-Coupled Workflows

Workflow definitions shall remain independent of

- messaging products
- database technology
- cloud providers
- workflow engine vendors

Business workflows shall remain portable.

---

# 18. Architecture Compliance

Workflow implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture

Architecture reviews shall verify

- correct architectural placement
- dependency compliance
- workflow responsibilities
- interface compliance
- lifecycle compliance
- documentation completeness

---

# 19. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| Workflow responsibilities respected | ☐ |
| Feature APIs used exclusively | ☐ |
| No direct repository access | ☐ |
| No business rules implemented | ☐ |
| Lifecycle documented | ☐ |
| Dependencies verified | ☐ |
| Architecture review completed | ☐ |

Workflow implementations shall not be approved until mandatory compliance requirements have been satisfied or an approved architectural exception exists.

---

# 20. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-282 Enterprise Event Pipeline Architecture Standard
- EA-283 Enterprise Event Processing Architecture Standard
- EA-284 Enterprise Event Routing Architecture Standard

---

# 21. Summary

This standard defines the architectural responsibilities, constraints and interfaces governing Workflow components within the MFM Enterprise Platform.

Workflow is responsible exclusively for business orchestration.

Workflow coordinates business execution but neither executes business rules nor performs technical event processing.

Common Enterprise Architecture requirements are inherited from EA-020.

Common Event Architecture requirements are inherited from EA-112.

This standard shall be regarded as the authoritative specification for Workflow Architecture within the MFM Enterprise Platform.

---

# End of Document
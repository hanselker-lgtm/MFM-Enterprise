# EA-290 Enterprise Topic Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-290 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Topic Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-26 |
| Applies To | All Enterprise Topic Components |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Legacy Topic Standard | Enterprise Architecture Team |
| 2.0 | 2026-07-26 | Complete consolidation aligned with EA-020, EA-112, EA-285, EA-286, EA-287 and EA-289 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-285 | Enterprise Event Messaging Architecture Standard |
| EA-286 | Enterprise Message Broker Architecture Standard |
| EA-287 | Enterprise Event Bus Architecture Standard |
| EA-289 | Enterprise Event Stream Architecture Standard |
| EA-291 | Enterprise Channel Architecture Standard |
| EA-292 | Enterprise Subscription Architecture Standard |
| EA-293 | Enterprise Event Distribution Architecture Standard |

---

# Architecture Compliance

This standard shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture
- EA-285 Enterprise Event Messaging Architecture Standard

This document defines only the responsibilities specific to Enterprise Topic Architecture.

Common architectural requirements are inherited from EA-020.

Common Enterprise Event Architecture is inherited from EA-112.

Common Messaging Architecture is inherited from EA-285.

---

# 1. Purpose

The purpose of this standard is to define the architectural responsibilities, constraints and interfaces governing Enterprise Topic components within the MFM Enterprise Platform.

An Enterprise Topic provides a logical categorisation of published events, enabling producers and consumers to communicate through a common semantic event namespace.

Topics separate event identity from delivery mechanisms and enable scalable publish-subscribe communication.

A Topic is not responsible for business logic, business orchestration, routing decisions, message transport or message distribution.

---

# 2. Scope

This standard applies to every Enterprise Topic implementation.

Examples include

- event topics
- domain topics
- integration topics
- notification topics
- audit topics
- system topics

This standard does not apply to

- business workflows
- event processing
- routing decisions
- broker implementation
- application business logic

Those responsibilities are defined in their respective Enterprise Architecture Standards.

---

# 3. Architectural Position

This standard defines the architecture of the Enterprise Topic component.

Within the Enterprise Messaging Layer, Topics provide the logical namespace through which publishers expose events and subscribers discover them.

Topics organise published events independently of the underlying transport technology.

---

# 4. Out of Scope

The following responsibilities are outside the scope of this standard

- business orchestration
- business rules
- technical processing
- routing decisions
- message transport
- message distribution
- domain modelling

---

# 5. Responsibilities

The Topic is responsible for

- organising published events
- providing logical event categorisation
- maintaining topic definitions
- supporting publisher registration
- supporting subscriber registration
- exposing topic metadata
- reporting topic status

The Topic shall never

- execute business logic
- determine routing decisions
- coordinate workflows
- transport messages
- process business data

---

# End of Part 1

---

# 6. Topic Architecture

An Enterprise Topic provides a logical namespace for categorising and publishing enterprise events.

Topics enable producers and consumers to communicate through shared event definitions without requiring knowledge of each other's implementation.

A Topic represents the semantic identity of published events and remains independent of the underlying messaging technology.

Topics shall support loose coupling, scalability and technology-independent event classification.

---

# 7. Topic Namespace

Every Topic shall belong to a well-defined namespace.

A namespace provides hierarchical organisation of related Topics and prevents naming conflicts across the enterprise.

Typical namespace levels may include

- enterprise
- domain
- capability
- application
- integration

Namespaces shall be globally unique within the enterprise.

Namespace structures shall remain stable over time.

---

# 8. Topic Hierarchy

Topics may be organised into hierarchical structures.

Example hierarchy

```text
Enterprise
    │
    ├── Finance
    │      ├── Invoice
    │      ├── Payment
    │      └── Accounting
    │
    ├── Membership
    │      ├── Member
    │      ├── Subscription
    │      └── Contact
    │
    └── Vessel
           ├── Registry
           ├── Maintenance
           └── Inspection
```

Hierarchies improve

- discoverability
- governance
- ownership
- documentation
- version management

Hierarchies shall not affect message routing or delivery.

---

# 9. Topic Metadata

Each Topic shall maintain metadata describing its purpose and usage.

Typical Topic metadata includes

- Topic Name
- Namespace
- Topic Identifier
- Version
- Description
- Owner
- Publisher Information
- Subscriber Information
- Retention Policy Reference
- Security Classification

Metadata shall remain independent of implementation technology.

---

# 10. Interfaces

The Topic communicates exclusively through approved architectural interfaces.

The Topic may receive

- Topic Registration Requests
- Publisher Registrations
- Subscriber Registrations
- Topic Metadata Requests
- Technical Configuration

The Topic may invoke

- Subscription Components
- Monitoring Services
- Governance Services

The Topic may return

- Topic Definition
- Topic Metadata
- Registration Status
- Validation Results
- Error Information

The Topic shall never invoke

- Workflow
- Pipeline
- Processing
- Routing
- Message Broker
- User Interfaces
- Repositories

Topic communication shall remain technology independent.

---

# 11. Topic Operation

Each Topic operation shall perform one well-defined topic management activity.

Typical Topic activities include

- registering topics
- validating topic definitions
- maintaining topic metadata
- registering publishers
- registering subscribers
- validating namespace integrity
- reporting topic status

Topic operations shall never execute business logic.

Topic operations shall never transport messages.

Topic operations shall never determine routing decisions.

---

# 12. Interaction with Other Standards

| Standard | Relationship |
|----------|--------------|
| EA-285 Messaging | Defines the Enterprise Messaging Layer |
| EA-286 Message Broker | May expose Topic functionality |
| EA-287 Event Bus | Publishes events to Topics |
| EA-289 Event Stream | May organise streamed events using Topics |
| EA-291 Channel | Carries messages associated with Topics |
| EA-292 Subscription | Defines Topic consumers |
| EA-293 Distribution | Supplies publication requests |
| EA-020 | Common architectural requirements |
| EA-112 | Enterprise Event Reference Architecture |

---

# End of Part 2

---

# 13. Topic Lifecycle

Every Enterprise Topic shall follow a defined lifecycle.

```text
Defined
    │
    ▼
Approved
    │
    ▼
Published
    │
    ▼
Operational
    │
    ▼
Deprecated
    │
    ▼
Retired
```

Alternative lifecycle states include

- Draft
- Suspended
- Archived

Each lifecycle transition shall be governed through Enterprise Architecture governance.

Deprecated Topics shall remain available according to the approved deprecation policy.

Retired Topics shall no longer accept new publisher registrations.

---

# 14. Topic Execution Model

The standard Topic execution sequence is illustrated below.

```text
Publisher
      │
      ▼
Validate Topic
      │
      ▼
Locate Namespace
      │
      ▼
Validate Topic Definition
      │
      ▼
Publish Event Reference
      │
      ▼
Expose Topic Metadata
      │
      ▼
Notify Registered Subscribers
```

The Topic provides the logical publication point.

Actual message transport is performed by the Messaging Layer.

Topics shall never execute business processing.

Topics shall never determine routing behaviour.

---

# 15. Topic Governance

Enterprise Topics shall be governed centrally.

Governance responsibilities include

- namespace management
- topic ownership
- naming approval
- version management
- lifecycle approval
- metadata quality
- documentation quality
- architectural compliance

Every Topic shall have an assigned owner.

Every Topic shall have documented business and technical descriptions.

Topic governance shall ensure consistency across the enterprise.

---

# 16. Design Constraints

Topic implementations shall

- provide globally unique topic identifiers
- support hierarchical namespaces
- maintain immutable topic identities
- support versioned topic definitions
- preserve metadata integrity
- support publisher and subscriber registration
- remain technology independent

Topic implementations shall never embed transport-specific behaviour.

Topic implementations shall expose metadata suitable for enterprise discovery and governance.

---

# 17. Dependency Matrix

| Topic May Use | Topic Shall Not Use |
|-----------------------------|----------------------------|
| Namespace Services | Workflow |
| Metadata Services | Pipeline Coordination |
| Governance Services | Processing Logic |
| Registration Services | Routing Decisions |
| Monitoring Services | Business Rules |
| Version Management | Domain Aggregates |
| Enterprise Messaging Interfaces | Repositories |
| Security Classification | User Interfaces |
| Topic Definitions | SQL Statements |
| Documentation Services | Application Services |

The Topic shall communicate exclusively through approved architectural interfaces.

---

# 18. Sequence Responsibilities

The responsibilities of the Topic relative to neighbouring architectural components are defined below.

| Component | Responsibility |
|-----------|----------------|
| Publisher | Publishes events to Topics |
| Topic | Provides logical event categorisation |
| Subscription | Registers event consumers |
| Channel | Provides communication paths |
| Event Bus | Propagates published events |
| Event Stream | Maintains ordered event streams |
| Message Broker | Coordinates message transport |

The Topic shall never perform Message Broker responsibilities.

The Topic shall never perform Event Bus responsibilities.

The Topic shall never execute consumer business logic.

The Topic shall never transport messages.

---

# End of Part 3

---

# 19. Implementation Guidelines

Topic implementations should

- remain focused exclusively on logical event categorisation
- support hierarchical namespace management
- expose stable Topic registration interfaces
- maintain immutable Topic identities
- support versioned Topic definitions
- provide comprehensive metadata for discovery and governance
- isolate Topic definitions from transport technologies
- minimize coupling to specific messaging platforms

Topic implementations should support enterprise-wide discoverability and governance.

---

# 20. Architecture Anti-Patterns

The following practices are prohibited.

## Business Logic inside Topics

Topics shall not implement

- business calculations
- business validation
- authorization decisions
- pricing logic
- domain rules
- business decisions

These responsibilities belong to Domain Capabilities.

---

## Message Transport inside Topics

Topics shall never

- transport messages
- queue messages
- stream messages
- deliver messages
- retry message delivery

These responsibilities belong to the Enterprise Messaging Layer.

---

## Routing Decisions inside Topics

Topics shall never

- determine event destinations
- evaluate routing policies
- modify routing behaviour
- select recipients

These responsibilities belong to the Routing component.

---

## Direct Domain Access

Topics shall never access

- Domain Aggregates
- Domain Services
- repositories
- databases
- SQL
- user interfaces

Topics shall remain isolated from business and persistence concerns.

---

## Technology-Coupled Topic Implementations

Topic implementations shall remain independent of

- messaging vendors
- cloud providers
- proprietary messaging platforms
- database products
- application frameworks

Topic definitions and metadata shall remain portable across approved messaging technologies.

---

# 21. Architecture Compliance

Topic implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-112 Enterprise Event Reference Architecture
- EA-285 Enterprise Event Messaging Architecture Standard

Architecture reviews shall verify

- correct architectural placement
- dependency compliance
- Topic responsibilities
- namespace compliance
- metadata quality
- governance compliance
- lifecycle compliance
- documentation completeness

---

# 22. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-285 compliance verified | ☐ |
| Topic responsibilities respected | ☐ |
| Namespace documented | ☐ |
| Topic metadata complete | ☐ |
| Governance documented | ☐ |
| Lifecycle documented | ☐ |
| Dependencies verified | ☐ |
| Architecture review completed | ☐ |

Topic implementations shall not be approved until all mandatory compliance requirements have been satisfied or an approved architectural exception exists.

---

# 23. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-285 Enterprise Event Messaging Architecture Standard
- EA-286 Enterprise Message Broker Architecture Standard
- EA-287 Enterprise Event Bus Architecture Standard
- EA-289 Enterprise Event Stream Architecture Standard
- EA-291 Enterprise Channel Architecture Standard
- EA-292 Enterprise Subscription Architecture Standard
- EA-293 Enterprise Event Distribution Architecture Standard

---

# 24. Summary

This standard defines the architectural responsibilities, constraints and interfaces governing Enterprise Topic components within the MFM Enterprise Platform.

The Topic is responsible exclusively for providing a logical, technology-independent namespace for enterprise events, enabling publishers and subscribers to communicate through shared semantic definitions.

The Topic does not perform business orchestration, business processing, routing decisions, message transport or message distribution.

Common Enterprise Architecture requirements are inherited from EA-020.

Common Enterprise Event Architecture requirements are inherited from EA-112.

Common Messaging Architecture requirements are inherited from EA-285.

This standard shall be regarded as the authoritative specification for Enterprise Topic Architecture within the MFM Enterprise Platform.

---

# End of Document
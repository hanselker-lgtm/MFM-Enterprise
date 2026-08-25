# EA-010 Event-Driven Architecture

| Property | Value |
|----------|-------|
| Document ID | EA-010 |
| Title | Event-Driven Architecture |
| Version | 1.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-17 |
| Applies To | Entire MFM Enterprise Platform |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | 2026-07-17 | Initial Event-Driven Architecture | Chief Enterprise Architect |

---

# Related Documents

This document extends the following Enterprise Architecture specifications.

| Document | Description |
|----------|-------------|
| EA-002 | Canonical Domain Model |
| EA-003 | Enterprise Service Catalog |
| EA-008 | Reference Architecture |
| EA-009 | Plugin Architecture |

EA-008 defines the architectural layers.

EA-009 defines how plugins participate in the event system.

This document specifies the event model used throughout the platform.

---

# 1. Purpose

The purpose of this document is to define the official Event-Driven Architecture (EDA) for the MFM Enterprise Platform.

The event architecture enables autonomous capabilities to collaborate through well-defined business events while maintaining loose coupling, high cohesion and long-term maintainability.

Events represent facts that have already occurred.

Events shall never represent commands or requests.

---

# 2. Scope

This specification applies to

- Core Platform
- Enterprise Services
- Business Capabilities
- Feature APIs
- Workflows
- Reporting
- Plugins
- Future distributed deployments

Every event published within the platform shall comply with this specification.

---

# 3. Objectives

## EDA-001 Loose Coupling

Capabilities shall communicate through events whenever synchronous communication is not required.

---

## EDA-002 Scalability

The architecture shall support future expansion from a single-process desktop application to distributed enterprise deployments without changing the business event model.

---

## EDA-003 Traceability

Every published event shall be traceable from origin to completion.

---

## EDA-004 Reliability

Events shall never leave the platform in an inconsistent state.

---

## EDA-005 Extensibility

New capabilities and plugins shall participate in the event system without modifications to existing capabilities.

---

## EDA-006 Auditability

Business events shall provide a complete audit trail for all significant business activities.

---

## EDA-007 Technology Independence

Business events shall remain independent of transport mechanisms, storage technologies and user interface frameworks.

---

# 4. Architectural Principles

The Event-Driven Architecture is governed by the following principles.

## EP-001

Events describe facts.

Events do not describe intentions.

---

## EP-002

Events are immutable.

Once published, an event shall never be modified.

---

## EP-003

Publishing an event shall never require knowledge of its subscribers.

---

## EP-004

Subscribers shall depend only on the published event contract.

---

## EP-005

Every event shall have exactly one publisher.

Multiple subscribers are permitted.

---

## EP-006

Events shall never expose internal implementation details of a capability.

---

## EP-007

Events shall represent business language rather than technical implementation.

---

# 5. Event Taxonomy

The platform recognises the following event categories.

| Category | Purpose |
|----------|---------|
| Domain Event | Business facts produced by a capability |
| Integration Event | Cross-capability communication |
| System Event | Platform lifecycle |
| Workflow Event | Workflow progression |
| Plugin Event | Plugin lifecycle and integration |
| Notification Event | User notifications |
| Audit Event | Audit logging |
| Infrastructure Event | Technical platform events |

Each event shall belong to exactly one primary category.

---

# 6. Event Characteristics

Every event shall satisfy the following characteristics.

- Immutable
- Serializable
- Versioned
- Timestamped
- Traceable
- Self-describing
- Independently testable
- Backwards compatible within a major version

Events shall remain valid even when processed long after publication.

---

# 7. Event Lifecycle Overview

Every event follows the lifecycle below.

```text
Business Action
       │
       ▼
Create Event
       │
       ▼
Validate Event
       │
       ▼
Publish Event
       │
       ▼
Dispatch Event
       │
       ▼
Handle Event
       │
       ▼
Audit Event
       │
       ▼
Archive Event
```

The following chapters define each stage in detail.

---

# End of Part 1

---

# 8. Domain Events

## 8.1 Purpose

Domain Events represent significant business facts that have occurred within a single capability.

A Domain Event shall be raised only after the associated business transaction has completed successfully.

Domain Events are the preferred mechanism for communicating business changes.

---

## 8.2 Characteristics

A Domain Event shall

- represent a completed business fact
- be immutable
- contain only business information
- be serializable
- include version information
- include audit metadata

A Domain Event shall never expose persistence details.

---

## 8.3 Examples

Examples include

- MemberCreated
- MemberUpdated
- MembershipRenewed
- InvoiceIssued
- PaymentReceived
- DocumentArchived
- VesselRegistered
- RestorationStarted
- GrantApproved

Events shall be named in the past tense.

---

# 9. Integration Events

## 9.1 Purpose

Integration Events communicate business facts across capabilities.

Integration Events are derived from Domain Events when information must leave the originating capability.

---

## 9.2 Transformation

The originating capability owns the transformation from

Domain Event

↓

Integration Event

Only the originating capability may perform this mapping.

---

## 9.3 Responsibilities

Integration Events shall

- expose stable contracts
- hide internal implementation
- remain backwards compatible
- support future distributed deployments

---

# 10. System Events

## 10.1 Purpose

System Events describe platform lifecycle activities.

Examples include

- PlatformStarted
- PlatformStopped
- UserAuthenticated
- UserSignedOut
- PluginActivated
- PluginRemoved
- BackupCompleted

System Events shall not contain business data.

---

# 11. Workflow Events

Workflow Events describe progression through business workflows.

Typical examples include

- WorkflowStarted
- ApprovalRequested
- ApprovalGranted
- WorkflowCompleted
- WorkflowCancelled

Workflow Events coordinate business processes.

They do not replace Domain Events.

---

# 12. Notification Events

Notification Events inform users about completed activities.

Examples

- InvoiceReady
- MembershipExpiring
- GrantDeadlineApproaching
- BackupFinished

Notification Events shall not trigger business processing.

---

# 13. Event Metadata

## 13.1 Purpose

Every event shall contain standard metadata.

Metadata enables

- tracing
- diagnostics
- auditing
- monitoring
- replay

---

## 13.2 Mandatory Metadata

Every event shall contain

| Property | Description |
|----------|-------------|
| EventId | Globally unique identifier |
| EventType | Event class |
| EventVersion | Schema version |
| Timestamp | UTC timestamp |
| CorrelationId | Related transaction |
| CausationId | Parent event |
| SourceCapability | Publishing capability |
| Publisher | Publisher identifier |

Additional metadata may be added when required.

---

# 14. Correlation Identifier

The Correlation Identifier links all events belonging to one logical business transaction.

Example

```text
Create Member

↓

MemberCreated

↓

MembershipActivated

↓

InvoiceIssued

↓

NotificationSent
```

All events shall share the same CorrelationId.

---

# 15. Causation Identifier

The Causation Identifier identifies the event that directly caused another event.

Example

```text
MemberCreated
      │
      ▼
MembershipActivated
      │
      ▼
InvoiceIssued
```

Each child event shall reference its immediate parent.

---

# 16. Event Contracts

Event contracts define the public structure of published events.

Contracts shall remain stable.

Breaking changes require

- new event version
- migration documentation
- compatibility assessment

Consumers shall depend only on documented contracts.

---

# 17. Event Naming

Events shall follow consistent naming conventions.

Rules

- Use business terminology.
- Use past tense.
- Avoid technical terminology.
- Use singular nouns.

Correct examples

- MemberCreated
- PaymentReceived
- VesselRegistered

Incorrect examples

- CreateMember
- UpdateInvoice
- SaveCustomer

---

# End of Part 2

---

# 18. Event Bus

## 18.1 Purpose

The Event Bus is the central communication mechanism for all published events within the MFM Enterprise Platform.

The Event Bus provides loose coupling between publishers and subscribers.

Publishers shall never know which subscribers receive an event.

Subscribers shall never know the publisher implementation.

---

## 18.2 Responsibilities

The Event Bus shall

- receive published events
- validate event contracts
- dispatch events
- manage subscriptions
- record diagnostics
- support synchronous dispatch
- support asynchronous dispatch
- support future distributed transports

The Event Bus shall remain independent of individual capabilities.

---

## 18.3 Architectural Position

```text
Capability

     │

Publish Domain Event

     │

     ▼

+----------------------+
|      Event Bus       |
+----------------------+
      │
      │
 ┌────┴─────────────┐
 ▼                  ▼
Subscriber A   Subscriber B
      │
      ▼
Subscriber C
```

The Event Bus shall never contain business logic.

---

# 19. Event Dispatching

## 19.1 Purpose

Dispatching is responsible for delivering published events to eligible subscribers.

Dispatching shall occur after successful publication.

---

## 19.2 Dispatch Sequence

The dispatch sequence shall be

```text
Publish Event

↓

Validate Contract

↓

Resolve Subscribers

↓

Dispatch Event

↓

Execute Subscribers

↓

Collect Results

↓

Audit Dispatch
```

---

## 19.3 Dispatch Rules

Dispatching shall

- preserve event integrity
- preserve metadata
- isolate subscriber failures
- support multiple subscribers
- record execution statistics

Subscriber execution order shall not be relied upon unless explicitly defined.

---

# 20. Event Subscription

## 20.1 Registration

Subscribers shall register through the Event Bus.

Registration shall include

- Event Type
- Subscriber Identifier
- Execution Mode
- Priority
- Subscription Status

---

## 20.2 Dynamic Registration

Plugins may register subscriptions during activation.

Subscriptions shall automatically be removed during plugin deactivation.

---

## 20.3 Subscription Rules

Subscribers shall

- subscribe explicitly
- process supported event versions
- ignore unknown metadata
- tolerate future event extensions

---

# 21. Delivery Guarantees

## 21.1 Delivery Model

The platform shall support the following delivery guarantees.

| Mode | Description |
|------|-------------|
| At Most Once | Optional future support |
| At Least Once | Preferred |
| Exactly Once | Future distributed deployments |

Desktop deployments shall default to At Least Once delivery.

---

## 21.2 Retry Policy

Transient failures may be retried automatically.

Retry behaviour shall be configurable.

Retry attempts shall be logged.

Permanent failures shall not be retried indefinitely.

---

## 21.3 Dead Letter Handling

Events that repeatedly fail processing shall be transferred to a Dead Letter Queue (DLQ).

The Dead Letter Queue shall preserve

- original payload
- metadata
- failure reason
- retry count
- timestamp

Desktop editions may implement the DLQ as persistent local storage.

Enterprise deployments may implement dedicated queue infrastructure.

---

# 22. Synchronous and Asynchronous Processing

## 22.1 Synchronous Processing

Synchronous event processing shall be used when

- immediate consistency is required
- execution is short-lived
- subscriber completion is required before continuing

---

## 22.2 Asynchronous Processing

Asynchronous processing shall be used when

- execution is long-running
- external services are contacted
- reports are generated
- notifications are delivered
- indexing is performed

---

## 22.3 Selection Criteria

The Workflow Layer determines whether event processing shall be synchronous or asynchronous.

Business requirements take precedence over technical optimisation.

---

# 23. Subscriber Behaviour

Subscribers shall

- be idempotent
- validate received data
- handle missing optional fields
- avoid side effects where possible
- publish additional events only after successful processing

Subscribers shall never modify received events.

---

# 24. Event Ordering

The platform shall preserve event ordering within a single business transaction whenever required.

Ordering shall be determined by

- Correlation Identifier
- Timestamp
- Sequence Number

Subscribers shall not assume global ordering across unrelated transactions.

---

# 25. Event Filtering

Subscribers may define filtering criteria.

Supported filters include

- Event Type
- Event Version
- Capability
- Category
- Metadata
- Custom Predicates

Filtering shall occur before subscriber execution.

---

# End of Part 3

---

# 26. Event Versioning

## 26.1 Purpose

Event Versioning ensures that the event architecture can evolve without breaking existing subscribers.

Every published event shall declare its schema version.

Versioning applies only to the event contract.

Business meaning shall remain stable whenever practical.

---

## 26.2 Versioning Rules

Event contracts shall follow Semantic Versioning.

| Change Type | Version Impact |
|-------------|----------------|
| Documentation only | None |
| Optional field added | Minor |
| New metadata | Minor |
| Breaking schema change | Major |
| Removed field | Major |

Breaking changes shall introduce a new event version.

Existing versions shall remain supported throughout the compatibility period.

---

## 26.3 Compatibility

Subscribers shall process the highest supported version.

Unknown optional properties shall be ignored.

Missing optional properties shall use documented default behaviour.

---

# 27. Event Persistence

## 27.1 Purpose

Published events may be persisted for auditing, diagnostics and future replay.

Persistence is independent of event processing.

The Event Store shall never replace the operational database.

---

## 27.2 Persisted Information

A persisted event shall contain

- Event Identifier
- Event Type
- Event Version
- Timestamp
- Correlation Identifier
- Causation Identifier
- Publisher
- Payload
- Metadata

---

## 27.3 Retention

Retention policies shall be configurable.

Policies may differ between

- Audit Events
- Business Events
- Infrastructure Events
- Diagnostic Events

Expired events may be archived according to organisational policy.

---

# 28. Event Replay

## 28.1 Purpose

Replay allows previously stored events to be processed again.

Replay shall be used only for

- diagnostics
- migration
- rebuilding projections
- testing
- disaster recovery

Replay shall never create duplicate business transactions.

---

## 28.2 Replay Rules

Replay shall preserve

- Event Identifier
- Timestamp
- Correlation Identifier
- Causation Identifier

Replay execution shall be clearly distinguishable from live processing.

---

## 28.3 Replay Safety

Subscribers participating in replay shall support idempotent processing.

Replay shall never violate business consistency.

---

# 29. Idempotency

## 29.1 Purpose

Subscribers shall tolerate duplicate delivery.

Processing the same event multiple times shall produce the same business result.

---

## 29.2 Requirements

Subscribers shall

- detect duplicate Event Identifiers
- ignore previously processed events
- preserve business consistency

Idempotency shall be documented for every subscriber.

---

# 30. Audit Integration

## 30.1 Purpose

The Event Architecture integrates directly with the Enterprise Audit Service.

Every significant business event shall produce an audit record.

---

## 30.2 Audit Information

Audit records shall include

- User
- Timestamp
- Capability
- Event Identifier
- Correlation Identifier
- Action
- Entity
- Outcome

Audit records shall be immutable.

---

# 31. Monitoring and Diagnostics

## 31.1 Purpose

The Event Bus shall expose operational metrics.

Monitoring shall support

- troubleshooting
- capacity planning
- performance analysis

---

## 31.2 Metrics

The platform shall record

- Events Published
- Events Processed
- Processing Duration
- Subscriber Failures
- Retry Count
- Dead Letter Count
- Queue Length
- Replay Count

Metrics shall be available through the Platform Monitoring Service.

---

# 31.3 Diagnostics

Diagnostic information shall include

- Publisher
- Subscriber
- Event Type
- Processing Time
- Failure Reason
- Retry Attempts

Diagnostic logging shall not expose confidential business information.

---

# 32. Governance

## 32.1 Ownership

Every published event shall have an owning capability.

Only the owning capability may modify the event contract.

---

## 32.2 Approval

New public Integration Events require architectural review.

Breaking changes require

- Architecture Decision Record (ADR)
- Compatibility assessment
- Migration guidance

---

## 32.3 Deprecation

Deprecated events shall remain supported throughout the published deprecation period.

Replacement events shall be documented before deprecation begins.

---

# 33. Compliance Checklist

Every implementation shall satisfy the following requirements.

- Events represent completed business facts.
- Events are immutable.
- Events are versioned.
- Events include mandatory metadata.
- Events use Correlation Identifiers.
- Events use Causation Identifiers.
- Subscribers are idempotent.
- Event contracts are documented.
- Event processing is audited.
- Event publication follows the Event Bus.
- No direct capability-to-capability event bypass is permitted.

---

# End of Part 4

---

# 34. Security Considerations

## 34.1 Purpose

The Event-Driven Architecture shall preserve confidentiality, integrity and availability of event data.

Security requirements apply equally to Core Platform components, Enterprise Services and Plugins.

---

## 34.2 Event Integrity

Events shall not be modified after publication.

Integrity shall be protected through

- immutable event contracts
- version validation
- controlled serialization
- audit logging

---

## 34.3 Authorization

Only authorised components may publish Integration Events.

Subscribers shall validate access rights before processing sensitive business information.

Authorization decisions remain the responsibility of the originating capability.

---

## 34.4 Sensitive Data

Events shall contain only the information required by subscribers.

Personally identifiable information (PII) shall be minimised.

Confidential information shall never be exposed unnecessarily through Integration Events.

---

## 34.5 Event Validation

All received events shall be validated before processing.

Validation shall include

- schema validation
- version validation
- metadata validation
- source validation

Invalid events shall be rejected and logged.

---

# 35. Testing Strategy

## 35.1 Purpose

The Event Architecture shall support comprehensive automated testing.

Testing shall verify correctness, robustness and compatibility.

---

## 35.2 Unit Testing

Unit tests shall verify

- event creation
- metadata generation
- serialization
- validation
- subscriber behaviour

---

## 35.3 Integration Testing

Integration tests shall verify

- Event Bus dispatching
- subscriber registration
- event ordering
- retry behaviour
- replay
- audit integration

---

## 35.4 Architecture Testing

Architecture tests shall verify

- dependency rules
- event ownership
- naming conventions
- version compatibility

---

## 35.5 Performance Testing

Performance tests shall measure

- publication latency
- dispatch latency
- subscriber execution time
- throughput
- memory usage

Results shall be recorded for regression analysis.

---

# 36. Reference Event Catalogue

The following table illustrates recommended business events.

| Capability | Example Events |
|------------|----------------|
| Contact | ContactCreated, ContactUpdated |
| Membership | MemberCreated, MembershipRenewed |
| Finance | InvoiceIssued, PaymentReceived |
| Documents | DocumentCreated, DocumentArchived |
| Vessel | VesselRegistered, VesselUpdated |
| Heritage | HeritageRecordCreated |
| Restoration | RestorationStarted, RestorationCompleted |
| Volunteers | VolunteerAssigned |
| Projects | ProjectCreated, ProjectClosed |
| Grants | GrantApplicationSubmitted, GrantApproved |

The catalogue is illustrative and shall evolve with the platform.

---

# 37. Future Evolution

The Event Architecture has been designed to support future expansion.

Planned enhancements include

- Distributed Event Bus
- Cloud-native messaging
- Event Store optimisation
- Event streaming
- External integration gateways
- Real-time monitoring dashboards
- Event analytics
- Event sourcing where appropriate

Future enhancements shall preserve existing event contracts whenever practical.

---

# Appendix A – Event Flow Example

```text
User Action
      │
      ▼
Workflow
      │
      ▼
Capability
      │
      ▼
Domain Event
      │
      ▼
Event Bus
      │
 ┌────┼─────────────┐
 ▼    ▼             ▼
Audit Notification Reporting
```

---

# Appendix B – Event Naming Examples

| Correct | Incorrect |
|----------|-----------|
| MemberCreated | CreateMember |
| InvoiceIssued | IssueInvoice |
| PaymentReceived | ReceivePayment |
| VesselRegistered | RegisterVessel |
| DocumentArchived | ArchiveDocument |

Event names shall always describe completed business facts.

---

# Appendix C – Event Lifecycle Summary

```text
Business Action

↓

Domain Event

↓

Validation

↓

Publication

↓

Dispatch

↓

Subscriber Processing

↓

Audit

↓

Persistence

↓

Archive
```

---

# Appendix D – Event Metadata Summary

| Field | Required |
|--------|----------|
| EventId | Yes |
| EventType | Yes |
| EventVersion | Yes |
| Timestamp | Yes |
| CorrelationId | Yes |
| CausationId | Yes |
| SourceCapability | Yes |
| Publisher | Yes |

---

# Final Statement

The Event-Driven Architecture establishes the official communication model for the MFM Enterprise Platform.

All business capabilities, Enterprise Services, workflows and plugins shall publish and consume events in accordance with this specification.

The architecture is designed to provide loose coupling, long-term maintainability and a clear evolution path from desktop deployments to distributed enterprise solutions while preserving architectural consistency.

End of Document.
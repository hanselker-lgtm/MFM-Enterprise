# EA-342 Enterprise Messaging Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-342 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Messaging Architecture Standard |
| Version | 2.0 |
| Status | Approved |
| Owner | Chief Enterprise Architect |
| Classification | Internal |
| Last Updated | 2026-07-27 |
| Applies To | Entire MFM Enterprise Platform |

---

# Revision History

| Version | Date | Description | Author |
|----------|------|-------------|--------|
| 1.x | Previous | Initial Enterprise Messaging Guidance | Enterprise Architecture Team |
| 2.0 | 2026-07-27 | Complete Enterprise Messaging Architecture aligned with EA-020, EA-111, EA-112, EA-320, EA-340 and EA-341 | Chief Enterprise Architect |

---

# Related Documents

| Document | Description |
|----------|-------------|
| EA-020 | Enterprise Architecture Common Requirements |
| EA-111 | Enterprise Architecture Blueprint |
| EA-112 | Enterprise Event Reference Architecture |
| EA-320 | Enterprise Infrastructure Layer Reference Architecture |
| EA-340 | Enterprise Integration Architecture Standard |
| EA-341 | Enterprise API Architecture Standard |
| EA-343 | Enterprise Event Streaming Architecture Standard |
| EA-344 | Enterprise Workflow Architecture Standard |

---

# Architecture Compliance

This standard defines the Enterprise Messaging Architecture.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Infrastructure Layer principles are inherited from EA-320.

Enterprise Integration Architecture principles are inherited from EA-340.

Enterprise API Architecture principles are inherited from EA-341.

All Enterprise Messaging implementations shall conform to this standard.

---

# 1. Purpose

The purpose of this standard is to define the Enterprise Architecture governing asynchronous messaging throughout the MFM Enterprise Platform.

The Enterprise Messaging Architecture shall

- standardize message-based communication
- enable loose coupling
- improve scalability
- improve resilience
- support reliable delivery
- simplify system integration
- remain technology independent

Messaging shall provide reliable communication without requiring synchronous dependencies between systems.

---

# 2. Scope

This standard applies to every message exchanged within the Enterprise Platform.

It governs

- message brokers
- queues
- topics
- publish-subscribe communication
- point-to-point messaging
- message routing
- message delivery
- retry mechanisms
- dead-letter handling
- messaging governance

The standard applies independently of messaging technology, broker implementation or communication protocol.

---

# 3. Enterprise Messaging Definition

Enterprise Messaging is the asynchronous exchange of commands, notifications and information between Enterprise systems through governed messaging infrastructure.

Enterprise Messaging includes

- command messages
- event notifications
- queue-based communication
- topic-based communication
- background processing
- workflow messaging
- system notifications
- integration messaging

Messaging shall enable reliable communication while preserving autonomy between communicating systems.

---

# 4. Enterprise Messaging Objectives

The Enterprise Messaging Architecture shall

- reduce coupling
- improve reliability
- improve scalability
- improve fault tolerance
- simplify distributed processing
- support eventual consistency
- enable operational resilience

Messaging capabilities shall be reusable Enterprise Infrastructure services.

---

# 5. Enterprise Messaging Responsibilities

The Enterprise Messaging Architecture is responsible for

- messaging standards
- broker governance
- routing
- message delivery
- retry handling
- dead-letter management
- monitoring
- lifecycle management
- security

Enterprise Messaging shall never expose infrastructure-specific behavior to business applications.

Messaging shall remain transparent, governed and technology independent.

---

# End of Part 1

---

# 6. Enterprise Messaging Architecture

The Enterprise Messaging Architecture provides the standardized framework for asynchronous communication between Enterprise applications, domains and infrastructure services.

The architecture consists of

- message brokers
- queues
- topics
- publishers
- consumers
- routing services
- dead-letter handling
- retry services
- monitoring services
- governance services

Enterprise applications shall exchange asynchronous information exclusively through approved Enterprise Messaging services.

Business logic shall remain independent of messaging technologies.

---

# 7. Message Brokers

Enterprise Messaging shall utilize approved Message Broker platforms.

Message Brokers are responsible for

- message transport
- routing
- delivery guarantees
- queue management
- topic management
- consumer coordination
- persistence where required
- monitoring support

The Message Broker shall remain an Infrastructure Layer component.

Applications shall never depend directly upon broker-specific APIs where Enterprise abstractions exist.

Broker implementations shall be replaceable without impacting business applications.

---

# 8. Queues

Queues provide reliable point-to-point message delivery.

Queue-based messaging shall be used for

- command processing
- background jobs
- workflow execution
- task distribution
- asynchronous processing
- integration requests

Queue processing shall

- preserve message durability where required
- support retry mechanisms
- support dead-letter handling
- support load balancing
- support horizontal scalability

Each message shall normally be processed by a single consumer.

---

# 9. Topics

Topics provide publish-subscribe communication.

Topic-based messaging shall be used when multiple consumers require the same information.

Typical use cases include

- business notifications
- domain events
- operational events
- integration events
- audit notifications
- monitoring events

Topic subscribers shall remain independent of one another.

Publishers shall not require knowledge of subscribing systems.

---

# 10. Publish/Subscribe

Publish/Subscribe shall be the preferred messaging pattern for Enterprise event distribution.

Publishers shall

- publish standardized messages
- remain independent of subscribers
- avoid consumer-specific behavior
- publish immutable messages whenever practical

Subscribers shall

- independently process messages
- tolerate duplicate delivery
- support retry processing
- remain loosely coupled

The Publish/Subscribe model shall maximize scalability and Enterprise autonomy.

---

# 11. Point-to-Point Messaging

Point-to-Point Messaging shall be used when work is assigned to exactly one processing component.

Typical scenarios include

- command execution
- scheduled processing
- asynchronous business operations
- document generation
- import processing
- export processing

Point-to-Point Messaging shall

- guarantee controlled delivery
- support retry mechanisms
- preserve transactional integrity where required
- isolate processing failures

Queue ownership shall be clearly defined.

---

# 12. Dependency Rules

Enterprise Messaging implementations shall comply with Enterprise dependency inversion principles.

Messaging services may depend upon

- Enterprise Integration Services
- Enterprise Security Services
- Enterprise Identity Services
- Infrastructure Services
- Monitoring Services

Business applications shall never depend directly upon

- broker implementations
- queue technologies
- topic implementations
- transport protocols
- vendor-specific messaging APIs

All dependencies shall flow toward Enterprise abstractions rather than infrastructure implementations.

---

# End of Part 2

---

# 13. Message Delivery Guarantees

Enterprise Messaging shall provide delivery guarantees appropriate to the business capability.

Supported delivery models include

- at-most-once delivery
- at-least-once delivery
- exactly-once delivery where supported and justified
- durable messaging
- persistent messaging
- transient messaging where acceptable

The selected delivery model shall balance

- business criticality
- reliability
- performance
- scalability
- operational complexity

Business-critical processes shall never rely upon best-effort message delivery.

---

# 14. Retry Policies

Enterprise Messaging shall implement standardized retry policies.

Retry mechanisms shall support

- automatic retries
- configurable retry intervals
- exponential backoff
- retry limits
- transient failure detection
- permanent failure detection

Retry processing shall

- avoid message duplication where possible
- prevent infinite retry loops
- generate operational alerts after repeated failures
- preserve message traceability

Retry policies shall be governed centrally across the Enterprise Platform.

---

# 15. Dead-Letter Queues

Dead-Letter Queues (DLQs) shall be implemented for all critical messaging infrastructures.

Messages shall be moved to a Dead-Letter Queue when

- retry limits are exceeded
- message validation fails
- processing repeatedly fails
- message corruption is detected
- routing cannot be completed

Dead-Letter Queues shall support

- operational investigation
- controlled replay
- auditing
- root cause analysis
- incident response

Dead-letter processing shall never become part of normal business operations.

---

# 16. Idempotency

Enterprise message processing shall be idempotent whenever practical.

Repeated delivery of the same message shall not produce inconsistent business results.

Idempotent processing may utilize

- unique message identifiers
- correlation identifiers
- duplicate detection
- processing history
- business transaction identifiers

Applications shall assume that duplicate messages may occur.

Idempotency shall be considered a mandatory design principle for distributed Enterprise systems.

---

# 17. Message Ordering

Message ordering requirements shall be explicitly defined for every messaging solution.

Where ordering is required, messaging infrastructure shall preserve

- causal ordering
- partition ordering
- workflow ordering
- business sequence integrity

Applications shall not assume global ordering unless explicitly guaranteed by the messaging platform.

Ordering constraints shall be minimized to improve scalability.

---

# 18. Monitoring

Enterprise Messaging shall support continuous operational monitoring.

Monitoring shall include

- queue depth
- topic activity
- broker availability
- message throughput
- delivery latency
- retry counts
- dead-letter volume
- consumer health
- publisher health
- routing failures
- processing failures

Monitoring shall support

- operational management
- capacity planning
- incident response
- governance
- compliance
- service optimization

Operational metrics shall be retained according to Enterprise monitoring policies.

---

# 19. Security

Enterprise Messaging shall comply with Enterprise Security Architecture.

Messaging security shall include

- authentication
- authorization
- encrypted transport
- message integrity
- payload encryption where required
- audit logging
- security classification
- non-repudiation where applicable

Only authorized publishers and consumers shall access Enterprise messaging infrastructure.

Sensitive business information shall be protected throughout the messaging lifecycle.

---

# 20. Enterprise Messaging Anti-Patterns

The following architectural anti-patterns are prohibited.

## Shared Queue Ownership

Multiple business domains shall not share ownership of the same business queue.

Ownership shall remain explicit.

---

## Consumer Knowledge

Publishers shall never require knowledge of individual message consumers.

Messaging shall remain loosely coupled.

---

## Infinite Retry Loops

Retry mechanisms shall never create endless processing cycles.

Retry limits shall always be enforced.

---

## Ignoring Dead-Letter Queues

Dead-Letter Queues shall be actively monitored and managed.

Accumulating failed messages without investigation is prohibited.

---

## Non-Idempotent Processing

Business-critical consumers shall not assume messages are delivered only once.

Duplicate delivery shall always be considered.

---

## Business Logic in Brokers

Message brokers shall provide infrastructure capabilities only.

Business logic shall remain within Enterprise applications and domain services.

---

# 21. Messaging Quality Principles

Every Enterprise Messaging implementation shall demonstrate

- reliability
- loose coupling
- scalability
- resiliency
- interoperability
- observability
- maintainability
- security
- traceability
- technology independence

Messaging quality shall be continuously measured and improved through governance, monitoring and operational feedback.

---

# End of Part 3

---

# 22. Implementation Guidelines

Enterprise Messaging implementations shall follow the architectural principles defined in EA-020, EA-111, EA-112, EA-320, EA-340 and EA-341.

Implementation shall ensure

- standardized message contracts
- centralized broker governance
- controlled queue ownership
- standardized topic management
- reliable delivery guarantees
- idempotent message processing
- resilient retry handling
- dead-letter management
- comprehensive monitoring
- technology independence

Enterprise Messaging implementations shall remain replaceable without requiring modifications to Enterprise business applications.

Messaging technologies shall implement Enterprise Architecture rather than define it.

---

# 23. Architecture Compliance

Enterprise Messaging implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-340 Enterprise Integration Architecture Standard
- EA-341 Enterprise API Architecture Standard
- this Enterprise Messaging Architecture Standard

Architecture reviews shall verify

- broker architecture
- queue ownership
- topic design
- publish-subscribe implementation
- point-to-point messaging
- delivery guarantees
- retry mechanisms
- dead-letter processing
- idempotent processing
- monitoring
- security
- dependency inversion

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 24. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-320 compliance verified | ☐ |
| EA-340 compliance verified | ☐ |
| EA-341 compliance verified | ☐ |
| Message contracts verified | ☐ |
| Queue ownership verified | ☐ |
| Topic configuration verified | ☐ |
| Delivery guarantees verified | ☐ |
| Retry policies verified | ☐ |
| Dead-Letter Queue management verified | ☐ |
| Idempotent processing verified | ☐ |
| Monitoring verified | ☐ |
| Security verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Messaging implementation shall satisfy all mandatory compliance requirements before being released into production.

---

# 25. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-340 Enterprise Integration Architecture Standard
- EA-341 Enterprise API Architecture Standard
- Enterprise Integration Patterns (Gregor Hohpe & Bobby Woolf)
- AMQP (Advanced Message Queuing Protocol)
- MQTT Version 5.0 Specification
- ISO/IEC 42010 Systems and Software Engineering — Architecture Description
- ISO/IEC 27001 Information Security Management Systems

---

# 26. Summary

This standard defines the Enterprise Messaging Architecture for the MFM Enterprise Platform.

The Enterprise Messaging Architecture provides the authoritative framework for asynchronous communication between Enterprise applications, services and infrastructure through governed messaging services.

This standard establishes

- Enterprise Messaging principles
- broker architecture
- queue architecture
- topic architecture
- publish-subscribe communication
- point-to-point messaging
- delivery guarantees
- retry mechanisms
- dead-letter management
- idempotent processing
- monitoring
- security
- implementation guidance
- governance requirements
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Infrastructure Layer principles are inherited from EA-320.

Enterprise Integration Architecture principles are inherited from EA-340.

Enterprise API Architecture principles are inherited from EA-341.

This standard shall be regarded as the authoritative Enterprise Messaging Architecture Standard for the MFM Enterprise Platform.

---

# 27. Future Evolution

This standard establishes the Enterprise foundation for resilient, scalable and loosely coupled messaging across the MFM Enterprise Platform.

Future architectural capabilities may include

- cloud-native messaging platforms
- event mesh integration
- intelligent message routing
- autonomous retry optimization
- AI-assisted message classification
- adaptive workload balancing
- policy-driven messaging governance
- cross-region message replication
- zero-trust messaging infrastructure
- autonomous operational observability

These capabilities shall continue to preserve

- interoperability
- reliability
- loose coupling
- governance
- security
- traceability
- scalability
- architectural consistency

The Enterprise Messaging Architecture shall evolve without compromising Enterprise reliability, resilience or technology independence.

---

# End of Document
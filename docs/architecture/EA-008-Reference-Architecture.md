# EA-008 Reference Architecture

| Property | Value |
|----------|-------|
| Document ID | EA-008 |
| Title | Reference Architecture |
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
| 1.0 | 2026-07-17 | Initial Architecture Baseline | Chief Enterprise Architect |

---

# Related Documents

This document shall be read together with the following architecture documents.

| Document | Description |
|----------|-------------|
| EA-001 | Enterprise Architecture Constitution |
| EA-002 | Canonical Domain Model |
| EA-003 | Enterprise Service Catalog |
| EA-004 | Capability Interaction |
| EA-005 | Naming Convention |
| EA-006 | Coding Standards |
| EA-007 | Enterprise Roadmap |

---

# 1. Purpose

The purpose of this document is to define the official technical reference architecture for the MFM Enterprise Platform.

This architecture provides a stable and long-term foundation for every software component developed within the platform.

The architecture shall ensure that MFM Enterprise remains maintainable, extensible and scalable over many years while preserving strict architectural consistency.

This document is normative.

All development SHALL comply with this document.

---

# 2. Scope

This document applies to every part of the platform including, but not limited to,

- Core Platform
- Enterprise Services
- Business Capabilities
- Maritime Capabilities
- Desktop Applications
- Reporting Components
- Future Web Applications
- Plugins
- Integrations
- APIs
- Infrastructure Components

The architecture is technology-aware but technology-independent wherever practical.

---

# 3. Architectural Vision

MFM Enterprise is designed as an Enterprise Platform rather than a traditional desktop application.

The platform shall support the complete operational lifecycle of maritime organisations including administration, restoration, finance, historical documentation and future digital services.

The architecture is designed to support future expansion without requiring fundamental redesign.

The architecture therefore prioritises:

- Maintainability
- Extensibility
- Loose Coupling
- High Cohesion
- Domain Ownership
- Enterprise Scalability
- Long-term Sustainability

---

# 4. Architectural Objectives

The platform shall achieve the following primary objectives.

## AO-001 Longevity

The platform shall support continuous development for decades without architectural degradation.

---

## AO-002 Modularity

Business functionality shall be divided into independent capabilities.

Capabilities shall own their own business logic and data.

---

## AO-003 Reusability

Platform services shall be reusable across every capability.

Business logic shall never be duplicated.

---

## AO-004 Separation of Concerns

User interface, workflow, business logic and persistence shall remain separated.

No architectural layer may assume responsibilities belonging to another layer.

---

## AO-005 Extensibility

Future capabilities shall be added without modifying existing capabilities whenever possible.

The architecture shall support plugin-based expansion.

---

## AO-006 Testability

Every architectural component shall be independently testable.

The architecture shall support:

- Unit Testing
- Integration Testing
- Architecture Testing
- End-to-End Testing

---

## AO-007 Security

Security shall be incorporated into every architectural layer.

Authentication, authorization and auditing are mandatory architectural concerns.

---

## AO-008 Traceability

Every important business action shall be traceable through audit records and domain events.

---

# 5. Architecture Overview

The MFM Enterprise Platform consists of three major architectural dimensions.

1. Business Architecture
2. Application Architecture
3. Technical Architecture

These dimensions operate together to provide a coherent enterprise platform.

```text
Business Architecture
        │
# 10. Enterprise Layer Responsibilities

This chapter defines the responsibilities, boundaries and interaction rules for every architectural layer within the MFM Enterprise Platform.

Each layer has one clearly defined purpose.

Responsibilities shall never overlap.

Business logic shall never migrate between layers.

---

# 10.1 Layer Overview

The architectural layers are organised as follows.

```text
Presentation
        │
        ▼
Reporting
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
Infrastructure
        │
        ▼
Persistence
```

Each layer communicates only with the layer directly below unless explicitly stated otherwise.

---

# 10.2 Presentation Layer

## Purpose

The Presentation Layer is responsible for all user interaction.

It provides the graphical user interface and translates user actions into workflow requests.

The Presentation Layer contains no business knowledge.

---

## Responsibilities

The Presentation Layer SHALL be responsible for:

- Windows
- Dialogs
- Navigation
- Menus
- Commands
- ViewModels
- Data Binding
- Input Validation
- Localization
- User Experience

---

## The Presentation Layer SHALL NOT

- execute business rules
- perform calculations
- access repositories
- execute SQL
- modify domain entities
- communicate directly with databases
- communicate directly with other capabilities

---

## Allowed Dependencies

Presentation

↓

Workflow

---

## Forbidden Dependencies

Presentation

↓

Repository

Presentation

↓

Database

Presentation

↓

Capability

Presentation

↓

Infrastructure

---

## Design Rules

Every window shall have a ViewModel.

Business entities shall never be exposed directly to the GUI.

The Presentation Layer shall communicate using DTOs.

---

# 10.3 Reporting Layer

## Purpose

The Reporting Layer generates information intended for presentation outside the application.

Reports are read-only.

---

## Responsibilities

The Reporting Layer SHALL generate

- PDF
- Excel
- CSV
- Word
- Printable reports
- Dashboards
- Statistics

---

## The Reporting Layer SHALL NOT

- modify business data
- execute workflows
- update domain entities
- perform persistence

---

## Allowed Dependencies

Reporting

↓

Feature APIs

---

## Forbidden Dependencies

Reporting

↓

Repository

Reporting

↓

Database

Reporting

↓

Workflow

---

## Design Rules

Reports shall use DTOs.

Reports shall never expose domain entities.

Large reports shall support asynchronous generation.

---

# 10.4 Workflow Layer

## Purpose

The Workflow Layer coordinates business processes.

It defines how business operations are executed.

It does not own business rules.

---

## Responsibilities

Examples include

- Create Member
- Renew Membership
- Register Invoice
- Restore Vessel
- Apply for Grant
- Register Inspection
- Archive Document

---

## Workflow Responsibilities

The Workflow Layer SHALL

- validate requests
- orchestrate capabilities
- control transactions
- publish events
- return DTOs

---

## Workflow SHALL NOT

- contain business rules
- access databases directly
- perform SQL
- render GUI

---

## Allowed Dependencies

Workflow

↓

Feature API

---

## Forbidden Dependencies

Workflow

↓

Repository

Workflow

↓

Database

---

## Example

```text
User

↓

Workflow

↓

Membership API

↓

Contact API

↓

Finance API

↓

Notification
```

---

# 10.5 Feature API Layer

## Purpose

Feature APIs expose business capabilities through stable contracts.

Feature APIs isolate capabilities from each other.

---

## Responsibilities

The Feature API SHALL

- expose use cases
- return DTOs
- validate contracts
- hide implementation details

---

## Feature APIs SHALL NOT

- expose repositories
- expose domain entities
- expose infrastructure

---

## Allowed Dependencies

Feature API

↓

Capability

---

## Forbidden Dependencies

Feature API

↓

Database

Feature API

↓

Repository

---

## Example

MembershipFeatureAPI

ProjectFeatureAPI

FinanceFeatureAPI

DocumentFeatureAPI

VolunteerFeatureAPI

VesselFeatureAPI

---

# 10.6 Capability Layer

## Purpose

Capabilities implement business functionality.

Each capability owns exactly one business domain.

---

## Responsibilities

A capability contains

- Domain Model
- Domain Services
- Factories
- Policies
- Repository Interfaces
- Application Services
- Domain Events

---

## Capability SHALL NOT

- know database technology
- access another capability's repository
- access GUI
- generate reports

---

## Ownership

Each capability owns

Business Rules

Business Entities

Business Validation

Business Events

Business Policies

---

## Examples

Membership

Finance

Documents

Projects

Assets

Heritage

Maintenance

Restoration

---

# 10.7 Infrastructure Layer

## Purpose

Infrastructure provides technical implementations required by the platform.

Infrastructure is replaceable.

---

## Responsibilities

Infrastructure implements

- SQLAlchemy
- File Storage
- OCR
- Email
- Logging
- Configuration
- Search
- Cache
- Authentication Providers
- External Integrations

---

## Infrastructure SHALL NOT

contain business rules.

---

## Design Principle

Infrastructure depends on Domain.

Domain never depends on Infrastructure.

---

# 10.8 Persistence Layer

## Purpose

Persistence stores information.

Nothing more.

---

## Responsibilities

Persistence includes

- SQLite
- PostgreSQL
- Blob Storage
- File System
- Object Storage

---

## Persistence SHALL NOT

- validate business rules
- calculate values
- execute workflows
- communicate with GUI

---

# 11. Dependency Matrix

| Layer | Allowed Dependencies |
|--------|----------------------|
| Presentation | Workflow |
| Reporting | Feature API |
| Workflow | Feature API |
| Feature API | Capability |
| Capability | Infrastructure |
| Infrastructure | Persistence |
| Persistence | None |

---

# 12. Architectural Integrity

Architectural integrity shall always have higher priority than implementation speed.

Temporary shortcuts shall never become permanent architecture.

If implementation pressure conflicts with architectural principles, the architecture shall prevail.

Every architectural deviation shall require explicit approval from the Chief Enterprise Architect and shall be documented as an Architecture Decision Record (ADR).

---

# End of Part 2

---

# 13. Logical Architecture

## 13.1 Overview

The logical architecture defines how the MFM Enterprise Platform is decomposed into autonomous functional units.

Each unit has a clearly defined responsibility.

Each unit owns its own business rules.

Each unit communicates only through approved architectural contracts.

The logical architecture is divided into three primary categories.

- Platform
- Business Capabilities
- Enterprise Services

```text
                MFM Enterprise

                     │

      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼

 Platform      Business Capabilities    Enterprise Services
```

---

# 13.2 Platform

The Platform provides reusable technical functionality.

The Platform contains no business-specific knowledge.

Platform components shall be reusable by every capability.

The Platform consists of the following areas.

| Component | Responsibility |
|------------|----------------|
| Common | Shared abstractions |
| Configuration | Configuration Management |
| Security | Authentication and Authorization |
| Audit | Audit Trail |
| Logging | Logging Infrastructure |
| Search | Enterprise Search |
| Media | File Management |
| Notifications | Internal Notifications |
| Localization | Languages |
| Workflow | Workflow Infrastructure |

Business logic shall never exist inside Platform components.

---

# 13.3 Business Capabilities

Business functionality is organised into autonomous capabilities.

Every capability owns

- Domain Model
- Business Rules
- Repository Interfaces
- Feature API
- Events
- DTOs

Capabilities remain independent.

No capability owns another capability.

---

# 13.4 Capability Catalogue

The following capabilities constitute Version 1 of the MFM Enterprise Platform.

| Capability | Primary Responsibility |
|------------|------------------------|
| Contact | Persons and Organisations |
| Membership | Members and Memberships |
| Finance | Accounting |
| Document | Documents |
| Projects | Projects |
| Events | Events |
| Communication | Communication |
| Volunteers | Volunteers |
| Assets | Physical Assets |
| Vessel | Ships and Boats |
| Heritage | Cultural Heritage |
| Maintenance | Maintenance Planning |
| Restoration | Restoration Projects |
| Grants | Grant Applications |

---

# 13.5 Capability Ownership

Each capability owns exactly one business domain.

Ownership includes

- Entities
- Business Rules
- Validation
- Events
- Repository Interfaces

Ownership never overlaps.

Example

Contact owns

- Person
- Organisation
- Address
- Phone
- Email

Finance owns

- Ledger
- Voucher
- Journal
- Fiscal Year
- Account

Projects owns

- Project
- Milestone
- Activity
- Budget

---

# 13.6 Capability Independence

Capabilities are autonomous.

Capabilities communicate through Feature APIs.

Capabilities never share repositories.

Capabilities never access another capability's persistence.

Example

Allowed

Membership

↓

Contact Feature API

Forbidden

Membership

↓

Contact Repository

---

# 14. Enterprise Services

Enterprise Services provide shared functionality.

Unlike capabilities, Enterprise Services own no business domain.

They provide technical services to the platform.

---

# 14.1 Identity Service

Responsibilities

- Global Identifiers
- UUID Generation
- Entity Identity
- Version Identity

Used by

Every Capability.

---

# 14.2 Relationship Service

Responsibilities

Maintain relationships between Enterprise Entities.

Examples

Person

↓

Member

↓

Project

↓

Document

↓

Invoice

---

# 14.3 Timeline Service

Responsibilities

Maintain historical timelines.

Every Enterprise Entity shall automatically receive a timeline.

Example

Create

↓

Modify

↓

Approve

↓

Archive

---

# 14.4 Audit Service

Responsibilities

Record every significant business action.

Examples

Create

Update

Delete

Approve

Reject

Export

Login

---

# 14.5 Notification Service

Responsibilities

Internal Notifications

Email

Future SMS

Future Push Notifications

---

# 14.6 Media Service

Responsibilities

Images

PDF

Video

CAD

Scanned Documents

Attachments

---

# 14.7 Search Service

Responsibilities

Enterprise-wide indexing.

Capabilities shall never implement their own search engines.

---

# 14.8 Configuration Service

Responsibilities

Platform configuration.

Capability configuration.

User preferences.

Feature flags.

---

# 14.9 Localization Service

Responsibilities

Languages.

Date formats.

Currencies.

Regional settings.

Translations.

---

# 14.10 AI Service

Responsibilities

Document summarisation.

Semantic Search.

OCR Analysis.

Knowledge Assistant.

Future decision support.

AI never replaces business rules.

---

# 15. Architectural Communication

Communication follows strict rules.

```text
Presentation

↓

Workflow

↓

Feature API

↓

Capability

↓

Enterprise Services

↓

Infrastructure
```

No component may bypass Feature APIs.

---

# 16. Enterprise Entity Flow

A typical business transaction follows the sequence below.

```text
User

↓

Presentation

↓

Workflow

↓

Feature API

↓

Capability

↓

Repository

↓

Database

↓

Domain Event

↓

Audit

↓

Notification

↓

DTO

↓

Presentation
```

Every business operation follows this pattern unless explicitly documented otherwise.

---

# End of Part 3

---

# 17. Physical Architecture

## 17.1 Overview

The physical architecture defines how software components are deployed across different editions of the MFM Enterprise Platform.

The logical architecture described in previous chapters remains identical across all deployment models.

Only the physical distribution of components changes.

The following deployment models are supported.

| Deployment | Purpose |
|------------|---------|
| Desktop | Single user |
| Team | Small organisations |
| Enterprise | Multi-user organisation |
| Cloud | Internet-hosted platform |

---

# 17.2 Desktop Edition

The Desktop Edition is the reference implementation.

Characteristics

- Single user
- Local database
- Local file storage
- No server required
- Offline capable

Architecture

```text
+----------------------+
|      PySide6 GUI     |
+----------------------+
           │
           ▼
+----------------------+
|      Workflow        |
+----------------------+
           │
           ▼
+----------------------+
|    Feature APIs      |
+----------------------+
           │
           ▼
+----------------------+
|    Capabilities      |
+----------------------+
           │
           ▼
+----------------------+
|   Infrastructure     |
+----------------------+
           │
           ▼
+----------------------+
|      SQLite          |
+----------------------+
```

---

# 17.3 Team Edition

The Team Edition allows multiple users to work against a shared database.

Characteristics

- Shared PostgreSQL database
- Shared media storage
- Central backup
- Multiple concurrent users

The application architecture remains unchanged.

Only the persistence layer differs.

---

# 17.4 Enterprise Edition

Enterprise introduces dedicated infrastructure services.

Additional components include

- PostgreSQL
- Object Storage
- Search Index
- Notification Server
- Background Workers

Business capabilities remain unchanged.

---

# 17.5 Cloud Edition

Cloud deployment separates client and server.

Example architecture

```text
Browser / Desktop

        │

        ▼

REST / RPC Gateway

        │

        ▼

Application Services

        │

        ▼

Business Capabilities

        │

        ▼

Infrastructure Services

        │

        ▼

PostgreSQL
```

The domain model remains identical.

---

# 18. Cross-Cutting Concerns

Cross-cutting concerns apply to every capability.

Capabilities shall never implement these independently.

---

# 18.1 Logging

Every capability shall use the Platform Logging Service.

Logging levels

- Trace
- Debug
- Information
- Warning
- Error
- Critical

Direct use of print() is prohibited.

---

# 18.2 Configuration

Configuration shall be provided through the Configuration Service.

Configuration shall never be hardcoded.

Supported sources

- TOML
- Environment Variables
- User Settings

---

# 18.3 Validation

Validation occurs on three levels.

| Level | Responsibility |
|---------|----------------|
| Presentation | Input validation |
| Workflow | Process validation |
| Domain | Business validation |

Business validation always has highest priority.

---

# 18.4 Localization

All user-visible text shall support translation.

The platform shall never contain hardcoded UI strings.

Dates, numbers and currencies shall be culture-aware.

---

# 18.5 Error Handling

Exceptions shall never be shown directly to users.

Errors shall be

- Logged
- Classified
- Wrapped
- Presented as user-friendly messages

---

# 18.6 Auditing

Every business transaction shall be auditable.

Audit information shall include

- Timestamp
- User
- Entity
- Action
- Previous Value
- New Value

Audit records are immutable.

---

# 19. Technology Standards

The following technologies are approved for Version 1.

| Area | Technology |
|------|------------|
| Language | Python |
| GUI | PySide6 |
| ORM | SQLAlchemy |
| Database | SQLite / PostgreSQL |
| Configuration | TOML |
| Testing | pytest |
| Packaging | setuptools |
| Linting | Ruff |
| Formatting | Black (optional policy) |

Introduction of additional frameworks requires architectural approval.

---

# 20. Coding Conventions

The architecture requires

- Static typing
- Type hints
- Dataclasses where appropriate
- Dependency Injection
- Repository Pattern
- Factory Pattern
- Value Objects
- Domain Events

The following are prohibited.

- Global mutable state
- Circular dependencies
- Business logic in GUI
- SQL in Presentation
- SQL in Domain
- Business logic in repositories

---

# End of Part 4

---

# 21. Quality Attribute Scenarios

## 21.1 Purpose

Quality attributes describe how the architecture shall behave under defined conditions.

Every architectural decision shall support one or more quality attributes.

The following quality attributes are considered mandatory for the MFM Enterprise Platform.

- Maintainability
- Extensibility
- Reliability
- Availability
- Security
- Performance
- Testability
- Scalability
- Portability

---

# 21.2 Maintainability

## Requirement

The platform shall be maintainable throughout its entire lifecycle.

## Scenario

Given a developer needs to introduce a new capability,

When the capability follows the Capability Blueprint,

Then no existing capability shall require modification.

---

# 21.3 Extensibility

## Requirement

New functionality shall be introduced with minimal impact.

## Scenario

Given a new Maritime capability,

When it is added,

Then existing capabilities continue operating unchanged.

---

# 21.4 Reliability

Business data shall never become inconsistent because of software architecture.

Transactions affecting multiple entities shall either

- complete successfully

or

- rollback completely.

Partial commits are prohibited.

---

# 21.5 Performance

The architecture shall prioritise correctness before optimisation.

Performance optimisation shall never violate architectural principles.

Performance improvements shall be measurable.

---

# 21.6 Security

Every business operation shall execute within a defined security context.

No anonymous modification of business entities is permitted.

Every operation shall be attributable to an authenticated identity.

---

# 21.7 Testability

Every architectural component shall be independently testable.

The architecture shall support

- Unit Tests
- Integration Tests
- Architecture Tests
- Acceptance Tests

---

# 22. Architecture Governance

## 22.1 Purpose

Architecture Governance ensures long-term consistency across the platform.

Every contributor shares responsibility for maintaining architectural integrity.

---

## 22.2 Architectural Authority

The Enterprise Architecture documentation constitutes the governing authority for software architecture.

Implementation shall conform to the architecture.

The architecture shall not be modified to accommodate poor implementations.

---

## 22.3 Architecture Decision Records

Every significant architectural decision shall be documented.

Each Architecture Decision Record (ADR) shall include

- Context
- Decision
- Alternatives
- Consequences
- Approval

ADR documents shall be stored in

```text
docs/architecture/adr/
```

---

## 22.4 Architectural Review

The following changes require architectural review.

- New Platform Services
- New Enterprise Services
- New Capability Types
- Cross-Capability Dependencies
- Public API Changes
- Infrastructure Replacement

---

## 22.5 Versioning

Architecture documents shall be version controlled.

Major architectural changes require a new document version.

Minor corrections shall update the current version.

---

# 23. Architecture Compliance

## 23.1 Compliance Rules

Every implementation shall comply with the Enterprise Architecture.

Compliance shall be verified during

- Code Review
- Architecture Review
- Continuous Integration
- Release Approval

---

## 23.2 Mandatory Requirements

Every capability shall

- follow the defined layer model
- expose Feature APIs
- own exactly one business domain
- provide automated tests
- implement audit logging
- support localisation

---

## 23.3 Prohibited Practices

The following practices are prohibited.

- Direct SQL from Presentation
- Business logic inside repositories
- Cross-capability database access
- Circular dependencies
- Duplicate business rules
- Hardcoded configuration
- Hidden dependencies

---

# 24. Future Evolution

The architecture has been designed for gradual expansion.

Planned architectural directions include

- Public REST APIs
- Plugin Marketplace
- Knowledge Graph
- Digital Twin
- AI-assisted workflows
- Mobile applications
- Public Heritage Portal

These future capabilities shall extend the architecture without violating existing principles.

---

# 25. Glossary

| Term | Definition |
|------|------------|
| Capability | Autonomous business module |
| Enterprise Service | Shared technical service |
| Feature API | Public interface to a capability |
| Workflow | Business process orchestration |
| DTO | Data Transfer Object |
| Domain Event | Immutable business event |
| Repository | Persistence abstraction |
| Aggregate | Consistency boundary in the domain model |
| Value Object | Immutable domain object |
| ADR | Architecture Decision Record |

---

# 26. References

This document references the following architecture documents.

- EA-001 Enterprise Architecture Constitution
- EA-002 Canonical Domain Model
- EA-003 Enterprise Service Catalog
- EA-004 Capability Interaction
- EA-005 Naming Convention
- EA-006 Coding Standards
- EA-007 Enterprise Roadmap

Additional documents shall reference this document as the primary architectural specification.

---

# Appendix A – Layer Summary

| Layer | Primary Responsibility |
|--------|------------------------|
| Presentation | User interaction |
| Reporting | Read-only output |
| Workflow | Process orchestration |
| Feature API | Capability contracts |
| Capability | Business rules |
| Infrastructure | Technical implementation |
| Persistence | Data storage |

---

# Appendix B – Dependency Summary

```text
Presentation
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
Infrastructure
        │
        ▼
Persistence
```

Dependencies shall always follow this direction.

---

# Appendix C – Final Statement

The MFM Enterprise Reference Architecture establishes the technical foundation for the entire platform.

All future development shall align with the principles, structures and constraints defined within this document.

The architecture is intended to evolve through controlled governance while preserving consistency, maintainability and long-term sustainability.

End of Document.
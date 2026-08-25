# EA-351 Master Data Management (MDM) Standard

| Property | Value |
|----------|-------|
| Document ID | EA-351 |
| Document Type | Enterprise Architecture Standard |
| Title | Master Data Management (MDM) Standard |
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
| 1.x | Previous | Initial Master Data Management Guidance | Enterprise Architecture Team |
| 2.0 | 2026-07-27 | Complete Enterprise Master Data Management Standard aligned with EA-020, EA-111, EA-112, EA-320, EA-340 through EA-345 and EA-350 | Chief Enterprise Architect |

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
| EA-342 | Enterprise Messaging Architecture Standard |
| EA-343 | Enterprise Event Streaming Architecture Standard |
| EA-344 | Enterprise Workflow Architecture Standard |
| EA-345 | Enterprise Business Process Architecture Standard |
| EA-350 | Enterprise Data Architecture Standard |

---

# Architecture Compliance

This standard defines the Enterprise Master Data Management Architecture.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Infrastructure Layer principles are inherited from EA-320.

Enterprise Integration Architecture principles are inherited from EA-340 through EA-345.

Enterprise Data Architecture principles are inherited from EA-350.

All Enterprise Master Data implementations shall conform to this standard.

---

# 1. Purpose

The purpose of this standard is to define the Enterprise Architecture governing Master Data Management (MDM) throughout the MFM Enterprise Platform.

The Enterprise MDM Architecture shall

- establish authoritative master data
- eliminate duplicate business information
- improve data quality
- strengthen governance
- enable interoperability
- support analytics and AI
- remain technology independent

Master Data Management shall ensure that shared business entities have one trusted representation across the Enterprise.

---

# 2. Scope

This standard applies to all Enterprise Master Data.

It governs

- master data domains
- systems of record
- golden records
- reference data
- synchronization
- stewardship
- ownership
- lifecycle management
- governance
- quality management

The standard applies independently of implementation technology, database platform or cloud provider.

---

# 3. Master Data Definition

Master Data represents the core business entities shared across multiple Enterprise systems.

Examples include

- members
- users
- organizations
- vessels
- suppliers
- customers
- employees
- products
- financial accounts
- locations

Master Data shall be regarded as authoritative Enterprise information requiring centralized governance.

---

# 4. Master Data Objectives

The Enterprise Master Data Management Architecture shall

- establish a single source of truth
- improve consistency
- eliminate duplication
- improve interoperability
- strengthen governance
- improve traceability
- support regulatory compliance
- support Enterprise analytics
- support AI capabilities

Master Data shall remain authoritative throughout its complete lifecycle.

---

# 5. Master Data Responsibilities

The Enterprise Master Data Management Architecture is responsible for

- master data domains
- systems of record
- golden records
- stewardship
- ownership
- synchronization
- governance
- lifecycle management
- compliance
- quality management

Each Master Data Domain shall have

- one accountable owner
- one authoritative system of record
- documented governance policies
- defined quality objectives
- assigned data stewards

---

# End of Part 1

---

# 6. Master Data Architecture

The Enterprise Master Data Architecture provides the standardized framework for managing authoritative business information across the MFM Enterprise Platform.

The architecture consists of

- master data domains
- systems of record
- golden records
- reference data
- synchronization services
- stewardship
- governance services
- quality management
- lifecycle management
- metadata integration

Master Data Architecture shall ensure that shared business entities are managed consistently throughout the Enterprise.

Business meaning shall always take precedence over technical implementation.

---

# 7. Master Data Domains

Enterprise Master Data shall be organized into clearly defined domains.

Typical Master Data Domains include

- Member
- User
- Organization
- Vessel
- Supplier
- Customer
- Employee
- Financial Account
- Asset
- Location
- Currency
- Country
- Classification
- Tax Code

Each Master Data Domain shall

- have one accountable owner
- define one authoritative System of Record
- publish standardized interfaces
- define quality objectives
- support governance
- maintain lifecycle documentation

No Master Data Domain shall overlap another without documented governance approval.

---

# 8. Systems of Record

Every Master Data Domain shall define exactly one authoritative System of Record.

The System of Record is responsible for

- creating master data
- maintaining master data
- approving updates
- publishing authoritative information
- ensuring quality
- maintaining audit history

Other Enterprise systems may consume Master Data but shall not become alternative authoritative sources.

Synchronization shall always originate from the designated System of Record.

---

# 9. Golden Records

Each Master Data entity shall have one Golden Record.

A Golden Record represents the trusted, consolidated and authoritative representation of a business entity.

Golden Records shall

- eliminate duplicates
- consolidate validated information
- maintain business identity
- preserve history
- support auditability
- improve interoperability

Golden Records shall remain uniquely identifiable across the Enterprise.

Identity resolution rules shall be centrally governed.

---

# 10. Reference Data

Reference Data provides standardized values used consistently across Enterprise systems.

Examples include

- countries
- currencies
- languages
- ports
- classifications
- vessel types
- accounting dimensions
- tax categories
- status codes
- organizational units

Reference Data shall

- be centrally governed
- be version controlled
- remain reusable
- support interoperability
- remain consistent across all consuming systems

Reference Data shall not be duplicated without governance approval.

---

# 11. Master Data Synchronization

Master Data shall be synchronized through approved Enterprise integration mechanisms.

Synchronization may use

- APIs
- messaging
- event streaming
- batch synchronization
- data replication
- scheduled synchronization

Synchronization shall

- preserve data integrity
- preserve auditability
- prevent conflicts
- support eventual consistency where appropriate
- support recovery after failures

Direct database synchronization between applications is prohibited unless explicitly approved by Enterprise Architecture.

---

# 12. Dependency Rules

Master Data implementations shall comply with Enterprise dependency inversion principles.

Master Data services may depend upon

- Domain Services
- Enterprise APIs
- Messaging Services
- Event Streaming Services
- Security Services
- Infrastructure Services
- Enterprise Data Services

Master Data implementations shall never depend directly upon

- user interfaces
- reporting tools
- workflow engines
- analytics platforms
- proprietary synchronization mechanisms
- vendor-specific database features

Master Data Architecture shall remain stable despite changes in implementation technologies.

---

# End of Part 2

---

# 13. Data Stewardship

Every Master Data Domain shall have one or more designated Data Stewards.

Data Stewards are responsible for

- maintaining data quality
- validating business rules
- resolving data conflicts
- approving changes
- monitoring data quality metrics
- maintaining metadata
- supporting governance
- coordinating with Process Owners
- ensuring regulatory compliance

Data Stewards shall work closely with Domain Owners to ensure that Master Data remains accurate, complete and authoritative.

Stewardship responsibilities shall be formally documented.

---

# 14. Master Data Quality

Enterprise Master Data shall maintain measurable quality standards.

Master Data Quality dimensions shall include

- accuracy
- completeness
- consistency
- uniqueness
- validity
- integrity
- timeliness
- availability

Quality controls shall include

- duplicate detection
- validation rules
- mandatory attributes
- identity verification
- business rule enforcement
- exception management

Master Data Quality shall be continuously measured and reported.

Quality thresholds shall be approved through Enterprise Governance.

---

# 15. Governance

Enterprise Master Data shall operate under centralized governance.

Governance shall include

- ownership
- stewardship
- lifecycle management
- policy management
- metadata governance
- quality management
- compliance management
- architecture governance
- audit governance
- change management

Every Master Data Domain shall define

- governance policies
- approval procedures
- ownership model
- stewardship responsibilities
- quality objectives
- lifecycle rules
- synchronization policies

Master Data Governance shall ensure consistent management across all Enterprise systems.

---

# 16. Security

Master Data shall comply with Enterprise Security Architecture.

Security controls shall include

- authentication
- authorization
- role-based access control
- least privilege
- encryption
- audit logging
- integrity verification
- confidentiality
- segregation of duties
- monitoring

Sensitive Master Data shall be protected

- at rest
- in transit
- during processing

Security policies shall align with Enterprise Data Classification requirements defined in EA-350.

---

# 17. Compliance

Enterprise Master Data shall comply with

- applicable legislation
- contractual obligations
- Enterprise policies
- Enterprise Architecture standards
- privacy regulations
- audit requirements
- retention policies
- security requirements

Compliance activities shall include

- evidence collection
- audit trails
- policy enforcement
- traceability
- reporting
- exception management

Compliance shall be continuously monitored throughout the Master Data lifecycle.

---

# 18. Monitoring

Enterprise Master Data shall support continuous operational monitoring.

Monitoring shall include

- data quality metrics
- synchronization status
- duplicate detection
- governance violations
- stewardship activities
- security events
- audit events
- replication status
- lifecycle events
- compliance status

Monitoring shall support

- Enterprise Operations
- Enterprise Governance
- Enterprise Analytics
- Enterprise AI
- regulatory auditing
- operational improvement

Monitoring information shall be retained according to Enterprise retention policies.

---

# 19. Master Data Anti-Patterns

The following architectural anti-patterns are prohibited.

## Multiple Systems of Record

Each Master Data Domain shall define exactly one authoritative System of Record.

Competing authoritative systems are prohibited.

---

## Duplicate Golden Records

A business entity shall never have multiple Golden Records.

Identity resolution shall eliminate duplicate authoritative records.

---

## Missing Ownership

Every Master Data Domain shall have documented ownership and stewardship.

Unowned Master Data is prohibited.

---

## Uncontrolled Synchronization

Master Data synchronization shall occur only through approved Enterprise integration mechanisms.

Direct database synchronization between applications is prohibited unless formally approved.

---

## Poor Master Data Quality

Master Data shall not knowingly contain unmanaged quality deficiencies.

Quality issues shall be measured, reported and corrected through established governance procedures.

---

## Missing Governance

Enterprise Master Data shall never exist outside centralized governance.

Governance shall apply throughout the complete Master Data lifecycle.

---

# 20. Master Data Quality Principles

Every Enterprise Master Data implementation shall demonstrate

- accuracy
- completeness
- consistency
- uniqueness
- integrity
- traceability
- governance
- interoperability
- security
- auditability

Master Data shall remain authoritative, trusted and reusable throughout its complete lifecycle.

---

# End of Part 3

---

# 21. Implementation Guidelines

Enterprise Master Data implementations shall follow the architectural principles defined in EA-020, EA-111, EA-112, EA-320 and EA-340 through EA-350.

Implementation shall ensure

- standardized Master Data domains
- centralized governance
- clearly defined ownership
- designated Systems of Record
- unique Golden Records
- measurable data quality
- controlled synchronization
- comprehensive monitoring
- complete auditability
- technology independence

Master Data implementations shall remain independent of database vendors, cloud providers and integration technologies.

Technology shall implement Master Data Architecture rather than define it.

---

# 22. Architecture Compliance

Enterprise Master Data implementations shall comply with

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-340 Enterprise Integration Architecture Standard
- EA-341 Enterprise API Architecture Standard
- EA-342 Enterprise Messaging Architecture Standard
- EA-343 Enterprise Event Streaming Architecture Standard
- EA-344 Enterprise Workflow Architecture Standard
- EA-345 Enterprise Business Process Architecture Standard
- EA-350 Enterprise Data Architecture Standard
- this Master Data Management Standard

Architecture reviews shall verify

- Master Data domains
- Systems of Record
- Golden Records
- ownership
- stewardship
- synchronization
- governance
- quality management
- security
- compliance
- dependency inversion

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 23. Compliance Checklist

| Requirement | Status |
|-------------|--------|
| EA-020 compliance verified | ☐ |
| EA-111 compliance verified | ☐ |
| EA-112 compliance verified | ☐ |
| EA-320 compliance verified | ☐ |
| EA-340 compliance verified | ☐ |
| EA-341 compliance verified | ☐ |
| EA-342 compliance verified | ☐ |
| EA-343 compliance verified | ☐ |
| EA-344 compliance verified | ☐ |
| EA-345 compliance verified | ☐ |
| EA-350 compliance verified | ☐ |
| Master Data domains verified | ☐ |
| Systems of Record verified | ☐ |
| Golden Records verified | ☐ |
| Data stewardship verified | ☐ |
| Synchronization verified | ☐ |
| Data quality metrics verified | ☐ |
| Governance verified | ☐ |
| Security verified | ☐ |
| Compliance verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Master Data implementation shall satisfy all mandatory compliance requirements before being released into production.

---

# 24. References

- EA-020 Enterprise Architecture Common Requirements
- EA-111 Enterprise Architecture Blueprint
- EA-112 Enterprise Event Reference Architecture
- EA-320 Enterprise Infrastructure Layer Reference Architecture
- EA-340 Enterprise Integration Architecture Standard
- EA-341 Enterprise API Architecture Standard
- EA-342 Enterprise Messaging Architecture Standard
- EA-343 Enterprise Event Streaming Architecture Standard
- EA-344 Enterprise Workflow Architecture Standard
- EA-345 Enterprise Business Process Architecture Standard
- EA-350 Enterprise Data Architecture Standard
- DAMA-DMBOK (Data Management Body of Knowledge)
- ISO 8000 Data Quality
- ISO/IEC 11179 Metadata Registries
- ISO/IEC 27001 Information Security Management Systems
- ISO/IEC 42010 Systems and Software Engineering — Architecture Description

---

# 25. Summary

This standard defines the Enterprise Master Data Management Architecture for the MFM Enterprise Platform.

The Enterprise Master Data Management Architecture provides the authoritative framework for managing shared business entities across the Enterprise.

This standard establishes

- Master Data principles
- Master Data domains
- Systems of Record
- Golden Records
- Reference Data
- synchronization
- stewardship
- governance
- quality management
- security
- compliance
- monitoring
- implementation guidance
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Infrastructure Layer principles are inherited from EA-320.

Enterprise Integration Architecture principles are inherited from EA-340 through EA-345.

Enterprise Data Architecture principles are inherited from EA-350.

This standard shall be regarded as the authoritative Master Data Management Standard for the MFM Enterprise Platform.

---

# 26. Future Evolution

This standard establishes the Enterprise foundation for Master Data Management across the MFM Enterprise Platform.

Future architectural capabilities may include

- AI-assisted entity matching
- automated Golden Record creation
- intelligent duplicate detection
- semantic Master Data models
- autonomous data stewardship
- policy-driven synchronization
- federated Master Data management
- knowledge graph integration
- real-time quality scoring
- predictive data governance

These capabilities shall continue to preserve

- authoritative ownership
- interoperability
- governance
- traceability
- security
- auditability
- maintainability
- architectural consistency

The Enterprise Master Data Management Architecture shall evolve without compromising Enterprise governance, data integrity or technology independence.

---

# End of Document
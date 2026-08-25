# EA-363 Enterprise Cryptography & PKI Architecture Standard

| Property | Value |
|----------|-------|
| Document ID | EA-363 |
| Document Type | Enterprise Architecture Standard |
| Title | Enterprise Cryptography & PKI Architecture Standard |
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
| 1.x | Previous | Enterprise Cryptography Guidance | Enterprise Architecture Team |
| 2.0 | 2026-07-27 | Complete Enterprise Cryptography & PKI Architecture Standard aligned with EA-020 through EA-362 | Chief Enterprise Architect |

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
| EA-351 | Master Data Management (MDM) Standard |
| EA-352 | Enterprise Data Quality Standard |
| EA-353 | Metadata & Data Catalog Standard |
| EA-354 | Enterprise Data Governance Standard |
| EA-355 | Enterprise Data Lifecycle & Retention Standard |
| EA-356 | Enterprise Analytics Architecture Standard |
| EA-357 | Enterprise Business Intelligence Architecture Standard |
| EA-358 | Enterprise AI & Machine Learning Architecture Standard |
| EA-359 | Enterprise Knowledge Graph Architecture Standard |
| EA-360 | Enterprise Security Architecture Standard |
| EA-361 | Enterprise Identity & Access Management (IAM) Architecture Standard |
| EA-362 | Enterprise Zero Trust Architecture Standard |

---

# Architecture Compliance

This standard defines the Enterprise Cryptography & PKI Architecture for the MFM Enterprise Platform.

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Infrastructure Architecture principles are inherited from EA-320.

Integration Architecture principles are inherited from EA-340 through EA-345.

Enterprise Information Architecture principles are inherited from EA-350 through EA-359.

Enterprise Security Architecture principles are inherited from EA-360.

Enterprise Identity & Access Management Architecture principles are inherited from EA-361.

Enterprise Zero Trust Architecture principles are inherited from EA-362.

All Enterprise Cryptography implementations shall comply with this standard.

---

# 1. Purpose

The purpose of this standard is to establish the Enterprise Cryptography & PKI Architecture governing cryptographic services, certificate management, key management and digital trust across the MFM Enterprise Platform.

The Enterprise Cryptography Architecture shall

- protect confidentiality
- protect integrity
- protect authenticity
- support non-repudiation
- enable secure communications
- protect cryptographic keys
- establish trusted digital identities
- support regulatory compliance
- enable Zero Trust Architecture
- remain technology independent

Cryptographic capabilities shall be treated as shared Enterprise services.

---

# 2. Scope

This standard applies to all Enterprise cryptographic capabilities including

- encryption
- digital signatures
- certificates
- Public Key Infrastructure (PKI)
- key management
- Hardware Security Modules (HSM)
- secure communications
- secrets protection
- API cryptography
- workload cryptography
- cloud cryptography
- database encryption
- storage encryption
- messaging security
- AI platform cryptography

This standard applies regardless of deployment model or technology provider.

---

# 3. Enterprise Cryptographic Principles

Enterprise Cryptography shall be governed by the following principles.

## Cryptography by Design

Cryptographic controls shall be incorporated during architecture and solution design rather than added after implementation.

---

## Strong Cryptography

Only Enterprise-approved cryptographic algorithms, protocols and key lengths shall be used.

Weak or deprecated algorithms shall be prohibited.

---

## Centralized Key Governance

Cryptographic keys shall be generated, protected, rotated, archived and destroyed according to centralized Enterprise governance.

---

## Separation of Duties

Key generation, key management, certificate administration and cryptographic auditing shall remain separated whenever practical.

---

## Algorithm Agility

Cryptographic services shall support migration to new algorithms without requiring major architectural redesign.

---

## Technology Independence

Enterprise Cryptography Architecture shall remain independent of vendors, cloud providers and cryptographic products.

---

# 4. Enterprise Cryptography Objectives

The Enterprise Cryptography Architecture shall

- strengthen Enterprise Security
- protect sensitive information
- establish digital trust
- secure Enterprise communications
- support secure cloud adoption
- enable secure APIs
- protect digital identities
- improve regulatory compliance
- support post-quantum readiness
- improve operational resilience

Cryptography shall function as a foundational Enterprise capability.

---

# 5. Enterprise Cryptography Responsibilities

Enterprise Cryptography Architecture is responsible for

- cryptographic governance
- PKI governance
- key management
- certificate lifecycle management
- algorithm governance
- cryptographic standards
- compliance support
- cryptographic auditing
- Enterprise trust services
- continuous improvement

Business Domains shall

- classify information
- identify cryptographic requirements
- support compliance activities
- participate in key ownership reviews

Technology Domains shall

- implement approved cryptographic services
- protect cryptographic material
- maintain secure configurations
- support certificate lifecycle management
- provide audit evidence
- support Enterprise governance

Cryptographic security remains a shared Enterprise responsibility.

---

# End of Part 1

---

# 6. Enterprise Cryptography Architecture

The Enterprise Cryptography Architecture defines the standardized framework for delivering cryptographic capabilities across the MFM Enterprise Platform.

The architecture consists of

- Enterprise Cryptographic Services
- Public Key Infrastructure (PKI)
- Key Management Services (KMS)
- Hardware Security Modules (HSM)
- Certificate Management Services
- Digital Signature Services
- Encryption Services
- Cryptographic Policy Services
- Cryptographic Audit Services
- Cryptographic Monitoring Services

Cryptographic services shall be implemented as reusable Enterprise capabilities.

Business applications shall consume Enterprise cryptographic services rather than implementing proprietary cryptographic solutions.

---

# 7. Public Key Infrastructure (PKI)

The Enterprise Public Key Infrastructure (PKI) shall provide trusted digital identities throughout the Enterprise.

The PKI shall support

- certificate issuance
- certificate validation
- certificate renewal
- certificate revocation
- certificate distribution
- certificate lifecycle management
- trust chain management
- certificate transparency
- digital signatures
- mutual authentication

The Enterprise PKI shall provide a consistent trust model across

- users
- services
- APIs
- workloads
- infrastructure
- devices
- cloud platforms

Trust anchors shall remain centrally governed.

---

# 8. Certificate Authorities (CA)

Certificate Authorities shall issue and manage Enterprise certificates.

The Enterprise PKI shall support

- Root Certificate Authorities
- Intermediate Certificate Authorities
- Issuing Certificate Authorities

Certificate Authorities shall

- remain highly protected
- support strong authentication
- support secure key storage
- support audit logging
- support lifecycle management
- support disaster recovery

Root Certificate Authorities shall remain offline whenever operationally feasible.

Certificate issuance shall follow documented Enterprise policies.

---

# 9. Registration Authorities (RA)

Registration Authorities shall verify identity before certificate issuance.

Registration Authorities shall perform

- identity verification
- certificate request validation
- policy validation
- certificate approval
- certificate renewal validation
- certificate revocation validation

Registration Authorities shall never issue certificates directly.

Identity validation shall comply with Enterprise identity governance policies.

---

# 10. Hardware Security Modules (HSM)

Hardware Security Modules shall protect Enterprise cryptographic keys.

HSMs shall provide

- secure key generation
- secure key storage
- cryptographic acceleration
- secure signing
- secure encryption
- secure decryption
- tamper resistance
- hardware-backed trust

Cryptographic keys classified as highly sensitive shall never exist outside approved HSM protection unless explicitly approved.

HSM operations shall be continuously monitored and audited.

---

# 11. Enterprise Key Management

Enterprise Key Management shall govern all cryptographic keys.

Key Management shall include

- key generation
- key registration
- key distribution
- key activation
- key rotation
- key escrow where approved
- key archival
- key destruction
- key recovery procedures
- key auditing

Every cryptographic key shall define

- owner
- purpose
- classification
- algorithm
- key strength
- activation date
- expiration date
- lifecycle status

Key rotation shall follow Enterprise cryptographic policies based upon key classification and risk.

---

# 12. Certificate Lifecycle Management

Enterprise certificates shall be managed throughout their complete lifecycle.

Lifecycle phases include

- certificate request
- identity validation
- certificate issuance
- deployment
- monitoring
- renewal
- revocation
- replacement
- archival
- destruction

Certificate lifecycle management shall support automation wherever practical.

Expired or revoked certificates shall never be accepted for authentication or encrypted communications.

---

# 13. Cryptographic Dependencies

Enterprise Cryptography implementations may depend upon

- Enterprise Security Services
- Enterprise IAM Services
- Enterprise Zero Trust Services
- Enterprise Infrastructure Services
- Enterprise Monitoring Services
- Enterprise Governance Services
- Enterprise Integration Services

Enterprise Cryptography Architecture shall never depend directly upon

- application-specific key stores
- hardcoded cryptographic material
- vendor-specific encryption implementations
- proprietary certificate repositories
- presentation technologies

Cryptographic Architecture shall remain portable, interoperable and governed at the Enterprise level.

---

# End of Part 2

---

# 14. Digital Signatures

Enterprise Digital Signature Services shall provide integrity, authenticity and non-repudiation for Enterprise communications and digital assets.

Digital signatures shall support

- document signing
- API request signing
- software signing
- code signing
- container image signing
- workflow approvals
- certificate-based signing
- transaction signing
- audit evidence
- regulatory compliance

Digital signature services shall use Enterprise-approved cryptographic algorithms and trusted certificates.

---

# 15. Encryption at Rest

Sensitive Enterprise information shall be protected through encryption while stored.

Encryption at Rest shall apply to

- databases
- file systems
- object storage
- backup media
- archives
- cloud storage
- container volumes
- virtual machine disks
- portable storage
- cryptographic key repositories

Encryption keys shall be managed independently of encrypted data.

Access to encrypted data shall require authorized key usage.

---

# 16. Encryption in Transit

All sensitive Enterprise communications shall be protected during transmission.

Encryption in Transit shall apply to

- APIs
- web applications
- messaging platforms
- event streaming
- service-to-service communication
- database connections
- cloud connectivity
- administrative interfaces
- backup replication
- remote administration

Only Enterprise-approved secure communication protocols shall be permitted.

Unencrypted transmission of sensitive information shall be prohibited.

---

# 17. Mutual TLS (mTLS)

Enterprise service-to-service communication shall use Mutual TLS (mTLS) wherever practical.

mTLS shall provide

- mutual authentication
- encrypted communication
- certificate validation
- workload identity verification
- protection against impersonation
- secure service discovery
- Zero Trust alignment

Certificates used for mTLS shall be issued and managed through the Enterprise PKI.

Certificate rotation shall be automated whenever feasible.

---

# 18. Cryptographic Algorithm Governance

Enterprise Cryptographic Governance shall define approved algorithms, protocols and key strengths.

Governance shall include

- approved algorithms
- prohibited algorithms
- key length requirements
- protocol requirements
- algorithm lifecycle
- cryptographic review
- migration planning
- vulnerability response
- compliance verification
- exception management

Cryptographic standards shall be reviewed regularly to address emerging threats and industry developments.

---

# 19. Post-Quantum Cryptography Readiness

The Enterprise Cryptography Architecture shall support future migration to post-quantum cryptographic algorithms.

Preparation activities shall include

- cryptographic inventory
- algorithm dependency analysis
- algorithm agility
- migration planning
- interoperability testing
- hybrid cryptographic support
- risk assessments
- standards monitoring
- vendor capability assessments
- roadmap development

Cryptographic implementations shall minimize dependencies that prevent future algorithm replacement.

---

# 20. Enterprise Cryptography Anti-Patterns

The following architectural anti-patterns are prohibited.

## Hardcoded Keys

Cryptographic keys shall never be embedded in source code, scripts, configuration files or container images.

---

## Weak Cryptography

Deprecated, weak or unapproved algorithms shall never be used.

Enterprise-approved cryptographic standards shall always be followed.

---

## Shared Private Keys

Private keys shall never be shared between identities, applications or services unless explicitly approved by Enterprise governance.

---

## Unmanaged Certificates

Certificates shall never be deployed without lifecycle management, monitoring and automated renewal where appropriate.

---

## Unencrypted Sensitive Data

Sensitive Enterprise information shall never be stored or transmitted without appropriate cryptographic protection.

---

## Manual Key Lifecycle

Cryptographic key lifecycle management shall not rely upon undocumented manual procedures where Enterprise automation is available.

---

# 21. Cryptographic Quality Principles

Every Enterprise Cryptography implementation shall demonstrate

- confidentiality
- integrity
- authenticity
- non-repudiation
- interoperability
- auditability
- scalability
- maintainability
- resilience
- algorithm agility

Cryptographic quality shall be continuously measured through governance, monitoring and compliance activities.

---

# 22. Continuous Cryptographic Improvement

Enterprise Cryptography shall support continuous improvement through

- cryptographic reviews
- key management assessments
- certificate lifecycle reviews
- penetration testing
- vulnerability assessments
- standards reviews
- compliance audits
- cryptographic inventory validation
- technology evaluations
- post-quantum readiness assessments

Continuous improvement shall

- strengthen Enterprise trust
- reduce cryptographic risk
- improve operational resilience
- enhance regulatory compliance
- support Enterprise Security objectives

Enterprise Cryptography Architecture shall evolve continuously while preserving governance, interoperability and architectural consistency.

---

# End of Part 3

---

# 23. Implementation Guidelines

Enterprise Cryptography implementations shall follow the architectural principles defined in EA-020, EA-111, EA-112, EA-320 and EA-340 through EA-362.

Implementation shall ensure

- cryptography by design
- Enterprise-approved cryptographic algorithms
- centralized key management
- Public Key Infrastructure (PKI)
- Hardware Security Module (HSM) protection
- automated certificate lifecycle management
- algorithm agility
- comprehensive monitoring
- cryptographic auditing
- technology independence

Enterprise cryptographic services shall be implemented as reusable Enterprise capabilities.

Technology choices shall implement the Enterprise Cryptography Architecture rather than define it.

---

# 24. Architecture Compliance

Enterprise Cryptography implementations shall comply with

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
- EA-351 Master Data Management (MDM) Standard
- EA-352 Enterprise Data Quality Standard
- EA-353 Metadata & Data Catalog Standard
- EA-354 Enterprise Data Governance Standard
- EA-355 Enterprise Data Lifecycle & Retention Standard
- EA-356 Enterprise Analytics Architecture Standard
- EA-357 Enterprise Business Intelligence Architecture Standard
- EA-358 Enterprise AI & Machine Learning Architecture Standard
- EA-359 Enterprise Knowledge Graph Architecture Standard
- EA-360 Enterprise Security Architecture Standard
- EA-361 Enterprise Identity & Access Management (IAM) Architecture Standard
- EA-362 Enterprise Zero Trust Architecture Standard
- this Enterprise Cryptography & PKI Architecture Standard

Architecture reviews shall verify

- Enterprise Cryptography Architecture
- PKI implementation
- Certificate Authority implementation
- Registration Authority implementation
- HSM implementation
- key management
- certificate lifecycle management
- digital signatures
- encryption at rest
- encryption in transit
- cryptographic governance
- monitoring
- compliance

Non-compliant implementations shall require an approved architectural exception before production deployment.

---

# 25. Compliance Checklist

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
| EA-351 compliance verified | ☐ |
| EA-352 compliance verified | ☐ |
| EA-353 compliance verified | ☐ |
| EA-354 compliance verified | ☐ |
| EA-355 compliance verified | ☐ |
| EA-356 compliance verified | ☐ |
| EA-357 compliance verified | ☐ |
| EA-358 compliance verified | ☐ |
| EA-359 compliance verified | ☐ |
| EA-360 compliance verified | ☐ |
| EA-361 compliance verified | ☐ |
| EA-362 compliance verified | ☐ |
| PKI verified | ☐ |
| HSM verified | ☐ |
| Key management verified | ☐ |
| Certificate lifecycle verified | ☐ |
| Cryptographic governance verified | ☐ |
| Compliance verified | ☐ |
| Architecture review completed | ☐ |
| Documentation approved | ☐ |

Every Enterprise Cryptography implementation shall satisfy all mandatory compliance requirements before being released into production.

---

# 26. References

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
- EA-351 Master Data Management (MDM) Standard
- EA-352 Enterprise Data Quality Standard
- EA-353 Metadata & Data Catalog Standard
- EA-354 Enterprise Data Governance Standard
- EA-355 Enterprise Data Lifecycle & Retention Standard
- EA-356 Enterprise Analytics Architecture Standard
- EA-357 Enterprise Business Intelligence Architecture Standard
- EA-358 Enterprise AI & Machine Learning Architecture Standard
- EA-359 Enterprise Knowledge Graph Architecture Standard
- EA-360 Enterprise Security Architecture Standard
- EA-361 Enterprise Identity & Access Management (IAM) Architecture Standard
- EA-362 Enterprise Zero Trust Architecture Standard
- ISO/IEC 19790 Security Requirements for Cryptographic Modules
- ISO/IEC 11770 Key Management
- NIST SP 800-57 Recommendation for Key Management
- NIST SP 800-131A Transitioning the Use of Cryptographic Algorithms and Key Lengths
- NIST SP 800-52 TLS Guidelines
- RFC 5280 Internet X.509 Public Key Infrastructure Certificate Profile
- RFC 8446 Transport Layer Security (TLS) 1.3
- FIPS 140-3 Security Requirements for Cryptographic Modules
- CA/Browser Forum Baseline Requirements
- The Open Group Architecture Framework (TOGAF)

---

# 27. Summary

This standard defines the Enterprise Cryptography & PKI Architecture for the MFM Enterprise Platform.

The Enterprise Cryptography Architecture provides the authoritative framework for cryptographic services, Public Key Infrastructure, certificate management, key management and digital trust across the Enterprise.

This standard establishes

- Enterprise Cryptography Architecture
- Public Key Infrastructure
- Certificate Authorities
- Registration Authorities
- Hardware Security Modules
- Enterprise Key Management
- Certificate Lifecycle Management
- Digital Signatures
- Encryption at Rest
- Encryption in Transit
- Mutual TLS
- Cryptographic Algorithm Governance
- Post-Quantum Cryptography Readiness
- implementation guidance
- compliance requirements

General Enterprise Architecture principles are inherited from EA-020.

Enterprise Architecture positioning is inherited from EA-111.

Enterprise Event Architecture principles are inherited from EA-112.

Infrastructure Architecture principles are inherited from EA-320.

Integration Architecture principles are inherited from EA-340 through EA-345.

Enterprise Information Architecture principles are inherited from EA-350 through EA-359.

Enterprise Security Architecture principles are inherited from EA-360.

Enterprise Identity & Access Management Architecture principles are inherited from EA-361.

Enterprise Zero Trust Architecture principles are inherited from EA-362.

This standard shall be regarded as the authoritative Enterprise Cryptography & PKI Architecture Standard for the MFM Enterprise Platform.

---

# 28. Future Evolution

This standard establishes the Enterprise cryptographic foundation for the MFM Enterprise Platform.

Future architectural capabilities may include

- post-quantum cryptographic algorithms
- hybrid classical/post-quantum deployments
- confidential computing
- threshold cryptography
- distributed key management
- cloud-native HSM integration
- automated certificate discovery
- autonomous certificate renewal
- cryptographic policy-as-code
- AI-assisted cryptographic monitoring
- crypto-agility automation
- quantum-safe migration governance

These capabilities shall continue to preserve

- confidentiality
- integrity
- authenticity
- non-repudiation
- auditability
- interoperability
- resilience
- governance
- technology independence

The Enterprise Cryptography & PKI Architecture shall evolve without compromising Enterprise governance, regulatory compliance or architectural consistency.

---

# End of Document
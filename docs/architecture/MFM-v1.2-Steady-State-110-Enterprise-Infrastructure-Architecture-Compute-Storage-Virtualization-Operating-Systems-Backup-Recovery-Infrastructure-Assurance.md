# MFM v1.2-Steady-State-110
## Enterprise Infrastructure Architecture, Compute, Storage, Virtualization, Operating Systems, Backup, Recovery & Infrastructure Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-110  
**Status:** Steady-State Enterprise Infrastructure Architecture & Operations Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Infrastructure Architecture / Compute / Storage / Virtualization / Operating Systems / Backup / Recovery / Infrastructure Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-tenth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-109 – Enterprise Network Architecture, Network Security, Connectivity, Segmentation, Remote Access, DNS, IP Management & Network Assurance.

The purpose is to establish the permanent enterprise operating model for infrastructure architecture, compute platforms, physical and virtual servers, operating systems, storage, virtualization, container infrastructure, infrastructure monitoring, infrastructure performance, capacity, availability, resilience, backup, recovery, patching, hardening, configuration, infrastructure incidents, changes, lifecycle, infrastructure security integration, exceptions, remediation, assurance, metrics, dashboards, maturity and continual enterprise infrastructure capability improvement.

The central objective is:

> **MFM must operate a secure, resilient, performant and governed infrastructure foundation that provides reliable compute and storage services while maintaining controlled configuration, capacity, availability, backup, recovery, security and lifecycle management.**

---

# 2. Scope

This document covers:

- Enterprise Infrastructure Architecture
- Compute Platforms
- Physical Servers
- Virtual Servers
- Operating Systems
- Storage
- Virtualization
- Container Infrastructure
- Infrastructure Monitoring
- Infrastructure Performance
- Infrastructure Capacity
- Infrastructure Availability
- Infrastructure Resilience
- Backup
- Recovery
- Patching
- Hardening
- Configuration
- Infrastructure Incidents
- Infrastructure Changes
- Infrastructure Lifecycle
- Infrastructure Security Integration
- Infrastructure Exceptions
- Infrastructure Remediation
- Infrastructure Assurance
- Infrastructure Metrics
- Infrastructure Dashboards
- Infrastructure Maturity
- Continual Enterprise Infrastructure Capability Improvement

---

# 3. Infrastructure Governance Objective

The primary objective is:

> **Establish clear authority, ownership, standards, architecture, risk controls and assurance for enterprise infrastructure services and platforms.**

# 4. Infrastructure Architecture Objective

The primary objective is:

> **Provide a coherent infrastructure architecture supporting reliable, secure, scalable and recoverable compute, storage, virtualization and platform services.**

# 5. Compute Objective

The primary objective is:

> **Provide appropriately sized, secure, resilient and manageable compute capacity for enterprise workloads.**

# 6. Storage Objective

The primary objective is:

> **Provide reliable, performant, protected and recoverable storage appropriate to workload criticality and data requirements.**

# 7. Virtualization Objective

The primary objective is:

> **Provide controlled abstraction of compute resources while maintaining security, performance, resilience, visibility and lifecycle governance.**

# 8. Backup and Recovery Objective

The primary objective is:

> **Protect critical infrastructure workloads and configurations through reliable backup and tested recovery capabilities.**

# 9. Infrastructure Assurance Objective

The primary objective is:

> **Provide evidence that material infrastructure services and controls remain secure, available, performant, resilient, recoverable and aligned with enterprise requirements.**

# 10. Infrastructure Principles

Infrastructure should be:

```text
Secure
Resilient
Performant
Scalable
Observable
Recoverable
Governed
Lifecycle-Controlled
```

# 11. Compute Principles

Compute should be:

```text
Right-Sized
Standardized
Hardened
Monitored
Resilient
Maintainable
```

# 12. Storage Principles

Storage should be:

```text
Reliable
Protected
Performant
Capacity-Aware
Recoverable
Lifecycle-Controlled
```

# 13. Recovery Principles

Recovery should be:

```text
Planned
Documented
Tested
Prioritized
Evidence-Based
```

# 14. Infrastructure Lifecycle

Infrastructure management should integrate:

```text
Plan
 ↓
Design
 ↓
Acquire
 ↓
Build
 ↓
Configure
 ↓
Operate
 ↓
Monitor
 ↓
Protect
 ↓
Recover
 ↓
Review
 ↓
Retire
```

# 15. Infrastructure Governance

Infrastructure governance should establish:

```text
Authority
Ownership
Standards
Architecture
Security
Risk
Assurance
```

# 16. Infrastructure Authority

Infrastructure authority should define who may:

```text
Approve Infrastructure Architecture
Approve Platform Standards
Approve Capacity
Approve Recovery Requirements
Approve Exceptions
Accept Infrastructure Risk
```

# 17. Infrastructure Ownership

Material infrastructure services and platforms should have accountable owners for:

```text
Architecture
Configuration
Operation
Security
Availability
Capacity
Recovery
Lifecycle
Evidence
```

# 18. Infrastructure Inventory

Material infrastructure assets should be inventoried.

Inventory may include:

```text
Physical Servers
Virtual Machines
Hypervisors
Clusters
Storage Systems
Datastores
Operating Systems
Container Hosts
Container Platforms
Backup Systems
Infrastructure Appliances
Management Platforms
```

# 19. Infrastructure Asset Attributes

Where appropriate:

```text
Owner
Location
Function
Criticality
Environment
Dependencies
Support Status
Lifecycle
```

# 20. Infrastructure Architecture

Infrastructure architecture should align with:

```text
Enterprise Architecture
Security Architecture
Network Architecture
Identity Architecture
Data Architecture
Application Architecture
Cloud Architecture
```

# 21. Environment Classification

Infrastructure should distinguish relevant environments:

```text
Production
Test
Development
Management
Recovery
Security
```

# 22. Production Infrastructure

Production infrastructure should receive controls proportionate to:

```text
Business Criticality
Availability
Security
Recovery
```

# 23. Non-Production Infrastructure

Non-production infrastructure should remain controlled and should not introduce unacceptable risk to production or sensitive data.

# 24. Compute Architecture

Compute architecture should consider:

```text
Capacity
Performance
Availability
Resilience
Security
Lifecycle
```

# 25. Physical Compute

Physical servers should be managed for:

```text
Hardware Health
Firmware
Operating System
Security
Capacity
Support
Lifecycle
```

# 26. Server Standards

Approved server standards should define where appropriate:

```text
Hardware
Firmware
Operating System
Security Baseline
Monitoring
Backup
Support
```

# 27. Virtualization

Virtualization platforms should have:

```text
Owner
Architecture
Security
Capacity
Availability
Monitoring
Recovery
Lifecycle
```

# 28. Hypervisor Security

Hypervisors should use approved security and configuration baselines.

# 29. Virtual Machine Governance

Virtual machines should have:

```text
Owner
Purpose
Application
Environment
Criticality
Operating System
Resources
Backup
Lifecycle
```

# 30. VM Sizing

Virtual machines should be appropriately sized for:

```text
CPU
Memory
Storage
Network
Workload
```

# 31. VM Sprawl

Unused or orphaned virtual machines should be identified and removed or formally retained.

# 32. Virtual Machine Snapshots

Snapshots should be controlled and removed when no longer required.

# 33. Virtualization Resilience

Critical virtualization services should have appropriate:

```text
Cluster Resilience
Host Redundancy
Storage Resilience
Network Resilience
Recovery
```

# 34. Container Infrastructure

Where containers are used, container infrastructure should be governed for:

```text
Platform
Images
Hosts
Runtime
Security
Networking
Storage
Monitoring
Lifecycle
```

# 35. Container Image Governance

Images should use approved sources and security controls.

# 36. Container Vulnerability Management

Container images and hosts should be included in vulnerability management.

# 37. Container Runtime Security

Runtime security should address:

```text
Privileges
Isolation
Secrets
Network Access
Logging
Monitoring
```

# 38. Operating Systems

Operating systems should be:

```text
Supported
Patched
Hardened
Monitored
Backed Up where Required
```

# 39. Operating System Standards

Approved OS standards should define:

```text
Version
Configuration
Security
Monitoring
Patch
Backup
Lifecycle
```

# 40. Operating System Hardening

Hardening should address:

```text
Services
Accounts
Permissions
Network Settings
Logging
Security Controls
```

# 41. Operating System Configuration

Material OS configurations should be controlled and documented.

# 42. OS Patch Management

Patches should be prioritized according to:

```text
Security Risk
Exploitability
Criticality
Vendor Guidance
Testing
```

# 43. Emergency Patching

Critical actively exploited vulnerabilities may require accelerated or emergency change.

# 44. Firmware Management

Material infrastructure firmware should be maintained according to:

```text
Security
Compatibility
Stability
Vendor Support
```

# 45. Infrastructure Configuration Management

Infrastructure configurations should be:

```text
Standardized
Versioned
Backed Up
Controlled
Auditable
```

# 46. Infrastructure as Code

Where appropriate, infrastructure should use controlled automation and infrastructure-as-code practices.

# 47. Infrastructure Automation

Automation may support:

```text
Provisioning
Configuration
Patching
Compliance
Monitoring
Recovery
```

with appropriate controls.

# 48. Configuration Drift

Unexpected infrastructure configuration drift should be detected and remediated.

# 49. Infrastructure Monitoring

Infrastructure monitoring should cover:

```text
Availability
CPU
Memory
Storage
Network
Processes
Hardware
Virtualization
Containers
Backup
```

# 50. Infrastructure Telemetry

Telemetry should support:

```text
Operations
Security
Capacity
Troubleshooting
Assurance
```

# 51. Infrastructure Performance

Performance should be assessed against:

```text
Baseline
Threshold
SLA
Workload Requirement
```

# 52. Compute Capacity

Capacity management should consider:

```text
CPU
Memory
Storage
Network
Growth
Peak Demand
```

# 53. Storage Capacity

Storage capacity should monitor:

```text
Used
Free
Growth
Performance
Recovery Requirements
```

# 54. Capacity Headroom

Critical infrastructure should maintain appropriate capacity headroom.

# 55. Storage Architecture

Storage architecture may include:

```text
Local Storage
SAN
NAS
Object Storage
Cloud Storage
```

according to requirements.

# 56. Storage Performance

Storage performance should consider:

```text
IOPS
Latency
Throughput
Queueing
Workload
```

# 57. Storage Resilience

Critical storage should have appropriate:

```text
Redundancy
Replication
Fault Tolerance
Recovery
```

# 58. Storage Integrity

Storage systems should protect against:

```text
Corruption
Unauthorized Change
Data Loss
Hardware Failure
```

# 59. Backup

Critical infrastructure workloads and configurations should be backed up according to business and recovery requirements.

# 60. Backup Scope

Backup may include:

```text
Virtual Machines
Physical Servers
Configurations
Databases
Application Data
Infrastructure Platforms
```

# 61. Backup Classification

Backup requirements should reflect:

```text
Criticality
RPO
RTO
Data Sensitivity
Recovery Dependency
```

# 62. Backup Frequency

Backup frequency should align with business recovery requirements.

# 63. Backup Retention

Backup retention should align with:

```text
Business Need
Legal Requirements
Regulatory Requirements
Storage
Recovery
```

# 64. Backup Security

Backups should be protected against:

```text
Unauthorized Access
Modification
Deletion
Ransomware
Credential Compromise
```

# 65. Backup Isolation

Where appropriate, critical backups should use logical or physical separation from production.

# 66. Backup Monitoring

Backup jobs should be monitored for:

```text
Success
Failure
Duration
Capacity
Integrity
```

# 67. Backup Verification

Backups should be periodically verified for recoverability.

# 68. Recovery

Recovery procedures should be documented for material infrastructure services.

# 69. Recovery Prioritization

Recovery should prioritize:

```text
Critical Services
Dependencies
Business Impact
Security
```

# 70. Recovery Time Objective

RTO requirements should be defined according to business criticality.

# 71. Recovery Point Objective

RPO requirements should be defined according to data and business requirements.

# 72. Recovery Dependencies

Recovery planning should identify dependencies on:

```text
Network
Identity
DNS
Storage
Applications
Cloud
Security
Suppliers
```

# 73. Recovery Testing

Recovery should be tested periodically according to risk.

# 74. Recovery Evidence

Recovery tests should record:

```text
Scope
Date
Result
Issues
Recovery Time
Recovery Point
Actions
```

# 75. Infrastructure Resilience

Resilience may include:

```text
Redundant Hosts
Clusters
Redundant Storage
Power Resilience
Network Resilience
Geographic Diversity
Recovery Capability
```

# 76. Failure Domains

Material infrastructure failure domains should be identified.

# 77. High Availability

Critical infrastructure services should have availability arrangements appropriate to business requirements.

# 78. Infrastructure Maintenance

Maintenance should be planned to minimize business impact.

# 79. Infrastructure Change Management

Material infrastructure changes should be:

```text
Requested
Assessed
Designed
Approved
Tested
Implemented
Validated
Recorded
```

# 80. Emergency Infrastructure Change

Emergency changes should follow controlled emergency procedures and receive retrospective review.

# 81. Infrastructure Change Impact

Impact analysis should consider:

```text
Applications
Data
Network
Security
Availability
Recovery
Dependencies
```

# 82. Infrastructure Incident Management

Infrastructure incidents should integrate with enterprise service and security incident management.

# 83. Infrastructure Incident Classification

Incidents may include:

```text
Hardware Failure
OS Failure
VM Failure
Hypervisor Failure
Storage Failure
Performance Degradation
Capacity Exhaustion
Backup Failure
Recovery Failure
Configuration Failure
Security Event
```

# 84. Infrastructure Incident Response

Response should integrate:

```text
Detect
 ↓
Triage
 ↓
Diagnose
 ↓
Contain
 ↓
Restore
 ↓
Validate
 ↓
Learn
```

# 85. Infrastructure Problem Management

Recurring infrastructure incidents should undergo root-cause analysis.

# 86. Root Cause

Root-cause analysis should consider:

```text
Hardware
Software
Configuration
Capacity
Dependencies
Change
Supplier
Human Error
```

# 87. Infrastructure Dependencies

Material infrastructure dependencies should be documented.

# 88. Supplier Management

Infrastructure suppliers should be governed for:

```text
Support
Availability
Security
Performance
Lifecycle
Contracts
```

# 89. Vendor Support

Critical platforms should have appropriate support arrangements.

# 90. End-of-Support Management

Unsupported infrastructure components should be:

```text
Identified
Risk-Assessed
Remediated
Upgraded
Replaced
Retired
```

# 91. Infrastructure Security Integration

Infrastructure management should integrate with:

```text
Cybersecurity
SOC
Vulnerability Management
Identity
Network Security
Data Security
```

# 92. Infrastructure Access

Administrative access should follow:

```text
Least Privilege
Strong Authentication
Privileged Access Controls
Monitoring
```

# 93. Infrastructure Security Monitoring

Material infrastructure security events should feed appropriate monitoring and SOC capabilities.

# 94. Infrastructure Vulnerability Management

Infrastructure should be regularly assessed for relevant vulnerabilities.

# 95. Infrastructure Hardening Assurance

Hardening compliance should be assessed against approved baselines.

# 96. Infrastructure Exceptions

Exceptions should identify:

```text
Requirement
Deviation
Reason
Risk
Compensating Control
Owner
Approval
Expiry
Review
```

# 97. Infrastructure Remediation

Remediation should identify:

```text
Finding
Root Cause
Action
Owner
Due Date
Evidence
Validation
```

# 98. Infrastructure Assurance

Assurance may include:

```text
Architecture Reviews
Configuration Reviews
Hardening Reviews
Patch Reviews
Capacity Reviews
Backup Reviews
Recovery Tests
Resilience Tests
Vulnerability Reviews
Supplier Reviews
Internal Audit
Independent Assurance
```

# 99. Infrastructure Evidence

Evidence should support:

```text
Architecture
Configuration
Patch
Hardening
Capacity
Backup
Recovery
Resilience
Security
Exceptions
Remediation
```

# 100. Infrastructure Metrics

Metrics may include:

```text
Infrastructure Availability
Compute Utilization
Memory Utilization
Storage Utilization
Storage Latency
Capacity Headroom
Hardware Failure Rate
VM Availability
Hypervisor Availability
Container Platform Availability
Patch Compliance
Hardening Compliance
Configuration Compliance
Configuration Drift
Vulnerability Remediation
Backup Success Rate
Backup Failure Rate
Recovery Test Success
RTO Achievement
RPO Achievement
Infrastructure Incident Volume
Mean Time to Restore
Change Success Rate
Emergency Change Rate
End-of-Support Exposure
Infrastructure Findings
Remediation Completion
```

# 101. Infrastructure Dashboard

May include:

```text
Infrastructure Health
Compute
Storage
Virtualization
Containers
Operating Systems
Capacity
Performance
Availability
Backup
Recovery
Security
Patching
Configuration
Incidents
Changes
Lifecycle
Findings
Remediation
```

# 102. Daily Review

Where appropriate:

```text
Critical Infrastructure Alerts
Hardware Failures
Storage Alerts
Backup Failures
Capacity Alerts
Security Alerts
Critical Platform Health
```

# 103. Weekly Review

May consider:

```text
Infrastructure Incidents
Capacity
Performance
Backup
Patching
Configuration Drift
Vulnerabilities
Supplier Issues
Open Actions
```

# 104. Monthly Review

May consider:

```text
Infrastructure Service Health
Availability
Performance
Capacity
Virtualization
Storage
Operating Systems
Containers
Backup
Recovery
Security
Patch Compliance
Configuration Compliance
Lifecycle
Assurance
```

# 105. Quarterly Review

May consider:

```text
Infrastructure Strategy
Architecture
Compute
Storage
Virtualization
Operating Systems
Containers
Capacity
Resilience
Backup
Recovery
Security
End-of-Support
Supplier Risk
Technical Debt
Assurance
Maturity
```

# 106. Annual Review

May consider:

```text
Infrastructure Strategy
Operating Model
Governance
Architecture
Compute
Storage
Virtualization
Operating Systems
Containers
Monitoring
Performance
Capacity
Availability
Resilience
Backup
Recovery
Patching
Hardening
Configuration
Security
Cloud Infrastructure
Suppliers
Lifecycle
Assurance
Maturity
Improvement
```

# 107. Infrastructure Maturity

Infrastructure capability maturity should be periodically assessed.

# 108. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Inventory
Architecture
Environment Classification
Compute
Physical Servers
Server Standards
Virtualization
Hypervisor Security
VM Governance
VM Sizing
VM Sprawl
Snapshots
Virtualization Resilience
Containers
Container Images
Container Vulnerabilities
Runtime Security
Operating Systems
OS Standards
Hardening
Configuration
Patch Management
Emergency Patching
Firmware
Configuration Management
Infrastructure as Code
Automation
Configuration Drift
Monitoring
Telemetry
Performance
Capacity
Storage
Storage Performance
Storage Resilience
Storage Integrity
Backup
Backup Scope
Backup Classification
Frequency
Retention
Security
Isolation
Monitoring
Verification
Recovery
RTO
RPO
Dependencies
Testing
Evidence
Resilience
Failure Domains
High Availability
Maintenance
Change Management
Emergency Change
Incident Management
Problem Management
Root Cause
Supplier Management
Vendor Support
End-of-Support
Security Integration
Administrative Access
Security Monitoring
Vulnerability Management
Hardening Assurance
Exceptions
Remediation
Assurance
Metrics
Improvement
```

# 109. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 110. Infrastructure Architecture Quality Gate

```text
Business Need
 ↓
Infrastructure Requirement
 ↓
Risk
 ↓
Architecture
 ↓
Compute / Storage
 ↓
Security
 ↓
Availability
 ↓
Recovery
 ↓
Monitoring
 ↓
Assurance
```

must be controlled.

# 111. Infrastructure Change Quality Gate

```text
Request
 ↓
Impact
 ↓
Design
 ↓
Risk
 ↓
Approval
 ↓
Test
 ↓
Implement
 ↓
Validate
 ↓
Evidence
```

must be controlled.

# 112. Backup Quality Gate

```text
Requirement
 ↓
Scope
 ↓
RPO / RTO
 ↓
Backup
 ↓
Monitoring
 ↓
Verification
 ↓
Recovery Test
 ↓
Evidence
```

must be controlled.

# 113. Recovery Quality Gate

```text
Failure
 ↓
Diagnosis
 ↓
Recovery Plan
 ↓
Restore
 ↓
Security Validation
 ↓
Service Validation
 ↓
Monitoring
 ↓
Lessons Learned
```

must be controlled.

# 114. Infrastructure Assurance Quality Gate

```text
Requirement
 ↓
Control
 ↓
Test
 ↓
Evidence
 ↓
Finding
 ↓
Remediation
 ↓
Validation
```

must be traceable.

# 115. Definition of Ready

An infrastructure architecture, compute platform, storage service, virtual machine, operating system, container platform, backup arrangement, recovery procedure, infrastructure change, exception, remediation or assurance review is Ready when purpose, owner, affected assets, business need, dependencies, capacity requirements, security requirements, availability requirements, recovery requirements, approval authority and acceptance criteria are defined.

# 116. Definition of Done

An infrastructure work item is Done when:

```text
Requirement / Infrastructure Event Identified
        ↓
Owner Assigned
        ↓
Infrastructure Action Completed
        ↓
Security / Performance / Capacity / Availability / Recovery Validation Completed where Required
        ↓
Infrastructure / Configuration / Asset / Backup / Recovery Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 117. Final Infrastructure Governance Principle

> **MFM must operate a secure, resilient, performant and governed infrastructure foundation that provides reliable compute and storage services while maintaining controlled configuration, capacity, availability, backup, recovery, security and lifecycle management.**

# 118. Final Compute Principle

> **Compute resources must be appropriately sized, standardized, hardened, monitored, resilient and lifecycle-controlled according to workload requirements and business criticality.**

# 119. Final Storage Principle

> **Storage must provide appropriate performance, integrity, resilience, protection, capacity and recovery capability according to data and workload requirements.**

# 120. Final Virtualization Principle

> **Virtualization must provide controlled resource abstraction while preserving security, performance, resilience, observability and lifecycle governance.**

# 121. Final Backup Principle

> **Critical infrastructure workloads and configurations must have reliable, protected and appropriately retained backups aligned with recovery requirements.**

# 122. Final Recovery Principle

> **Recovery capability must be documented, prioritized, tested and supported by evidence demonstrating that critical infrastructure can be restored within required objectives.**

# 123. Final Security Principle

> **Infrastructure security must integrate identity, network, vulnerability, hardening, monitoring and privileged access controls throughout the infrastructure lifecycle.**

# 124. Final Lifecycle Principle

> **Infrastructure platforms, operating systems, configurations, firmware, virtual machines, storage, containers and dependencies must be governed from acquisition through retirement.**

# 125. Final Assurance Principle

> **Material infrastructure controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 126. Final Improvement Principle

> **Infrastructure incidents, capacity constraints, vulnerabilities, backup failures, recovery findings, configuration weaknesses and assurance results must continuously improve MFM's infrastructure capability.**

# 127. Final Integration Principle

> **Infrastructure Architecture and Operations must integrate with Enterprise Architecture, Network, Cybersecurity, Identity, Data, Applications, Cloud, Service Management, Configuration Management, Asset Management, Change Management, Suppliers, Risk, Compliance, Legal and Business Continuity.**

# 128. Final Steady-State Infrastructure Principle

> **MFM must operate a secure, resilient, performant and governed infrastructure foundation that provides reliable compute and storage services while maintaining controlled configuration, capacity, availability, backup, recovery, security and lifecycle management.**

# 129. Summary

MFM v1.2-Steady-State-110 establishes the permanent Enterprise Infrastructure Architecture and Infrastructure Operations baseline.

It defines:

- Infrastructure Governance / Authority / Ownership / Inventory
- Infrastructure Architecture / Environment Classification
- Compute Architecture / Physical Servers / Server Standards
- Virtualization / Hypervisor Security / VM Governance / VM Sizing / VM Sprawl
- VM Snapshots / Virtualization Resilience
- Container Infrastructure / Image Governance / Vulnerability / Runtime Security
- Operating Systems / OS Standards / Hardening / Configuration
- Patch Management / Emergency Patching / Firmware
- Infrastructure Configuration Management / Infrastructure as Code / Automation / Drift
- Infrastructure Monitoring / Telemetry / Performance / Capacity
- Storage Architecture / Performance / Resilience / Integrity
- Backup / Scope / Classification / Frequency / Retention / Security / Isolation
- Backup Monitoring / Verification
- Recovery / RTO / RPO / Dependencies / Testing / Evidence
- Infrastructure Resilience / Failure Domains / High Availability
- Maintenance / Change Management / Emergency Change / Impact
- Infrastructure Incident / Problem / Root Cause Management
- Infrastructure Dependencies / Supplier Management / Vendor Support
- End-of-Support Management
- Infrastructure Security Integration / Administrative Access / Security Monitoring
- Infrastructure Vulnerability / Hardening Assurance
- Infrastructure Exceptions / Remediation / Assurance / Evidence
- Infrastructure Metrics / Infrastructure Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Infrastructure Maturity
- Infrastructure Architecture / Change / Backup / Recovery / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 130. Next Document

**MFM v1.2-Steady-State-111 – Enterprise Cloud Architecture, Cloud Governance, Cloud Security, Cloud Operations, Cloud Cost Management & Cloud Assurance**

It shall establish the permanent enterprise operating model for cloud strategy, cloud architecture, cloud governance, cloud service models, cloud landing zones, cloud accounts/subscriptions, cloud networking, cloud identity, cloud security, cloud workloads, cloud data, cloud monitoring, cloud resilience, cloud backup, disaster recovery, cloud operations, cloud cost management, FinOps, cloud supplier management, cloud configuration, cloud compliance, cloud exceptions, cloud remediation, cloud assurance, cloud metrics, dashboards, maturity and continual enterprise cloud capability improvement supporting MFM.

# 131. Document Control

**Document:** MFM v1.2-Steady-State-110  
**Version:** 1.2  
**Status:** Steady-State Enterprise Infrastructure Architecture & Operations Baseline  
**Previous Document:** MFM v1.2-Steady-State-109  
**Next Document:** MFM v1.2-Steady-State-111  
**Lifecycle:** Steady-State Operation  
**Infrastructure Governance Authority:** Enterprise Infrastructure Architecture  
**Compute Authority:** Compute / Server Infrastructure  
**Storage Authority:** Enterprise Storage Management  
**Virtualization Authority:** Virtualization Platform Management  
**Operating System Authority:** Platform / Operating System Management  
**Container Authority:** Container Platform Management  
**Backup Authority:** Backup and Data Protection Infrastructure  
**Recovery Authority:** Infrastructure Recovery / Operational Resilience  
**Infrastructure Security Authority:** Infrastructure Security / Cybersecurity  
**Network Authority:** Enterprise Network Architecture  
**Cloud Authority:** Enterprise Cloud Architecture  
**Identity Authority:** Identity and Access Management  
**Data Authority:** Enterprise Data Management  
**Application Authority:** Enterprise Application Management  
**Security Operations Authority:** Security Operations Center  
**Service Authority:** Enterprise Service Management  
**Configuration Authority:** Configuration Management  
**Asset Authority:** Enterprise Asset Management  
**Change Authority:** Enterprise Change Management  
**Supplier Authority:** Supplier / Third-Party Management  
**Risk Authority:** Enterprise Risk Management  
**Compliance Authority:** Enterprise Compliance  
**Legal Authority:** Legal / Regulatory Affairs  
**Continuity Authority:** Business Continuity / Operational Resilience  
**Assurance Authority:** Infrastructure Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Infrastructure Capability Improvement  

**Principle:** MFM must operate a secure, resilient, performant and governed infrastructure foundation that provides reliable compute and storage services while maintaining controlled configuration, capacity, availability, backup, recovery, security and lifecycle management.

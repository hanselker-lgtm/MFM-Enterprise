# MFM v1.2-Steady-State-109
## Enterprise Network Architecture, Network Security, Connectivity, Segmentation, Remote Access, DNS, IP Management & Network Assurance

**Version:** 1.2  
**Document ID:** MFM v1.2-Steady-State-109  
**Status:** Steady-State Enterprise Network Architecture & Operations Baseline  
**Lifecycle:** Post-Implementation / Steady-State Operation  
**Document Type:** Network Architecture / Network Security / Connectivity / Segmentation / Remote Access / DNS / IP Management / Network Assurance Document  

---

# 1. Purpose

This document establishes the one-hundred-and-ninth document in the MFM v1.2 Steady-State series.

It follows MFM v1.2-Steady-State-108 – Enterprise Identity & Access Management, IAM Governance, Privileged Access, Authentication, Authorization & Identity Assurance.

The purpose is to establish the permanent enterprise operating model for network architecture, network governance, connectivity, routing, switching, segmentation, firewalling, remote access, VPN, wireless, DNS, DHCP, IP address management, network monitoring, network performance, network resilience, network configuration, network incidents, network changes, network lifecycle, network security integration, network exceptions, network remediation, network assurance, network metrics, dashboards, maturity and continual enterprise network capability improvement.

The central objective is:

> **MFM must operate a secure, resilient, observable and governed enterprise network that provides reliable connectivity while enforcing appropriate segmentation, access control, performance, availability, security and lifecycle management.**

---

# 2. Scope

This document covers:

- Enterprise Network Architecture
- Network Governance
- Network Connectivity
- Routing
- Switching
- Network Segmentation
- Firewalling
- Remote Access
- VPN
- Wireless Networking
- DNS
- DHCP
- IP Address Management
- Network Monitoring
- Network Performance
- Network Resilience
- Network Configuration
- Network Incidents
- Network Changes
- Network Lifecycle
- Network Security Integration
- Network Exceptions
- Network Remediation
- Network Assurance
- Network Metrics
- Network Dashboards
- Network Maturity
- Continual Enterprise Network Capability Improvement

---

# 3. Network Governance Objective

The primary objective is:

> **Establish clear authority, ownership, standards, risk controls and assurance for enterprise network services and infrastructure.**

# 4. Network Architecture Objective

The primary objective is:

> **Provide a coherent network architecture supporting secure, resilient and performant connectivity between users, systems, applications, cloud services, sites and approved external parties.**

# 5. Connectivity Objective

The primary objective is:

> **Provide reliable connectivity appropriate to business requirements, criticality and risk.**

# 6. Network Security Objective

The primary objective is:

> **Control network access and communication through segmentation, authentication, authorization, filtering, monitoring and secure configuration.**

# 7. Network Assurance Objective

The primary objective is:

> **Provide evidence that material network services and controls remain secure, available, resilient, performant and aligned with enterprise requirements.**

# 8. Network Principles

The network should be:

```text
Secure
Resilient
Observable
Performant
Standardized
Governed
Lifecycle-Controlled
```

# 9. Network Security Principles

Network security should be:

```text
Segmented
Least-Privilege
Identity-Aware where Appropriate
Defense-in-Depth
Continuously Monitored
Risk-Based
```

# 10. Connectivity Principles

Connectivity should be:

```text
Purposeful
Reliable
Redundant where Required
Capacity-Aware
Observable
Recoverable
```

# 11. Network Lifecycle

Network management should integrate:

```text
Plan
 ↓
Design
 ↓
Build
 ↓
Configure
 ↓
Operate
 ↓
Monitor
 ↓
Change
 ↓
Recover
 ↓
Review
 ↓
Retire
```

# 12. Network Governance

Network governance should establish:

```text
Authority
Ownership
Standards
Architecture
Security
Risk
Assurance
```

# 13. Network Authority

Network authority should define who may:

```text
Approve Network Architecture
Approve Network Standards
Approve Segmentation
Approve Firewall Rules
Approve Remote Access
Approve Exceptions
Accept Network Risk
```

# 14. Network Ownership

Material network services and components should have accountable owners for:

```text
Architecture
Configuration
Operation
Security
Availability
Capacity
Evidence
Lifecycle
```

# 15. Network Inventory

Material network assets should be inventoried.

Inventory may include:

```text
Routers
Switches
Firewalls
Wireless Controllers
Access Points
VPN Gateways
Load Balancers
DNS Services
DHCP Services
Network Links
Cloud Network Components
```

# 16. Network Asset Attributes

Where appropriate:

```text
Owner
Location
Function
Criticality
IP Information
Dependencies
Support Status
Lifecycle
```

# 17. Network Architecture

Network architecture should align with:

```text
Enterprise Architecture
Security Architecture
Identity Architecture
Data Architecture
Application Architecture
Infrastructure Architecture
Cloud Architecture
```

# 18. Network Zones

Network architecture should define appropriate zones such as:

```text
User
Server
Management
Guest
Production
Development
Security
DMZ
Cloud
External
```

# 19. Network Segmentation

Segmentation should be based on:

```text
Risk
Trust
Data Sensitivity
Application Dependency
Business Criticality
```

# 20. Segmentation Objectives

Segmentation should limit:

```text
Unauthorized Access
Lateral Movement
Uncontrolled Communication
Blast Radius
```

# 21. Micro-Segmentation

Where appropriate, micro-segmentation may provide additional control between workloads and services.

# 22. Network Trust Boundaries

Material trust boundaries should be identified and protected.

# 23. Routing

Routing architecture should provide:

```text
Correct Path Selection
Resilience
Controlled Advertisement
Monitoring
```

# 24. Dynamic Routing

Dynamic routing protocols should be governed for:

```text
Authentication
Peerings
Advertisements
Filtering
Monitoring
```

# 25. Static Routing

Static routes should be documented and reviewed where operationally material.

# 26. Routing Security

Routing controls should protect against unauthorized:

```text
Route Injection
Route Advertisement
Peer Modification
```

# 27. Switching

Switching architecture should provide:

```text
Segmentation
Redundancy
Performance
Manageability
Security
```

# 28. VLAN Governance

VLANs should have:

```text
Purpose
Owner
Scope
Security Classification
Lifecycle
```

# 29. Network Access Control

Where appropriate, network access control should validate:

```text
Identity
Device
Location
Security State
Authorization
```

# 30. Firewall Governance

Firewall rules should have:

```text
Source
Destination
Service
Purpose
Owner
Approval
Expiry / Review
```

# 31. Firewall Rule Lifecycle

Rules should be:

```text
Requested
Risk-Assessed
Approved
Implemented
Monitored
Reviewed
Removed
```

# 32. Firewall Rule Review

Material firewall rules should be periodically reviewed for:

```text
Business Need
Scope
Risk
Usage
Obsolescence
```

# 33. Default Deny

Where appropriate, network security should use deny-by-default principles with explicitly authorized exceptions.

# 34. Network Address Translation

NAT configurations should be documented and governed where they affect security or traceability.

# 35. Network Security Monitoring

Network security monitoring should provide visibility into relevant:

```text
Connections
Flows
Threats
Firewall Events
DNS
Remote Access
```

# 36. Network Flow Monitoring

Material network flows should be observable where required for security and operations.

# 37. Intrusion Detection / Prevention

Where implemented, IDS/IPS should support:

```text
Detection
Prevention
Investigation
Response
```

# 38. Network Threat Detection

Network threat detection should integrate with:

```text
SIEM
SOC
Threat Intelligence
Incident Response
```

# 39. Remote Access

Remote access should be:

```text
Authorized
Authenticated
Encrypted
Monitored
Risk-Based
```

# 40. VPN

VPN services should have:

```text
Authentication
Authorization
Encryption
Configuration Standards
Monitoring
Lifecycle
```

# 41. Remote Access Authentication

Remote access should use authentication appropriate to risk, including stronger controls for privileged or sensitive access.

# 42. Remote Access Authorization

Access should be limited according to:

```text
User
Role
Device
Purpose
Resource
Duration
```

# 43. Remote Access Device Security

Where appropriate, remote devices should meet defined security requirements before access is permitted.

# 44. Remote Access Monitoring

Remote access should be monitored for:

```text
Authentication
Sessions
Anomalies
Abuse
```

# 45. Wireless Network

Wireless services should be governed for:

```text
Security
Authentication
Segmentation
Coverage
Performance
Availability
```

# 46. Wireless Network Types

Where appropriate:

```text
Corporate
Guest
Operational
IoT
Management
```

should be logically separated.

# 47. Wireless Authentication

Wireless authentication should align with identity and security architecture.

# 48. Wireless Security

Wireless security should protect against:

```text
Unauthorized Access
Rogue Access Points
Weak Encryption
Misconfiguration
```

# 49. DNS

DNS services should be governed for:

```text
Architecture
Availability
Security
Resolution
Change
Monitoring
```

# 50. DNS Security

DNS security should address:

```text
Unauthorized Changes
Spoofing
Poisoning
Malicious Domains
Data Exfiltration Indicators
```

# 51. DNS Monitoring

Relevant DNS activity should be monitored where appropriate.

# 52. DNS Records

Material DNS records should have:

```text
Owner
Purpose
Lifecycle
Change Control
```

# 53. DHCP

DHCP services should be governed for:

```text
Scope
Reservations
Security
Availability
Monitoring
```

# 54. IP Address Management

IP address management should maintain authoritative information for:

```text
Networks
Subnets
Addresses
Assignments
Reservations
VLANs
```

# 55. IPAM Ownership

IP address records should have appropriate ownership and lifecycle control.

# 56. Network Naming

Network naming conventions should support:

```text
Consistency
Identification
Automation
Troubleshooting
```

# 57. Network Configuration Management

Network configurations should be:

```text
Standardized
Versioned
Backed Up
Controlled
Auditable
```

# 58. Configuration Backup

Material network configurations should be backed up and recoverable.

# 59. Configuration Drift

Unexpected configuration drift should be detected and investigated.

# 60. Network Hardening

Network devices and services should use approved security hardening baselines.

# 61. Network Vulnerability Management

Network infrastructure should be included in vulnerability management.

# 62. Network Patch Management

Network devices should receive appropriate security and lifecycle updates.

# 63. Network Monitoring

Network monitoring should cover:

```text
Availability
Latency
Packet Loss
Bandwidth
Errors
Capacity
Security
```

# 64. Network Performance

Performance should be measured against relevant:

```text
Baseline
Threshold
SLA
Business Requirement
```

# 65. Network Capacity

Capacity management should consider:

```text
Current Utilization
Growth
Peak Demand
Criticality
Redundancy
```

# 66. Network Availability

Critical network services should have availability targets appropriate to business requirements.

# 67. Network Resilience

Resilience may include:

```text
Redundant Links
Redundant Devices
Diverse Paths
Failover
High Availability
```

# 68. Network Failure Domains

Material failure domains should be identified and minimized where practical.

# 69. Network Recovery

Recovery should address:

```text
Configuration
Connectivity
Routing
Security
DNS
DHCP
Monitoring
```

# 70. Network Disaster Recovery

Critical network services should have documented recovery procedures.

# 71. Network Testing

Recovery and resilience should be tested periodically according to risk.

# 72. Network Change Management

Material network changes should be:

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

# 73. Emergency Network Change

Emergency changes should follow controlled emergency procedures and receive retrospective review.

# 74. Network Change Impact

Impact analysis should consider:

```text
Connectivity
Security
Applications
Cloud
Users
Operations
Recovery
```

# 75. Network Incident Management

Network incidents should integrate with enterprise service and security incident management.

# 76. Network Incident Classification

Incidents may include:

```text
Outage
Performance Degradation
Connectivity Failure
Routing Failure
Security Event
Configuration Failure
DNS Failure
DHCP Failure
VPN Failure
Wireless Failure
```

# 77. Network Incident Response

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

# 78. Network Problem Management

Recurring network incidents should undergo root-cause analysis and problem management.

# 79. Network Root Cause

Root-cause analysis should consider:

```text
Configuration
Capacity
Hardware
Software
Routing
Security
Dependencies
Human Error
Supplier
```

# 80. Network Service Dependencies

Material network services should document dependencies on:

```text
Power
Connectivity Providers
Cloud
Identity
DNS
DHCP
Applications
Security Services
```

# 81. Network Supplier Management

Network suppliers should be governed for:

```text
Availability
Support
Security
Performance
Contracts
Lifecycle
```

# 82. Network Provider Diversity

Critical connectivity should consider provider diversity where business risk warrants it.

# 83. Network Service Levels

Network service levels should define:

```text
Availability
Performance
Response
Recovery
Support
```

# 84. Network Security Integration

Network management should integrate with:

```text
Cybersecurity
SOC
SIEM
Threat Intelligence
Vulnerability Management
Identity
```

# 85. Identity-Aware Networking

Where appropriate, network access should integrate with identity and device context.

# 86. Cloud Networking

Cloud networks should align with enterprise network and security standards.

# 87. Cloud Connectivity

Cloud connectivity may include:

```text
VPN
Dedicated Connectivity
Private Peering
Approved Internet Connectivity
```

# 88. Cloud Network Segmentation

Cloud environments should use appropriate segmentation for:

```text
Production
Development
Management
Security
Data
```

# 89. Network Telemetry

Network telemetry should support:

```text
Operations
Security
Capacity
Troubleshooting
Assurance
```

# 90. Network Documentation

Network documentation should include appropriate:

```text
Architecture
Topology
Addressing
Routing
Firewalling
Dependencies
Recovery
```

# 91. Network Topology

Material network topology should be documented and maintained.

# 92. Network Architecture Diagrams

Architecture diagrams should reflect material changes.

# 93. Network Knowledge Management

Operational knowledge should include:

```text
Runbooks
Troubleshooting
Recovery
Known Errors
Configurations
Supplier Contacts
```

# 94. Network Exceptions

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

# 95. Network Remediation

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

# 96. Network Assurance

Assurance may include:

```text
Architecture Reviews
Configuration Reviews
Firewall Reviews
Segmentation Reviews
Access Reviews
Vulnerability Reviews
Resilience Tests
Recovery Tests
Supplier Reviews
Internal Audit
Independent Assurance
```

# 97. Network Evidence

Evidence should support:

```text
Architecture
Configuration
Firewall Rules
Segmentation
Access
Monitoring
Availability
Recovery
Exceptions
Remediation
```

# 98. Network Metrics

Metrics may include:

```text
Network Availability
Connectivity Availability
Latency
Packet Loss
Bandwidth Utilization
Capacity Headroom
Network Incident Volume
Mean Time to Restore
Firewall Rule Review Completion
Configuration Compliance
Configuration Drift
Vulnerability Remediation
VPN Availability
VPN Usage
Wireless Availability
DNS Availability
DHCP Availability
IPAM Accuracy
Network Change Success Rate
Emergency Change Rate
Network Findings
Remediation Completion
```

# 99. Network Dashboard

May include:

```text
Network Health
Connectivity
Security
Performance
Capacity
Firewall
Remote Access
Wireless
DNS
DHCP
IPAM
Incidents
Changes
Resilience
Findings
Remediation
```

# 100. Daily Review

Where appropriate:

```text
Critical Outages
Security Events
Connectivity Failures
Performance Alerts
VPN Health
DNS / DHCP Health
Network Provider Issues
```

# 101. Weekly Review

May consider:

```text
Network Incidents
Performance Trends
Capacity
Firewall Changes
Configuration Drift
Vulnerabilities
Remote Access
Supplier Issues
Open Actions
```

# 102. Monthly Review

May consider:

```text
Network Service Health
Availability
Performance
Capacity
Security
Segmentation
Firewall Governance
Remote Access
Wireless
DNS
DHCP
IPAM
Changes
Assurance
```

# 103. Quarterly Review

May consider:

```text
Network Strategy
Architecture
Connectivity
Segmentation
Security
Cloud Networking
Remote Access
Capacity
Resilience
Supplier Risk
Technical Debt
Assurance
Maturity
```

# 104. Annual Review

May consider:

```text
Network Strategy
Operating Model
Governance
Architecture
Connectivity
Routing
Switching
Segmentation
Firewalling
Remote Access
VPN
Wireless
DNS
DHCP
IPAM
Monitoring
Performance
Capacity
Resilience
Recovery
Security
Cloud Networking
Suppliers
Assurance
Maturity
Improvement
```

# 105. Network Maturity

Network capability maturity should be periodically assessed.

# 106. Maturity Dimensions

Assess:

```text
Governance
Strategy
Authority
Ownership
Inventory
Architecture
Zones
Segmentation
Trust Boundaries
Routing
Dynamic Routing
Static Routing
Routing Security
Switching
VLAN Governance
Network Access Control
Firewall Governance
Firewall Lifecycle
Firewall Reviews
Default Deny
NAT
Security Monitoring
Flow Monitoring
IDS / IPS
Threat Detection
Remote Access
VPN
Authentication
Authorization
Device Security
Wireless
Wireless Segmentation
Wireless Authentication
Wireless Security
DNS
DNS Security
DNS Monitoring
DNS Records
DHCP
IPAM
Naming
Configuration Management
Configuration Backup
Configuration Drift
Hardening
Vulnerability Management
Patch Management
Network Monitoring
Performance
Capacity
Availability
Resilience
Failure Domains
Recovery
Disaster Recovery
Testing
Change Management
Emergency Change
Change Impact
Incident Management
Problem Management
Root Cause
Dependencies
Supplier Management
Provider Diversity
Service Levels
Security Integration
Identity-Aware Networking
Cloud Networking
Cloud Connectivity
Cloud Segmentation
Telemetry
Documentation
Topology
Architecture Diagrams
Knowledge Management
Exceptions
Remediation
Assurance
Metrics
Improvement
```

# 107. Maturity Levels

```text
1 – Initial
2 – Repeatable
3 – Defined
4 – Managed
5 – Optimized
```

# 108. Network Architecture Quality Gate

```text
Business Need
 ↓
Network Requirement
 ↓
Risk
 ↓
Architecture
 ↓
Segmentation
 ↓
Security
 ↓
Connectivity
 ↓
Resilience
 ↓
Monitoring
 ↓
Assurance
```

must be controlled.

# 109. Firewall Quality Gate

```text
Need
 ↓
Source
 ↓
Destination
 ↓
Service
 ↓
Risk
 ↓
Approval
 ↓
Implementation
 ↓
Monitoring
 ↓
Review
 ↓
Removal
```

must be controlled.

# 110. Network Change Quality Gate

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

# 111. Network Recovery Quality Gate

```text
Failure
 ↓
Diagnosis
 ↓
Recovery Plan
 ↓
Configuration / Connectivity Restore
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

# 112. Network Assurance Quality Gate

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

# 113. Definition of Ready

A network architecture, connectivity change, firewall rule, segmentation design, remote access service, DNS/DHCP change, IP allocation, network recovery procedure, exception, remediation or assurance review is Ready when purpose, owner, affected network assets, business need, dependencies, risk, security requirements, availability requirements, approval authority and acceptance criteria are defined.

# 114. Definition of Done

A network work item is Done when:

```text
Requirement / Network Event Identified
        ↓
Owner Assigned
        ↓
Network Action Completed
        ↓
Security / Connectivity / Performance / Resilience Validation Completed where Required
        ↓
Network / Configuration / Topology / IPAM / Firewall Records Updated
        ↓
Evidence Captured
        ↓
Findings / Exceptions Addressed
        ↓
Outcome Accepted
```

# 115. Final Network Governance Principle

> **MFM must operate a secure, resilient, observable and governed enterprise network that provides reliable connectivity while enforcing appropriate segmentation, access control, performance, availability, security and lifecycle management.**

# 116. Final Architecture Principle

> **Network architecture must provide controlled and resilient connectivity while maintaining clear trust boundaries and alignment with enterprise security, identity, data, application, infrastructure and cloud architecture.**

# 117. Final Segmentation Principle

> **Network segmentation must reduce unauthorized communication, lateral movement and operational blast radius according to risk and business requirements.**

# 118. Final Firewall Principle

> **Firewall rules must be explicitly justified, risk-assessed, approved, monitored, periodically reviewed and removed when no longer required.**

# 119. Final Connectivity Principle

> **Critical connectivity must provide appropriate availability, capacity, resilience and recovery according to business criticality.**

# 120. Final Monitoring Principle

> **Material network services must be sufficiently observable to detect availability, performance, security and capacity conditions in time to support effective action.**

# 121. Final Lifecycle Principle

> **Network assets, configurations, services, rules, addresses and dependencies must be governed throughout their complete lifecycle.**

# 122. Final Assurance Principle

> **Material network controls must be supported by reliable evidence and periodically assessed through risk-based assurance.**

# 123. Final Improvement Principle

> **Network incidents, outages, security findings, capacity constraints, configuration weaknesses and assurance results must continuously improve MFM's network capability.**

# 124. Final Integration Principle

> **Network Architecture and Operations must integrate with Enterprise Architecture, Cybersecurity, Identity, Data, Applications, Infrastructure, Cloud, Service Management, Configuration Management, Asset Management, Change Management, Suppliers, Risk, Compliance, Legal and Business Continuity.**

# 125. Final Steady-State Network Principle

> **MFM must operate a secure, resilient, observable and governed enterprise network that provides reliable connectivity while enforcing appropriate segmentation, access control, performance, availability, security and lifecycle management.**

# 126. Summary

MFM v1.2-Steady-State-109 establishes the permanent Enterprise Network Architecture and Network Operations baseline.

It defines:

- Network Governance / Authority / Ownership / Inventory
- Network Architecture / Zones / Segmentation / Trust Boundaries
- Routing / Dynamic Routing / Static Routing / Routing Security
- Switching / VLAN Governance / Network Access Control
- Firewall Governance / Firewall Rule Lifecycle / Reviews
- Default Deny / NAT
- Network Security Monitoring / Flow Monitoring / IDS / IPS
- Network Threat Detection
- Remote Access / VPN / Authentication / Authorization / Device Security
- Wireless Networking / Segmentation / Authentication / Security
- DNS / DNS Security / DNS Monitoring / DNS Records
- DHCP
- IP Address Management / Naming
- Network Configuration / Backup / Drift / Hardening
- Vulnerability / Patch Management
- Network Monitoring / Performance / Capacity / Availability
- Network Resilience / Failure Domains / Recovery / Disaster Recovery / Testing
- Network Change / Emergency Change / Impact
- Network Incident / Problem / Root Cause Management
- Network Dependencies / Supplier Management / Provider Diversity
- Network Service Levels
- Network Security Integration / Identity-Aware Networking
- Cloud Networking / Connectivity / Segmentation
- Network Telemetry / Documentation / Topology / Architecture Diagrams
- Network Knowledge Management
- Network Exceptions / Remediation / Assurance / Evidence
- Network Metrics / Network Dashboard
- Daily / Weekly / Monthly / Quarterly / Annual Reviews
- Network Maturity
- Network Architecture / Firewall / Change / Recovery / Assurance Quality Gates
- Definition of Ready
- Definition of Done

# 127. Next Document

**MFM v1.2-Steady-State-110 – Enterprise Infrastructure Architecture, Compute, Storage, Virtualization, Operating Systems, Backup, Recovery & Infrastructure Assurance**

It shall establish the permanent enterprise operating model for infrastructure architecture, compute platforms, physical and virtual servers, operating systems, storage, virtualization, container infrastructure, infrastructure monitoring, infrastructure performance, capacity, availability, resilience, backup, recovery, patching, hardening, configuration, infrastructure incidents, changes, lifecycle, infrastructure security integration, exceptions, remediation, assurance, metrics, dashboards, maturity and continual enterprise infrastructure capability improvement supporting MFM.

# 128. Document Control

**Document:** MFM v1.2-Steady-State-109  
**Version:** 1.2  
**Status:** Steady-State Enterprise Network Architecture & Operations Baseline  
**Previous Document:** MFM v1.2-Steady-State-108  
**Next Document:** MFM v1.2-Steady-State-110  
**Lifecycle:** Steady-State Operation  
**Network Governance Authority:** Enterprise Network Architecture  
**Network Operations Authority:** Network Operations  
**Network Security Authority:** Network Security / Cybersecurity  
**Connectivity Authority:** Enterprise Connectivity  
**Routing Authority:** Network Engineering  
**Firewall Authority:** Network Security / Firewall Management  
**Remote Access Authority:** Remote Access / VPN Management  
**Wireless Authority:** Wireless Network Management  
**DNS Authority:** DNS Management  
**DHCP Authority:** DHCP Management  
**IPAM Authority:** IP Address Management  
**Infrastructure Authority:** Enterprise Infrastructure Architecture  
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
**Assurance Authority:** Network Assurance / Internal Audit / Independent Assurance  
**Improvement Authority:** Continual Enterprise Network Capability Improvement  

**Principle:** MFM must operate a secure, resilient, observable and governed enterprise network that provides reliable connectivity while enforcing appropriate segmentation, access control, performance, availability, security and lifecycle management.

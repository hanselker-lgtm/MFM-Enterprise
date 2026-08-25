# EA-IMETA-PC-RG-413

## AUTHORITY, ROLES & SEPARATION-OF-DUTIES MODEL

### 1. Document Registry

| Field | Definition |
|---|---|
| Physical File ID | EA-IMETA-PC-RG-413 |
| Domain | Post-Closure / Regression Governance |
| Document Type | Authority, Roles & Separation-of-Duties Architecture |
| Status | Active Working Baseline |
| Version | 1.0 |
| Parent | EA-IMETA-PC-RG-412 |
| Governing Architecture | EA-IMETA-MASTER-01 |
| Primary Purpose | Define who may perform, review, verify, approve, suspend, revoke and reopen controlled PC-RG activities |
| Architectural Boundary | Identity → Role → Permission → Scope → Authority → Action → Evidence → Audit |

---

# 2. Purpose

EA-IMETA-PC-RG-413 defines the authority model for the PC-RG lifecycle.

RG-410 defines which state transitions are permitted.

RG-411 defines how workflows orchestrate those transitions.

RG-412 defines how decisions and evidence are recorded.

This document defines **who is authorised to perform each material action and under what conditions**.

The governing principle is:

> **A permission to execute a technical action is not automatically authority to make a business decision.**

---

# 3. Authority Chain

The authority model SHALL distinguish:

```text
IDENTITY
   ↓
ROLE
   ↓
PERMISSION
   ↓
SCOPE
   ↓
AUTHORITY
   ↓
ACTION
   ↓
DECISION
   ↓
AUDIT
```

Each layer has a different purpose.

---

# 4. Identity

Identity represents the authenticated actor.

Possible actors:

```text
PERSON
SERVICE
SYSTEM
AGENT
EXTERNAL PARTY
```

Every material action SHALL be attributable to an identity.

Anonymous material lifecycle actions SHALL not be permitted.

---

# 5. Role

A role represents a defined responsibility.

Initial PC-RG role catalogue:

```text
CASE OWNER
ASSESSOR
VALIDATOR
VERIFIER
ACCEPTANCE AUTHORITY
CLOSURE AUTHORITY
MONITORING OWNER
REGRESSION ASSESSOR
REMEDIATION OWNER
REVALIDATOR
REVERIFIER
REACCEPTANCE AUTHORITY
AUDITOR
SECURITY ADMINISTRATOR
SYSTEM ADMINISTRATOR
WORKFLOW ADMINISTRATOR
```

Roles SHALL be assigned according to organisational governance.

---

# 6. Permission

A permission authorises a technical operation.

Examples:

```text
READ_CASE
CREATE_EVIDENCE
EDIT_EVIDENCE
PERFORM_VALIDATION
PERFORM_VERIFICATION
REQUEST_ACCEPTANCE
GRANT_ACCEPTANCE
REQUEST_CLOSURE
CLOSE_CASE
START_MONITORING
CONFIRM_REGRESSION
CREATE_REMEDIATION
COMPLETE_REMEDIATION
PERFORM_REVALIDATION
PERFORM_REVERIFICATION
GRANT_REACCEPTANCE
SUSPEND
REVOKE
REOPEN
VIEW_AUDIT
ADMINISTER_WORKFLOW
```

Permission SHALL not by itself establish decision authority.

---

# 7. Scope

Authority SHALL be limited by scope.

Possible scope dimensions:

```text
CASE
PROJECT
BUSINESS UNIT
FUNCTION
RISK CLASS
GEOGRAPHY
DATA CLASSIFICATION
SYSTEM
CUSTOMER
TIME PERIOD
```

Example:

```text
Verifier
+
Permission = VERIFY
+
Scope = assigned cases
```

does not imply authority to verify every case.

---

# 8. Authority

Authority is the approved right to make a governed decision.

Authority SHALL identify:

```text
Decision Type
Role
Scope
Delegation
Conditions
Effective Period
Approval Basis
```

---

# 9. Authority Types

Initial catalogue:

```text
PERFORM
REVIEW
VERIFY
RECOMMEND
APPROVE
ACCEPT
CLOSE
SUSPEND
REVOKE
REOPEN
OVERRIDE
DELEGATE
AUDIT
ADMINISTER
```

These SHALL be separately controlled.

---

# 10. Authority Matrix

| Activity | Perform | Review | Verify | Approve |
|---|---|---|---|---|
| Validation | Validator | Reviewer | Verifier | — |
| Verification | Verifier | Independent Reviewer | Verification Authority | — |
| Acceptance | Case Team | Reviewer | Verifier | Acceptance Authority |
| Closure | Case Owner | Closure Reviewer | — | Closure Authority |
| Monitoring | Monitoring Owner | Reviewer | — | — |
| Regression | Regression Assessor | Reviewer | Independent Verifier | — |
| Remediation | Remediation Owner | Reviewer | Remediation Verifier | — |
| Revalidation | Revalidator | Reviewer | Re-verifier | — |
| Reacceptance | Case Team | Reviewer | Re-verifier | Reacceptance Authority |

Actual organisational assignments SHALL be configured outside this logical model.

---

# 11. Separation of Duties

Separation of duties SHALL prevent a single actor from controlling incompatible stages where risk requires independence.

Preferred separation:

```text
VALIDATOR
   ≠
VERIFIER
   ≠
ACCEPTANCE AUTHORITY
```

and:

```text
REMEDIATION OWNER
   ≠
INDEPENDENT REMEDIATION VERIFIER
```

---

# 12. Conflict of Interest

An actor SHALL not perform a controlled action where a declared conflict makes the actor unsuitable.

The system SHOULD support:

```text
Conflict Declaration
Conflict Review
Recusal
Replacement
Audit
```

---

# 13. Role Assignment

Role assignment SHALL include:

```text
Actor
Role
Scope
Effective From
Effective Until
Assigned By
Reason
Status
```

Assignments SHALL be auditable.

---

# 14. Role Lifecycle

```text
REQUESTED
   ↓
APPROVED
   ↓
ACTIVE
   ↓
SUSPENDED
   ↓
REVOKED / EXPIRED
```

An expired or revoked role SHALL not authorize new actions.

---

# 15. Delegation

Authority may be delegated only where delegation is permitted.

A delegation SHALL define:

```text
Delegator
Delegate
Authority
Scope
Effective Period
Conditions
Approval
```

Delegation SHALL not silently transfer authority beyond its defined scope.

---

# 16. Delegation Limits

The architecture SHOULD prevent:

```text
DELEGATE
  ↓
DELEGATE AGAIN
  ↓
UNCONTROLLED AUTHORITY CHAIN
```

Subdelegation SHALL require explicit permission.

---

# 17. Emergency Authority

Emergency overrides MAY exist for defined scenarios.

They SHALL require:

```text
Emergency Trigger
Emergency Authority
Scope
Reason
Duration
Actions
Evidence
Post-Event Review
```

Emergency authority SHALL not become a general bypass mechanism.

---

# 18. System Authority

Automated services may perform technical actions.

Examples:

```text
Create monitoring record
Generate notification
Queue workflow
Calculate threshold
Create audit event
```

A service SHALL not infer business approval authority from its ability to execute a technical operation.

---

# 19. AI / Agent Authority

Agents SHALL have explicit authority scopes.

Possible levels:

```text
READ
ANALYSE
SUGGEST
PREPARE
EXECUTE
```

Material decision authority SHALL be separately approved.

An agent SHALL not infer:

```text
EXECUTE
=
APPROVE
```

---

# 20. Agent Permission Boundary

The architecture SHALL enforce:

```text
AGENT REQUEST
   ↓
IDENTITY
   ↓
ROLE
   ↓
PERMISSION
   ↓
SCOPE
   ↓
STATE GUARD
   ↓
ACTION
```

Failure at any stage SHALL block the action.

---

# 21. Authority and State

Authority SHALL be checked against current state.

Example:

```text
VERIFIED
   ↓
Acceptance Authority?
   ↓
YES
   ↓
Acceptance permitted
```

But:

```text
DRAFT
   ↓
Acceptance Authority?
   ↓
YES
   ↓
Acceptance STILL BLOCKED
```

because the state guards are not satisfied.

---

# 22. Authority and Evidence

Authority alone does not make a decision valid.

The system SHALL verify:

```text
Authority
+
Required Evidence
+
Criteria
+
State
+
Risk
```

before permitting a material decision.

---

# 23. Authority and Conditions

Conditional authority SHALL record:

```text
Condition
Scope
Duration
Required Review
Consequence
```

A breached authority condition SHALL trigger the defined restriction or escalation.

---

# 24. Approval Model

Material approvals SHALL be explicit.

An approval record SHALL contain:

```text
Approval ID
Decision
Actor
Role
Authority
Scope
Evidence
Timestamp
Conditions
Rationale
Resulting State
```

---

# 25. Multi-Level Approval

High-risk decisions MAY require multiple approvals.

```text
ASSESSMENT
   ↓
FUNCTIONAL APPROVAL
   ↓
RISK APPROVAL
   ↓
EXECUTIVE / DESIGNATED AUTHORITY
```

The required number and type of approvals SHALL be risk-based.

---

# 26. Approval Independence

Where multiple approvals are required, the architecture SHALL support independent approval roles.

The same person SHALL not satisfy multiple independent approval requirements unless an explicitly authorised exception exists.

---

# 27. Review vs Verification

The architecture SHALL distinguish:

```text
REVIEW
```

from:

```text
VERIFICATION
```

A review may examine completeness or quality.

Verification determines whether the defined assurance requirement has been satisfied.

A reviewer does not automatically become a verifier.

---

# 28. Perform vs Approve

The architecture SHALL distinguish:

```text
PERFORM
```

from:

```text
APPROVE
```

Example:

```text
Validator performs validation.
Acceptance Authority approves reliance.
```

Completing the first action SHALL not imply permission for the second.

---

# 29. Suspend vs Revoke

The authority model SHALL distinguish:

```text
SUSPEND
```

from:

```text
REVOKE
```

Suspension temporarily restricts reliance.

Revocation formally removes reliance within scope.

Different authorities MAY be assigned.

---

# 30. Reopen Authority

Reopening SHALL require explicit authority.

A user who can close a case SHALL not automatically be able to reopen it unless the role model permits it.

The reopening decision SHALL record:

```text
Reason
Authority
Scope
Affected State
Required Work
```

---

# 31. Audit Authority

Auditors SHALL have sufficient read access to reconstruct decisions but SHALL not receive unnecessary write permissions.

Preferred principle:

```text
AUDIT
=
READ + ANALYSE + REPORT
```

not:

```text
AUDIT = ADMIN
```

---

# 32. Administrative Authority

System administrators may administer technical configuration.

They SHALL not automatically receive business decision authority.

Administrative operations SHALL be audited.

Examples:

```text
Change role assignment
Change workflow configuration
Manage system users
Modify technical configuration
```

These are not equivalent to:

```text
Approve acceptance
Approve reacceptance
Revoke reliance
```

---

# 33. Privileged Access

Privileged access SHALL support:

```text
Just-in-Time Access
Least Privilege
Approval
Time Limitation
Session Logging
Audit
Review
```

Where technically appropriate.

---

# 34. Permission Inheritance

Permission inheritance SHALL be controlled.

A higher-level role SHALL not automatically receive every lower-level business authority unless explicitly designed.

This prevents accidental privilege escalation.

---

# 35. Scope Enforcement

Every material permission check SHOULD evaluate:

```text
Actor
Role
Permission
Object
Scope
State
Authority
```

A successful authentication alone SHALL never be sufficient.

---

# 36. Access Decision

Conceptually:

```text
REQUEST
  ↓
IDENTITY VALID?
  ↓
ROLE ACTIVE?
  ↓
PERMISSION PRESENT?
  ↓
SCOPE VALID?
  ↓
STATE ALLOWS ACTION?
  ↓
AUTHORITY PRESENT?
  ↓
EVIDENCE / GUARDS SATISFIED?
  ↓
ALLOW
```

Otherwise:

```text
DENY
```

---

# 37. Denial Handling

Denied material actions SHALL provide an appropriate reason category.

Examples:

```text
NO PERMISSION
OUT OF SCOPE
ROLE EXPIRED
STATE INVALID
AUTHORITY MISSING
EVIDENCE MISSING
SEPARATION OF DUTIES VIOLATION
CONFLICT OF INTEREST
CONDITION BREACHED
```

Security-sensitive systems may limit the detail shown to the requester.

---

# 38. SoD Violation

A separation-of-duties violation SHALL be treated as a control failure.

```text
ACTION REQUEST
   ↓
SoD CHECK
   ↓
VIOLATION
   ↓
BLOCK
   ↓
AUDIT
   ↓
ESCALATION
```

---

# 39. Compensating Controls

Where strict separation is impractical, a compensating control MAY be approved.

It SHALL define:

```text
Risk
Exception
Compensating Control
Independent Review
Duration
Authority
Evidence
Expiry
```

Permanent informal exceptions SHALL not be permitted.

---

# 40. Role Conflict Matrix

Illustrative high-risk conflicts:

| Role A | Role B | Default |
|---|---|---|
| Validator | Verifier | Separate |
| Verifier | Acceptance Authority | Separate |
| Remediation Owner | Remediation Verifier | Separate |
| Case Owner | Independent Auditor | Separate |
| System Administrator | Business Approver | Separate |
| Agent | Final Acceptance Authority | Separate unless explicitly approved |

---

# 41. Authority Expiry

Authority SHALL support expiry.

```text
ACTIVE
  ↓
EXPIRING
  ↓
EXPIRED
```

Expired authority SHALL not authorize new decisions.

Existing historical decisions remain valid unless otherwise determined.

---

# 42. Authority Revocation

Authority may be revoked.

```text
ACTIVE
  ↓
REVOKED
```

Revocation SHALL record:

```text
Who revoked
Why
When
Scope
Affected roles
Affected workflows
Required follow-up
```

---

# 43. Authority Impact Analysis

When authority changes, the system SHOULD identify affected:

```text
Open Cases
Pending Tasks
Pending Decisions
Active Workflows
Delegations
Approvals
Monitoring
Revalidation
Reacceptance
```

Material impact SHALL trigger review.

---

# 44. Authority Continuity

The organisation SHALL define fallback authority for critical workflows.

Example:

```text
Primary Acceptance Authority
        ↓ unavailable
Delegated / Alternate Authority
        ↓
Decision
```

Fallback authority SHALL be explicit, not assumed.

---

# 45. Quorum

Some decisions MAY require quorum.

The quorum definition SHALL specify:

```text
Minimum Number
Required Roles
Independence
Scope
Decision Rule
```

Example:

```text
2 of 3 authorised reviewers
+
1 designated acceptance authority
```

---

# 46. Dual Control

High-risk actions MAY require dual control.

```text
ACTOR A PREPARES
      ↓
ACTOR B APPROVES
      ↓
SYSTEM EXECUTES
```

The two actors SHALL be independently identifiable.

---

# 47. Four-Eyes Principle

For designated critical decisions:

```text
ONE PERSON PREPARES
+
ANOTHER PERSON REVIEWS
```

The system SHALL prevent self-approval where the control requires independence.

---

# 48. Service-to-Service Authority

Services acting on behalf of workflows SHALL identify:

```text
Service Identity
Calling Workflow
Calling Actor
Delegated Scope
Permission
Action
```

A downstream service SHALL not blindly trust a caller's claimed business authority.

---

# 49. API Enforcement

Authority SHALL be enforced server-side.

Example:

```text
POST /acceptance/grant
```

requires:

```text
Authenticated Actor
+
Acceptance Permission
+
Correct Scope
+
VERIFIED State
+
Required Evidence
+
No SoD Conflict
+
Acceptance Authority
```

---

# 50. UI Enforcement

The UI SHALL reflect authority but SHALL not be the authoritative enforcement layer.

Example:

```text
Approve button hidden/disabled
```

is useful usability behaviour.

But the backend SHALL independently reject an unauthorised request.

---

# 51. Audit of Authority

The system SHALL audit:

```text
Role Assignment
Role Removal
Permission Change
Delegation
Authority Change
Approval
Override
SoD Exception
Privileged Access
Emergency Authority
```

---

# 52. Authority History

Historical authority SHALL be retained.

The system SHALL support:

```text
Who had authority on date X?
Who delegated authority?
Was the authority valid when the decision was made?
What scope applied?
```

This is required for retrospective audit.

---

# 53. Decision Validation

Before storing a material decision, the system SHOULD validate:

```text
Actor Identity
Role
Permission
Scope
Authority
State
Evidence
Criteria
SoD
Conditions
```

A failed validation SHALL prevent or appropriately classify the decision.

---

# 54. Authority Data Model

Conceptual entities:

```text
Identity
Role
Permission
Scope
Authority
Delegation
Assignment
Conflict
Approval
Override
Exception
```

Relationships:

```text
Identity
  ↓
Role Assignment
  ↓
Role
  ↓
Permission
  ↓
Scope
  ↓
Authority
  ↓
Action
  ↓
Decision
```

---

# 55. MFM Service Boundary

The conceptual MFM implementation should include:

```text
Identity Service
Role Service
Permission Service
Authority Service
Delegation Service
SoD Service
Approval Service
Access Decision Service
Audit Service
```

These services SHALL integrate with:

```text
Workflow
State
Evidence
Decision
```

services.

---

# 56. Policy Evaluation

The architecture SHOULD support central policy evaluation.

Conceptually:

```text
canPerform(actor, action, object, context)
```

returns:

```text
ALLOW
DENY
REQUIRES_APPROVAL
REQUIRES_DUAL_CONTROL
REQUIRES_ESCALATION
```

The result SHALL be auditable for material decisions.

---

# 57. Policy Versioning

Authority policies SHALL be versioned.

Historical decisions SHALL retain the policy version used.

Changes to:

```text
Roles
Permissions
Scopes
SoD Rules
Approval Rules
Delegation Rules
```

SHALL be change controlled.

---

# 58. AI Governance

AI/agent permissions SHALL be versioned and auditable.

The system SHALL record:

```text
Agent Identity
Model
Model Version
Role
Permission
Scope
Action
Human Oversight
Result
```

Agent permissions SHALL default to least privilege.

---

# 59. Agent Escalation

Agents SHALL escalate when:

```text
Authority unclear
Evidence insufficient
State invalid
Policy conflict
SoD conflict
Risk threshold exceeded
Action outside scope
Confidence / certainty below defined threshold
```

The agent SHALL not invent authority to resolve the situation.

---

# 60. Authority Testing

The test architecture SHALL include:

```text
Authorised action succeeds
Unauthorised action fails
Out-of-scope action fails
Expired authority fails
Revoked authority fails
SoD conflict fails
Missing evidence fails
Wrong state fails
Delegated authority works only in scope
Emergency authority expires correctly
```

---

# 61. Security Testing

Security testing SHALL verify:

```text
Privilege Escalation
Role Manipulation
Scope Bypass
Direct API Bypass
Token Reuse
Session Misuse
Delegation Abuse
Administrative Abuse
Agent Permission Escalation
```

---

# 62. Authority Metrics

The MFM system SHOULD report:

```text
Active Roles
Expired Roles
Delegations
Pending Approvals
SoD Violations
Access Denials
Emergency Overrides
Privileged Actions
Authority Changes
Unresolved Conflicts
```

Metrics SHALL be based on authoritative records.

---

# 63. Acceptance Criteria

EA-IMETA-PC-RG-413 is accepted when:

- identity, role, permission, scope and authority are distinct;
- material actions have explicit authority;
- state guards are enforced;
- separation of duties is configurable;
- role assignments are auditable;
- delegation is controlled;
- emergency authority is time-bound;
- system administrators do not automatically receive business authority;
- AI/agent authority is explicit;
- API and UI controls are separated;
- historical authority can be reconstructed;
- authority changes support impact analysis;
- positive and negative authority tests exist.

---

# 64. Next Step

The next logical artifact is the **PC-RG policy and rules engine model**, because authority now defines who may act, while a policy model must define how criteria, thresholds, conditions, risk rules and decision logic are evaluated consistently.

Provisional next artifact:

> **EA-IMETA-PC-RG-414 — POLICY, RULES & DECISION LOGIC MODEL**

This will establish the executable policy boundary between requirements, authority and lifecycle decisions.

---

# 65. Governing Principle

> **Authority is contextual, scoped and time-bound. Permission enables an action; authority legitimises a decision; state guards determine whether the action is currently allowed; audit proves what occurred.**

# END OF EA-IMETA-PC-RG-413

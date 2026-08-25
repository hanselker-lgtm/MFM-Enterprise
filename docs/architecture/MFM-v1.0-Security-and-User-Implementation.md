# MFM v1.0 SECURITY & USER IMPLEMENTATION

## MaritimForeningsManager — Konkret implementeringsgrundlag for authentication, users, roles, permissions, sessions and audit

**Version:** 1.0  
**Status:** Implementation Baseline  
**Parent:** MFM v1.0 Database & Core Foundation Implementation  
**Purpose:** Establish the first protected application layer so all later MFM business modules can operate under one consistent security model

---

# 1. Purpose

This document defines the concrete implementation baseline for:

- users;
- authentication;
- password hashing;
- roles;
- permissions;
- sessions;
- first-run administrator setup;
- authorisation;
- security events;
- audit events;
- administrative controls;
- security testing.

The objective is to make security a working application capability rather than only an architectural concept.

---

# 2. Scope

This implementation covers:

```text
USER
AUTHENTICATION
AUTHORISATION
ROLE
PERMISSION
SESSION
AUDIT
SECURITY EVENTS
```

It does not implement the full accounting, membership, project or grant modules.

Those modules SHALL consume this security layer.

---

# 3. Security Principle

> **No protected business operation is trusted merely because it was initiated from the GUI.**

The security boundary is below the GUI:

```text
USER
 ↓
GUI
 ↓
SERVICE
 ↓
AUTHORISATION
 ↓
BUSINESS OPERATION
 ↓
AUDIT
```

---

# 4. Security Objectives

MFM v1.0 SHALL provide:

```text
Confidentiality
Integrity
Accountability
Availability
Least Privilege
Separation of Duties
```

For a small association, these objectives SHALL be implemented without unnecessary complexity.

---

# 5. Security Architecture

```text
                    USER
                      ↓
                  LOGIN GUI
                      ↓
                 AuthService
                      ↓
              UserRepository
                      ↓
                PASSWORD HASH
                      ↓
                  SESSION
                      ↓
             PermissionService
                      ↓
              BUSINESS SERVICE
                      ↓
                 AUDIT SERVICE
```

---

# 6. Security Components

Minimum components:

```text
AuthService
UserService
RoleService
PermissionService
SessionContext
AuditService
SecurityRepository
UserRepository
RoleRepository
PermissionRepository
```

A separate repository is optional if existing repository structure is sufficient.

---

# 7. User Entity

Minimum user fields:

```text
id
username
display_name
password_hash
status
created_at
updated_at
last_login_at
```

Optional:

```text
email
```

---

# 8. User Status

Recommended controlled values:

```text
ACTIVE
DISABLED
LOCKED
```

A disabled or locked user SHALL not authenticate.

---

# 9. Username

Usernames SHALL be unique.

Comparison SHOULD be case-insensitive.

Example:

```text
Treasurer
treasurer
TREASURER
```

SHOULD represent the same username.

---

# 10. Username Rules

Minimum:

- required;
- trimmed;
- non-empty;
- unique.

The application MAY impose a reasonable length limit.

---

# 11. Display Name

Display name is separate from username.

Example:

```text
Username: treasurer
Display name: Treasurer
```

---

# 12. Password Storage

Passwords SHALL never be stored in plaintext.

The database SHALL store only a password hash and required algorithm metadata.

---

# 13. Password Hashing

Use a password-specific adaptive hashing algorithm supported by the selected Python security library.

Acceptable implementation choices include:

```text
Argon2
bcrypt
PBKDF2
```

The selected implementation SHALL use a cryptographically appropriate salt.

---

# 14. Password Verification

Authentication SHALL compare the supplied password against the stored password hash using the hashing library.

The application SHALL never decrypt a password.

---

# 15. Password Policy

MFM v1.0 SHOULD require:

```text
minimum reasonable length
```

and SHOULD reject obviously weak passwords.

The policy SHALL remain usable for volunteer administrators.

---

# 16. Password Change

Users SHALL be able to change their own password.

Administrators MAY reset another user's password through a controlled process.

---

# 17. Password Reset

A local desktop application does not require email-based password reset for v1.0.

Administrator-assisted reset is sufficient.

---

# 18. Password Reset Rule

An administrator reset SHALL:

```text
invalidate existing sessions
require new password
create audit event
```

---

# 19. First-Run Administrator

On first installation, MFM SHALL provide a controlled administrator setup.

Flow:

```text
FIRST START
 ↓
CREATE ADMINISTRATOR
 ↓
SET PASSWORD
 ↓
CONFIRM
 ↓
STORE HASH
 ↓
AUDIT
 ↓
LOGIN
```

---

# 20. Default Password

There SHALL be no universal default administrator password.

---

# 21. First-Run State

The application SHALL determine whether an administrator has already been configured.

Example:

```text
admin_setup_complete
```

may be stored in configuration or database state.

---

# 22. First-Run Race Prevention

First-run initialization SHALL prevent creation of multiple conflicting initial administrators.

The operation SHALL be transactional.

---

# 23. Authentication

Authentication operation:

```text
username
+
password
        ↓
lookup user
        ↓
verify status
        ↓
verify password
        ↓
create session
```

---

# 24. Authentication Failure

If authentication fails:

```text
deny access
do not create session
record security event
```

The user message SHOULD remain generic.

---

# 25. Generic Login Error

Prefer:

```text
Invalid username or password.
```

Do not reveal whether:

```text
username exists
```

or whether the password alone was wrong.

---

# 26. Failed Login Protection

Repeated failed authentication attempts SHOULD be rate-limited or temporarily blocked.

For a local desktop application, a simple counter and lockout mechanism is sufficient.

---

# 27. Login Attempt Table

Optional table:

```text
security_events
```

may record:

```text
timestamp
username
result
source
```

Do not store passwords.

---

# 28. Account Locking

Recommended:

```text
5 failed attempts
→ temporary lock
```

The exact threshold MAY be configurable.

---

# 29. Lockout Duration

A reasonable local value may be:

```text
15 minutes
```

Administrators MAY manually unlock a user.

---

# 30. Disabled User

If status is:

```text
DISABLED
```

authentication SHALL fail.

---

# 31. Locked User

If status is:

```text
LOCKED
```

authentication SHALL fail until unlocked or the lock expires according to policy.

---

# 32. Session

A successful login creates a session context.

Minimum:

```text
user_id
login_time
last_activity
```

---

# 33. Session Identifier

The application MAY use a secure random session identifier.

It SHALL not use:

```text
username
timestamp alone
```

as a session token.

---

# 34. Session Lifetime

Recommended inactivity timeout:

```text
30 minutes
```

The value MAY be configurable.

---

# 35. Session Timeout

When the session expires:

```text
session invalid
 ↓
return to login
```

Unsaved form data SHOULD be handled safely.

---

# 36. Logout

Logout SHALL:

```text
invalidate session
clear current user
record audit/security event
return to login
```

---

# 37. Application Exit

Normal application shutdown SHALL invalidate the active session context.

---

# 38. Concurrent Sessions

MFM v1.0 MAY allow one or multiple sessions depending on deployment.

For a local single-user desktop installation, one active session is sufficient.

---

# 39. Session Context

A session context SHOULD expose:

```text
user_id
username
display_name
roles
permissions
login_time
last_activity
```

---

# 40. Session Security

Business services SHALL obtain the current authenticated identity from the controlled session context.

A GUI field SHALL never be trusted as the user identity.

---

# 41. Role

A role groups permissions.

Examples:

```text
ADMIN
TREASURER
BOARD
MEMBER_ADMIN
PROJECT_MANAGER
READ_ONLY
```

---

# 42. Role Principle

Roles SHALL be business-readable.

Avoid role names such as:

```text
ROLE_17
```

when a clear name is possible.

---

# 43. Administrator Role

`ADMIN` SHALL manage system administration.

It SHALL not automatically imply permission to bypass financial controls without explicit design.

---

# 44. Treasurer Role

The `TREASURER` role SHOULD include permissions for:

```text
accounting
payments
bank reconciliation
financial reports
```

but not necessarily user administration.

---

# 45. Board Role

The `BOARD` role SHOULD be primarily read-oriented:

```text
management reports
project overview
grant overview
financial overview
```

Specific write permissions may be added where required.

---

# 46. Member Administrator

`MEMBER_ADMIN` SHOULD manage:

```text
members
memberships
fees
member communication data
```

but should not automatically receive unrestricted accounting permissions.

---

# 47. Project Manager

`PROJECT_MANAGER` SHOULD manage:

```text
projects
project budgets
project documents
project status
```

Financial posting permissions remain separately controlled.

---

# 48. Read Only

`READ_ONLY` SHALL not change business data.

It MAY view authorised reports and records.

---

# 49. Permission

Permissions SHALL be granular enough to enforce important boundaries.

Examples:

```text
VIEW_MEMBERS
EDIT_MEMBERS
VIEW_ACCOUNTING
CREATE_VOUCHER
POST_VOUCHER
REVERSE_VOUCHER
VIEW_PROJECTS
EDIT_PROJECTS
VIEW_GRANTS
EDIT_GRANTS
VIEW_DOCUMENTS
MANAGE_DOCUMENTS
VIEW_REPORTS
EXPORT_REPORTS
MANAGE_USERS
MANAGE_ROLES
VIEW_AUDIT
CREATE_BACKUP
RESTORE_BACKUP
```

---

# 50. Permission Naming

Use:

```text
VERB_OBJECT
```

Examples:

```text
POST_VOUCHER
EDIT_MEMBER
VIEW_REPORTS
```

---

# 51. Permission Principle

A permission SHALL represent an actual security decision.

Do not create hundreds of theoretical permissions.

---

# 52. Role-Permission Relationship

Database:

```text
roles
permissions
role_permissions
```

Many-to-many.

---

# 53. User-Role Relationship

Database:

```text
users
roles
user_roles
```

Many-to-many.

A user MAY have multiple roles.

---

# 54. Effective Permissions

Effective permissions are:

```text
UNION of permissions from all assigned roles
```

unless an explicit deny model is introduced.

MFM v1.0 SHOULD avoid deny permissions.

---

# 55. Least Privilege

Users SHALL receive only permissions needed for their responsibilities.

---

# 56. Separation of Duties

Financially sensitive operations SHOULD be separable.

Example:

```text
CREATE_VOUCHER
```

may be available to one role while:

```text
POST_VOUCHER
```

is restricted.

---

# 57. Approval Boundary

Where the association requires approval, MFM SHOULD support:

```text
prepared
approved
posted
```

as separate states.

---

# 58. Security Enforcement

Permission checks SHALL occur inside the service layer.

Example:

```python
accounting_service.post_voucher(...)
```

must verify:

```text
POST_VOUCHER
```

before changing data.

---

# 59. GUI Permission Check

The GUI MAY hide or disable a button based on permissions.

But this is only usability.

It is not the security boundary.

---

# 60. Service Permission Check

The service SHALL perform the authoritative check.

---

# 61. Direct Invocation Test

If a read-only user calls:

```text
AccountingService.post_voucher()
```

directly:

```text
DENIED
```

must occur.

---

# 62. Permission Failure

Permission failure SHALL:

```text
stop operation
avoid data change
record security/audit event where appropriate
return controlled error
```

---

# 63. Permission Exception

Use a dedicated:

```text
PermissionDeniedError
```

or equivalent application exception.

---

# 64. UserService

`UserService` SHALL provide controlled operations:

```text
create_user()
disable_user()
enable_user()
lock_user()
unlock_user()
change_password()
reset_password()
assign_role()
remove_role()
```

---

# 65. User Creation

Creating a user SHALL:

```text
validate username
validate password
hash password
create record
assign initial roles
audit
```

within appropriate transactional boundaries.

---

# 66. User Disable

Disabling a user SHALL:

```text
change status
invalidate active session(s)
audit
```

---

# 67. User Enable

Enabling a user SHALL:

```text
change status
audit
```

It SHALL not silently assign new permissions.

---

# 68. Role Assignment

Role changes SHALL be auditable.

Example:

```text
Treasurer role assigned to user X.
```

---

# 69. Role Removal

Role removal SHALL also be audited.

---

# 70. Last Administrator Protection

MFM SHALL prevent accidental removal or disabling of the last active administrator.

---

# 71. Administrator Count

Before disabling/removing an administrator:

```text
active administrator count
```

SHALL be checked.

---

# 72. Last Administrator Rule

If only one active administrator remains:

```text
operation denied
```

unless an equivalent administrator is created or assigned in the same controlled operation.

---

# 73. Role Modification

Changes to system roles SHALL be restricted.

For v1.0, administrators MAY manage user-role assignments without editing the built-in permission definitions.

---

# 74. Permission Definition

System permissions SHOULD be seeded and stable in v1.0.

Custom permissions are not required.

---

# 75. Security Repository

A security repository MAY expose:

```text
find_user_by_username()
get_user_roles()
get_role_permissions()
get_user_permissions()
record_security_event()
```

---

# 76. User Repository

`UserRepository` SHOULD expose:

```text
create()
get_by_id()
get_by_username()
update_status()
update_password_hash()
update_last_login()
```

---

# 77. Role Repository

`RoleRepository` SHOULD expose:

```text
get_by_id()
get_by_name()
list()
assign_to_user()
remove_from_user()
```

---

# 78. Permission Repository

`PermissionRepository` SHOULD expose:

```text
get_by_name()
list()
get_for_role()
get_for_user()
```

---

# 79. AuditService

`AuditService` SHALL provide a consistent method for business accountability.

Conceptually:

```text
record(
    user,
    action,
    entity,
    entity_id,
    description
)
```

---

# 80. Audit Event

Minimum:

```text
timestamp
user_id
action
entity_type
entity_id
description
```

---

# 81. Audit Event Types

Examples:

```text
LOGIN_SUCCESS
LOGIN_FAILURE
LOGOUT
USER_CREATED
USER_DISABLED
USER_ENABLED
PASSWORD_CHANGED
PASSWORD_RESET
ROLE_ASSIGNED
ROLE_REMOVED
PERMISSION_DENIED
```

Business modules add:

```text
VOUCHER_POSTED
MEMBER_UPDATED
PROJECT_CREATED
GRANT_APPROVED
DOCUMENT_ADDED
```

---

# 82. Audit Immutability

No normal UI function SHALL allow:

```text
edit audit
delete audit
```

---

# 83. Audit Display

Users with:

```text
VIEW_AUDIT
```

may view audit events.

---

# 84. Audit Filtering

Audit screen SHOULD support:

```text
date range
user
action
entity
entity id
```

---

# 85. Audit Export

Audit export MAY be available to authorised administrators.

Exports SHALL themselves be auditable where appropriate.

---

# 86. Security Events versus Audit

Security events describe:

```text
authentication
authorisation
account security
```

Audit events describe:

```text
business accountability
```

They may share infrastructure but should remain conceptually distinct.

---

# 87. Security Event Examples

```text
LOGIN_FAILURE
ACCOUNT_LOCKED
PERMISSION_DENIED
SESSION_EXPIRED
```

---

# 88. Audit Examples

```text
MEMBER_CREATED
VOUCHER_POSTED
PROJECT_CREATED
GRANT_APPROVED
DOCUMENT_ATTACHED
```

---

# 89. Login Success

On successful login:

```text
last_login_at
```

SHALL be updated.

A security event SHALL be recorded.

---

# 90. Login Failure

On failed login:

```text
attempt counter
security event
```

SHALL be updated.

---

# 91. Failed Login Counter

Counter MAY be stored on user:

```text
failed_login_count
locked_until
```

or in a dedicated security table.

---

# 92. Successful Login Reset

After successful login:

```text
failed_login_count = 0
locked_until = NULL
```

where this model is used.

---

# 93. Lockout Audit

Locking an account SHALL generate:

```text
ACCOUNT_LOCKED
```

---

# 94. Unlock Audit

Administrative unlock SHALL generate:

```text
ACCOUNT_UNLOCKED
```

---

# 95. Session Expiration Audit

A session timeout MAY generate:

```text
SESSION_EXPIRED
```

---

# 96. Security Configuration

Security settings MAY include:

```text
session_timeout_minutes
max_failed_logins
lockout_minutes
minimum_password_length
```

---

# 97. Secure Defaults

Default configuration SHALL favour:

```text
enabled authentication
reasonable session timeout
password hashing
audit enabled
```

---

# 98. No Security Bypass

There SHALL be no hidden:

```text
ADMIN = bypass everything
```

mechanism outside the defined permission model.

---

# 99. Development Bypass

Development-only bypasses SHALL never be active in production.

---

# 100. Test Authentication

Automated tests SHALL create test users with known synthetic passwords.

Passwords SHALL never be committed to production configuration.

---

# 101. Password Test

Test:

```text
correct password → success
wrong password → failure
changed password → old denied
new password → success
```

---

# 102. User Status Test

Test:

```text
ACTIVE → login allowed
DISABLED → login denied
LOCKED → login denied
```

---

# 103. Permission Test

Test:

```text
permission exists → allowed
permission missing → denied
```

---

# 104. Role Test

Test:

```text
role assigned → permission available
role removed → permission unavailable
```

---

# 105. Multi-Role Test

A user with:

```text
BOARD
TREASURER
```

SHALL receive the union of authorised permissions.

---

# 106. Last Administrator Test

Attempt to disable the only administrator.

Expected:

```text
DENIED
NO CHANGE
AUDIT
```

---

# 107. Session Test

Test:

```text
login
session active
timeout
session invalid
```

---

# 108. Logout Test

After logout:

```text
protected operation
```

must fail.

---

# 109. Direct Service Security Test

Call protected service without session.

Expected:

```text
AuthenticationRequired
```

---

# 110. Direct Service Permission Test

Call protected service with insufficient permission.

Expected:

```text
PermissionDenied
```

---

# 111. Audit Test

Execute a material business operation.

Expected:

```text
audit event exists
correct user
correct action
correct entity
```

---

# 112. Audit Tampering Test

Attempt to modify an audit event through normal service/API.

Expected:

```text
DENIED
```

---

# 113. Password Storage Test

Inspect database test fixture.

Expected:

```text
no plaintext password
```

---

# 114. SQL Security Test

Username/password values containing SQL metacharacters SHALL not produce SQL injection.

---

# 115. Session Identity Test

Change GUI-visible user data without changing session.

Expected:

```text
service still uses authenticated session identity
```

---

# 116. Permission Cache

MFM v1.0 MAY cache permissions in the session for performance.

If roles change, the session SHALL be refreshed or invalidated.

---

# 117. Role Change During Session

When a user's role changes:

```text
existing session
```

SHOULD be invalidated or permission cache refreshed immediately.

---

# 118. Disable During Session

Disabling a user SHALL invalidate active sessions where feasible.

---

# 119. Security Context

A service SHOULD receive a security context:

```text
SecurityContext
```

containing authenticated identity and permission evaluation.

---

# 120. Security Context Contract

Minimum operations:

```text
is_authenticated()
has_permission()
require_permission()
require_authenticated()
```

---

# 121. Example

Conceptually:

```python
security.require_permission("POST_VOUCHER")
```

If permission is missing:

```text
PermissionDeniedError
```

---

# 122. Service Pattern

Recommended:

```text
def post_voucher(...):
    security.require_permission("POST_VOUCHER")
    validate(...)
    transaction(...)
    audit(...)
```

---

# 123. Security Check Ordering

Preferred:

```text
AUTHENTICATION
 ↓
AUTHORISATION
 ↓
VALIDATION
 ↓
TRANSACTION
```

Do not reveal unnecessary business information to unauthorised users.

---

# 124. Audit Ordering

For successful operations:

```text
business change
+
audit
 ↓
commit
```

where audit is part of the required atomic operation.

---

# 125. Permission Failure Audit

A permission failure SHOULD be recorded as a security event.

It SHALL not reveal sensitive information to the user.

---

# 126. Audit Failure

If audit is mandatory for a material state change and audit cannot be written:

```text
ROLLBACK
```

The system SHALL not silently perform the business operation without accountability.

---

# 127. Authentication Failure

If security-event logging fails during a failed login, the application SHOULD still deny login.

Security logging failure must never turn a failed authentication into success.

---

# 128. Database Transaction Security

User creation, role assignment and security-critical changes SHALL use appropriate transactions.

---

# 129. User Creation Example

```text
BEGIN
 ↓
validate username
 ↓
hash password
 ↓
insert user
 ↓
assign role
 ↓
audit
 ↓
COMMIT
```

---

# 130. User Disable Example

```text
BEGIN
 ↓
verify target
 ↓
verify last-admin rule
 ↓
disable user
 ↓
invalidate sessions
 ↓
audit
 ↓
COMMIT
```

---

# 131. Password Change Example

```text
AUTHENTICATED
 ↓
verify current password
 ↓
validate new password
 ↓
hash new password
 ↓
save
 ↓
invalidate other sessions
 ↓
audit
 ↓
COMMIT
```

---

# 132. Administrator Reset Example

```text
ADMIN AUTHORISED
 ↓
validate target
 ↓
generate/set temporary password
 ↓
hash
 ↓
invalidate sessions
 ↓
force password change
 ↓
audit
 ↓
COMMIT
```

---

# 133. Temporary Password

If administrator reset uses a temporary password, it SHALL:

```text
be generated securely
be communicated securely
expire or require immediate change
```

---

# 134. Password Change Required

A user with a temporary password SHOULD be marked:

```text
must_change_password = true
```

---

# 135. Role Assignment Example

```text
ADMIN
 ↓
UserService.assign_role()
 ↓
permission validation
 ↓
database update
 ↓
audit
 ↓
refresh session
```

---

# 136. Role Removal Example

Same controlled process applies.

---

# 137. Security GUI

Minimum screens:

```text
Login
Users
Roles
User Roles
Change Password
Audit
```

---

# 138. Login Screen

Minimum:

```text
Username
Password
Login
Exit
```

---

# 139. Login Screen Rules

Do not display:

```text
password requirements
```

until useful for password creation/change.

---

# 140. User Administration

User list SHOULD show:

```text
username
display name
status
roles
last login
```

---

# 141. User Form

Minimum:

```text
username
display name
status
roles
```

Password fields are only shown when creating/changing/resetting.

---

# 142. Role Assignment GUI

Use controlled selection.

Do not expose raw role IDs.

---

# 143. Permission GUI

For v1.0, permission definitions MAY be read-only.

Administrators manage roles rather than arbitrary permission creation.

---

# 144. Audit GUI

Audit list SHOULD support:

```text
timestamp
user
action
entity
description
```

---

# 145. Security Status

Administration screen MAY show:

```text
current user
roles
session timeout
last login
```

---

# 146. Navigation Security

If user lacks:

```text
MANAGE_USERS
```

the User Administration screen SHALL not be accessible.

---

# 147. Audit Access

If user lacks:

```text
VIEW_AUDIT
```

audit data SHALL not be accessible.

---

# 148. Export Security

If user lacks:

```text
EXPORT_REPORTS
```

report export SHALL be denied even if report viewing is permitted.

---

# 149. Backup Security

If user lacks:

```text
CREATE_BACKUP
```

manual backup creation SHALL be denied.

---

# 150. Restore Security

Restore SHALL be restricted to an administrative permission such as:

```text
RESTORE_BACKUP
```

---

# 151. Financial Security

Financial permissions SHOULD be separated:

```text
VIEW_ACCOUNTING
CREATE_VOUCHER
EDIT_VOUCHER
POST_VOUCHER
REVERSE_VOUCHER
RECONCILE_BANK
```

---

# 152. Membership Security

Membership permissions:

```text
VIEW_MEMBERS
CREATE_MEMBER
EDIT_MEMBER
MANAGE_MEMBERSHIP
MANAGE_FEES
```

---

# 153. Project Security

Project permissions:

```text
VIEW_PROJECTS
CREATE_PROJECT
EDIT_PROJECT
MANAGE_PROJECT_BUDGET
CLOSE_PROJECT
```

---

# 154. Grant Security

Grant permissions:

```text
VIEW_GRANTS
CREATE_GRANT
EDIT_GRANT
APPROVE_GRANT
RECORD_GRANT_RECEIPT
```

---

# 155. Document Security

Document permissions:

```text
VIEW_DOCUMENTS
ADD_DOCUMENT
EDIT_DOCUMENT_METADATA
ARCHIVE_DOCUMENT
```

---

# 156. Reporting Security

Reporting permissions:

```text
VIEW_REPORTS
EXPORT_REPORTS
VIEW_FINANCIAL_REPORTS
```

---

# 157. Security Permission Baseline

The v1.0 permission set SHOULD remain limited to real operational decisions.

---

# 158. Permission Matrix

Example baseline:

| Permission | ADMIN | TREASURER | BOARD | MEMBER_ADMIN | PROJECT_MANAGER | READ_ONLY |
|---|---:|---:|---:|---:|---:|---:|
| VIEW_MEMBERS | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| EDIT_MEMBER | ✓ |  |  | ✓ |  |  |
| VIEW_ACCOUNTING | ✓ | ✓ | ✓ |  |  | ✓ |
| CREATE_VOUCHER | ✓ | ✓ |  |  |  |  |
| POST_VOUCHER | ✓ | ✓ |  |  |  |  |
| REVERSE_VOUCHER | ✓ | ✓ |  |  |  |  |
| VIEW_PROJECTS | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| EDIT_PROJECT | ✓ |  |  |  | ✓ |  |
| MANAGE_PROJECT_BUDGET | ✓ | ✓ |  |  | ✓ |  |
| VIEW_GRANTS | ✓ | ✓ | ✓ |  | ✓ | ✓ |
| APPROVE_GRANT | ✓ |  | ✓ |  |  |  |
| VIEW_DOCUMENTS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ADD_DOCUMENT | ✓ | ✓ |  | ✓ | ✓ |  |
| VIEW_REPORTS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| EXPORT_REPORTS | ✓ | ✓ | ✓ |  | ✓ |  |
| MANAGE_USERS | ✓ |  |  |  |  |  |
| MANAGE_ROLES | ✓ |  |  |  |  |  |
| VIEW_AUDIT | ✓ | ✓ | ✓ |  |  |  |
| CREATE_BACKUP | ✓ | ✓ |  |  |  |  |
| RESTORE_BACKUP | ✓ |  |  |  |  |  |

This is a baseline, not a mandatory organisational policy. The association MAY adjust role assignments.

---

# 159. Governance Boundary

The software SHALL enforce technical permissions.

The association's board remains responsible for defining who should receive those permissions.

---

# 160. Human Authority

MFM SHALL not autonomously:

```text
grant a user new authority
```

or:

```text
change a user's role
```

without authorised human action.

---

# 161. AI Boundary

AI features, if added later, SHALL not:

```text
create administrator
grant permissions
bypass authorisation
disable audit
```

---

# 162. Audit Boundary

Audit is a record of what happened.

It is not a mechanism for approving actions.

---

# 163. Security Safe State

If security infrastructure fails:

```text
DENY protected action
```

This is preferable to allowing an uncertain operation.

---

# 164. Fail Closed

For protected operations:

```text
unknown permission
→ DENY
```

not:

```text
unknown permission
→ ALLOW
```

---

# 165. Authentication Safe State

If user identity cannot be established:

```text
NO PROTECTED ACTION
```

---

# 166. Role Safe State

If role data cannot be loaded:

```text
NO PROTECTED ACTION
```

unless the operation is explicitly public and safe.

---

# 167. Audit Safe State

If mandatory audit cannot be recorded:

```text
ROLLBACK MATERIAL CHANGE
```

---

# 168. Security Health

The application SHOULD be able to detect:

```text
missing permission definitions
broken role assignments
invalid user state
```

---

# 169. Security Startup Validation

At startup verify:

```text
required roles exist
required permissions exist
admin exists
schema compatible
```

---

# 170. Seed Roles

Initial roles SHALL be inserted idempotently.

Running initialization twice SHALL not duplicate them.

---

# 171. Seed Permissions

Initial permissions SHALL be inserted idempotently.

---

# 172. Role-Permission Seeding

Default role assignments SHALL be deterministic.

---

# 173. Custom Role Changes

For v1.0, administrators MAY be allowed to assign built-in roles.

Custom role creation is optional.

---

# 174. Role Deletion

Built-in roles SHOULD not be physically deleted.

They MAY be disabled in a future extension if required.

---

# 175. Permission Deletion

Built-in permissions SHALL not be deleted through ordinary administration.

---

# 176. Security Database Constraints

Recommended:

```text
users.username UNIQUE
roles.name UNIQUE
permissions.name UNIQUE
user_roles(user_id, role_id) UNIQUE
role_permissions(role_id, permission_id) UNIQUE
```

---

# 177. Password Hash Migration

If the hashing algorithm changes in a future release, MFM MAY rehash the password after successful authentication.

---

# 178. Password Hash Metadata

The stored hash should contain or be associated with sufficient algorithm information to permit future verification.

---

# 179. Password Policy Change

Changing the password policy SHALL not invalidate existing passwords unless explicitly required.

---

# 180. Session Invalidation

Security-sensitive changes SHALL invalidate sessions where necessary.

Examples:

```text
password reset
user disabled
role change
permission change
```

---

# 181. Current Session after Password Change

A user may remain in the current session after changing their own password, provided the session is revalidated.

Other sessions SHOULD be invalidated.

---

# 182. Administrator Role Change

Changing an administrator's role SHALL immediately affect future permission checks.

---

# 183. Session Permission Cache

If permissions are cached:

```text
role change
→ refresh/invalidate cache
```

---

# 184. Security Service API

Recommended conceptual API:

```text
authenticate(username, password)
logout(session)
get_current_user()
require_authenticated()
require_permission(permission)
has_permission(permission)
```

---

# 185. User Service API

Recommended:

```text
create_user()
update_user()
disable_user()
enable_user()
lock_user()
unlock_user()
change_password()
reset_password()
assign_role()
remove_role()
```

---

# 186. Audit Service API

Recommended:

```text
record()
record_security_event()
record_login()
record_logout()
```

---

# 187. Session API

Recommended:

```text
create()
get()
touch()
invalidate()
is_valid()
```

---

# 188. Repository API

Repositories SHALL remain persistence-focused.

---

# 189. Security Testing Strategy

Security tests SHALL be primarily service-level.

GUI tests alone are insufficient.

---

# 190. Security Regression Set

Every security defect SHALL become a regression test.

---

# 191. Example Regression

Bug:

```text
Read-only user could post voucher by calling service directly.
```

Regression:

```text
test_read_only_cannot_post_voucher()
```

---

# 192. Example Regression

Bug:

```text
Disabled user remained logged in.
```

Regression:

```text
test_disabling_user_invalidates_session()
```

---

# 193. Example Regression

Bug:

```text
Last administrator could be removed.
```

Regression:

```text
test_last_admin_cannot_be_removed()
```

---

# 194. Example Regression

Bug:

```text
Audit missing after user role change.
```

Regression:

```text
test_role_change_creates_audit()
```

---

# 195. Security Acceptance Criteria

MFM v1.0 security implementation is accepted when:

```text
passwords are hashed
login works
logout works
sessions expire
roles work
permissions work
service-level authorisation works
audit works
last-admin protection works
disabled users cannot login
security tests pass
```

---

# 196. Security Release Blockers

Release SHALL be blocked by:

```text
plaintext passwords
bypassable service permissions
missing audit on mandatory material operations
broken session invalidation
disabled users able to authenticate
SQL injection
universal default password
```

---

# 197. Practical Implementation Order

Implement in this order:

```text
1. security tables
2. password hashing
3. UserRepository
4. RoleRepository
5. PermissionRepository
6. AuthService
7. SessionContext
8. PermissionService
9. AuditService
10. UserService
11. login GUI
12. administration GUI
13. security tests
```

---

# 198. First Security Milestone

The first milestone:

```text
application starts
 ↓
administrator created
 ↓
administrator logs in
 ↓
dashboard opens
 ↓
logout works
```

---

# 199. Second Security Milestone

Add:

```text
roles
permissions
```

and protect the first business service.

---

# 200. Third Security Milestone

Add:

```text
audit
session timeout
failed-login protection
```

---

# 201. Fourth Security Milestone

Protect:

```text
accounting
membership
projects
grants
documents
reports
```

as each module is implemented.

---

# 202. Security and Accounting

Accounting SHALL not be implemented as an unsecured standalone GUI feature.

The service SHALL require:

```text
authentication
permission
```

from its first implementation.

---

# 203. Security and Membership

Membership service SHALL require appropriate membership permissions.

---

# 204. Security and Projects

Project service SHALL require appropriate project permissions.

---

# 205. Security and Grants

Grant approval SHALL require explicit authority.

---

# 206. Security and Documents

Document access SHALL be controlled according to document permissions and future entity-level rules.

---

# 207. Security and Reporting

Reports SHALL be filtered according to report permissions.

---

# 208. Security and Backup

Restore SHALL require stronger authority than ordinary backup creation.

---

# 209. Security and Configuration

Only authorised administrators may change security-sensitive configuration.

---

# 210. Configuration Audit

Changes to:

```text
session timeout
password policy
lockout policy
```

SHALL be auditable.

---

# 211. Security Logging

Technical security failures SHALL be logged.

---

# 212. Privacy Principle

MFM stores personal data.

The security model SHALL therefore minimise unnecessary exposure.

---

# 213. Personal Data in Logs

Do not place unnecessary:

```text
address
phone
email
```

in technical logs.

---

# 214. Personal Data in Audit

Audit descriptions SHOULD identify the action without duplicating unnecessary personal information.

---

# 215. Export Protection

Authorised exports may contain personal data.

Export permissions SHALL therefore be controlled.

---

# 216. Document Access

Documents may contain sensitive association information.

Document access SHALL not automatically be unrestricted merely because the user can see the project.

Entity-specific controls MAY be introduced later.

---

# 217. Security Architecture Simplicity

MFM v1.0 SHALL not introduce:

```text
OAuth
SSO
LDAP
cloud identity
multi-factor infrastructure
```

unless future deployment requires them.

---

# 218. Future Extension

The security model SHOULD allow future:

```text
MFA
central identity
server deployment
remote access
```

without requiring a complete rewrite.

---

# 219. No Future Dependency

These future capabilities SHALL not be required for v1.0.

---

# 220. Security Documentation

The user/administrator documentation SHALL explain:

```text
login
password change
user creation
role assignment
disable user
audit
backup permissions
```

---

# 221. Administrator Checklist

```text
[ ] Create administrator
[ ] Change initial password
[ ] Create required users
[ ] Assign roles
[ ] Review permissions
[ ] Test login
[ ] Test logout
[ ] Verify audit
[ ] Verify backup access
```

---

# 222. Security Acceptance Scenario

Complete scenario:

```text
Create administrator
 ↓
Login
 ↓
Create Treasurer
 ↓
Assign Treasurer role
 ↓
Login as Treasurer
 ↓
Access accounting
 ↓
Attempt user administration
 ↓
DENIED
 ↓
Post authorised transaction
 ↓
Audit event
 ↓
Logout
```

Expected:

```text
security boundaries respected
```

---

# 223. Read-Only Acceptance Scenario

```text
Login as READ_ONLY
 ↓
View report
 ↓
Export if authorised
 ↓
Attempt edit member
 ↓
DENIED
 ↓
Attempt post voucher
 ↓
DENIED
```

---

# 224. Disabled User Scenario

```text
User active
 ↓
Login
 ↓
Administrator disables user
 ↓
Session invalidated
 ↓
User cannot continue protected operations
```

---

# 225. Password Change Scenario

```text
Login
 ↓
Change password
 ↓
Logout
 ↓
Old password denied
 ↓
New password accepted
```

---

# 226. Last Administrator Scenario

```text
Two administrators
 ↓
Remove one
 ↓
Allowed

One administrator remains
 ↓
Attempt removal
 ↓
DENIED
```

---

# 227. Audit Scenario

```text
User role changed
 ↓
Audit event
 ↓
Correct actor
 ↓
Correct target
 ↓
Correct old/new state
```

---

# 228. Security Failure Scenario

If permission database cannot be read:

```text
protected operation
 ↓
FAIL CLOSED
 ↓
no business data change
 ↓
technical error logged
```

---

# 229. Final Security Architecture

```text
                         USER
                           ↓
                        LOGIN
                           ↓
                      AUTHSERVICE
                           ↓
                     SESSION CONTEXT
                           ↓
                   PERMISSION SERVICE
                           ↓
                    BUSINESS SERVICE
                           ↓
                    TRANSACTION
                           ↓
                       AUDIT
                           ↓
                      DATABASE
```

---

# 230. Final Security Rules

```text
RULE 1
Passwords SHALL never be stored in plaintext.

RULE 2
Authentication SHALL be required for protected operations.

RULE 3
Authorisation SHALL be enforced in services.

RULE 4
GUI visibility is not a security control.

RULE 5
Permissions SHALL default to deny.

RULE 6
Material changes SHALL be auditable.

RULE 7
Audit records SHALL not be normally editable or deletable.

RULE 8
The last active administrator SHALL be protected.

RULE 9
Disabled users SHALL not authenticate.

RULE 10
Security-sensitive changes SHALL invalidate or refresh affected sessions.

RULE 11
Security failures SHALL fail closed.

RULE 12
MFM v1.0 security SHALL remain proportionate to the association.
```

---

# 231. Final Implementation Principle

> **Security must be built into every MFM business service from the beginning, not added after the application is finished.**

The implementation sequence is:

```text
AUTHENTICATE
 ↓
AUTHORISE
 ↓
EXECUTE
 ↓
AUDIT
```

---

# 232. Next Implementation Layer

After this security baseline is implemented, the next major implementation file SHALL be:

```text
MFM v1.0 ACCOUNTING CORE IMPLEMENTATION
```

The accounting module will then be built on:

```text
Database Foundation
+
Security
+
Audit
```

---

# 233. Final Governing Principle

> **Every MFM operation must have a known actor, a known authority, a controlled execution path and, where material, an auditable result.**

# END OF MFM v1.0 SECURITY & USER IMPLEMENTATION

# EA-IMETA-BUILD-01
# SYSTEM FOUNDATION

### Version 1.0
### Status: COMPLETE
### Governing Architecture: EA-IMETA-MASTER-01
### Implementation Basis: EA-IMETA-IMPLEMENTATION-01 through -08

---

# 1. PURPOSE

EA-IMETA-BUILD-01 defines the technical foundation for constructing the actual EA-IMETA system.

The previous EA-IMETA work established the architecture and implementation roadmap.

This document begins the physical build.

The purpose is to establish:

- repository structure
- source-code structure
- runtime structure
- configuration
- environment separation
- logging
- error handling
- security foundation
- dependency management
- database foundation
- API foundation
- service foundation
- testing foundation
- migration foundation
- deployment foundation
- documentation foundation

The central principle is:

> BUILD A STABLE, TESTABLE AND MAINTAINABLE FOUNDATION BEFORE ADDING BUSINESS CAPABILITIES.

---

# 2. BUILD PROGRAM

The physical build follows:

```text
BUILD-01
SYSTEM FOUNDATION
        ↓
BUILD-02
REPOSITORY & DATABASE
        ↓
BUILD-03
METAMODEL ENGINE
        ↓
BUILD-04
WORKFLOW & GOVERNANCE ENGINE
        ↓
BUILD-05
INTEGRATION LAYER
        ↓
BUILD-06
KNOWLEDGE GRAPH
        ↓
BUILD-07
DASHBOARD & DECISION SERVICES
        ↓
BUILD-08
AI & AGENT LAYER
        ↓
BUILD-09
ADAPTIVE ARCHITECTURE
        ↓
BUILD-10
INTEGRATION TEST & SYSTEM VALIDATION
```

---

# 3. BUILD-01 SCOPE

BUILD-01 establishes the technical skeleton only.

It includes:

```text
PROJECT
RUNTIME
CONFIGURATION
LOGGING
ERROR HANDLING
SECURITY FOUNDATION
DATABASE CONNECTION FOUNDATION
API FOUNDATION
SERVICE FOUNDATION
TEST FOUNDATION
MIGRATION FOUNDATION
DEPLOYMENT FOUNDATION
```

It does not yet implement the complete EA-IMETA metamodel.

---

# 4. TARGET TECHNOLOGY PRINCIPLES

The initial implementation should use technologies that are:

- mature
- maintainable
- well documented
- widely supported
- suitable for Windows and server deployment
- suitable for API development
- suitable for database integration
- suitable for later AI integration

The architecture shall avoid unnecessary technology complexity during the foundation phase.

---

# 5. RECOMMENDED BASE STACK

Initial recommended stack:

```text
Language:
Python 3.x

API:
FastAPI

Database:
PostgreSQL

ORM / Database Access:
SQLAlchemy

Validation:
Pydantic

Migrations:
Alembic

Testing:
pytest

API Testing:
httpx / FastAPI TestClient

Configuration:
environment variables + typed settings

Logging:
Python logging / structured logging

Packaging:
pyproject.toml

Version Control:
Git
```

The exact versions shall be pinned in the implementation repository.

---

# 6. ARCHITECTURE STYLE

The system should use a modular layered architecture.

```text
PRESENTATION
     ↓
API
     ↓
APPLICATION SERVICES
     ↓
DOMAIN
     ↓
REPOSITORIES
     ↓
DATABASE
```

Supporting infrastructure:

```text
CONFIGURATION
LOGGING
SECURITY
OBSERVABILITY
INTEGRATION
```

---

# 7. CORE DESIGN RULE

Business logic shall not be placed directly inside API route handlers.

Avoid:

```text
API
 ↓
SQL
 ↓
BUSINESS LOGIC
```

Prefer:

```text
API
 ↓
APPLICATION SERVICE
 ↓
DOMAIN
 ↓
REPOSITORY
 ↓
DATABASE
```

---

# 8. PROJECT DIRECTORY

Initial project structure:

```text
ea-imeta/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
├── src/
│   └── ea_imeta/
│       │
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── router.py
│       │   └── health.py
│       │
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── logging.py
│       │   ├── security.py
│       │   └── exceptions.py
│       │
│       ├── db/
│       │   ├── __init__.py
│       │   ├── session.py
│       │   └── base.py
│       │
│       ├── domain/
│       │   └── __init__.py
│       │
│       ├── services/
│       │   └── __init__.py
│       │
│       ├── repositories/
│       │   └── __init__.py
│       │
│       └── models/
│           └── __init__.py
│
├── migrations/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── api/
│
├── docs/
│
├── scripts/
│
└── deployment/
```

---

# 9. SOURCE PACKAGE

The Python package shall be named:

```text
ea_imeta
```

The package shall not use generic names such as:

```text
app
project
main_app
manager
```

This reduces import ambiguity.

---

# 10. APPLICATION ENTRY POINT

The application entry point shall be:

```text
src/ea_imeta/main.py
```

It shall expose the application object.

Conceptually:

```python
from fastapi import FastAPI

app = FastAPI(
    title="EA-IMETA",
    version="1.0.0",
)
```

The final application factory pattern should be preferred for testability.

---

# 11. APPLICATION FACTORY

Recommended structure:

```text
create_app()
```

The application factory should:

1. create the FastAPI application
2. load configuration
3. configure logging
4. register middleware
5. register routers
6. register exception handlers
7. configure health endpoints

---

# 12. API ROOT

Initial API root:

```text
/api/v1
```

All future API resources should be versioned.

Example:

```text
/api/v1/health
/api/v1/repository
/api/v1/workflows
/api/v1/graph
```

---

# 13. API VERSIONING

The initial API version is:

```text
v1
```

Breaking changes shall use a new API version.

Example:

```text
/api/v1
/api/v2
```

Existing clients should not silently break.

---

# 14. HEALTH ENDPOINT

The foundation shall expose:

```text
GET /api/v1/health
```

Example response:

```json
{
  "status": "ok",
  "service": "ea-imeta",
  "version": "1.0.0"
}
```

---

# 15. READINESS ENDPOINT

A readiness endpoint should be provided:

```text
GET /api/v1/health/ready
```

It should verify required dependencies where appropriate.

Example:

```text
API
DATABASE
CONFIGURATION
```

---

# 16. LIVENESS ENDPOINT

A liveness endpoint:

```text
GET /api/v1/health/live
```

should confirm that the application process is running.

Liveness should not perform expensive dependency checks.

---

# 17. CONFIGURATION

Configuration shall be externalized.

Do not hard-code:

```text
database passwords
API keys
secret keys
environment-specific URLs
```

Configuration should come from:

```text
environment variables
configuration files
secret management
```

---

# 18. ENVIRONMENT MODEL

The build shall support:

```text
DEVELOPMENT
TEST
STAGING
PRODUCTION
```

Each environment shall have separate configuration.

---

# 19. ENVIRONMENT VARIABLES

Initial variables:

```text
EA_IMETA_ENV
EA_IMETA_APP_NAME
EA_IMETA_VERSION
EA_IMETA_LOG_LEVEL

DATABASE_URL

SECRET_KEY

API_PREFIX
```

Additional variables will be introduced by later build phases.

---

# 20. ENVIRONMENT FILE

A development `.env` file may be used locally.

It must never be committed with secrets.

The repository should contain:

```text
.env.example
```

instead.

---

# 21. SECRET MANAGEMENT

Secrets shall be managed outside source code.

Initial principle:

```text
LOCAL DEVELOPMENT
→ .env / local secret store

TEST
→ test secret configuration

STAGING
→ managed secret store

PRODUCTION
→ enterprise secret management
```

---

# 22. CONFIGURATION OBJECT

Typed configuration should be exposed through one central settings object.

Conceptually:

```python
class Settings:
    app_name
    version
    environment
    database_url
    secret_key
    log_level
```

Business services should not read environment variables directly.

---

# 23. DATABASE FOUNDATION

The initial database platform is:

```text
PostgreSQL
```

The database connection shall be centralized.

No module should independently create database connections.

---

# 24. DATABASE SESSION

The database layer shall provide:

```text
engine
session factory
transaction handling
```

Conceptually:

```text
Application Service
        ↓
Repository
        ↓
Session
        ↓
PostgreSQL
```

---

# 25. TRANSACTION PRINCIPLE

Transactions shall be explicit.

A service operation should normally:

```text
BEGIN
 ↓
READ / WRITE
 ↓
VALIDATE
 ↓
COMMIT
```

or:

```text
ROLLBACK
```

on failure.

---

# 26. DATABASE CONNECTION POOL

Production database access should use connection pooling.

Pool settings shall be environment-specific.

The application shall avoid creating a new physical connection for every request.

---

# 27. DATABASE MIGRATIONS

Database schema changes shall use:

```text
Alembic
```

Never rely on manual production database changes.

---

# 28. MIGRATION PRINCIPLE

Every schema change shall be:

```text
VERSIONED
REVIEWED
TESTED
REPEATABLE
ROLLBACK-AWARE
```

---

# 29. INITIAL MIGRATION

BUILD-01 does not yet create the full EA-IMETA schema.

The initial migration may create only:

```text
schema metadata
migration tracking
optional system metadata
```

The main domain tables belong to BUILD-02.

---

# 30. DATABASE SCHEMA NAMESPACE

The preferred database schema is:

```text
ea_imeta
```

This avoids mixing EA-IMETA tables with unrelated application tables.

---

# 31. DOMAIN SEPARATION

Later domain areas may use logical modules such as:

```text
architecture
governance
workflow
integration
graph
analytics
ai
adaptive
```

The physical database design will be defined in later build phases.

---

# 32. LOGGING

Logging is mandatory.

The system shall log:

```text
APPLICATION START
APPLICATION STOP
REQUEST
ERROR
WARNING
SECURITY EVENT
DATABASE ERROR
INTEGRATION ERROR
IMPORTANT STATE CHANGE
```

---

# 33. LOG LEVELS

Use:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Production should normally use:

```text
INFO
```

unless troubleshooting requires otherwise.

---

# 34. STRUCTURED LOGGING

Where practical, logs should contain:

```text
timestamp
level
service
environment
request_id
user_id
operation
message
error
```

Sensitive values must not be logged.

---

# 35. REQUEST CORRELATION

Each API request should have a correlation identifier.

Example:

```text
X-Request-ID
```

This identifier should propagate through relevant services.

---

# 36. ERROR HANDLING

The application shall use controlled exception handling.

Do not expose raw stack traces to production users.

---

# 37. ERROR RESPONSE

A standard error response should contain:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "request_id": "..."
  }
}
```

Internal details remain in logs.

---

# 38. DOMAIN EXCEPTIONS

Domain-specific exceptions should be defined centrally.

Examples:

```text
ObjectNotFoundError
ValidationError
AuthorizationError
ConflictError
IntegrationError
ConfigurationError
```

---

# 39. ERROR CATEGORIES

Errors should be classified:

```text
VALIDATION
AUTHENTICATION
AUTHORIZATION
NOT_FOUND
CONFLICT
DATABASE
INTEGRATION
INTERNAL
```

---

# 40. SECURITY FOUNDATION

BUILD-01 establishes security boundaries but does not yet implement the full identity system.

Initial requirements:

```text
AUTHENTICATION
AUTHORIZATION
SECRET MANAGEMENT
AUDIT
INPUT VALIDATION
SECURE DEFAULTS
```

---

# 41. AUTHENTICATION

The production identity architecture shall support an enterprise identity provider.

Possible mechanisms:

```text
OIDC
OAuth 2.0
JWT
Enterprise SSO
```

The final provider is an architecture decision for the target deployment.

---

# 42. AUTHORIZATION

Authorization shall eventually be based on:

```text
USER
ROLE
ORGANIZATION
DOMAIN
OBJECT
ACTION
CLASSIFICATION
```

BUILD-01 establishes the extension point.

---

# 43. SECURE DEFAULTS

The application shall default to:

```text
NO DEBUG IN PRODUCTION
NO SECRET IN SOURCE
NO UNAUTHENTICATED WRITE
NO UNCONTROLLED CORS
NO VERBOSE ERROR DETAILS
```

---

# 44. CORS

CORS shall be explicitly configured.

Do not use:

```text
allow_origins=["*"]
```

in production unless there is a documented security justification.

---

# 45. INPUT VALIDATION

All API inputs shall be validated.

Validation should occur before business logic.

Pydantic models should define request and response contracts.

---

# 46. OUTPUT VALIDATION

API responses should use typed response models where appropriate.

This prevents accidental leakage of internal fields.

---

# 47. DEPENDENCY MANAGEMENT

All Python dependencies shall be declared in:

```text
pyproject.toml
```

Dependencies shall be version controlled.

---

# 48. DEPENDENCY POLICY

Before adding a dependency consider:

```text
MAINTENANCE
SECURITY
LICENSE
MATURITY
COMMUNITY
PERFORMANCE
NECESSITY
```

Avoid dependencies that duplicate standard functionality without clear benefit.

---

# 49. PYPROJECT

The project shall use modern Python packaging.

Conceptual sections:

```text
[build-system]
[project]
[project.dependencies]
[project.optional-dependencies]
```

Development dependencies should be separated where appropriate.

---

# 50. CODE QUALITY

The build shall establish:

```text
formatting
linting
type checking
tests
```

Recommended tools may include:

```text
Ruff
Pytest
MyPy
```

The exact toolchain may be adjusted later.

---

# 51. TEST STRUCTURE

Tests shall be separated:

```text
tests/
├── unit/
├── integration/
└── api/
```

---

# 52. UNIT TESTS

Unit tests validate isolated logic.

They should be:

```text
FAST
DETERMINISTIC
ISOLATED
```

---

# 53. INTEGRATION TESTS

Integration tests validate:

```text
DATABASE
SERVICES
REPOSITORIES
EXTERNAL BOUNDARIES
```

---

# 54. API TESTS

API tests validate:

```text
ENDPOINT
REQUEST
AUTHORIZATION
RESPONSE
ERROR HANDLING
```

---

# 55. TEST DATABASE

Tests should use a dedicated database or isolated test environment.

Production databases must never be used for automated tests.

---

# 56. TEST DATA

Test data should be synthetic.

Sensitive production data shall not be copied into development or test environments without approved controls.

---

# 57. CI FOUNDATION

The repository should establish continuous integration.

Initial CI sequence:

```text
CHECKOUT
 ↓
INSTALL
 ↓
LINT
 ↓
TYPE CHECK
 ↓
UNIT TEST
 ↓
INTEGRATION TEST
 ↓
BUILD
```

---

# 58. CI FAILURE RULE

A failed required quality gate should prevent a successful build artifact.

---

# 59. VERSION CONTROL

Git is the source-control system.

Recommended branches:

```text
main
develop
feature/*
fix/*
```

The exact branching strategy may be simplified for a small team.

---

# 60. COMMIT PRINCIPLES

Commits should be:

```text
SMALL
COHERENT
DESCRIPTIVE
BUILDABLE
```

Avoid giant commits containing unrelated changes.

---

# 61. RELEASE VERSIONING

Use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
0.1.0
0.2.0
1.0.0
```

The initial BUILD-01 implementation may remain:

```text
0.1.0
```

until the foundation is accepted.

---

# 62. DOCUMENTATION

The repository shall contain:

```text
README
ARCHITECTURE
DEVELOPMENT GUIDE
CONFIGURATION GUIDE
TESTING GUIDE
DEPLOYMENT GUIDE
API GUIDE
CHANGELOG
```

Later phases add domain-specific documentation.

---

# 63. README REQUIREMENTS

The README shall explain:

```text
WHAT EA-IMETA IS
HOW TO INSTALL
HOW TO RUN
HOW TO TEST
HOW TO CONFIGURE
HOW TO CONTRIBUTE
```

---

# 64. LOCAL DEVELOPMENT

A developer should be able to:

```text
CLONE
 ↓
CREATE ENVIRONMENT
 ↓
INSTALL
 ↓
CONFIGURE
 ↓
START DATABASE
 ↓
RUN MIGRATIONS
 ↓
START API
 ↓
RUN TESTS
```

---

# 65. LOCAL START COMMAND

The exact command shall be documented.

A typical FastAPI development command is:

```text
uvicorn ea_imeta.main:app --reload
```

The final project should preferably expose a simpler documented command.

---

# 66. DATABASE DEVELOPMENT

Local development may use:

```text
PostgreSQL
Docker PostgreSQL
```

Docker may be used for infrastructure convenience, but it shall not be mandatory if the target environment does not use Docker.

---

# 67. CONTAINERIZATION

Containerization should be supported where useful.

Initial architecture:

```text
EA-IMETA API
      ↓
PostgreSQL
```

Additional containers are introduced only when required.

---

# 68. DOCKER PRINCIPLE

Containers shall not hide architecture dependencies.

The project documentation must explain:

```text
PORTS
VOLUMES
ENVIRONMENT
NETWORK
DEPENDENCIES
```

---

# 69. DEPLOYMENT ENVIRONMENTS

The foundation should support:

```text
LOCAL
DEV
TEST
STAGING
PRODUCTION
```

---

# 70. DEPLOYMENT PRINCIPLE

Deployments shall be repeatable.

Avoid manual undocumented production configuration.

---

# 71. DATABASE BACKUP FOUNDATION

The system must define a backup strategy.

At minimum:

```text
BACKUP
RETENTION
RESTORE
TEST
```

A backup is not considered reliable until restore has been tested.

---

# 72. DISASTER RECOVERY FOUNDATION

The implementation shall document:

```text
RPO
RTO
BACKUP
RESTORE
RECOVERY PROCEDURE
```

Actual target values will be defined during deployment design.

---

# 73. OBSERVABILITY FOUNDATION

The system should prepare for:

```text
LOGGING
METRICS
TRACING
HEALTH
ALERTING
```

BUILD-01 establishes the interfaces; detailed observability belongs to later phases.

---

# 74. METRICS FOUNDATION

Initial application metrics:

```text
REQUEST COUNT
REQUEST LATENCY
ERROR COUNT
DATABASE HEALTH
```

---

# 75. AUDIT FOUNDATION

The platform shall eventually provide immutable audit records for material operations.

BUILD-01 establishes the audit service boundary.

Detailed audit entities are defined later.

---

# 76. SYSTEM IDENTIFIER

Each installation should have a unique system identity.

Example:

```text
EA-IMETA-INSTANCE-ID
```

This becomes useful for distributed environments and integration.

---

# 77. TIME HANDLING

The system shall use:

```text
UTC
```

internally for timestamps.

User interfaces may display local time.

---

# 78. IDENTIFIER STANDARD

The architecture should use stable identifiers.

The exact identifier strategy will be finalized in BUILD-02.

BUILD-01 must not create competing identifier schemes.

---

# 79. API CONTRACT PRINCIPLE

API contracts shall be:

```text
EXPLICIT
VERSIONED
VALIDATED
DOCUMENTED
```

FastAPI's OpenAPI output should be used as a starting point.

---

# 80. API DOCUMENTATION

Development API documentation should be available through the framework.

Production exposure of interactive API documentation shall be controlled by environment and security policy.

---

# 81. SERVICE FOUNDATION

Application services should be organized around business capabilities.

Examples for later phases:

```text
ArchitectureService
WorkflowService
IntegrationService
GraphService
AnalyticsService
AIService
AdaptiveService
```

BUILD-01 creates the service layer only.

---

# 82. REPOSITORY FOUNDATION

Repositories abstract data access.

Example:

```text
Repository
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Domain logic should not depend directly on database implementation details.

---

# 83. DOMAIN FOUNDATION

The domain layer will later contain:

```text
ENTITIES
VALUE OBJECTS
DOMAIN RULES
DOMAIN EVENTS
```

BUILD-01 keeps it intentionally minimal.

---

# 84. DEPENDENCY DIRECTION

Dependencies should flow inward:

```text
API
 ↓
APPLICATION
 ↓
DOMAIN
 ↑
INFRASTRUCTURE
```

Infrastructure should implement interfaces required by the application/domain rather than defining business rules.

---

# 85. NO CIRCULAR DEPENDENCIES

The build shall prevent circular module dependencies.

Examples to avoid:

```text
service A → service B
service B → service A
```

Use explicit orchestration or domain abstractions.

---

# 86. IMPORT DISCIPLINE

All imports should use the package namespace:

```text
ea_imeta....
```

Avoid fragile relative imports that depend on the current working directory.

---

# 87. ENTRYPOINT DISCIPLINE

The application shall be started from a defined project entry point.

Do not rely on:

```text
python random_file.py
```

from arbitrary directories.

---

# 88. PYTHON ENVIRONMENT

A dedicated virtual environment should be used.

Example:

```text
.venv
```

It shall not be committed to Git.

---

# 89. PYTHON VERSION

The project shall define a supported Python version range in project metadata.

The development and production environments should use the same major/minor version family.

---

# 90. FILE ENCODING

All source files shall use:

```text
UTF-8
```

---

# 91. LINE ENDINGS

The repository should standardize line endings through:

```text
.gitattributes
```

This avoids Windows/Linux line-ending conflicts.

---

# 92. GITIGNORE

The `.gitignore` shall exclude at minimum:

```text
.venv/
__pycache__/
*.pyc
.env
.pytest_cache/
.mypy_cache/
.ruff_cache/
dist/
build/
*.egg-info/
```

---

# 93. DEVELOPMENT SCRIPTING

Reusable development commands should be placed in:

```text
scripts/
```

Examples:

```text
run_dev
run_tests
run_migrations
reset_test_db
```

The exact implementation may use Python, PowerShell or platform-independent tooling.

---

# 94. WINDOWS SUPPORT

Because the initial development environment may be Windows-based, scripts shall avoid unnecessary Unix-only assumptions.

Where possible:

```text
Python scripts
```

should be preferred for cross-platform operations.

---

# 95. CONFIGURATION VALIDATION

The application shall fail clearly at startup when mandatory configuration is missing.

Example:

```text
DATABASE_URL missing
```

should produce a clear configuration error.

---

# 96. STARTUP VALIDATION

Application startup should validate:

```text
CONFIGURATION
DATABASE CONNECTION
REQUIRED SERVICES
VERSION
```

Only required checks should block startup.

---

# 97. SHUTDOWN

The application should support graceful shutdown.

It should:

```text
STOP ACCEPTING WORK
FINISH SAFE OPERATIONS
CLOSE DATABASE CONNECTIONS
FLUSH LOGS
EXIT
```

---

# 98. SECURITY EVENT FOUNDATION

Security-relevant events shall be identifiable.

Examples:

```text
LOGIN FAILURE
AUTHORIZATION FAILURE
SENSITIVE ACCESS
ADMINISTRATIVE CHANGE
SECURITY CONFIGURATION CHANGE
```

Detailed identity implementation is later.

---

# 99. AUDIT VS LOG

Logs and audit records are different.

```text
LOG
→ operational troubleshooting

AUDIT
→ accountable business/security history
```

Do not treat ordinary application logs as the sole audit trail.

---

# 100. ERROR RECOVERY

The foundation shall distinguish:

```text
RETRYABLE
NON-RETRYABLE
```

Transient infrastructure errors may be retried.

Validation and authorization errors normally should not.

---

# 101. RETRY SAFETY

Retries must not create duplicate business operations.

Later services shall use:

```text
IDEMPOTENCY
TRANSACTION BOUNDARIES
CORRELATION IDS
```

---

# 102. FEATURE FLAGS

The platform may use feature flags for controlled rollout.

Initial principle:

```text
FEATURE
→ FLAG
→ ENVIRONMENT
→ USER / ROLE
```

Feature flags shall be documented and retired when no longer needed.

---

# 103. BUILD ARTIFACT

A successful build should produce a versioned artifact.

Examples:

```text
Python package
Docker image
deployment package
```

The artifact shall be traceable to:

```text
Git commit
version
build timestamp
environment
```

---

# 104. BUILD METADATA

The application should expose version information.

Example:

```text
GET /api/v1/health
```

should include application version.

---

# 105. RELEASE CHECKLIST

Before a release:

```text
[ ] Tests pass
[ ] Lint passes
[ ] Type check passes
[ ] Dependencies reviewed
[ ] Configuration reviewed
[ ] Migration tested
[ ] Documentation updated
[ ] Version updated
[ ] Artifact created
[ ] Rollback understood
```

---

# 106. FOUNDATION ACCEPTANCE TEST

BUILD-01 shall demonstrate:

```text
[ ] Repository created
[ ] Python environment works
[ ] Dependencies install
[ ] Application starts
[ ] Health endpoint works
[ ] Readiness endpoint works
[ ] Configuration loads
[ ] Database connection works
[ ] Logging works
[ ] Error handling works
[ ] Tests run
[ ] CI runs
[ ] Migration framework works
[ ] API documentation works
[ ] Version is exposed
```

---

# 107. MINIMUM RUNNING SYSTEM

At the end of BUILD-01 the system should be capable of:

```text
START
 ↓
LOAD CONFIG
 ↓
CONNECT DATABASE
 ↓
START API
 ↓
REPORT HEALTH
 ↓
ACCEPT TEST REQUEST
 ↓
LOG REQUEST
 ↓
SHUT DOWN CLEANLY
```

This is the minimum technical foundation.

---

# 108. BUILD-01 DELIVERABLES

The build shall produce:

1. project repository
2. Python package
3. pyproject.toml
4. configuration system
5. environment template
6. application factory
7. FastAPI foundation
8. health endpoints
9. database connection layer
10. migration framework
11. logging foundation
12. error handling foundation
13. security foundation
14. test framework
15. CI pipeline
16. development documentation
17. deployment foundation
18. backup/recovery foundation
19. release checklist
20. BUILD-01 acceptance report

---

# 109. BUILD-01 ACCEPTANCE CRITERIA

BUILD-01 is accepted when:

```text
[ ] Project structure exists
[ ] Source package imports cleanly
[ ] Application starts from defined entry point
[ ] Configuration is externalized
[ ] PostgreSQL connection is functional
[ ] Alembic is functional
[ ] Health endpoint is functional
[ ] Logging is functional
[ ] Standard error response is functional
[ ] Basic security boundary exists
[ ] Tests execute successfully
[ ] CI executes successfully
[ ] API documentation is generated
[ ] Local development procedure is documented
[ ] Deployment procedure is documented
[ ] Git repository is clean and reproducible
```

---

# 110. NEXT BUILD PHASE

After BUILD-01 acceptance, the next document is:

## EA-IMETA-BUILD-02
### REPOSITORY & DATABASE

BUILD-02 will implement:

- EA-IMETA database schema
- architecture objects
- identifiers
- relationships
- lifecycle
- classifications
- ownership
- evidence
- metadata
- repository services
- repository APIs
- migrations
- repository tests

---

# 111. CRITICAL BUILD RULE

Do not implement the entire EA-IMETA system inside `main.py`.

Use the defined layers:

```text
API
 ↓
APPLICATION
 ↓
DOMAIN
 ↓
REPOSITORY
 ↓
DATABASE
```

---

# 112. CRITICAL PROJECT RULE

The physical implementation shall remain aligned with:

```text
EA-IMETA-MASTER-01
```

and:

```text
EA-IMETA-IMPLEMENTATION-01
EA-IMETA-IMPLEMENTATION-02
EA-IMETA-IMPLEMENTATION-03
EA-IMETA-IMPLEMENTATION-04
EA-IMETA-IMPLEMENTATION-05
EA-IMETA-IMPLEMENTATION-06
EA-IMETA-IMPLEMENTATION-07
EA-IMETA-IMPLEMENTATION-08
```

Any material deviation shall become an architecture change.

---

# 113. BUILD TRACEABILITY

Every major build component shall be traceable to:

```text
MASTER ARCHITECTURE
        ↓
IMPLEMENTATION REQUIREMENT
        ↓
BUILD COMPONENT
        ↓
TEST
        ↓
ACCEPTANCE
```

---

# 114. TECHNICAL DEBT RULE

Technical debt shall be recorded rather than hidden.

Each technical debt item should include:

```text
ID
DESCRIPTION
IMPACT
RISK
OWNER
PRIORITY
TARGET RESOLUTION
STATUS
```

---

# 115. NO PREMATURE COMPLEXITY

BUILD-01 shall not introduce:

```text
microservices
event buses
Kubernetes
multiple databases
AI orchestration
complex distributed caching
```

unless a later architecture phase requires them.

Start with a modular monolith.

---

# 116. MODULAR MONOLITH

The recommended initial physical architecture is:

```text
             EA-IMETA
                 |
      +----------+----------+
      |          |          |
     API      SERVICES    DOMAIN
      |          |          |
      +----------+----------+
                 |
             DATABASE
```

This provides strong module boundaries without unnecessary distributed-system complexity.

---

# 117. FUTURE DISTRIBUTION

Later components may become separate services if justified:

```text
Integration Service
Graph Service
AI Service
Adaptive Service
```

The decision shall be evidence-based.

---

# 118. BUILD PHILOSOPHY

The physical build should follow:

```text
SIMPLE
 ↓
MODULAR
 ↓
TESTABLE
 ↓
OBSERVABLE
 ↓
SECURE
 ↓
SCALABLE
```

not:

```text
COMPLEX
 ↓
DISTRIBUTED
 ↓
DIFFICULT TO OPERATE
```

---

# 119. FINAL BUILD-01 PRINCIPLES

1. Establish a clean technical foundation.
2. Keep the first implementation modular.
3. Separate API, application, domain and infrastructure concerns.
4. Externalize configuration.
5. Never commit secrets.
6. Centralize database access.
7. Version database migrations.
8. Establish structured logging.
9. Establish controlled errors.
10. Establish security boundaries early.
11. Test from the beginning.
12. Automate quality checks.
13. Make local setup reproducible.
14. Support Windows development without sacrificing portability.
15. Avoid premature distributed complexity.
16. Keep every build component traceable to the architecture.
17. Make the foundation stable before implementing the EA-IMETA domain.

---

# 120. BUILD-01 COMPLETION STATEMENT

EA-IMETA-BUILD-01 establishes the technical foundation from which the actual EA-IMETA platform will be constructed.

The project now moves from:

```text
ARCHITECTURE SPECIFICATION
```

to:

```text
PHYSICAL SYSTEM FOUNDATION
```

The next step is not to add every feature at once.

The next step is to build the authoritative repository and database correctly.

Therefore:

> BUILD THE FOUNDATION ONCE, BUILD THE CAPABILITIES ON TOP OF IT.

---

# END OF EA-IMETA-BUILD-01
## SYSTEM FOUNDATION
## COMPLETE

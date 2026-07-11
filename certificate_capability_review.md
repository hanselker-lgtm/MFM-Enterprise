# Certificate Capability Review (CERT-007)

## Purpose
Review CAP-10 Certificates and Compliance implementation (CERT-001..CERT-006) for design conformance, boundary integrity, transaction safety, API safety, and lock readiness.

## Review Scope
Reviewed layers:
- Domain: src/mfm/domain/certificates/*
- Persistence models + mapper: src/mfm/database/models/certificate_model.py, src/mfm/database/models/certificate_compliance_observation_model.py, src/mfm/database/mappers/certificate_mapper.py
- Repository contract + SQLite implementation: src/mfm/repositories/certificate_repository.py, src/mfm/infrastructure/persistence/sqlite/sqlite_certificate_repository.py
- Application services: src/mfm/application/certificates/*
- Feature API: src/mfm/application/features/certificates/*
- E2E workflows: tests/application/features/certificates/test_certificate_feature_e2e_workflows.py
- Supporting tests: tests/domain/certificates/test_certificate_domain.py, tests/database/test_certificate_mapper.py, tests/database/test_sqlite_certificate_repository.py, tests/application/certificates/test_certificate_use_cases.py, tests/application/features/certificates/test_certificate_features.py
- Architecture standards and guards: docs/design/certificates_compliance.md, docs/architecture/public_api_standard.md, tests/architecture/test_dependency_guard.py, tests/architecture/test_feature_api_architecture.py
- Repo memory: /memories/repo/notes.md

## Reviewed Commits
- CERT-001: faaf57a
- CERT-002: 26fcdeb
- CERT-003: 6dbe85b
- CERT-004: 2f7b535
- CERT-005: 32990d3
- CERT-006: 71dc1b5

Commit-scope inspection for the above commits shows only certificate capability files and certificate-focused tests changed.

## Design Conformance
Result: PASS (with one MINOR architecture-guard gap).

Conformance verified for:
- bounded context and capability responsibility
- aggregate boundary centered on Certificate
- CertificateTarget approved types (VESSEL, ORGANIZATION)
- controlled CertificateTypeReference model
- chronology and validity rules in domain
- explicit-date status evaluation path
- lifecycle transitions owned by domain methods
- renewal modeled as new aggregate B linked to A via renewed_from_certificate_id
- issuer snapshot persistence and history exposure
- document reference as metadata only
- feature execute(request) standard and immutable DTOs
- E2E workflows proving real SQLite roundtrips

## Aggregate Boundary Review
Result: PASS.

Evidence:
- Lifecycle and invariants in domain aggregate: src/mfm/domain/certificates/certificate.py
- Renewal rules in domain aggregate method renew(...): src/mfm/domain/certificates/certificate.py
- Chronology enforced in domain constructor and helpers: src/mfm/domain/certificates/certificate.py
- Feature and application layers delegate/orchestrate only.

No external behavior ownership leakage found for lifecycle or renewal rules.

## CertificateTarget Review
Result: PASS.

Evidence:
- Immutable value object with UUID normalization/validation: src/mfm/domain/certificates/certificate_target.py
- Supported values enforced through enum parsing path from application requests.
- No vessel/organization aggregate ownership in CERT code.
- Identity/reference-only use confirmed through repository/application/feature/E2E layers.

## CertificateType Review
Result: PASS.

Evidence:
- Controlled type model: CertificateTypeReference + CertificateTypeId
- Mapper roundtrip reconstructs type consistently: src/mfm/database/mappers/certificate_mapper.py
- Feature/application map to safe DTO representations.
- No legislation hardcoding found in cert domain core.

## Issuer Historical Snapshot Review
Result: PASS.

Evidence across layers:
- Domain model stores issuer_name_snapshot in IssuerReference: src/mfm/domain/certificates/issuer_reference.py
- Mapper persists and reloads issuer snapshot: src/mfm/database/mappers/certificate_mapper.py
- History response exposes both A and B snapshots independently through feature/application DTOs.
- E2E workflow proves A snapshot stays Maritime Authority A and B snapshot stays Maritime Authority B after new-session database roundtrip: tests/application/features/certificates/test_certificate_feature_e2e_workflows.py

No normalization from shared issuer identity observed.

## Validity Model Review
Result: PASS.

Evidence:
- Chronology checks in domain: issued_date <= valid_from <= expires_at when expiry exists.
- Non-expiring certificates supported (expires_at None).
- Boundary-date semantics covered in tests and E2E workflows.
- Mapper preserves persisted dates as-is.

## Expiry and Status Review
Result: PASS.

Evidence:
- Explicit as_of_date flows Feature -> Application -> Domain.
- EXPIRING is derived and not persisted as lifecycle mutation.
- EXPIRED transition is domain-owned and persisted when evaluate_status crosses expiry.
- Repository expiring/expired queries are read-side and do not mutate state.

## Renewal Review
Result: PASS.

Evidence:
- Flow verified end-to-end via public APIs and real persistence boundary with new session.
- Context proof (not IDs only) for A, B, and supported chain A->B->C captured in E2E assertions.
- renewed_from relation correctly set on B/C and A remains unchanged.

## Historical Certificate Truth Review
Result: PASS.

Evidence:
- A and B remain separate records with independent snapshots and notes.
- New-session history retrieval verifies preserved context fields.
- Repository roundtrip verifies separate aggregate records and relations.

## Lifecycle Review
Result: PASS.

Evidence:
- Valid activation, suspension, revocation transitions.
- Invalid transitions rejected by domain exceptions and mapped at app/feature boundaries.
- No direct lifecycle state ownership outside domain methods.

## Inspection and Compliance Review
Result: PASS.

Evidence:
- Compliance finding (requires_maintenance_work) represented as certificate-owned data.
- No maintenance command/workflow ownership in certificate capability.

## Maintenance Boundary Review
Result: PASS.

Evidence:
- No maintenance repository/application/feature dependencies in src/mfm/**/certificates/**/*.py
- CERT-001..CERT-006 commit scopes show no maintenance capability file changes.
- E2E compliance workflow verifies no maintenance table side effects.

## Fleet Boundary Review
Result: PASS.

Evidence:
- VESSEL target is UUID reference only.
- No fleet repository/application/feature imports in cert capability code.
- CERT commit scopes contain no Fleet capability file changes.

## Organization Boundary Review
Result: PASS.

Evidence:
- ORGANIZATION target handled as identity/reference only.
- No organization repository/application/feature imports in cert capability code.
- Issuer snapshot is certificate-owned historical state, not reconstructed from organization data.

## Technical Configuration Boundary Review
Result: PASS.

Evidence:
- No TECHNICAL_COMPONENT target introduced in v1.
- No technical-configuration dependencies in cert capability code.
- No technical configuration file changes in CERT-001..CERT-006 scopes.

## Document Reference Review
Result: PASS.

Evidence:
- document_reference/external_document_id treated as metadata fields only.
- Preserved through mapper/repository/history roundtrip.
- No binary/blob/filesystem/document-management subsystem introduced.

## Domain Event Review
Result: PASS.

Evidence:
- Meaningful events implemented: CertificateCreated/Activated/Expired/Suspended/Revoked/Renewed.
- Events emitted from domain operations.
- Mapper restoration calls pull_events() to avoid false historical event emission on reload: src/mfm/database/mappers/certificate_mapper.py

## Persistence and Mapper Review
Result: PASS.

Evidence:
- Mapper cleanly maps domain<->ORM including compliance observation ordering and renewal relation.
- Reload path reconstructs domain objects and clears restoration events.
- No mapper-level business rule ownership detected.

## Repository Review
Result: PASS.

Evidence:
- Contract placement: src/mfm/repositories/certificate_repository.py
- SQLite implementation uses mapper and session from UnitOfWork wrapper.
- No repository commit ownership.
- Returns domain certificates.
- Query semantics for get_by_id/exists/list/get_by_target/get_active_by_target/get_expiring/get_expired/get_renewal_history validated by tests.

## Transaction Integrity Review
Result: PASS.

Evidence:
- State-changing use cases commit on success inside application UoW orchestration.
- E2E rollback proof includes transaction-stage failure (simulated commit failure) and verifies no partial B persisted, A unchanged.
- Domain-invalid renewal path also covered.

## Application Review
Result: PASS.

Evidence:
- Application services use repository contract via AbstractUnitOfWork.
- No SQLAlchemy/persistence model imports.
- Domain lifecycle/evaluation/renewal behavior invoked in domain methods.
- DTO responses are immutable and API-safe.

## Feature API Review
Result: PASS.

Evidence:
- execute(request) standard across all certificate features.
- Immutable request/response DTOs.
- Feature delegates to application services, no direct repository/UoW ownership.
- Exception mapping follows project pattern.

## Public API Leakage Review
Result: PASS.

Evidence:
- Response DTOs expose primitive/public-safe values and nested DTOs only.
- No aggregate/value-object/persistence model leakage in feature responses (including history collections).
- Architecture feature-api guard passes.

## End-to-End Review
Result: PASS.

Evidence:
- CERT-006 tests use real stack: Feature -> Application -> Domain -> Repository -> Mapper -> SQLAlchemy -> SQLite.
- No repository or mapper mocks in primary workflows.
- Renewal historical truth and issuer snapshots asserted across new-session boundaries.
- Explicit-date status evaluation and rollback/capability-boundary workflows covered.

## Architecture Compliance Review
Result: PASS with one MINOR finding.

Evidence:
- Permanent architecture tests pass.
- Existing guards enforce domain/application/feature dependency rules and feature DTO safety.
- Guard gap identified: no permanent architecture test explicitly forbids hidden clock patterns in certificate runtime code.

## Locked Capability Protection
Result: PASS.

Evidence from commit scopes CERT-001..CERT-006:
- No production/test changes in locked capabilities: Asset Core, Fleet, Technical Configuration, Maintenance.

## Test Results
Focused CERT tests:
- python -m pytest -q tests/domain/certificates/test_certificate_domain.py tests/database/test_certificate_mapper.py tests/database/test_sqlite_certificate_repository.py tests/application/certificates/test_certificate_use_cases.py tests/application/features/certificates/test_certificate_features.py tests/application/features/certificates/test_certificate_feature_e2e_workflows.py
- Result: 87 passed in 8.85s

Architecture compliance tests:
- python -m pytest -q tests/architecture/test_dependency_guard.py tests/architecture/test_feature_api_architecture.py
- Result: 10 passed in 1.63s

Full suite:
- python -m pytest -q
- Result: 820 passed in 33.20s

Warnings observed: 0

## Findings
### C007-MIN-001
- Severity: MINOR
- Area: Architecture Compliance
- File/location: tests/architecture/test_dependency_guard.py; tests/architecture/test_feature_api_architecture.py
- Current behaviour: Permanent architecture guards do not explicitly enforce absence of hidden clock patterns (date.today, datetime.now, datetime.today, time.time) in certificate runtime modules.
- Expected behaviour: Permanent architecture guard should fail if hidden clock usage appears in certificate domain/application/feature runtime code.
- Impact: Regression risk; hidden-clock behavior could be introduced later without architecture-gate detection.
- Smallest recommended correction: Add a permanent architecture test that scans src/mfm/**/certificates/**/*.py for hidden clock calls.
- Required regression proof: Introduce a temporary hidden-clock call in certificate runtime code and confirm architecture test fails, then remove and confirm pass.

## Risks
1. Without an explicit permanent hidden-clock architecture guard, future changes could introduce time-coupled behavior despite current compliance.

## Lock Recommendation
READY FOR LOCK

Justification:
- No BLOCKER findings.
- No MAJOR findings.
- Historical certificate truth and issuer snapshot history are proven through new-session persistence roundtrips.
- Renewal/lifecycle ownership remains in domain.
- No hidden clock usage found in current certificate runtime code.
- Transaction integrity acceptable and proven by rollback workflow.
- Maintenance/Fleet/Organization/Technical boundaries intact.
- Locked capabilities unchanged.
- Public API leakage not detected.
- Architecture compliance and full suite pass with 0 failures and 0 warnings.

# RELEASE-002 Baseline Verification

Date: 2026-07-17
Scope: Post CAP-16 Accounting baseline verification
Status: PASS

## Repository Status

The repository is structurally consistent for the accounting baseline after CAP-16 lock.

Verified lock-state sources:
- `docs/architecture/capability_roadmap.md`
- `docs/architecture/capabilities/CAP-16-Accounting.md`
- `docs/design/projects-lock.md`
- `docs/architecture/capabilities/CAP-15-Document-Management.md`

## Locked Capabilities

Confirmed LOCKED capabilities in the authoritative roadmap:
- CAP-07 Fleet
- CAP-08 Technical Configuration
- CAP-09 Maintenance
- CAP-10 Certificates and Compliance
- CAP-11 Voyages
- CAP-14 Projects
- CAP-15 Document Management
- CAP-16 Accounting

## Test Status

Accounting capability tests: PASS
- `python -m pytest -q tests/application/features/accounting`
- Result: 10 passed

Full regression suite: PASS
- `python -m pytest -q`
- Result: 1171 passed

## Ruff Status

Repository-wide Ruff: PASS
- `python -m ruff check .`
- Result: All checks passed

## Dependency Verification

- No cyclic capability dependencies were detected in the repository architecture checks.
- CAP-14, CAP-15, and CAP-16 are marked LOCKED in the roadmap.
- Public Feature APIs remain the only cross-capability entry points for the locked CAP-16 surface.
- ACC commit history verified present for ACC-001 through ACC-007.
- Discovery milestones (XXX-000) are documentation milestones and are excluded from Git-history verification.

## Architecture Verification

- Domain -> Application -> Infrastructure direction remains intact.
- No architecture-layer violations were discovered in the accounting scope.
- CAP-16 accounting feature and end-to-end workflows remain feature-layer only and do not expose ORM models or persistence internals.
- Accounting invariants remain enforced through the application/domain boundary.

## Outstanding Risks

- None.

## Baseline Conclusion

The accounting capability is locked and the repository-wide quality gates are green.

Discovery milestones (XXX-000) are documentation milestones and are excluded from Git-history verification.

RELEASE-002 baseline verification passes.

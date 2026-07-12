# Changelog

## v0.10.0-alpha - 2026-07-12

Voyages capability lock release.

### Changed
- Voyages capability status formalized as `CAP-11 Voyages: LOCKED` in design documentation.
- CAP-11 lock constraints documented for capability boundaries (vessel identity/reference only, planned and actual context independence, historical voyage truth, no Fleet/Maintenance/Certificate/Technical Configuration ownership).

### Quality
- Voyages lock verification completed against focused VOY tests, permanent architecture compliance tests, and full regression suite.
- Test suite status at lock: 907 passed, 0 failures, 0 warnings.

## v0.9.0-alpha - 2026-07-11

Certificates and Compliance capability lock release.

### Changed
- Certificates and Compliance capability status formalized as `CAP-10 Certificates and Compliance: LOCKED` in design documentation.
- CAP-10 lock constraints documented for capability boundaries (Maintenance workflow ownership, Fleet/Organization identity-only references, no Technical Configuration target expansion without a new capability plan).

### Quality
- Certificates and Compliance lock verification completed against focused CERT tests, permanent architecture compliance tests, and full regression suite.
- Test suite status at lock: 820 passed, 0 failures, 0 warnings.

## v0.8.0-alpha - 2026-07-11

Maintenance capability lock release.

### Changed
- Maintenance capability status formalized as `CAP-09 Maintenance: LOCKED` in design documentation.
- Maintenance lock constraints documented for capability scope boundaries (Technical Configuration ownership, Certificates, Voyages outside CAP-09).

### Quality
- Maintenance lock verification completed against full regression suite and permanent architecture compliance tests.
- Test suite status at lock: 733 passed, 0 failures, 0 warnings.

## v0.7.0-alpha - 2026-07-11

Technical Configuration capability lock release.

### Changed
- Technical Configuration capability status formalized as `CAP-08 Technical Configuration: LOCKED` in design documentation.
- Technical Configuration lock constraints documented for capability scope boundaries (Maintenance, Certificates, Voyages excluded from CAP-08).

### Quality
- Technical Configuration lock verification completed against full regression suite and permanent architecture compliance tests.
- Test suite status at lock: 651 passed, 0 failures, 0 warnings.

## v0.6.0-alpha - 2026-07-11

Fleet capability lock release.

### Changed
- Fleet capability status formalized as `CAP-07 Fleet: LOCKED` in design documentation.
- Fleet lock constraints documented for capability scope boundaries (Engine, Maintenance, Certificates, Voyages excluded from Fleet Core).

### Quality
- Fleet lock verification completed against full regression suite and permanent architecture compliance tests.
- Test suite status at lock: 570 passed, 0 failures, 0 warnings.

## v0.5.0-alpha - 2026-07-10

Contact module freeze release.

### Added
- Application use cases for contacts: create, update, delete, get, search, and list.
- Full test coverage for contact application workflows, including query and delete cascade scenarios.

### Changed
- Contact repository interface finalized for add, update, get, get_by_number, list, search, exists, and delete operations.
- Contact module exports aligned in the application contact package.

### Fixed
- Removed documented dead code in contact phone value object.
- Removed documented unused imports in contact database model.
- Preserved not-found exception compatibility in update contact flow.

### Quality
- Release review completed for contact domain, application, mapper, model, and repository layers.
- Test suite status at release: 64 passed, 0 failures, 0 warnings.

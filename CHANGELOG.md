# Changelog

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

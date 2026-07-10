# Changelog

## v0.6.0-alpha - 2026-07-10

Asset capability freeze release.

### Added
- Asset core domain model with immutable value objects and lifecycle operations.
- Asset persistence models, mapper, and SQLite repository implementation.
- Asset application use cases and feature layer facades.
- End-to-end integration workflows for create, transfer ownership, relocate, retire, and dispose.
- Asset capability review report: READY FOR LOCK.

### Quality
- Architecture gates green (dependency guard and feature API compliance).
- Test suite status at review: 513 passed, 0 failures, 0 warnings.

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

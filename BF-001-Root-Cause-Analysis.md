# BF-001 Root Cause Analysis

Date: 2026-07-17
Issue: Startup crash from end-user entrypoint (`python -m mfm`).

## Symptom

- Command `python -m mfm` failed before completing startup.
- Traceback terminated in `src/mfm/application/app.py` with:
  - `NameError: name 'ConfigManager' is not defined`

## Root Cause

`src/mfm/application/app.py` referenced startup symbols that were not imported or defined in the module:

- `ConfigManager`
- `ApplicationContext`
- `LoggingManager`
- `DatabaseService`
- `ServiceRegistry`

The first unresolved symbol (`ConfigManager`) triggered an immediate `NameError` and prevented application startup.

## Scope

- Impacted path: runtime entrypoint (`src/mfm/__main__.py` -> `src/mfm/main.py` -> `src/mfm/application/app.py`).
- Impact level: Critical (application not launchable from documented command).

## Fix Applied

Targeted, startup-only correction in `src/mfm/application/app.py`:

1. Imported existing canonical classes:
   - `ConfigManager` from `mfm.config.manager`
   - `ApplicationContext` from `mfm.application_context`
   - `LoggingManager` from `mfm.common.logging`
2. Removed references to undefined startup symbols (`DatabaseService`, `ServiceRegistry`) that do not exist in the current codebase.
3. Kept startup behavior minimal and unchanged in intent:
   - load config
   - create application context
   - initialize logging
   - log startup completion

No new functionality was added.
No unrelated refactor was performed.

## Verification

- `python -m mfm`: PASS (startup completes, logs emitted)
- `python -m pytest -q`: PASS (1290 passed)
- `python -m ruff check .`: PASS (All checks passed)
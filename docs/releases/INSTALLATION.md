# Installation Procedure

## Purpose

Define a repeatable installation baseline for MFM Enterprise release candidates.

## Supported Baseline

Current validated baseline:
- OS: Windows
- Python: 3.13+
- Database: SQLite (default)

## Prerequisites

1. Python 3.13 or newer is installed and available in PATH.
2. Write permissions to installation target and data/log directories.
3. Required runtime dependencies can be installed from package metadata.

## Install Steps (Source Distribution Baseline)

1. Obtain release candidate source.
2. Create and activate virtual environment.
3. Install dependencies and package.
4. Verify config files.
5. Start application.

Example command flow:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python -m mfm
```

## Configuration Setup

Required configuration baseline:
- config/default.toml must exist and be valid.
- config/user.toml is optional and overrides defaults.

Operator should verify:
- application name/version
- database provider/path
- logging level/directory/filename
- GUI style

## Database Initialization

Development baseline:
- Development table creation may be performed by runtime initialization.

Production-like baseline:
- Use controlled migration process (see docs/releases/UPGRADE.md).

## Post-Install Verification

1. Application process starts successfully.
2. Main shell opens and navigation is available.
3. Log file is created under configured logging directory.
4. Basic database health check succeeds.

## Troubleshooting

Common checks:
- Python version mismatch.
- Missing dependencies.
- Invalid TOML configuration.
- Missing write permissions for database/log paths.

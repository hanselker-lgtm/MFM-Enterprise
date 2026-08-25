# Building a desktop installer

MFM Enterprise can be packaged as a standalone desktop application
using [PyInstaller](https://pyinstaller.org/), so end users don't
need Python installed at all.

## Windows

Requires a Windows PC (PyInstaller builds for the OS it runs on —
you cannot produce a Windows `.exe` from Linux or macOS).

1. Copy this whole project checkout to the Windows machine.
2. Open a Command Prompt in the project's root folder.
3. Run:
   ```
   packaging\build_windows.bat
   ```
4. The finished app is in `dist\MFM Enterprise\`. Copy that entire
   folder when distributing — `MFM Enterprise.exe` needs everything
   alongside it in `_internal`. Users double-click
   `MFM Enterprise.exe` to run it.

## macOS / Linux

Same idea, run on that OS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install PySide6 SQLAlchemy alembic pyinstaller
pyinstaller packaging/mfm.spec --noconfirm
```

## Where the app stores its data

Once packaged, the app no longer reads or writes anything next to
the executable (that location may be read-only, e.g. under
`Program Files`). Instead it uses:

- **Windows**: `%APPDATA%\MFM Enterprise\`
- **macOS**: `~/Library/Application Support/MFM Enterprise/`
- **Linux**: `~/.local/share/mfm-enterprise/`

The database, logs, and any local config overrides (`user.toml`)
live there, and persist across app updates. This is created and
migrated automatically on first launch.

## Making a proper installer (optional next step)

The PyInstaller build is a ready-to-run folder, not yet a
double-click installer with Start Menu shortcuts, an uninstaller,
etc. For that, wrap the `dist\MFM Enterprise\` output with:

- Windows: [Inno Setup](https://jrsoftware.org/isinfo.php) (free) or
  [WiX Toolset](https://wixtoolset.org/)
- macOS: a `.dmg` via `hdiutil` or
  [create-dmg](https://github.com/create-dmg/create-dmg)

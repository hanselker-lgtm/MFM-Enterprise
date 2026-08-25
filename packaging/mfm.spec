# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for MFM Enterprise.

Build with (from the project root):

    pyinstaller packaging/mfm.spec --noconfirm

Produces a --onedir bundle under dist/MFM Enterprise/. --onedir (not
--onefile) is used deliberately: --onefile re-extracts the whole
bundle to a temp directory on every launch, which is slow and, for a
Qt app with many files, more fragile. --onedir starts faster and is
just as easy to distribute as a zipped folder or an installer.
"""

import sys
from pathlib import Path

block_cipher = None

PROJECT_ROOT = Path(SPECPATH).resolve().parent

datas = [
    (str(PROJECT_ROOT / "config" / "default.toml"), "config"),
    (str(PROJECT_ROOT / "alembic.ini"), "."),
]

# Bundle the whole migrations/ tree (env.py, script.py.mako, versions/*.py)
for path in (PROJECT_ROOT / "migrations").rglob("*.py"):
    rel = path.relative_to(PROJECT_ROOT)
    datas.append((str(path), str(rel.parent)))

a = Analysis(
    [str(PROJECT_ROOT / "packaging" / "run_mfm.py")],
    pathex=[str(PROJECT_ROOT / "src")],
    binaries=[],
    datas=datas,
    hiddenimports=[
        "mfm.database.metadata",
        "alembic",
        "alembic.runtime.migration",
        "logging.config",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="MFM Enterprise",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="MFM Enterprise",
)

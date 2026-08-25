@echo off
REM Build MFM Enterprise as a Windows desktop application.
REM
REM Run this from a Windows PC with Python 3.12+ installed, from the
REM root of the project checkout (the folder containing this
REM "packaging" folder).
REM
REM Result: dist\MFM Enterprise\MFM Enterprise.exe
REM         (copy the entire "MFM Enterprise" folder when distributing --
REM          it needs everything inside _internal alongside the .exe)

setlocal

echo === Creating virtual environment ===
python -m venv .venv
call .venv\Scripts\activate.bat

echo === Installing dependencies ===
python -m pip install --upgrade pip
pip install PySide6 SQLAlchemy alembic pyinstaller

echo === Building with PyInstaller ===
pyinstaller packaging\mfm.spec --noconfirm

echo.
echo === Done ===
echo The application is in: dist\MFM Enterprise\
echo Run it by double-clicking: dist\MFM Enterprise\MFM Enterprise.exe

endlocal

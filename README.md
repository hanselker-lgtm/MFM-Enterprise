# MFM Enterprise

Maritim Forenings Manager Enterprise (MFM) er et integreret administrations- og dokumentationssystem udviklet til maritime kulturhistoriske foreninger. Systemet understøtter hele foreningens arbejde – fra kontaktregister og medlemsadministration til økonomi, fartøjsbevaring, restaureringsprojekter, fondsadministration og dokumentarkiv. MFM udvikles første gang til fiskeskibet Álvur SA 98, men er designet, så det kan anvendes af andre maritime kulturhistoriske foreninger i Danmark, Færøerne, Grønland og resten af Norden.

## Status

MFM Enterprise er en desktop-applikation (Python / PySide6/Qt), der kører mod en lokal SQLite-database via Alembic-migrationer. Følgende arbejdsflader er koblet til rigtige data og fuldt funktionelle:

- **Projekter** – oprettelse, søgning, status og budget-vs-faktisk-rapportering
- **Bogføring** – posteringer, regnskabsår, projekt-bogføring
- **Dokumenter** – dokumentarkiv med versionering
- **Medlemskaber** – medlemsregistrering og medlemskabstyper
- **Kontingentopkrævning** – gebyrplaner og automatisk årlig fakturering med journalposteringer
- **Organisationer** – stamdata for foreningen

Følgende områder er endnu kun stub-sider i brugerfladen: Organisationsroller, Kontaktkommunikation, Events/Aktiviteter, Dokumentarkiv (separat modul), Indstillinger og Logs.

## Kom i gang (udvikling)

Kræver Python 3.12+.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install PySide6 SQLAlchemy alembic pytest pytest-qt

# Opsæt databasen (kører automatisk migrationer ved første start,
# men kan også køres manuelt):
python -m alembic upgrade head

# Start programmet:
PYTHONPATH=src python -m mfm
```

## Tests

```bash
python -m pytest -q
```

## Databasemigrationer

Skemaet styres af Alembic. Ny migration efter en modelændring:

```bash
python -m alembic revision --autogenerate -m "beskrivelse af ændringen"
python -m alembic upgrade head
```

## Installerbar desktop-app

Se [packaging/README.md](packaging/README.md) for at bygge en færdig .exe (Windows) eller app (macOS/Linux) med PyInstaller — ingen Python-installation krævet for slutbrugeren.

## Licens

MIT – se [LICENSE](LICENSE).

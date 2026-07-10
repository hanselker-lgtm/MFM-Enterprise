# ORG-000 Domain Design: Organization

## Purpose
Formalet med Organization-domænet er at modellere medlemsdrevet foreningsdrift med konsistente forretningsregler på tværs af kontaktdata, medlemskab, kontingentopkrævning, debitorstyring og finansiel bogføring.

Domænet skal:
- sikre entydig identitet for contacts, members og membership types
- understøtte livscyklus for medlem og medlemskab
- generere kontingentgrundlag, fakturaer og finansielle posteringer
- eksponere stabile application entry points (Features) med transport-sikre API-kontrakter

## Bounded Context
Løsningen er organiseret i følgende bounded contexts under domain-laget:

- Contact Context
  - ansvar: identitet, kontaktoplysninger og partityper (person/organisation)
  - centrale objekter: Contact, Person, Organisation, Address, Email, Phone

- Member Context
  - ansvar: medlemsidentitet og medlemsstatus
  - centrale objekter: Member, MemberStatus

- Membership Context
  - ansvar: medlemskabstype, medlemskabsrelation og status
  - centrale objekter: MembershipType, Membership, MembershipStatus

- Contingent Context
  - ansvar: kontingentplaner, gyldighedsperioder og faktureringsregler
  - centrale objekter: ContingentPlan, InvoiceRule, BillingPeriod

- Finance Context
  - ansvar: faktura, betaling, open items og aging
  - centrale objekter: Invoice, InvoiceLine, Payment, Receivable, AccountsReceivable, AgingBucket

- Accounting Context
  - ansvar: finanskontoplan, journaler og periodisering
  - centrale objekter: LedgerAccount, JournalEntry, JournalLine, FiscalYear, FiscalPeriod

Bemærkning:
Domænet indeholder desuden tomme/pladsholder-kontekster (document, fund, project, vessel), som ikke indgår i aktiv forretningsflow på nuværende tidspunkt.

## Aggregates
Følgende aggregates behandles som primære konsistensgrænser:

- Contact aggregate
  - root: Contact
  - invariants: gyldig partitype og kontaktidentitet

- Member aggregate
  - root: Member
  - invariants: unikt member_number, gyldig statusovergang

- MembershipType aggregate
  - root: MembershipType
  - invariants: unik code, gyldig type-definition

- ContingentPlan aggregate
  - root: ContingentPlan
  - invariants: gyldigt beløb, gyldighedsinterval, faktureringsregel

- Invoice aggregate
  - root: Invoice
  - invariants: mindst én linje, konsistent total, gyldig status og referencespor

- JournalEntry aggregate
  - root: JournalEntry
  - invariants: balancerede debit/credit-linjer, gyldig status og posting_date

## Value Objects
Værdityper bruges til at udtrykke domænebetydning uden identitet. Centrale value objects omfatter:

- Contact: Address, Email, Phone
- Membership/Member: status-enums
- Contingent: Money, Currency, BillingPeriod, InvoiceRule
- Finance: Money, Currency, InvoiceNumber, PaymentReference, status-enums
- Accounting: AccountNumber, NormalBalance, AccountCategory/Group/Type, PostingSide, FiscalYearStatus

Designregel:
Value objects er immutable og anvendes til valideret, semantisk stærk repræsentation af domænedata.

## Entities
Centrale entities i domænet:

- Contact, Person, Organisation
- Member
- Membership, MembershipType
- ContingentPlan
- Invoice, InvoiceLine
- Payment, Receivable
- LedgerAccount, JournalEntry, JournalLine, FiscalYear, FiscalPeriod

Entities bærer identitet over tid og indgår i aggregate-konsistens.

## Repositories
Repository interfaces ligger i application boundary-laget og abstraherer persistence:

- ContactRepository
- MemberRepository
- MembershipTypeRepository
- ContingentPlanRepository
- UnitOfWork abstrahering via session-like kontrakt

Principper:
- repository interfaces beskriver domæneorienterede operationer (ikke SQL/ORM-detaljer)
- konkrete implementationer lever i persistence-laget (database/repositories)
- applikationslag afhænger af interfaces, ikke af konkrete infrastrukturlag

## Events
Domæne-/applikationsevents bruges til at signalere væsentlige tilstandsskift mellem use cases:

- MemberEnrolledEvent
  - udsendes ved vellykket enrollment

- InvoiceCreatedEvent
  - udsendes ved oprettelse af kontingentfaktura

- PaymentRegisteredEvent
  - udsendes ved registrering af betaling

Events dispatches synkront via application event dispatcher og bruges til orchestration uden tæt kobling mellem features/workflows.

## Features
Feature-laget er offentlig application API for domænebrugsscenarier.

Aktive feature-entry points omfatter:
- CreateMemberFeature
- CreateAnnualContingentFeature
- ListGeneralLedgerFeature
- AccountsReceivableService
- OpenItemsService

Feature-ansvar:
- modtage request DTO
- validere request
- orkestrere domæneregler via repositories/uow
- returnere response DTO
- udstille fejl via standardiseret exception-hierarki

## Public API
Public API følger standarden i architecture/public_api_standard.md:

- signatur: execute(request)
- request/response: immutable DTO'er
- response må ikke eksponere domain objects
- exceptions: ApplicationException, ValidationException, BusinessRuleViolation, RepositoryException
- navngivning: konsekvent feature- og DTO-konvention

Dette giver stabil kontrakt mod GUI/integrationer og reducerer coupling til domæne- og persistence-detaljer.

## Ikke mål
Dette designnotat omfatter ikke:

- detaljeret fysisk datamodel eller migration-plan
- UI-design, komponenthierarki eller navigation
- runtime deployment-arkitektur
- integration med eksterne systemer/protokoller
- performance tuning, caching eller skaleringstaktikker
- detaljerede sekvensdiagrammer pr. use case

Notatet definerer alene domænemodel, ansvar og arkitektoniske grænser for Organization-kernen.

## Capability Status (ORG)

Status pr. 2026-07-10:
- ORG-006: persistence-modeller + mapper på plads og testet.
- ORG-007: repository contracts + SQLite repositories med UnitOfWork på plads.
- ORG-008: application use cases med immutable DTO, events og rollback-tests på plads.
- ORG-009: feature layer facades med public API standard på plads.
- ORG-010: end-to-end integration workflows gennem hele stakken på plads.
- ORG-011: capability review dokumenteret i organization_capability_review.md.

Kvalitetsgate:
- Domain, persistence, repositories, application og feature layer valideres af eksisterende testpakke.
- Architecture compliance håndhæves via dependency guard og feature API architecture tests.

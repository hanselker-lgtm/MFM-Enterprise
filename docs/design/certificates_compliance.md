# CERT-000 Certificates and Compliance Capability Design

## Purpose
Certificates and Compliance capability etablerer et generisk domaene til registrering og styring af:
- certificates
- statutory documents
- inspections relateret til certificate issuance/validity/renewal
- validity periods
- expiry
- renewal requirements
- compliance status
- historical certificate records

Maalet er at understotte maritime fartoejer og maritime foreninger uden hardcoding af Alvur-specifik lovgivning eller lokale myndighedsregler i domain core.

## Bounded Context
Certificates and Compliance er et selvstaendigt bounded context.

Capability'en ejer:
- certificate identity
- certificate type
- certificate holder/target reference
- issue information
- validity period
- expiry state
- renewal tracking
- certificate status
- certificate history
- compliance observations inden for certificate-scope

Capability'en ejer IKKE:
- Vessel identity
- TechnicalComponent identity
- maintenance planning
- maintenance execution
- component lifecycle
- accounting
- document binary storage
- voyages

## Capability Responsibility
Certificates and Compliance har ansvar for:
- at modellere certificate lifecycle og validity state
- at evaluere expiry/compliance status ud fra eksplicit supplied current date
- at bevare historiske certificate records ved renewal
- at registrere certificate-relaterede inspections/compliance observations
- at eksponere stabil public API-kontrakt via application services og feature layer

Certificates and Compliance har ikke ansvar for:
- vedligeholdelsesarbejde eller work order lifecycle
- mutation af vessel eller organization master data
- lagring af dokumentbinaerer

## Aggregate Boundaries
Primary aggregate root:
1. Certificate

Boundary-beslutning:
- Certificate ejer identity, validity, lifecycle, renewal relation og historisk issuer snapshot.
- Inspection/compliance observation modelleres som certificate-owned entity/value data kun naar observationen vedroerer udstedelse, validering eller renewal.
- Maintenance inspections forbliver i Maintenance capability.

Transactional consistency rules:
- Certificate-transaktioner beskytter certificate invariants, lifecycle transitions og renewal relations.
- Renewal opretter et nyt Certificate aggregate og bevarer det gamle aggregate uaendret.

## Certificate Target
Value Object: CertificateTarget
- target_type
- target_id

Target types i v1:
- VESSEL
- ORGANIZATION

Vurdering af ekstra target types:
- PERSON: ikke medtaget i v1, da behov ikke er dokumenteret som capability-kernescenarie.
- TECHNICAL_COMPONENT: ikke medtaget i v1, da component compliance i denne fase modelleres via vessel/organization certifikatansvar; direkte component-targeting kan vurderes i senere capability med explicit scope-governance.

Regler:
- target_id er identity/reference (UUID) til ekstern capability.
- identity/reference only.
- ingen direkte cross-capability domain object references.

## Certificate Aggregate
Certificate aggregate root (foreslaaet state i v1):
- certificate_id
- certificate_type
- certificate_number
- target (CertificateTarget)
- issuer (IssuerReference)
- issued_date
- valid_from
- expires_at (optional for non-expiring)
- status (persisted lifecycle state)
- renewal_required
- renewed_from_certificate_id (optional)
- document_reference (optional metadata/reference)
- notes (optional)

Aggregate invariants:
- certificate_id er globalt unik.
- certificate_number + issuer identity skal vaere konsistent og ikke tom.
- target skal vaere gyldig CertificateTarget.
- chronology rules (se Validity Model) skal overholdes.
- renewed_from_certificate_id maa ikke pege paa sig selv.
- revoked certificate kan ikke reaktiveres.
- renewal maa ikke destruktivt overskrive tidligere certificate.

## Certificate Type
Valgt model i v1: controlled value object med certificate_type_id.

Begrundelse:
- Enum er for rigid til internationale/statutory variationer.
- Fri string er ukontrolleret og skaber datakvalitetsrisiko.
- Controlled value object giver governance og udvidelighed uden hardcoding af national lovgivning i domain core.

Foreslaaet model:
- CertificateTypeReference
  - certificate_type_id (stabil identity)
  - code (kontrolleret kode)
  - display_name_snapshot (optional til historisk visning)

## Validity Model
Valideringsmodeller i v1:
- Non-expiring certificate: expires_at = null
- Fixed expiry date: expires_at sat eksplicit
- Renewal required before expiry: renewal_required flag + policy i application/service layer

Chronology rules:
- issued_date <= valid_from
- hvis expires_at findes: valid_from <= expires_at
- hvis expires_at findes: issued_date <= expires_at

Ingen skjult system clock dependency; current/as_of date leveres eksplicit til evaluering.

## Expiry Calculation
Ansvar:
- Domain/service evaluerer certificate status ud fra persisted lifecycle state + explicit as_of_date.

Statusmodel beslutning:
- Persisted lifecycle state: DRAFT, ACTIVE, SUSPENDED, REVOKED, EXPIRED.
- EXPIRING er derived status (ikke persisted).

Begrundelse:
- EXPIRING afhaenger af policy-window relativt til as_of_date og kan variere per use case.
- Persisting EXPIRING skaber risiko for stale state og clock-coupling.

Derived evaluation eksempel:
- ACTIVE + expiry inden for configured threshold => EXPIRING (derived)
- ACTIVE + expiry passeret ved as_of_date => EXPIRED

## Certificate Lifecycle
Lifecycle i v1:
- DRAFT -> ACTIVE
- ACTIVE -> SUSPENDED
- ACTIVE -> REVOKED
- ACTIVE -> EXPIRED (ved evaluering/as_of over expiry)
- SUSPENDED -> ACTIVE (hvis business policy tillader)
- SUSPENDED -> REVOKED

Terminal states:
- REVOKED er terminal.
- EXPIRED er terminal for det konkrete certificate record.

Renewal behavior:
- Renewal skaber nyt certificate (Certificate B) med relation til tidligere certificate (Certificate A).
- Certificate A bevares historisk og overskrives ikke.

## Certificate Renewal
Kontrolleret renewal relation i v1:
- renewed_from_certificate_id paa nyt certificate

Regler:
- Certificate B maa referere Certificate A som renewed_from.
- Certificate A forbliver immutable mht. historiske issue/validity/issuer/number snapshots.
- Historik maa ikke reduceres til kun current certificate.

## Historical Certificate Truth
Historisk sandhedskrav:
- Certificate A (issued 2027, context A) bevares efter renewal.
- Certificate B (issued 2028, context B) oprettes som separat record.
- Certificate A bevarer original issuer, dates og certificate_number.
- Renewal relation mellem A og B bevares.

Konsekvens:
- Nutidens certificate state maa ikke omskrive historiske records.
- Issuer navn i gamle records maa ikke muteres af senere master-data aendringer.

## Inspection Boundary
Skel:
- Maintenance Inspection: teknisk vedligeholdelsesarbejde og execution lifecycle (Maintenance ejer).
- Statutory/Certificate Inspection: observationer direkte relateret til certificate issuance/validity/renewal (Certificates/Compliance ejer).

Boundary-regel:
- Certificates registrerer kun inspection information, naar den har direkte certificate-compliance ansvar.
- Ingen duplicate ownership af samme inspection-lifecycle paa tvaers af capabilities.

## Maintenance Boundary
Assessment:
- Certificate kan have inspection/compliance resultat, der indikerer behov for vedligehold.
- Maintenance forbliver eneste ejer af maintenance work.

Certificates maa ikke:
- oprette MaintenancePlan
- aendre MaintenanceTask/Requirement
- complete WorkOrder
- skrive MaintenanceRecord

Maintenance maa ikke:
- issue certificate
- renew certificate
- revoke certificate
- aendre certificate validity

Fremtidigt integration point (design-only):
- Certificate compliance finding kan publicere reference/event, som Maintenance kan konsumere via separat orkestrering uden direkte write-adgang mellem contexts.

## Fleet Boundary
Certificate target kan referere Vessel identity via CertificateTarget(VESSEL, target_id).

Boundary-regler:
- Certificates maa ikke mutere Vessel.
- Certificates maa ikke eje Vessel state.
- Certificates maa ikke importere Fleet infrastructure internals.
- identity/reference only.

## Organization Boundary
Certificate target kan referere Organization identity via CertificateTarget(ORGANIZATION, target_id).

Boundary-regler:
- Ingen kopiering af Organization aggregate state.
- identity/reference only.

## Issuer Model
Valgt model: IssuerReference value object.

Foreslaaede felter:
- issuer_type (AUTHORITY, CLASSIFICATION_SOCIETY, INSPECTION_BODY, OTHER_ORGANIZATION)
- issuer_id_or_external_key (kontrolleret identity/reference)
- issuer_name_snapshot

Beslutning:
- issuer_name_snapshot gemmes i certificate record for historisk sandhed.
- Senere navneaendringer i eksterne registre maa ikke omskrive historiske certificate records.

## Document Reference
CERT-000 designer kun metadata/reference til dokument.

Valgt model i v1:
- document_reference (opaque reference string)
- external_document_id (optional)

Afgraensning:
- Ingen binary document storage.
- Ingen blob/filesystem management.
- Ingen separat document management capability i denne fase.

## Domain Events
Relevante events i v1 (design-only):
- CertificateCreated
- CertificateActivated
- CertificateExpired
- CertificateSuspended
- CertificateRevoked
- CertificateRenewed

Principper:
- kun events med reel domain responsibility.
- undgaa event inflation for trivielle feltopdateringer.

## Repositories
Aggregate root repository:
- CertificateRepository

Noedvendige queries i v1:
- add
- get_by_id
- get_by_target
- get_active_by_target
- get_expiring
- get_expired
- get_renewal_history
- update
- exists

Ingen spekulative query-endpoints ud over dokumenterede capability-behov.

## Application Services
Foreslaaede use cases i v1:
- CreateCertificateUseCase
- ActivateCertificateUseCase
- EvaluateCertificateStatusUseCase
- SuspendCertificateUseCase
- RevokeCertificateUseCase
- RenewCertificateUseCase
- GetCertificateHistoryUseCase
- GetExpiringCertificatesUseCase

Orchestration-princip:
- Application services orkestrerer repository/UoW og eksplicit status-evaluering med supplied as_of_date.

## Feature API
Public API foelger MFM Enterprise Public API Standard:
- execute(request)
- immutable Request DTO
- immutable Response DTO
- API-safe primitive/public types
- no domain object leakage
- no persistence model leakage

## End-to-End Workflows
Planlagte E2E workflows for senere implementation/verification:
1. Create vessel certificate
2. Activate certificate
3. Evaluate valid certificate
4. Evaluate expiring certificate
5. Evaluate expired certificate
6. Renew certificate and preserve history
7. Suspend certificate
8. Revoke certificate
9. Organization-target certificate
10. Failure and rollback
11. Capability boundary workflow

## Architecture
Dependency direction:
- Certificates may reference identities fra Fleet og Organization.
- Technical Configuration identities maa kun refereres, hvis fremtidig godkendt target type kraever det (ikke i v1).
- Certificates maa ikke dependere paa infrastructure internals fra locked capabilities.
- Maintenance og Certificates forbliver separate sibling capabilities.
- No reverse dependency fra locked capabilities til Certificates.

Locked capabilities i denne fase:
- Asset Core
- Fleet
- Technical Configuration
- Maintenance

## Alvur Validation Scenarios
Scenarierne anvendes kun til designvalidering.

Scenario 1:
- Vessel certificate issued by authority med fixed expiry date.
- Validity evalueres med explicit as_of_date.
- Renewal opretter nyt certificate, gammelt certificate bevares.

Scenario 2:
- Certificate-relateret inspection finder behov for maintenance work.
- Certificates registrerer compliance observation.
- Maintenance forbliver ejer af maintenance workflow; ingen WorkOrder-oprettelse/completion i Certificates.

Scenario 3:
- Historisk certificate bevarer original issuer_name_snapshot og certificate_number, selv hvis issuer metadata senere aendres.

## Risks
- historical certificate overwrite
- derived/persisted status confusion
- hidden clock dependency
- renewal history loss
- issuer snapshot corruption
- maintenance inspection ownership overlap
- cross-capability target leakage
- public API domain leakage

## Ikke maal
CERT-000 omfatter ikke:
- maintenance planning
- maintenance execution
- technical component lifecycle
- voyages
- accounting
- insurance
- binary document storage
- document management
- automated authority integration
- notifications
- GUI

## Design Recommendation
READY FOR DOMAIN IMPLEMENTATION

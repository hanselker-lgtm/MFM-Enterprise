from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.application.contact_communication.contact_communication_service import (
    ContactCommunicationService,
)
from mfm.application.contact_communication.contact_communication_service import (
    SetupContactCommunicationRequest,
)
from mfm.application.document_archive.document_archive_service import (
    AddArchiveVersionRequest,
)
from mfm.application.document_archive.document_archive_service import (
    ArchiveDocumentRecordRequest,
)
from mfm.application.document_archive.document_archive_service import AttachArchiveRequest
from mfm.application.document_archive.document_archive_service import (
    CreateArchiveDocumentRequest,
)
from mfm.application.document_archive.document_archive_service import DocumentArchiveService
from mfm.application.events_activities.events_activities_service import AddActivityRequest
from mfm.application.events_activities.events_activities_service import CreateEventRequest
from mfm.application.events_activities.events_activities_service import (
    EventsActivitiesService,
)
from mfm.application.events_activities.events_activities_service import (
    RegisterParticipantRequest,
)
from mfm.application.features.annual_contingent_generation import (
    CreateAnnualContingentResponse,
)
from mfm.application.membership.membership_management_service import (
    MembershipManagementService,
)
from mfm.application.membership.membership_management_service import (
    RegisterMembershipRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
    MembershipBillingService,
)
from mfm.application.membership_billing.membership_billing_service import (
    RunMembershipBillingRequest,
)
from mfm.application.membership_billing.membership_billing_service import (
    SetupFeeScheduleRequest,
)
from mfm.application.reporting.document_archive_summary_service import (
    DocumentArchiveSummaryRequest,
)
from mfm.application.reporting.document_archive_summary_service import (
    DocumentArchiveSummaryService,
)
from mfm.domain.document_archive.document import Document
from mfm.domain.events_activities.event_activity_profile import EventActivityProfile
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_type import MembershipType
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile


class _MembershipRepository:
    def __init__(self) -> None:
        self.memberships: dict[UUID, Membership] = {}
        self.members: set[UUID] = set()

    def add(self, membership: Membership) -> None:
        self.memberships[membership.id] = membership

    def update(self, membership: Membership) -> None:
        self.memberships[membership.id] = membership

    def get(self, membership_id: UUID) -> Membership | None:
        return self.memberships.get(membership_id)

    def list_by_member(self, member_id: UUID) -> list[Membership]:
        return [m for m in self.memberships.values() if m.member_id == member_id]

    def member_exists(self, member_id: UUID) -> bool:
        return member_id in self.members


class _MembershipTypeRepository:
    def __init__(self, membership_type: MembershipType) -> None:
        self._membership_type = membership_type

    def get(self, membership_type_id: UUID) -> MembershipType | None:
        if membership_type_id == self._membership_type.id:
            return self._membership_type
        return None


class _BillingRepository:
    def __init__(self) -> None:
        self.store: dict[UUID, MembershipBillingProfile] = {}

    def get(self, membership_type_id: UUID) -> MembershipBillingProfile | None:
        return self.store.get(membership_type_id)

    def save(self, profile: MembershipBillingProfile) -> None:
        self.store[profile.membership_type_id] = profile


class _AnnualContingentFeature:
    def __init__(self) -> None:
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        return CreateAnnualContingentResponse(
            processed=5,
            invoices_created=4,
            journal_drafts_created=4,
            skipped=1,
            warnings=(),
            errors=(),
        )


class _EventsRepository:
    def __init__(self) -> None:
        self.store: dict[UUID, EventActivityProfile] = {}

    def get(self, event_id: UUID) -> EventActivityProfile | None:
        return self.store.get(event_id)

    def save(self, profile: EventActivityProfile) -> None:
        self.store[profile.event.event_id] = profile


class _DocumentArchiveRepository:
    def __init__(self) -> None:
        self.store: dict[UUID, Document] = {}

    def get(self, document_id: UUID) -> Document | None:
        return self.store.get(document_id)

    def save(self, document: Document) -> None:
        self.store[document.document_id] = document

    def list(self) -> list[Document]:
        return list(self.store.values())


class _CreateDocumentFeature:
    def execute(self, request):
        doc_id = uuid4()
        return type(
            "CreateDocumentResponseObj",
            (),
            {
                "document": type(
                    "DocumentResponseObj",
                    (),
                    {
                        "document_id": doc_id,
                        "document_number": request.document_number,
                        "document_title": request.document_title,
                        "document_type": request.document_type,
                        "status": request.status,
                    },
                )()
            },
        )()


class _RegisterDocumentVersionFeature:
    def execute(self, request):
        _ = request
        return None


class _AttachReferenceFeature:
    def execute(self, request):
        _ = request
        return None


class _ArchiveDocumentFeature:
    def execute(self, request):
        _ = request
        return None


class _ContactCommunicationRepository:
    def __init__(self) -> None:
        self.store = {}

    def get(self, contact_id: UUID):
        return self.store.get(contact_id)

    def save(self, profile) -> None:
        self.store[profile.contact_id] = profile


def _dt(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour, 0, tzinfo=UTC)


def test_int001_membership_billing_and_accounting_contract() -> None:
    membership_type_id = uuid4()
    membership_type = MembershipType(id=membership_type_id, code="GEN", name="General")

    membership_repo = _MembershipRepository()
    member_id = uuid4()
    membership_repo.members.add(member_id)
    membership_service = MembershipManagementService(
        membership_repository=membership_repo,
        membership_type_repository=_MembershipTypeRepository(membership_type),
    )
    membership = membership_service.register_membership(
        RegisterMembershipRequest(
            member_id=member_id,
            membership_type_id=membership_type_id,
        )
    )

    annual_feature = _AnnualContingentFeature()
    billing_service = MembershipBillingService(
        repository=_BillingRepository(),
        annual_contingent_feature=annual_feature,
    )
    billing_service.setup_fee_schedule(
        SetupFeeScheduleRequest(
            membership_type_id=membership.membership_type_id,
            membership_type_code=membership.membership_type_code,
            membership_type_name=membership.membership_type_name,
            amount=Decimal("1200.00"),
            currency="DKK",
            due_days=14,
        )
    )
    result = billing_service.run_billing(
        RunMembershipBillingRequest(
            membership_type_id=membership.membership_type_id,
            fiscal_year=2026,
            billing_date=date(2026, 1, 1),
            dry_run=False,
        )
    )

    assert result.run_invoices_created == 4
    assert annual_feature.last_request is not None
    assert annual_feature.last_request.membership_type_id == membership.membership_type_id


def test_int001_membership_events_registration_contract() -> None:
    member_id = uuid4()
    events_service = EventsActivitiesService(repository=_EventsRepository())

    created = events_service.create_event(
        CreateEventRequest(
            event_name="Integration Event",
            venue_name="Hall A",
            venue_address="Dock 1",
            venue_capacity=100,
            start_at=_dt(9),
            end_at=_dt(17),
        )
    )
    events_service.add_activity(
        AddActivityRequest(
            event_id=created.event_id,
            title="Kickoff",
            start_at=_dt(10),
            end_at=_dt(11),
        )
    )
    registered = events_service.register_participant(
        RegisterParticipantRequest(
            event_id=created.event_id,
            member_id=member_id,
            registered_at=_dt(8),
        )
    )

    assert registered.registrations_count == 1


def test_int001_document_links_cover_membership_org_events_billing_projects() -> None:
    repository = _DocumentArchiveRepository()
    archive_service = DocumentArchiveService(
        repository=repository,
        create_document_feature=_CreateDocumentFeature(),
        register_document_version_feature=_RegisterDocumentVersionFeature(),
        attach_reference_feature=_AttachReferenceFeature(),
        archive_document_feature=_ArchiveDocumentFeature(),
    )

    created = archive_service.create_document(
        CreateArchiveDocumentRequest(
            document_number="DOC-INT001-001",
            document_title="Platform Integration Evidence",
            document_type="EVIDENCE",
            folder_name="Integration",
            folder_path="/docs/integration",
            category_code="INT",
            category_name="Integration",
            initial_storage_key="docs/integration/doc-int001-001/v1.pdf",
            created_at=_dt(9),
        )
    )

    archive_service.add_version(
        AddArchiveVersionRequest(
            document_id=created.document_id,
            version_number=2,
            storage_key="docs/integration/doc-int001-001/v2.pdf",
            created_at=_dt(10),
        )
    )

    pairs = (
        ("MEMBERSHIP", "MEMBERSHIP"),
        ("ORGANIZATION", "ORGANIZATION"),
        ("EVENTS", "EVENT"),
        ("BILLING", "INVOICE"),
        ("PROJECTS", "PROJECT"),
    )
    for capability, aggregate_type in pairs:
        archive_service.attach(
            AttachArchiveRequest(
                document_id=created.document_id,
                target_capability=capability,
                target_aggregate_type=aggregate_type,
                target_aggregate_id=str(uuid4()),
                description=f"Integration link for {capability}",
                checked_at=_dt(11),
            )
        )

    archived = archive_service.archive(
        ArchiveDocumentRecordRequest(
            document_id=created.document_id,
            reason="Review completed",
            archived_at=_dt(12),
        )
    )

    summary = DocumentArchiveSummaryService(repository=repository).execute(
        DocumentArchiveSummaryRequest(include_archived=True)
    )

    assert archived.archived is True
    assert summary.integration.membership_links == 1
    assert summary.integration.organization_links == 1
    assert summary.integration.events_links == 1
    assert summary.integration.billing_links == 1
    assert summary.integration.projects_links == 1


def test_int001_communication_contract_across_capability_contexts() -> None:
    service = ContactCommunicationService(repository=_ContactCommunicationRepository())

    contexts = (
        "membership",
        "organization",
        "events",
        "billing",
        "projects",
        "documents",
    )

    for idx, _context in enumerate(contexts, start=1):
        response = service.setup(
            SetupContactCommunicationRequest(
                contact_id=uuid4(),
                email_address=f"contact{idx}@example.com",
                phone_number=f"+45110000{idx:02d}",
                postal_line1=f"Street {idx}",
                postal_code="1000",
                postal_city="Copenhagen",
                postal_country="DK",
                allow_marketing=False,
            )
        )
        assert response.method_count == 3

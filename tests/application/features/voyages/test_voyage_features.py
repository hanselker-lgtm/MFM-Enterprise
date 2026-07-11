from __future__ import annotations

from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.voyages.arrive_voyage_feature import ArriveVoyageFeature
from mfm.application.features.voyages.arrive_voyage_feature import ArriveVoyageRequest
from mfm.application.features.voyages.cancel_voyage_feature import CancelVoyageFeature
from mfm.application.features.voyages.cancel_voyage_feature import CancelVoyageRequest
from mfm.application.features.voyages.create_voyage_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.voyages.create_voyage_feature import CreateVoyageFeature
from mfm.application.features.voyages.create_voyage_feature import CreateVoyageRequest
from mfm.application.features.voyages.create_voyage_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.voyages.create_voyage_feature import (
    ValidationException as FeatureValidationException,
)
from mfm.application.features.voyages.create_voyage_feature import VoyageLocationInput
from mfm.application.features.voyages.depart_voyage_feature import DepartVoyageFeature
from mfm.application.features.voyages.depart_voyage_feature import DepartVoyageRequest
from mfm.application.features.voyages.get_voyage_feature import GetVoyageFeature
from mfm.application.features.voyages.get_voyage_feature import GetVoyageRequest
from mfm.application.features.voyages.list_vessel_voyages_feature import (
    ListVesselVoyagesFeature,
)
from mfm.application.features.voyages.list_vessel_voyages_feature import (
    ListVesselVoyagesRequest,
)
from mfm.application.features.voyages.plan_voyage_feature import PlanVoyageFeature
from mfm.application.features.voyages.plan_voyage_feature import PlanVoyageRequest
from mfm.application.voyages.arrive_voyage import ArriveVoyageUseCase
from mfm.application.voyages.cancel_voyage import CancelVoyageUseCase
from mfm.application.voyages.create_voyage import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.voyages.create_voyage import (
    CreateVoyageResponse as ServiceCreateVoyageResponse,
)
from mfm.application.voyages.create_voyage import CreateVoyageUseCase
from mfm.application.voyages.create_voyage import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.voyages.create_voyage import (
    ValidationException as ServiceValidationException,
)
from mfm.application.voyages.depart_voyage import DepartVoyageUseCase
from mfm.application.voyages.get_voyage import GetVoyageUseCase
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesUseCase
from mfm.application.voyages.plan_voyage import PlanVoyageUseCase
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.repositories.voyage_repository import VoyageRepository
from tests.application.voyages.test_voyage_use_cases import FakeVoyageUnitOfWork


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _location(name: str, external_id: str) -> VoyageLocationInput:
    return VoyageLocationInput(
        name_snapshot=name,
        location_external_id=external_id,
        locality_snapshot=f"{name} locality",
        country_snapshot=f"{name} country",
    )


def _service_create_response() -> ServiceCreateVoyageResponse:
    from mfm.application.voyages.create_voyage import CreateVoyageResponse
    from mfm.application.voyages.create_voyage import VoyageLocationResponse
    from mfm.application.voyages.create_voyage import VoyagePurposeResponse
    from mfm.application.voyages.create_voyage import VoyageResponse

    return CreateVoyageResponse(
        voyage=VoyageResponse(
            voyage_id=UUID("00000000-0000-0000-0000-00000000E001"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000E101"),
            status="DRAFT",
            voyage_reference="VOY-FEAT-001",
            planned_departure_location=VoyageLocationResponse(
                name_snapshot="Port A",
                location_external_id="PORT-A",
                locality_snapshot="Port A locality",
                country_snapshot="Port A country",
            ),
            planned_arrival_location=VoyageLocationResponse(
                name_snapshot="Port B",
                location_external_id="PORT-B",
                locality_snapshot="Port B locality",
                country_snapshot="Port B country",
            ),
            planned_departure_at=_aware_utc(2029, 1, 1, 8, 0),
            planned_arrival_at=_aware_utc(2029, 1, 1, 18, 0),
            actual_departure_location=None,
            actual_arrival_location=None,
            departed_at=None,
            arrived_at=None,
            voyage_purpose=VoyagePurposeResponse(
                purpose_code="OPERATIONAL",
                purpose_detail="Feature test",
            ),
            notes="Feature notes",
            cancellation_reason=None,
            cancelled_at=None,
            cancelled_by_reference=None,
            document_reference="VOY-DOC-FEAT",
        )
    )


def _seed_voyage(
    uow: FakeVoyageUnitOfWork,
    *,
    voyage_id: UUID,
    vessel_id: UUID,
    planned_departure_at: datetime,
) -> Voyage:
    voyage = Voyage(
        id=voyage_id,
        vessel_id=vessel_id,
        planned_departure_location=LocationSnapshot(
            name_snapshot="Port A",
            location_external_id="PORT-A",
            locality_snapshot="Port A locality",
            country_snapshot="Port A country",
        ),
        planned_arrival_location=LocationSnapshot(
            name_snapshot="Port B",
            location_external_id="PORT-B",
            locality_snapshot="Port B locality",
            country_snapshot="Port B country",
        ),
        planned_departure_at=planned_departure_at,
        planned_arrival_at=planned_departure_at.replace(hour=18),
        voyage_reference=f"REF-{voyage_id}",
        voyage_purpose=VoyagePurpose(purpose_code=VoyagePurposeCode.OPERATIONAL),
        notes="Seed",
        document_reference="SEED-DOC",
    )
    uow._repository._items[voyage.id.value] = voyage
    return voyage


def test_create_voyage_feature_happy_path_request_mapping_and_no_domain_leakage() -> None:
    service = StubService(response=_service_create_response())
    feature = CreateVoyageFeature(service=service)

    response = feature.execute(
        CreateVoyageRequest(
            voyage_id=UUID("00000000-0000-0000-0000-00000000E001"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000E101"),
            planned_departure_location=_location("Port A", "PORT-A"),
            planned_arrival_location=_location("Port B", "PORT-B"),
            planned_departure_at=_aware_utc(2029, 1, 1, 8, 0),
            planned_arrival_at=_aware_utc(2029, 1, 1, 18, 0),
            voyage_reference="VOY-FEAT-001",
            purpose_code="OPERATIONAL",
            purpose_detail="Feature test",
            notes="Feature notes",
            document_reference="VOY-DOC-FEAT",
        )
    )

    assert response.voyage.voyage_reference == "VOY-FEAT-001"
    assert response.voyage.status == "DRAFT"
    assert isinstance(response.voyage.vessel_id, UUID)
    assert is_dataclass(response.voyage)
    assert not isinstance(response.voyage, Voyage)
    assert service.last_request.vessel_id == UUID("00000000-0000-0000-0000-00000000E101")


def test_create_voyage_feature_validation_and_application_error_mapping() -> None:
    feature = CreateVoyageFeature(service=StubService(response=None))

    with pytest.raises(FeatureValidationException):
        feature.execute(
            CreateVoyageRequest(
                vessel_id=uuid4(),
                planned_departure_location=_location("Port A", "PORT-A"),
                planned_arrival_location=_location("Port B", "PORT-B"),
                planned_departure_at=_aware_utc(2029, 1, 1, 8, 0),
                planned_arrival_at=_aware_utc(2029, 1, 1, 18, 0),
                purpose_code=1,  # type: ignore[arg-type]
            )
        )

    duplicate = CreateVoyageFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate reference"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(
            CreateVoyageRequest(
                vessel_id=uuid4(),
                planned_departure_location=_location("Port A", "PORT-A"),
                planned_arrival_location=_location("Port B", "PORT-B"),
                planned_departure_at=_aware_utc(2029, 1, 1, 8, 0),
                planned_arrival_at=_aware_utc(2029, 1, 1, 18, 0),
            )
        )

    rollback = CreateVoyageFeature(
        service=StubService(error=ServiceRepositoryException("rollback"))
    )
    with pytest.raises(FeatureRepositoryException):
        rollback.execute(
            CreateVoyageRequest(
                vessel_id=uuid4(),
                planned_departure_location=_location("Port A", "PORT-A"),
                planned_arrival_location=_location("Port B", "PORT-B"),
                planned_departure_at=_aware_utc(2029, 1, 1, 8, 0),
                planned_arrival_at=_aware_utc(2029, 1, 1, 18, 0),
            )
        )

    invalid = CreateVoyageFeature(
        service=StubService(error=ServiceValidationException("invalid purpose"))
    )
    with pytest.raises(FeatureValidationException):
        invalid.execute(
            CreateVoyageRequest(
                vessel_id=uuid4(),
                planned_departure_location=_location("Port A", "PORT-A"),
                planned_arrival_location=_location("Port B", "PORT-B"),
                planned_departure_at=_aware_utc(2029, 1, 1, 8, 0),
                planned_arrival_at=_aware_utc(2029, 1, 1, 18, 0),
            )
        )


def test_plan_depart_arrive_cancel_get_and_list_feature_mapping_with_real_services() -> None:
    uow = FakeVoyageUnitOfWork()

    create_feature = CreateVoyageFeature(service=CreateVoyageUseCase(unit_of_work=uow))
    plan_feature = PlanVoyageFeature(service=PlanVoyageUseCase(unit_of_work=uow))
    depart_feature = DepartVoyageFeature(service=DepartVoyageUseCase(unit_of_work=uow))
    arrive_feature = ArriveVoyageFeature(service=ArriveVoyageUseCase(unit_of_work=uow))
    cancel_feature = CancelVoyageFeature(service=CancelVoyageUseCase(unit_of_work=uow))
    get_feature = GetVoyageFeature(service=GetVoyageUseCase(unit_of_work=uow))
    list_feature = ListVesselVoyagesFeature(service=ListVesselVoyagesUseCase(unit_of_work=uow))

    created = create_feature.execute(
        CreateVoyageRequest(
            voyage_id=UUID("00000000-0000-0000-0000-00000000E201"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000E301"),
            planned_departure_location=_location("Port A", "PORT-A"),
            planned_arrival_location=_location("Port B", "PORT-B"),
            planned_departure_at=_aware_utc(2029, 2, 1, 8, 0),
            planned_arrival_at=_aware_utc(2029, 2, 1, 18, 0),
            voyage_reference="VOY-FLOW",
            purpose_code="DEMONSTRATION",
            purpose_detail="Truth proof",
        )
    )

    planned = plan_feature.execute(
        PlanVoyageRequest(voyage_id=created.voyage.voyage_id)
    )
    assert planned.voyage.status == "PLANNED"

    departed = depart_feature.execute(
        DepartVoyageRequest(
            voyage_id=created.voyage.voyage_id,
            departed_at=_aware_utc(2029, 2, 1, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )
    assert departed.voyage.status == "UNDERWAY"

    arrived = arrive_feature.execute(
        ArriveVoyageRequest(
            voyage_id=created.voyage.voyage_id,
            arrived_at=_aware_utc(2029, 2, 1, 20, 0),
            actual_arrival_location=_location("Port C", "PORT-C"),
        )
    )
    assert arrived.voyage.status == "COMPLETED"

    loaded = get_feature.execute(GetVoyageRequest(voyage_id=created.voyage.voyage_id))

    assert loaded.voyage.planned_departure_location.name_snapshot == "Port A"
    assert loaded.voyage.planned_arrival_location.name_snapshot == "Port B"
    assert loaded.voyage.actual_departure_location is not None
    assert loaded.voyage.actual_departure_location.name_snapshot == "Port A"
    assert loaded.voyage.actual_arrival_location is not None
    assert loaded.voyage.actual_arrival_location.name_snapshot == "Port C"
    assert loaded.voyage.planned_departure_at == _aware_utc(2029, 2, 1, 8, 0)
    assert loaded.voyage.planned_arrival_at == _aware_utc(2029, 2, 1, 18, 0)
    assert loaded.voyage.departed_at == _aware_utc(2029, 2, 1, 9, 0)
    assert loaded.voyage.arrived_at == _aware_utc(2029, 2, 1, 20, 0)

    cancelled_created = create_feature.execute(
        CreateVoyageRequest(
            voyage_id=UUID("00000000-0000-0000-0000-00000000E202"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000E302"),
            planned_departure_location=_location("Port A", "PORT-A"),
            planned_arrival_location=_location("Port B", "PORT-B"),
            planned_departure_at=_aware_utc(2029, 3, 1, 8, 0),
            planned_arrival_at=_aware_utc(2029, 3, 1, 18, 0),
        )
    )
    plan_feature.execute(PlanVoyageRequest(voyage_id=cancelled_created.voyage.voyage_id))
    cancelled = cancel_feature.execute(
        CancelVoyageRequest(
            voyage_id=cancelled_created.voyage.voyage_id,
            cancellation_reason="Weather closure",
            cancelled_at=_aware_utc(2029, 3, 1, 7, 30),
            cancelled_by_reference="planner",
        )
    )
    assert cancelled.voyage.status == "CANCELLED"
    assert cancelled.voyage.actual_departure_location is None
    assert cancelled.voyage.actual_arrival_location is None

    vessel_a = UUID("00000000-0000-0000-0000-00000000E401")
    vessel_b = UUID("00000000-0000-0000-0000-00000000E402")

    _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000E501"),
        vessel_id=vessel_a,
        planned_departure_at=_aware_utc(2029, 4, 1, 8, 0),
    )
    _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000E502"),
        vessel_id=vessel_a,
        planned_departure_at=_aware_utc(2029, 4, 2, 8, 0),
    )
    _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000E503"),
        vessel_id=vessel_b,
        planned_departure_at=_aware_utc(2029, 4, 3, 8, 0),
    )

    listed = list_feature.execute(ListVesselVoyagesRequest(vessel_id=vessel_a))
    ids = [item.voyage_id for item in listed.voyages]
    assert UUID("00000000-0000-0000-0000-00000000E501") in ids
    assert UUID("00000000-0000-0000-0000-00000000E502") in ids
    assert UUID("00000000-0000-0000-0000-00000000E503") not in ids


def test_feature_error_mapping_for_not_found_lifecycle_and_arrival_chronology() -> None:
    uow = FakeVoyageUnitOfWork()
    plan_feature = PlanVoyageFeature(service=PlanVoyageUseCase(unit_of_work=uow))

    with pytest.raises(FeatureBusinessRuleViolation):
        plan_feature.execute(
            PlanVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000E900"))
        )

    voyage = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000E203"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000E303"),
        planned_departure_at=_aware_utc(2029, 5, 1, 8, 0),
    )
    plan_feature.execute(PlanVoyageRequest(voyage_id=voyage.id.value))

    depart_feature = DepartVoyageFeature(service=DepartVoyageUseCase(unit_of_work=uow))
    depart_feature.execute(
        DepartVoyageRequest(
            voyage_id=voyage.id.value,
            departed_at=_aware_utc(2029, 5, 1, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        ArriveVoyageFeature(service=ArriveVoyageUseCase(unit_of_work=uow)).execute(
            ArriveVoyageRequest(
                voyage_id=voyage.id.value,
                arrived_at=_aware_utc(2029, 5, 1, 8, 30),
                actual_arrival_location=_location("Port C", "PORT-C"),
            )
        )


def test_hidden_clock_protection_and_public_safety_annotations_runtime_values() -> None:
    response = _service_create_response().voyage
    feature_response = CreateVoyageFeature(service=StubService(response=_service_create_response())).execute(
        CreateVoyageRequest(
            vessel_id=response.vessel_id,
            planned_departure_location=_location("Port A", "PORT-A"),
            planned_arrival_location=_location("Port B", "PORT-B"),
            planned_departure_at=response.planned_departure_at,
            planned_arrival_at=response.planned_arrival_at,
        )
    )

    assert isinstance(feature_response.voyage.voyage_id, UUID)
    assert isinstance(feature_response.voyage.vessel_id, UUID)
    assert isinstance(feature_response.voyage.status, str)
    assert isinstance(feature_response.voyage.planned_departure_at, datetime)
    assert feature_response.voyage.actual_arrival_location is None


def test_feature_request_validation_for_explicit_timestamps_and_inputs() -> None:
    depart = DepartVoyageFeature(service=StubService(response=None))

    with pytest.raises(FeatureValidationException):
        depart.execute(
            DepartVoyageRequest(
                voyage_id=uuid4(),
                departed_at="not-a-datetime",  # type: ignore[arg-type]
                actual_departure_location=_location("Port A", "PORT-A"),
            )
        )

    arrive = ArriveVoyageFeature(service=StubService(response=None))
    with pytest.raises(FeatureValidationException):
        arrive.execute(
            ArriveVoyageRequest(
                voyage_id=uuid4(),
                arrived_at="not-a-datetime",  # type: ignore[arg-type]
                actual_arrival_location=_location("Port C", "PORT-C"),
            )
        )


def test_list_vessel_voyages_nested_collection_is_public_safe() -> None:
    uow = FakeVoyageUnitOfWork()
    vessel = UUID("00000000-0000-0000-0000-00000000E700")

    _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000E701"),
        vessel_id=vessel,
        planned_departure_at=_aware_utc(2029, 6, 1, 8, 0),
    )

    listed = ListVesselVoyagesFeature(service=ListVesselVoyagesUseCase(unit_of_work=uow)).execute(
        ListVesselVoyagesRequest(vessel_id=vessel)
    )

    assert isinstance(listed.voyages, tuple)
    assert len(listed.voyages) == 1
    assert not isinstance(listed.voyages[0], Voyage)
    assert is_dataclass(listed.voyages[0])


def test_feature_maps_unexpected_service_error_to_repository_exception() -> None:
    feature = GetVoyageFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(FeatureRepositoryException):
        feature.execute(GetVoyageRequest(voyage_id=uuid4()))

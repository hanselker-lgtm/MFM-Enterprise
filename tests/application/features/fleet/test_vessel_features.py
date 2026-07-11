from __future__ import annotations

from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.fleet.change_vessel_registration_feature import (
    BusinessRuleViolation as ChangeRegistrationBusinessRuleViolation,
)
from mfm.application.features.fleet.change_vessel_registration_feature import (
    ChangeVesselRegistrationFeature,
)
from mfm.application.features.fleet.change_vessel_registration_feature import (
    ChangeVesselRegistrationRequest,
)
from mfm.application.features.fleet.change_vessel_registration_feature import (
    ChangeVesselRegistrationResponse,
)
from mfm.application.features.fleet.change_vessel_registration_feature import (
    ValidationException as ChangeRegistrationValidationException,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    BusinessRuleViolation as ChangeStatusBusinessRuleViolation,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    ChangeVesselStatusFeature,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    ChangeVesselStatusRequest,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    ChangeVesselStatusResponse,
)
from mfm.application.features.fleet.create_vessel_feature import (
    BusinessRuleViolation as CreateVesselBusinessRuleViolation,
)
from mfm.application.features.fleet.create_vessel_feature import CreateVesselFeature
from mfm.application.features.fleet.create_vessel_feature import CreateVesselRequest
from mfm.application.features.fleet.create_vessel_feature import CreateVesselResponse
from mfm.application.features.fleet.create_vessel_feature import (
    RepositoryException as CreateVesselRepositoryException,
)
from mfm.application.features.fleet.create_vessel_feature import (
    ValidationException as CreateVesselValidationException,
)
from mfm.application.features.fleet.rename_vessel_feature import RenameVesselFeature
from mfm.application.features.fleet.rename_vessel_feature import RenameVesselRequest
from mfm.application.features.fleet.rename_vessel_feature import RenameVesselResponse
from mfm.application.features.fleet.update_vessel_dimensions_feature import (
    UpdateVesselDimensionsFeature,
)
from mfm.application.features.fleet.update_vessel_dimensions_feature import (
    UpdateVesselDimensionsRequest,
)
from mfm.application.features.fleet.update_vessel_dimensions_feature import (
    UpdateVesselDimensionsResponse,
)
from mfm.application.features.fleet.update_vessel_feature import (
    UpdateVesselFeature,
)
from mfm.application.features.fleet.update_vessel_feature import (
    UpdateVesselRequest,
)
from mfm.application.features.fleet.update_vessel_feature import (
    UpdateVesselResponse,
)
from mfm.application.fleet.change_vessel_registration import (
    ChangeVesselRegistrationResponse as ServiceChangeRegistrationResponse,
)
from mfm.application.fleet.change_vessel_status import (
    ChangeVesselStatusResponse as ServiceChangeStatusResponse,
)
from mfm.application.fleet.create_vessel import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.fleet.create_vessel import (
    CreateVesselResponse as ServiceCreateVesselResponse,
)
from mfm.application.fleet.create_vessel import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.fleet.create_vessel import (
    ValidationException as ServiceValidationException,
)
from mfm.application.fleet.rename_vessel import (
    RenameVesselResponse as ServiceRenameVesselResponse,
)
from mfm.application.fleet.update_vessel import (
    UpdateVesselResponse as ServiceUpdateVesselResponse,
)
from mfm.application.fleet.update_vessel_dimensions import (
    UpdateVesselDimensionsResponse as ServiceUpdateDimensionsResponse,
)
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_status import VesselStatus


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


def test_create_vessel_feature_happy_path_and_response_mapping() -> None:
    vessel_id = uuid4()
    asset_id = uuid4()
    service = StubService(
        response=ServiceCreateVesselResponse(
            vessel_id=vessel_id,
            asset_id=asset_id,
            registration="OY-FEAT-001",
            name="Feature Vessel",
            status="ACTIVE",
        )
    )
    feature = CreateVesselFeature(service=service)

    response = feature.execute(
        CreateVesselRequest(
            asset_id=asset_id,
            registration="OY-FEAT-001",
            name="Feature Vessel",
            shipyard="Odense",
            build_year=2020,
            construction_material=VesselMaterial.STEEL,
            length=20.0,
            beam=5.0,
            draft=1.8,
            status=VesselStatus.ACTIVE,
        )
    )

    assert isinstance(response, CreateVesselResponse)
    assert isinstance(response.vessel_id, UUID)
    assert response.registration == "OY-FEAT-001"
    assert response.status == "ACTIVE"
    assert service.last_request.registration == "OY-FEAT-001"
    assert not isinstance(response.status, VesselStatus)


def test_create_vessel_feature_duplicate_registration_mapping() -> None:
    feature = CreateVesselFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate registration"))
    )

    with pytest.raises(CreateVesselBusinessRuleViolation):
        feature.execute(
            CreateVesselRequest(
                asset_id=uuid4(),
                registration="OY-FEAT-DUP",
                name="Duplicate",
                shipyard="Yard",
                build_year=2010,
                construction_material=VesselMaterial.OTHER,
                length=10.0,
                beam=3.0,
                draft=1.0,
                status=VesselStatus.ACTIVE,
            )
        )


def test_update_vessel_feature_happy_path() -> None:
    vessel_id = uuid4()
    service = StubService(
        response=ServiceUpdateVesselResponse(
            vessel_id=vessel_id,
            shipyard="Esbjerg",
            build_year=2018,
            construction_material="COMPOSITE",
        )
    )
    feature = UpdateVesselFeature(service=service)

    response = feature.execute(
        UpdateVesselRequest(
            vessel_id=vessel_id,
            shipyard="Esbjerg",
            build_year=2018,
            construction_material=VesselMaterial.COMPOSITE,
        )
    )

    assert isinstance(response, UpdateVesselResponse)
    assert response.shipyard == "Esbjerg"
    assert response.construction_material == "COMPOSITE"


def test_rename_vessel_feature_happy_path() -> None:
    vessel_id = uuid4()
    service = StubService(
        response=ServiceRenameVesselResponse(vessel_id=vessel_id, name="Renamed")
    )
    feature = RenameVesselFeature(service=service)

    response = feature.execute(
        RenameVesselRequest(vessel_id=vessel_id, name="Renamed")
    )

    assert isinstance(response, RenameVesselResponse)
    assert response.name == "Renamed"


def test_change_registration_feature_happy_path() -> None:
    vessel_id = uuid4()
    service = StubService(
        response=ServiceChangeRegistrationResponse(
            vessel_id=vessel_id,
            registration="OY-FEAT-NEW",
        )
    )
    feature = ChangeVesselRegistrationFeature(service=service)

    response = feature.execute(
        ChangeVesselRegistrationRequest(
            vessel_id=vessel_id,
            registration="OY-FEAT-NEW",
        )
    )

    assert isinstance(response, ChangeVesselRegistrationResponse)
    assert response.registration == "OY-FEAT-NEW"


def test_update_dimensions_feature_happy_path() -> None:
    vessel_id = uuid4()
    service = StubService(
        response=ServiceUpdateDimensionsResponse(
            vessel_id=vessel_id,
            length=30.0,
            beam=6.2,
            draft=2.1,
        )
    )
    feature = UpdateVesselDimensionsFeature(service=service)

    response = feature.execute(
        UpdateVesselDimensionsRequest(vessel_id=vessel_id, length=30.0, beam=6.2, draft=2.1)
    )

    assert isinstance(response, UpdateVesselDimensionsResponse)
    assert response.length == 30.0


def test_change_status_feature_happy_path() -> None:
    vessel_id = uuid4()
    service = StubService(
        response=ServiceChangeStatusResponse(vessel_id=vessel_id, status="LAID_UP")
    )
    feature = ChangeVesselStatusFeature(service=service)

    response = feature.execute(
        ChangeVesselStatusRequest(vessel_id=vessel_id, status=VesselStatus.LAID_UP)
    )

    assert isinstance(response, ChangeVesselStatusResponse)
    assert response.status == "LAID_UP"


def test_invalid_state_transition_mapping() -> None:
    feature = ChangeVesselStatusFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid state transition"))
    )

    with pytest.raises(ChangeStatusBusinessRuleViolation):
        feature.execute(
            ChangeVesselStatusRequest(vessel_id=uuid4(), status=VesselStatus.ACTIVE)
        )


def test_validation_error_mapping() -> None:
    feature = CreateVesselFeature(service=StubService(response=None))

    with pytest.raises(CreateVesselValidationException):
        feature.execute(
            CreateVesselRequest(
                asset_id=uuid4(),
                registration="",
                name="X",
                shipyard="Y",
                build_year=2010,
                construction_material=VesselMaterial.OTHER,
                length=10.0,
                beam=3.0,
                draft=1.0,
                status=VesselStatus.ACTIVE,
            )
        )


def test_application_exception_mapping() -> None:
    create_feature = CreateVesselFeature(
        service=StubService(error=ServiceValidationException("invalid request"))
    )
    with pytest.raises(CreateVesselValidationException):
        create_feature.execute(
            CreateVesselRequest(
                asset_id=uuid4(),
                registration="OY-FEAT-MAP",
                name="Map",
                shipyard="Yard",
                build_year=2015,
                construction_material=VesselMaterial.OTHER,
                length=10.0,
                beam=3.0,
                draft=1.0,
                status=VesselStatus.ACTIVE,
            )
        )

    unknown_feature = CreateVesselFeature(service=StubService(error=RuntimeError("boom")))
    with pytest.raises(CreateVesselRepositoryException):
        unknown_feature.execute(
            CreateVesselRequest(
                asset_id=uuid4(),
                registration="OY-FEAT-MAP2",
                name="Map2",
                shipyard="Yard",
                build_year=2015,
                construction_material=VesselMaterial.OTHER,
                length=10.0,
                beam=3.0,
                draft=1.0,
                status=VesselStatus.ACTIVE,
            )
        )


def test_change_registration_validation_mapping() -> None:
    feature = ChangeVesselRegistrationFeature(service=StubService(response=None))

    with pytest.raises(ChangeRegistrationValidationException):
        feature.execute(
            ChangeVesselRegistrationRequest(vessel_id=uuid4(), registration="   ")
        )


def test_no_domain_objects_leak_through_feature_public_api() -> None:
    service = StubService(
        response=ServiceCreateVesselResponse(
            vessel_id=uuid4(),
            asset_id=uuid4(),
            registration="OY-FEAT-NOLEAK",
            name="No Leak",
            status="RESTORATION",
        )
    )
    feature = CreateVesselFeature(service=service)

    response = feature.execute(
        CreateVesselRequest(
            asset_id=uuid4(),
            registration="OY-FEAT-NOLEAK",
            name="No Leak",
            shipyard="Yard",
            build_year=2017,
            construction_material=VesselMaterial.STEEL,
            length=18.0,
            beam=4.8,
            draft=1.6,
            status=VesselStatus.RESTORATION,
        )
    )

    assert isinstance(response.vessel_id, UUID)
    assert isinstance(response.asset_id, UUID)
    assert isinstance(response.registration, str)
    assert isinstance(response.name, str)
    assert isinstance(response.status, str)
    assert not isinstance(response.status, VesselStatus)

from __future__ import annotations

from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import CreateAssetResponse as ServiceCreateAssetResponse
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.application.asset.dispose_asset import DisposeAssetResponse as ServiceDisposeAssetResponse
from mfm.application.asset.relocate_asset import RelocateAssetResponse as ServiceRelocateAssetResponse
from mfm.application.asset.retire_asset import RetireAssetResponse as ServiceRetireAssetResponse
from mfm.application.asset.transfer_asset import TransferAssetResponse as ServiceTransferAssetResponse
from mfm.application.asset.update_asset import UpdateAssetResponse as ServiceUpdateAssetResponse
from mfm.application.features.asset.create_asset_feature import BusinessRuleViolation as CreateAssetBusinessRuleViolation
from mfm.application.features.asset.create_asset_feature import CreateAssetFeature
from mfm.application.features.asset.create_asset_feature import CreateAssetRequest
from mfm.application.features.asset.create_asset_feature import CreateAssetResponse
from mfm.application.features.asset.create_asset_feature import RepositoryException as CreateAssetRepositoryException
from mfm.application.features.asset.create_asset_feature import ValidationException as CreateAssetValidationException
from mfm.application.features.asset.dispose_asset_feature import BusinessRuleViolation as DisposeAssetBusinessRuleViolation
from mfm.application.features.asset.dispose_asset_feature import DisposeAssetFeature
from mfm.application.features.asset.dispose_asset_feature import DisposeAssetRequest
from mfm.application.features.asset.dispose_asset_feature import DisposeAssetResponse
from mfm.application.features.asset.dispose_asset_feature import RepositoryException as DisposeAssetRepositoryException
from mfm.application.features.asset.dispose_asset_feature import ValidationException as DisposeAssetValidationException
from mfm.application.features.asset.relocate_asset_feature import RelocateAssetFeature
from mfm.application.features.asset.relocate_asset_feature import RelocateAssetRequest
from mfm.application.features.asset.relocate_asset_feature import RelocateAssetResponse
from mfm.application.features.asset.relocate_asset_feature import ValidationException as RelocateAssetValidationException
from mfm.application.features.asset.retire_asset_feature import BusinessRuleViolation as RetireAssetBusinessRuleViolation
from mfm.application.features.asset.retire_asset_feature import RetireAssetFeature
from mfm.application.features.asset.retire_asset_feature import RetireAssetRequest
from mfm.application.features.asset.retire_asset_feature import RetireAssetResponse
from mfm.application.features.asset.retire_asset_feature import ValidationException as RetireAssetValidationException
from mfm.application.features.asset.transfer_ownership_feature import TransferOwnershipFeature
from mfm.application.features.asset.transfer_ownership_feature import TransferOwnershipRequest
from mfm.application.features.asset.transfer_ownership_feature import TransferOwnershipResponse
from mfm.application.features.asset.transfer_ownership_feature import ValidationException as TransferOwnershipValidationException
from mfm.application.features.asset.update_asset_feature import BusinessRuleViolation as UpdateAssetBusinessRuleViolation
from mfm.application.features.asset.update_asset_feature import UpdateAssetFeature
from mfm.application.features.asset.update_asset_feature import UpdateAssetRequest
from mfm.application.features.asset.update_asset_feature import UpdateAssetResponse
from mfm.application.features.asset.update_asset_feature import ValidationException as UpdateAssetValidationException
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_status import AssetStatus


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


def test_create_asset_feature_happy_path_response_mapping_and_service_call() -> None:
    asset_id = uuid4()
    service = StubService(
        response=ServiceCreateAssetResponse(
            asset_id=asset_id,
            asset_number="ASSET-FEAT-001",
            name="Feature Asset",
            status=AssetStatus.ACTIVE,
        )
    )
    feature = CreateAssetFeature(service=service)

    response = feature.execute(
        CreateAssetRequest(
            asset_number="ASSET-FEAT-001",
            name="Feature Asset",
            description="Feature test",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Warehouse",
            acquisition_date=date(2026, 1, 1),
        )
    )

    assert isinstance(response, CreateAssetResponse)
    assert isinstance(response.asset_id, UUID)
    assert response.status == "ACTIVE"
    assert service.last_request.asset_number == "ASSET-FEAT-001"


def test_create_asset_feature_validation_duplicate_asset_number_and_rollback_mapping() -> None:
    feature = CreateAssetFeature(service=StubService(response=None))

    with pytest.raises(CreateAssetValidationException):
        feature.execute(
            CreateAssetRequest(
                asset_number="",
                name="Asset",
                description="x",
                category=AssetCategory.OTHER,
                owner_id=None,
                location="Warehouse",
            )
        )

    duplicate_feature = CreateAssetFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate asset number"))
    )
    with pytest.raises(CreateAssetBusinessRuleViolation):
        duplicate_feature.execute(
            CreateAssetRequest(
                asset_number="ASSET-FEAT-002",
                name="Asset",
                description="x",
                category=AssetCategory.OTHER,
                owner_id=None,
                location="Warehouse",
            )
        )

    rollback_feature = CreateAssetFeature(
        service=StubService(error=ServiceRepositoryException("rollback"))
    )
    with pytest.raises(CreateAssetRepositoryException):
        rollback_feature.execute(
            CreateAssetRequest(
                asset_number="ASSET-FEAT-003",
                name="Asset",
                description="x",
                category=AssetCategory.OTHER,
                owner_id=None,
                location="Warehouse",
            )
        )


def test_update_asset_feature_happy_path_response_mapping_and_invalid_state_transition_mapping() -> None:
    asset_id = uuid4()
    service = StubService(
        response=ServiceUpdateAssetResponse(
            asset_id=asset_id,
            name="Updated Asset",
            status=AssetStatus.RETIRED,
        )
    )
    feature = UpdateAssetFeature(service=service)

    response = feature.execute(
        UpdateAssetRequest(asset_id=asset_id, name="Updated Asset")
    )

    assert isinstance(response, UpdateAssetResponse)
    assert response.status == "RETIRED"

    invalid_transition_feature = UpdateAssetFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid state transition"))
    )
    with pytest.raises(UpdateAssetBusinessRuleViolation):
        invalid_transition_feature.execute(
            UpdateAssetRequest(asset_id=uuid4(), name="Blocked Update")
        )


def test_update_asset_feature_validation() -> None:
    feature = UpdateAssetFeature(service=StubService(response=None))

    with pytest.raises(UpdateAssetValidationException):
        feature.execute(UpdateAssetRequest(asset_id=uuid4(), name="   "))


def test_transfer_ownership_feature_happy_path_validation_and_service_call() -> None:
    asset_id = uuid4()
    owner_id = uuid4()
    service = StubService(
        response=ServiceTransferAssetResponse(asset_id=asset_id, owner_id=owner_id)
    )
    feature = TransferOwnershipFeature(service=service)

    response = feature.execute(
        TransferOwnershipRequest(asset_id=asset_id, owner_id=owner_id)
    )

    assert isinstance(response, TransferOwnershipResponse)
    assert response.owner_id == owner_id
    assert service.last_request.owner_id == owner_id

    with pytest.raises(TransferOwnershipValidationException):
        feature.execute(TransferOwnershipRequest(asset_id=asset_id, owner_id="bad"))  # type: ignore[arg-type]


def test_relocate_asset_feature_happy_path_validation_and_response_mapping() -> None:
    asset_id = uuid4()
    service = StubService(
        response=ServiceRelocateAssetResponse(asset_id=asset_id, location="Harbor")
    )
    feature = RelocateAssetFeature(service=service)

    response = feature.execute(RelocateAssetRequest(asset_id=asset_id, location="Harbor"))

    assert isinstance(response, RelocateAssetResponse)
    assert response.location == "Harbor"

    with pytest.raises(RelocateAssetValidationException):
        feature.execute(RelocateAssetRequest(asset_id=asset_id, location="  "))


def test_retire_asset_feature_happy_path_validation_and_invalid_state_transition_mapping() -> None:
    asset_id = uuid4()
    service = StubService(
        response=ServiceRetireAssetResponse(
            asset_id=asset_id,
            status=AssetStatus.RETIRED,
            retired_date=date(2026, 5, 1),
        )
    )
    feature = RetireAssetFeature(service=service)

    response = feature.execute(
        RetireAssetRequest(asset_id=asset_id, retired_on=date(2026, 5, 1))
    )

    assert isinstance(response, RetireAssetResponse)
    assert response.status == "RETIRED"

    with pytest.raises(RetireAssetValidationException):
        feature.execute(RetireAssetRequest(asset_id=asset_id, retired_on="bad"))  # type: ignore[arg-type]

    invalid_transition_feature = RetireAssetFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid state transition"))
    )
    with pytest.raises(RetireAssetBusinessRuleViolation):
        invalid_transition_feature.execute(
            RetireAssetRequest(asset_id=uuid4(), retired_on=date(2026, 5, 1))
        )


def test_dispose_asset_feature_happy_path_validation_and_rollback_mapping() -> None:
    asset_id = uuid4()
    service = StubService(
        response=ServiceDisposeAssetResponse(
            asset_id=asset_id,
            status=AssetStatus.DISPOSED,
            retired_date=date(2026, 6, 1),
        )
    )
    feature = DisposeAssetFeature(service=service)

    response = feature.execute(
        DisposeAssetRequest(asset_id=asset_id, disposed_on=date(2026, 6, 1))
    )

    assert isinstance(response, DisposeAssetResponse)
    assert response.status == "DISPOSED"

    with pytest.raises(DisposeAssetValidationException):
        feature.execute(DisposeAssetRequest(asset_id=asset_id, disposed_on="bad"))  # type: ignore[arg-type]

    invalid_transition_feature = DisposeAssetFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid state transition"))
    )
    with pytest.raises(DisposeAssetBusinessRuleViolation):
        invalid_transition_feature.execute(
            DisposeAssetRequest(asset_id=uuid4(), disposed_on=date(2026, 6, 1))
        )

    rollback_feature = DisposeAssetFeature(
        service=StubService(error=ServiceRepositoryException("rollback"))
    )
    with pytest.raises(DisposeAssetRepositoryException):
        rollback_feature.execute(
            DisposeAssetRequest(asset_id=uuid4(), disposed_on=date(2026, 6, 1))
        )


def test_features_map_service_validation_exception_consistently() -> None:
    create_feature = CreateAssetFeature(
        service=StubService(error=ServiceValidationException("invalid request"))
    )
    with pytest.raises(CreateAssetValidationException):
        create_feature.execute(
            CreateAssetRequest(
                asset_number="ASSET-FEAT-100",
                name="Asset",
                description="x",
                category=AssetCategory.OTHER,
                owner_id=None,
                location="Warehouse",
            )
        )

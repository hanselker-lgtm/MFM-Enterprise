"""Fleet feature facades following Public API Standard."""

from mfm.application.features.fleet.change_vessel_registration_feature import (
    ChangeVesselRegistrationFeature,
    ChangeVesselRegistrationRequest,
    ChangeVesselRegistrationResponse,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    ChangeVesselStatusFeature,
    ChangeVesselStatusRequest,
    ChangeVesselStatusResponse,
)
from mfm.application.features.fleet.create_vessel_feature import (
    CreateVesselFeature,
    CreateVesselRequest,
    CreateVesselResponse,
)
from mfm.application.features.fleet.rename_vessel_feature import (
    RenameVesselFeature,
    RenameVesselRequest,
    RenameVesselResponse,
)
from mfm.application.features.fleet.update_vessel_dimensions_feature import (
    UpdateVesselDimensionsFeature,
    UpdateVesselDimensionsRequest,
    UpdateVesselDimensionsResponse,
)
from mfm.application.features.fleet.update_vessel_feature import (
    UpdateVesselFeature,
    UpdateVesselRequest,
    UpdateVesselResponse,
)

__all__ = [
    "ChangeVesselRegistrationFeature",
    "ChangeVesselRegistrationRequest",
    "ChangeVesselRegistrationResponse",
    "ChangeVesselStatusFeature",
    "ChangeVesselStatusRequest",
    "ChangeVesselStatusResponse",
    "CreateVesselFeature",
    "CreateVesselRequest",
    "CreateVesselResponse",
    "RenameVesselFeature",
    "RenameVesselRequest",
    "RenameVesselResponse",
    "UpdateVesselDimensionsFeature",
    "UpdateVesselDimensionsRequest",
    "UpdateVesselDimensionsResponse",
    "UpdateVesselFeature",
    "UpdateVesselRequest",
    "UpdateVesselResponse",
]

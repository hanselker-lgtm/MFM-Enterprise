"""Fleet domain package."""

from mfm.domain.fleet.exceptions import DuplicateVesselRegistrationError
from mfm.domain.fleet.exceptions import InvalidVesselAssetIdError
from mfm.domain.fleet.exceptions import InvalidVesselDimensionsError
from mfm.domain.fleet.exceptions import InvalidVesselNameError
from mfm.domain.fleet.exceptions import InvalidVesselRegistrationError
from mfm.domain.fleet.exceptions import InvalidVesselStatusTransitionError
from mfm.domain.fleet.exceptions import VesselError
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_dimensions import VesselDimensions
from mfm.domain.fleet.vessel_id import VesselId
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus

__all__ = [
    "DuplicateVesselRegistrationError",
    "InvalidVesselAssetIdError",
    "InvalidVesselDimensionsError",
    "InvalidVesselNameError",
    "InvalidVesselRegistrationError",
    "InvalidVesselStatusTransitionError",
    "Vessel",
    "VesselDimensions",
    "VesselError",
    "VesselId",
    "VesselMaterial",
    "VesselRegistration",
    "VesselStatus",
]

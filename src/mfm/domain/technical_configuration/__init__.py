"""Technical configuration domain package."""

from mfm.domain.technical_configuration.component_link import ComponentLink
from mfm.domain.technical_configuration.component_link_role import ComponentLinkRole
from mfm.domain.technical_configuration.component_replacement_record import (
    ComponentReplacementRecord,
)
from mfm.domain.technical_configuration.exceptions import ComponentLinkNotFoundError
from mfm.domain.technical_configuration.exceptions import DuplicateTechnicalComponentError
from mfm.domain.technical_configuration.exceptions import InvalidChronologyError
from mfm.domain.technical_configuration.exceptions import InvalidComponentLinkError
from mfm.domain.technical_configuration.exceptions import InvalidReplacementRelationError
from mfm.domain.technical_configuration.exceptions import (
    InvalidTechnicalComponentLifecycleError,
)
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentNameError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentStatusError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentTypeError
from mfm.domain.technical_configuration.exceptions import (
    InvalidTechnicalConfigurationStatusTransitionError,
)
from mfm.domain.technical_configuration.exceptions import (
    InvalidTechnicalConfigurationVesselIdError,
)
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalSpecificationError
from mfm.domain.technical_configuration.exceptions import TechnicalComponentAlreadyInstalledError
from mfm.domain.technical_configuration.exceptions import TechnicalComponentNotFoundError
from mfm.domain.technical_configuration.exceptions import TechnicalConfigurationError
from mfm.domain.technical_configuration.identifiers import ComponentLinkId
from mfm.domain.technical_configuration.identifiers import ComponentReplacementRecordId
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId
from mfm.domain.technical_configuration.identifiers import TechnicalConfigurationId
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
)
from mfm.domain.technical_configuration.technical_configuration_status import (
    TechnicalConfigurationStatus,
)
from mfm.domain.technical_configuration.technical_specification import (
    SpecificationEntry,
)
from mfm.domain.technical_configuration.technical_specification import (
    TechnicalSpecification,
)
from mfm.domain.technical_configuration.value_objects import BuildYear
from mfm.domain.technical_configuration.value_objects import ComponentModelName
from mfm.domain.technical_configuration.value_objects import ComponentNotes
from mfm.domain.technical_configuration.value_objects import ManufacturerName
from mfm.domain.technical_configuration.value_objects import ReplacementReason
from mfm.domain.technical_configuration.value_objects import SerialNumber

__all__ = [
    "BuildYear",
    "ComponentLink",
    "ComponentLinkId",
    "ComponentLinkNotFoundError",
    "ComponentLinkRole",
    "ComponentModelName",
    "ComponentNotes",
    "ComponentReplacementRecord",
    "ComponentReplacementRecordId",
    "DuplicateTechnicalComponentError",
    "InvalidChronologyError",
    "InvalidComponentLinkError",
    "InvalidReplacementRelationError",
    "InvalidTechnicalComponentLifecycleError",
    "InvalidTechnicalComponentNameError",
    "InvalidTechnicalComponentStatusError",
    "InvalidTechnicalComponentTypeError",
    "InvalidTechnicalConfigurationStatusTransitionError",
    "InvalidTechnicalConfigurationVesselIdError",
    "InvalidTechnicalSpecificationError",
    "ManufacturerName",
    "ReplacementReason",
    "SerialNumber",
    "SpecificationEntry",
    "TechnicalComponent",
    "TechnicalComponentAlreadyInstalledError",
    "TechnicalComponentId",
    "TechnicalComponentNotFoundError",
    "TechnicalComponentStatus",
    "TechnicalComponentType",
    "TechnicalConfiguration",
    "TechnicalConfigurationError",
    "TechnicalConfigurationId",
    "TechnicalConfigurationStatus",
    "TechnicalSpecification",
]

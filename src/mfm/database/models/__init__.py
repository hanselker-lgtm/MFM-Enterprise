from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.contact_person_model import ContactPersonModel
from mfm.database.models.contact_organisation_model import ContactOrganisationModel
from mfm.database.models.contact_email_model import ContactEmailModel
from mfm.database.models.contact_phone_model import ContactPhoneModel
from mfm.database.models.contact_address_model import ContactAddressModel
from mfm.database.models.contingent_plan_model import ContingentPlanModel
from mfm.database.models.certificate_model import CertificateModel
from mfm.database.models.certificate_compliance_observation_model import (
    CertificateComplianceObservationModel,
)
from mfm.database.models.inventory_item_model import InventoryItemModel
from mfm.database.models.inventory_stock_movement_model import InventoryStockMovementModel
from mfm.database.models.inventory_stock_position_model import InventoryStockPositionModel
from mfm.database.models.member_model import MemberModel
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.database.models.maintenance_plan_model import MaintenancePlanModel
from mfm.database.models.maintenance_record_model import MaintenanceRecordModel
from mfm.database.models.maintenance_requirement_model import MaintenanceRequirementModel
from mfm.database.models.technical_component_link_model import TechnicalComponentLinkModel
from mfm.database.models.technical_component_model import TechnicalComponentModel
from mfm.database.models.technical_component_replacement_model import (
    TechnicalComponentReplacementModel,
)
from mfm.database.models.technical_configuration_model import TechnicalConfigurationModel
from mfm.database.models.vessel_dimensions_model import VesselDimensionsModel
from mfm.database.models.vessel_model import VesselModel
from mfm.database.models.voyage_model import VoyageModel
from mfm.database.models.work_order_model import WorkOrderModel

__all__ = [
    "BaseModel",
    "ContactModel",
    "ContactPersonModel",
    "ContactOrganisationModel",
    "ContactEmailModel",
    "ContactPhoneModel",
    "ContactAddressModel",
    "ContingentPlanModel",
    "CertificateModel",
    "CertificateComplianceObservationModel",
    "InventoryItemModel",
    "InventoryStockPositionModel",
    "InventoryStockMovementModel",
    "MemberModel",
    "MembershipTypeModel",
    "MaintenancePlanModel",
    "MaintenanceRequirementModel",
    "MaintenanceRecordModel",
    "WorkOrderModel",
    "TechnicalConfigurationModel",
    "TechnicalComponentModel",
    "TechnicalComponentLinkModel",
    "TechnicalComponentReplacementModel",
    "VesselDimensionsModel",
    "VesselModel",
    "VoyageModel",
]

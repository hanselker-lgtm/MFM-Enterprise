"""Contact communication domain package."""

from mfm.domain.contact_communication.communication_preference import (
    CommunicationPreference,
)
from mfm.domain.contact_communication.communication_preference import PreferenceFrequency
from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)
from mfm.domain.contact_communication.contact_method import ContactMethod
from mfm.domain.contact_communication.contact_method import ContactMethodType
from mfm.domain.contact_communication.email_address import EmailAddress
from mfm.domain.contact_communication.notification import Notification
from mfm.domain.contact_communication.notification import NotificationStatus
from mfm.domain.contact_communication.phone_number import PhoneNumber
from mfm.domain.contact_communication.postal_address import PostalAddress

__all__ = [
    "CommunicationPreference",
    "ContactCommunicationProfile",
    "ContactMethod",
    "ContactMethodType",
    "EmailAddress",
    "Notification",
    "NotificationStatus",
    "PhoneNumber",
    "PostalAddress",
    "PreferenceFrequency",
]

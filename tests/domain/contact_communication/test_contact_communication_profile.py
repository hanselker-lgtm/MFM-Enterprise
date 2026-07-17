from __future__ import annotations

from uuid import uuid4

import pytest

from mfm.domain.contact_communication.communication_preference import (
    CommunicationPreference,
)
from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)
from mfm.domain.contact_communication.contact_method import ContactMethod
from mfm.domain.contact_communication.contact_method import ContactMethodType
from mfm.domain.contact_communication.email_address import EmailAddress
from mfm.domain.contact_communication.notification import Notification
from mfm.domain.contact_communication.phone_number import PhoneNumber
from mfm.domain.contact_communication.postal_address import PostalAddress


def test_profile_supports_required_capability_components() -> None:
    contact_id = uuid4()
    profile = ContactCommunicationProfile(contact_id=contact_id)

    email_method = ContactMethod(
        method_type=ContactMethodType.EMAIL,
        email=EmailAddress("person@example.com"),
        is_primary=True,
    )
    phone_method = ContactMethod(
        method_type=ContactMethodType.PHONE,
        phone=PhoneNumber("+45 20 30 40 50"),
    )
    postal_method = ContactMethod(
        method_type=ContactMethodType.POSTAL,
        postal=PostalAddress(
            line1="Harbor Street 1",
            postal_code="5700",
            city="Svendborg",
            country="Denmark",
        ),
    )

    profile.add_method(email_method)
    profile.add_method(phone_method)
    profile.add_method(postal_method)

    profile.set_preference(
        CommunicationPreference(
            preferred_method_id=email_method.id,
            allow_marketing=True,
        )
    )

    profile.schedule_notification(
        Notification(
            contact_id=contact_id,
            method_id=email_method.id,
            subject="Welcome",
            message="Communication profile created",
        )
    )

    assert len(profile.methods) == 3
    assert profile.preference is not None
    assert profile.preference.allow_marketing is True
    assert len(profile.notifications) == 1


def test_preference_requires_existing_method() -> None:
    profile = ContactCommunicationProfile(contact_id=uuid4())

    with pytest.raises(ValueError, match="does not exist"):
        profile.set_preference(
            CommunicationPreference(preferred_method_id=uuid4())
        )


def test_notification_requires_matching_contact() -> None:
    contact_id = uuid4()
    profile = ContactCommunicationProfile(contact_id=contact_id)
    email_method = ContactMethod(
        method_type=ContactMethodType.EMAIL,
        email=EmailAddress("person@example.com"),
        is_primary=True,
    )
    profile.add_method(email_method)

    with pytest.raises(ValueError, match="must match"):
        profile.schedule_notification(
            Notification(
                contact_id=uuid4(),
                method_id=email_method.id,
                subject="Mismatch",
                message="Invalid contact",
            )
        )

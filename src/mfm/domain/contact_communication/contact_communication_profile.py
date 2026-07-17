"""Aggregate root for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID

from mfm.domain.contact_communication.communication_preference import CommunicationPreference
from mfm.domain.contact_communication.contact_method import ContactMethod
from mfm.domain.contact_communication.notification import Notification


@dataclass(slots=True)
class ContactCommunicationProfile:
    """Communication profile for one contact."""

    contact_id: UUID
    methods: list[ContactMethod] = field(default_factory=list)
    notifications: list[Notification] = field(default_factory=list)
    preference: CommunicationPreference | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValueError("contact_id must be UUID")
        self.methods = list(self.methods)
        self.notifications = list(self.notifications)

    def add_method(self, method: ContactMethod) -> None:
        if any(item.id == method.id for item in self.methods):
            raise ValueError(f"Contact method {method.id} already exists")

        if method.is_primary:
            for existing in self.methods:
                existing.is_primary = False

        self.methods.append(method)

    def set_preference(self, preference: CommunicationPreference) -> None:
        if not any(item.id == preference.preferred_method_id for item in self.methods):
            raise ValueError(
                f"Preferred method {preference.preferred_method_id} does not exist"
            )
        self.preference = preference

    def schedule_notification(self, notification: Notification) -> None:
        if notification.contact_id != self.contact_id:
            raise ValueError("notification.contact_id must match profile contact_id")
        if not any(item.id == notification.method_id for item in self.methods):
            raise ValueError(f"Contact method {notification.method_id} does not exist")

        self.notifications.append(notification)

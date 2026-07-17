"""Contact method entity for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from uuid import UUID
from uuid import uuid4

from mfm.domain.contact_communication.email_address import EmailAddress
from mfm.domain.contact_communication.phone_number import PhoneNumber
from mfm.domain.contact_communication.postal_address import PostalAddress


class ContactMethodType(str, Enum):
    """Supported contact method channels."""

    EMAIL = "EMAIL"
    PHONE = "PHONE"
    POSTAL = "POSTAL"


@dataclass(slots=True)
class ContactMethod:
    """Contact method that can be used for communication."""

    method_type: ContactMethodType
    id: UUID = field(default_factory=uuid4)
    email: EmailAddress | None = None
    phone: PhoneNumber | None = None
    postal: PostalAddress | None = None
    is_primary: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.method_type, ContactMethodType):
            self.method_type = ContactMethodType(str(self.method_type).upper())

        if self.method_type is ContactMethodType.EMAIL and self.email is None:
            raise ValueError("email method requires email value")
        if self.method_type is ContactMethodType.PHONE and self.phone is None:
            raise ValueError("phone method requires phone value")
        if self.method_type is ContactMethodType.POSTAL and self.postal is None:
            raise ValueError("postal method requires postal value")

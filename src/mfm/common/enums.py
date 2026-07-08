"""
Shared enums.
"""

from enum import Enum


class ContactType(str, Enum):

    PERSON = "PERSON"

    ORGANISATION = "ORGANISATION"

class ContactStatus(str, Enum):

    ACTIVE = "ACTIVE"

    INACTIVE = "INACTIVE"

    ARCHIVED = "ARCHIVED"

    DELETED = "DELETED"


class AddressType(str, Enum):

    HOME = "HOME"

    POSTAL = "POSTAL"

    WORK = "WORK"

    OTHER = "OTHER"


class EmailType(str, Enum):

    PRIVATE = "PRIVATE"

    WORK = "WORK"

    OTHER = "OTHER"


class PhoneType(str, Enum):

    MOBILE = "MOBILE"

    LANDLINE = "LANDLINE"

    WORK = "WORK"

    OTHER = "OTHER"


class RelationType(str, Enum):

    CONTACT_PERSON = "CONTACT_PERSON"

    MEMBER_OF = "MEMBER_OF"

    SUPPLIER = "SUPPLIER"

    SPONSOR = "SPONSOR"

    DONOR = "DONOR"

    AUTHORITY = "AUTHORITY"

    OTHER = "OTHER"
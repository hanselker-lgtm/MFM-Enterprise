"""
Domain exceptions for Contact.
"""

class ContactError(Exception):
    """Base exception for the Contact domain."""


class InvalidEmailError(ContactError):
    """Raised when an e-mail address is invalid."""


class InvalidPhoneError(ContactError):
    """Raised when a phone number is invalid."""


class DuplicatePrimaryEmailError(ContactError):
    """Raised when more than one primary e-mail exists."""


class DuplicatePrimaryPhoneError(ContactError):
    """Raised when more than one primary phone exists."""


class DuplicateContactNumberError(ContactError):
    """Raised when a contact_number already exists."""


class ContactNotFoundException(ContactError):
    """Raised when a contact could not be found."""


class ContactNotFoundError(ContactNotFoundException):
    """Raised when a contact could not be found."""
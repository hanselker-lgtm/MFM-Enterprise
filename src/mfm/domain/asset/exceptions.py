"""Domain exceptions for Asset."""


class AssetError(Exception):
    """Base exception for asset domain errors."""


class InvalidAssetNameError(AssetError):
    """Raised when asset name is missing or invalid."""


class InvalidAssetNumberError(AssetError):
    """Raised when asset number is missing or invalid."""


class DuplicateAssetNumberError(AssetError):
    """Raised when asset number uniqueness is violated."""


class InvalidAssetLocationError(AssetError):
    """Raised when asset location is missing or invalid."""


class InvalidAssetOwnerError(AssetError):
    """Raised when owner identifier is invalid."""


class InvalidAssetDateError(AssetError):
    """Raised when asset date constraints are violated."""


class InvalidAssetStatusTransitionError(AssetError):
    """Raised when asset status transition is not allowed."""


class AssetSerializationError(AssetError):
    """Raised when serialized asset payload is invalid."""

"""Controlled purpose codes for voyages."""

from __future__ import annotations

from enum import StrEnum


class VoyagePurposeCode(StrEnum):
    """Generic voyage purpose classification."""

    OPERATIONAL = "OPERATIONAL"
    TRAINING = "TRAINING"
    PRESERVATION = "PRESERVATION"
    DEMONSTRATION = "DEMONSTRATION"
    TRANSFER = "TRANSFER"
    INSPECTION = "INSPECTION"
    OTHER = "OTHER"
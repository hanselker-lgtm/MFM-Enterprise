"""Event handler protocol for application domain event dispatching."""

from __future__ import annotations

from typing import Protocol

from mfm.common.domain_event import DomainEvent


class EventHandler(Protocol):
    """Contract for synchronous domain event handlers."""

    def handle(self, event: DomainEvent) -> None:
        """Handle a domain event synchronously."""

"""Synchronous dispatcher for domain events."""

from __future__ import annotations

from mfm.application.events.event_handler import EventHandler
from mfm.application.events.event_registry import EventRegistry
from mfm.common.domain_event import DomainEvent


class DomainEventDispatcher:
    """Registers and dispatches domain events to synchronous handlers."""

    def __init__(self, registry: EventRegistry | None = None) -> None:
        self._registry = registry or EventRegistry()

    def register(self, event_type: type[DomainEvent], handler: EventHandler) -> None:
        self._registry.register(event_type, handler)

    def unregister(self, event_type: type[DomainEvent], handler: EventHandler) -> None:
        self._registry.unregister(event_type, handler)

    def dispatch(self, event: DomainEvent) -> None:
        handlers = self._registry.get_handlers(type(event))
        for handler in handlers:
            try:
                handler.handle(event)
            except Exception:
                # Keep dispatching remaining handlers; caller may inspect side-effects.
                continue

    def clear(self) -> None:
        self._registry.clear()

    def has_handlers(self, event_type: type[DomainEvent]) -> bool:
        return self._registry.has_handlers(event_type)

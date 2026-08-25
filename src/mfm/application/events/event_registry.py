"""In-memory event handler registry."""

from __future__ import annotations

from collections import defaultdict

from mfm.application.events.event_handler import EventHandler
from mfm.common.domain_event import DomainEvent


class EventRegistry:
    """Stores event handlers by event type."""

    def __init__(self) -> None:
        self._handlers: dict[type[DomainEvent], list[EventHandler]] = defaultdict(list)

    def register(self, event_type: type[DomainEvent], handler: EventHandler) -> None:
        handlers = self._handlers[event_type]
        if handler not in handlers:
            handlers.append(handler)

    def unregister(self, event_type: type[DomainEvent], handler: EventHandler) -> None:
        handlers = self._handlers.get(event_type)
        if not handlers:
            return

        if handler in handlers:
            handlers.remove(handler)

        if not handlers:
            self._handlers.pop(event_type, None)

    def get_handlers(self, event_type: type[DomainEvent]) -> list[EventHandler]:
        return list(self._handlers.get(event_type, []))

    def clear(self) -> None:
        self._handlers.clear()

    def has_handlers(self, event_type: type[DomainEvent]) -> bool:
        return len(self._handlers.get(event_type, [])) > 0

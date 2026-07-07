"""
Base Aggregate Root.
"""

from __future__ import annotations

from typing import List

from mfm.common.domain_event import DomainEvent


class AggregateRoot:
    """
    Base Aggregate Root supporting Domain Events.
    """

    def __init__(self) -> None:
        self._events: List[DomainEvent] = []
        self.version: int = 1

    def add_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[DomainEvent]:
        events = self._events.copy()
        self._events.clear()
        return events
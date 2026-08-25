from __future__ import annotations

from dataclasses import dataclass

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class MemberEnrolledEvent(DomainEvent):
    member_number: str = ""


class RecordingHandler:
    def __init__(self, sink: list[str], label: str) -> None:
        self._sink = sink
        self._label = label

    def handle(self, event: DomainEvent) -> None:
        _ = event
        self._sink.append(self._label)


class FailingHandler:
    def __init__(self, sink: list[str], label: str) -> None:
        self._sink = sink
        self._label = label

    def handle(self, event: DomainEvent) -> None:
        _ = event
        self._sink.append(self._label)
        raise RuntimeError("boom")


def test_register():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []
    handler = RecordingHandler(sink, "h1")

    dispatcher.register(MemberEnrolledEvent, handler)

    assert dispatcher.has_handlers(MemberEnrolledEvent) is True


def test_unregister():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []
    handler = RecordingHandler(sink, "h1")
    dispatcher.register(MemberEnrolledEvent, handler)

    dispatcher.unregister(MemberEnrolledEvent, handler)

    assert dispatcher.has_handlers(MemberEnrolledEvent) is False


def test_multiple_handlers():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []

    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "h1"))
    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "h2"))

    dispatcher.dispatch(MemberEnrolledEvent(member_number="M-1"))

    assert sink == ["h1", "h2"]


def test_no_handlers():
    dispatcher = DomainEventDispatcher()

    dispatcher.dispatch(MemberEnrolledEvent(member_number="M-1"))

    assert dispatcher.has_handlers(MemberEnrolledEvent) is False


def test_ordering():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []

    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "first"))
    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "second"))
    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "third"))

    dispatcher.dispatch(MemberEnrolledEvent(member_number="M-1"))

    assert sink == ["first", "second", "third"]


def test_duplicate_registration_is_ignored():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []
    handler = RecordingHandler(sink, "h1")

    dispatcher.register(MemberEnrolledEvent, handler)
    dispatcher.register(MemberEnrolledEvent, handler)

    dispatcher.dispatch(MemberEnrolledEvent(member_number="M-1"))

    assert sink == ["h1"]


def test_exception_isolation():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []

    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "before"))
    dispatcher.register(MemberEnrolledEvent, FailingHandler(sink, "failing"))
    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "after"))

    dispatcher.dispatch(MemberEnrolledEvent(member_number="M-1"))

    assert sink == ["before", "failing", "after"]


def test_clear():
    dispatcher = DomainEventDispatcher()
    sink: list[str] = []
    dispatcher.register(MemberEnrolledEvent, RecordingHandler(sink, "h1"))

    dispatcher.clear()

    assert dispatcher.has_handlers(MemberEnrolledEvent) is False

"""Integration tests for webhook events."""

from hypothesis import given

from anaml_client.models.event import Event

from generators import EventGen


@given(EventGen)
def test_event_round_trip(event: Event):
    assert event == Event.from_json(event.to_json())

import datetime

from nostr_toolkit.tests.infra.conftest import assert_json_equals
from nostr_toolkit.domain.events import NostrEvent
from nostr_toolkit.domain.primitives import Hex32, Hex64
from nostr_toolkit.infra.serializers import json_to_event, event_to_json

hex32_one = Hex32("0000000000000000000000000000000000000000000000000000000000000001")
hex64_two = Hex64(
    "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002"
)


def test_text_event_to_json(example_events):
    json_text_event = event_to_json(
        NostrEvent(
            pubkey=hex32_one,
            kind=1,
            created_at=datetime.datetime.fromtimestamp(1),
            tags=[],
            content="foo",
            sig=hex64_two,
        )
    )

    assert_json_equals(json_text_event, example_events[0])


def test_json_to_text_event(example_events):
    nostr_text_event = json_to_event(example_events[0])

    assert nostr_text_event.pubkey == hex32_one
    assert nostr_text_event.kind == 1
    assert nostr_text_event.created_at == datetime.datetime.fromtimestamp(1)
    assert nostr_text_event.tags == []
    assert nostr_text_event.content == "foo"
    assert nostr_text_event.sig == hex64_two

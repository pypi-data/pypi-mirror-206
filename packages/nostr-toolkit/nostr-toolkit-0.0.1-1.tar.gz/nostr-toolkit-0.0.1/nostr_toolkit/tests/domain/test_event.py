import datetime

from nostr_toolkit.domain.events import NostrEvent
from nostr_toolkit.domain.primitives import Hex32, Hex64


def test_nostr_text_event_id_is_serialized_hash():
    event = NostrEvent(
        pubkey=Hex32(
            "db3ff32b3fb818468b7ea2b91b8d4a0485112746f6384630aa1c4a345e80928f"
        ),
        created_at=datetime.datetime.utcfromtimestamp(1680610292),
        kind=1,
        tags=[],
        content="Hello world",
        sig=Hex64(
            "710e945d2e424bfe72815a4a398c11b9bafd2a7f4d37a92a02996bd3b8f3dd7f3da060ee230146241ad2ecfb6932583838153feac47126ac52db346dd1428485"
        ),
    )
    assert event.id == Hex32(
        "a4d73d7407fa9a5a48fffe67663f8e6938406e7dd5e49464bfe83c59f861877d"
    )

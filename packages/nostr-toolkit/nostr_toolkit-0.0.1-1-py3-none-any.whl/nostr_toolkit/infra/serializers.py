import datetime

from nostr_toolkit.domain.events import NostrEvent
from nostr_toolkit.domain.primitives import (
    JSONType,
    Hex32,
    Hex64,
)


def json_to_event(json: JSONType) -> NostrEvent:
    return NostrEvent(
        Hex32(json.get("pubkey")),
        json.get("kind"),
        datetime.datetime.fromtimestamp(json.get("created_at")),
        json.get("tags"),
        json.get("content"),
        Hex64(json.get("sig")),
    )


def event_to_json(nostr_event: NostrEvent) -> JSONType:
    # wrap as str hex instances
    # wrap as int datetime (it is a float)
    return {
        "id": str(nostr_event.id),
        "pubkey": str(nostr_event.pubkey),
        "kind": nostr_event.kind,
        "created_at": int(nostr_event.created_at.timestamp()),
        "tags": nostr_event.tags,
        "content": nostr_event.content,
        "sig": str(nostr_event.sig),
    }

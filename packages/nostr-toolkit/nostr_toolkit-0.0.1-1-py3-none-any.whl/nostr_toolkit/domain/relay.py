from typing import Protocol

from nostr_toolkit.domain.events import NostrEvent


class NostrRelayStorage(Protocol):
    def add_event(self, event: NostrEvent):
        pass

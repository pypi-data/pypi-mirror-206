import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

from nostr_toolkit.domain.primitives import Hex64, Hex32, sha256

NostrKindType = int

class NostrEventTag:
    pass


@dataclass
class NostrEvent:
    pubkey: Hex32
    kind: int
    created_at: datetime
    tags: List[NostrEventTag]
    content: str
    sig: Hex64

    @property
    def id(self) -> Hex32:
        serialized = self._serialize()
        hashed = sha256(serialized.encode("utf-8"))
        return Hex32(str(hashed))

    # Not the same as JSON serialization! This is just for id purposes.
    def _serialize(self) -> str:
        # https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures
        return f'[0,"{self.pubkey}",{self._serialize_created_at()},{self.kind},{self._serialize_tags()},"{self.content}"]'

    def _serialize_tags(self) -> str:
        return json.dumps(self.tags)

    def _serialize_created_at(self) -> int:
        return int(self.created_at.timestamp())

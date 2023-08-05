import hashlib
import string
from typing import List, Dict
from typing_extensions import TypeAlias

from nostr_toolkit.domain.exceptions import InvalidHexError


class Hex:
    """Represents a hexadecimal string"""

    def __init__(self, source: str):
        self._source: str = source
        if not set(self._source).issubset(string.hexdigits):
            raise InvalidHexError()

    def __repr__(self):
        return repr(self._source)

    def __str__(self):
        return self._source

    def __len__(self):
        return len(self._source)

    def __eq__(self, other):
        if hasattr(other, "_source"):
            return self._source.lower() == other._source.lower()
        return False


class Hex32(Hex):
    """Represents a 32-bytes hexadecimal string"""

    def __init__(self, source: str):
        super().__init__(source)
        if not len(self) == 64:
            raise InvalidHexError()


class Hex64(Hex):
    """Represents a 64-bytes hexadecimal string"""

    def __init__(self, source: str):
        super().__init__(source)
        if not len(self) == 128:
            raise InvalidHexError()


def sha256(to_hash) -> Hex:
    return Hex(hashlib.sha256(to_hash).hexdigest())


# https://github.com/python/typing/issues/182
JSONType: TypeAlias = (
    Dict[str, "JSONType"] | List["JSONType"] | str | int | float | bool | None  # type: ignore
)

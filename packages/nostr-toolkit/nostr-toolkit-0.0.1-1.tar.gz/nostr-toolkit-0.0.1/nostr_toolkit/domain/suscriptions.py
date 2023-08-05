from typing import Callable

from nostr_toolkit.domain.exceptions import InvalidSubscriptionId


class SubscriptionId:
    def __init__(self, source):
        self._source = source
        if not source or len(source) > 64:
            raise InvalidSubscriptionId()

    def __repr__(self):
        return self._source


SubscriptionIdProvider = Callable[[], SubscriptionId]


class SubscriptionIdContextManager:
    # noinspection PyUnresolvedReferences
    """
    A context manager with a defined SuscriptionId

    >>> client = NostrClient()
    >>> filters = EventRequestFilters()
    >>> with SubscriptionIdContextManager() as subscription_id:
    >>>    client.request_events(subscription_id, filters)
    """

    def __init__(self, provider: SubscriptionIdProvider):
        self.provider = provider

    def __enter__(self) -> SubscriptionId:
        return self.provider()

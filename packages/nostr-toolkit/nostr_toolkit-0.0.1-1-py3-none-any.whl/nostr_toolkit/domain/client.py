from typing import Protocol, List

from nostr_toolkit.domain.events import NostrEvent
from nostr_toolkit.domain.suscriptions import SubscriptionId


class EventRequestFilters:
    pass


class NostrClient(Protocol):
    def publish_events(self, events: List[NostrEvent]) -> None:
        pass

    def request_events(
        self, subscription_id: SubscriptionId, filters: EventRequestFilters
    ) -> None:
        pass

    def close_subscription(self, subscription_id: SubscriptionId) -> None:
        pass

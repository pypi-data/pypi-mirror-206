class NostrError(Exception):
    pass


class InvalidHexError(NostrError):
    pass


class InvalidSubscriptionId(NostrError):
    pass


class InvalidEventKind(NostrError):
    pass


class UndefinedEventKind(NostrError):
    pass

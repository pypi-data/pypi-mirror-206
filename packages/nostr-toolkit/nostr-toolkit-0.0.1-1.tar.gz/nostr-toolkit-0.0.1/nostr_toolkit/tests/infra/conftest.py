import json
import pathlib
import pytest

from nostr_toolkit.domain.primitives import JSONType


@pytest.fixture
def example_events(request) -> JSONType:
    file = pathlib.Path(request.node.fspath.strpath)
    with file.with_name("example_events.json").open() as f:
        return json.load(f)


def assert_json_equals(json_1: JSONType, json_2: JSONType):
    assert json.dumps(json_1, sort_keys=True) == json.dumps(json_2, sort_keys=True)

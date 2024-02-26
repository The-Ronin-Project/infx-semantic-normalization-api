import pytest
from test.conftest import client, application


def test_map_endpoint(client):
    with pytest.raises(NotImplementedError):
        client.get("/map")

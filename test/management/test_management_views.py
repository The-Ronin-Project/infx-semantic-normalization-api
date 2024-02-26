import pytest
from test.conftest import client, application


def test_load_concept_map_endpoint(client):
    with pytest.raises(NotImplementedError):
        client.get("/load_concept_map")

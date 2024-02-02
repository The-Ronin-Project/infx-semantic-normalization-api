

def test_ping(client):
    response = client.get("/ping")
    assert (response.data.decode('ascii') == "pong")

import pytest

from server.server import app


@pytest.fixture
def client():
    app.app.testing = True
    with app.app.test_client() as c:
        yield c


def test__index_endpoint(client):
    response = client.get('/')
    assert response.data == b'Test data server'


def test__status_endpoint(client):
    response = client.get('/status')
    assert response.status_code == 200


def test__testdata_endpoint(client):
    response = client.get('/testdata')
    assert response.json == {"testdata": {"key A1": "value A1", "key B1": "value B1", "key C1": "value C1"}}
    response = client.get('/testdata')
    assert response.json == {"testdata": {"key A2": "value A2", "key B2": "value B2", "key C2": "value C2"}}
    response = client.get('/testdata')
    assert response.json == {"testdata": {"key A1": "value A1", "key B1": "value B1", "key C1": "value C1"}}

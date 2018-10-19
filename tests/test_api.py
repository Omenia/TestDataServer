import pytest

from source.server import app


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

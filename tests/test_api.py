import os
from datetime import datetime

import pytest
from freezegun import freeze_time

from server.testdataserver import app
import server.database as db


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as c:
        yield c


@pytest.fixture(scope='function')
def create_database_setup(request):
    def teardown():
        os.remove(os.path.join(basedir, 'testitem.db'))
        if os.path.exists(os.path.join(basedir, 'testitem_orig.db')):
            os.rename(
                os.path.join(basedir, 'testitem_orig.db'), os.path.join(basedir, 'testitem.db')
            )

    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if os.path.exists(os.path.join(basedir, 'testitem.db')):
        os.rename(os.path.join(basedir, 'testitem.db'), os.path.join(basedir, 'testitem_orig.db'))

    # todo: testdata needs to be set differently to database when configuring testdata is done from GUI
    with freeze_time((datetime(2018, 1, 1, hour) for hour in range(1, 3))):
        db.create()

    request.addfinalizer(teardown)


def test__index_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200


def test__status_endpoint(client):
    response = client.get('/api/v1/status')
    assert response.status_code == 200


# todo: test will break when configured from GUI is implemented
def test__testdata_next_endpoint(client, create_database_setup):
    datetimes = (datetime(2018, 1, 1, hour) for hour in range(3, 6))
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/next')
        assert response.json == {
            "testdata": {
                "item": "{'key A1': 'value A1', 'key B1': 'value B1', 'key C1': 'value C1'}",
                "status": "available",
                "timestamp": "2018-01-01T03:00:00Z",
            }
        }
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/next')
        assert response.json == {
            "testdata": {
                "item": "{'key A2': 'value A2', 'key B2': 'value B2', 'key C2': 'value C2'}",
                "status": "available",
                "timestamp": "2018-01-01T04:00:00Z",
            }
        }
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/next')
        assert response.json == {
            "testdata": {
                "item": "{'key A1': 'value A1', 'key B1': 'value B1', 'key C1': 'value C1'}",
                "status": "available",
                "timestamp": "2018-01-01T05:00:00Z",
            }
        }


# todo: test will break when configured from GUI is implemented
def test__testdata_endpoint(client, create_database_setup):
    # todo: workaround until configuration from GUI is implemented
    datetimes = (datetime(2018, 1, 1, hour) for hour in range(3, 5))
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/next')
        assert response.json == {
            "testdata": {
                "item": "{'key A1': 'value A1', 'key B1': 'value B1', 'key C1': 'value C1'}",
                "status": "available",
                "timestamp": "2018-01-01T03:00:00Z",
            }
        }
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/next')
        assert response.json == {
            "testdata": {
                "item": "{'key A2': 'value A2', 'key B2': 'value B2', 'key C2': 'value C2'}",
                "status": "available",
                "timestamp": "2018-01-01T04:00:00Z",
            }
        }
    # end of workaround

    response = client.get('/api/v1/testdata')
    print(response.json)
    assert response.json == {
        "testdata": {
            "setti": [
                {
                    "item": "{'key A1': 'value A1', 'key B1': 'value B1', 'key C1': 'value C1'}",
                    "status": "available",
                    "timestamp": "2018-01-01T03:00:00Z",
                },
                {
                    "item": "{'key A2': 'value A2', 'key B2': 'value B2', 'key C2': 'value C2'}",
                    "status": "available",
                    "timestamp": "2018-01-01T04:00:00Z",
                },
            ]
        }
    }

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

    db.create()
    datetimes = (datetime(2018, 1, 1, hour) for hour in range(1, 3))
    with freeze_time(datetimes):
        db.add_testdata_to_db(
            {
                'name': 'test',
                'items': '{"username": "user1", "password": "passwd", "email": "user1@example.com"}',
            }
        )
    with freeze_time(datetimes):
        db.add_testdata_to_db(
            {
                'name': 'test',
                'items': '{"username": "user2", "password": "passwd", "email": "user2@example.com"}',
            }
        )

    request.addfinalizer(teardown)


def test__index_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200


def test__status_endpoint(client):
    response = client.get('/api/v1/status')
    assert response.status_code == 200


# todo: issue-34
def test__testdata_next_endpoint(client, create_database_setup):
    datetimes = (datetime(2018, 1, 1, hour) for hour in range(3, 6))
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/test')
        assert response.json == {
            "testdata": {
                "item": '{"username": "user1", "password": "passwd", "email": "user1@example.com"}',
                "status": "available",
                "timestamp": "2018-01-01T03:00:00Z",
            }
        }
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/test')
        assert response.json == {
            "testdata": {
                "item": '{"username": "user2", "password": "passwd", "email": "user2@example.com"}',
                "status": "available",
                "timestamp": "2018-01-01T04:00:00Z",
            }
        }
    with freeze_time(datetimes):
        response = client.get('/api/v1/testdata/test')
        assert response.json == {
            "testdata": {
                "item": '{"username": "user1", "password": "passwd", "email": "user1@example.com"}',
                "status": "available",
                "timestamp": "2018-01-01T05:00:00Z",
            }
        }


# todo: issue-34
def test__testdata_endpoint(client, create_database_setup):
    response = client.get('/api/v1/testdata')
    assert response.json == {
        "testdata": {
            "test": [
                {
                    "item": '{"username": "user1", "password": "passwd", "email": "user1@example.com"}',
                    "status": "available",
                    "timestamp": "2018-01-01T01:00:00Z",
                },
                {
                    "item": '{"username": "user2", "password": "passwd", "email": "user2@example.com"}',
                    "status": "available",
                    "timestamp": "2018-01-01T02:00:00Z",
                },
            ]
        }
    }

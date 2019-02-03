import os
from pathlib import Path

import pytest

import database


@pytest.fixture(scope='function')
def create_database_setup(request):
    def teardown():
        os.remove(os.path.join(basedir, 'testitem.db'))
        if os.path.exists(os.path.join(basedir, 'testitem_orig.db')):
            os.rename(
                os.path.join(basedir, 'testitem_orig.db'), os.path.join(basedir, 'testitem.db')
            )

    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db'))
    if os.path.exists(os.path.join(basedir, 'testitem.db')):
        os.rename(os.path.join(basedir, 'testitem.db'), os.path.join(basedir, 'testitem_orig.db'))

    request.addfinalizer(teardown)


@pytest.fixture(scope='function')
def database_exists_setup(request):
    def teardown():
        os.remove(db_file)

    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/testitem.db'))
    if not os.path.exists(db_file):
        Path(db_file).touch()
        request.addfinalizer(teardown)


def test__create_database(create_database_setup):
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/testitem.db'))
    assert not os.path.exists(db_file)
    database.setup()
    assert os.path.exists(db_file)


def test__database_exists(database_exists_setup, mocker):
    m = mocker.Mock()
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/testitem.db'))
    assert os.path.exists(db_file)
    database.setup()
    m.create.assert_not_called()

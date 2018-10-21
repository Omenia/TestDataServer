import pytest

import server


@pytest.fixture(scope='function')
def missing_config_file_setup(request):
    def teardown():
        server.app.app.config['TEST_DATA_CONFIG'] = 'test-data-config-example.txt'

    server.app.app.config['TEST_DATA_CONFIG'] = 'dummy-file'

    request.addfinalizer(teardown)


@pytest.fixture(scope='function')
def missing_test_data_config_variable_setup(request):
    def teardown():
        server.app.app.config['TEST_DATA_CONFIG'] = 'test-data-config-example.txt'

    server.app.app.config.pop('TEST_DATA_CONFIG')
    request.addfinalizer(teardown)


def test__set_test_data_items__ok():
    assert server.set_test_data_items() == []


def test__set_test_data_items__file_not_found(missing_config_file_setup):
    with pytest.raises(SystemExit, match=r'^ERROR: dummy-file defined by TEST_DATA_CONFIG is not a file$'):
        server.set_test_data_items()


def test__set_test_data_items__test_data_config_variable_missing(missing_test_data_config_variable_setup):
    with pytest.raises(SystemExit, match=r'^ERROR: TEST_DATA_CONFIG variable not defined in config.py$'):
        server.set_test_data_items()

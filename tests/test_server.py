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


@pytest.fixture(scope='function')
def invalid_json_setup(request, tmp_path):
    def teardown():
        server.app.app.config['TEST_DATA_CONFIG'] = 'test-data-config-example.txt'

    d = tmp_path
    f = d / "config-file.txt"
    f.write_text('invalid json')
    server.app.app.config['TEST_DATA_CONFIG'] = f

    request.addfinalizer(teardown)


def test__set_test_data_items__ok():
    assert server.set_test_data_items() == [{"key A1": "value A1", "key B1": "value B1", "key C1": "value C1"},
                                            {"key A2": "value A2", "key B2": "value B2", "key C2": "value C2"}]


def test__set_test_data_items__file_not_found(missing_config_file_setup):
    with pytest.raises(SystemExit, match=r'^ERROR: dummy-file defined by TEST_DATA_CONFIG is not a file$'):
        server.set_test_data_items()


def test__set_test_data_items__test_data_config_variable_missing(missing_test_data_config_variable_setup):
    with pytest.raises(SystemExit, match=r'^ERROR: TEST_DATA_CONFIG variable not defined in config.py$'):
        server.set_test_data_items()


def test__set_test_data_items__invalid_json(invalid_json_setup):
    with pytest.raises(SystemExit, match=r'^ERROR: Invalid json for test data item \(invalid json\)$'):
        server.set_test_data_items()

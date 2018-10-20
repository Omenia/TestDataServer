import server


def test__test_data_config_path():
    assert server.TEST_DATA_CONFIG == '/path/to/test/data/configuration/file'

import sys
import os.path
import json


# todo: to be removed when test data items are set with GUI
def set_test_data_items(app):
    try:
        path = app.app.config['TEST_DATA_CONFIG']
        if not os.path.isfile(os.path.abspath(path)):
            sys.exit(f'ERROR: {path} defined by TEST_DATA_CONFIG is not a file')
    except KeyError:
        sys.exit('ERROR: TEST_DATA_CONFIG variable not defined in config.py')

    with open(path, 'r') as f:
        items = f.readlines()

    test_data_items = []
    for item in items:
        try:
            test_data_items.append(json.loads(item))
        except ValueError:
            sys.exit(f'ERROR: Invalid json for test data item ({item})')

    return test_data_items

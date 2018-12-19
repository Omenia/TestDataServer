import sys
import os.path
import json

import database


ITEMS = None


def get_testdata_next():
    return {"testdata": database.get_testdata_next()}


# todo: to be removed when test data items are set with GUI
def set_test_data_items(app):
    global ITEMS
    try:
        path = app.config['TEST_DATA_CONFIG']
        if not os.path.isfile(os.path.abspath(path)):
            sys.exit(f'ERROR: {path} defined by TEST_DATA_CONFIG is not a file')
    except KeyError:
        sys.exit('ERROR: TEST_DATA_CONFIG variable not defined in config.py')

    with open(path, 'r') as f:
        items = f.readlines()

    ITEMS = []
    for item in items:
        try:
            ITEMS.append(json.loads(item))
        except ValueError:
            sys.exit(f'ERROR: Invalid json for test data item ({item})')


# todo: to be removed when test data items are set with GUI
def get_ITEMS():
    global ITEMS
    return ITEMS


def get_testdata():
    return {"testdata": database.get_testdata()}

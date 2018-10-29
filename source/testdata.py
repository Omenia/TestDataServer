import sys
import os.path
import json


ITEMS = None


def read():
    # todo: ITEMS handling to be removed when db is used
    global ITEMS
    item = ITEMS.pop(0)
    ITEMS.append(item)
    return {"testdata": item}


# todo: to be removed when test data items are set with GUI
def set_test_data_items(app):
    global ITEMS
    try:
        path = app.app.config['TEST_DATA_CONFIG']
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

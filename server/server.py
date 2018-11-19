import sys
import os.path
import json

import connexion
from flask import render_template


# todo: this should be moved to separate file when database is taken into use
def read_test_data():
    item = TEST_DATA_ITEMS.pop(0)
    TEST_DATA_ITEMS.append(item)
    return {"testdata": item}


def set_test_data_items():
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


app = connexion.App(__name__, specification_dir='./', static_folder='templates/static', template_folder='./templates', static_url_path='')

app.add_api('swagger.yml')

app.app.config.from_object('config')
TEST_DATA_ITEMS = set_test_data_items()


@app.route('/')
def home():
    return render_template('app.html')
    # return 'Test data server'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

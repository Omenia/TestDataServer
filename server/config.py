import os.path

import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(
    __name__,
    specification_dir='./',
    static_folder='templates/static',
    template_folder='./templates',
    static_url_path='',
)

connex_app.add_api('swagger.yml')

app = connex_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, '../testitem.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# todo: remove when test items are configured from GUI
app.config['TEST_DATA_CONFIG'] = 'test-data-config-example.txt'

db = SQLAlchemy(app)

ma = Marshmallow(app)


# todo: remove when test items are configured from GUI
def get_test_data_config_file():
    return TEST_DATA_CONFIG

import connexion
from flask import render_template

import database
import testdata

app = connexion.App(__name__, specification_dir='./', static_folder='templates/static', template_folder='./templates',
                    static_url_path='')

app.add_api('swagger.yml')

app.app.config.from_object('config')
testdata.set_test_data_items(app)
database.setup()


@app.route('/')
def home():
    return render_template('app.html')
    # return 'Test data server'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

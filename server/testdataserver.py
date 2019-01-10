from flask import render_template

import database
import testdata
from config import app


testdata.set_test_data_items(app)
database.setup()


@app.route('/')
def home():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

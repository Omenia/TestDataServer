from flask import render_template

import database
from config import app


database.setup()


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/configuration')
def configuration():
    return render_template('configuration.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

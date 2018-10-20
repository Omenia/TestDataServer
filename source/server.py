import connexion

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

app.app.config.from_object('config')
TEST_DATA_CONFIG = app.app.config['TEST_DATA_CONFIG']


@app.route('/')
def home():
    return 'Test data server'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

import config
import database
import testdata


app = config.connex_app
app.add_api('swagger.yml')

app.app.config.from_object('config')
testdata.set_test_data_items(app)
database.setup()


@app.route('/')
def home():
    return 'Test data server'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

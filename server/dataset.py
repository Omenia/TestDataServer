import database


def post_dataset(body):
    database.add_testdata_to_db(body)

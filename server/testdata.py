import database


def get_testdata_next(dataset):
    return {"testdata": database.get_testdata_next(dataset)}


def get_testdata():
    return {"testdata": database.get_testdata()}


def post_dataset(body):
    database.add_testdata_to_db(body.get('dataset'), body.get('items'))


def delete_dataset(dataset):
    database.delete_dataset(dataset)


def delete_dataset_item(dataset, item):
    database.delete_dataset_item(dataset, item)

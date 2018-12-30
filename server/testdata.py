import database


def get_testdata_next(dataset):
    return {"testdata": database.get_testdata_next(dataset)}


def get_testdata():
    return {"testdata": database.get_testdata()}

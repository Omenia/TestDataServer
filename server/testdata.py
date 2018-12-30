import database


def get_testdata_next():
    return {"testdata": database.get_testdata_next()}


def get_testdata():
    return {"testdata": database.get_testdata()}

import os.path
from datetime import datetime

from config import db
from models import TestItem
from testdata import get_ITEMS


def setup():
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testitem.db'))
    if not os.path.exists(db_file):
        create()


def create():
    db.create_all()
    db.session.commit()
    add_testdata_to_db()  # todo: remove when testdata is set from GUI


# todo: remove when testdata is set from GUI
def add_testdata_to_db():
    items = get_ITEMS()
    for item in items:
        # todo: dataset 'setti' is now hard coded
        testitem = TestItem(
            dataset='setti', item=str(item), status='available', timestamp=datetime.now()
        )
        db.session.add(testitem)
    db.session.commit()


def get_all_testdata():
    testdata = {}
    for row in db.session.query(TestItem, TestItem.dataset).order_by(TestItem.timestamp).all():
        data = {
            'item': row.TestItem.item,
            'status': row.TestItem.status,
            'timestamp': row.TestItem.timestamp,
        }
        if row.TestItem.dataset not in testdata:
            testdata[row.TestItem.dataset] = [data]
        else:
            testdata[row.TestItem.dataset].append(data)

    return testdata


def get_testdata():
    item = db.session.query(TestItem, TestItem.dataset).order_by(TestItem.timestamp).first()
    item.TestItem.timestamp = datetime.now()
    db.session.commit()
    return {
        'item': item.TestItem.item,
        'status': item.TestItem.status,
        'timestamp': item.TestItem.timestamp,
    }
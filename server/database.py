import os.path
from datetime import datetime

from config import db
from models import TestItem


def setup():
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../testitem.db'))
    if not os.path.exists(db_file):
        create()


def create():
    db.create_all()
    db.session.commit()


def get_testdata():
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


def get_testdata_next(dataset):
    item = (
        db.session.query(TestItem, TestItem.dataset)
        .filter(TestItem.dataset == dataset)
        .order_by(TestItem.timestamp)
        .first()
    )
    item.TestItem.timestamp = datetime.now()
    db.session.commit()
    return {
        'item': item.TestItem.item,
        'status': item.TestItem.status,
        'timestamp': item.TestItem.timestamp,
    }


def add_testdata_to_db(dataset, items):
    for item in items:
        testitem = TestItem(
            dataset=dataset,
            item=str(item),
            status='available',
            timestamp=datetime.now(),
        )
        db.session.add(testitem)
    db.session.commit()


def delete_dataset(dataset):
    db.session.query(TestItem.dataset).filter(TestItem.dataset == dataset).delete()
    db.session.commit()


def delete_dataset_item(dataset, item):
    db.session.query(TestItem.item).filter(TestItem.item == item).filter(TestItem.dataset == dataset).delete()
    db.session.commit()

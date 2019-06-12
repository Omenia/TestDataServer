import os.path
from datetime import datetime

from sqlalchemy import func

from config import db
from models import Item, Dataset


def setup():
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/testitem.db'))
    if not os.path.exists(db_file):
        create()


def create():
    db.create_all()
    db.session.commit()
    db.session.close()


def get_testdata():
    testdata = []
    for row_d in db.session.query(Dataset, Dataset.name).all():
        items = []
        for row in (
            db.session.query(Item, Item.dataset_name)
            .filter(Item.dataset_name == row_d.Dataset.name)
            .order_by(Item.timestamp)
            .all()
        ):
            items.append(
                {'item': row.Item.item, 'status': row.Item.status, 'timestamp': row.Item.timestamp}
            )
        testdata.append(
            {'dataset': row_d.Dataset.name, 'datatype': row_d.Dataset.datatype, 'items': items}
        )

    return testdata


def get_testdata_next(dataset):
    rows = (
        db.session.query(Dataset, Dataset.name, Dataset.datatype)
        .filter(Dataset.name == dataset)
        .first()
    )
    if not rows:
        return 'does not exist'

    if rows.datatype == 'next':
        item = (
            db.session.query(Item, Item.dataset_name)
            .filter(Item.dataset_name == dataset)
            .order_by(Item.timestamp)
            .first()
        )
        item.Item.timestamp = datetime.now()
        db.session.commit()
        return {
            'item': item.Item.item,
            'status': item.Item.status,
            'timestamp': item.Item.timestamp,
        }
    elif rows.datatype == 'random':
        item = (
            db.session.query(Item, Item.dataset)
            .filter(Item.dataset_name == dataset)
            .order_by(func.random())
            .first()
        )
        return {
            'item': item.Item.item,
            'status': item.Item.status,
            'timestamp': item.Item.timestamp,
        }


def add_testdata_to_db(dataset, items, datatype):
    count = db.session.query(Dataset, Dataset.name).filter(Dataset.name == dataset).all()
    if len(count) > 0:
        return 'exists'

    new_dataset = Dataset(name=dataset, datatype=datatype)
    for item in items:
        testitem = Item(
            dataset_name=dataset, item=str(item), status='available', timestamp=datetime.now()
        )
        new_dataset.items.append(testitem)
        db.session.add(testitem)
    db.session.add(new_dataset)
    db.session.commit()
    return 'added'


def _delete_testdata_data(count):
    if count == 0:
        return 'does not exist'
    db.session.commit()
    return 'deleted'


def delete_dataset(dataset):
    count = db.session.query(Item.dataset_name).filter(Item.dataset_name == dataset).delete()
    _delete_testdata_data(count)
    count = db.session.query(Dataset.name).filter(Dataset.name == dataset).delete()
    return _delete_testdata_data(count)


def delete_dataset_item(dataset, item):
    count = (
        db.session.query(Item.item)
        .filter(Item.item == item)
        .filter(Item.dataset_name == dataset)
        .delete()
    )
    return _delete_testdata_data(count)


def add_item_to_db(dataset, item):
    count = db.session.query(Dataset, Dataset.name).filter(Dataset.name == dataset).all()
    if len(count) == 0:
        return 'dataset does not exist'

    testitem = Item(
            dataset_name=dataset, item=str(item), status='available', timestamp=datetime.now()
        )
    db.session.add(testitem)
    db.session.commit()
    return 'added'

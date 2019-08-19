import os.path
import json
from datetime import datetime, timedelta

from sqlalchemy import func

from config import db
from models import Item, Dataset, Settings


def setup():
    db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db/testitem.db'))
    if not os.path.exists(db_file):
        create()


def create():
    db.create_all()
    db.session.add(Settings())
    db.session.commit()
    db.session.close()


def get_testdata():
    testdata = []
    for row in db.session.query(Dataset, Dataset.name).all():
        testdata.append(
            {
                'dataset': row.Dataset.name,
                'datatype': row.Dataset.datatype,
                'items': _get_items(row.Dataset.name, Item.item),
            }
        )
    return testdata


def _get_items(dataset_name, order):
    items = []
    for row in (
        db.session.query(Item, Item.dataset_name)
        .filter(Item.dataset_name == dataset_name)
        .order_by(order)
        .all()
    ):
        items.append(
            {'item': row.Item.item, 'status': row.Item.status, 'timestamp': row.Item.timestamp}
        )
    return items


def _get_item(dataset, order):
    return (
        db.session.query(Item, Item.dataset_name)
        .filter(Item.dataset_name == dataset)
        .filter(Item.status == 'available')
        .order_by(order)
        .first()
    )


def get_testdata_next(dataset):
    rows = (
        db.session.query(Dataset, Dataset.name, Dataset.datatype)
        .filter(Dataset.name == dataset)
        .first()
    )
    if not rows:
        return None
    item = _get_item(dataset, {'next': Item.timestamp, 'random': func.random()}[rows.datatype])
    if not item:
        return 'no items'
    if rows.datatype == 'next':
        settings = db.session.query(Settings, Settings.use_status).first()
        if settings.Settings.use_status:
            item.Item.status = 'reserved'
    item.Item.timestamp = datetime.now()
    db.session.commit()
    return {'item': item.Item.item, 'status': item.Item.status, 'timestamp': item.Item.timestamp}


def add_testdata_to_db(dataset, items, datatype):
    count = db.session.query(Dataset, Dataset.name).filter(Dataset.name == dataset).all()
    if len(count) > 0:
        return 'exists'

    new_dataset = Dataset(name=dataset, datatype=datatype)
    for item in items:
        testitem = Item(
            dataset_name=dataset,
            item=json.dumps(item),
            status='available',
            timestamp=datetime.now(),
        )
        new_dataset.items.append(testitem)
        db.session.add(testitem)
    db.session.add(new_dataset)
    db.session.commit()
    return 'added'


def _commit_if_existing(count):
    if count == 0:
        return None
    db.session.commit()
    return 'commited'


def delete_dataset(dataset):
    item_result = db.session.query(Item.dataset_name).filter(Item.dataset_name == dataset).delete()
    _commit_if_existing(item_result)
    dataset_result = db.session.query(Dataset.name).filter(Dataset.name == dataset).delete()
    return _commit_if_existing(dataset_result)


def delete_dataset_item(dataset, item):
    result = 0
    items = db.session.query(Item, Item.dataset_name).filter(Item.dataset_name == dataset).all()
    for db_item in items:
        if json.loads(item) == json.loads(db_item.Item.item):
            result = (
                db.session.query(Item.item)
                .filter(Item.item == json.dumps(db_item.Item.item))
                .filter(Item.dataset_name == dataset)
                .delete()
            )
            break
    return _commit_if_existing(result)


def add_item_to_db(dataset, item):
    count = db.session.query(Dataset, Dataset.name).filter(Dataset.name == dataset).all()
    if len(count) == 0:
        return None

    testitem = Item(
        dataset_name=dataset, item=str(item), status='available', timestamp=datetime.now()
    )
    db.session.add(testitem)
    db.session.commit()
    return 'added'


def update_item_status(dataset, item, status):
    found_item = False
    items = db.session.query(Item, Item.dataset_name).filter(Item.dataset_name == dataset).all()
    for db_item in items:
        if json.loads(item) == json.loads(db_item.Item.item):
            found_item = (
                db.session.query(Item, Item.status)
                .filter(Item.item == json.dumps(db_item.Item.item))
                .filter(Item.dataset_name == dataset)
                .first()
            )
            break

    if not found_item:
        return None
    found_item.Item.status = status
    db.session.commit()
    return 'updated'


def get_settings():
    settings = db.session.query(Settings, Settings.use_status).first()
    return {
        'use_status': settings.Settings.use_status,
        'use_quarantine': settings.Settings.use_quarantine,
        'timeout': str(settings.Settings.timeout),
    }


def update_settings(use_status, use_quarantine, timeout):
    try:
        time_list = timeout.split(':')
        timeout_delta = timedelta(
            hours=int(time_list[0]), minutes=int(time_list[1]), seconds=int(time_list[2])
        )
    except (IndexError, ValueError):
        return 'timeout error'
    settings = db.session.query(Settings, Settings.use_status).first()
    settings.Settings.use_status = use_status
    settings.Settings.use_quarantine = use_quarantine
    settings.Settings.timeout = timeout_delta
    db.session.commit()
    return 'updated'


def quarantine_items():
    settings = db.session.query(Settings, Settings.use_status).first()
    if not settings.Settings.use_quarantine:
        return
    for item in db.session.query(Item, Item.dataset_name).filter(Item.status == 'reserved').all():
        if item.Item.timestamp + settings.Settings.timeout < datetime.now():
            update_item_status(item.Item.dataset_name, item.Item.item, 'quarantined')

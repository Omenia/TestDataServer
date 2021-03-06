from http import HTTPStatus
import urllib.parse
import json

import database


def _set_response(status, message):
    return (
        {'detail': message, 'status': status.value, 'title': status.phrase, 'type': 'about:blank'},
        status.value,
    )


def _check_json(item):
    try:
        json.loads(item)
    except (json.decoder.JSONDecodeError, TypeError):
        return False
    return True


def get_testdata_next(dataset):
    database.quarantine_items()
    dataset = database.get_testdata_next(dataset)
    if not dataset:
        return _set_response(HTTPStatus.NOT_FOUND, 'dataset does not exist')
    elif dataset == 'no items':
        return _set_response(HTTPStatus.CONFLICT, 'no items available')
    return dataset


def get_testdata():
    database.quarantine_items()
    return {"testdata": database.get_testdata()}


def post_dataset(body):
    if body.get('datatype') not in ['next', 'random']:
        return _set_response(HTTPStatus.BAD_REQUEST, "unsupported 'datatype'")
    for item in body.get('items'):
        if not _check_json(json.dumps(item)):
            return _set_response(HTTPStatus.BAD_REQUEST, "item is not json")
    status = database.add_testdata_to_db(
        body.get('dataset').strip(), body.get('items'), body.get('datatype')
    )
    if status == 'added':
        return _set_response(HTTPStatus.CREATED, '')
    elif status == 'exists':
        return _set_response(HTTPStatus.CONFLICT, 'dataset exists already')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')


def _deletion_response(status, searched):
    if status == 'commited':
        return _set_response(HTTPStatus.OK, '')
    elif not status:
        return _set_response(HTTPStatus.NOT_FOUND, f'{searched} does not exist')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')


def delete_dataset(dataset):
    status = database.delete_dataset(dataset.strip())
    return _deletion_response(status, 'dataset')


def delete_dataset_item(dataset, item):
    if not _check_json(item):
        return _set_response(HTTPStatus.BAD_REQUEST, "item is not json")
    status = database.delete_dataset_item(dataset.strip(), urllib.parse.unquote(item))
    return _deletion_response(status, 'dataset item')


def post_dataset_item(dataset, item):
    if not _check_json(item):
        return _set_response(HTTPStatus.BAD_REQUEST, "item is not json")
    status = database.add_item_to_db(dataset, urllib.parse.unquote(item))
    if status == 'added':
        return _set_response(HTTPStatus.CREATED, '')
    elif not status:
        return _set_response(HTTPStatus.NOT_FOUND, 'dataset does not exist')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')


def put_dataset_item_status(dataset, item, body):
    if body.get('status') not in ['available', 'out of use']:
        return _set_response(HTTPStatus.BAD_REQUEST, "unsupported 'status'")
    if not _check_json(item):
        return _set_response(HTTPStatus.BAD_REQUEST, "item is not json")
    status = database.update_item_status(dataset, urllib.parse.unquote(item), body.get('status'))
    if status == 'updated':
        return _set_response(HTTPStatus.OK, '')
    elif not status:
        return _set_response(HTTPStatus.NOT_FOUND, 'item does not exist')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')


def get_settings():
    return {"settings": database.get_settings()}


def put_settings(body):
    status = database.update_settings(
        body.get('use_status'), body.get('use_quarantine'), body.get('timeout')
    )
    if status == 'updated':
        return _set_response(HTTPStatus.OK, '')
    elif status == 'timeout error':
        return _set_response(HTTPStatus.BAD_REQUEST, 'Incorrect timeout syntax')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')

from http import HTTPStatus

import database


def _set_response(status, message):
    return (
        {'detail': message, 'status': status.value, 'title': status.phrase, 'type': 'about:blank'},
        status.value,
    )


def get_testdata_next(dataset):
    dataset = database.get_testdata_next(dataset)
    if not dataset:
        return _set_response(HTTPStatus.NOT_FOUND, 'dataset does not exist')
    return {"testdata": dataset}


def get_testdata():
    return {"testdata": database.get_testdata()}


def post_dataset(body):
    if body.get('datatype') not in ['next', 'random']:
        return _set_response(HTTPStatus.BAD_REQUEST, "unsupported 'datatype'")
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
    status = database.delete_dataset_item(dataset.strip(), item)
    return _deletion_response(status, 'dataset item')


def post_dataset_item(dataset, item):
    status = database.add_item_to_db(dataset, item)
    if status == 'added':
        return _set_response(HTTPStatus.CREATED, '')
    elif not status:
        return _set_response(HTTPStatus.NOT_FOUND, 'dataset does not exist')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')


def put_dataset_item_status(dataset, item, body):
    if body.get('status') not in ['available', 'out of use']:
        return _set_response(HTTPStatus.BAD_REQUEST, "unsupported 'status'")
    status = database.update_item_status(dataset, item, body.get('status'))
    if status == 'updated':
        return _set_response(HTTPStatus.CREATED, '')
    elif not status:
        return _set_response(HTTPStatus.NOT_FOUND, 'item does not exist')
    else:
        return _set_response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Unknown error')

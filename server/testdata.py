import database


def get_testdata_next(dataset):
    dataset = database.get_testdata_next(dataset)
    if dataset == 'does not exist':
        return (
            {
                'detail': 'dataset does not exist',
                'status': 404,
                'title': 'Not Found',
                'type': 'about:blank',
            },
            404,
        )
    return {"testdata": dataset}


def get_testdata():
    return {"testdata": database.get_testdata()}


def post_dataset(body):
    if body.get('datatype') not in ['next', 'random']:
        return (
            {
                'detail': "unsupported 'datatype'",
                'status': 400,
                'title': 'Bad Request',
                'type': 'about:blank',
            },
            400,
        )
    status = database.add_testdata_to_db(
        body.get('dataset').strip(), body.get('items'), body.get('datatype')
    )
    if status == 'added':
        return '', 201
    elif status == 'exists':
        return (
            {
                'detail': "dataset exists already",
                'status': 409,
                'title': 'Conflict',
                'type': 'about:blank',
            },
            409,
        )

    else:
        return '', 500


def _deletion_response(status, searched):
    if status == 'deleted':
        return
    elif status == 'does not exist':
        return (
            {
                'detail': f'{searched} does not exist',
                'status': 404,
                'title': 'Not Found',
                'type': 'about:blank',
            },
            404,
        )


def delete_dataset(dataset):
    status = database.delete_dataset(dataset.strip())
    return _deletion_response(status, 'dataset')


def delete_dataset_item(dataset, item):
    status = database.delete_dataset_item(dataset.strip(), item)
    return _deletion_response(status, 'dataset item')

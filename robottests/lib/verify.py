from robot.api import logger
import requests


class Verify(object):
    def _get_testdata(self, base_url):
        response = requests.get(base_url + '/testdata')
        if response.status_code != 200:
            raise AssertionError(
                f'Getting testdata failed ({response.status_code}: {response.text})'
            )
        return response.json()['testdata']

    def _get_dataset_items(self, base_url, dataset_name):
        for dataset in self._get_testdata(base_url):
            if dataset['dataset'] == dataset_name:
                return [items['item'] for items in dataset['items']]

    def _get_item_data(self, data, base_url, dataset_name, expected_item):
        for dataset in self._get_testdata(base_url):
            if dataset['dataset'] == dataset_name:
                items = dataset['items']
                break
        for item in items:
            if item['item'] == expected_item:
                return item[data]
        raise AssertionError(f'Item ({expected_item}) could not be found')

    def verify_new_dataset(self, base_url, dataset_name, items):
        """
        Verify that new dataset has been stored to database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        :param items: items for dataset
        """
        db_item_list = self._get_dataset_items(base_url, dataset_name)

        for item in items.splitlines():
            if item not in db_item_list:
                raise AssertionError(f'Expected dataset item ({item}) not found in database')

        logger.info('New dataset verified.')

    @staticmethod
    def verify_dataset_does_no_exist_in_db(base_url, dataset_name):
        """
        Verify that dataset does not exist in database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        """
        response = requests.get(base_url + '/testdata/' + dataset_name)
        if response.status_code != 404:
            raise AssertionError(
                f'Getting testdata failed ({response.status_code}: {response.text})'
            )

        logger.info('Dataset not existing verified.')

    def verify_dataset_item_does_no_exist_in_db(self, base_url, dataset_name, item):
        """
        Verify that dataset item does not exist in database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        :param item: dataset item to be searched
        """
        if item in self._get_dataset_items(base_url, dataset_name):
            raise AssertionError(f'Unexpected dataset item ({item}) found in database')

        logger.info('Dataset item not existing verified.')

    def verify_dataset_item_exists_in_db(self, base_url, dataset_name, item):
        """
        Verify that dataset item  exists in database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        :param item: dataset item to be searched
        """
        if item not in self._get_dataset_items(base_url, dataset_name):
            raise AssertionError(f'Expected dataset item ({item}) not found in database')

        logger.info('Dataset item existing verified.')

    @staticmethod
    def verify_get_testdata_response(response, datasets):
        """
        Verify that dataset item  exists in database.

        :param response: requests.response
        :param datasets: expected datasets and items
        """
        if response.status_code != 200:
            raise AssertionError(
                f'Unexpected status code! Expected: 200, actual: {response.status_code}'
            )

        response_datasets = []
        for dataset in response.json()['testdata']:
            response_datasets.append(
                {
                    'dataset': dataset['dataset'],
                    'datatype': dataset['datatype'],
                    'items': [item['item'] for item in dataset['items']],
                }
            )

        if datasets != response_datasets:
            raise AssertionError(
                f'Datasets did not match! Expected: {datasets}, actual: {response_datasets}'
            )

        logger.info('GET /testdata response verified.')

    @staticmethod
    def verify_get_testdata_dataset_response(item, previous_response, response):
        """
        Verify /testdata/<dataset> response.

        :param item: expected item
        :param previous_response: previous requests.response to /testdata/<dataset> request
        :param response: requests.response to /testdata/<dataset> request
        """
        if previous_response.status_code != 200 or response.status_code != 200:
            raise AssertionError(
                f'Wrong status code(s). Previous: {previous_response.status_code} \
                ({previous_response.text}), current: {response.status_code} ({response.text})'
            )
        previous_json = previous_response.json()['testdata']
        response_json = response.json()['testdata']
        if previous_json['item'] == response_json['item']:
            raise AssertionError(f'Unexpected item {response.json()}')
        if previous_json['timestamp'] >= response_json['timestamp']:
            raise AssertionError(
                f'Wrong item returned (timestamp). Previous: {previous_response.json()}, \
                    current: {response.json()}'
            )
        if response_json['item'] != item:
            raise AssertionError(
                f'Wrong item returned (value). Expected: {item}, actual: {response.json()}'
            )

        logger.info('GET /testdata/<dataset> response verified.')

    def verify_item_status(self, base_url, dataset, item, status):
        """
        Verify that new dataset has been stored to database.

        :param base_url: base url for api
        :param dataset: name of dataset to be searched
        :param item: item which status is checked
        :param status: expected status for item
        """
        item_status = self._get_item_data('status', base_url, dataset, item)

        if status != item_status:
            raise AssertionError(f'Unexpected item status ({item_status}), expected ({status})')

        logger.info('Item status verified.')

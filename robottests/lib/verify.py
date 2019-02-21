from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import requests


class Verify(object):
    def _get_dataset_items(self, base_url, dataset_name):
        response = requests.get(base_url + '/testdata')
        if response.status_code != 200:
            BuiltIn().fail(
                'Getting testdata failed ({}: {})'.format(response.status_code, response.text)
            )

        for dataset in response.json()['testdata']:
            if dataset['dataset'] == dataset_name:
                return [items['item'] for items in dataset['items']]

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
                BuiltIn().fail('Expected dataset item ({}) not found in database'.format(item))

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
            BuiltIn().fail(
                'Getting testdata failed ({}: {})'.format(response.status_code, response.text)
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
            BuiltIn().fail('Unexpected dataset item ({}) found in database'.format(item))

        logger.info('Dataset item not existing verified.')

    def verify_dataset_item_exists_in_db(self, base_url, dataset_name, item):
        """
        Verify that dataset item  exists in database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        :param item: dataset item to be searched
        """
        if item not in self._get_dataset_items(base_url, dataset_name):
            BuiltIn().fail('Expected dataset item ({}) not found in database'.format(item))

        logger.info('Dataset item existing verified.')

    @staticmethod
    def verify_get_testdata_response(response, datasets):
        """
        Verify that dataset item  exists in database.

        :param response: requests.response
        :param datasets: expected datasets and items
        """
        if response.status_code != 200:
            BuiltIn().fail(
                'Unexpected status code! Expected: 200, actual: {}'.format(response.status_code)
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
            BuiltIn().fail(
                'Datasets did not match! Expected: {}, actual: {}'.format(
                    datasets, response_datasets
                )
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
            BuiltIn().fail(
                'Wrong status code(s). Previous: {} ({}), current: {} ({})'.format(
                    previous_response.status_code,
                    previous_response.text,
                    response.status_code,
                    response.text,
                )
            )
        previous_json = previous_response.json()['testdata']
        response_json = response.json()['testdata']
        if previous_json['item'] == response_json['item']:
            BuiltIn().fail('Unexpected item {}'.format(response.json()))
        if previous_json['timestamp'] >= response_json['timestamp']:
            BuiltIn().fail(
                'Wrong item returned (timestamp). Previous: {}, current: {}'.format(
                    previous_response.json(), response.json()
                )
            )
        if response_json['item'] != item:
            BuiltIn().fail(
                'Wrong item returned (value). Expected: {}, actual: {}'.format(
                    item, response.json()
                )
            )

        logger.info('GET /testdata/<dataset> response verified.')

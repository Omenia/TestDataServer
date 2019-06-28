import datetime

from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import requests

import resources.gui.aliases as alias


SELENIUM = 'SeleniumLibrary'


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
    def verify_get_testdata_dataset_response(item, response):
        """
        Verify /testdata/<dataset> response.

        :param item: expected item
        :param response: requests.response to /testdata/<dataset> request
        """
        if response.json()['testdata']['item'] != item:
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

    @staticmethod
    def verify_dataset_in_dashboard(dataset, items, status):
        """
        Verify dataset and items in dashboard.

        :param dataset: name of dataset
        :param items: list of dataset items
        :param status: expected status for items
        """
        selenium = BuiltIn().get_library_instance(SELENIUM)
        dataset_name = selenium.get_webelement(
            alias.DASHBOARD_PAGE['dataset'].format(dataset_name=dataset)
        ).text
        if dataset not in dataset_name:
            raise AssertionError(f'Dataset ({dataset}) could not be found.')

        for index in range(1, len(items) + 1):
            item_name = selenium.get_webelement(
                alias.DASHBOARD_PAGE['item-name'].format(dataset_name=dataset, index=index)
            ).text
            if item_name != items[index - 1]:
                raise AssertionError(f'Item ({item_name}) could not be found.')

            item_time = selenium.get_webelement(
                alias.DASHBOARD_PAGE['item-time'].format(dataset_name=dataset, index=index)
            ).text
            if datetime.date.today().isoformat() not in item_time:
                raise AssertionError(f'Item timestamp ({item_time}) could not be found.')

            item_status = selenium.get_webelement(
                alias.DASHBOARD_PAGE['item-status'].format(dataset_name=dataset, index=index)
            ).text
            if status != item_status:
                raise AssertionError(f'Unexpected item status ({item_status}), expected ({status})')

        logger.info('Dataset in dashboard verified.')

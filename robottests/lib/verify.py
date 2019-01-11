from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import requests


class Verify(object):
    def _get_dataset_items(self, base_url, dataset_name):
        response = requests.get(base_url + '/api/v1/testdata')
        if response.status_code != 200:
            BuiltIn().fail(
                'Getting testdata failed ({}: {})'.format(response.status_code, response.text)
            )

        return [items['item'] for items in response.json()['testdata'][dataset_name]]

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
                BuiltIn().fail('Expected dataset item ({}}) not found in database'.format(item))

        logger.info('New dataset verified.')

    @staticmethod
    def verify_dataset_does_no_exist_in_db(base_url, dataset_name):
        """
        Verify that dataset does not exist in database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        """
        response = requests.get(base_url + '/api/v1/testdata/' + dataset_name)
        # todo: status code needs to be changed when error handling is implemented
        if response.status_code != 500:
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
            BuiltIn().fail('Unexpected dataset item ({}}) found in database'.format(item))

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

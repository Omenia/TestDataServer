from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import requests


class Verify(object):
    @staticmethod
    def verify_new_dataset(base_url, dataset_name, dataset_items):
        """
        Verify that new dataset has been stored to database.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be searched
        :param dataset_items: items for dataset
        """
        response = requests.get(base_url + '/api/v1/testdata')
        if response.status_code != 200:
            BuiltIn().fail(
                'Getting testdata failed ({}: {})'.format(response.status_code, response.text)
            )

        db_item_list = [items['item'] for items in response.json()['testdata'][dataset_name]]

        for item in dataset_items.splitlines():
            if item not in db_item_list:
                BuiltIn().fail('Expected dataset item ({}}) not found in database'.format(item))

        logger.info('New dataset verified.')

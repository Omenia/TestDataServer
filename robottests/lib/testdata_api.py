import json

from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import requests


class TestdataApi(object):
    @staticmethod
    def add_dataset(base_url, dataset_name, *dataset_items):
        """
        Add new dataset.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be added
        :param dataset_items: items for dataset
        """
        response = requests.post(
            base_url + '/api/v1/testdata',
            json={'dataset': dataset_name, 'items': dataset_items}
        )
        if response.status_code != 200:
            BuiltIn().fail(
                'Adding new dataset failed ({}: {})'.format(response.status_code, response.text)
            )

        logger.info('New dataset added.')

    @staticmethod
    def delete_dataset(base_url, dataset_name):
        """
        Delete dataset.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be deleted
        :param dataset_items: items for dataset
        """
        response = requests.delete(base_url + '/api/v1/testdata/' + dataset_name)
        if response.status_code != 200:
            BuiltIn().fail(
                'Deleting dataset failed ({}: {})'.format(response.status_code, response.text)
            )

        logger.info('Dataset deleted.')

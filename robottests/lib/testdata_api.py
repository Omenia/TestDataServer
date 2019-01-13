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
            base_url + '/testdata', json={'dataset': dataset_name, 'items': dataset_items}
        )
        if response.status_code != 201:
            BuiltIn().fail(
                'Adding new dataset failed ({}: {})'.format(response.status_code, response.text)
            )

        logger.info('New dataset added.')

    def add_multiple_dataset(self, base_url, datasets):
        """
        Add multiple dataset.

        :param base_url: base url for api
        :param datasets: dict of datasets and their items in a list
        """
        for dataset, items in datasets.items():
            self.add_dataset(base_url, dataset, *items)

    @staticmethod
    def delete_dataset(base_url, dataset_name):
        """
        Delete dataset.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be deleted
        """
        response = requests.delete(base_url + '/testdata/' + dataset_name)
        if response.status_code != 200:
            BuiltIn().fail(
                'Deleting dataset failed ({}: {})'.format(response.status_code, response.text)
            )

        logger.info('Dataset deleted.')

    def delete_multiple_dataset(self, base_url, dataset_names):
        """
        Delete multiple dataset.

        :param base_url: base url for api
        :param datasets: list of dataset names
        """
        for dataset in dataset_names:
            self.delete_dataset(base_url, dataset)

    @staticmethod
    def send_get_request(base_url, endpoint):
        """
        Send GET request.

        :param base_url: base url for api
        :param endpoint: endpoint for request
        :rtype: requests.Response
        """
        return requests.get(base_url + endpoint)

    @staticmethod
    def send_get_testdata_dataset_request(base_url, dataset_name):
        """
        Send GET /testdata/<dataset> request.

        :param base_url: base url for api
        :param dataset_name: dataset name
        :rtype: requests.Response
        """
        return requests.get(base_url + '/testdata/' + dataset_name)

    @staticmethod
    def send_post_testdata_request(base_url, body_json):
        """
        Send POST /testdata request.

        :param base_url: base url for api
        :param body_json: body parameters in json
        :rtype: requests.Response
        """
        return requests.post(
            base_url + '/testdata',
            json=json.loads(body_json),
            headers={'Content-Type': 'application/json'}
        )

    @staticmethod
    def send_delete_testdata_dataset_request(base_url, dataset_name):
        """
        Send DELETE /testdata/<dataset> request.

        :param base_url: base url for api
        :param dataset_name: dataset name
        :rtype: requests.Response
        """
        return requests.delete(base_url + '/testdata/' + dataset_name)

    @staticmethod
    def send_get_testdata_dataset_item_request(base_url, dataset_name, item):
        """
        Send DELETE /testdata/<dataset>/<item> request.

        :param base_url: base url for api
        :param dataset_name: dataset name
        :parma item: dataset item
        :rtype: requests.Response
        """
        return requests.delete(base_url + '/testdata/' + dataset_name + '/' + item)

import json

from robot.api import logger
import requests


class TestdataApi(object):
    @staticmethod
    def add_dataset(base_url, dataset_name, datatype, dataset_items):
        """
        Add new dataset.

        :param base_url: base url for api
        :param dataset_name: name of dataset to be added
        :param datatype: dataset datatype
        :param dataset_items: items for dataset
        """
        response = requests.post(
            base_url + '/testdata',
            json={'dataset': dataset_name, 'items': dataset_items, 'datatype': datatype},
        )
        if response.status_code != 201:
            raise AssertionError(
                f'Adding new dataset failed ({response.status_code}: {response.text})'
            )

        logger.info('New dataset added.')

    @staticmethod
    def delete_dataset(base_url, dataset_name):
        """
        Delete dataset.

        :param base_url: endpoint url
        """
        response = requests.delete(base_url + '/testdata/' + dataset_name)
        if response.status_code != 200:
            raise AssertionError(
                'Deleting dataset failed ({response.status_code}: {response.text})'
            )

        logger.info('Dataset deleted.')

    def delete_datasets(self, base_url):
        """
        Delete datasets from database.

        :param base_url: base url for api
        """
        response = requests.get(base_url + '/testdata')
        for index in range(len(response.json()['testdata'])):
            self.delete_dataset(base_url, response.json()['testdata'][index]['dataset'])

    @staticmethod
    def send_get_request(url):
        """
        Send GET request.

        :param base_url: endpoint url
        :rtype: requests.Response
        """
        return requests.get(url)

    @staticmethod
    def send_post_request(url, body_json):
        """
        Send POST request.

        :param base_url: endpoint url
        :param body_json: body parameters in json
        :rtype: requests.Response
        """
        return requests.post(
            url, json=json.loads(body_json), headers={'Content-Type': 'application/json'}
        )

    @staticmethod
    def send_delete_request(url):
        """
        Send DELETE request.

        :param url: endpoint url
        :rtype: requests.Response
        """
        return requests.delete(url)

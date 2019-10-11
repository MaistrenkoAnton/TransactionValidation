import copy

from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from rest_framework_xml.parsers import XMLParser

from transactions.service import TransactionService
from transactions.tests.data_json import json_sample
from transactions.tests.data_xml import xml_sample

REST_URL = 'transactions:rest'
XML_URL = 'transactions:xml'


class TestTransactionView(APITestCase):

    def setUp(self) -> None:
        self.data = copy.deepcopy(json_sample)

    def test_rest_data_valid(self):
        url = reverse(REST_URL)
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': 'Data is valid'})

    def test_tax_id_is_missed(self):
        url = reverse(REST_URL)
        self.data['taxes'] = [{
          "id": None,
          "name": "string",
          "inclusion_type": "string",
          "is_custom_amount": True,
          "applied_money": {
            "amount": 1,
            "currency": "USD"
          }
        }]
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_tax_name_is_missed(self):
        url = reverse(REST_URL)
        self.data['taxes'] = [{
            "id": 1,
            "name": None,
            "inclusion_type": "string",
            "is_custom_amount": True,
            "applied_money": {
                "amount": 1,
                "currency": "USD"
            }
        }]
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['taxes'][0]['name'][0], ErrorDetail(string='This field may not be null.', code='null')
        )

    def test_is_custom_amount_wrong_format(self):
        url = reverse(REST_URL)
        self.data['taxes'] = [{
            "id": 1,
            "name": 'Tax',
            "inclusion_type": "string",
            "is_custom_amount": 'WRONG',
            "applied_money": {
                "amount": 1,
                "currency": "USD"
            }
        }]
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['taxes'][0]['is_custom_amount'][0],
            ErrorDetail(string='Must be a valid boolean.', code='invalid')
        )

    def test_tax_currency_is_wrong(self):
        url = reverse(REST_URL)
        self.data['taxes'] = [{
            "id": 1,
            "name": 'Tax',
            "inclusion_type": "string",
            "is_custom_amount": True,
            "applied_money": {
                "amount": 1,
                "currency": "WRONG"
            }
        }]
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['taxes'][0]['applied_money']['currency'][0],
            ErrorDetail(string='Currency name is not valid.', code='invalid')
        )


class TestXMLTransactionView(APITestCase):

    def setUp(self) -> None:
        self.data = xml_sample

    def test_xml_data_valid(self):
        url = reverse(XML_URL)
        response = self.client.post(url, data=self.data, content_type='application/xml')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': 'Data is valid'})

    def test_xml_json_taxes_mapping(self):
        parsed = TransactionService.parse_xml(self.data)
        self.assertEqual(len(parsed['taxes']), len(json_sample['taxes']))
        self.assertEqual(parsed['taxes'][0]['id'], json_sample['taxes'][0]['id'])
        self.assertEqual(parsed['taxes'][0]['inclusion_type'], json_sample['taxes'][0]['inclusion_type'])
        self.assertEqual(parsed['taxes'][0]['name'], json_sample['taxes'][0]['name'])
        self.assertEqual(float(parsed['taxes'][0]['rate']), json_sample['taxes'][0]['rate'])

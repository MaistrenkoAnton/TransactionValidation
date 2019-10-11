from django.test import TestCase
from rest_framework.exceptions import ErrorDetail

from transactions.serializers import TaxSerializer


class TestTaxSerializer(TestCase):

    def test_serializer_is_valid(self):
        data = {
            "id": "cfc92a12-f847-4942-b6ec-1454d194c9ba",
            "name": "Sales Tax",
            "rate": 0.16,
            "inclusion_type": "INCLUSIVE",
            "is_custom_amount": True,
            "applied_money": {
                "amount": 483,
                "currency": "JOD"
            }
        }
        self.assertTrue(TaxSerializer(data=data).is_valid())

    def test_serializer_wrong_uuid(self):
        data = {
            "id": "WRONG",
            "name": "Sales Tax",
            "rate": 0.16,
            "inclusion_type": "INCLUSIVE",
            "is_custom_amount": True,
            "applied_money": {
                "amount": 483,
                "currency": "JOD"
            }
        }
        serializer = TaxSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors['id'][0],
            ErrorDetail(string='Must be a valid UUID.', code='invalid')
        )

    def test_serializer_wrong_rate(self):
        data = {
            "id": "cfc92a12-f847-4942-b6ec-1454d194c9ba",
            "name": "Sales Tax",
            "rate": "wrong",
            "inclusion_type": "INCLUSIVE",
            "is_custom_amount": True,
            "applied_money": {
                "amount": 483,
                "currency": "JOD"
            }
        }
        serializer = TaxSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors['rate'][0],
            ErrorDetail(string='A valid number is required.', code='invalid')
        )

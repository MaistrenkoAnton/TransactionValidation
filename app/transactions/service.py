import json

import six
import defusedxml.ElementTree as etree

from rest_framework.exceptions import ParseError
from rest_framework_xml.parsers import XMLParser

from transactions.serializers import TransactionSerializer


class TransactionService:
    """
    Service helps to validate data
    """
    @classmethod
    def validate(cls, data):
        """
        Validate transaction data
        :param data: json, dict, xml
        :return: dict with validation result and errors
        """
        if cls.is_valid_json(data):
            data = json.loads(data)
        if cls.is_valid_xml(data):
            data = XMLParser().parse(data)
        serializer_data = TransactionSerializer(data=data)
        return {
            'is_valid': serializer_data.is_valid(),
            'errors': serializer_data.errors
        }

    @staticmethod
    def is_valid_json(data):
        """
        Check if json is valid
        :param data: string
        :return: Boolean
        """
        try:
            json.loads(data)
        except (ValueError, TypeError) as e:
            return False
        return True

    @staticmethod
    def is_valid_xml(data):
        """
        Check if xml is valid
        :param data: string
        :return: Boolean
        """
        try:
            etree.fromstring(data)
        except (ParseError, etree.ParseError, TypeError) as e:
            return False
        return True

    @staticmethod
    def parse_xml(data):
        """
        Parse xml dict
        :param data: string
        :return: dict
        """
        try:
            tree = etree.fromstring(data)
        except (etree.ParseError, ValueError) as exc:
            raise ParseError('XML parse error - %s' % six.text_type(exc))
        data = XMLParser()._xml_convert(tree)
        return data

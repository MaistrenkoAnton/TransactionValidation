from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.service import TransactionService
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer


class TransactionView(APIView):
    """
    Validate transaction REST request
    """
    permission_classes = (AllowAny,)
    parser_classes = (XMLParser, JSONParser)
    renderer_classes = (XMLRenderer, JSONRenderer)

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT))
    def post(self, request):
        transaction_data = TransactionService.validate(request.data)
        if transaction_data['is_valid']:
            return Response({'result': 'Data is valid'})
        return Response(transaction_data['errors'], status=status.HTTP_400_BAD_REQUEST)

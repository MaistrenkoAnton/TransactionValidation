from django.urls import path

from transactions.views import TransactionView, XmlTransactionView


urlpatterns = [
    path('json', TransactionView.as_view(), name='rest'),
    path('xml', XmlTransactionView.as_view(), name='xml'),
]

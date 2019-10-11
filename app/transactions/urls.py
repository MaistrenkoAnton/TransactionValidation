from django.urls import path

from transactions.views import TransactionView


urlpatterns = [
    path('', TransactionView.as_view(), name='validate'),
]

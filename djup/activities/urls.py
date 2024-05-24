from django.urls import path
from activities.views import TransactionListAPIView

urlpatterns = [
    path('transactions/list/', TransactionListAPIView.as_view()),
]

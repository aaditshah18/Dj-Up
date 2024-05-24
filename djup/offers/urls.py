from django.urls import path
from offers.views import OfferListAPIView

urlpatterns = [
    path('list/', OfferListAPIView.as_view()),
]
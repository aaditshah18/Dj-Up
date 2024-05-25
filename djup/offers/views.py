from rest_framework import generics
from offers.models import Offers
from offers.serializers import OffersListSerializer
from rest_framework.permissions import AllowAny


class OfferListAPIView(generics.ListCreateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersListSerializer
    permission_classes = [AllowAny]

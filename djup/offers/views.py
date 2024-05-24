from rest_framework import generics
from offers.models import Offers
from offers.serializers import OffersListSerializer


class OfferListAPIView(generics.ListCreateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # status = self.request.query_params.get('status')
        # if status:
        #     queryset = queryset.filter(status=status)
        return queryset

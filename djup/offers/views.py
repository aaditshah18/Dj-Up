from django.db.models import Q
from rest_framework import generics
from offers.models import Offers
from offers.serializers import OffersListSerializer
from rest_framework.permissions import AllowAny


class OfferListAPIView(generics.ListCreateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get('name')
        q_filters = Q()  # Start with an empty Q object
        if name:
            q_filters &= Q(name__icontains=name)  # Case-insensitive name search

        return queryset.filter(q_filters)

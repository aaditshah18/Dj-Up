from rest_framework import serializers
from offers.models import Offers

class OffersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offers
        fields = '__all__'
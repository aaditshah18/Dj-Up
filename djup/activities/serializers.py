from rest_framework import serializers
from activities.models import Transactions


class TransactionsSerializer(serializers.ModelSerializer):
    offer_name = serializers.CharField(source='offer_id.name')
    member_name = serializers.CharField(source='member_id.name')

    class Meta:
        model = Transactions
        fields = '__all__'

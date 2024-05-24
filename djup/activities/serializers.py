from rest_framework import serializers
from activities.models import Transactions


class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'

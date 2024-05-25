from rest_framework import serializers
from members.models import Members
from activities.serializers import TransactionsSerializer


class MembersListSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()

    class Meta:
        model = Members
        fields = '__all__'

    def get_transactions(self, obj):
        transactions_queryset = obj.transactions_set.all()  # Example filter
        return TransactionsSerializer(transactions_queryset, many=True).data

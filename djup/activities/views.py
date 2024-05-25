from rest_framework import generics
from activities.models import Transactions
from activities.serializers import TransactionsSerializer
from rest_framework.permissions import AllowAny


class TransactionListAPIView(generics.ListCreateAPIView):
    serializer_class = TransactionsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Transactions.objects.all().select_related("member_id", "offer_id")

        return queryset

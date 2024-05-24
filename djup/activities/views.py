from rest_framework import generics
from activities.models import Transactions
from activities.serializers import TransactionsSerializer


class TransactionListAPIView(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # status = self.request.query_params.get('status')
        # if status:
        #     queryset = queryset.filter(status=status)
        return queryset

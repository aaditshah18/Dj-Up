from rest_framework import generics
from members.models import Members
from rest_framework.permissions import AllowAny
from members.serializers import MembersListSerializer


class MembersListAPIView(generics.ListCreateAPIView):

    serializer_class = MembersListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Members.objects.all().prefetch_related("transactions_set")
        return queryset

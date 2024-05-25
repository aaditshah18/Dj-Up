from rest_framework import generics
from members.models import Members
from rest_framework.permissions import AllowAny
from members.serializers import MembersListSerializer


class MembersListAPIView(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        # status = self.request.query_params.get('status')
        # if status:
        #     queryset = queryset.filter(status=status)
        return queryset

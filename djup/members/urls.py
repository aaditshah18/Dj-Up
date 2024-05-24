from django.urls import path
from members.views import MembersListAPIView

urlpatterns = [
    path('list/', MembersListAPIView.as_view()),
]
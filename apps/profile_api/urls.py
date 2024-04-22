from django.urls import path
from apps.profile_api.views import InviteUserList

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('', InviteUserList.as_view(), name='invite_list'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc")
]


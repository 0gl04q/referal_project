from django.urls import path, include
from django.contrib.auth.views import logout_then_login

from apps.accounts import views

urlpatterns = [
    path('', views.main, name='main'),

    path('profile/', views.profile, name='profile'),
    path('profile/api/', include('apps.profile_api.urls')),

    path('login/', views.login_by_phone_number, name='login'),
    path('login/verify', views.phone_verify_code, name='verify'),
    path('logout/', logout_then_login, name='logout')
]

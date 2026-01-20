from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('create', CreateUserView.as_view(), name='create_user'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', TokenBlacklistView.as_view(), name='token_blacklist')
]
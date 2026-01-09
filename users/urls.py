from django.urls import path
from rest_framework.permissions import AllowAny

from users.views import UserCreateAPIView, UserDeleteAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "users"


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("user/<int:pk>/delete/", UserDeleteAPIView.as_view(), name="user_delete"),
]

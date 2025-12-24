from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.serializers import UserSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    """
    Регистрация пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDeleteAPIView(DestroyAPIView):
    """
    Удаление пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import CustomPagination
from habits.permissions import IsOwnerOrPublicReadOnly
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """API view для создания привычки"""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(ListAPIView):
    """API view для получения списка привычек"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        # свои привычки или чужие публичные
        return Habit.objects.filter(Q(user=user) | Q(is_public=True))


class HabitRetrieveAPIView(RetrieveAPIView):
    """API view для получения детальной информации о привычке"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPublicReadOnly]


class HabitUpdateAPIView(UpdateAPIView):
    """API view для обновления привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPublicReadOnly]


class HabitDestroyAPIView(DestroyAPIView):
    """API view для удаления привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPublicReadOnly]

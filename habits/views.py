from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """API view для создания привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListAPIView(ListAPIView):
    """API view для получения списка привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveAPIView(RetrieveAPIView):
    """API view для получения детальной информации о привычке"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(UpdateAPIView):
    """API view для обновления привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(DestroyAPIView):
    """API view для удаления привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

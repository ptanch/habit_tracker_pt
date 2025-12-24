from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для представления привычки"""

    user = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Habit
        fields = "__all__"

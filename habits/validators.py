from rest_framework.serializers import ValidationError
from datetime import timedelta


def validate_habits(value):
    if not {"is_pleasant", "reward", "related_habit"} & value.keys():
        return value

    is_pleasant = value.get("is_pleasant")
    related_habit = value.get("related_habit")
    reward = value.get("reward")
    execution_time = value.get("execution_time")
    periodicity = value.get("periodicity")

    # Нельзя одновременно reward и related_habit
    if related_habit and reward:
        raise ValidationError("Нельзя указывать и вознаграждение, и связанную привычку")

    # Приятная привычка
    if is_pleasant:
        if related_habit:
            raise ValidationError("Приятная привычка не может иметь связанную привычку")
        if reward:
            raise ValidationError("Приятная привычка не может иметь вознаграждение")

    # Полезная привычка
    else:
        if not related_habit and not reward:
            raise ValidationError("Полезная привычка должна иметь награду или связанную привычку")

    # Время выполнения ≤ 120 секунд
    if execution_time and execution_time > timedelta(seconds=120):
        raise ValidationError("Время выполнения привычки не может превышать 120 секунд")

    # Связанная привычка должна быть приятной
    if related_habit and not related_habit.is_pleasant:
        raise ValidationError("Связанная привычка должна быть приятной")

    # Периодичность: не реже 1 раза в 7 дней
    if periodicity and periodicity > 7:
        raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")

    return value

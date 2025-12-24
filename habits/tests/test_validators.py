from datetime import timedelta

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from habits.models import Habit
from habits.validators import validate_habits
from users.models import User


class HabitValidatorTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            password="12345"
        )

        self.pleasant_habit = Habit.objects.create(
            user=self.user,
            action="Принять ванну",
            place="Дом",
            time="20:00",
            is_pleasant=True,
            periodicity=1,
        )

    # Нельзя reward + related_habit
    def test_reward_and_related_habit_together(self):
        data = {
            "is_pleasant": False,
            "related_habit": self.pleasant_habit,
            "reward": "Шоколад",
            "periodicity": 1,
        }

        with self.assertRaises(ValidationError):
            validate_habits(data)

    # Полезная привычка без награды и связанной
    def test_useful_habit_without_reward_and_related(self):
        data = {
            "is_pleasant": False,
            "periodicity": 1,
        }

        with self.assertRaises(ValidationError):
            validate_habits(data)

    # Время выполнения больше 120 секунд
    def test_execution_time_more_than_120_seconds(self):
        data = {
            "is_pleasant": False,
            "reward": "Чай",
            "execution_time": timedelta(seconds=121),
            "periodicity": 1,
        }

        with self.assertRaises(ValidationError):
            validate_habits(data)

    # Связанная привычка должна быть приятной
    def test_related_habit_must_be_pleasant(self):
        useful_habit = Habit.objects.create(
            user=self.user,
            action="Прогулка",
            place="Улица",
            time="18:00",
            is_pleasant=False,
            reward="Отдых",
            periodicity=1,
        )

        data = {
            "is_pleasant": False,
            "related_habit": useful_habit,
            "periodicity": 1,
        }

        with self.assertRaises(ValidationError):
            validate_habits(data)

    # Приятная привычка не может иметь reward
    def test_pleasant_habit_cannot_have_reward(self):
        data = {
            "is_pleasant": True,
            "reward": "Конфета",
            "periodicity": 1,
        }

        with self.assertRaises(ValidationError):
            validate_habits(data)

    # Периодичность больше 7 дней
    def test_periodicity_more_than_7_days(self):
        data = {
            "is_pleasant": False,
            "reward": "Фильм",
            "periodicity": 8,
        }

        with self.assertRaises(ValidationError):
            validate_habits(data)

    # Валидные данные
    def test_valid_useful_habit_with_reward(self):
        data = {
            "is_pleasant": False,
            "reward": "Десерт",
            "execution_time": timedelta(seconds=60),
            "periodicity": 3,
        }

        try:
            validate_habits(data)
        except ValidationError:
            self.fail("validate_habit() выбросил ValidationError на валидных данных")

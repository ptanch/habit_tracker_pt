from datetime import timedelta, time

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from habits.models import Habit

User = get_user_model()


class HabitAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="habit@example.com",
            password="StrongPassword123"
        )

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

    def test_create_habit(self):
        """
        Авторизованный пользователь может создать полезную привычку
        (с обязательным reward)
        """
        url = reverse("habits:habit_create")

        data = {
            "action": "Выпить стакан воды",
            "place": "Дом",
            "time": "09:00:00",
            "execution_time": "00:01:00",
            "periodicity": 1,
            "is_pleasant": False,
            "reward": "Чашка кофе",
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)

        habit = Habit.objects.first()
        self.assertEqual(habit.user, self.user)
        self.assertEqual(habit.action, "Выпить стакан воды")

    def test_list_habits(self):
        """
        Пользователь может получить список только своих привычек
        """
        Habit.objects.create(
            user=self.user,
            action="Прогулка",
            time=time(9, 0),
            execution_time=timedelta(seconds=30),
            is_pleasant=True,
        )

        url = reverse("habits:habit_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 1)

    def test_delete_habit(self):
        """
        Пользователь может удалить только свою привычку
        """
        habit = Habit.objects.create(
            user=self.user,
            action="Удаляемая привычка",
            time=time(9, 0),
            execution_time=timedelta(seconds=30),
            is_pleasant=True,
        )

        url = reverse("habits:habit_delete", args=[habit.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=habit.id).exists())

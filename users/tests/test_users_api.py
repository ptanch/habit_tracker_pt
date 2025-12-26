from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPITestCase(APITestCase):

    def test_user_registration(self):
        """Пользователь может зарегистрироваться"""
        url = reverse("users:register")
        data = {
            "email": "testuser@example.com",
            "password": "StrongPassword123",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="testuser@example.com").exists())

    def test_user_login(self):
        """Пользователь может получить JWT токен"""
        user = User.objects.create_user(
            email="login@example.com",
            password="StrongPassword123"
        )

        url = reverse("users:login")
        data = {
            "email": "login@example.com",
            "password": "StrongPassword123",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

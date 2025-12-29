from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    """Класс для представления пользователя"""

    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите свою почту"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите свой номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватарка",
        help_text="Загрузите свое фото",
    )
    telegram = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name="Телеграм никнейм",
        help_text="Введите свой тг ник",
    )

    tg_chat_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Telegram chat ID",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email or str(self.pk)

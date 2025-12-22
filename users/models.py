from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    """
    Добавлен кастомный менеджер для корректной работы UserManager
    при создании пользователей, для команды createsuperuser
    """

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return super().create_superuser(email=email, password=password, **extra_fields)


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

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email or str(self.pk)

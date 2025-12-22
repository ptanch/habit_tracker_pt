from django.db import models


class Habit(models.Model):
    """Класс для представления привычки"""

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    place = models.CharField(
        max_length=255,
        verbose_name="Место",
        help_text="Введите место, в котором необходимо выполнять привычку",
    )
    time = models.TimeField(
        verbose_name="Время",
        help_text="Введите время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
        help_text="Действие, которое представляет собой привычка",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Привычка",
        help_text="Привычка, которую можно привязать к выполнению полезной привычки",
    )
    related_habit = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="useful_habits",
        help_text="Привычка связанная с другой привычкой (только для полезных)",
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1, help_text="периодичность в днях"
    )
    reward = models.CharField(
        max_length=255,
        verbose_name="Вознаграждение",
        help_text="Чем пользователь должен себя вознаградить после выполнения",
    )
    execution_time = models.DurationField(
        help_text="Время на выполнение",
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action or f"Habit #{self.pk}"

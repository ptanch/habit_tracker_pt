from django.utils import timezone
from celery import shared_task
from habits.models import Habit
from datetime import timedelta
from habits.services import send_telegram_message


@shared_task
def send_habits_reminders():
    """Отправляет пользователю сообщение о необходимости выполнить привычку"""

    now = timezone.localtime()

    # Фильтр: только привычки с привязанным tg_chat_id
    habits = Habit.objects.filter(user__tg_chat_id__isnull=False)

    for habit in habits:
        # Проверка last_run_at: пропуск, если уже отправляли раньше, чем периодичность
        if habit.last_run_at:
            delta = now - habit.last_run_at
            if delta < timedelta(days=habit.periodicity):
                continue

        # Проверка времени: отправляем, если сейчас >= привычки по часам и минутам
        if habit.time.hour == now.hour and habit.time.minute == now.minute:
            send_telegram_message(
                chat_id=habit.user.tg_chat_id,
                message=f"Напоминание:\n{habit.action}\nМесто: {habit.place}",
            )
            habit.last_run_at = now
            habit.save(update_fields=["last_run_at"])

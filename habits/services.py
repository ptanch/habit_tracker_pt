import requests
from config import settings


def send_telegram_message(chat_id, message):
    """Функция отправки уведомлений в телеграмм"""

    url = f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage"
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")

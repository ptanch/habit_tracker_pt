# Базовый образ
FROM python:3.12-slim-bookworm

# Отключаем создание .pyc и буферизацию
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Рабочая директория
WORKDIR /app

# Системные зависимости
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry через pip
RUN pip install --upgrade pip \
 && pip install poetry==1.8.3

ENV PATH="/root/.local/bin:$PATH"

# Копируем только файлы зависимостей (важно для кэша)
COPY pyproject.toml poetry.lock ./

# Отключаем venv внутри контейнера
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# Копируем проект
COPY . .

# Открываем порт
EXPOSE 8000
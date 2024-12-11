FROM python:3.12-slim

LABEL authors="Игорь"

# Рабочая директория
WORKDIR /app

# Установка зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

# Обновление PATH и часового пояса
ENV PATH="/root/.local/bin:$PATH" \
    TZ=Europe/Moscow

# Установка часового пояса контейнера
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Копирование файлов для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Установка зависимостей
RUN poetry install --no-root

# Копирование исходного кода
COPY ./src ./src
COPY main.py ./
COPY .env ./

# Запуск основного приложения
CMD ["poetry run python main.py"]
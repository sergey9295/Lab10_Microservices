# Первый этап: сборка
FROM python:3.12.7-slim AS builder
WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

# Второй этап: рабочий контейнер
FROM python:3.12.7-slim AS working
WORKDIR /app

# Копирование установленных зависимостей из первого этапа
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Запуск команд
CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py loaddata books_dump.json \
    && python manage.py runserver 0.0.0.0:8000

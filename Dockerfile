FROM python:3.12-slim
LABEL authors="ivan"

# Сначала создаем рабочую директорию
WORKDIR /app

COPY requirements.txt .
#КОмандро -r установить все зависимости из  requirements.txt
RUN pip install -r requirements.txt

#Копируем остальной функционал
COPY .

#Запускаем весь проект
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
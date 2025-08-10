# SmartEducation-LMS

Бэкенд-сервер для системы онлайн-обучения (LMS), разработанный на **Django** с использованием **Django Rest Framework (DRF)**.  
Проект предоставляет полноценный API для управления учебными материалами, такими как курсы и уроки.

---

## 🚀 Ключевые особенности

- **Гибкие модели** — реализованы модели `Course` и `Lesson` со связью «один ко многим», а также кастомная модель `Users` с расширенными полями.
- **Полный CRUD-функционал** — поддержка операций создания, чтения, обновления и удаления для всех моделей.
- **Мощная база данных** — использование PostgreSQL для надёжного и масштабируемого хранения данных.
- **Безопасность** — конфигурация базы данных и ключи хранятся в `.env`, который скрыт от системы контроля версий.
- **Чистый код** — структура проекта следует лучшим практикам Django, зависимости зафиксированы в `requirements.txt`.

---

## 📦 Установка и запуск
Клонируйте репозиторий и перейдите в папку проекта:
```bash
git clone https://github.com/Doczadrot/SmartEducation-LMS.git
cd SmartEducation-LMS
Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
Установите зависимости:

pip install -r requirements.txt
Создайте в корневой папке файл .env на основе .env_example и заполните своими данными:

env
SECRET_KEY='<ваш_секретный_ключ>'
DEBUG=True
DB_NAME=smart_education_app
DB_USER=postgres
DB_PASSWORD=<ваш_пароль>
DB_HOST=localhost
DB_PORT=5432


Примените миграции и создайте суперпользователя:
python manage.py migrate
python manage.py createsuperuser
Запустите сервер разработки:


python manage.py runserver
После запуска проект будет доступен по адресу:
http://127.0.0.1:8000/
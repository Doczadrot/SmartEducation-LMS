SmartEducation-LMS
Бэкенд-сервер для системы онлайн-обучения (LMS), разработанный на Django с использованием Django Rest Framework (DRF). Проект предоставляет полноценный API для управления учебными материалами, такими как курсы и уроки.

🚀 Ключевые особенности
Гибкие модели — реализованы модели Course и Lesson со связью «один ко многим», а также кастомная модель Users с расширенными полями.

Полный CRUD-функционал — поддержка операций создания, чтения, обновления и удаления для всех моделей.

Мощная база данных — использование PostgreSQL для надёжного и масштабируемого хранения данных.

Безопасность — конфигурация базы данных и ключи хранятся в .env, который скрыт от системы контроля версий.

Чистый код — структура проекта следует лучшим практикам Django, зависимости зафиксированы в requirements.txt.

Контейнеризация — проект полностью упакован в Docker для лёгкого развёртывания и управления средой.

📦 Установка и запуск
Запуск с помощью Docker Compose
Этот метод является предпочтительным, так как он автоматически поднимает все необходимые сервисы, включая базу данных PostgreSQL.

Убедитесь, что у вас установлен Docker и Docker Compose.

Клонируйте репозиторий и перейдите в папку проекта:

git clone [https://github.com/Doczadrot/SmartEducation-LMS.git](https://github.com/Doczadrot/SmartEducation-LMS.git)
cd SmartEducation-LMS

Создайте в корневой папке файл .env на основе .env_example и заполните его данными.

Запустите проект с помощью Docker Compose:

docker-compose up --build

Выполните миграции и создайте суперпользователя:

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

После запуска проект будет доступен по адресу:
http://127.0.0.1:8000/

⚙️ Файлы Docker
Dockerfile: Содержит инструкции для сборки образа Django-приложения. Он устанавливает зависимости из requirements.txt и настраивает окружение.

docker-compose.yaml: Определяет и запускает мультиконтейнерное приложение. Он связывает сервисы web (Django) и db (PostgreSQL), настраивает переменные окружения, тома и сети для их взаимодействия.

⚠️ Установка и запуск (без Docker)
Если вы хотите запустить проект без Docker, следуйте этим шагам:

Клонируйте репозиторий:

git clone [https://github.com/Doczadrot/SmartEducation-LMS.git](https://github.com/Doczadrot/SmartEducation-LMS.git)
cd SmartEducation-LMS

Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

Установите зависимости:

pip install -r requirements.txt

Создайте в корневой папке файл .env на основе .env_example и заполните его своими данными.

Установите и настройте PostgreSQL локально.

Примените миграции и создайте суперпользователя:

python manage.py migrate
python manage.py createsuperuser

Запустите сервер разработки:

python manage.py runserver

Проект будет доступен по адресу:
http://127.0.0.1:8000/
# 🎓 SmartEducation-LMS

Бэкенд-сервер для системы онлайн-обучения (LMS), разработанный на Django с использованием Django Rest Framework (DRF). Проект предоставляет полноценный API для управления учебными материалами, такими как курсы и уроки.

## 🚀 Ключевые особенности

- **Гибкие модели** — реализованы модели Course и Lesson со связью «один ко многим», а также кастомная модель Users с расширенными полями
- **Полный CRUD-функционал** — поддержка операций создания, чтения, обновления и удаления для всех моделей
- **Мощная база данных** — использование PostgreSQL для надёжного и масштабируемого хранения данных
- **Безопасность** — конфигурация базы данных и ключи хранятся в .env, который скрыт от системы контроля версий
- **Чистый код** — структура проекта следует лучшим практикам Django, зависимости зафиксированы в requirements.txt
- **Контейнеризация** — проект полностью упакован в Docker для лёгкого развёртывания и управления средой
- **CI/CD Pipeline** — автоматическое тестирование и деплой через GitHub Actions

## 🌐 Демо

- **Приложение:** http://your-server-ip:8000          1
- **Админка:** http://your-server-ip:8000/admin/        
- **API Documentation:** http://your-server-ip:8000/api/docs/        

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

---

## 🚀 CI/CD и Автоматический Деплой

Проект настроен для автоматического тестирования и деплоя через GitHub Actions.

### 📋 Что происходит автоматически:

1. **При каждом push** запускаются тесты
2. **При успешных тестах** в ветке `main` происходит автоматический деплой на сервер
3. **При ошибках** деплой не выполняется

### 🔧 Настройка GitHub Secrets

Для работы CI/CD необходимо настроить следующие секреты в GitHub:

1. Перейдите в **Settings** → **Secrets and variables** → **Actions**
2. Добавьте следующие секреты:

```
SSH_PRIVATE_KEY=-----BEGIN OPENSSH PRIVATE KEY----- ... -----END OPENSSH PRIVATE KEY-----
SERVER_HOST=your-server-ip
SERVER_USER=your-server-username

SECRET_KEY=your-django-secret-key-50-characters-long
POSTGRES_DB=your-database-name
POSTGRES_USER=your-database-user
POSTGRES_PASSWORD=your-database-password

STRIPE_PUBLISHABLE_KEY=pk_live_your_stripe_publishable_key
STRIPE_SECRET_KEY=sk_live_your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=whsec_your_stripe_webhook_secret

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 🔑 Настройка SSH ключей


```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com" -f ~/.ssh/smarteducation_deploy
```


```bash
ssh-copy-id -i ~/.ssh/smarteducation_deploy.pub your-user@your-server-ip
```


```bash
cat ~/.ssh/smarteducation_deploy
# Скопируйте весь вывод в SECRET SSH_PRIVATE_KEY в GitHub
```

### 🧪 Запуск тестов локально

```bash
# Активируйте виртуальное окружение
source venv/bin/activate

# Запустите тесты
cd SmartEducation
python manage.py test

# Или с подробным выводом
python manage.py test --verbosity=2
```

### 🔄 Workflow файл

Workflow находится в `.github/workflows/deploy.yml` и включает:

- **Тестирование**: Установка зависимостей, запуск тестов с PostgreSQL и Redis
- **Деплой**: Копирование кода на сервер, обновление зависимостей, миграции, перезапуск

### 📊 Мониторинг деплоя

- **GitHub Actions**: Проверяйте статус в разделе Actions репозитория
- **Логи сервера**: `ssh your-user@your-server-ip && tail -f /home/user/server.log`
- **Статус приложения**: http://your-server-ip:8000

### 🐛 Откат при ошибках

В случае ошибки деплоя на сервере создается бэкап:

```bash
# Подключитесь к серверу
ssh your-user@your-server-ip

# Посмотрите доступные бэкапы
ls -la /home/user/SmartEducation.backup.*

# Восстановите из бэкапа
sudo systemctl stop smarteducation
mv SmartEducation SmartEducation.broken
mv SmartEducation.backup.YYYYMMDD_HHMMSS SmartEducation
sudo systemctl start smarteducation
```

### 📝 Советы по разработке

1. **Тестируйте локально** перед push
2. **Не пушьте в main** напрямую - используйте feature ветки
3. **Проверяйте логи** GitHub Actions при ошибках
4. **Обновляйте тесты** при добавлении нового функционала

---

## 🖥️ Системные требования

### Локальная разработка:
- Python 3.12+
- PostgreSQL 15+
- Redis 6+
- Git

### Продакшен сервер:
- Ubuntu 22.04+
- 2+ GB RAM
- 20+ GB диск
- SSH доступ

---

## 📚 Документация API

После запуска приложения API документация доступна по адресам:
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/
- **OpenAPI Schema**: http://localhost:8000/api/schema/

---

## 🤝 Как внести изменения

1. **Fork** репозитория
2. Создайте **feature ветку**: `git checkout -b feature/amazing-feature`
3. **Commit** изменения: `git commit -m 'Add amazing feature'`
4. **Push** в ветку: `git push origin feature/amazing-feature`
5. Создайте **Pull Request**

---

## 📧 Поддержка

Если у вас возникли вопросы или проблемы:

- Создайте [Issue](https://github.com/Doczadrot/SmartEducation-LMS/issues)
- Проверьте [Wiki](https://github.com/Doczadrot/SmartEducation-LMS/wiki) с дополнительной документацией# SSH Deploy Test
# Тест нового SSH ключа
# Тест PEM SSH ключа

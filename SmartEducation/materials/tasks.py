import logging
from datetime import timedelta

from celery import shared_task
from celery.utils.time import timezone
from django.core.mail import send_mail
from .models import Course, Subscription
from users.models import Users

logger = logging.getLogger(__name__)

@shared_task #декоратор  который превращает обычную функцию в задачу Celery
def subscription_course_mail(course_id):
    """Находим емайлы подписчиков"""

    course = Course.objects.get(id=course_id)
    list_subscribs = Subscription.objects.filter(course=course)
    subscription_mail = [subscription.user.email for subscription in list_subscribs]

    send_emails.delay(subscription_mail) # Отложеный вызов двух функций ч

@shared_task
def send_emails(subscription_mail):
    """"Функция отправки сообщенний"""
    # Встроеная функция джанго
    send_mail('Обновление курса', 'Курс обновлён.', 'admin@example.com', subscription_mail)

@shared_task
def test_message():
    message = "Привет это тестовая функция"
    logger.info(message)
    print(message)
    return message

@shared_task
def deactivate_users():
    """Функция удаление неактивных пользователей"""
    now_data = timezone.now()
    thirty_days = timedelta(days=30)
    date_month_ago = now_data - thirty_days

    inactive_users = Users.objects.filter(last_login__lt=date_month_ago) #выявили пользователей
    # Получаем список пользователей, которых нужно заблокировать
    for user in inactive_users:
        user.is_active = False
        user.save()



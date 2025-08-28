
from datetime import timedelta
from django.conf import settings
from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from materials.models import Course, Subscription


@shared_task
def subscription_course_mail(course_id, course_title):
    try:
        subscriptions = Subscription.objects.filter(course=course_id)
        if not subscriptions.exists():
            print(f"Подписок не найдено для курса с ID: {course_id}")
            return

        for subscription in subscriptions:
            email_address = subscription.user.email
            subject = f"Обновление курса: {course_title}"
            message = f"Здравствуйте, {subscription.user.username}!\n\nКурс '{course_title}' был обновлен."

            print(f"Отправка письма на: {email_address} для курса: {course_title}")
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email_address],
                fail_silently=False
            )

    except Exception as e:
        print(f"Произошла ошибка в subscription_course_mail: {e}")


@shared_task
def deactivate_users():
    """Задача для деактивации неактивных пользователей"""
    User = get_user_model()
    thirty_days_ago = timezone.now() - timedelta(days=30)

    deactivated_count = User.objects.filter(last_login__lt=thirty_days_ago, is_active=True).update(is_active=False)

    print(f"--- Запуск задачи: deactivate_users ---")
    print(f"--- Задача завершена. Деактивировано {deactivated_count} пользователей. ---")


@shared_task
def delete_deactivated_users():
    """Функция для полного удаления пользователей заходили более 60 дней."""
    print("--- Запуск задачи: delete_deactivated_users ---")
    User = get_user_model()
    sixty_days_ago = timezone.now() - timedelta(days=60)

    users_to_delete = User.objects.filter(last_login__lt=sixty_days_ago, is_active=False)
    deleted_count = users_to_delete.count()
    users_to_delete.delete()

    print(f"--- Задача завершена. Удалено {deleted_count} пользователей. ---")

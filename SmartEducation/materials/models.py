from django.conf import settings
from django.db import models
from django.db.models import CASCADE # Импортируем CASCADE для удаления связанных объектов

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    image = models.ImageField(upload_to='materials/avatar', verbose_name='AVATAR', blank=True, null=True)
    description = models.TextField(blank=True, help_text='Введите описание', verbose_name='Описание курса')
    author = models.ForeignKey("users.Users",on_delete=CASCADE) # Связь с моделью пользователя, который создал курс
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=100)
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название урока')
    preview = models.ImageField(upload_to='materials/avatar', verbose_name='AVATAR', blank=True, null=True)
    description = models.TextField(blank=True, help_text='Введите описание', verbose_name='Описание урока')
    link_video = models.URLField(help_text="Ведите ссылку", unique=True, blank=True, null=True)
    course = models.ForeignKey("materials.Course", on_delete=CASCADE) # Связь с моделью курса, к которому относится урок
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name='Автор', blank=True, null=True)


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        unique_together = ('user', 'course')  # Уникальное ограничение
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f"Подписка пользователя {self.user} на курс  {self.course.title}"

from django.db import models
from django.db.models import CASCADE


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    image = models.ImageField(upload_to='materials/avatar', verbose_name='AVATAR', blank=True, null=True)
    description = models.TextField(blank=True, help_text='Введите описание', verbose_name='Описание курса')
    author = models.ForeignKey("users.Users",on_delete=CASCADE)

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название урока')
    preview = models.ImageField(upload_to='materials/avatar', verbose_name='AVATAR', blank=True, null=True)
    description = models.TextField(blank=True, help_text='Введите описание', verbose_name='Описание урока')
    link_video = models.URLField(help_text="Ведите ссылку", unique=True)
    course = models.ForeignKey("materials.Course", on_delete=CASCADE)

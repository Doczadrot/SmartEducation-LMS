
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Users(AbstractUser):
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        unique=True,
        help_text="Введите номер телефона в международном формате"
    )
    city = models.CharField(max_length=200, verbose_name='Город', help_text='Введите название города')
    avatar = models.ImageField(upload_to='users/avatar',verbose_name='AVATAR', blank=True, null=True)
    groups = models.ManyToManyField('auth.Group',blank=True,
    help_text='Группы, к которым принадлежит этот пользователь. Пользователь получит все права, предоставленные каждой из его групп',
        related_name="customuser_set",  # Важно для избежания конфликтов related_name
        related_query_name="customuser")
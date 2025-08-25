
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import CASCADE
from materials.models import Lesson, Course

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


class Pays(models.Model):
    payment_urls = models.URLField(max_length=1000, null=True, blank=True, verbose_name='Cсылка на платеж')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    paid_course = models.ForeignKey(Course, on_delete=CASCADE, null=True, blank=True, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=CASCADE, null=True, blank=True, verbose_name='Оплаченный урок')
    summ_pays = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Сумма оплаты')
    variant_pays = models.CharField(max_length=20, choices=(('chash', 'Наличные'),
                                                            ('transfer', 'Перевод')))

    def __str__(self):
        return f"Платеж от {self.user.email} на сумму {self.summ_pays} за {self.paid_course if self.paid_course else self.paid_lesson}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ['-date']
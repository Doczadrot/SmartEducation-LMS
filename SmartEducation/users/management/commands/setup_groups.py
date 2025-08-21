from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from materials.models import Course, Lesson

class Command(BaseCommand):
    help = 'Создает группу "Модератор" и назначает ей права.'

    def handle(self, *args, **options):
        self.stdout.write('Создание группы модераторов...')

        moderator_group, created = Group.objects.get_or_create(name='Модератор')

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор" создана.'))
        else:
            self.stdout.write('Группа "Модератор" уже существует.')

        # Выдача прав
        lesson_ct = ContentType.objects.get_for_model(Lesson)
        course_ct = ContentType.objects.get_for_model(Course)

        # Права на просмотр и изменение
        permissions = [
            Permission.objects.get(codename='view_lesson', content_type=lesson_ct),
            Permission.objects.get(codename='change_lesson', content_type=lesson_ct),
            Permission.objects.get(codename='view_course', content_type=course_ct),
            Permission.objects.get(codename='change_course', content_type=course_ct),
        ]

        # Назначение прав
        moderator_group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Права успешно назначены группе "Модератор".'))
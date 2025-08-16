from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Заполняет базу данных фикстурами из папки fixtures'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаю заполнение базы данных...')

        try:
            call_command('loaddata', 'pays.json')
            self.stdout.write(self.style.SUCCESS('База данных успешно заполнена!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Произошла ошибка: {e}'))
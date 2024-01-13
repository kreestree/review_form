from django.core.management import BaseCommand

from problems.models import FactoryArea


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Добавление записей')
        factory_areas = ['Намотки', 'Первой сборки', 'Второй сборки']
        for area in factory_areas:
            new_area, is_created = FactoryArea.objects.get_or_create(area_title=area)
            if is_created:
                self.stdout.write(self.style.SUCCESS(f'Запись "{new_area}" создана'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Запись "{new_area}" уже существует'))

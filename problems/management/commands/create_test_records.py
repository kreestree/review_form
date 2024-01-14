from django.core.management import BaseCommand
import csv

from problems.models import FactoryArea, Equipment


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Добавление записей')

        areas = ['Намотка обмоток',
                         'Магнитопроводов',
                         'Сборки',
                         'ТВО',
                         'Изготовление изоляции',
                         'Металлоконструкций']
        for area in areas:
            new_area, is_created = FactoryArea.objects.get_or_create(area_title=area)
            if is_created:
                self.stdout.write(self.style.SUCCESS(f'Запись "{new_area}" создана'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Запись "{new_area}" уже существует'))

        winding_area = FactoryArea.objects.get(area_title='Намотка обмоток')
        magnetic_circuits_area = FactoryArea.objects.get(area_title='Магнитопроводов')
        assembly_area = FactoryArea.objects.get(area_title='Сборки')
        tvo_area = FactoryArea.objects.get(area_title='ТВО')
        isolation_area = FactoryArea.objects.get(area_title='Изготовление изоляции')
        metal_structures_area = FactoryArea.objects.get(area_title='Металлоконструкций')

        areas = {
            'Намотка обмоток': winding_area,
            'Магнитопроводов': magnetic_circuits_area,
            'Сборки': assembly_area,
            'ТВО': tvo_area,
            'Изготовление изоляции': isolation_area,
            'Металлоконструкций': metal_structures_area,
        }

        with open('problems/management/commands/records.csv', 'r', encoding='utf-8', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)
            for row in reader:
                factory_area_name, equipment_name, inventory_number = map(str.strip, row)
                if inventory_number:
                    new_equipment, is_created = Equipment.objects.get_or_create(equipment_name=equipment_name,
                                                                                inventory_number=inventory_number,
                                                                                factory_area=areas[factory_area_name])
                else:
                    new_equipment, is_created = Equipment.objects.get_or_create(equipment_name=equipment_name,
                                                                                factory_area=areas[factory_area_name])

                if is_created:
                    self.stdout.write(self.style.SUCCESS(f'Запись "{new_equipment}" создана'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Запись "{new_equipment}" уже существует'))

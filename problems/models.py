from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe


class Equipment(models.Model):
    '''Модель для оборудования.'''

    equipment_name = models.CharField(max_length=200, verbose_name='Оборудование')
    inventory_number = models.CharField(max_length=10,
                                        verbose_name='Инвентарный номер',
                                        null=True,
                                        blank=True, )
    factory_area = models.ForeignKey('FactoryArea',
                                     on_delete=models.CASCADE,
                                     verbose_name='Участок',
                                     related_name='equipment')

    def __str__(self) -> str:
        return f'{self.equipment_name}, инв.№: {self.inventory_number}'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class FactoryArea(models.Model):
    '''Модель для участка.'''

    area_title = models.CharField(max_length=150, verbose_name='Участок')

    def __str__(self) -> str:
        return str(self.area_title)

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'
        ordering = ['area_title']


class Problems(models.Model):
    '''Модель для проблем.'''

    factory_area = models.ForeignKey('FactoryArea',
                                     on_delete=models.CASCADE,
                                     verbose_name='Участок')
    equipment = models.ForeignKey('Equipment',
                                  on_delete=models.PROTECT,
                                  verbose_name='Оборудование')
    problem_description = models.TextField(max_length=2000, verbose_name='Проблема')
    employee_full_name = models.CharField(max_length=150, verbose_name='Ф.И.О. работника')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self) -> str:
        return f'Проблема на участке "{self.factory_area}"'

    def get_absolute_url(self) -> str:
        return reverse('problem', kwargs={'problem_pk': self.pk})

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'


class Image(models.Model):
    '''Модель для изображений.'''

    problem = models.ForeignKey('Problems',
                                on_delete=models.CASCADE,
                                related_name='images',
                                verbose_name='Проблема')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')

    @property
    def thumbnail_preview(self) -> str:
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" target="_blank">'
                             f'<img src="{self.image.url}" width=auto height="200" />'
                             f'</a>')
        return ""

    def __str__(self) -> str:
        return self.image.url

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

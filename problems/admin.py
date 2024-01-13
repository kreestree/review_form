from django.contrib import admin
from django.db.models import QuerySet
from django.utils.safestring import mark_safe
from problems.models import Image, Problems, Equipment, FactoryArea


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    '''Модель для отображения изображений в админ-панели.'''

    list_display = ('problem', 'thumbnail_preview')
    readonly_fields = ['thumbnail_preview']


class ImageInline(admin.StackedInline):
    '''Inline для отображения изображений в модели проблем.'''
    readonly_fields = ['thumbnail_preview']
    model = Image
    extra = 0


@admin.register(Problems)
class ProblemAdmin(admin.ModelAdmin):
    '''Модель для отображения проблем в админ-панели.'''
    list_display = ('time_create',
                    'factory_area',
                    'problem_description',
                    'employee_full_name',
                    'show_photos')
    list_display_links = ('time_create', 'problem_description')
    search_fields = ('factory_area__area_title', 'employee_full_name')
    list_filter = ('time_create', 'factory_area__area_title')
    inlines = [ImageInline]

    def get_queryset(self, request) -> QuerySet:
        return Problems.objects.prefetch_related('images')

    def show_photos(self, problem) -> str:
        images = problem.images.all()
        if images:
            return mark_safe('<br><br>\n'.join(list(map(lambda image: image.thumbnail_preview, images))))

    show_photos.short_description = 'Фото'
    show_photos.allow_tags = True


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    '''Модель для отображения оборудования в админ-панели.'''
    list_display = 'equipment_name', 'inventory_number', 'factory_area'


admin.site.register(FactoryArea)

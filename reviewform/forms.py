from io import BytesIO

from django import forms
from django.core.exceptions import ValidationError
import PIL
from problems.models import Problems
from django.core.files import File


class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImageInput())
        super().__init__(*args, **kwargs)

    @staticmethod
    def compress(images):
        try:
            for i, image in enumerate(images):
                im = PIL.Image.open(image)
                im = im.convert('RGB')
                im_io = BytesIO()  # create a BytesIO object
                im.save(im_io, 'JPEG', quality=90, optimize=True)  # save image to BytesIO object
                images[i] = File(im_io, name=image.name)  # create a django-friendly Files object
        except PIL.UnidentifiedImageError:
            raise ValidationError('Произошла ошибка при обработке изображений')
        return images

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            images = [single_file_clean(d, initial) for d in data]
        else:
            images = [single_file_clean(data, initial)]

        if images:
            if len(images) > 10:
                raise ValidationError('Максимум 10 изображений')
            for image in images:
                if image.content_type.split('/')[0] != 'image':
                    raise ValidationError('Допускаются только изображения')
                if image.size > 5_242_880:
                    raise ValidationError('Изображение не должно весить больше 5 МБ')
            self.compress(images)
        return images


class AddProblemForm(forms.ModelForm):
    image_field = MultipleImageField(required=False, label = 'Прикрепите изображения (не более десяти)')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_field'].widget.attrs.update({'accept': "image/*", 'class': 'form-control'})

        for field in ('factory_area', 'equipment'):
            self.fields[field].empty_label = 'Не выбран'
            self.fields[field].widget.attrs['class'] = 'form-select'

        for field in 'problem_description', 'employee_full_name':
            self.fields[field].widget.attrs.update({'placeholder': self.fields[field].label})

        for field in 'problem_description', 'employee_full_name':
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Problems
        fields = ['factory_area', 'equipment', 'problem_description', 'employee_full_name']
        labels = {
            'problem_description': 'Опишите проблему',
            'employee_full_name': 'Ваше имя'
        }

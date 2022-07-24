from .models import Kniteka
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class KnitekaForm(ModelForm):
    class Meta:
        model = Kniteka
        fields = ['title', 'anons']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            # 'texstura': Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Текст статті'
            # }),
            # 'date': DateTimeInput(attrs={
            #     'class': 'form-control datetimepicker-input',
            #     'placeholder': 'YYYY-mm-dd H:M:S'
            # }),

        }
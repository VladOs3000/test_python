from django import forms
from .models import Kniteka
from .models import Book
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, FileField

class KnitekaForm(ModelForm):
    class Meta:
        model = Kniteka
        fields = ['title', 'anons', 'gener1', 'gener2', 'gener3', 'formatbook', 'path']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва'
            }),
            'gener1': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр'
            }),
            'gener2': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр'
            }),
            'gener3': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр'
            }),
            'formatbook': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Назва'
            }),
            'anons': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Анотація'
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

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pdf']
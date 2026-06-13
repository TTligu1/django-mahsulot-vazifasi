from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from myfiles.models import Mahsulot


class MahsulotForm(ModelForm):

    class Meta:
        model = Mahsulot
        fields = '__all__'

        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'narx': forms.TextInput(attrs={'class': 'form-control'}),
            'kategoriya': forms.TextInput(attrs={'class': 'form-control'}),
            'soni': forms.TextInput(attrs={'class': 'form-control'}),
            'faol': forms.TextInput(attrs={'class': 'form-control'}),
            'tavsif': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_yili(self):
        y = self.cleaned_data['yili']

        if y < 1600 or y > 2025:
            raise ValidationError('Yili xato')

        return y

    def clean(self):
        data = super().clean()
        return data
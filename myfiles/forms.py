from django import forms
from .models import Mahsulot


class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Mahsulot
        fields = ['nomi', 'janr']  # Modellaringiz maydonlariga qarab o'zgartiring

        # O'sha siz HTMLga yozib qo'ygan kod shu yerda bo'lishi kerak:
        widgets = {
            'nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'janr': forms.Select(attrs={'class': 'form-control'}),
        }
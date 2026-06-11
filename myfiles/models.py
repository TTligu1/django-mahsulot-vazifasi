from django.db import models


class Mahsulot(models.Model):
    JANR = [('drama', 'Drama'), ('komediya', 'Komediya')]
    nomi = models.CharField(max_length=150)
    rejissor = models.CharField(max_length=120)
    yili = models.IntegerField()
    janr = models.CharField(max_length=20, choices=JANR)
    reyting = models.DecimalField(max_digits=3, decimal_places=1)
# forms.py



from django import forms
from . models import Mahsulot

class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Mahsulot
        fields = ['nomi', 'rejissor', 'yili', 'janr', 'reyting']

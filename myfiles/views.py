from django.contrib.gis.db.backends.postgis.const import POSTGIS_TO_GDAL
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from .forma import MahsulotForm
from .models import Mahsulot

def royxat(request):
    mahsulotlar = Mahsulot.objects.all()
    return render(request, 'royxat.html', {
        'mahsulotlar': mahsulotlar
    })



def qoshish(request):
    if request.method == 'POST':
        form = MahsulotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('royxat')
    else:
        form = MahsulotForm()
    return render(request, 'forma.html', {'form': form})

def tahrirlash(request , pk):
    if request.method == 'POST':
        mahsulot = get_object_or_404(Mahsulot, pk=pk)
        form = MahsulotForm(request.POST or None, instance=mahsulot)
        if form.is_valid():
            form.save()
            return redirect('royxat')
        return render (request , 'forma.html', {'form': form})


def ochirish(request , pk):
    mahsulot = get_object_or_404(Mahsulot, pk=pk)
    if request.method == 'POST':
        mahsulot.delete()
        return redirect('royxat')
    return render(request, 'ochirish.html', {'form': Mahsulot})

def clean_yili(self):
    y = self.cleaned_data['yili']
    if y < 1600 or y > 2025:
        raise ValidationError('yili error')
    return y

def clean(self):
    data = super().clean()
    if data.get('yili') == 'oziq-ovqat,Oziq-ovqat' and (data.get('qoshilgan_sana') or 0) > 7    :
        raise ValidationError('qoshilgan_sana error')
    return data
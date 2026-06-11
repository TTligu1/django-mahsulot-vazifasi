from django.shortcuts import render, redirect, get_object_or_404
from .forms import MahsulotForm
from .models import Mahsulot


def qoshish(request):
    if request.method == 'POST':
        form = MahsulotForm(request.POST)
        if form.is_valid():
            form.save()  # bazaga yozadi
            return redirect(
                'mahsulotlar_roʻyxati')  # Ma'lumot saqlangach, boshqa sahifaga yo'naltirish (ixtiyoriy, lekin tavsiya etiladi)
    else:
        form = MahsulotForm()

    # Bu return ikkala holat uchun ham ishlashi uchun if/else lardan tashqarida turishi kerak
    return render(request, 'forma.html', {'form': form})


def tahrirlash(request, pk):
    film = get_object_or_404(Mahsulot, pk=pk)
    form = MahsulotForm(request.POST or None, instance=film) # instance = muhim!
    if form.is_valid():
        form.save()
        return redirect('royxat')
    return render(request, 'forma.html', {'form': form})


def ochirish(request, pk):
    mahsulot = get_object_or_404(Mahsulot, pk=pk)
    if request.method == 'POST':
        mahsulot.delete()
        return redirect('royxat')
    return render(request, 'ochirish.html', {'mahsulot': mahsulot})

# bitta maydon: yil 1900..2025 oralig'ida
def clean_yili(self):
    y = self.cleaned_data['yili']
    if y < 1900 or y > 2025:
        raise forms.ValidationError('Yil notoʻgʻri')
    return y
# bir nechta maydon: drama bo'lsa reyting 7+ bo'lsin
def clean(self):
    data = super().clean()
    if data.get('janr') == 'drama' and (data.get('reyting') or 0) < 7:
        raise forms.ValidationError('Drama uchun reyting past')
    return data
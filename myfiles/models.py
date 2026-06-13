from django.db import models


class Mahsulot(models.Model):
    Kategoryasi = [('oziq-ovqat','Oziq-ovqat'),('kiyim','Kiyim'),('texnika','Texnika' )]
    nomi = models.CharField(max_length=150)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    kategoriya = models.CharField(choices=Kategoryasi, max_length=50)
    soni = models.PositiveIntegerField()
    faol = models.BooleanField()
    tavsif = models.TextField(blank=True)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)



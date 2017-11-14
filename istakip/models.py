from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class IsTakip(models.Model):
    kullanici = models.ForeignKey(User)
    başlık = models.CharField(max_length=25, blank=True)
    acıklama = models.TextField(max_length=250)
    oluşturma_tarihi = models.DateTimeField(default=datetime.now(),blank=True)
    sonlanma_tarihi = models.DateTimeField(null=True,blank=True)
    başlangıç_tarihi = models.DateTimeField(null=True,blank=True)
    durumu = models.CharField(max_length=2,default=1)
    durum_güncelleme_tarihi = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.başlık



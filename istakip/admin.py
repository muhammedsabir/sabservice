from django.contrib import admin
from istakip.models import *
from .models import IsTakip

class IsTakipAdmin(admin.ModelAdmin):
    list_display = ('kullanici','başlık','acıklama','oluşturma_tarihi','sonlanma_tarihi','başlangıç_tarihi','durumu','durum_güncelleme_tarihi')
    list_filter = ["kullanici","durumu"]
    #search_fields = ["kullanici"]
    class Meta:
        model = IsTakip


admin.site.register(IsTakip,IsTakipAdmin)

# Register your models here.

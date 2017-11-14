from rest_framework import serializers
from .models import IsTakip

class IsTakipSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsTakip
        fields = '__all__'

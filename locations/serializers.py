# serializers.py
from rest_framework import serializers
from .models import Province

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

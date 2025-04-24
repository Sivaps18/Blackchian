from rest_framework import serializers
from .models import RevenueShare

class RevenueShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueShare
        fields = '__all__'

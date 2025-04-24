from rest_framework import serializers
from .models import UserVerificationData

class UserVerificationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVerificationData
        fields = '__all__'

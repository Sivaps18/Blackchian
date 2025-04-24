from rest_framework import serializers
from .models import ComplianceRecord

class ComplianceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceRecord
        fields = '__all__'

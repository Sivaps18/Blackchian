from rest_framework import serializers
from .models import ContentModerationAction

class ContentModerationActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModerationAction
        fields = '__all__'

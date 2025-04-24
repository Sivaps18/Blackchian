from rest_framework import serializers
from .models import GovernanceProposal

class GovernanceProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernanceProposal
        fields = '__all__'

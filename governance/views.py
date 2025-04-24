from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import GovernanceProposal
from .serializers import GovernanceProposalSerializer

class GovernanceProposalViewSet(viewsets.ModelViewSet):
    queryset = GovernanceProposal.objects.all()
    serializer_class = GovernanceProposalSerializer

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        proposal = self.get_object()
        # Implement voting mechanism here
        # Example: record vote, update proposal status, notify users
        # This is a placeholder implementation
        return Response({'status': 'vote recorded'}, status=status.HTTP_200_OK)

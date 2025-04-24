from rest_framework import viewsets
from .models import RevenueShare
from .serializers import RevenueShareSerializer

class RevenueShareViewSet(viewsets.ModelViewSet):
    queryset = RevenueShare.objects.all()
    serializer_class = RevenueShareSerializer

    # Example: Add payment processing or payout management methods here

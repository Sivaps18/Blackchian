from rest_framework import viewsets
from .models import ComplianceRecord
from .serializers import ComplianceRecordSerializer

class ComplianceRecordViewSet(viewsets.ModelViewSet):
    queryset = ComplianceRecord.objects.all()
    serializer_class = ComplianceRecordSerializer

    # Example: Add audit trails or compliance checks here

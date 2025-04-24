from rest_framework import viewsets
from .models import AnalyticsMetric
from .serializers import AnalyticsMetricSerializer

class AnalyticsMetricViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsMetric.objects.all()
    serializer_class = AnalyticsMetricSerializer

    # Example: Add data aggregation or reporting methods here

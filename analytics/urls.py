from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalyticsMetricViewSet

router = DefaultRouter()
router.register(r'metrics', AnalyticsMetricViewSet, basename='analyticsmetric')

urlpatterns = [
    path('', include(router.urls)),
]

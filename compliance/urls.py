from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplianceRecordViewSet

router = DefaultRouter()
router.register(r'records', ComplianceRecordViewSet, basename='compliancerecord')

urlpatterns = [
    path('', include(router.urls)),
]

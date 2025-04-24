from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RevenueShareViewSet

router = DefaultRouter()
router.register(r'shares', RevenueShareViewSet, basename='revenueshare')

urlpatterns = [
    path('', include(router.urls)),
]

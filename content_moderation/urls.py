from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentModerationActionViewSet

router = DefaultRouter()
router.register(r'actions', ContentModerationActionViewSet, basename='contentmoderationaction')

urlpatterns = [
    path('', include(router.urls)),
]

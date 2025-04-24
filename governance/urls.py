from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GovernanceProposalViewSet

router = DefaultRouter()
router.register(r'proposals', GovernanceProposalViewSet, basename='proposal')

urlpatterns = [
    path('', include(router.urls)),
]

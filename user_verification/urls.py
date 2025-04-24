from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserVerificationDataViewSet, CustomObtainAuthToken, LogoutView

router = DefaultRouter()
router.register(r'verifications', UserVerificationDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='api_token_logout'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/governance/', include('governance.urls')),
    path('api/content-moderation/', include('content_moderation.urls')),
    path('api/user-verification/', include('user_verification.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/revenue-sharing/', include('revenue_sharing.urls')),
    path('api/compliance/', include('compliance.urls')),
]

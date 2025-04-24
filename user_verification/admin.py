from django.contrib import admin
from .models import UserVerificationData

@admin.register(UserVerificationData)
class UserVerificationDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'verification_status', 'verification_method', 'reputation_points')
    list_filter = ('verification_status', 'verification_method')
    search_fields = ('user__username',)

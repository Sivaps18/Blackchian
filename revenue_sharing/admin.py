from django.contrib import admin
from .models import RevenueShare

@admin.register(RevenueShare)
class RevenueShareAdmin(admin.ModelAdmin):
    list_display = ('share_id', 'user', 'amount', 'source', 'timestamp')
    list_filter = ('source',)
    search_fields = ('user__username', 'source')

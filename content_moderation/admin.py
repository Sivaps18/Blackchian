from django.contrib import admin
from .models import ContentModerationAction

@admin.register(ContentModerationAction)
class ContentModerationActionAdmin(admin.ModelAdmin):
    list_display = ('action_id', 'moderator', 'content_id', 'action_type', 'timestamp')
    list_filter = ('action_type',)
    search_fields = ('moderator__username', 'content_id', 'reason')

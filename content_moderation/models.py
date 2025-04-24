from django.db import models
from django.contrib.auth.models import User

class ContentModerationAction(models.Model):
    ACTION_TYPE_CHOICES = [
        ('flag', 'Flag'),
        ('remove', 'Remove'),
        ('suspend_user', 'Suspend User'),
        ('warn', 'Warn'),
    ]

    action_id = models.AutoField(primary_key=True)
    moderator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moderation_actions')
    content_id = models.CharField(max_length=255)  # Assuming content is identified by a string ID
    action_type = models.CharField(max_length=20, choices=ACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    def __str__(self):
        return f"Action {self.action_type} on content {self.content_id} by {self.moderator.username}"

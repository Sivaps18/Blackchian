from django.db import models

class AnalyticsMetric(models.Model):
    METRIC_TYPE_CHOICES = [
        ('user_activity', 'User Activity'),
        ('engagement', 'Engagement'),
        ('content_performance', 'Content Performance'),
        ('revenue', 'Revenue'),
    ]

    metric_id = models.AutoField(primary_key=True)
    metric_type = models.CharField(max_length=50, choices=METRIC_TYPE_CHOICES)
    metric_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_type} - {self.metric_value} at {self.timestamp}"

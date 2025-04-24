from django.contrib import admin
from .models import AnalyticsMetric

@admin.register(AnalyticsMetric)
class AnalyticsMetricAdmin(admin.ModelAdmin):
    list_display = ('metric_id', 'metric_type', 'metric_value', 'timestamp')
    list_filter = ('metric_type',)
    search_fields = ('metric_type',)

from django.contrib import admin
from .models import ComplianceRecord

@admin.register(ComplianceRecord)
class ComplianceRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'regulation_name', 'compliance_status', 'last_audit_date')
    list_filter = ('compliance_status',)
    search_fields = ('regulation_name',)

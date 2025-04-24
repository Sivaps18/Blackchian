from django.db import models

class ComplianceRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    regulation_name = models.CharField(max_length=255)
    compliance_status = models.CharField(max_length=50)
    last_audit_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ComplianceRecord {self.record_id} - {self.regulation_name} - {self.compliance_status}"

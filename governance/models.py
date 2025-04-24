from django.db import models
from django.contrib.auth.models import User

class GovernanceProposal(models.Model):
    PROPOSAL_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('executed', 'Executed'),
    ]

    proposal_id = models.AutoField(primary_key=True)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposals')
    proposal_type = models.CharField(max_length=100)
    proposal_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    proposal_status = models.CharField(max_length=20, choices=PROPOSAL_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Proposal {self.proposal_id} by {self.submitter.username} - {self.proposal_status}"

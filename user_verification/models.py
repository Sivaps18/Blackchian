from django.db import models
from django.contrib.auth.models import User

class UserVerificationData(models.Model):
    VERIFICATION_STATUS_CHOICES = [
        ('unverified', 'Unverified'),
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_STATUS_CHOICES, default='unverified')
    verification_method = models.CharField(max_length=100, blank=True, null=True)
    reputation_points = models.IntegerField(default=0)

    def __str__(self):
        return f"UserVerificationData for {self.user.username} - {self.verification_status}"

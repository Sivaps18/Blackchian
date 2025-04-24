from django.db import models
from django.contrib.auth.models import User

class RevenueShare(models.Model):
    share_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='revenue_shares')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"RevenueShare {self.share_id} for {self.user.username} - {self.amount}"

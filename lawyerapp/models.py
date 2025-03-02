from django.db import models
from clientapp.models import clients
from django.utils import timezone

class request_payment(models.Model):
    client = models.ForeignKey(clients, on_delete=models.CASCADE)
    amt = models.FloatField()
    due_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    invoice_number = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    
    def __str__(self):
        return f"Payment request for {self.client.name} - ${self.amt}"
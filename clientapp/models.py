from django.db import models
from django.conf import settings
from adminapp.models import lawyer

from userapp.models import Appointment

# Create your models here.
class clients(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    lid = models.ForeignKey(lawyer,models.CASCADE)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class messages(models.Model):
    title = models.CharField(max_length=30)
    msg = models.CharField(max_length=1000)
    client = models.ForeignKey('clients', on_delete=models.CASCADE)
    lawyer_name = models.ForeignKey(lawyer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message To {self.client} From {self.lawyer_name} at {self.created_at.strftime('%H:%M:%S')}"

class Case(models.Model):
    client = models.ForeignKey(clients, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    description = models.TextField()
    document = models.FileField(upload_to='case_documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Case for {self.client.name} - {self.created_at.strftime('%Y-%m-%d')}"    
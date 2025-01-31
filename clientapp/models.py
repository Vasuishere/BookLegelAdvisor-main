from django.db import models
from django.conf import settings
from adminapp.models import lawyer
# from userapp.models import case_categories

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
    message = models.CharField(max_length=1000)
    # client = models.
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender}send message to {self.client}"
    

from django.db import models

# Create your models here.
class lawyers(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    experience = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    def __str__(self):
        return self.name

class apponitment(models.Model):
    Name = models.CharField(max_length=25)
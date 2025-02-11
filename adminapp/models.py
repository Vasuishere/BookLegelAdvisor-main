from django.db import models

# Create your models here.
class adminuser(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class lawyer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Education(models.Model):
    lawyer = models.ForeignKey(lawyer, on_delete=models.CASCADE, related_name="educations")
    degree = models.CharField(max_length=100)
    expertise = models.CharField(max_length=25)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"Education - {self.lawyer}"
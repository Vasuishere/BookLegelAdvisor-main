from django.db import models
from clientapp.models import clients
from adminapp.models import lawyer

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=25)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Attorneys(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=30)
    image = models.FileField(upload_to='image/')
    def __str__(self):
        return self.name
    

class Client_Review(models.Model):
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    discription = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')
    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.FileField(upload_to='image/')
    tittle = models.CharField(max_length=100)
    des = models.TextField(max_length=1500)
    
    def __str__(self):
        return self.tittle

class Types_Law(models.Model):
    law_tittle = models.CharField(max_length=50)
    point = models.CharField(max_length=150)
    detail = models.CharField(max_length=550)
    image = models.ImageField(upload_to='image/')
    def __str__(self):
        return self.law_tittle

class Practice_Area(models.Model):
    Practice_Area_det = models.CharField(max_length=1000)
    Practice_Area_law_title = models.CharField(max_length=50)
    Practice_Area_pid = models.ForeignKey(Types_Law,models.CASCADE)
    Practice_Area_image = models.ImageField(upload_to='image/')


class case_categories(models.Model):
    case_categories = models.CharField(max_length=50)
    def __str__(self):
        return self.case_categories
    
class case_studies(models.Model):
    case_studies_tittle = models.CharField(max_length=100)
    case_studies_date = models.CharField(max_length=20)
    detail = models.TextField(max_length=2000)
    case_studies_image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(case_categories,models.CASCADE)
    def __str__(self):
        return self.case_studies_tittle

class Appointment(models.Model):
    userid = models.ForeignKey(clients,models.CASCADE)
    lid = models.ForeignKey(lawyer,models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneno = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    message = models.TextField(max_length=2000)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    up_doc1 = models.FileField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.name


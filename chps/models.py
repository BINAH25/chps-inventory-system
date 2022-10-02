from django.db import models
from datetime import datetime
# Create your models here.


class Registration(models.Model):
    registration = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    nhis_number = models.CharField(max_length=100)
    complaint = models.TextField(max_length=1000)
    date1 = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    pulse = models.CharField(max_length=100)
    observation = models.TextField(max_length=1000)
    diagnosis = models.TextField(max_length=1000)
    treatment = models.TextField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.firstname + " " + self.lastname
    

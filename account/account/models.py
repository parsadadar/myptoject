from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    password= models.CharField(max_length=30, null=True, blank=True, default=None)
    email = models.CharField(max_length=50, null=True, blank=True, default=None)

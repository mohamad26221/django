from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    fathername = models.CharField(max_length=20,default=None,null=True)
    mothername = models.CharField(max_length=20,default=None,null=True)
    phone = models.IntegerField(unique=True,null=True)
    idNumber = models.IntegerField(default=None,null=True)
    idNationalNumber = models.IntegerField(unique=True,default=None,null=True)
    university = models.CharField(max_length=20,default=None,null=True)
    faculty = models.CharField(max_length=20,default=None,null=True)
    section = models.CharField(max_length=20,default=None,null=True)
    unitNumber = models.IntegerField(default=None,null=True)
    roomNumber = models.IntegerField(default=None,null=True)
    city = models.CharField(max_length=20,default=None,null=True)
    year = models.IntegerField(default=None,null=True)
    status = models.CharField(max_length=20,default=None,null=True)
    job = models.CharField(max_length=20,null=True,default=None)
    typejob = models.CharField(max_length=20,null=True,default=None)
    token = models.CharField(max_length=20,null=True,default=None)
    email = models.EmailField(unique=True,null=False)
    

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['username']



    def __str__(self):
        return self.username
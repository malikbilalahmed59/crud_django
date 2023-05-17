from django.db import models
from django.contrib.auth.hashers import make_password

class UserInformation(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    Cnic_number = models.CharField(max_length=13)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.first_name+self.last_name


# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    
    """ Extend User Model """
    
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(max_length=10)
    phone_number = models.CharField(max_length=10)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
    
   
        

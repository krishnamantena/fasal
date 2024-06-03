#from django.db import models

# Create your models here.
from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


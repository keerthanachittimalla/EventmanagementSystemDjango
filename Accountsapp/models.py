#from django.db import models

# Create your models here.
# models.py

'''from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20)#, choices=[('organizers', 'Organizer'), ('students', 'Student')])
    
    def __str__(self):
        return self.username'''
'''
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.username
'''
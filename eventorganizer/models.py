from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser # for role column in user table
# Create your models here.
class Oraganizerdata(models.Model):
    event_Id=models.IntegerField()
    event_Name=models.CharField(max_length=40)
    event_Location=models.CharField(max_length=200)
    event_Image=models.ImageField(upload_to="static")
    event_Time=models.TimeField()
    event_Date=models.DateField()
    event_Price=models.IntegerField()
    organizerid=models.CharField(max_length=8)
    event_orginfo=models.CharField(max_length=300)


'''class Registrations(models.Model):
    event=models.ForeignKey(Oraganizerdata,on_delete=models.CASCADE)
    #student=models.ForeignKey(User,on_delete=models.CASCADE)
    #student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    registration_date=models.DateTimeField(auto_now_add=True)'''

class Registeredto(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=40)
    eventid=models.IntegerField()
    eventname=models.CharField(max_length=40)
    organizerid=models.IntegerField()

# models.py

#from django.db import models
'''
class CustomUser(AbstractUser):
    role = models.CharField(max_length=20)#, choices=[('organizers', 'Organizer'), ('students', 'Student')])
'''
class Meta:
    db_table="Events"

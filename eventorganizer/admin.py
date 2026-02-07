from django.contrib import admin
from .models import Oraganizerdata,Registeredto #,Registrations
#from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Oraganizerdata)
admin.site.register(Registeredto)
#admin.site.register(Registrations)

# Create groups
'''
organizers_group, created = Group.objects.get_or_create(name="organizers")
students_group, created = Group.objects.get_or_create(name="participants")'''

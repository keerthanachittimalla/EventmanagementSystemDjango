from django.apps import AppConfig
from django.dispatch import Signal

class AccountsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Accountsapp'
'''
# apps.py
#from django.apps import AppConfig
from django.contrib.auth.models import Group

#class YourAppConfig(AppConfig):
  #  name = 'your_app_name'

def ready(self):
        import Accountsapp.signals  # Import the signals module to connect signals
        # Ensure groups are created
        Group.objects.get_or_create(name='organizers')
        Group.objects.get_or_create(name='participants')
'''
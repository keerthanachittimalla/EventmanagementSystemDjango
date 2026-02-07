# signals.py
'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def assign_user_group(sender, instance, created, **kwargs):
    if created:
        #if instance.email.endswith('@studentdomain.com'):  # Example condition
        paticipants = Group.objects.get(name='participants')
        #else:
        organizers = Group.objects.get(name='organizers')
        instance.groups.add(paticipants)
        instance.groups.add(organizers)
'''
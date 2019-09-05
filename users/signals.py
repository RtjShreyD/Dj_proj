'''The purpose of this file is to help in auto create a user profile
when a new user is registered'''

from django.db.models.signals import post_save  
from django.contrib.auth.models import User   #User model here will be the sender of signal
from django.dispatch import receiver #this will be the reciever decorator to recv s/g and perform some task
from .models import Profile

@receiver(post_save, sender=User) #If a user is saved send the signl, which will be recvd by recievr  
def create_profile(sender, instance, created, **kwargs):  #this function is the receiver
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
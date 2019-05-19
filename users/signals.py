from django.db.models.signals import post_save # a signal is fired after an object is saved
from django.contrib.auth.models import User
# a receiver is a function that gets this signal and perform some task
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

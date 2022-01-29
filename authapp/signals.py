
from importlib import import_module
import profile
from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserRegistrationModel

class AuthappConfig(AppConfig):
    name = 'authapp'

    def ready(self):
        from . import signals

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile = UserRegistrationModel.objects.create(user=instance)
        profile.save()
        
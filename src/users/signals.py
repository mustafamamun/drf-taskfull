from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import uuid

from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(pre_save, sender=User)
def set_username(sender, instance, raw, **kwargs):
    if not instance.username:
        username = f'{instance.first_name}_{instance.last_name}_{uuid.uuid4()}'.lower()
        instance.username = username
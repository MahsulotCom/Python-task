from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.user.models import User
from apps.user.utils import add_permissions


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        add_permissions(instance)


@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    add_permissions(instance)

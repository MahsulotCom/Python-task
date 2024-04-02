from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.user.models import User
from apps.user.utils import add_permissions


@receiver(pre_save, sender=User)
def user_permissions(sender, instance, **kwargs):
    add_permissions(instance)


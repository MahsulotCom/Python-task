from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel
from apps.users.managers import UserManager


class User(AbstractUser, TimeStampedModel):
    shop = models.ForeignKey(
        "main.Shop",
        on_delete=models.SET_NULL,
        related_name="users",
        verbose_name=_("Shop"),
        null=True,
        blank=True,
    )
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

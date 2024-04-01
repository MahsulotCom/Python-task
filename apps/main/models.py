from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel, TreeManager

from apps.common.models import TimeStampedModel


class CustomTreeManager(TreeManager):
    def get_queryset(self):
        return super().get_queryset().order_by("order", "title")


class Category(MPTTModel, TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    order = models.IntegerField(_("Order"), default=0)  # For ordering categories
    icon = models.FileField(_("Icon"), upload_to="icons/", null=True, blank=True)  # For category icons
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    objects = CustomTreeManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

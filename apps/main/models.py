from django.core.exceptions import ValidationError
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


class Product(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    amount = models.PositiveIntegerField(_("Amount"))
    price = models.FloatField(_("Price"))
    categories = models.ManyToManyField(Category, related_name="products", verbose_name=_("Categories"))
    shop = models.ForeignKey(
        "main.shop", on_delete=models.SET_NULL, related_name="products", verbose_name=_("Shop"), null=True
    )
    active = models.BooleanField(_("Active"), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name=_("Product"))
    image = models.ImageField(_("Image"), upload_to="product_images/")
    order = models.IntegerField(_("Order"), default=0)
    is_main = models.BooleanField(_("Main Image"), default=False)

    def __str__(self):
        return f"{self.product.title} Image"

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        ordering = ("-is_main", "order")

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude)
        if self.is_main:
            # Check if there's already a main image for the product
            main_images_count = self.product.images.filter(is_main=True).exclude(pk=self.pk).count()
            if main_images_count > 0:
                raise ValidationError({"is_main": _("There can only be one main image for each product.")})


class Shop(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to="shop_images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")
        ordering = ("-created_at",)

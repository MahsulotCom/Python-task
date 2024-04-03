from datetime import datetime
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.utils.html import mark_safe
from apps.common.models import BaseModel
from apps.common.utils import compress_image, upload
from apps.shop.models import Shop
from apps.category.models import Category

class Attribute(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.attribute.title} - {self.value}'


class Product(BaseModel):
    title = models.CharField(max_length=256)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to=upload, null=True, blank=True)
    price = models.DecimalField(max_digits=21, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    is_new = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        image = self.image
        if image:
            if image.size > settings.IMAGE_SIZE_TO_COMPRESS:
                self.image = compress_image(image)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    attribute_value = models.ManyToManyField(AttributeValue)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'


class ProductVariantImage(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload)
    order = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        image = self.image
        if image:
            if image.size > settings.IMAGE_SIZE_TO_COMPRESS:
                self.image = compress_image(image)
        super(ProductVariantImage, self).save(*args, **kwargs)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""


class Discount(models.Model):
    product = models.ManyToManyField(Product, related_name='discounts')
    product_variant = models.ManyToManyField(ProductVariant, related_name='discounts')
    name = models.CharField(max_length=100)
    amount = models.PositiveSmallIntegerField(null=True, blank=True)
    percent = models.PositiveSmallIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


__all__ = ['Attribute', 'AttributeValue', 'Product', 'ProductVariant', 'ProductVariantImage', 'Discount']
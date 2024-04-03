from django.db import models

from common.models import TimeStampModel


class Category(models.Model):
    # relations
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    # fields
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Shop(TimeStampModel):
    # fields
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='shop_imgs/')

    def __str__(self):
        return f"{self.title}"


class Product(TimeStampModel):
    # relations
    category = models.ManyToManyField(Category)
    product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)

    # fields
    title = models.CharField(max_length=250)
    description = models.TextField()
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class Images(models.Model):
    # relations
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    # fields
    image = models.ImageField(upload_to='product_imgs/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.image.name}"

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

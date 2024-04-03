from django.db import models
from django.contrib.auth.models import User

from task.models import BaseModel


class Category(BaseModel):
    parent_category = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="child",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title


class Product(BaseModel):
    categories = models.ManyToManyField(
        Category,
        related_name="products",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    amount = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.title


class Shop(BaseModel):
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shops',
    )
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    image = models.ImageField(upload_to='shopimages/')

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'

    def __str__(self):
        return self.title


class Image(BaseModel):
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )
    url = models.CharField(max_length=4000)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Image'

    def __str__(self):
        return self.products.title


class Order(BaseModel):
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    customer =models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='users',
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.customer.username


from django.db import models

# Create your models here.

class Shop(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    image = models.ImageField(upload_to='shop/images')

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    amount = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product/images')
    # images
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)

    def __str__(self) -> str:
        return self.title


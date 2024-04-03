from django.db import models

from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, related_name='product_category')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product/images')

    def __str__(self):
        return str(self.product.title)

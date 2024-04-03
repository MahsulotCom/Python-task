from django.db import models

from product.models import Product


class Shop(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="shops")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='shop/images/')

    def __str__(self):
        return self.title

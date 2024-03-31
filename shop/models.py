from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='children')

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ManyToManyField('ProductImages')
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='product_images/')


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()

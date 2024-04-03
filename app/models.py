from django.db import models


# Shop model
class Shop(models.Model):
    title = models.CharField(max_length=255, verbose_name='Shop title')
    description = models.TextField(verbose_name='Shop description')
    image = models.ImageField(upload_to='shop_images/', verbose_name='Shop image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.title


# -----------------------------------------------------------


# Category model

class Category(models.Model):
    parent = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="children",
    )
    title = models.CharField(max_length=255, verbose_name='Category title')
    description = models.TextField(verbose_name='Category description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


# -------------------------------------------------------------

# Product model

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    category = models.ManyToManyField(Category, verbose_name='Category',
                                      related_name='products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Shop')
    amount = models.PositiveIntegerField(verbose_name='Amount')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    is_available = models.BooleanField(default=True, verbose_name='Availability')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


# -----------------------------------------------------------------------------------------------


# Product Image model

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product image',
                                related_name='product_images')
    image = models.ImageField(upload_to='product_images/', verbose_name='Product image')

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'

    def __str__(self):
        return self.image.url

# -----------------------------------------------------------------------------------------------

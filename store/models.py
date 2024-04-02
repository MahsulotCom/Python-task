from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    parent = models.ForeignKey(
        to='self', null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        app_label = 'store'
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products_category', on_delete=models.CASCADE)
    is_active = models.BooleanField(
        "Is Active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
                  "Unselect this instead of deleting accounts."
    )

    class Meta:
        app_label = 'store'
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.title}"


class Images(models.Model):
    image = models.ImageField(upload_to='images/product/%Y/%m/%d')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')

    class Meta:
        app_label = 'store'
        db_table = 'images'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f"{self.product.title}"


class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/shop/%Y/%m/%d')
    products = models.ManyToManyField(Product, related_name='shop_products')

    class Meta:
        app_label = 'store'
        db_table = 'shop'
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.title

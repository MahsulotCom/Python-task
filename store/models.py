from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shop_pics/')
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    parent_categories = models.ManyToManyField('self', symmetrical=False, related_name='child_categories', blank=True)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, null=True)
    active = models.BooleanField(default=True)
    orders = models.IntegerField(default=0)
    images = models.ManyToManyField('ProductImage', related_name='products', blank=True)  
    
    def __str__(self):
        return self.title
    

class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products_order")
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.product.amount >= self.quantity:
            if not self.pk:
                # Check if it's a new order
                super().save(*args, **kwargs)  # Call the parent save method to save the order
                self.product.orders += self.quantity
                self.product.amount -= self.quantity
                self.product.save()  
            else:
                # It's an existing order, so only update the quantity
                old_order = Orders.objects.get(pk=self.pk)
                old_quantity = old_order.quantity
                self.product.orders += (self.quantity - old_quantity)
                self.product.amount -= (self.quantity - old_quantity)
                self.product.save()  
                super().save(*args, **kwargs)  # Call the parent save method to save the order
        else:
            raise ValidationError("Not enough products.")
        
    def __str__(self):
        return f"{self.product.title} - Order #{self.pk}"
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.image.name
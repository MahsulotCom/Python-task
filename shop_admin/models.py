from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=220)
    description=models.TextField()
    parents=models.ManyToManyField('self', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} || {self.created_at}"
    
class Shop(models.Model):
    title=models.CharField(max_length=220)
    description=models.TextField()
    image_url=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} || {self.created_at}"


class Product(models.Model):
    category = models.ManyToManyField(Category)
    title=models.CharField(max_length=220)
    description=models.TextField()
    amount=models.IntegerField()
    price=models.FloatField()
    images=models.TextField()
    active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        category_titles = ', '.join(category.title for category in self.category.all())
        return f"{category_titles} || {self.title} || {self.active} || {self.created_at}"
    
   
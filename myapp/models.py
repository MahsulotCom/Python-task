from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=280)
    description = models.TextField()
    imageURL = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title



class Category(models.Model):
    title = models.CharField(max_length=280)
    description = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    title = models.CharField(max_length=280)
    amount = models.IntegerField()
    price = models.FloatField()
    images = models.TextField()
    active = models.BooleanField()

    def set_images(self, image_urls):
        self.images = ','.join(image_urls)

    def get_images(self):
        return self.images.split(',') if self.images else []

    def __str__(self):
        return self.title
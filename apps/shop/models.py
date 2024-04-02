from django.db import models
from apps.common.utils import compress_image, upload


# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to=upload)

    def save(self, *args, **kwargs):
        image = self.image
        if image:
            if image.size > settings.IMAGE_SIZE_TO_COMPRESS:
                self.image = compress_image(image)
        super(Shop, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
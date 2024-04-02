from django.db import models

from images.models import Image
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image_files(self, shop):
        """
        Retrieves all image files associated with a given shop.

        :param shop: The shop for which to retrieve image files.
        :type shop: Shop

        :return: A list of URLs pointing to the image files.
        :rtype: List[str]
        """
        shop_content_type = ContentType.objects.get_for_model(shop)
        image_files = Image.objects.filter(
            model_type=shop_content_type, model_id=shop.id
        )
        return [image_file.media_file.url for image_file in image_files]

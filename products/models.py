from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.models import ContentType
from images.models import Image


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField()
    number_of_orders = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    shop = models.ForeignKey(
        "shops.Shop",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image_files(self, product):
        """
        Retrieves all image files associated with a given product.

        :param product: The product for which to retrieve image files.
        :type product: Product

        :return: A list of URLs pointing to the image files.
        :rtype: List[str]
        """
        product_content_type = ContentType.objects.get_for_model(product)
        image_files = Image.objects.filter(
            model_type=product_content_type, model_id=product.id
        )
        return [image_file.media_file.url for image_file in image_files]

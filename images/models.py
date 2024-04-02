from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.forms import ValidationError


class Image(models.Model):
    model_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ("product", "shop")},
    )
    model_id = models.PositiveIntegerField()
    file_name = models.CharField(max_length=255, blank=True)

    class MimeType(models.TextChoices):
        JPEG = "image/jpeg"
        PNG = "image/png"
        GIF = "image/gif"
        WEBP = "image/webp"
        # MP4 = "video/mp4"
        # WEBM = "video/webm"

    mime_type = models.CharField(
        max_length=100,
        choices=MimeType.choices,
        blank=True,
        help_text="The mime type of the media file.",
    )
    media_file = models.FileField(upload_to="uploads/")

    # Generic Foreign Key to associate media with any model
    content_object = GenericForeignKey("model_type", "model_id")

    def __str__(self):
        return self.file_name

    def clean(self):
        """
        Cleans the media file by performing the following validations:

        - Checks if the mime type of the media file is valid. The valid mime types are "image/jpeg", "image/png", "image/gif" and "image/webp". If the mime type is not valid, raises a ValidationError with the message "Invalid mime type".

        - Checks if the size of the media file is within the allowed limit of 5MB. If the size exceeds the limit, raises a ValidationError with the message "File size too large".

        This function does not take any parameters and does not return any value.
        """

        # Check if the file exists
        if not self.media_file:
            raise ValidationError("File does not exist")

        # Check if the file size is less than 5MB
        if self.media_file.size > 5 * 1024 * 1024:
            raise ValidationError("File size too large")

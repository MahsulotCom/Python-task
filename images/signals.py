from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Image


def get_mime_type(file_name):
    import mimetypes

    return mimetypes.guess_type(file_name, strict=False)[0]


@receiver(pre_save, sender=Image)
def pre_save_media(sender, instance: Image, **kwargs):
    print("pre_save_media")
    if instance.media_file:
        instance.file_name = instance.media_file.name
        mime_type = get_mime_type(instance.media_file.path)
        # check if mime type is valid
        if mime_type not in ["image/jpeg", "image/png", "image/gif", "image/webp"]:
            raise ValueError("Invalid mime type")
        if mime_type:
            instance.mime_type = mime_type


# This connects the pre_save_media function to the pre_save signal of the Image model
pre_save.connect(pre_save_media, sender=Image)

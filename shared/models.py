from django.db import models


class BaseModel(models.Model):
    """
    A base model that provides common fields for other models.

    Attributes:
        created_at (DateTimeField): The date and time when the model instance was created.
        updated_at (DateTimeField): The date and time when the model instance was last updated.
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True

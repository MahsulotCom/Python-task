from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class Category(MPTTModel, models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parent_category')

    @classmethod
    def publish(cls):
        return cls.objects.all()

    def __str__(self):
        return self.title

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

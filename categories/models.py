from django.db import models
from django.db.utils import IntegrityError
from products.models import Product


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_categories",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_products(self):
        return Product.objects.filter(category=self)

    def get_all_paths(self):
        if self.parent_category:
            return self.parent_category.get_all_paths() + " -> " + self.title
        else:
            return self.title

    def get_ancestors(self):
        if self.parent_category:
            return self.parent_category.get_ancestors() + [self]
        else:
            return [self]

    def save(self, *args, **kwargs):
        # Check for circular references
        if self.parent_category and self in self.parent_category.get_ancestors():
            raise IntegrityError(
                "A category cannot be a parent of itself or any of its ancestors."
            )

        super().save(*args, **kwargs)

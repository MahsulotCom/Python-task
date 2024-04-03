from django.db import models
from shared.models import BaseModel
from store.managers import BaseManager


class Shop(BaseModel):
    """
    Represents a shop in the store.
    """

    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to="shop_images/", verbose_name="Image")

    objects = BaseManager()

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.title


class Category(BaseModel):
    """
    Represents a category in the store.
    """

    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    parent_categories = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="subcategories",
        verbose_name="Parent Categories",
    )

    objects = BaseManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_possible_paths(self):
        """
        Returns a list of possible paths to reach this category.
        """
        paths = []
        for path in self._recurse_parents():
            paths.append(" -> ".join([category.title for category in path]))

        return paths

    def _recurse_parents(self, path=None):
        """
        Recursively finds all parent categories of this category.
        """
        if path is None:
            path = []
        if self in path:
            return [path]
        path.append(self)
        if self.parent_categories.exists():
            for parent in self.parent_categories.all():
                parent._recurse_parents(path)
        return [path]


class Product(BaseModel):
    """
    Represents a product in the store.
    """

    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    amount = models.PositiveIntegerField(verbose_name="Amount")
    is_active = models.BooleanField(verbose_name="Active")

    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="products", verbose_name="Shop"
    )
    categories = models.ManyToManyField(
        "Category", related_name="products", verbose_name="Categories"
    )

    objects = BaseManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def get_main_image(self):
        """
        Returns the URL of the main image for this product.
        """
        return self.images.first().image.url


class ProductImage(BaseModel):
    """
    Represents an image associated with a product.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="Product"
    )
    image = models.ImageField(upload_to="product_images/", verbose_name="Image")

    objects = BaseManager()

    def __str__(self):
        return self.product.title

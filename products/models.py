from django.db import models


class Category(models.Model):
    parent = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="children",
    )
    title = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    amount = models.PositiveIntegerField(default=0, verbose_name="Количество")
    price = models.FloatField(default=0, verbose_name="Цена")
    active = models.BooleanField(default=True, verbose_name="Активность")
    category = models.ManyToManyField(
        Category,
        related_name="products",
        verbose_name="Категории",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Продукт",
    )
    url = models.CharField(
        max_length=2048,
        verbose_name="Ссылка на изоброжение",
    )

    class Meta:
        verbose_name = "Изоброжение"
        verbose_name_plural = "Изоброжения"

    def __str__(self) -> str:
        return self.product.title


class Shop(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="shops",
        verbose_name="Продукт",
    )
    title = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="shop_images/",
        verbose_name="Изоброжение",
    )

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self) -> str:
        return self.title

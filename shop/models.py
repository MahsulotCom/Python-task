from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Называние")
    description = models.TextField(verbose_name="Описание")
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='children')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Product(models.Model):
    description = models.TextField(verbose_name="Описание")
    title = models.CharField(max_length=100, verbose_name="Называние")
    amount = models.IntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    active = models.BooleanField(default=True, verbose_name="Активность")
    category = models.ManyToManyField(Category, related_name='products',
                                      verbose_name="Продукты")

    class Meta:
        verbose_name_plural = "Продукты"
        verbose_name = "Продукт"

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    url = models.CharField(max_length=1024, verbose_name="Ссылка")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name="Продукт", related_name="images")

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображение"

    def __str__(self):
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
    image = models.ImageField(upload_to="shop_images/",
                              verbose_name="Изоброжение")

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.title

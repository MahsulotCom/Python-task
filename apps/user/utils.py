from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from apps.user.models import User
from apps.shop.models import Shop
from apps.category.models import Category
from apps.product.models import *


def add_permissions(instance):
    if instance.role == User.Customer:
        return
    elif instance.is_superuser is True:
        instance.role = User.SUPER_ADMIN
    elif instance.role == User.SUPER_ADMIN:
        instance.is_superuser = True
    elif instance.role == User.SHOP_ADMIN:
        shop_content_type = ContentType.objects.get_for_model(Shop)
        for permission in Permission.objects.filter(content_type=shop_content_type):
            instance.user_permissions.add(permission)
    elif instance.role == user.PRODUCT_ADMIN:
        product_content_types = [ContentType.objects.get_for_model(ex_model) for ex_model in
                                 [Attribute, AttributeValue, Product, ProductVariant,
                                  ProductVariantImage, Discount]]
        for content_type in product_content_types:
            for permission in Permission.objects.filter(content_type=content_type):
                instance.user_permissions.add(permission)
    elif instance.role == user.CATEGORY_ADMIN:
        category_content_type = ContentType.objects.get_for_models(Category)
        for permission in Permission.objects.filter(content_type=category_content_type):
            instance.user_permissions.add(permission)
    instance.save()
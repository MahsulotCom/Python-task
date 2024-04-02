from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from apps.user.models import User
from apps.shop.models import Shop
from apps.category.models import Category
from apps.product.models import *
from apps.order.models import Order, OrderProduct


def add_permissions(instance):
    if instance.role == User.Customer:
        return
    elif instance.is_superuser is True:
        instance.role = User.SUPER_ADMIN
    elif instance.role == User.SUPER_ADMIN:
        instance.is_superuser = True
    elif instance.role == User.SHOP_ADMIN:
        shop_content_type = ContentType.objects.get_for_model(Shop)
        permissions = [permission for permission in Permission.objects.filter(content_type=shop_content_type)]
        instance.user_permissions.set(permissions)
    elif instance.role == User.PRODUCT_ADMIN:
        permissions = []
        product_content_types = [ContentType.objects.get_for_model(ex_model) for ex_model in
                                 [Attribute, AttributeValue, Product, ProductVariant,
                                  ProductVariantImage, Discount]]
        for content_type in product_content_types:
            permissions += [permission for permission in Permission.objects.filter(content_type=content_type)]
        instance.user_permissions.set(permissions)
    elif instance.role == User.CATEGORY_ADMIN:
        category_content_type = ContentType.objects.get_for_models(Category)
        permissions = [permission for permission in Permission.objects.filter(content_type=category_content_type)]
        instance.user_permissions.set(permissions)
    elif instance.role == User.ORDER_ADMIN:
        permissions = []
        order_content_types = [ContentType.objects.get_for_model(ex_model) for ex_model in [Order, OrderProduct]]
        for content_type in order_content_types:
            permissions += [permission for permission in Permission.objects.filter(content_type=content_type)]
        instance.user_permissions.set(permissions)
    instance.save()
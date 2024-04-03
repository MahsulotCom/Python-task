from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from shop.permissions import productadmin_permissions

PRODUCT_ADMIN, SUPER_USER = (
    "product_admin",
    "super_user"
)


MEASURE_CHOICES = (
    ('kg', 'Kilogram'),
    ('ton', 'Ton'),
    ('liter', 'Liter'),
    ('meter', 'Meter'),
    ('piece', 'Piece'),
)


class User(AbstractUser):
    USER_ROLES = (
        ("product_admin", "Product Admin"),
        ("super_user", "Super User")
    )

    user_roles = models.CharField(max_length=31, choices=USER_ROLES, default="product_admin")
    staff_active = models.BooleanField(default=False)  # Define the staff_active field

    def __str__(self):
        return self.username

    @classmethod
    def create(cls, username, email, password, user_roles="product_admin", staff_active=False):
        user = cls(username=username, email=email, user_roles=user_roles, staff_active=staff_active)
        user.set_password(password)
        user.save()
        return user

    def save(self, *args, **kwargs):
        if self.staff_active:
            self.is_staff = True

        return super().save()


class Shop(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    image_url = models.ImageField()

    def __str__(self):
        return self.title


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    measure = models.CharField(max_length=13, choices=MEASURE_CHOICES)
    price = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.ImageField()

    def __str__(self):
        return f"Image for {self.product.title}"


class Order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    sell_price = models.FloatField()

    def __str__(self):
        return f"Order for {self.product.title}"

    def update_product_amount(self):
        self.product.amount -= self.amount
        self.product.save()



from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission

"""
It is a signal handler in Django. 
Specifically, it is using the post_save signal,
 which is sent by the Django framework after a 
 model instance is saved. In this case, 
 the signal is triggered when a User model instance is saved. 
"""
@receiver(post_save, sender=User)
def add_reviewer_to_group(sender, instance, **kwargs):
    if instance.user_roles == PRODUCT_ADMIN:

        group = Group.objects.get(name="productadmin")

        if not group:
            Group.objects.create(name="productadmin")
            permissions = Permission.objects.filter(codename__in=productadmin_permissions)
            group.permissons.add(*permissions)
            group.save()

        instance.groups.add(group)



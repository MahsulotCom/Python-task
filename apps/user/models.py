from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.user.managers import CustomUserManager


phone_regex_validator = RegexValidator(
    regex=r"^\+?1?\d{9,12}$",
    message=_(
        "The phone number must be entered in the format: “+99891234567”. Up to 13 digits allowed."
    ),
)


class AddressModel(models.Model):
    city = models.CharField(max_length=256, blank=True)
    district = models.CharField(max_length=256, blank=True)
    street = models.CharField(max_length=256, blank=True)
    building_number = models.IntegerField(null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    house_number = models.IntegerField(null=True, blank=True)
    is_main = models.BooleanField(default=False)
    comment_for_courier = models.TextField(blank=True)

    def __str__(self):
        return f"{self.city} {self.district}, {self.street}"


class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER = 'Customer'
    SUPER_ADMIN = 'Super Admin'
    SHOP_ADMIN = 'Shop Admin'
    PRODUCT_ADMIN = 'Product Admin'
    CATEGORY_ADMIN = 'Category Admin'
    user_role = (
        (CUSTOMER, CUSTOMER),
        (SUPER_ADMIN, SUPER_ADMIN),
        (SHOP_ADMIN, SHOP_ADMIN),
        (PRODUCT_ADMIN, PRODUCT_ADMIN),
        (CATEGORY_ADMIN, CATEGORY_ADMIN)
    )
    MALE = 'male'
    FEMALE = 'female'
    gender_choices = (
        (MALE, MALE),
        (FEMALE, FEMALE)
    )
    role = models.CharField(max_length=32, choices=user_role, default=CUSTOMER)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=12, validators=(phone_regex_validator,),unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=16, choices=gender_choices)
    email = models.EmailField(blank=True)
    address = models.ManyToManyField(AddressModel)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"







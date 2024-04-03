from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    course = models.ForeignKey(to=Course,
                               on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=155)
    study = models.CharField(max_length=200, null=True, blank=True)
    level = models.CharField(max_length=155, null=True, blank=True)
    phone_number = models.CharField(max_length=9)
    region = models.ForeignKey(to=Region,
                               on_delete=models.CASCADE)
    address_line = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=100, null=True, blank=True)
    fathers_age = models.CharField(max_length=155, null=True, blank=True)
    fathers_job = models.CharField(max_length=100, null=True, blank=True)
    fathers_phone = models.CharField(max_length=100, null=True, blank=True)
    mothers_name = models.CharField(max_length=100, null=True, blank=True)
    mothers_age = models.CharField(max_length=155, null=True, blank=True)
    mothers_job = models.CharField(max_length=100, null=True, blank=True)
    mothers_phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a phone number!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, validators=[integer_validator], null=True, blank=True, unique=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

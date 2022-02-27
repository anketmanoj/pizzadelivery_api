from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

"""Create a custom user model using BaseUserManager """


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    # create a superuser using methods that takes the arguments of self, email, password and any extra fields
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user should have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user should have is_superuser=True')

        if extra_fields.get('is_active') is not True:
            raise ValueError('Super user should have is_active=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=255, unique=True)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return f"User == {self.email}"

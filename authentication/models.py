from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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

    def create_superuser(self, email, password, **extra_fields):
        pass

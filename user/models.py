from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, is_staff=False, is_superuser=False):
        if not email:
            raise ('User must have a email')
        if not password:
            raise('User must have a password')
        if not name:
            raise ('User must have a name')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.name = name
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, email, password, name):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user


class Profile(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.TextField(max_length=50)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
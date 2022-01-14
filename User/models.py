from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    objects = UserManager()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

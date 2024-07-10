from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import uuid
from .managers import CustomUserManager

class User(AbstractBaseUser,PermissionsMixin):
    public_id = models.UUIDField(db_index=True,unique=True,editable=False,default=uuid.uuid4)

    firts_name = models.CharField(max_length=20,unique=True,blank=False)

    last_name = models.CharField(max_length=25,blank=True)

    email = models.EmailField(db_index=True,unique=True,blank=True)

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now=True)

    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['firts_name','last_name']

    objects = CustomUserManager()



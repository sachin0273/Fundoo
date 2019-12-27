from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(null=True, blank=True)

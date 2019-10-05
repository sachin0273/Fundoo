from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Password(models.Model):
    confirm_password = models.CharField(max_length=12)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField()
    time_stamp = models.DateTimeField(auto_now_add=True)

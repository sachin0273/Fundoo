from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField()
    time_stamp = models.DateTimeField(auto_now_add=True)
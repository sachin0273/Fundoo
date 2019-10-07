from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    file = models.URLField(blank=True,null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

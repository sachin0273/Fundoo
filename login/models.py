from django.db import models


# Create your models here.

class Password(models.Model):
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

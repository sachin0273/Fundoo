from django.db import models


# Create your models here.

class Password(models.Model):
    confirm_password = models.CharField(max_length=12)

# import self as self
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Label(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=250)
    note = models.CharField(max_length=250, blank=True)
    image = models.FileField(blank=True)
    collaborator = models.ManyToManyField(User, related_name='collaborator', blank=True)
    label = models.ManyToManyField(Label, related_name='label', blank=True)
    is_archive = models.BooleanField('is_archive', default=False)
    is_trash = models.BooleanField('is_trash', default=False)
    is_pin = models.BooleanField('is_pin', default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField(null=True, blank=True)



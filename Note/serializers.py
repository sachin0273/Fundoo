from .models import Note, Label

from rest_framework import serializers


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "note", "image", "is_archive", "is_pin", "user", "collaborator", "label"]


class LabelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

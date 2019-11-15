from .models import Note, Label

from rest_framework import serializers


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "note", "image", "is_archive", "is_pin", "collaborator", "label"]


class LabelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

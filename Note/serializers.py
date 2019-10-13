from .models import Note

from rest_framework import serializers


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'note', 'is_archive', 'is_pin', 'is_trash']

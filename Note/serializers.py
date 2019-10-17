
from .models import Note, Label

from rest_framework import serializers


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class LabelSerializers(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'

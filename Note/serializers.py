from Note.documents import NoteDocument
from .models import Note, Label
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

User = get_user_model()


class NoteSerializers(serializers.ModelSerializer):
    """
    here we creating serializer for posting a note
    """

    class Meta:
        model = Note
        fields = ["id", "title", "note", "image", "is_archive", "is_pin", "collaborator", "label", "reminder", "color"]


class LabelSerializers(serializers.ModelSerializer):
    """

    here we creating serializer for posting a label

    """

    class Meta:
        model = Label
        fields = ['id', 'name']


class CollaboratorSerializer(serializers.ModelSerializer):
    """

    here we creating serializer for serialize email of user for collaborator field

    """

    class Meta:
        model = User
        fields = ['id', 'email']


class NotesSerializer(serializers.ModelSerializer):
    """

    here we creating serializer for getting a serialized data

    """
    label = LabelSerializers(many=True, read_only=True)
    collaborator = CollaboratorSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = '__all__'


class NoteSerializerPut(serializers.ModelSerializer):
    """

    here we creating serializer for updating data into Note model

    """
    class Meta:
        model = Note
        fields = '__all__'

from Note.documents import NoteDocument
from .models import Note, Label

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "note", "image", "is_archive", "is_pin", "collaborator", "label", "reminder", "color"]


class LabelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


# class PublisherDocumentSerializer(DocumentSerializer):
#     """Serializer for Publisher document."""
#
#     class Meta(NoteDocument):
#         """Meta options."""
#         # index_classes = (NoteDocument,)
#         # Note, that since we're using a dynamic serializer,
#         # we only have to declare fields that we want to be shown. If
#         # somehow, dynamic serializer doesn't work for you, either extend
#         # or declare your serializer explicitly.
#         fields = '__all__'

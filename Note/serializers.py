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

# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
#
# from . import documents as articles_documents


# class ArticleDocumentSerializer(DocumentSerializer):
#     class Meta:
#         document = articles_documents.ArticleDocument
#         fields = (
#             'id',
#             'title',
#             'body',
#             'author',
#             'created',
#             'modified',
#             'pub_date',
#         )

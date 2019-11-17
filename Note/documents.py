from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer, tokenizer

from .models import Note, Label

html_strip = analyzer(
    'html_strip',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=3),
    filter=["lowercase", "stop", "snowball"]
)


@registry.register_document
class NoteDocument(Document):
    label = fields.ObjectField(properties={
        'name': fields.TextField()
    })

    title = fields.TextField(
        analyzer=html_strip
    )
    reminder = fields.StringField(
    )
    note = fields.TextField(
        analyzer=html_strip
    )
    user_id = fields.IntegerField()

    color = fields.StringField()

    class Index:
        # Name of the Elasticsearch index
        name = 'search_note'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Note

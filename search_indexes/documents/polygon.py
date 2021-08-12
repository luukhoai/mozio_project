from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from polygons.models import Polygon


# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class PolygonDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )

    price = fields.FloatField()
    provider_name = fields.TextField()
    geo = fields.GeoPointField(attr='geo_field_indexing')

    def prepare_provider_name(self, instance):
        return instance.provider.name

    class Django(object):
        model = Polygon

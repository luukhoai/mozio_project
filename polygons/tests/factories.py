import factory
from polygons.models import Polygon
from factory.fuzzy import FuzzyFloat


class PolygonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Polygon

    name = factory.Faker('name')
    price = FuzzyFloat(0.0, 55.32)
    geo = {'type': 'Point', 'coordinates': [0, 0]}
    slug = factory.Faker('slug')

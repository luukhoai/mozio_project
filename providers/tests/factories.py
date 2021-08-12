import factory

from providers.models import Provider


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    name = factory.Faker('name')
    email = factory.Faker('email')
    phone_number = '+12345678'
    language = 'VN'
    currency = 'USD'
    slug = factory.Faker('slug')

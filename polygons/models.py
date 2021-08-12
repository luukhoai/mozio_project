from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from providers.models import Provider


# Create your models here.
class Polygon(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(MinValueValidator(0))
    provider = models.ForeignKey(
        Provider, related_name='polygons', on_delete=models.CASCADE)
    geo = models.JSONField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        unique_together = ['name', 'provider_id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify('{} {}'.format(self.name, self.provider.name))
        super(Polygon, self).save(*args, **kwargs)

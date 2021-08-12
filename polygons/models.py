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
        unique_together = ['name', 'provider']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify('{} {}'.format(self.name, self.provider.name))
        super(Polygon, self).save(*args, **kwargs)

    @property
    def geo_field_indexing(self):
        """return a dictionary of geo contains lat, lon"""
        return {
            'lat': self.geo['coordinates'][0],
            'lon': self.geo['coordinates'][1],
        }

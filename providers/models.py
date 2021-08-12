from django.db import models
from .validators import phone_regex
from django.utils.text import slugify
# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=17, validators=[phone_regex()])
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=5)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Provider, self).save(*args, **kwargs)

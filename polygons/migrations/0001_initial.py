# Generated by Django 3.2.6 on 2021-08-12 08:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0003_alter_provider_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(verbose_name=django.core.validators.MinValueValidator(0))),
                ('geo', models.JSONField()),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polygons', to='providers.provider')),
            ],
            options={
                'unique_together': {('name', 'provider_id')},
            },
        ),
    ]

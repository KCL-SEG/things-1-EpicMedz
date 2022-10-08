# Generated by Django 4.1.2 on 2022-10-08 23:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_thing_description_thing_name_thing_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0, 'Value cannot be less than 0'), django.core.validators.MaxValueValidator(100, 'Value cannot be greater than 100')]),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-08 23:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='description',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0, 'Value cannot be less than 0'), django.core.validators.MaxValueValidator(101, 'Value cannot be greater than 100')]),
        ),
    ]
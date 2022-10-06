from django.db import models
from django.db.models import Model

# Create your models here.

class Thing(Model):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()

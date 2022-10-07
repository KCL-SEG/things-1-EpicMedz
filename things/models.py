from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Thing(Model):
    name = models.CharField(unique = True, max_length = 30, blank = False)
    description = models.CharField(unique = False, max_length = 120, blank = True )
    quantity = models.IntegerField(unique = False, validators = [
        MinValueValidator(0, "Value cannot be less than 0"),
        MaxValueValidator(101, "Value cannot be greater than 100"
        )])

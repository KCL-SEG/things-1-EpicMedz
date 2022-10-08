from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.

class Thing(Model):
    name = models.CharField(max_length = 30, unique = True, blank = False)
    description = models.CharField(max_length = 120, blank = True)
    quantity = models.IntegerField(unique = False, default = 1, validators = [
        MinValueValidator(0, "Value cannot be less than 0"),
        MaxValueValidator(100, "Value cannot be greater than 100"
        )])

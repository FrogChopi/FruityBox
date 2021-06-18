from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0, validators=[ MinValueValidator(0) ])
    price = models.IntegerField(default=1, validators=[ MinValueValidator(1) ])

    def __str__(self) :
        return self.name


class Bundle(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1, validators=[ MinValueValidator(1) ])
    content = models.ManyToManyField(Fruit)

    def __str__(self) :
        return self.name



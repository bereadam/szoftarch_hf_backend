from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    subcategories = models.ManyToManyField('Category', blank=True)
    # pois = models.ManyToManyField(Poi)

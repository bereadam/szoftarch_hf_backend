from django.db import models
from model.models.poi import Poi


class Category(models.Model):
    name = models.CharField(max_length=200)
    subcategories = models.ManyToManyField('Category', blank=True)
    pois = models.ManyToManyField(Poi)

    def add_subcategory(self, subcategory):
        self.subcategories.add(subcategory)
        self.save()

    def add_poi(self, poi):
        self.pois.add(poi)
        self.save()

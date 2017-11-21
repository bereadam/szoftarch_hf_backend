from django.db import models
from model.models.poi import Poi


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('Category', default=None, blank=True, null=True)
    subcategories = models.ManyToManyField('Category', blank=True)
    pois = models.ManyToManyField(Poi, blank=True)

    def add_subcategory(self, subcategory):
        self.subcategories.add(subcategory)
        subcategory.parent = self
        subcategory.save()
        self.save()

    def add_poi(self, poi):
        self.pois.add(poi)
        self.save()

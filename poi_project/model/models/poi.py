from django.db import models


class Poi(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    desc = models.TextField()

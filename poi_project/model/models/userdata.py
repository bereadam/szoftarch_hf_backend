from django.db import models
from model.models.poi import Poi
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_pois = models.ManyToManyField(Poi)

    def get(user):
        return UserData.objects.get(user=user)
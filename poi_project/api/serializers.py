from rest_framework import serializers
from model.models.category import Category
from model.models.poi import Poi


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = '__all__'

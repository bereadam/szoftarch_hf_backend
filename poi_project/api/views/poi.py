from rest_framework import viewsets
from model.models.poi import Poi
from api.serializers import PoiSerializer


class PoiViewSet(viewsets.ModelViewSet):

    queryset = Poi.objects.all()
    serializer_class = PoiSerializer
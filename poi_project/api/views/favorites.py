from rest_framework.views import APIView
from model.models.userdata import UserData
from django.http.response import HttpResponse, JsonResponse
from model.models.poi import Poi


class FavoritePoisView(APIView):
    def get(self, request):
        udata = UserData.get(request.user)
        pois = udata.fav_pois.all()

        return JsonResponse({"Text": [x.id for x in pois]})


class AddFavoritePoiView(APIView):
    def get(self, request, poiID):

        if poiID is None:
            return HttpResponse("poiID is missing!", status=400)

        try:
            poi = Poi.objects.get(pk=poiID)
        except Poi.DoesNotExist:
            return HttpResponse("Poi does not exist!", status=404)

        udata = UserData.get(request.user)

        udata.fav_pois.add(poi)

        return HttpResponse()


class RemoveFavoritePoiView(APIView):
    def get(self, request, poiID):

        if poiID is None:
            return HttpResponse("poiID is missing!", status=400)

        try:
            poi = Poi.objects.get(pk=poiID)
        except Poi.DoesNotExist:
            return HttpResponse("Poi does not exist!", status=404)

        udata = UserData.get(request.user)

        udata.fav_pois.remove(poi)

        return HttpResponse()

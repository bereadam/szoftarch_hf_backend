from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from model.models.poi import Poi
from api.serializers import PoiSerializer
import json


class PoiSearchView(APIView):
    def post(self, request):
        json_data = json.loads(request.body)

        try:
            search_text = json_data["Text"]
        except KeyError as e:
            return HttpResponse(str(e.args[0]) + 'is missing!', status=400)

        results = Poi.objects.filter(name__contains=search_text)

        return JsonResponse([PoiSerializer(x).data for x in results], safe=False)

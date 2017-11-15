from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from model.models.category import Category
from model.models.poi import Poi
from api.serializers import CategorySerializer
from django.http import HttpResponse
import json


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryView(APIView):
    def post(self, request):

        json_data = json.loads(request.body)

        try:
            parent_category = Category.objects.get(pk=json_data['parentID'])
            subcategory = Category.objects.get(pk=json_data['subcategoryId'])
        except Category.DoesNotExist:
            return HttpResponse('Category does not exist!', status=404)
        except KeyError as e:
            return HttpResponse(str(e.args[0]) + 'is missing!', status=400)

        parent_category.add_subcategory(subcategory)

        return Response(CategorySerializer(parent_category).data)

class AddPoiView(APIView):
    def post(self, request):

        json_data = json.loads(request.body)

        try:
            parent_category = Category.objects.get(pk=json_data['parentCategoryID'])
            poi = Poi.objects.get(pk=json_data['poiId'])
        except Category.DoesNotExist:
            return HttpResponse('Category does not exist!', status=404)
        except Poi.DoesNotExist:
            return HttpResponse('Poi does not exist!', status=404)
        except KeyError as e:
            return HttpResponse(str(e.args[0]) + 'is missing!', status=400)

        parent_category.add_poi(poi)

        return Response(CategorySerializer(parent_category).data)

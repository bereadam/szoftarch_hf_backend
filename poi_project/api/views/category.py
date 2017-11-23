from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from model.models.category import Category
from model.models.poi import Poi
from api.serializers import CategorySerializer, PoiSerializer
from django.http import HttpResponse
import json
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.permissions import EditCategory
from django.http.response import JsonResponse


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (EditCategory,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = Category.objects.filter(parent=None)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class SubcategoryView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)

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
    permission_classes = (IsAuthenticated, IsAdminUser,)

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


class CategoryWithSubcategoriesAndPois(APIView):
    def get(self, request, id):

        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return HttpResponse("Category does not exist", status=404)

        result = {}
        result['name'] = category.name
        result['parent'] = CategorySerializer(category.parent).data
        result['subcategories'] = [CategorySerializer(x).data for x in category.subcategories.all()]
        result['pois'] = [PoiSerializer(x).data for x in category.pois.all()]

        return JsonResponse(result)
from django.conf.urls import url, include
from rest_framework import routers
from api.views.category import CategoryViewSet, SubcategoryView
from api.views.poi import PoiViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'poi', PoiViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'addSubcategory$', SubcategoryView.as_view()),
]

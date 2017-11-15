from django.conf.urls import url, include
from rest_framework import routers
from api.views.category import CategoryViewSet, SubcategoryView

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'addSubcategory$', SubcategoryView.as_view())
]

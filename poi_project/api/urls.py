from django.conf.urls import url, include
from rest_framework import routers
from api.views.category import CategoryViewSet, SubcategoryView, AddPoiView
from api.views.poi import PoiViewSet
from api.views.auth import LoginView, LogoutView, RegisterView

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'poi', PoiViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'addSubcategory$', SubcategoryView.as_view()),
    url(r'addPoi', AddPoiView.as_view()),
    url(r'register', RegisterView.as_view()),
    url(r'logout', LogoutView.as_view()),
    url(r'login', LoginView.as_view()),
]

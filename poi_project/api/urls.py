from django.conf.urls import url, include
from rest_framework import routers
from api.views.category import CategoryViewSet, SubcategoryView, AddPoiView
from api.views.poi import PoiViewSet
from api.views.auth import LoginView, LogoutView, RegisterView
from api.views.favorites import FavoritePoisView, AddFavoritePoiView, RemoveFavoritePoiView

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'poi', PoiViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'addSubcategory$', SubcategoryView.as_view()),
    url(r'addPoi$', AddPoiView.as_view()),
    url(r'register$', RegisterView.as_view()),
    url(r'logout$', LogoutView.as_view()),
    url(r'login$', LoginView.as_view()),
    url(r'favorites$', FavoritePoisView.as_view()),
    url(r'favorite/add/(?P<poiID>[0-9]+)$', AddFavoritePoiView.as_view()),
    url(r'favorite/remove/(?P<poiID>[0-9]+)$', RemoveFavoritePoiView.as_view())
]

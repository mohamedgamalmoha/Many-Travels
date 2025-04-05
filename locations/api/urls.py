from django.urls import path, include

from rest_framework import routers

from locations.api.views import CountryViewSet, CityViewSet, StateViewSet


app_name = 'locations'

router = routers.DefaultRouter()
router.register('countries', CountryViewSet, basename='country')
router.register('cities', CityViewSet, basename='city')
router.register('states', StateViewSet, basename='state')


urlpatterns = [
    path('', include(router.urls), name='locations_routes'),
]

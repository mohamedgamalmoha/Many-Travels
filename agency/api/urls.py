from django.urls import path, include

from rest_framework import routers

from agency.api.views import AgencyViewSet, TravelViewSet


app_name = 'agency'

router = routers.DefaultRouter()
router.register('agencies', AgencyViewSet, basename='agency')
router.register('travels', TravelViewSet, basename='travel')

urlpatterns= [
    path('', include(router.urls), name='agency_routes')
]

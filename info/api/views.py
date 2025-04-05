from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView

from info.models import MainInfo, Service, AboutUs, Theme
from info.api.serializer import (MainInfoSerializer, ServiceSerializer, AboutUsSerializer, ThemeSerializer,
                                 ContactUsSerializer)


class MainInfoAPIView(RetrieveAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.get_queryset().first()


class ServiceAPIView(ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]


class AboutUsAPIView(ListAPIView):
    queryset = AboutUs.objects.filter(is_active=True)
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny]


class ThemeAPIView(ListAPIView):
    queryset = Theme.objects.filter(is_active=True)
    serializer_class = ThemeSerializer
    permission_classes = [AllowAny]


class ContactUsAPIView(CreateAPIView):
    serializer_class = ContactUsSerializer
    permission_classes = [AllowAny]

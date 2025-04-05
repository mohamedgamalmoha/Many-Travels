from django.urls import path

from info.api.views import MainInfoAPIView, ServiceAPIView, AboutUsAPIView, ThemeAPIView, ContactUsAPIView


app_name = 'info'

urlpatterns = [
    path('main-info/', MainInfoAPIView.as_view(), name='main-info'),
    path('services/', ServiceAPIView.as_view(), name='services'),
    path('about-us/', AboutUsAPIView.as_view(), name='about-us'),
    path('themes/', ThemeAPIView.as_view(), name='themes'),
    path('contact-us/', ContactUsAPIView.as_view(), name='contact-us')
]

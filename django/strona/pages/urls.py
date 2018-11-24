from django.urls import path

from .views import AboutPageView, HomePageView, autorPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('autor/', autorPageView.as_view(), name='autor'),
]

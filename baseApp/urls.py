from django.urls import path

from .views import HomePage

app_name = 'base'

urlpatterns = [
    path('',HomePage.as_view(),name='homePage'),
]
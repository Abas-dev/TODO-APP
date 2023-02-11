from django.urls import path

from .views import HomePage,LoginPage,RegisterPage,UpdatePage

app_name = 'base'

urlpatterns = [
    path('',HomePage.as_view(),name='homePage'),
    path('login/',LoginPage.as_view(),name='login'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('update/',UpdatePage.as_view(),name='update'),
]
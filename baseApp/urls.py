from django.urls import path

from .views import HomePageView,LoginPageView,RegisterPageView,CreatePageView,DeleteDataView,DisplayPageView,LogOutView

app_name = 'base'

urlpatterns = [
    path('',HomePageView.as_view(),name='homePage'),

    path('login/',LoginPageView.as_view(),name='login'),
    path('logout/',LogOutView.as_view(), name = 'logout'),
    path('register/',RegisterPageView.as_view(),name='register'),

    path('add/', CreatePageView.as_view(),name='add'),
    path('detail/<int:pk>',DisplayPageView.as_view(), name='detail'),
    path('delete/<int:pk>',DeleteDataView.as_view(),name='delete'),

]
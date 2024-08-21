from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('welcome', views.welcome),
    path('authorized', views.authorized),
]

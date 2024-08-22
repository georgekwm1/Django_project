from django.urls import path
from . import views

# app_name = 'notes'

urlpatterns = [
    path('notes/', views.lists),
    path('notes/<int:pk>/', views.detail)
]

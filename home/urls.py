from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    # path('welcome/', views.HomeView.as_view(), name='welcome'),
    path('authorized/', views.AuthorizedView.as_view()),
]

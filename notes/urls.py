from django.urls import path
from . import views

# app_name = 'notes'

urlpatterns = [
    path('notes/', views.NoteListView.as_view(), name='all.notes'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note.detail'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note.delete'),
    path('notes/new/', views.NoteCreateView.as_view(), name='notes.new'),
]

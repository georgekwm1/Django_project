from django.shortcuts import render
from .models import Note
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

# Create your views here.


# def lists(request):
#     all_notes = Note.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


# def detail(request, pk):
#     try:
#         note = Note.objects.get(pk=pk)
#         return render(request, 'notes/notes_detail.html', {'note': note})
#     except Note.DoesNotExist:
#         raise Http404('Note does not exist')

# views.py
class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'notes/notes_form.html'
    success_url = '/smart/notes'


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

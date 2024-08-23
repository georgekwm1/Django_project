from django.shortcuts import render
from .models import Note
from django.http import Http404

# Create your views here.


def lists(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
        return render(request, 'notes/notes_detail.html', {'note': note})
    except Note.DoesNotExist:
        raise Http404('Note does not exist')

# views.py

from django.shortcuts import render
from .models import Note
from django.http import Http404
import os
from django.conf import settings
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


def get_css_files():
    css_folder = os.path.join(settings.STATICFILES_DIRS[0], '5.3')
    css_files = []

    for root, dirs, files in os.walk(css_folder):
        for file in files:
            if file.endswith('.scss'):
                # Construct the relative path to the static folder
                relative_path = os.path.relpath(os.path.join(
                    root, file), settings.STATICFILES_DIRS[0])
                css_files.append(relative_path)
    return css_files


def get_scss_files():
    scss_folder = os.path.join(settings.STATICFILES_DIRS[0], 'scss')
    scss_files = []

    for root, dirs, files in os.walk(scss_folder):
        for file in files:
            if file.endswith('.css'):
                # Construct the relative path to the static folder
                relative_path = os.path.relpath(os.path.join(
                    root, file), settings.STATICFILES_DIRS[0])
                scss_files.append(relative_path)
    return scss_files


def your_view(request):
    css_files = get_css_files()
    return render(request, 'index.html', {'css_files': css_files})


def your_scss_view(request):
    scss_files = get_scss_files()
    return render(request, 'index.html', {'scss_files': scss_files})

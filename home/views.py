from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# class HomeView(TemplateView):
#     template_name = 'home/welcome.html'
#     extra_content = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = "/admin"


def home(request):
    return HttpResponse('Hello world!')


def welcome(request):
    return render(request, 'home/welcome.html', {'today': datetime.now()})


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

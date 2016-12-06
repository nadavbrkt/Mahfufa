# Create your views here.

from django.shortcuts import render

from .models import Soldier


def index(request):
    return render(request, 'soldiers/home.html')


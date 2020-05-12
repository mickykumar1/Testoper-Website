# mysite/views.py

from django.http import HttpResponse
from django.shortcuts import render


def home (request) :
    """
    The Blog homepage
    """
    return render(request, 'home.html')

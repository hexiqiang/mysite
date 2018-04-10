from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(require):
    return render(require, 'about/about.html')
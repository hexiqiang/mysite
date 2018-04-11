from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(require,id):
    return render(require, 'single/single.html')
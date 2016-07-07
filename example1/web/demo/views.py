from django.http import HttpResponse
from django.shortcuts import render

# from .models import Pizza

def home(request):
    return HttpResponse("hello from docker")

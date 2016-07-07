import socket

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    hostname = socket.gethostname()
    return HttpResponse("<h1>hostname {}</h1>".format(hostname))

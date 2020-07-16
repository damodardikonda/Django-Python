from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def india_apps(request):
    return HttpResponse('<h1> Mad in India is allowed </h1>')

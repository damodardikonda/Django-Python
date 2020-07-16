from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def boycott_china(request):
    return HttpResponse('<h1> Boycott chinese App')

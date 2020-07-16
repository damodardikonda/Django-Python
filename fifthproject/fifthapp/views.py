from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    return HttpResponse('<h1>This is First View</h1>')

def second_view(request):
    return HttpResponse('<h1>This is Srcond View</h1>')

def third_view(request):
    return HttpResponse('<h1>This is Third View</h1>')

def fourth_view(request):
    return HttpResponse('<h1>This is Fourth View</h1>')

def fifth_view(request):
    return HttpResponse('<h1>This is Fifth View</h1>')

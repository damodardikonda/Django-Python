from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def good_morning(request):
    return HttpResponse('<h1> Gooodd Morning have a nice day</h1>')


def good_afternoon(request):
    return HttpResponse('<h1>  good_afternoon have a nice day</h1>')


def good_evening(request):
    return HttpResponse('<h1> Gooodd evening have a nice day</h1>')

from django.shortcuts import render
import datetime
# Create your views here.
def abc(request):
    dt=datetime.datetime.now();
    d={
        'datess':dt,
        'name':'Damodar',
        'Phone':9876543,
        }
    return render(request,'tp/res.html',context=d)

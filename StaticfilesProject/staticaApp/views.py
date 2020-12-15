from django.shortcuts import render
import datetime
# Create your views here.

def dateandtime():

    dt=datetime.datetime.now();
    d={
       'datess':dt,
       'name':'Damodar',
       'Phone':9876543,
    }
    return render(request,'staticaApp/res.html',context=d)

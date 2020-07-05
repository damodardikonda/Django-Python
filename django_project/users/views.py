from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm # this is an predefined library for form
from django.contrib import messages
from .forms import UserRegisterationForms # it will create by us for form

# Create your views here.
def register(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST) # it will place an information of form in ..
        form=UserRegisterationForms(request.POST)
        if form.is_valid():
            form.save()# it will save automatically user
            username=form.cleaned_data.get('username')#if form is valid then get an username
            messages.success(request,f'Account created for {username}')# it will print only once.. success() is an method
            return redirect('blog-home')#after execution it will return at blog.home
    else:
            #form=UserCreationForm()# here we are creating an object of that predefined class form
            form=UserRegisterationForms()

    return render(request,'users/register.html',{'form':form})

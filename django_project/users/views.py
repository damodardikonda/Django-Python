from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm # this is an predefined library for form
from django.contrib import messages
from django.contrib.auth.decorators import login_required # it library provide functionalitywhich chek that you are logged in or not while accessing profile
from .forms import UserRegisterationForms,UserUpdateForm,ProfileUpdateForm # it will create by us for form

# Create your views here.
def register(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST) # it will place an information of form in ..
        form=UserRegisterationForms(request.POST)
        if form.is_valid():
            form.save()# it will save automatically user
            username=form.cleaned_data.get('username')#if form is valid then get an username
            messages.success(request,f'Your account is Created.. Now you are able to Login')# it will print only once.. success() is an method
            return redirect('Login')#after execution it will return at blog.home
    else:
            #form=UserCreationForm()# here we are creating an object of that predefined class form
            form=UserRegisterationForms()

    return render(request,'users/register.html',{'form':form})

# this is called as decorators
@login_required # if you are logged in then only you can access that profile page
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user);#creting an object of an user class..if you didnot passes an instance then it will created new user but it will not updte that user
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile);# creating object of an profile class

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account is updated')# it will print only once.. success() is an method
            return redirect('profile')#after execution it will return at profile
    else:
        u_form=UserUpdateForm(instance=request.user);#creting an object of an user class
        p_form=ProfileUpdateForm(instance=request.user.profile);# creating object of an profile class


# instance will give a current login user
    context={

             'u_form':u_form,
             'p_form':p_form,

             }
    return render(request, 'users/profile.html',context)

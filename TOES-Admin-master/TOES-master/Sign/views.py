from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse
# Create your views her

from requests.auth import HTTPBasicAuth
import requests
import json


AUTH_TOKEN = 'Token f5be3af7fbf162161432eea21f01cd19231d5062'

prof_username = ''
def sign_in(request):
    if request.method == 'POST':
        print("damodarrr")
        #Retriving username & password form login form template
        username = request.POST.get('username')
        password = request.POST.get('password')

        prof_username = username
        data = {
            'email': username,
            'password':  password,
        }
        # post login details to this api
        url = 'http://52.201.220.252/authapp/token/login/'
        result = requests.post(url, json=data)

        #accessing token and putting it into djoser Authorization format
        AUTH_TOKEN = 'Token {}'.format(result.json()['auth_token'])
        print(AUTH_TOKEN)
        #This Api provides User Information name , is_admin, is_superuser, email, phone etc
        user_info_api = 'http://52.201.220.252/authapp/users/me/'

        #requsting user info form api
        user_info = requests.get(user_info_api, headers={'Authorization': AUTH_TOKEN})

        #storing userinfo response in access in json format
        access = user_info.json()

        #condition so that only admin and superuser can login
        if access['is_admin'] == True or access['is_superuser']==True:
            return redirect('Home')
        else:
            message="You Don’t Have Permission To Access on this Server"
            return HttpResponse(message)
    return render(request , 'Sign/sign_in.html')


def sign_up(request):
    print(request.method)

    if request.method == 'POST':
        print("dikomhg")
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        data = {
            'is_superuser':0,
            'is_admin':1,
            'name':name,
            'username':username,
            'phone': 'NULL',
            'password':password,
            're_password':re_password,
            'email':email,
        }

        create_user_api = 'http://52.201.220.252/authapp/users/'
        requests.post(create_user_api, json=data)
        return redirect('sign_in')
    return render(request , 'Sign/sign_up.html',)


def forget_pass(request):
    return render( request , 'Sign/forget_pass.html')

def home(request):
    if request.method=='POST':
        url = 'http://52.201.220.252/authapp/token/logout/'
        result = requests.post(url, headers={'Authorization': AUTH_TOKEN})
        print(result.json())
        return redirect('sign_in')
    return render(request, 'Sign/home.html')

def register(request):
    return render(request, 'Sign/register.html')

def create_user(request):
    print(request.method)
    print("shiiiiiiiiiiiiiii")
    if request.method == 'POST':
        name = request.POST('name')
        dob = request.POST('dob')
        phone = request.POST('phone')
        gender = request.POST('gender')
        address = request.POST('address')
        username = request.POST('username')
        aadhar = request.POST('aadhar')

        data = {
            'is_superuser':0,
            'is_admin':1,
            'name':name,
            'dob':dob,
            'phone': phone,
            'gender':gender,
            'address':address,
            'username':username,
            'aadhar':aadhar,
            'smartphone':True,
        }
        print("heyyyyyy")
        print(data)
        create_user_api = 'http://52.201.220.252/users/'
        requests.post(create_user_api, json=data)
        #return redirect('phone_disp_second')
    print("chetyaa")

    return render(request ,'Sign/create_user.html')

def phone_disp_second(request):
    print(request.method)
    if request.method == 'POST':
        category1 = request.POST.get('category1')
        category1_vc = request.POST.get('category1_vc')
        category1_ex = request.POST.get('category1_ex')
        category2 = request.POST.get('category2')
        category2_vc = request.POST.get('category2_vc')
        category2_ex = request.POST.get('category2_ex')
        category3 = request.POST.get('category3')
        category3_vc = request.POST.get('category3_vc')
        category3_ex = request.POST.get('category3_ex')
        city = request.POST.get('city')
        data = {
            'city':city,
            'category1':category1,
            'category1_vc':category1_vc,
            'category1_ex':category1_ex,
            'category2': 'category2',
            'category2_vc':category2_vc,
            'category2_ex':category2_ex,
            'category3':category3,
            'category3_vc':category3_vc,
            'category3_ex':category3_ex,

        }

        create_user_api = 'http://52.201.220.252/worker/'
        requests.post(create_user_api, json=data)
        return redirect('phone_disp')

    return render( request , 'Sign/phone_disp_second.html' )

def phone_disp(request):
    url = 'http://52.201.220.252/api/withoutsmartphone/'
    response = requests.get(url , headers = {'Authorization' : AUTH_TOKEN})
    response = response.json()
    print(response)

    return render( request , 'Sign/phone_disp.html',{'response'  :response} )

def recruiters(request):

    url = 'http://52.201.220.252/job/'
    response = requests.get(url , headers = {'Authorization' : AUTH_TOKEN})
    response = response.json()
    #print(response.json())
    return render(request , 'Sign/recruiters.html', {'response' : response})

def workers(request):
    url = 'http://52.201.220.252/api/allcategories/'
    json_data={}
    '''
    Search = request.POST.get('Search')
    if search != "":
        json_data = {
             'Search' : Search
        }
        response = request.get(url , json = json_data , headers={'Authorization':AUTH_TOKEN})
        response=response.json()
    else :
    '''
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response=response.json()
    print(response)
    return render(request,'Sign/workers.html', {'response' : response})
'''
def workerpainter_contact(request):
    json_data={}
    data ={}
    data2={}
    contact = request.POST.get('contact','')
    json_data = request.GET
    print(json_data)
    data = json_data.dict()
    print(data)
    var_contact = data['contact']
    print(var_contact)
    endpoint = var_contact
    print("endpoint is "+ endpoint)

    data2 = {
       'var_contact' : var_contact
    }

    url = 'http://127.0.0.1:8000/api/specific/workerdetails/'
    response = requests.get(url+endpoint  , headers={'Authorization':AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/workerpainter.html',{'response':response})
'''
def workerpainter(request):
    '''
    json_data={}
    data ={}
    data2={}
    contact = request.POST.get('contact','')
    json_data = request.GET
    print(json_data)
    data = json_data.dict()
    print(data)
    var_contact = data['contact']
    print(var_contact)
    endpoint = var_contact
    print("endpoint is "+ endpoint)

    if contact != "":
        url = 'http://127.0.0.1:8000/api/specific/workerdetails/'
        response = requests.get(url+endpoint  , headers={'Authorization':AUTH_TOKEN})
        response=response.json()
        print(" Response is"+response)
    else :
    '''
    url = 'http://52.201.220.252/api/category/painter/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/workerpainter.html',{'response':response})


def workerplumber(request):
    '''
    json_data={}
    data ={}
    data2={}
    contact = request.POST.get('contact','')
    json_data = request.GET
    print(json_data)
    data = json_data.dict()
    print(data)

    var_contact = data['contact']
    print(var_contact)
    endpoint = var_contact
    print("endpoint is "+ endpoint)
    if contact != "":

        data2 = {
           'var_contact' : var_contact
        }

        url = 'http://127.0.0.1:8000/api/specific/workerdetails/'
        response = requests.get(url+endpoint  , headers={'Authorization':AUTH_TOKEN})
        response=response.json()
    else :
    '''
    url = 'http://52.201.220.252/api/category/plumber/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/workerplumber.html',{'response':response})



def profile(request):
    '''
    dict = {}
    url = 'http://127.0.0.1:8000/users/'
    if prof_username != "":
         dict = {'prof_username' : 'prof_username' }
         json_data = json.dumps(dict)
         response = requests.get(url  , data = dict, headers={'Authorization':AUTH_TOKEN})
         response.json()
    '''
    url = 'http://52.201.220.252/users/me/'
    response = requests.get(url , headers={'Authorization':AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/profile.html',{'response':response})

def driver(request):
    url = 'http://52.201.220.252/api/category/driver/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/driver.html',{'response':response})



def electrician(request):
    url = 'http://52.201.220.252/api/category/electrician/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/electrician.html',{'response':response})



def carpenter(request):
    url = 'http://52.201.220.252/api/category/carpenter/'
    response = requests.get(url , headers={'Authorization': AUTH_TOKEN})
    response=response.json()
    return render(request , 'Sign/carpenter.html',{'response':response})

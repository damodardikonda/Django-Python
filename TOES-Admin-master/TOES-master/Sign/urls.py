from django.urls import path , include
from . import views

urlpatterns = [


    path('', views.sign_in ,name ='sign_in'),
    path('sign_up/' , views.sign_up , name = 'sign_up'),
    path('forget_pass/', views.forget_pass , name = 'forget_pass'),
    path('home/' , views.home , name = 'Home'),
    path('register/' , views.register , name = 'register'),
    path('create_user/' , views.create_user , name = 'create_user'),
    path('phone_disp/' , views.phone_disp , name = 'phone_disp'),
    path('workers/' ,views.workers , name ='workers' ),
    path('recruiters/' ,views.recruiters , name ='recruiters' ),
    path('workerpainter/' , views.workerpainter , name = 'workerpainter'),
    #path('workerpainter/<str:contact>' , views.workerpainter_contact),
    path('workerplumber/',views.workerplumber, name='workerplumber'),
    path('profile/', views.profile , name = 'profile'),
    path('driver/',views.driver , name = 'driver'),
    path('electrician/' , views.electrician , name = 'electrician'),
    path('carpenter/' , views.carpenter , name = 'carpenter'),
    path('phone_disp_second/' , views.phone_disp_second , name='phone_disp_second')


]


from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),# we cant pass actually name of class .. we have to pass an method()
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),#1 parameter is an path name.
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    #<int:pk> shows that gives primarty key but it will always an integer not string or else..
    path('about/', views.about, name='blog-about'),
]

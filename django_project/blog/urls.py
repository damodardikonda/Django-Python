
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),# we cant pass actually name of class .. we have to pass an method()
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),#for displaying the user post with username
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),#1 parameter is an path name.
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('post/new/', PostCreateView.as_view(), name='post_create'),
    #<int:pk> shows that gives primarty key but it will always an integer not string or else..
    path('about/', views.about, name='blog-about'),
]

from django.shortcuts import render
from django.views.generic import( ListView,
                                  DetailView,
                                  CreateView,#if user want to create view
                                  UpdateView,#if user want to updat view
                                  DeleteView,#want to delete view
)#this is used for creating list and DetailView is used for taking each post detail
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin# if someone doesnt have an account
#  and he want to post an blog then it will take him to login page
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model=Post #remember we are providing an class name in to that models
    template_name='blog/home.html'#<app>/<model>_<viewType>.html
    context_object_name='posts'
    ordering=['-date_posted']# it will place latest post on the top


class PostDetailView(DetailView):# it for the dailed view for post
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']# we want that two fields .

# this is for cretingnew post through Websites

    def form_valid(self,form):         # overriding form valid() method
         form.instance.author=self.request.user           # it  sets the current user tothat instance author
         return super().form_valid(form)             # it is validating that parent form

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#UserPassesTestMixing:- it will allow only those user to chang thepost0
    model=Post
    fields=['title','content']# we want that two fields .

# this is for cretingnew post through Websites

    def form_valid(self,form):         # overriding form valid() method
         form.instance.author=self.request.user           # it  sets the current user tothat instance author
         return super().form_valid(form)             # it is validating that parent form

    def test_func(self):
        post=self.get_object() #it will get current User
        if self.request.user==p.author: #if user has its own post then oly allow to update it.
            return True
        return False #else author wont be able to update it

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):# it for the delete post
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object() #it will get current User
        if self.request.user==Post.author: #if user has its own post then oly allow to update it.
            return True
        return False #else author wont be able to update it


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

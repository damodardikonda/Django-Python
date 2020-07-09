from django.shortcuts import render
from django.views.generic import( ListView,
                                  DetailView,
                                  CreateView,#if user want to create view
)#this is used for creating list and DetailView is used for taking each post detail
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

class PostCreateView(CreateView):
    model=Post
    fields=['title','content']# we want that two fields .

# this is for cretingnew post through Websites

    def form_valid(self,form):         # overriding form valid() method
         form.instance.author=self.request.user           # it  sets the current user tothat instance author
         return super().form_valid(form)             # it is validating that parent form


class PostDetailView(DetailView):# it for the dailed view for post
    model=Post



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

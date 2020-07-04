from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)# it will add an Blog and post in admin webpage

from django.shortcuts import render
from django.urls import reverse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

# Create your views here.

#Function Views

''' def post_list(request):
    post_list = Post.objects.all()
    return render(request , 'post/list.html' , {'post_list' : post_list})
 '''

''' def post_detail(request , id):
    pass '''

#Class Based Views

class PostList(ListView):
    model = Post 


class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    pass

class PostDelete(DeleteView):
    pass
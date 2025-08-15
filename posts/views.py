from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
# Create your views here.


# Create your views here.
class PostListView(ListView):
    #template_name  attribute is to render a specific html file
    template_name="posts/list.html"
    #model is for which table we want to retrieve the data
    model=Post
    #context is a python dictionary that holds the data for the generic view
    #and this context travels to the htmls
    #by default the context name of ListView and DetailView is 
    context_object_name="posts_list"

class PostDetailView(DetailView):
    template_name="posts/detail.html"
    model=Post
    context_object_name="single_post"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model=Post
from django.shortcuts import render
from django.views.generic import ListView ,DetailView 
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["author" ,"title" ,"band_name" ,"album_name" ,"rating"]

class PostUpdateView(UpdateView):
    model = Post
    fields = ["band_name" , "album_name" , "title" ,"rating"]
    template_name = "post_edit.html"

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("home")
    template_name = "post_delete.html"
# Create your views here.

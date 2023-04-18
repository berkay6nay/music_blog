from django.shortcuts import render
from django.views.generic import ListView ,DetailView 
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title" ,"band_name" ,"album_name" ,"body" ,"rating"]
    def form_valid(self, form):
        if form.instance.author == self.request.user:
            return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["band_name" , "album_name" , "title" ,"body" , "rating"]
    template_name = "post_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("home")
    template_name = "post_delete.html"
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    
# Create your views here.

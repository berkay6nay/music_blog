from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView ,DetailView 
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Post , Profile
from django.contrib import messages

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
    
    def form_valid(self,form):
        form.instance.author = self.request.user
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

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_page.html"

    def get_context_data(self, *args, **kwargs):
        
        context = super(ProfileDetailView , self).get_context_data()
        page_user = get_object_or_404(Profile , id = self.kwargs["pk"])
        context["page_user"] = page_user
        return context
    
class EditProfilePageView(UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ["bio" , "profile_pic"]
    success_url = reverse_lazy("home")

    
# Create your views here.

from django.urls import path
from .views import BlogListView,PostCreateView,BlogDetailView,PostUpdateView,PostDeleteView,ProfileDetailView,EditProfilePageView

urlpatterns = [
    path("" , BlogListView.as_view() , name = "home"),
    path("post/new/" , PostCreateView.as_view() ,name="post_new") ,
    path("post/<int:pk>/edit" , PostUpdateView.as_view() , name= "post_edit"),
    path("post/<int:pk>/delete" , PostDeleteView.as_view() , name="post_delete"),
    path("post/<int:pk>/" , BlogDetailView.as_view() , name="post_detail"),
    path("profile/<int:pk>/" ,ProfileDetailView.as_view() , name = "profile_page"),
    path("profile/<int:pk>/edit_profile" , EditProfilePageView.as_view() , name="edit_profile_page"),
    
    ]
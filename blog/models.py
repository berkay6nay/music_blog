from django.db import models
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100,default="")
    band_name = models.CharField(max_length=50,default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL , 
                               on_delete=models.CASCADE , )
    body = RichTextField(blank=True , null=True)
    rating = models.CharField(max_length=2)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail" , kwargs={"pk" : self.pk})
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE  )
    bio = models.TextField(editable=True)
    profile_pic = models.ImageField(null=True , blank= True , upload_to="images/profile_pics" , editable=True)
    def __str__(self):
        return str(self.user)
    
# Create your models here.

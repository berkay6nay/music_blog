from django.db import models
from django.urls import reverse
from django.conf import settings
class Post(models.Model):
    title = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100,default="")
    band_name = models.CharField(max_length=50,default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL , 
                               on_delete=models.CASCADE , )
    body = models.TextField(max_length=5000)
    rating = models.CharField(max_length=2)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail" , kwargs={"pk" : self.pk})
# Create your models here.

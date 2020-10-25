from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=50)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  picture = models.ImageField(upload_to = 'pictures/', default='static/images/database_login.jpg')
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
  likes = models.ManyToManyField(get_user_model(), related_name = 'post_likes')

  def liked(self):
    return self.likes.count()

  def __str__(self):
    return self.title + '|' + str(self.author)

  def get_absolute_url(self):
    return reverse('post_detail', args = [str(self.id)])

class UserProfile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null = True)
  bio = models.TextField()
  profile_picture = models.ImageField(null = True, blank=True, upload_to='profile/')
  website_url = models.CharField(max_length=255, null=True, blank=True)
  twitter_url = models.CharField(max_length=255, null=True, blank=True)
  facebook_url = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return str(self.user)


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  comment = models.CharField(max_length=140)
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.post.comment + '|' + str(self.author)

  def get_absolute_url(self):
    return reverse('post_detail', args = [str(self.id)])
    

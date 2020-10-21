from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=50)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  picture = models.ImageField(upload_to = 'pictures/', default='static/images/database_login.jpg')
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
  likes = models.ManyToManyField(get_user_model(), related_name = 'post_likes')

  def __str__(self):
    return self.title + '|' + str(self.author)

  def get_absolute_url(self):
    return reverse('post_detail', args = [str(self.id)])
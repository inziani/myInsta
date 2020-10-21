from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'post_list.html'
  login_url = 'login'

class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post
  template_name = 'post_detail.html'
  login_url = 'login'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
  model = Post
  fields = ('title', 'body', 'picture')
  template_name = 'post_edit.html'
  login_url = 'login'

  def test_func(self):
    obj=self.get_object()
    return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('post_list')
  login_url = 'login'

  def test_func(self):
    obj=self.get_object()
    return obj.author == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView): 
  model = Post
  template_name = 'post_new.html' 
  fields = ('title', 'body','picture', )
  login_url = 'login'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)



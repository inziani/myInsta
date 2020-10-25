from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model


from .models import Post, Comment

# Create your views here.



def LikeView(request, pk):
  post = get_object_or_404(Post, id = request.POST.get('post_id'))
  
  post.likes.add(request.user)
  print(post.likes.all().count()) 
  return HttpResponseRedirect(reverse('post_list'))


class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'post_list.html'
  login_url = 'login'



class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post
  template_name = 'post_detail.html'
  login_url = 'login'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    like = get_object_or_404(Post, id=self.kwargs['pk'])
    total_likes = like.liked()
    context['total_likes'] = total_likes
    return context

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

    # =========================================

class CommentCreateView(LoginRequiredMixin, CreateView): 
  model = Comment
  template_name = 'add_comment.html' 
  fields = ('comment',)
  login_url = 'login'

  def form_valid(self, form,**kwargs):
    form.instance.author = self.request.user
    form.instance.post_id = Post.objects.get(pk=self.kwargs.get(['pk']))
    return super().form_valid(form)


# ****************************************   







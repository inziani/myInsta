from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'signup.html'

class UserEditView(UpdateView):
  form_class = CustomUserChangeForm
  success_url = reverse_lazy('home')
  template_name = 'edit_profile.html'

  def get_object(self):
    return self.request.user

from django import forms
from .models import Post, Comment

# class CommentForm(forms.ModelForm):

#   class meta:
#     model = Comment
#     fields = ('comment')
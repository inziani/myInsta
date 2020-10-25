from django.contrib import admin
from .models import Post, Comment, UserProfile


class CommentInline(admin.StackedInline):
  model = Comment

class PostAdmin(admin.ModelAdmin): 
  inlines = [ CommentInline,
]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(UserProfile)

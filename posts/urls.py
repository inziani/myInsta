from django.urls import path
from . import views


from .views import PostListView, PostUpdateView, PostDetailView, PostDeleteView, PostCreateView, LikeView, add_comment


urlpatterns = [
  path('post/<int:pk>/comment/', views.add_comment, name = 'comment'),
  path('like/<int:pk>', LikeView, name = 'like_post'),
  path('<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_edit'),
  path('<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
  path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
  path('new/', PostCreateView.as_view(), name = 'post_new'),
  path('', PostListView.as_view(), name = 'post_list'),

]
from django.urls import path


from .views import PostListView, PostUpdateView, PostDetailView, PostDeleteView, PostCreateView, LikeView, CommentCreateView


urlpatterns = [
  path('post<int:pk>/comment/', CommentCreateView.as_view(), name = 'comment'),
  path('like/<int:pk>', LikeView, name = 'like_post'),
  path('<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_edit'),
  path('<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
  path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
  path('new/', PostCreateView.as_view(), name = 'post_new'),
  path('', PostListView.as_view(), name = 'post_list'),

]
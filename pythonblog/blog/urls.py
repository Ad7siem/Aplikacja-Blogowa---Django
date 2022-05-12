from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView # post_list, post_detail, post_create, post_update, post_delete,

app_name = 'blog'
urlpatterns = [
    # path('', post_list, name = 'post_list'),
    # path('create', post_create, name='post_create'),
    # path('<slug:get_slug>', post_detail, name = 'post_detail'),
    # path('<slug:get_slug>/update', post_update, name = 'post_update'),
    # path('<slug:get_slug>/delete', post_delete, name = 'post_delete'),

    path('', PostListView.as_view(), name='post_list'),
    path('<slug:get_slug>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<slug:get_slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('<slug:get_slug>/delete', PostDeleteView.as_view(), name='post_delete'),
]
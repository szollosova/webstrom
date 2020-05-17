from django.urls import path

from post.views import PostDetailView, PostListView

app_name = 'post'

urlpatterns = [
    path('', PostDetailView.as_view(), name='post-detail-view'),
    path('post-feed/', PostListView.as_view(), name='post-list-view')
]

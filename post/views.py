from django.views.generic import DetailView, ListView


class PostDetailView(DetailView):
    template_name = 'post/post.html'


class PostListView(ListView):
    pass

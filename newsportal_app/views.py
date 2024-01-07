from django.views.generic import DetailView, ListView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'date_of_creation'
    template_name = 'news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

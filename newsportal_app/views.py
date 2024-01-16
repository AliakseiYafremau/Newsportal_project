from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group

from .forms import PostForm
from .values import news, article
from .filters import PostFilter, PostSearchFilter
from .models import Post, Author


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostSearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filtered_list"] = PostSearchFilter(self.request.GET, Post.objects.all())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('newsportal_app.add_post', )
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        product = form.save(commit='False')
        if self.request.path == '/newspaper/news/create':
            product.type = news
        elif self.request.path == '/newspaper/article/create':
            product.type = article
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('newsportal_app.change_post', )
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newsportal_app.delete_post', )
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class LoginView(LoginRequiredMixin, TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context

@login_required
def add_to_author(request):
    user = request.user
    author_group = Group.objects.get(name="authors")
    if not user.groups.filter(name="authors").exists():
        author_group.user_set.add(user)
        Author.objects.create(user=user)
    return redirect('main_page')

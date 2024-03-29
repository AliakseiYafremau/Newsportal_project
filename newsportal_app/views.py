from django.utils import timezone

import pytz
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from rest_framework import viewsets

from .forms import PostCreateForm, PostUpdateForm
from .serializers import AuthorSerializer, PostSerializer
from .values import news, article
from .filters import PostFilter, PostSearchFilter
from .models import Post, Author, Category


def redirect_to_main(request):
    return redirect('post_list')


class PostList(ListView):
    """ Представление страницы со списком всех новостей """
    model = Post
    template_name = 'views/news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = timezone.now()
        context['timezones'] = pytz.common_timezones
        context['filterset'] = self.filterset
        return context

    def post(self, request):
        request.session['django_timezone'] = request.POST.get('timezone')
        return redirect('/')


class PostSearchView(TemplateView):
    """ Представление поиска новостей """
    template_name = 'views/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filtered_list"] = PostSearchFilter(self.request.GET, Post.objects.all())
        return context


class PostDetail(DetailView):
    """ Представление новости """
    model = Post
    template_name = 'views/post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    """ Представление создания новости """
    permission_required = ('newsportal_app.add_post', )
    form_class = PostCreateForm
    model = Post
    template_name = 'views/post_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.author = Author.objects.get(user=self.request.user)

        #product = form.save(commit='False')
        #if self.request.path == '/newspaper/news/create':
        #    product.type = news
        #elif self.request.path == '/newspaper/article/create':
        #    product.type = article

        form.instance.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    """ Представление изменения новости """
    permission_required = ('newsportal_app.change_post', )
    form_class = PostUpdateForm
    model = Post
    template_name = 'views/post_update.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    """ Представление удаления новости """
    permission_required = ('newsportal_app.delete_post', )
    model = Post
    template_name = 'views/post_delete.html'
    success_url = reverse_lazy('post_list')


class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'views/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context


class CategoryListView(PostList):

    model = Post
    template_name = 'views/categories.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date_of_creation')
        self.filterset = PostFilter(self.request.GET, queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_subscriber'] = self.request.user in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def add_to_author(request):
    user = request.user
    author_group = Group.objects.get(name="authors")
    if not user.groups.filter(name="authors").exists():
        author_group.user_set.add(user)
        Author.objects.create(user=user)
    return redirect('main_page')


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = _('You are successfully subscribed')

    return render(request, 'views/subscribe.html', {'category': category, 'message': message})


@login_required()
def invalid_form(request):
    return render(request, 'views/invalid_create_form.html', {'username': request.user.username})


class CheckView(View):
    def get(self, request):
        return HttpResponse('hello')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostNewsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type='NE')
    serializer_class = PostSerializer


class PostArticlesViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type='AR')
    serializer_class = PostSerializer

from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearchView, LoginView, add_to_author, \
    CategoryListView, subscribe

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('news/create', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('article/create', PostCreate.as_view(), name='post_create'),
    path('article/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('main/', LoginView.as_view(), name='main_page'),
    path('add_to_authors/', add_to_author, name='add_to_authors'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_news_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
]

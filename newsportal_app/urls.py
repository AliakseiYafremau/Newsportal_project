from django.urls import path, include
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearchView, \
    MainPageView, add_to_author, CategoryListView, subscribe, invalid_form, CheckView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearchView.as_view(), name='post_search'),
    path('news/create', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('main/', MainPageView.as_view(), name='main_page'),
    path('add_to_authors/', add_to_author, name='add_to_authors'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_news_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('invalid_form', invalid_form, name='invalid_create_form'),
    path('check', CheckView.as_view(), name='check'),
]

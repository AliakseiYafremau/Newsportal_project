from django.urls import path, include
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearchView, \
    MainPageView, add_to_author, CategoryListView, subscribe, invalid_form,\
    CheckView, AuthorViewSet, PostNewsViewSet, PostArticlesViewSet
from rest_framework import routers


router = routers.DefaultRouter()
#router.register(r'author', AuthorViewSet)
router.register(r'news', PostNewsViewSet)
router.register(r'articles', PostArticlesViewSet)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('routers/', include(router.urls)),
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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearchView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearchView.as_view(), name='post_search'),
    path('news/create', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('article/create', PostCreate.as_view(), name='post_create'),
    path('article/<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
]
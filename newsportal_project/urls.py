"""newsportal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from newsportal_app.views import AuthorViewSet, PostNewsViewSet, PostArticlesViewSet

from newsportal_app.views import redirect_to_main

router = routers.DefaultRouter()
#router.register(r'author', AuthorViewSet)
router.register(r'news', PostNewsViewSet, basename='news')
router.register(r'articles', PostArticlesViewSet, basename='articles')

urlpatterns = [
    #path('', redirect_to_main),
    path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('newspaper/', include('newsportal_app.urls'), name='newspaper'),
    path('accounts/', include('allauth.urls')),
    path('routers/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

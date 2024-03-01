from django.contrib import admin
from .models import Author, Post, PostCategory, Comment, Category


def nullfy_rating(modeladmin, request, queryset):
    queryset.update(rating=0)

def increase_rating(modeladmin, request, queryset):
    for el in queryset:
        el.rating = el.rating + 1
        el.save()


def decrease_rating(modeladmin, request, queryset):
    for el in queryset:
        if el.rating > 0:
            el.rating = el.rating - 1
            el.save()


nullfy_rating.short_description = 'Обнулить рейтинг'
increase_rating.short_description = 'Повысить рейтинг на 1'
decrease_rating.short_description = 'Понизить рейтинг на 1'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'author', 'date_of_creation', 'rating')
    actions = [nullfy_rating, increase_rating, decrease_rating]


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)

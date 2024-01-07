from django.contrib.auth.models import User
from django.db import models
from .values import news, article, TYPE_OF_POST


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        total_rating = 0
        posts_rating = Post.objects.filter(author=self)
        comments_rating = Comment.objects.filter(user=self.user)
        posts_comment_rating = Comment.objects.filter(post__author=self)

        for post in posts_rating:
            total_rating += post.rating * 3

        for comment in comments_rating:
            total_rating += comment.rating

        for post_comment in posts_comment_rating:
            total_rating += post_comment.rating

        self.rating = total_rating


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=TYPE_OF_POST, default=news)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.text) < 125:
            return self.text
        else:
            return self.text[:125] + '...'

    def __str__(self):
        return f'{self.title}-{self.author.user.username}'


class PostCategory(models.Model):
    class Meta:
        verbose_name_plural = 'PostCategories'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

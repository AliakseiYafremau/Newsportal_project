from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0)

    #def update_rating(self):
    #    total_rating = 0
    #    total_rating +=


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255, unique=True, default='default')


news = "NE"
article = "AR"


class Post(models.Model):

    TYPE_OF_POST = [
        (news, "News"),
        (article, "Article")
    ]

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

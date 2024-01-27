from datetime import date

from django.core.exceptions import ValidationError

from .profanities import profanity_list
from django import forms
from .models import Post, Author

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()

        user = cleaned_data.get("user")
        today = date.today()
        current_post_number = Post.objects.filter(author=Author.objects.get(user=self.user),
                                                  date_of_creation__date=today).count()
        if current_post_number >= 3:
            raise ValidationError("You cannot add more than 3 posts")
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        for word in profanity_list:
            if word in title:
                raise ValidationError({
                    "title": "Title has profanities"
                })
            if word in text:
                raise ValidationError({
                    "text": "Text has profanities"
                })

        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

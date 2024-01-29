'''
py manage.py runserver
open redis-server.exe as administrator
celery -A newsportal_project worker -l INFO --pool=solo
'''
from datetime import date, timedelta

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from newsportal_app.models import Category, Post
from newsportal_project import settings


@shared_task
def send_notifications(preview, post_id, title, subscribers):
    for sub_id in subscribers:
        user = User.objects.get(id=sub_id)
        html_content = render_to_string(
            'post_created_email.html',
            {
                'text': preview,
                'title': title,
                'name': user.username,
                'link': f"{settings.SITE_URL}/newspaper/{post_id}"
            }
        )

        msg = EmailMultiAlternatives(
            subject=title,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()

        print(f'task "send notifications" for user "{user.username}" successfully done!')


@shared_task
def send_newsletter():
    for category in Category.objects.all():
        for sub in category.subscribers.all():
            content = render_to_string(
                'newsletter.html',
                {
                    'name': sub.username,
                    'posts': Post.objects.filter(date_of_creation__date__gte=(date.today()-timedelta(weeks=1)), category__name__contains=category.name),
                    'link': f"{settings.SITE_URL}/newspaper/"
                }
            )

            msg = EmailMultiAlternatives(
                subject='Newsletter',
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[sub.email],
            )

            msg.attach_alternative(content, 'text/html')
            msg.send()
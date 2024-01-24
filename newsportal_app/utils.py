from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import date, timedelta

from newsportal_app.models import Post, Category
from newsportal_project import settings


def send_notifications(preview, post_id, title, subscribers):
    for sub in subscribers:
        html_content = render_to_string(
            'post_created_email.html',
            {
                'text': preview,
                'title': title,
                'name': sub.username,
                'link': f"{settings.SITE_URL}/newspaper/{post_id}"
            }
        )

        msg = EmailMultiAlternatives(
            subject=title,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[sub.email],
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()


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
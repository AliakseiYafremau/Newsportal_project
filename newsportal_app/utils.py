from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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
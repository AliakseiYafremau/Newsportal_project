from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from newsportal_project import settings


def send_notifications(preview, post_id, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f"{settings.SITE_URL}/newspaper/{post_id}"
        }
    )
    print(subscribers)

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
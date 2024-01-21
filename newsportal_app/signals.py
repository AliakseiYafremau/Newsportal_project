from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .utils import send_notifications

from newsportal_app.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []
        for category in categories:
            subscribers = category.subscribers.all()
            subscribers_emails += [sub.email for sub in subscribers]

        send_notifications(instance.text[:50], instance.pk, instance.title, subscribers_emails)

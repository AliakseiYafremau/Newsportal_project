from django.apps import AppConfig


class NewsportalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsportal_app'

    def ready(self):
        import newsportal_app.signals

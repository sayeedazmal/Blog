from django.apps import AppConfig


class WebBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_blog'

    def ready(self) -> None:
        import web_blog.signals

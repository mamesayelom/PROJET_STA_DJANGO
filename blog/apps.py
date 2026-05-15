from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    #cette méthode s’exécute automatiquement quand Django démarre: python manage.py runserver
    def ready(self):
        #pour activer les signaux Django.
        import blog.signals

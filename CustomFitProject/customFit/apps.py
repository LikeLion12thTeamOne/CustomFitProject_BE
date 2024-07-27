from django.apps import AppConfig


class CustomfitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customFit'

    def ready(self):    #앱이 로드될 때 실행되며, signals.py 실행
        import customFit.signals
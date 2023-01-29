from django.apps import AppConfig



class MailAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_app'
    def ready(self):
        from jobs import updater
        updater.start()
        

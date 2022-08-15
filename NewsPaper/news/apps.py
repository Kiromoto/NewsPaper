from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals

        from .tasks import weekly_mails
        from .scheduler import scheduler
        print('def ready...OK! import...OK! Started!')

        scheduler.add_job(
            id='mail send',
            func=weekly_mails,
            trigger='interval',
            seconds=5,
        )

        scheduler.start()

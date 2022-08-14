from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals

        from .tasks import weekly_mails, delete_old_job_executions
        from .scheduler import appointment_scheduler
        print('A print start from APPS.py')

        appointment_scheduler.add_job(
            id='print 10 seconds',
            func=weekly_mails(),
            trigger='interval',
            seconds=5,
        )

        appointment_scheduler.add_job(id="delete_old_job_executions",
                                      func=delete_old_job_executions,
                                      trigger='interval',
                                      second=11,
                                      max_instances=1,
                                      replace_existing=True,
                                      )


        appointment_scheduler.start()

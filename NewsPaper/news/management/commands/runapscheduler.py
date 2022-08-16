import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

import time
from news.tasks import weekly_mails

logger = logging.getLogger(__name__)


# наша задача по выводу текста на экран
def my_job():
    weekly_mails()
    n_time = time.localtime()
    print(f'Print from my_job. Time: {n_time}')


# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        # scheduler.add_job(my_job,
        #                   trigger=CronTrigger(day_of_week="fri", hour="11", minute="45"), # То же, что и интервал, но задача тригера таким образом более понятна django
        #                   id="my_job",   # уникальный айди
        #                   max_instances=1,
        #                   replace_existing=True,)

        scheduler.add_job(my_job,
                          trigger=CronTrigger(second="*/20"),
                          # То же, что и интервал, но задача тригера таким образом более понятна django
                          id="my_job",  # уникальный айди
                          max_instances=1,
                          replace_existing=True, )

        logger.info("Added job 'my_job'.")

        # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
        scheduler.add_job(delete_old_job_executions,
                          trigger=CronTrigger(day_of_week="mon", hour="10", minute="00"),
                          id="delete_old_job_executions",
                          max_instances=1,
                          replace_existing=True,
                          )

        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

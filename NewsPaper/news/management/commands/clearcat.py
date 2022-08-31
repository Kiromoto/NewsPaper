from django.core.management.base import BaseCommand, CommandError
from news.models import Post, PostCategory, Category

class Command(BaseCommand):
    help = '''Удаляет все новости выбранной категории. 
    Для удаления категории введите команду: manage.py clearcat <номер категории>
    Для очистки доступны категории:
    '''
    for c in Category.objects.all():
        help += f'<{c.name} - {c.id}>' + f'\n'

    missing_args_message = 'Недостаточно аргументов для выполнения команды'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('catnumber', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.readable()
        cn = options['catnumber'][0]
        self.stdout.write(f'Вы действительно хотите удалить все новости категории - {Category.objects.get(id=cn)}? y/n: ')
        answer = input()

        if (answer == 'yes') or (answer == 'y'):
            try:
                Post.objects.filter(post_category=Category.objects.get(id=cn)).delete()
                self.stdout.write(self.style.SUCCESS(f'Succesfully delete all posts in category: {Category.objects.get(id=cn)}'))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'No one post in category {Category.objects.get(id=cn)}. Deleting was aborted!'))
        else:
            self.stdout.write(self.style.ERROR('Отмена удаления новостей категории.'))

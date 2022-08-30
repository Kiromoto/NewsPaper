from django.core.management.base import BaseCommand, CommandError
from news.models import Post, PostCategory, Category

class Command(BaseCommand):
    help = '''Удаляет все новости выбранной категории. 
    Для удаления категории введите команду: manage.py clearcat <номер категории>
    Для очистки доступны категории:
    '''
    for c in Category.objects.all():
        help += f'{c.name} - {c.id}'

    missing_args_message = 'Недостаточно аргументов для выполнения команды'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('catnumber', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.readable()

        # self.stdout.write(f'Вы действительно хотите удалить все новости категории {Category.objects.get(id=options("catnumber")).name}? y/n: ')
        print(catnumber)
        self.stdout.write(f'Вы действительно хотите удалить все новости категории {["catnumber"]}')

        # answer = input()
        #
        # if (answer == 'yes') or (answer == 'y'):
        #     post_for_del = Post.objects.filter(id=PostCategory.objects.filter(category_id=options("catnumber")))
        #
        #     for p in post_for_del:
        #         self.stdout.write(self.style.SUCCESS(f'Succesfully delete post: {p}'))
        #     return
        #
        # self.stdout.write(self.style.ERROR('Ошибка! Не удалось удалить новости выбранной категории'))




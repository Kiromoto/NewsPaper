from datetime import date, timedelta
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def weekly_mails():
    print('Print from TASKS.py every 5 seconds! weekly_mails')
    # try:
    for user_one in User.objects.all():
        print('START USER!!!START USER!!!START USER!!!START USER!!!START USER!!!START USER!!!START USER!!!START USER!!!START USER!!!START USER!!!')
        user_cat = []
        user_posts = []
        user_cat.clear()
        user_posts.clear()
        print(f'user ID = {user_one.id}')
        cat = CategorySubscriber.objects.filter(subscriber_user_id=user_one.id).values('category_name')
        print(cat)
        if cat:
            for el in cat:
                user_cat.append(el["category_name"])
        else:
            print(f'У пользователя {user_one.username} нет подписок')

        if user_one.email and user_cat:
            print(f'Пользователь: {user_one.username}. Его электронная почта: {user_one.email}')
            for cat_id in user_cat:
                cat_p = PostCategory.objects.filter(category_id=cat_id).values('post_id')
                for i in cat_p:
                    if Post.objects.get(id=i['post_id']) not in user_posts:
                        p = Post.objects.get(id=i['post_id'])
                        d = p.post_create_datetime
                        date_from = date.today()-timedelta(days=7)
                        print(f'Опубликован: {d}. Сейчас: {date.today()}. 7 дней назад: {date_from}')
                        user_posts.append(Post.objects.get(id=i['post_id']))
            print(user_posts)

            subject = f'Здравствуйте, {user_one.username}, вот самые интересные новости за прошлую неделю на NewsPaper.'

            ur = []
            for p in user_posts:
                ur.append({p: f'http://127.0.0.1:8000{p.get_absolute_url()}'})
            print(ur)

            html_content = render_to_string('send_everyweek.html', {'ur': ur, })
            msg = EmailMultiAlternatives(subject=subject,
                                         from_email='tlfordjango@mail.ru',
                                         to=[user_one.email, ],
                                         )

            msg.attach_alternative(html_content, 'text/html')
            try:
                msg.send()
            except Exception as e:
                print(f'Не удалось отправить письмо на почтовый адрес: {user_one.email}. Ошибка: {e}')
            else:
                print(f'Письмо с новостями отправлено: {user_one.email} !!!!!!')
            finally:
                ur.clear()

        else:
            print(f'У пользователя {user_one.username} не указан E-mail.')

    print('END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!END USER!!!')

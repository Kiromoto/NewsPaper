from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


def weekly_mails():
    print('Print from TASKS.py every 5 seconds! weekly_mails')
    recipient_email_list = ['kiromotossindzi@gmail.com', ]

    # try:
    for user_one in User.objects.all():
        user_cat = []
        print(f'user ID = {user_one.id}')
        cat = CategorySubscriber.objects.filter(subscriber_user_id=user_one.id).values('category_name')
        for el in cat:
            print(el)
        print(f'user_one.subscriber.all() for {user_one.username} === {cat}')
        print(f'{user_one.username} электронная почта: {user_one.email}')


        # cat = PostCategory.objects.filter(post_id=instance.id).values('category_id')
        # idcat = cat[0]["category_id"]
        # namecat = Category.objects.filter(postcategory__post_id=instance.id)
        # y1 = CategorySubscriber.objects.filter(category_name=idcat)
        # if y1:
        #     for el in y1:
        #         u = User.objects.get(id=el.subscriber_user_id)
        #         if u.email and u.email not in recipient_email_list:
        #             recipient_email_list.append(u.email)
    # except Exception:
    #     print('Ошибка получения данных о категории')
    # else:
    #     print('try is OK!')
    #     # subject = f'Опубликована новая статья в вашей любимой категории "{namecat[0].name}" на NewsPaper.'
    #     # ur = f'http://127.0.0.1:8000{instance.get_absolute_url()}'
    #     # html_content = render_to_string('post_emailsend.html', {'post': instance, 'ur': ur, })
    #     # msg = EmailMultiAlternatives(subject=subject,
    #     #                              body=instance.post_text[:20],
    #     #                              from_email='tlfordjango@mail.ru',
    #     #                              to=recipient_email_list,
    #     #                              )
    #     #
    #     # msg.attach_alternative(html_content, 'text/html')
    #     # msg.send()
    # finally:
    #     print(recipient_email_list)






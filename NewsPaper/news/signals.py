from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers
from .models import Post, Category, PostCategory, User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import request


@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    # if created:
    if PostCategory.objects.get(post_id=instance.id).category_id:
        category_name = PostCategory.objects.get(post_id=instance.id).category_id
    elif Category.objects.filter(postcategory__post_id=instance.id).exists():
        cat = Category.objects.filter(postcategory__post_id=instance.id)
        category_name = cat[0].name
    else:
        category_name = 'без категории'

    subject = f'Опубликована новая статья в вашей любимой категории "{category_name}" на NEWS.'
    ur = f'http://127.0.0.1:8000{instance.get_absolute_url()}'

    html_content = render_to_string('post_emailsend.html', {'post': instance, 'ur': ur, })

    msg = EmailMultiAlternatives(subject=subject,
                                 body=instance.post_text[:20],
                                 from_email='tlfordjango@mail.ru',
                                 to=['kiromotossindzi@gmail.com', ],
                                 )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print('______________________________________')
    print(msg)
    print('______________________________________')




from django.views.generic import ListView
from .models import Post


class ProductsList(ListView):
    model = Post
    ordering = 'post_create_datetime'
    template_name = 'news.html'
    context_object_name = 'news'
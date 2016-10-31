from django.utils import timezone
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_field__lte=timezone.now()).order_by('publish_field')
    return render(request, 'blog/post_list.html', {'posts': posts})
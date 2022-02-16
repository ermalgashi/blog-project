import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.


def all_posts(request):
    return HttpResponse("<html><body>It is now.</body></html>")


def get_post(request, id):
    posts = Posts.objects.get(pk=id)
    context = {
        "title": posts.title,
        "content": posts.content,
        "author": posts.author,
    }
    return render(request, "posts/detail_view.html", context)

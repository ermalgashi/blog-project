from django.shortcuts import render

from .models import Posts

# Create your views here.


def all_posts(request):
    posts = Posts.objects.all()
    return render(request, "posts/list_view.html", context={"posts": posts})


def get_post(request, id):
    posts = Posts.objects.get(pk=id)
    context = {
        "title": posts.title,
        "content": posts.content,
        "author": posts.author,
        "last_edited": posts.last_edited,
    }
    return render(request, "posts/detail_view.html", context)

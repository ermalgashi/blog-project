from django.shortcuts import render, redirect
from .forms import PostForm

from .models import Posts

# Create your views here.


def all_posts(request):
    posts = Posts.objects.all()
    return render(request, "posts/list_view.html", context={"posts": posts})


def get_post(request, id):
    post = Posts.objects.get(pk=id)
    context = {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "last_edited": post.last_edited,
    }
    return render(request, "posts/detail_view.html", context)


def edit_post(request, id):
    post = Posts.objects.get(pk=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("get_post", post.id)
    else:
        form = PostForm(instance=post)

    context = {"form": form}
    return render(request, "posts/edit_view.html", context=context)

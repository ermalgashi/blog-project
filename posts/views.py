from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm

from .models import Posts, Category

# Create your views here.


def all_posts(request, cat_id=None):
    posts = None
    if cat_id is not None:
        c_page = get_object_or_404(Category, id=cat_id)
        posts = Posts.objects.filter(category=c_page)
    else:
        posts = Posts.objects.all()

    return render(request, "posts/list_view.html", context={"posts": posts})


def get_post(request, cat_id, id):
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
            return redirect("get_post", post.category.id, post.id)
    else:
        form = PostForm(instance=post)

    context = {"form": form}
    return render(request, "posts/edit_view.html", context=context)

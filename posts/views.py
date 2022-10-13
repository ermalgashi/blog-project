from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, ContactForm

from .models import Posts, Category

# Create your views here.


def all_posts(request, c_slug=None):
    posts = None
    c_page = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        posts = Posts.objects.filter(category=c_page)
    else:
        posts = Posts.objects.all()

    return render(request, "posts/list_view.html", context={"posts": posts})


def get_post(request, c_slug, post_slug):
    post = Posts.objects.get(category__slug=c_slug, slug=post_slug)
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


def about_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "posts/contact_us.html", context=context)

from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("contact/", views.contact_us, name="contact_us"),
    path("<slug:c_slug>/", views.all_posts, name="get_posts_by_category"),
    path("<slug:c_slug>/<slug:post_slug>/", views.get_post, name="get_post"),
    path("<slug:post_slug>/edit", views.edit_post, name="edit_post"),
]

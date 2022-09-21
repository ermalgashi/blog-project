from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("<int:cat_id>/", views.all_posts, name="get_posts_by_category"),
    path("<int:cat_id>/<int:id>/", views.get_post, name="get_post"),
    path("<int:id>/edit", views.edit_post, name="edit_post"),
]

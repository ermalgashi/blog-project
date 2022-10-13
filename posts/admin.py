from django.contrib import admin
from .models import Posts, Category, Contact


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    readonly_fields = ("author",)
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, "author", None) is None:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "content",
    )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
